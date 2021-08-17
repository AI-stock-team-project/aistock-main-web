from django.db import models
from django.contrib.auth.models import User
# from user.models import User


class BoardConfig(models.Model):
    """
    게시판 설정 테이블
    """
    # 외부에서 이용되는 게시판 id
    route = models.CharField(max_length=255, default='sample')
    # 게시판 구분상 이름
    name = models.CharField(max_length=255, default='sample')
    # 게시판 표시되는 이름
    display_name = models.CharField(max_length=255, default='sample')
    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 활성 여부 (기본값 true)
    is_active = models.BooleanField(default=True)
    # 삭제 여부 (기본값 false)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "board_config"
    
    def __str__(self):
        return self.name

    # Here's where to take a look
    def soft_delete(self):
        self.is_deleted = True
        self.save()
    
    def soft_restore(self):
        self.is_deleted = False
        self.save()

        
class Board(models.Model):
    """
    게시물 테이블
    """
    title = models.CharField(max_length=200, default='')
    contents = models.TextField(default='')
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    g_no = models.IntegerField(default=0)
    o_no = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(BoardConfig, on_delete=models.CASCADE)

    class Meta:
        db_table = "board_posts"


