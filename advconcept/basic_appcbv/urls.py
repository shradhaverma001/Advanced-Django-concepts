from django.conf.urls import url
from basic_appcbv import views

app_name = 'basic_appcbv'
# the above name should be same as provided in the base.html or base file having navbar list using templates 
# i.e., href="{% url 'basic_appcbv:list' % }" this list is the name we provided below.
urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(), name='list')

]

# the reason for giving the name ='list' is for url template tag.