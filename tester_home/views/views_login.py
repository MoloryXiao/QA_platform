from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import auth     # 登录验证模块
from django.contrib.auth.decorators import login_required   # 登录态装饰器


def login(request):
    if request.method == "GET":
        return render(request,"index.html")
    else:
        name = request.POST.get("username", "")
        password = request.POST.get("password", "")
        verify_res = auth.authenticate(username=name,password=password)
        print(verify_res)
        if verify_res is not None:
            # return render(request, "mock_manage.html", {"username": name})
            auth.login(request, verify_res) # 记录用户登录态
            request.session["username"] = name
            return HttpResponseRedirect("/mock_manage/")
        else:
            return render(request, "index.html", {"fail_reason": "用户名或密码错误！"})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


def relogin(request):
    return HttpResponseRedirect("/login/")