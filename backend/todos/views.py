import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Todo


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = list(Todo.objects.values('id', 'title', 'completed', 'created_at'))
        return JsonResponse(todos, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        todo = Todo.objects.create(title=data['title'])
        return JsonResponse(
            {'id': todo.id, 'title': todo.title, 'completed': todo.completed,
             'created_at': todo.created_at.isoformat()},
            status=201,
        )


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse(
            {'id': todo.id, 'title': todo.title, 'completed': todo.completed,
             'created_at': todo.created_at.isoformat()}
        )
    elif request.method == 'PUT':
        data = json.loads(request.body)
        todo.title = data.get('title', todo.title)
        todo.completed = data.get('completed', todo.completed)
        todo.save()
        return JsonResponse(
            {'id': todo.id, 'title': todo.title, 'completed': todo.completed,
             'created_at': todo.created_at.isoformat()}
        )
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'deleted': True})
