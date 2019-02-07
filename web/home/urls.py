from django.urls import path
from django.views.generic import RedirectView

from home import views

urlpatterns = [
    path('about/', views.Front.as_view(), name='about'),
    path('', RedirectView.as_view(pattern_name='about'), name='home'),
]
