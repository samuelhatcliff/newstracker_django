from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test_story', views.test_story, name="test story"),
    path('headlines', views.headlines_call, name='headlines')
]

