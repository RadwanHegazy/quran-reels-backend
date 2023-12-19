from django.db import models
from quran.models import Verse
from users.models import User

class Text (models.Model) :
    verse = models.ForeignKey(Verse,related_name='verse_text',on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    font_size = models.IntegerField()

class Image (models.Model) : 
    img = models.ImageField(upload_to='story-image/')
    scale = models.FloatField(default=1)


class Reel (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    text = models.ForeignKey(Text,on_delete=models.CASCADE)
