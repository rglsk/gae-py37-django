from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin


from tasks.serializers import TaskSerializer
from tasks.models import Task


class TaskView(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super(TaskView, self).list(request, *args, **kwargs)


class CommentView(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super(CommentView, self).list(request, *args, **kwargs)
