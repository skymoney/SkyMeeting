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
        $("#newPassword").val("");
        $("#repeatPassword").val("");
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
        $("#passwordForm").submit();
    });

});