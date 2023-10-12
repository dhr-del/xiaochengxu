from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    chouma = models.IntegerField(default=1000)
    xuan1 = models.IntegerField(default=0)
    xuan2 = models.IntegerField(default=0)
    xuan3 = models.IntegerField(default=0)
    xuan4 = models.IntegerField(default=0)
    xuan5 = models.IntegerField(default=0)
    lishijilu = models.TextField(default='')
    pipeizhuangtai = models.IntegerField(default=0)#默认没有处于匹配状态
    time = models.CharField(max_length=100)
    class Meta:
        app_label = 'app'
        db_table = 'app_users'