from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте вам нужно aктивирорвать ваш аккаунт',
        f'Нажмите сюда чтобы активировать ваш аккаунт: \n{full_link}',
        'joseph@gmail.com',
        [user],
        fail_silently=False
    )
