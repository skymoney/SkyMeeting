var selectNavItem = function(name){
	var target = $("#navList").children("li[data-name='" + name + "']");
	if(target.length != 0)
	{
		target.siblings("li").each(function(){
			$(this).removeClass("active");
		});
		target.addClass("active");
	}
};

$(function(){
	// js for language change
	$("#langList").find("a").click(function(){
		var langCode = $(this).attr("data-lang-code");
		var form = $("#langForm");
		form.find("input[name='language']").val(langCode);
		form.submit();
	});
});