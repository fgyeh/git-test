from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='出版日期')
    is_delete = models.BooleanField(default=False)
    # 书和出版社是一对多
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)
    # 书和作者是多对多
    authors = models.ManyToManyField('Author')


class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社名')
    addr = models.CharField(max_length=32, verbose_name='出版社地址')
    is_delete = models.BooleanField(default=False)


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='作者年龄')
    email = models.EmailField(verbose_name='邮箱')
    is_delete = models.BooleanField(default=False)
    # 一对一
    author_detail = models.OneToOneField('AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField(verbose_name='手机号')
    addr = models.CharField(max_length=32, verbose_name='作者地址')
    is_delete = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他')
    )
    gender = models.IntegerField(choices=gender_choices, null=True)

    score_choices = (
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '及格'),
        ('D', '不及格'),
    )
    # 只需要保证字段类型和列举出来的元祖第一个数据类型一致即可
    score = models.CharField(choices=score_choices, max_length=1, null=True)