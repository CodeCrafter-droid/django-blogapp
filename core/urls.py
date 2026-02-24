from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:categoryid>', views.post_by_category,name='post_by_category'),
    path('blogs/<slug:slug>/',views.blogspage,name='blogspage'),
    path('blog/search/',views.search,name='search'),
    path('blog/like/<int:comment_id>/',views.toggle_comment_like,name='like')
]