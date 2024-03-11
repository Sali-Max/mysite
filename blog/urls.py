from django.urls import path
from . import views
app_name="blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.list, name='list'),
    path('addpost',views.addPost,name='addpost'),
    path("post/<id>", views.postView, name="post"),
    path('server', views.serverInfo,name='serverInfo')
]