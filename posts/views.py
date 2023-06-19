from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


# =========================================== function View =========================================== #
def post_list(request):
    data = Post.objects.all()
    return render(request, 'posts.html', {'posts': data})


def post_detail(request, id_post):
    data = Post.objects.get(id=id_post)
    return render(request, 'post.html', {'post': data})


def add_post(request):
    pass


def edit_post(request):
    pass


def delete_post(request):
    pass


# =========================================== Class View =========================================== #
class PostList(generic.ListView):
    model = Post


class PostDetail(generic.DetailView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = ['title', 'content', 'publish', 'image', 'tags']
    success_url = '/blog/'


class PostUpdate(generic.UpdateView):
    model = Post
    fields = ['title', 'content', 'publish', 'image', 'tags']
    success_url = '/blog/'
    template_name = 'posts/post_edit.html'


class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/blog/'
