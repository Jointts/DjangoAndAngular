from django.conf.urls import *
from rest_framework import routers
from ToDoList import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, 'post-list')

urlpatterns = patterns('',
                       url(r'posts', 'ToDoList.views.index'),
                       )
