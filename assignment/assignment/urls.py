from django.conf.urls import patterns, include, url
from django.contrib import admin
from my_social_network import views
from my_social_network import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', include('my_social_network.urls')),
    url(r'^users/(?P<username>\w+)/followers$', views.display_user_follower,name="followers"),
    url(r'^users/(?P<username>\w+)/following$', views.display_user_following,name="following"),
)
