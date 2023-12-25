from rest_framework import status, permissions, decorators
from rest_framework.response import Response

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def UserProfile (request) : 
    try : 
        user = request.user
        data = {
            'full_name' : user.full_name,
            'picture' : user.picture.url,
            'id' : user.id
        }

        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as error : 
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)