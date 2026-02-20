from django.db import models
from django.utils import timezone
from django.urls import reverse

#0 Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img= models.ImageField(upload_to='blog_images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts',null=True, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-created_at']

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']       
class tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    posts = models.ManyToManyField(BlogPost, related_name='tags', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', args=[self.slug])  # Make sure you have this route in urls.py

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['name']
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']