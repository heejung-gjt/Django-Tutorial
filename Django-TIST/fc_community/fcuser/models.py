from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password=models.CharField(max_length=64,
                                verbose_name='비밀번호')
    useremail = models.EmailField(max_length=128,
                                    verbose_name='사용자 이메일')
    
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')
    def __str__(self):   #클래스가 문자열로 변환되었을때 어떻게 변환할지 바꿔주는 내장함수 __str__로 username을 반환되게 변경
        return self.username

    class Meta:
        db_table='fcuser_fcuser' #테이블명 지정
        verbose_name='사용자'
        verbose_name_plural ='사용자'

    #모델을 관리할 수 있는 관리자 페이지 생성