from django.db.models.signals import post_save
from django.dispatch import receiver

from robots.models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def robot_created(sender, instance, **kwargs):
    order = Order.objects.filter(robot_serial=instance.serial)
    message = f"""Добрый день!\nНедавно вы интересовались нашим роботом модели '{instance.model}', версии '{instance.version}'.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
    if order:
        print(message)
