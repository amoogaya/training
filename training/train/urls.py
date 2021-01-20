from django.conf.urls import url
from . import views

app_name = 'train'

urlpatterns = [
    url(r'^index/$', views.index_view, name='index'),
    url(r'^addrequest/$', views.add_request, name='add_request'),

]