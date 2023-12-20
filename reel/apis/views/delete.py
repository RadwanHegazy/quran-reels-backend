from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from reel.apis.serializers import ReelSerializer
from reel.models import Reel



@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAuthenticated])
def DeleteReel (request, reel_uuid) : 
    try : 
        user = request.user

        try : 
            reel = Reel.objects.get(uuid=reel_uuid)
        except Reel.DoesNotExist :
            return Response({
                "message" : 'reel not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        if user != reel.user :
            return Response({
                'message': "you don't have permissions to delete this reel"
            },status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
        reel.delete()
        return Response(status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)