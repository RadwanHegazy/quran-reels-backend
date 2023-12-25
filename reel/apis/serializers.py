from rest_framework import serializers
from reel.models import Image, Text, Reel
from users.models import User
from quran.models import Verse

class VerseSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = Verse
        fields = ('text','audio',)

class UserSerializer (serializers.ModelSerializer) : 
    class Meta :
        model = User
        fields = ('full_name','picture',)

class TextSerializer (serializers.ModelSerializer) : 
    verse = VerseSerializer()
    class Meta :
        model = Text
        fields = '__all__'

class ImageSerializer (serializers.ModelSerializer) : 
    class Meta :
        model = Image
        fields = '__all__'

class ReelSerializer (serializers.ModelSerializer) : 
    image = ImageSerializer()
    text = TextSerializer()
    user = UserSerializer()
    class Meta :
        model = Reel
        fields = '__all__'


class AllReelsSerializer (serializers.ModelSerializer) : 
    user = UserSerializer()
    image = ImageSerializer()
    class Meta : 
        model = Reel
        fields = ('uuid','user','image',)