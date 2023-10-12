from django.contrib import admin
from django.urls import path
from app.views import save_user_info
from app.views import save_AI_info1
from app.views import save_AI_info2
from app.views import save_AI_info3
from app.views import defen
from app.views import users_sorted_by_chouma
from app.views import save_play_info
from app.views import save_two_play
from app.views import save_bendi_info1
from app.views import save_bendi_info2
from app.views import save_bendi_info3
from app.views import pipeiduiixang
from app.views import save_zaixian_info
from app.views import jilu

urlpatterns = [
    path("admin/", admin.site.urls),
    path('save_user_info/', save_user_info, name='save_user_info'),#保存用户信息
    path('save_AI_info1/', save_AI_info1, name='save_AI_info1'),#保存一轮AI选定区
    path('save_AI_info2/', save_AI_info2, name='save_AI_info2'),#保存二轮AI选定区
    path('save_AI_info3/', save_AI_info3, name='save_AI_info3'),#保存三轮轮AI选定区
    path('defen/', defen, name='defen'),#计算得分
    path('users_sorted_by_chouma/', users_sorted_by_chouma, name='users_sorted_by_chouma'),#将筹码按大到小顺序传给前端
    path('save_play_info/', save_play_info, name='save_play_info'),#传递倍率 选定区给数据库
    path('save_two_play/', save_two_play, name='save_two_play'),#本地两个玩家对战 传递筹码 选定区给数据库
    path('save_bendi_info1/', save_bendi_info1, name='save_bendi_info1'),#本地第一轮托管算法
    path('save_bendi_info2/', save_bendi_info2, name='save_bendi_info2'),#本地第一轮托管算法
    path('save_bendi_info3/', save_bendi_info3, name='save_bendi_info3'),#本地第一轮托管算法
    path('pipeiduiixang/', pipeiduiixang, name='pipeiduiixang'),#返回匹配的玩家
    path('save_zaixian_info/', save_zaixian_info, name='save_zaixian_info'),#返回在线匹配后的结果
    path('jilu/', jilu, name='jilu'),#返回在线匹配后的结果
    # 其他 URL 配置
]
