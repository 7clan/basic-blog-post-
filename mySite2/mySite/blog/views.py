from datetime import datetime
from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
from .models import tag
from django.views.generic import ListView
from django.views import View

from django.views.generic import DetailView
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/postDetails.html'  # make a template just for detail
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    
  

def tag_detail(request, slug):
    try:
        tag_instance = tag.objects.get(slug=slug)
    except tag.DoesNotExist:
        raise Http404("Tag not found")
    
    posts = tag_instance.posts.all()
    return render(request, 'blog/index.html', {
        'tag': tag_instance,
        'posts': posts
    })
def get_all_tags(request):
    tags = tag.objects.all()
    return render(request, 'blog/allPosts.html', {'all_tags': tags})
def post_comment(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        content = request.POST.get("content")
        author = request.POST.get("author")
        email = request.POST.get("email")
        Comment.objects.create(content=content, post=post, author=author, email=email)
    return redirect("post_detail", slug=post.slug)

class ReadLaterView(View):
    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug)
        if 'read_later' not in request.session:
            request.session['read_later'] = []
        if post.id not in request.session['read_later']:
            request.session['read_later'].append(post.id)
        request.session.modified = True
        return redirect("post_detail", slug=post.slug)

    def get(self, request):
        saved_ids = request.session.get('read_later', [])
        posts = BlogPost.objects.filter(id__in=saved_ids)
        return render(request, 'blog/read-later.html', {'posts': posts})

