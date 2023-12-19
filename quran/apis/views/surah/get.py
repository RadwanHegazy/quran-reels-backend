from rest_framework import status, decorators
from rest_framework.response import Response
from quran.models import Surah
from quran.apis.serializers import SurahSerializer

@decorators.api_view(['GET'])
def GetSurah (request) : 
    try : 
        query = Surah.objects.all()
        serializer = SurahSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    except Exception as error : 
        return Response({
            'message' f"an error accured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)