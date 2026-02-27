from core.models import blog, category, comment
from rest_framework import viewsets, mixins, generics, status
from rest_framework.views import APIView, Response
from core.serializers import blogserializer, categoryserializer, commentserializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# Create your views here.
class BlogAPI(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = blogserializer
    # filterset_fields = ['status', 'is_featured', 'category']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return blog.objects.all()
        return blog.objects.filter(status=1)

class CategoryAPI(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    queryset = category.objects.all()
    serializer_class = categoryserializer

# class CommentAPI(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = comment.objects.all()
#     serializer_class = commentserializer

#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
   
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         blog_id = self.kwargs.get('pk')
#         serializer.save(
#             user=self.request.user,
#             blogg_id=blog_id
#         )

class commentapi(APIView):

    def get(self,request):
        com = comment.objects.all()
        serialized = commentserializer(com,many=True)
        print(serialized)
        print(serialized.data)
        return Response(serialized.data,status=200)
      
    
class postcomment(APIView):
    serializer_class = commentserializer

    def post(self,request,blog_pk):
        serialized = commentserializer(data=request.data)
        print(request.data)
        if serialized.is_valid():
            serialized.save(user=request.user,blogg_id=blog_pk)
            return Response(serialized.data,status=201)
        return Response(serialized.errors,status=400)
    
    def get(self,request,blog_pk):
        com = comment.objects.filter(blogg_id=blog_pk)
        serialized = commentserializer(com,many=True)
        print(serialized)
        print(serialized.data)
        return Response(serialized.data,status=200)
    

class patchdeletecomment(APIView):
    serializer_class = commentserializer
    
    def patch(self,request,com_pk):
        com = comment.objects.get(id=com_pk)
        serialized = commentserializer(com,data=request.data,partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=200)
        return Response(serialized.errors,status=400)
    
    def delete(self,request,com_pk):
        com = comment.objects.get(id=com_pk)
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        











