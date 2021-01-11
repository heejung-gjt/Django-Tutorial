from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')
    def __str__(self):   #클래스가 문자열로 변환되었을때 어떻게 변환할지 바꿔주는 내장함수 __str__로 username을 반환되게 변경
        return self.name

    class Meta:
        db_table='fcuser_tag' #테이블명 지정
        verbose_name='태그'
        verbose_name_plural ='태그'
