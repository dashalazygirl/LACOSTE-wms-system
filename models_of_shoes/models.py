from django.db import models

class Models_of_shoes(models.Model):
    select=[('муж.','Мужской'),('жен.','Женский')]
    # select_one = [('1','Ближний'),('2','Дальний')]
    articul=models.CharField(max_length=20, verbose_name="Артикул")
    model_s=models.CharField(max_length=20, verbose_name="Модель")
    color=models.CharField("Цвет", max_length=20)
    short=models.CharField( max_length=20, verbose_name="Короткий код")
    sex=models.CharField(max_length=10,default='жен.',choices=select, verbose_name="Пол")
    size_f=models.CharField(max_length=10, verbose_name="Размер USA")
    size_r=models.FloatField(verbose_name="Размер RU")
    season=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Категория',blank=True)
    amount=models.PositiveIntegerField(verbose_name="Количество")
    sclad = models.ForeignKey('Sclad',on_delete=models.CASCADE,verbose_name= "Cклад",blank=True)
    picture = models.ImageField('картинка', upload_to='models_of_shoes', blank= True)
    picture_2 = models.ImageField('Картинка (дополнительная)', upload_to='models_of_shoes', blank=True)


    def __str__(self):
        return f"{self.articul} - {self.sex}"

    class Meta :
        verbose_name="Модель кроссовок"
        verbose_name_plural="Модели кроссовок"
        ordering = ('id',)

class Arhiv(models.Model):
    select=[('муж.','Мужской'),('жен.','Женский')]
    # select_one = [('1','Ближний'),('2','Дальний')]
    articul=models.CharField(max_length=20, verbose_name="Артикул")
    model_s=models.CharField(max_length=20, verbose_name="Модель")
    color=models.CharField("Цвет", max_length=20)
    short=models.CharField( max_length=20, verbose_name="Короткий код")
    sex=models.CharField(max_length=10,default='жен.',choices=select, verbose_name="Пол")
    size_f=models.CharField(max_length=10, verbose_name="Размер FR")
    size_r=models.FloatField(verbose_name="Размер RU")
    season=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Категория')
    amount=models.PositiveIntegerField(verbose_name="Количество")
    sclad = models.ForeignKey('Sclad',on_delete=models.CASCADE,verbose_name= "Cклад")
    picture = models.ImageField('картинка', upload_to='models_of_shoes', blank= True)
    picture_2 = models.ImageField('Картинка (дополнительная)', upload_to='models_of_shoes', blank=True)

    def __str__(self):
        return f"{self.articul} - {self.sex}"

    class Meta :
        verbose_name="Архив кроссовок"
        verbose_name_plural="Архив кроссовок"
        ordering = ('id',)
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категория')
    opisanie = models.TextField(verbose_name='Описание категории')

    class Meta :
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return f"{self.name} "

class Sclad(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название склада')

    class Meta :
        verbose_name="Склад"
        verbose_name_plural="Склады"

    def __str__(self):
        return f"{self.name}"

