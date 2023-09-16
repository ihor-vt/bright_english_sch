from django.utils.translation import gettext_lazy as _


def contact_form_message(
        formatted_datetime, name, email, mobile_phone, description):
    message = _(f"""
    Дата і час: {formatted_datetime},
    Ім'я: {name}
    Пошта: {email}
    Телефон: {mobile_phone}
    Примітка: {description}
    """)
    return message


def sumscribe_welcome_message(customer_email):
    message = _(f"""
    Вітаємо {customer_email},

    Дякуємо, що приєдналися до інформаційної розсилки Bright Language School! Ми раді вітати вас в нашій спільноті і ділитися з вами останніми новинами, оновленнями та особливими пропозиціями.

    Що ви можете очікувати від нас:
    - Щомісячний лист з цікавими статтями та корисними порадами з вивчення мов.
    - Оголошення про наші акції, знижки та спеціальні пропозиції.
    - Важливі повідомлення та оновлення від Bright Language School.

    Ми завжди працюємо над тим, щоб надавати вам якісний контент та послуги. Ваша підтримка дуже важлива для нас.

    Якщо у вас є які-небудь питання або пропозиції, будь ласка, не соромтеся зв'язатися з нами. Ми завжди готові слухати вас!

    Дякуємо ще раз за вашу підписку. Ми сподіваємося, що наші матеріали будуть корисні та надихнуть вас.

    З найкращими побажаннями,
    Команда Bright Language School
    """)
    return message
