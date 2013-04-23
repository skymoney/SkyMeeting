$(function(){
    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#profileForm").validations();
    $("#passwordForm").validations();
    // ===============================
    

    
    // validation patch
    var checkRepeatPassword = function(){
        if($("#repeatPassword").val() != $("#newPassword").val())
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

    $("#passwordFormOk").click(function(){
        if(checkRepeatPassword() == false)
        {
            return false;
        }
        $("#passwordForm").submit();
    });

});