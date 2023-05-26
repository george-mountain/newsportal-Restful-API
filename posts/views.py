"""
-------------------------------------------------------
Using Generic views for the views.

In this case, we will write a single view for each object

For example, for user view, we will two views which are:
UserList view and UserDetail view.

The same is applicable to posts etc.
-------------------------------------------------------

using viewsets
"""

# from django.contrib.auth import get_user_model  # new
# from rest_framework import generics, permissions  # new

# from .models import Post
# from .permissions import IsAuthorOrReadOnly  # new
# from .serializers import PostSerializer, UserSerializer  # new


# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAdminUser,)  # new
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


"""
------------------------------------
Using Viewset for the views.

In this case, we just combine the related views

into one view. For example, all user views are 
related and all post views are related.

Instead of having these vies as separate views, we can combine them

using viewsets
"""

from django.contrib.auth import get_user_model
from rest_framework import viewsets  # new
from rest_framework.permissions import IsAdminUser  # new

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    permission_classes = [IsAdminUser]  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
