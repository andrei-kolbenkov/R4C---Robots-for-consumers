from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from robots.models import Robot
from django.conf import settings

@receiver(post_save, sender=Robot)
def check_order_for_robot(sender, instance, created, **kwargs):
    """
    Этот сигнал срабатывает после создания нового робота.
    Если на данного робота уже существует заказ, то уведомляем.
    """
    if created:
        # Проверяем, есть ли заказ на этого робота
        orders = Order.objects.filter(robot_serial=instance.serial)

        if orders.exists():
            # Если заказ существует, например, можно изменить статус заказа или уведомить клиента
            for order in orders:
                order.status = 'completed'
                order.save()
                # Отправляем уведомление пользователю. Сообщение будет выведено в консоль
                send_email_to_customer(order.customer.email, order.robot_serial)
                print(f"Заказ №{order.id} робота {instance.serial} снова доступен.")



def send_email_to_customer(email, robot_serial):
    subject = f"Робот {robot_serial} теперь в наличии"
    message = f"""
    Добрый день!

    Недавно вы интересовались нашим роботом модели {robot_serial}.
    Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.

    Спасибо за ваш интерес!
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Отправитель
        [email],  # Получатель
        fail_silently=False,
    )
