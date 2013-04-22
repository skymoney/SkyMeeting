$(function(){
    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    // $("#signinForm").validations();
    $("#newAccountForm").validations();

    // validation patch
    var checkRepeatPassword = function(){
    	if($("#repeatPassword").val() != $("#inputPassword").val())
    	{
    		$("#repeatPasswordError").show();
    		return false;
    	}
    	else
    	{
    		$("#repeatPasswordError").hide();
    		return true;
    	}
    };
    $("#repeatPassword").blur(checkRepeatPassword);

    $("#newAccountFormOk").click(function(){
    	if(checkRepeatPassword() == false)
    	{
    		return false;
    	}
    	$("#newAccountForm").submit();
    });


});