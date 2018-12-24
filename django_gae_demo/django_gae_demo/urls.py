from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from tasks.views import TaskView
from tasks.queues import LogTasksJob
from tasks.queues import LogTaskQueue

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tasks', TaskView)


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'cron/tasks/log', LogTasksJob.as_view()),
    url(r'^queues/tasks/(?P<pk>\d+)/log$', LogTaskQueue.as_view()),
    url(r'^', include(router.urls))
]
