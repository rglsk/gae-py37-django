from rest_framework import serializers
from tasks.models import Comment
from tasks.models import Task


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'created')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'comments')

    comments = CommentSerializer(many=True, read_only=True)
