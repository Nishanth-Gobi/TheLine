from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blogpost
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Blogpost
    template_name = 'home.html'
    ordering = ['-pub_date']


class BlogpostDetailView(DetailView):
    model = Blogpost
    template_name = 'blogpost.html'


class NewBlogpost(CreateView):
    model = Blogpost
    form_class = PostForm
    template_name = 'new_blogpost.html'


class UpdateBlogpost(UpdateView):
    model = Blogpost
    form_class = EditForm
    template_name = 'edit_blogpost.html'


class DeleteBlogpost(DeleteView):
    model = Blogpost
    # template_name = 'delete.html'
    success_url = reverse_lazy('home')
