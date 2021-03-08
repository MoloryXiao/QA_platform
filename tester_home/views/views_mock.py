from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 登录态装饰器
from tester_home.models.mock import MockConfig
from django.http import HttpResponseRedirect,HttpResponse


@login_required
def mock_manage(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["mock_configs"] = MockConfig.objects.all()
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

#
# def mock_modify(request, mock_id):
#     rtn_dict = dict()
#     rtn_dict["username"] = request.session.get("username")
#
#     p = mock.objects.get(id=mock_id)
#     rtn_dict["mock_id"] = mock_id
#     rtn_dict["mock_name"] = p.name
#     rtn_dict["mock_description"] = p.description
#     rtn_dict["mock_status"] = p.status
#
#     if request.method == "GET":
#         rtn_dict["type"] = "modify"
#         return render(request, "mock_manage.html", rtn_dict)
#     else:
#         rtn_dict["type"] = "list"
#         p.name = request.POST.get("mock_name", "")
#         p.description  = request.POST.get("mock_description", "")
#         if request.POST.getlist("is_valid"):
#             p.status = request.POST.getlist("is_valid")[0]
#         else:
#             p.status = 0
#
#         if p.name == '':
#             rtn_dict["type"] = "modify"
#             rtn_dict["error_info"] = "项目名称不能为空，修改失败！"
#             return render(request, "mock_manage.html", rtn_dict)
#
#         p.save()
#         return HttpResponseRedirect("/mock_manage/")
#
#


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
