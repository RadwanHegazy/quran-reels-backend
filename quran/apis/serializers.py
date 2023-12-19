from rest_framework import serializers
from quran.models import Surah, Verse


class SurahSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = Surah
        fields = "__all__"

class VerseSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = Verse
        fields = "__all__"
