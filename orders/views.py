from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


from robots.models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def robot_created(sender, instance, **kwargs):
    mail_from = 'devtest.tst@yandex.ru'
    order = Order.objects.filter(robot_serial=instance.serial).select_related('customer').get()
    message = f"""Добрый день!\nНедавно вы интересовались нашим роботом модели '{instance.model}', версии '{instance.version}'.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
    mail_to = order.customer.email
    if order:
        send_mail(
            'Заказ робота',
            message,
            mail_from,
            [mail_to],
            fail_silently=False
        )
