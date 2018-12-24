import json
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tasks.models import Task
from google.cloud import tasks_v2beta3


class LogTasksJob(APIView):
    client = tasks_v2beta3.CloudTasksClient()

    @classmethod
    def create_task(cls, task, payload):
        parent = cls.client.queue_path('gae-django-py37-226320', 'europe-west3', 'default')
        task = {
            'app_engine_http_request': {
                'http_method': 'POST',
                'relative_uri': f'/queues/tasks/{task.id}/log',
                'body': payload.encode()
            }
        }
        cls.client.create_task(parent, task)

    def get(self, request, format=None):
        tasks = Task.objects.all()
        for task in tasks:
            self.create_task(task, json.dumps({'name': task.name}))

        return Response(status=status.HTTP_200_OK)


class LogTaskQueue(APIView):

    def post(self, request, pk, format=None):
        logging.critical(json.loads(request.body))
        return Response(status=status.HTTP_200_OK)
