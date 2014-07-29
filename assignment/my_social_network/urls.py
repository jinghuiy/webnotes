from django.conf.urls import patterns, include, url
from my_social_network import views

urlpatterns=patterns('',
    url(r'^$',views.online_users,name="online_users"),
             
                     
)