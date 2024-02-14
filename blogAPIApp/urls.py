from django.urls import path
from . import views
urlpatterns=[
path('', views.index),
path('get_all_posts/', views.GetAllPosts),
path('create_new_post/', views.CreatePost),
path('delete_post/', views.DeletePost),
path('get_post/', views.GetPost),
path('update_post/', views.UpdatePost),
]