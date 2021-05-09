from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# this is a class based view(CBV).
# rather than calling the index.html file give a basic http response
class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")

# Create your views here.
# # below is a function based view file
# def index(request):
#     return render(request,'index.html')
    