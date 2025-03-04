from django.urls  import path
from .views import get_users,create_user,user_detail,get_posts,ExempleRoute

urlpatterns=[
    path('users/',get_users,name="get_user"),
    path('users/create',create_user,name="create_user"),
    path('users/<int:pk>',user_detail,name="user_detail"),
    path('posts/',get_posts,name="user_posts"),
    path('liste/',ExempleRoute.as_view())
]