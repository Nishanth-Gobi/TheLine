from django.urls import path
from .views import HomeView, BlogpostDetailView, NewBlogpost, UpdateBlogpost, DeleteBlogpost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogpost/<int:pk>', BlogpostDetailView.as_view(), name='blogpost-detailed'),
    path('new_blogpost/', NewBlogpost.as_view(), name='new-blogpost'),
    path('blogpost/edit/<int:pk>', UpdateBlogpost.as_view(), name='edit-blogpost'),
    path('blogpost/delete/<int:pk>', DeleteBlogpost.as_view(), name='delete-blogpost'),
]
