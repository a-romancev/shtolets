from django.urls import path

from gallery import views

urlpatterns = [
    path('', views.Gallery.as_view(), name='gallery'),
]
