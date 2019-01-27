from django.urls import path

from home import views

urlpatterns = [
    path('', views.Front.as_view(), name='front'),
]
