from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 登录态装饰器
from tester_home.models.mock import MockConfig


@login_required
def mock_manage(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["mock_configs"] = MockConfig.objects.all()
    return render(request, "mock_manage.html", {"username": request.session.get("username")})