from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Order
from customers.models import Customer
from robots.models import Robot



@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        robot_serial = data.get("robot_serial")

        # Проверяем, был ли передан email и serial
        if not email or not robot_serial:
            return JsonResponse({"error": "Email или серийный номер не переданы"}, status=400)

        # Находим клиента по email, если не найден — создаем нового
        customer, created = Customer.objects.get_or_create(email=email)

        # Проверяем наличие робота

        robot_count = Robot.objects.filter(serial=robot_serial).count()
        if robot_count > 0:
            # Если робот существует, создаем заказ
            order = Order.objects.create(customer=customer, robot_serial=robot_serial, status='completed')
            return JsonResponse({"message": f"Заказ успешно создан. Робот '{robot_serial}' в наличии. Всего в наличии {robot_count}", "order_id": order.id})

        else:
            # Если робота нет, создаем заказ с ожиданием
            order = Order.objects.create(customer=customer, robot_serial=robot_serial, status='waiting')
            return JsonResponse({"message": f"Заказ создан, но робота '{robot_serial}' нет в наличии. Мы сообщим Вам о поступлении", "order_id": order.id})

    return JsonResponse({"error": "Неправильный метод запроса"}, status=400)
