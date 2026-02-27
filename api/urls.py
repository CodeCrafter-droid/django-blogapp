from rest_framework.routers import DefaultRouter
from .views import BlogAPI, CategoryAPI, commentapi, postcomment, patchdeletecomment
from django.urls import path
router =  DefaultRouter()
router.register(r'blog',BlogAPI)
router.register(r'category',CategoryAPI)


urlpatterns = [
   #  path('comment/',CommentAPI.as_view()),
   #  path('comment/<int:pk>/',CommentAPI.as_view()),
   path('comment/',commentapi.as_view()),
   path('comment/<int:blog_pk>',postcomment.as_view()),
   path('comment/patch/<int:com_pk>',patchdeletecomment.as_view())
]+router.urls
