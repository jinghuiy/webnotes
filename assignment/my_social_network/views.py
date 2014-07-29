from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader


from my_social_network.models import UserLink
from django.contrib.auth.models import User

def online_users(request):
  users = User.objects.all()
  return render_to_response("my_social_network/online_users.html", {
      'users': users,
    })

def display_user_following(request,username):
  userlinks = UserLink.objects.all()
  following_links = userlinks.filter(to_user__username=username)
  return render_to_response("my_social_network/username.html", {
    'username': username,
    'following_links':following_links,
    })
  
def display_user_follower(request,username):
  userlinks = UserLink.objects.all()
  follower_links = userlinks.filter(from_user__username=username)
  return render_to_response("my_social_network/username1.html", {
    'username': username,
    'follower_links':follower_links,
    })