from django.db import models


class Surah (models.Model) : 
    name = models.CharField(max_length=100)

    def __str__(self) : 
        return f'{self.name}'
    

class Verse (models.Model) : 
    surah = models.ForeignKey(Surah,on_delete=models.CASCADE)
    text = models.TextField()
    audio = models.CharField(max_length=1000)

    def __str__(self) : 
        return f'{self.text}, {self.surah}'
    