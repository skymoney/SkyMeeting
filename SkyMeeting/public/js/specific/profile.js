$(function(){
	// ===============================
	// initialization
	// ===============================
	selectNavItem("profile");

    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#profileForm").validations();
    $("#passwordForm").validations();
    // ===============================
    
    

    // edit profile
    $("#editProfileLink").click(function(){
    	$("#profileDiv").hide();
    	$("#profileForm").show();
    });
    $("#profileFormCancel").click(function(){
        $("#profileDiv").show();
        $("#profileForm").hide();
    });
    $("#profileFormOk").click(function(){
        $("#profileForm").submit();
    });



    // change password
    $("#changePasswordLink").click(function(){
        $("#accountDiv").hide();
        $("#passwordForm").show();
    });
    $("#passwordFormCancel").click(function(){
        $("#accountDiv").show();
        $("#passwordForm").hide();

        // clear password input
        $("#oldPassword").val("");
        $("#newPassword").val("");
        $("#repeatPassword").val("");

        // clear errors
        $("#passwordForm").find(".alert-msg").each(function(){
            $(this).hide();
        });
    });

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
            "/editaccount/",
            {
                "oldPassword": $("#oldPassword").val(),
                "newPassword": $("#newPassword").val()
            },
            function(data)
            {
                var result = eval("(" + data + ")");
                if(result.success == "true")
                {
                    // success, and close form
                    $("#passwordFormCancel").click();
                }
                else
                {
                    // error message
                    $("#changePasswordError").text(result.errors).show();
                }

                // reset ajax flag!!! enable button
                enableButton($("#passwordFormOk"));
            }
        );
    });

});