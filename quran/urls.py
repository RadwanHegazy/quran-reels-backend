from django.urls import path
from quran.apis.views.surah import get as get_surah
from quran.apis.views.verse import get as get_verse, retreive 


urlpatterns = [
    path('surah/',get_surah.GetSurah),
    path('surah/<int:surah_id>/',get_verse.GetSurahVerses),
    path('verse/<int:verse_id>/',retreive.GetSurahVersesDetails),
]
