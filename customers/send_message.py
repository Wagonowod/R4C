from django.core.mail import send_mail

from R4C import settings


def send_message(instance, order):
    message = f"""Добрый день!\nНедавно вы интересовались нашим роботом модели '{instance.model}', версии '{instance.version}'.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
    mail_to = order.customer.email
    send_mail(
        'Заказ робота',
        message,
        settings.EMAIL_HOST_USER,
        [mail_to],
        fail_silently=False
    )
