from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/<str:pk>', views.post, name="post"),
    path('postdelete/<str:pk>', views.postdelete, name='postdelete'),
    path('postupdate/<str:pk>', views.updatepost, name='postupdate'),
]