$(function(){
    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#forgetForm").validations();
    // ===============================


	$("#forgetFormOk").click(function(){
        // ajax flag!!! disable button
        disableButton($("#forgetFormOk"));
        $("#forgetFormOk").val(gettext("Sending..."));

        $.post(
        	"/forgetpassword/",
        	{
        		"email": $("#inputEmail").val()
        	},
        	function(data)
        	{
        		var result = eval("(" + data + ")");
        		if(result.success == "true")
        		{
        			// success, and close form
        			$("#forgetModal").modal("hide");
        		}
        		else
        		{
        			// error message
        			$("#sendEmailError").text(result.errors).show();
        		}

		        // reset ajax flag!!! enable button
        		enableButton($("#forgetFormOk"));
        		$("#forgetFormOk").val(gettext("Send"));
        	}
        );
	});


	// login error message feedback
	// ......
});