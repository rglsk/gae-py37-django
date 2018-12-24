from tasks.models import Comment
from tasks.models import Task


def test_create_task(app):
    data = {'name': 'My milk', 'description': 'Go to Biedronka'}

    response = app.post('/tasks', data, format='json')

    assert response.status_code == 201

    tasks = Task.objects.all()

    assert len(tasks) == 1
    assert response.json()['name'] == data['name']
    assert response.json()['description'] == data['description']
    assert response.json()['status'] == tasks[0].status == tasks[0].IN_PROGRESS


def test_get_tasks_list(app):
    data = {'name': 'My milk', 'description': 'Go to Biedronka'}
    task = Task.objects.create(**data)
    comment = Comment.objects.create(text='my comment', task=task)

    response = app.get('/tasks', format='json')

    assert response.status_code == 200

    task_data = response.json()[0]
    assert task_data['name'] == task.name
    assert task_data['description'] == task.description
    assert task_data['comments'][0]['text'] == comment.text
    assert task_data['comments'][0]['id'] == comment.id
