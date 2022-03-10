from rest_framework import generics
from .models import Post
from .serializer import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ["__all__"]
    search_fields = ["__all__"]

class PostPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ["__all__"]
    search_fields = ["__all__"]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ["__all__"]
    search_fields = ["__all__"]

class PostDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostPut(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostPatch(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer