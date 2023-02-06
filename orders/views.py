from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.send_message import send_message

from robots.models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def robot_created(sender, instance, **kwargs):
    try:
        order = Order.objects.filter(robot_serial=instance.serial).select_related('customer').get()
        if order:
            send_message(instance, order)
    except Order.DoesNotExist:
        print('Такого заказа не существует')
    except:
        print('Не удалось отправить письмо')
