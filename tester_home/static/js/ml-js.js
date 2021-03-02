function clear_input(){
	var divEle= document.getElementById('form-search').reset();
}

function see_password(){
    var divEle= document.getElementById('eye_style');
    var divEle2= document.getElementById('password');
    if(divEle2.type==='password')
    {
        divEle.className='glyphicon glyphicon-eye-close';
        divEle2.setAttribute('type','text');
    }else
    {
        divEle.className='glyphicon glyphicon-eye-open';
        divEle2.setAttribute('type','password');
    }
}

function showDeleteModal(obj) {
    var $tds = $(obj).parent().parent().children();// 获取到所有列
    var project_id = $tds[0].innerHTML;
    var project_name = $tds[1].innerHTML;
    $("#cfm_project_id").html(project_id);
    $("#cfm_project_info").html(project_name);
    $("#deleteProjectModal").modal({
        backdrop : 'static',
        keyboard : false
    });
}
function deleteProjectConfirm() {
	id = document.getElementById("cfm_project_id").innerHTML;
    location.href='/project_manage/project_delete/'+id+'/';
}