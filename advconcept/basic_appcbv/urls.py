from django.conf.urls import url
from basic_appcbv import views

app_name = 'basic_appcbv'
# the above name should be same as provided in the base.html or base file having navbar list using templates 
# i.e., href="{% url 'basic_appcbv:list' % }" this list is the name we provided below.
urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(), name='list'),
    # url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update')
]

# the reason for giving the name ='list' is for url template tag.
# d in the above regular expression means digit plus.
# it is taking primary key of the school as the display.
