from users.models import User
from rest_framework import status, decorators
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



@decorators.api_view(['POST'])
def RegisterView (request) : 
    try : 

        user = User.objects.create_user(
            email = request.data.get('email',None),
            password = request.data.get('password',None),
            full_name = request.data.get('full_name',None),
        )

        picture = request.data.get('picture',None)

        if picture is not None :
            user.picture = picture
        
        user.save()

        tokens = RefreshToken.for_user(user=user)

        tokens = {
            'access' : str(tokens.access_token),
            'refresh' : str(tokens)
        }

        return Response(tokens,status=status.HTTP_200_OK)
    
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)