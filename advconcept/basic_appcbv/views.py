from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.http import HttpResponse
from . import models

# from below you will be provided with a list of records in this model.
class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

# the ListView we are inheriting is doing the work of creating the context dictionary.It takes the model you called i.e. school and _list.
# School_list, by  default list view will return context name as model_name_list and detail view return as model_name by you can also assign by yourself.
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_appcbv/school_detail.html'
    # by using template_name this point out to the template

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    
class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    


# # This is template view with CBV
class IndexView(TemplateView):
    template_name = 'index.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = "BASIC INJECTION"
#         return context
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
    