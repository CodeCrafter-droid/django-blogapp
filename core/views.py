from django.shortcuts import render,redirect,get_object_or_404
from .models import category, blog, comment
from django.db.models import Q
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    blogs = blog.objects.filter(status=1)

    context ={
        'blogs':blogs,
    }
    return render(request,'home.html',context)

def post_by_category(request, categoryid):
    posts = blog.objects.filter(status = 1,category=categoryid)
    cat = get_object_or_404(category,pk=categoryid)
    print(request.user)
    # for i in posts:
    #     print(i.category)
    context ={
        'posts':posts,
        'cat':cat,
    }
    
    return render(request,'post_by_category.html',context)

def blogspage(request,slug):
    post = blog.objects.get(slug=slug,status=1)
    comments = comment.objects.filter(blogg=post)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
            if form.is_valid():
                    comments = form.save(commit=False)  
                    comments.user = request.user         
                    comments.blogg = post                
                    comments.save()
                    return redirect('blogspage',slug=post.slug)
    
    context ={
        'post':post,
        'comments':comments,
        'form':form,
    }

    return render(request,'blogspage.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)
    context = {
        'posts' : blogs,
        'keyword' : keyword
    }

    return render(request,'search.html',context)

@require_POST
@login_required
def toggle_comment_like(request, comment_id):
    commentt = get_object_or_404(comment, id=comment_id)

    if commentt.likes.filter(id=request.user.id).exists():
        commentt.likes.remove(request.user)  # Unlike
    else:
        commentt.likes.add(request.user)     # Like

    return redirect(request.META.get('HTTP_REFERER', '/'))

            



