from rest_framework import status, decorators
from rest_framework.response import Response
from quran.models import Surah, Verse
from quran.apis.serializers import VerseSerializer

@decorators.api_view(['GET'])
def GetSurahVerses (request, surah_id) : 
    try : 

        try : 
            surah = Surah.objects.get(id=surah_id)
        except Surah.DoesNotExist : 
            return Response({
                'message' : 'model not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        query = Verse.objects.filter(surah=surah)
        serializer = VerseSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    except Exception as error : 
        return Response({
            'message' f"an error accured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)