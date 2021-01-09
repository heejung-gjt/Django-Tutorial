from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=32,
                                verbose_name='Title')
    contents=models.TextField(verbose_name='Content')
    writer = models.ForeignKey('fcuser.Fcuser',on_delete=models.CASCADE, verbose_name='작성자')  # 모델을 id로 연결하는 필드를 만들어준다 fcuser에 있는 Fcuser와 연결해준다. 사용자가 삭제 한 경우 사용자의 모든 게시글을 삭제해준다
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')
    
    def __str__(self):   #클래스가 문자열로 변환되었을때 어떻게 변환할지 바꿔주는 내장함수 __str__로 username을 반환되게 변경
        return self.title

    class Meta:
        db_table='board' #테이블명 지정
        verbose_name='게시글'
        verbose_name_plural ='게시글'

    #모델을 관리할 수 있는 관리자 페이지 생성