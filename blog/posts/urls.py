from django.urls import path
from .views import PostList, PostDetail, PostDelete, PostPut, PostPatch, PostPost

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('delete/<int:pk>',PostDelete.as_view()),
    path('put/<int:pk>',PostPut.as_view()),
    path('patch/<int:pk>',PostPatch.as_view()),
    path('post/',PostPost.as_view()),

]