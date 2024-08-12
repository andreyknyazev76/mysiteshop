from django.db import models
from users.models import User

class Application(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата оформления заявки")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    description_address = models.CharField(max_length=600, verbose_name=" Краткое описание проблемы и адрес")
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа")

    class Meta:
        db_table = "application"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Обращение № {self.pk} | Клиент {self.user.first_name} {self.user.last_name}"
        

