from django import forms
from core.models import category, blog
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User, Group


class AddCategory(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter category'
        })

class AddPost(forms.ModelForm):
    class Meta:
        model = blog 
        fields = ('title','category','blog_body','featured_image','short_description','status','is_featured')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Title'
        })
        
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter category'
        })
        
        self.fields['blog_body'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter blog here'
        })
        
        self.fields['short_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter a short description'
        })


class AddUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "groups", "user_permissions", "is_superuser", "is_staff", "is_active"]

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)

        if not current_user.is_superuser:
            self.fields.pop("is_superuser")
            self.fields.pop("user_permissions")
            self.fields["groups"].queryset = Group.objects.filter(name="Editor")

        for field in self.fields.values():
         field.widget.attrs.update({
            'class': 'form-control'
        })

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "groups", "user_permissions", "is_superuser", "is_staff", "is_active"]

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)

        if not current_user.is_superuser:
            self.fields.pop("is_superuser")
            self.fields.pop("user_permissions")
            self.fields["groups"].queryset = Group.objects.filter(name="Editor")

        for field in self.fields.values():
         field.widget.attrs.update({
            'class': 'form-control'
        })
         
class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"
