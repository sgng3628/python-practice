from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards', blank=True)
    #related_name 이 없다고 하면, user.board_set.all()를 사용해야함
    # 1:n 의 관계에서 user.board_set.all() 도 똑같이 사용해야함. 이둘의 겹침을 방지하기 위해서 related_name 을 설정해줌
    
    def __str__(self):
        return f'글 번호-> {self.id}, 제목->{self.title}, 내용->{self.content}'