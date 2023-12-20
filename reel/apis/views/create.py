from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from reel.apis.serializers import ReelSerializer, TextSerializer, ImageSerializer, UserSerializer
from reel.models import Text, Verse, Reel, Image


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateReel (request) : 
    try : 
        
        # Text model
        verse_id = request.data.get('verse')
        verse_id = int(verse_id)
        
        try :
            verse = Verse.objects.get(id=verse_id)
        except Verse.DoesNotExist : 
            return Response({'message':"verse not found"},status=status.HTTP_404_NOT_FOUND)
        
        x = request.data.get('x')
        y = request.data.get('y')
        font_size = request.data.get('font_size')

        text = Text.objects.create(
            verse = verse,
            x = x,
            y = y,
            font_size = font_size,
        )

        text.save()

        # Image Model
        img = request.data.get('img')
        scale = float(request.data.get('scale'))

        image = Image.objects.create(
            img = img,
            scale = scale
        )

        image.save()


        # Reel Model

        reel = Reel.objects.create(
            user = request.user,
            image = image,
            text = text
        )

        reel.save()

        serializer = ReelSerializer(reel)

        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    except Exception as error :
        return Response({
            'message' f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)