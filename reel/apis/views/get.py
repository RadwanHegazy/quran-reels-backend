from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from reel.apis.serializers import AllReelsSerializer
from reel.models import Reel



@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def GetReels (request) : 
    try : 
        query = Reel.objects.order_by('-date')
        serializer = AllReelsSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message':f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)