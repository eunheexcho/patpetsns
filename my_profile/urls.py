from django.urls import path, re_path
from my_profile import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('post_new/', views.post_new, name='post_new'),
]