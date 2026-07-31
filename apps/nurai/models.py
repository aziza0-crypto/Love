from django.db import models


class Student(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )

    age = models.IntegerField(
        verbose_name="Возраст"
    )

    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )

    email = models.EmailField(
        verbose_name="Email"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )


    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


    def __str__(self):
        return self.name



class Application(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон"
    )

    email = models.EmailField(
        verbose_name="Email"
    )

    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий"
    )

    agree = models.BooleanField(
        default=False,
        verbose_name="Согласие"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата заявки"
    )


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


    def __str__(self):
        return self.name