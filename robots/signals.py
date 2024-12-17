from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Robot

@receiver(pre_save, sender=Robot)
def generate_serial(sender, instance, **kwargs):
    # Формируем поле serial как "model-version". Выполняется только при запросе на создание робота через API
    if not instance.serial:  # Только если serial ещё не задано
        instance.serial = f"{instance.model}-{instance.version}"