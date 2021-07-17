# coding: utf-8
"""
 @Topic:

 @Date: 2021-07-17

 @Author: lette.xiao

 @Copyright（C）: 2014-2021 X-Financial Inc. All rights reserved.
"""
from apps.mock.models import ViewerIp
import datetime


def tag_user_ip(request, location):
    if 'HTTP_X_FORWARDED_FOR' in request.META:        # 获取用户真实IP地址
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']
    print("访问者IP：", user_ip)
    print("访问位置：", location)
    obj = ViewerIp.objects.filter(user_ip=user_ip, location=location).last()
    if obj:
        ViewerIp.objects.create(user_ip=user_ip,
                                location=location,
                                create_time=datetime.datetime.now(),
                                views_count=obj.views_count + 1)
    else:
        ViewerIp.objects.create(user_ip=user_ip,
                                location=location,
                                create_time=datetime.datetime.now(),
                                views_count=1)

