"""
------------------------------
USING GENERIC URLS

In using the generic urls, we will have a url for each end point of our project.

Every endpoint of the api, will have a separate url.

-----------------------------------
"""


# from django.urls import path
# from .views import PostList, PostDetail, UserList, UserDetail  # new


# urlpatterns = [
#     path("users/", UserList.as_view()),  # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]


"""
------------------------------
USING ROUTER FOR URLS

Routers work directly with viewsets to automatically generate URL patterns
for us. 

We will use SimpleRouter but it’s also possible to create
custom routers for more advanced functionality

-----------------------------------
"""


from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import UserViewSet, PostViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")


urlpatterns = router.urls
