from django.db import models
from django.conf import settings

class Vacancies(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100)
    workExperience = models.CharField(verbose_name="Опыт работы", max_length=50)
    salary = models.CharField(verbose_name="Зарплата",max_length=30)
    requirements = models.CharField(verbose_name="Требования",max_length=300)
    responsibilities = models.CharField(verbose_name="Обязанности",max_length=200)
    conditions = models.CharField(verbose_name="Условия",max_length=200)
    def __str__(self):
        return self.title 
    
    
# class File(models.Model):
#     name = models.CharField(max_length=40)
#     text = models.CharField(max_length=40)
#     file = models.FileField(upload_to="docx/", null=True,unique=True)
#     def __str__(self):
#         return self.text
    

MEDIA_CHOICES = (
    ('instagram','INSTAGRAM'),
    ('site', 'SITE'),
    ('youtube','YOUTUBE'),
    ('vkontakte','VKONTAKTE'),
    ('magazine','MAGAZINE'),
)

class MassMedia(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=40)
    link = models.TextField(verbose_name="Ссылка",null=True,unique=True, blank = True)
    text = models.CharField(verbose_name="Краткий текст",max_length=100)
    date = models.DateField(verbose_name="Дата публикации",) 
    media = models.CharField(verbose_name="Вид медии",max_length=9, choices=MEDIA_CHOICES, default='site')
    file = models.FileField(verbose_name="Путь к файлу",upload_to="docx/", null=True, blank = True)

    def __str__(self):
        return self.title
    


class pdfCart(models.Model):
    title = models.CharField(verbose_name="Реквизиты",max_length=80,unique=True, blank = True)
    file = models.FileField(verbose_name="Путь к реквизитам",upload_to="media/docx/", null=True, blank = True)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(verbose_name="Наименование",max_length=80,unique=True, blank = True)

    def __str__(self):
        return self.title