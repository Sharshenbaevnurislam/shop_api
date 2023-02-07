from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте вам нужно aктивирорвать ваш аккаунт',
        f'Нажмите сюда чтобы а  ктивировать ваш аккаунт: \n{full_link}',
        'joseph@gmail.com',
        [user],
        fail_silently=False
    )


def send_reset_email(user):
    code = user.activation_code
    email = user.email
    send_mail("Letter with password reset code", f"Your reset code {code}", 'from@exapmle.com', [email, ], fail_silently=False)


def send_notification(user_email, order_id, price):
    send_mail(
        'Уведомление о создании заказа!',
        f'''Вы создали заказ №{order_id}, ожидайте звонка!
        Полная стоимость вашего заказа: {price}.
        Спасибо что выбрали нас!''',
        'from@exmple.com',
        [user_email], fail_silently=False
    )
