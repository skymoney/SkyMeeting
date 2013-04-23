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
        
        // ajax flag!!! disable button
        disableButton($("#passwordFormOk"));

        $.post(
            "/setpassword/",
            {
                "newPassword": $("#newPassword").val()
            },
            function(data)
            {
                var result = eval("(" + data + ")");
                if(result.success == "true")
                {
                    // success message
                    $("#resetPasswordHint").show();
                    // redirect to login page
                    setTimeout(function(){
                        location.href = "/";
                    }, 2000);
                }
                else
                {
                    // error message
                    $("#resetPasswordError").text(result.errors).show();

                    // reset ajax flag!!! enable button
                    enableButton($("#passwordFormOk"));
                }
            }
        );
    });

});