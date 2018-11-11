from django.views import generic
from django.shortcuts import render


class Index(generic.View):
    def get(self, request):
        return render(request, 'home/index.html')
