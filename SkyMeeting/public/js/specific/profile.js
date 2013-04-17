$(function(){
	// ===============================
	// initialization
	// ===============================
	selectNavItem("profile");

    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#profileForm").validations();
    // ===============================
    

    $("#editProfileLink").click(function(){
    	$("#profileDiv").hide();
    	$("#profileForm").show();
    });
    $("#profileFormCancel").click(function(){
        $("#profileDiv").show();
        $("#profileForm").hide();
    });
});