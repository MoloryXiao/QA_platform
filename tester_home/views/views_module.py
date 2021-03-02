from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 登录态装饰器
from tester_home.models.module import Module


@login_required
def module_manage(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["modules"] = Module.objects.all()
    return render(request, "module_manage.html", rtn_dict)

