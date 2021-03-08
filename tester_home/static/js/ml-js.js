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

function showDeleteProjectModal(obj) {
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

function showDeleteMockConfigModal(obj) {
    var $tds = $(obj).parent().parent().children();// 获取到所有列
    var project_id = $tds[0].innerHTML;
    var project_name = $tds[1].innerHTML;
    $("#cfm_mock_config_id").html(project_id);
    $("#cfm_mock_config_info").html(project_name);
    $("#deleteMockConfigModal").modal({
        backdrop : 'static',
        keyboard : false
    });
}

function deleteProjectConfirm() {
	id = document.getElementById("cfm_project_id").innerHTML;
    location.href='/project_manage/project_delete/'+id+'/';
}

function deleteMockConfigConfirm() {
	id = document.getElementById("cfm_mock_config_id").innerHTML;
    location.href='/mock_manage/mock_delete/'+id+'/';
}

function visible_merchant_field(){
    document.getElementById("div_merchant_field").removeAttribute("hidden");
}
function invisible_merchant_field(){
    document.getElementById("div_merchant_field").setAttribute("hidden",true);
}
function visible_merchant_field_mod(){
    document.getElementById("div_merchant_field_modify").removeAttribute("hidden");
}
function invisible_merchant_field_mod(){
    document.getElementById("div2_merchant_field_modify").setAttribute("hidden",true);
}

function clear_modal_form(){
//    document.getElementById("add_business_form").reset();
//    document.getElementById("div_merchant_field").setAttribute("hidden",true);
    $(add_business_form).data('formValidation').resetForm();

}
$(document).ready(function() {
	    $('#add_business_form').formValidation({
	        message: 'This value is not valid',
	        icon: {
	            valid: 'glyphicon glyphicon-ok',
	            invalid: 'glyphicon glyphicon-remove',
	            validating: 'glyphicon glyphicon-refresh'
	        },
	        fields: {
	            add_business_name: {
	                row: '.col-sm-6',
	                validators: {
	                    notEmpty: {
	                        message: '业务名称不能为空'
	                    }
	                }
	            },
	            add_business_tag: {
	                row: '.col-sm-6',
	                validators: {
	                    notEmpty: {
	                        message: '唯一标识不能为空'
	                    },
	                    stringLength: {
	                        min: 3,
	                        max: 15,
	                        message: '唯一标识字段必须在3-15个字符之间'
	                    },
	                    regexp: {
	                        regexp: /^[a-zA-Z0-9_\.]+$/,
	                        message: '接口匹配字段只能是字符'
	                    }
	                }
	            },
	            add_mock_type: {
	                row: '.col-sm-7',
	                validators: {
	                    notEmpty: {
	                        message: '必须选择匹配方式'
	                    }
	                }
	            },
	        }
	    });
	});