from django.shortcuts import render, redirect, get_object_or_404
from core.models import category, blog
from .forms import AddCategory, AddPost, AddUser, EditUser, ChangePassword
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.


def dashboard(request):
    cat_count = category.objects.all().count()
    blog_count = blog.objects.all().count()
    context = {
        'cat_count' : cat_count,
        'blog_count' : blog_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    form = AddCategory()
    if request.method == "POST":
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
        return redirect('categories')
    return render(request,'dashboard/add_category.html',{'form':form})

@require_POST
def delete_category(request,pk):
    get_object_or_404(category,pk=pk).delete()
    return redirect('categories')

def edit_category(request, pk):
    categoryy = get_object_or_404(category,pk=pk)

    if request.method == "POST":
        form = AddCategory(request.POST, instance=categoryy)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = AddCategory(instance=categoryy)

    return render(request, 'dashboard/edit_category.html', {'form': form, 'cat':categoryy})

def post(request):
    posts = blog.objects.all()
    
    return render(request,'dashboard/post.html',{'posts':posts})


def add_post(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            x =  form.save(commit=False)  # return the model object that is created
            x.author = request.user
            x.save()
            base_slug = slugify(x.title)     #x.slug = "-".join(x.title.split())
            slug = base_slug
            counter = 1
            while type(x).objects.filter(slug=slug).exclude(pk=x.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            x.slug = slug
            x.save()
            return redirect('posts')
    return render(request,'dashboard/add_post.html',{'form':form})
        
@require_POST
def delete_category(request,pk):
    get_object_or_404(blog,pk=pk).delete()
    return redirect('posts')

def edit_post(request, pk):
    post = get_object_or_404(blog,pk=pk)

    if request.method == "POST":
        form = AddPost(request.POST, instance=post)
        if form.is_valid():
            x =  form.save(commit=False)  # return the model object that is created
            base_slug = slugify(x.title)     #x.slug = "-".join(x.title.split())
            slug = base_slug
            counter = 1
            while type(x).objects.filter(slug=slug).exclude(pk=x.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            x.slug = slug
            x.save()
            return redirect('posts')
    else:
        form = AddPost(instance=post)

    return render(request, 'dashboard/edit_post.html', {'form': form, 'post':post})


def users(request):
    who = request.user
    current_user = User.objects.filter(id=request.user.id)
    if not who.is_superuser:
        user = User.objects.filter(is_superuser=False)
    else:
        user =  User.objects.all()
    return render(request,'dashboard/user.html',{'users':user})    

def add_user(request):
    form = AddUser(request.POST or None, current_user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users')   
    return render(request,'dashboard/add_user.html',{'form':form})

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)

    if request.method == "POST":
        form = EditUser(request.POST, instance=user, current_user = request.user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUser(instance=user, current_user = request.user)

    return render(request, 'dashboard/edit_user.html', {'form': form, 'user':user})

@require_POST
def delete_user(request,pk):
        get_object_or_404(User,pk=pk).delete()
        return redirect('users')

def change_password(request):
    if request.method == "POST":
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # prevents logout
            messages.success(request, "Your password was successfully updated!")
            return redirect("change_password")
    else:
        form = ChangePassword(request.user)

    return render(request, "dashboard/change_password.html", {"form": form})

