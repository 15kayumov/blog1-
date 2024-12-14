from .models import Post,Post2
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
class HomeListViev(ListView):
    model=Post
    template_name='home.html'

class AbautListViev(ListView):
    model=Post2
    template_name='abaut.html'

class Post_detail(DetailView):
    model=Post
    template_name='post_detail.html'

class Abaut_detail(DetailView):
    model=Post2 
    template_name='abaut_detail.html'
class signup(ListView):
    template_name="signup.html"
class login(ListView):
    template_name="login.html"
class PostCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','img','text','number']
class HomeDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
class AbautDeleteView(DeleteView):
    model=Post2
    template_name='abaut_delete.html'
    success_url=reverse_lazy('abaut')
class PostUpdetView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','img','text','number']