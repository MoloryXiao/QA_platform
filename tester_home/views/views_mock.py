from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 登录态装饰器
from tester_home.models.mock import MockConfig
from django.http import HttpResponseRedirect,HttpResponse


@login_required
def mock_manage(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["mock_configs"] = MockConfig.objects.all()
    rtn_dict["type"] = "list"
    return render(request, "mock_manage.html", rtn_dict)


def mock_add(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    if request.method == "GET":
        rtn_dict["type"] = "add"
        return render(request, "mock_manage.html", rtn_dict)
    else:
        rtn_dict["type"] = "list"
        business_name = request.POST.get("add_business_name", "")
        business_tag = request.POST.get("add_business_tag", "")

        message_format = 0
        if request.POST.getlist("add_message_format"):
            message_format = request.POST.getlist("add_message_format")[0]

        mock_type = 0
        if request.POST.getlist("add_mock_type"):
            mock_type = request.POST.getlist("add_mock_type")[0]

        mock_match_field = request.POST.get("add_mock_match_field", "")

        is_diff_merchant = 0
        if request.POST.getlist("add_is_diff_merchant"):
            is_diff_merchant = request.POST.getlist("add_is_diff_merchant")[0]

        merchant_field = request.POST.get("add_merchant_field", "")

        print(business_name,
              business_tag,
              message_format,
              mock_type,
              mock_match_field,
              is_diff_merchant,
              merchant_field)

        MockConfig.objects.create(business_name=business_name,
                                  business_tag=business_tag,
                                  message_format=message_format,
                                  mock_type=mock_type,
                                  mock_match_field=mock_match_field,
                                  is_diff_merchant=is_diff_merchant,
                                  merchant_field=merchant_field,
                                  status=1)
        return HttpResponseRedirect("/mock_manage/")


def mock_modify(request, mock_config_id):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")

    m = MockConfig.objects.get(id=mock_config_id)
    rtn_dict["mock_config"] = m

    if request.method == "GET":
        rtn_dict["type"] = "modify"
        return render(request, "mock_manage.html", rtn_dict)
    else:
        m.business_name = request.POST.get("modify_business_name", "")
        m.business_tag = request.POST.get("modify_business_tag", "")
        m.mock_match_field = request.POST.get("modify_mock_match_field", "")
        m.merchant_field = request.POST.get("modify_merchant_field", "")

        rtn_dict["type"] = "list"
        if request.POST.getlist("modify_message_format"):
            m.message_format = int(request.POST.getlist("modify_message_format")[0])
        else:
            m.message_format = 0

        if request.POST.getlist("modify_mock_type"):
            m.mock_type = int(request.POST.getlist("modify_mock_type")[0])
        else:
            m.mock_type = 0

        if request.POST.getlist("modify_is_diff_merchant"):
            m.is_diff_merchant = int(request.POST.getlist("modify_is_diff_merchant")[0])
            if m.is_diff_merchant == 0:
                m.merchant_field = ''
        else:
            m.is_diff_merchant = 0

        if m.business_name == '':
            rtn_dict["type"] = "modify"
            rtn_dict["error_info"] = "业务名称不能为空，修改失败！"
            return render(request, "mock_manage.html", rtn_dict)
        elif m.business_tag == '':
            rtn_dict["type"] = "modify"
            rtn_dict["error_info"] = "唯一标识不能为空，修改失败！"
            return render(request, "mock_manage.html", rtn_dict)

        m.save()
        print("save")
        return HttpResponseRedirect("/mock_manage/")


def mock_delete(request, mock_config_id):
    MockConfig.objects.get(id=mock_config_id).delete()
    return HttpResponseRedirect("/mock_manage/")


def mock_search(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["type"] = "list"
    business_name = request.POST.get("search_business_name", "")
    business_tag = request.POST.get("search_business_tag", "")

    if business_name == "" and business_tag == "":
        rtn_dict["mock_configs"] = MockConfig.objects.all()
    elif business_name != "" and business_tag != "":
        rtn_dict["mock_configs"] = MockConfig.objects.filter(business_name__contains=business_name, business_tag__contains=business_tag)
    elif business_name != "":
        rtn_dict["mock_configs"] = MockConfig.objects.filter(business_name__contains=business_name)
    elif business_tag != "":
        rtn_dict["mock_configs"] = MockConfig.objects.filter(business_tag__contains=business_tag)

    return render(request, "mock_manage.html", rtn_dict)
