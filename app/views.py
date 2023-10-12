# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import UserSerializer
#
#
# # views.py
# from rest_framework import viewsets
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# from django.http import JsonResponse
#
# def save_user_info(request):
#     # if request.method == 'POST':
#         nickname = request.POST.get('nickname')  # 获取用户昵称
#         response_data = {'nickname':nickname}  # 将昵称封装到一个字典
#         return JsonResponse(response_data)
import json
import copy
import time
from datetime import datetime
from .models import User
from django.db.models import F, Func

def save_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        nickname = data.get('nickname')
        # chou = data.get('chouma')

        # 查询name为"AI"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name=nickname)
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
        # 创建一个User对象，并将nickname赋值给name字段
            user.name=nickname
        # user = User(name=nickname, chouma=chouma)
        user.save()
        response_data = {'chouma': user.chouma} #要封装成字典
        return JsonResponse(response_data)

# AI
# 全局变量
arr_xuan=[0]
fflag = 0
# 第一轮
# 判断是否有连续数字
def has_consecutive_numbers(arr):
    arr=sorted(arr)  # 对数组进行排序

    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 1:
            return True

    return False

# 将连续数字取出放进arr_xuan
def find_consecutive_numbers(arr):
    arr.sort()  # 对数组进行排序

    consecutive_arr = []
    current_sequence = [arr[0]]  # 存放当前连续数字序列的列表

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            current_sequence.append(arr[i])
        else:
            if len(current_sequence) > 1:
                consecutive_arr.extend(current_sequence)
            current_sequence = [arr[i]]

    if len(current_sequence) > 1:
        consecutive_arr.extend(current_sequence)

    return list(set(consecutive_arr))

# 判断是否有相同的数字
def has_duplicate_numbers(arr):
    # 使用集合(set)存储数组中的数字
    num_set = set()

    for num in arr:
        # 如果数字已经在集合中，则表示存在重复数字
        if num in num_set:
            return True

        # 将数字添加到集合中
        num_set.add(num)

    # 遍历完成后，没有发现重复数字
    return False

