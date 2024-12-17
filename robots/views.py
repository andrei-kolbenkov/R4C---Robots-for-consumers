from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RobotForm
import json

@csrf_exempt  # Отключение проверки CSRF (только для API)
def create_robot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Считываем JSON из тела запроса
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        form = RobotForm(data)
        if form.is_valid():
            robot = form.save()
            return JsonResponse({
                'id': robot.id,
                'model': robot.model,
                'version': robot.version,
                'created': robot.created
            }, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
