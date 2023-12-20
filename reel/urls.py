from django.urls import path
from .apis.views import get, create, retreive, delete


urlpatterns = [
    path('get/',get.GetReels),
    path('create/',create.CreateReel),
    path('delete/<str:reel_uuid>/',delete.DeleteReel),
    path('retrive/<str:reel_uuid>/',retreive.RetreiveReel),
]