# 取出重复数字放进arr_xuan
def find_duplicate_numbers(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    duplicate_numbers = []
    for num, count in count_dict.items():
        if count > 1:
            duplicate_numbers.append((num, count))

    max_count = 0
    for num, count in duplicate_numbers:
        if count > max_count:
            max_count = count

    arr_xuan = []
    for num, count in duplicate_numbers:
        if count == max_count:
            arr_xuan.extend([num] * count)

    return duplicate_numbers, arr_xuan

def save_AI_info1(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data = data.get('RobotTou')
        length = len(data)
        arr_tou = copy.copy(data)

        # print(arr_tou)

        if has_consecutive_numbers(arr_tou) == True:
            arr_xuan = find_consecutive_numbers(arr_tou)
            fflag = 1
        elif has_duplicate_numbers(arr_tou) == True:
            result, arr_xuan = find_duplicate_numbers(arr_tou)
            fflag = 2
        # 排除一些特殊情况
        if fflag == 1 and len(arr_xuan) < 3 and has_duplicate_numbers(arr_tou) == True:
            result, arr_xuan = find_duplicate_numbers(arr_tou)
            fflag = 2
        if arr_xuan == [1, 2, 3, 5, 6]:
            arr_xuan = [1, 2, 3]
            fflag = 1
        # print('第一轮选定区:', arr_xuan)


        # 查询name为"AI"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="AI")
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            user.chouma = 10000
            user.xuan1, user.xuan2, user.xuan3, user.xuan4, user.xuan5 = 0, 0, 0, 0, 0

            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()

            length = len(arr_xuan)
            for i in range(length):
                globals()[f'xuan{i + 1}'] = arr_xuan[i]
            my_dict = {i: arr_xuan[i] for i in range(length)}
        time.sleep(1)  # 延迟1秒
        response_data = my_dict  # 要封装成字典
        return JsonResponse(response_data)

# AI 第二轮
# 判断增加一个数字是否会更连续
def longest_consecutive_length(arr):
    # 创建一个集合来存储数组中的数字
    num_set = set(arr)
    max_length = 0

    # 遍历数组中的每个数字
    for num in arr:
        # 如果当前数字的前一个数字不在集合中，则当前数字是一个连续序列的开始
        if num - 1 not in num_set:
            current_length = 1
            # 增加当前数字的后续连续数字的长度
            while num + 1 in num_set:
                num += 1
                current_length += 1
            # 更新最大长度
            max_length = max(max_length, current_length)

    return max_length

def save_AI_info2(request):
    user, created = User.objects.get_or_create(name="AI")
    arr_xuan = [user.xuan1, user.xuan2, user.xuan3, user.xuan4, user.xuan5]
    arr_xuan = [x for x in arr_xuan if x != 0]
    print(arr_xuan,'22222')
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data = data.get('RobotTou')
        arr_tou = copy.copy(data)
        # 如果正常的话这些不需要
        arr_tou=[5]
        # arr_xuan=[1,2,3]
        fflag=1
        my_dict = {}

        if fflag == 1:  # 连续：小顺子大顺子
            for elem in arr_tou:
                if elem in arr_xuan:
                    continue
                else:
                    previous_length = longest_consecutive_length(arr_xuan)
                    arr_xuan.append(elem)
                    current_length = longest_consecutive_length(arr_xuan)
                    if current_length > previous_length:
                        arr_xuan = sorted(arr_xuan)
                    else:
                        arr_xuan.remove(elem)

        else:  # 重复
            if (has_duplicate_numbers(arr_tou) == False):  # 新生成的投掷区没有重复值
                arr_xuan_unique = list(set(arr_xuan))
                arr_xuan_unique = sorted(arr_xuan_unique, reverse=True)
                # print(arr_xuan_unique)
                for elem in arr_xuan_unique:
                    if elem in arr_tou:
                        arr_xuan.append(elem)
                        if (len(arr_xuan) == 5):
                            break
            else:  # 新生成的投掷区有重复值
                result, arr = find_duplicate_numbers(arr_tou)
                arr_xuan.extend(arr)
        arr_xuan = [x for x in arr_xuan if x != 0]
        print('第二轮选定区:', arr_xuan)

        # 查询name为"AI"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="AI")
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            # user.chouma = 22222
            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()

            length = len(arr_xuan)

            for i in range(length):
                globals()[f'xuan{i + 1}'] = arr_xuan[i]
        my_dict = {i: arr_xuan[i] for i in range(length)}
        time.sleep(1)  # 延迟1秒
        response_data = my_dict  # 要封装成字典
        return JsonResponse(response_data)

def save_AI_info3(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data = data.get('RobotTou')
        arr_tou = copy.copy(data)
        # 查询name为"AI"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="AI")
        arr_xuan = [user.xuan1, user.xuan2, user.xuan3, user.xuan4, user.xuan5]
        arr_xuan = [x for x in arr_xuan if x != 0]
        arr_xuan.extend(arr_tou)
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            # user.chouma = 33333
            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()
        length = len(arr_xuan)
        for i in range(length):
            globals()[f'xuan{i + 1}'] = arr_xuan[i]
        my_dict = {i: arr_xuan[i] for i in range(length)}
        time.sleep(1)  # 延迟1秒
        response_data = my_dict  # 要封装成字典
        return JsonResponse(response_data)

##计算得分
# 判断双对
def check_shuangdui(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    num_twice = 0
    for count in counts.values():
        if count == 2:
            num_twice += 1

    return num_twice == 2
# 判断三连
def check_sanlian(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    num_count_3 = None
    other_nums = []
    for num, count in counts.items():
        if count == 3:
            num_count_3 = num
        else:
            other_nums.append(num)

    if num_count_3 is not None and len(other_nums) == 2:
        return True

    return False
# 判断葫芦
def check_hulu(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    num_count_3 = None
    num_count_2 = None
    for num, count in counts.items():
        if count == 3:
            num_count_3 = num
        elif count == 2:
            num_count_2 = num

    if num_count_3 is not None and num_count_2 is not None:
        return True

    return False
# 判断四连
def check_silian(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for count in counts.values():
        if count == 4:
            return True

    return False
# 判断五连
def check_wulian(arr):
    first_num = arr[0]
    for num in arr:
        if num != first_num:
            return False
    return True
# 判断小顺子
def check_xiaoshunzi(arr):
    arr.sort()  # 先对数组进行从小到大排序

    for i in range(len(arr) - 3):
        if arr[i] + 1 == arr[i + 1] and arr[i + 1] + 1 == arr[i + 2] and arr[i + 2] + 1 == arr[i + 3]:
            return True

    return False
# 判断大顺子
def check_dashunzi(arr):
    arr.sort()  # 先对数组进行从小到大排序

    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return False

    return True

# 数组求和
def sum_array(arr):
    total = sum(arr)
    return total

#计算得分
def defen(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        nickname = data.get('nickname')
        user, created = User.objects.get_or_create(name=nickname)
        arr_xuan = [user.xuan1, user.xuan2, user.xuan3, user.xuan4, user.xuan5]
        flag = 0
        if check_shuangdui(arr_xuan) == True:
            flag = 10
        if check_sanlian(arr_xuan) == True:
            flag = 10
        if check_hulu(arr_xuan) == True:
            flag = 20
        if check_silian(arr_xuan) == True:
            flag = 40
        if check_wulian(arr_xuan) == True:
            flag = 100
        if check_xiaoshunzi(arr_xuan) == True:
            flag = 30
        if check_dashunzi(arr_xuan) == True:
            flag = 60
        total = sum_array(arr_xuan) + flag
        user.chouma = 55555
        user.save()
        response_data = {'nickname': nickname,'得分':total}  # 要封装成字典
        return JsonResponse(response_data)

def get_users_sorted_by_chouma():
    sorted_users = User.objects.order_by('-chouma')  # 按照 chouma 字段降序排列
    return sorted_users
#传给前端排行榜的数据
from django.http import JsonResponse

def users_sorted_by_chouma(request):
    if request.method == 'POST':
        sorted_users = get_users_sorted_by_chouma()
        data = [
            {'name': user.name, 'chouma': user.chouma}
            for user in sorted_users
        ]
        return JsonResponse(data, safe=False)

#不需要request的计算得分
def defen2(arr):
    flag = 0
    if check_shuangdui(arr) == True:
        flag = 10
    if check_sanlian(arr) == True:
        flag = 10
    if check_hulu(arr) == True:
        flag = 20
    if check_silian(arr) == True:
        flag = 40
    if check_wulian(arr) == True:
        flag = 100
    if check_xiaoshunzi(arr) == True:
        flag = 30
    if check_dashunzi(arr) == True:
        flag = 60
    total = sum_array(arr) + flag
    return total

# AI 和玩家的结算界面
def save_play_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        xuandingquyu = data.get('PeoTou')
        beishu = data.get('beiCount')
        monCount2 = data.get('monCount2')
        # print(xuandingquyu,'玩家')
        # user, created = User.objects.get_or_create(name=nickname)
        # user.chouma = chouma
        # user.save()
        # 查询name为"d hr"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="d hr")
        # 如果已存在该用户，则修改chouma字段的值
        if not created:# 已存在 没有新创造
            user.chouma = monCount2
            for i in range(len(xuandingquyu)):
                if i == 0:
                    user.xuan1 = xuandingquyu[i]
                elif i == 1:
                    user.xuan2 = xuandingquyu[i]
                elif i == 2:
                    user.xuan3 = xuandingquyu[i]
                elif i == 3:
                    user.xuan4 = xuandingquyu[i]
                elif i == 4:
                    user.xuan5 = xuandingquyu[i]
            user.save()
        # response_data = {'PeoTou':xuandingquyu,'beihsu':beishu,'monCount2':monCount2}  # 要封装成字典
        # 返回AI 和玩家 的得分和筹码
        play_defen=defen2(xuandingquyu)
        ai_user = User.objects.get(name="AI")
        AI_defen=defen2([ai_user.xuan1, ai_user.xuan2, ai_user.xuan3, ai_user.xuan4, ai_user.xuan5])
        m=(9+beishu)*abs(play_defen-AI_defen)
        if play_defen > AI_defen:# 玩家赢
            user = User.objects.get(name="d hr")
            user.chouma += m
            user.lishijilu += f"赢了 {ai_user.name} {m}筹码,"
            user.time = user.time+','+str(datetime.now())
            user.save()

            ai_user = User.objects.get(name="AI")
            ai_user.chouma -= m
            ai_user.lishijilu += f"输给 {user.name} {m}筹码,"
            ai_user.time = ai_user.time+','+str(datetime.now())
            ai_user.save()
        else: #AI赢
            user = User.objects.get(name="d hr")
            user.chouma -= m
            user.lishijilu += f"输给 {ai_user.name} {m}筹码,"
            user.time = user.time+','+str(datetime.now())
            user.save()

            ai_user = User.objects.get(name="AI")
            ai_user.chouma += m
            ai_user.lishijilu += f"赢了 {user.name} {m}筹码,"
            ai_user.time = ai_user.time+','+str(datetime.now())
            ai_user.save()
        response_data={'玩家得分':play_defen,'AI得分':AI_defen,'玩家筹码':User.objects.get(name="d hr").chouma,'AI筹码':User.objects.get(name="AI").chouma}
        # response_data = {'message':'筹码传递成功'}  # 要封装成字典
        return JsonResponse(response_data)

# 本地两个玩家结算界面
def save_two_play(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        wanjia1_xuan = data.get('wanjia1')
        wanjia2_xuan = data.get('wanjia2')
        wanjia1_chouma = data.get('Peo1Mon')
        wanjia2_chouma = data.get('Peo2Mon')
        zongBei = data.get('zongBei')
        # print(type(wanjia1_chouma))
        # 计算AI 和玩家 的得分和筹码
        wanjia1_defen=defen2(wanjia1_xuan)
        wanjia2_defen=defen2(wanjia2_xuan)
        m=abs(wanjia2_defen-wanjia1_defen)*zongBei
        if wanjia1_defen > wanjia2_defen:
            wanjia1_chouma = int(wanjia1_chouma) - m
            wanjia2_chouma = int(wanjia2_chouma) + m
        else:
            wanjia1_chouma = int(wanjia1_chouma) - m
            wanjia2_chouma = int(wanjia2_chouma) + m
        response_data={'玩家1得分':wanjia1_defen,'玩家2得分':wanjia2_defen,'玩家1筹码':wanjia1_chouma,'玩家2筹码':wanjia2_chouma}
        # response_data = {'message':'筹码传递成功'}  # 要封装成字典
        return JsonResponse(response_data)

# 一轮托管
def save_bendi_info1(request):
    my_dict={}
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data = data.get('RobotTou')
        length = len(data)
        arr_tou = copy.copy(data)

        if has_consecutive_numbers(arr_tou) == True:
            arr_xuan = find_consecutive_numbers(arr_tou)
            fflag = 1
        elif has_duplicate_numbers(arr_tou) == True:
            result, arr_xuan = find_duplicate_numbers(arr_tou)
            fflag = 2
        # 排除一些特殊情况
        if fflag == 1 and len(arr_xuan) < 3 and has_duplicate_numbers(arr_tou) == True:
            result, arr_xuan = find_duplicate_numbers(arr_tou)
            fflag = 2
        if arr_xuan == [1, 2, 3, 5, 6]:
            arr_xuan = [1, 2, 3]
            fflag = 1

        # 查询name为"wanjia1"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="wanjia1")
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            user.chouma = 11111
            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()

            length = len(arr_xuan)
            for i in range(length):
                globals()[f'xuan{i + 1}'] = arr_xuan[i]
            my_dict = {i: arr_xuan[i] for i in range(length)}
        response_data = my_dict  # 要封装成字典
        return JsonResponse(response_data)
# 二轮托管
def save_bendi_info2(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data1 = data.get('RobotTou')
        arr_tou = copy.copy(data1)
        data2 = data.get('RobotSelect')
        arr_xuan = copy.copy(data2)

        if has_consecutive_numbers(arr_xuan)==True: # 连续：小顺子大顺子
            for elem in arr_tou:
                if elem in arr_xuan:
                    continue
                else:
                    previous_length = longest_consecutive_length(arr_xuan)
                    arr_xuan.append(elem)
                    current_length = longest_consecutive_length(arr_xuan)
                    if current_length > previous_length:
                        arr_xuan = sorted(arr_xuan)
                    else:
                        arr_xuan.remove(elem)

        else:  # 重复
            if (has_duplicate_numbers(arr_tou) == False):  # 新生成的投掷区没有重复值
                arr_xuan_unique = list(set(arr_xuan))
                arr_xuan_unique = sorted(arr_xuan_unique, reverse=True)
                # print(arr_xuan_unique)
                for elem in arr_xuan_unique:
                    if elem in arr_tou:
                        arr_xuan.append(elem)
                        if (len(arr_xuan) == 5):
                            break
            else:  # 新生成的投掷区有重复值
                result, arr = find_duplicate_numbers(arr_tou)
                arr_xuan.extend(arr)
        arr_xuan = [x for x in arr_xuan if x != 0]
        print('第二轮选定区:', arr_xuan)

        # 查询name为"wanjia1"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="wanjia1")
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            # user.chouma = 2222235
            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()

        length = len(arr_xuan)

        for i in range(length):
            globals()[f'xuan{i + 1}'] = arr_xuan[i]
        my_dict = {i: arr_xuan[i] for i in range(length)}
        print(my_dict)
        # 要封装成字典
        response_data = my_dict
        return JsonResponse(response_data)

# 三轮托管
def save_bendi_info3(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data1 = data.get('RobotTou')
        arr_tou = copy.copy(data1)
        data2 = data.get('RobotSelect')
        arr_xuan = copy.copy(data2)
        arr_xuan.extend(arr_tou)
        # 将选定区存进数据库里
        # 查询name为"wanjia1"的用户，如果不存在则创建新用户
        user, created = User.objects.get_or_create(name="wanjia1")
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:
            # user.chouma = 222224
            for i in range(len(arr_xuan)):
                if i == 0:
                    user.xuan1 = arr_xuan[i]
                elif i == 1:
                    user.xuan2 = arr_xuan[i]
                elif i == 2:
                    user.xuan3 = arr_xuan[i]
                elif i == 3:
                    user.xuan4 = arr_xuan[i]
                elif i == 4:
                    user.xuan5 = arr_xuan[i]
            user.save()
        length = len(arr_xuan)

        for i in range(length):
            globals()[f'xuan{i + 1}'] = arr_xuan[i]
        my_dict = {i: arr_xuan[i] for i in range(length)}
        response_data = my_dict  # 要封装成字典
        return JsonResponse(response_data)

# 返回筹码数最接近的用户 返回匹配到的玩家的筹码和昵称 前端给我传
def pipeiduiixang(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data1 = data.get('nickname')#玩家二昵称
        data2 = data.get('monCount')#玩家二筹码
        user = User.objects.exclude(name=data1).exclude(name='wanjia1').order_by(Func(F('chouma') - int(data2), function='ABS')).first()
        response_data = {'nickname': user.name, '筹码': user.chouma}
        return JsonResponse(response_data)

def save_zaixian_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        play1_xuandingquyu = data.get('play1_xuandingquyu')
        play1_nickname = data.get('play1_nickname')
        play1_chouma = data.get('play1_chouma')
        play2_xuandingquyu = data.get('play2_xuandingquyu')
        play2_nickname = data.get('play2_nickna')
        play2_chouma = data.get('play2_chouma')
        zongbeilv=data.get('zongbeilv')
        # print(xuandingquyu,'玩家')
        # user, created = User.objects.get_or_create(name=nickname)
        # user.chouma = chouma
        # user.save()
        # 查询玩家一的用户，如果不存在则创建新用户
        play1, created = User.objects.get_or_create(name=play1_nickname)
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:  # 已存在 没有新创造
            for i in range(len(play1_xuandingquyu)):
                if i == 0:
                    play1.xuan1 = play1_xuandingquyu[i]
                elif i == 1:
                    play1.xuan2 = play1_xuandingquyu[i]
                elif i == 2:
                    play1.xuan3 = play1_xuandingquyu[i]
                elif i == 3:
                    play1.xuan4 = play1_xuandingquyu[i]
                elif i == 4:
                    play1.xuan5 = play1_xuandingquyu[i]
            play1.save()
        # 查询玩家二的用户，如果不存在则创建新用户
        play2, created = User.objects.get_or_create(name=play2_nickname)
        # 如果已存在该用户，则修改chouma字段的值为1000
        if not created:  # 已存在 没有新创造
            for i in range(len(play2_xuandingquyu)):
                if i == 0:
                    play2.xuan1 = play2_xuandingquyu[i]
                elif i == 1:
                    play2.xuan2 = play2_xuandingquyu[i]
                elif i == 2:
                    play2.xuan3 = play2_xuandingquyu[i]
                elif i == 3:
                    play2.xuan4 = play2_xuandingquyu[i]
                elif i == 4:
                    play2.xuan5 = play2_xuandingquyu[i]
            play1.save()
        # 返回AI 和玩家 的得分和筹码
        play1_defen = defen2(play1_xuandingquyu)
        play2_defen = defen2(play2_xuandingquyu)
        m = (9 + zongbeilv) * abs(play1_defen - play2_defen)
        if play1_defen > play2_defen:# 玩家一赢
            play1 = User.objects.get(name=play1_nickname)
            play1.chouma += m
            play1_chouma += m
            play1.lishijilu += f"赢了 {play2_nickname} {m}筹码,"
            play1.time = play1.time+','+str(datetime.now())
            play1.save()

            play2_user = User.objects.get(name=play2_nickname)
            play2_user.chouma -= m
            play2_chouma = -m
            play2.lishijilu += f"输给 {play1_nickname} {m}筹码,"
            play2.time = play2.time+','+str(datetime.now())
            play2.save()
        else:# 玩家二赢
            play1 = User.objects.get(name=play1_nickname)
            play1.chouma -= m
            play1.lishijilu += f"输给 {play2_nickname} {m}筹码,"
            play1.time = play1.time+','+str(datetime.now())
            play1.save()

            play2 = User.objects.get(name=play2_nickname)
            play2.chouma += m
            play2.lishijilu += f"赢了 {play1_nickname} {m}筹码,"
            play2.time = play2.time+','+str(datetime.now())
            play2.save()
        time.sleep(2)  # 延迟2秒
        response_data = {'玩家1昵称': play1_nickname, '玩家2昵称': play2_nickname,
                         '玩家1得分': play1_defen, '玩家2得分': play2_defen,
                         '玩家1筹码': play1.chouma,
                         '玩家2筹码': play2.chouma}
        # response_data = {'message':'筹码传递成功'}  # 要封装成字典
        return JsonResponse(response_data)

def jilu(request):#返回游戏记录给前端
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data1 = data.get('nickname')#玩家昵称
        print(data1,'11111')
        user = User.objects.get(name=data1)
        response_data = {'历史记录':user.lishijilu,'时间':user.time}
        return JsonResponse(response_data)
