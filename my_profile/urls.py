from django.urls import path, re_path
from my_profile import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('post_new/', views.post_new, name='post_new'),
    # re_path(r'^(?P<post_pk>\d+)/comment/create/$', views.comment_create, name='comment_create'),
    path('comment/new/', views.comment_new, name='comment_new'),
]