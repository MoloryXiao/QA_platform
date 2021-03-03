from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 登录态装饰器
from tester_home.models.project import Project
from django.http import HttpResponseRedirect


@login_required
def project_manage(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["projects"] = Project.objects.all()
    rtn_dict["type"] = "list"
    return render(request, "project_manage.html", rtn_dict)


def project_add(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    if request.method == "GET":
        rtn_dict["type"] = "add"
        return render(request, "project_manage.html", rtn_dict)
    else:
        rtn_dict["type"] = "list"
        name = request.POST.get("project_name", "")
        description = request.POST.get("project_description", "")
        if request.POST.getlist("is_valid"):
            status = request.POST.getlist("is_valid")[0]
        else:
            status = 0
        print(name, description, status)

        if name == '':
            rtn_dict["type"] = "add"
            rtn_dict["error_info"] = "项目名称不能为空，提交失败！"
            return render(request, "project_manage.html", rtn_dict)

        Project.objects.create(name=name, description=description, status=status)
        return HttpResponseRedirect("/project_manage/")


def project_modify(request, project_id):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")

    p = Project.objects.get(id=project_id)
    rtn_dict["project_id"] = project_id
    rtn_dict["project_name"] = p.name
    rtn_dict["project_description"] = p.description
    rtn_dict["project_status"] = p.status

    if request.method == "GET":
        rtn_dict["type"] = "modify"
        return render(request, "project_manage.html", rtn_dict)
    else:
        rtn_dict["type"] = "list"
        p.name = request.POST.get("project_name", "")
        p.description  = request.POST.get("project_description", "")
        if request.POST.getlist("is_valid"):
            p.status = request.POST.getlist("is_valid")[0]
        else:
            p.status = 0

        if p.name == '':
            rtn_dict["type"] = "modify"
            rtn_dict["error_info"] = "项目名称不能为空，修改失败！"
            return render(request, "project_manage.html", rtn_dict)

        p.save()
        return HttpResponseRedirect("/project_manage/")


def project_delete(request, project_id):
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect("/project_manage/")


def project_search(request):
    rtn_dict = dict()
    rtn_dict["username"] = request.session.get("username")
    rtn_dict["type"] = "list"
    name = request.POST.get("search_project_name", "")
    description = request.POST.get("search_project_description", "")
    if name == "" and description == "":
        rtn_dict["projects"] = Project.objects.all()
    elif name != "" and description != "":
        rtn_dict["projects"] = Project.objects.filter(name__contains=name, description__contains=description)
    elif name != "":
        rtn_dict["projects"] = Project.objects.filter(name__contains=name)
    elif description != "":
        rtn_dict["projects"] = Project.objects.filter(description__contains=description)

    return render(request, "project_manage.html", rtn_dict)
