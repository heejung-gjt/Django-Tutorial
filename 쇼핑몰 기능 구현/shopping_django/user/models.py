from django.db import models

# Create your models here.

class User(models.Model): # models에 Model을 상속받는다
    email = models.EmailField(verbose_name='이메일')
    pwd = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'