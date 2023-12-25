from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from reel.apis.serializers import ReelSerializer
from reel.models import Reel



@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def RetreiveReel (request, reel_uuid) : 
    try : 

        try : 
            reel = Reel.objects.get(uuid=reel_uuid)
        except Reel.DoesNotExist :
            return Response({
                "message" : 'reel not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = ReelSerializer(reel)

        return Response(serializer.data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)