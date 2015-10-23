from django.shortcuts import render_to_response
from ToDoList.models import Post
from ToDoList.serializers import PostSerializer
from ToDoList.permissions import permissions
from rest_framework import viewsets
from django.template import RequestContext


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint for listing posts"""
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        if 'id' in self.kwargs:
            idnr = self.kwargs['id']
            return Post.objects.filter(id=idnr).all()
        return Post.objects.all()


def index(request):
    return render_to_response('posts.html', RequestContext(request))
