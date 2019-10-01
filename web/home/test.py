from django.views import generic
from django.shortcuts import render


class Testfront(generic.View):
    def get(self, request):
        return render(request, 'home/test.html')
    def post(self, request):
        return render(request, 'home/test.html')