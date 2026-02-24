from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class blog(models.Model):
    status_choices = [
        (0,'Draft'),
        (1,'Published'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True,blank=True)
    blog_body = models.TextField(max_length=2000)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    status = models.IntegerField(choices=status_choices,default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class sociallinks(models.Model):
    platform = models.CharField(max_length=25)
    links = models.URLField(max_length=100)

    def __str__(self):
        return self.platform
    
class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogg = models.ForeignKey(blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    likes = models.ManyToManyField(
        User,
        related_name="liked_comments",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    