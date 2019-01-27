from django.views import generic
from django.shortcuts import render


class Front(generic.View):
    def get(self, request):
        return render(request, 'home/front.html')
