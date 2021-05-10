from django.shortcuts import render
from django.views.generic import View, TemplateView
# from django.http import HttpResponse

# This is template view with CBV
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "BASIC INJECTION"
        return context
# if the index.html file is in different folder under templates folder then template_name = 'folder_name/index.html'

# # this is a class based view(CBV).
# # rather than calling the index.html file give a basic http response
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

# Create your views here.
# # below is a function based view file
# def index(request):
#     return render(request,'index.html')
    