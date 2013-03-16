$(function() {

	// click event for customized checkbox
	$("div.checker input").click(function(){
		var target = $(this).parent("span");
		if(target.hasClass("checked"))
		{
			target.removeClass("checked");
		}
		else
		{
			target.addClass("checked");
		}
	});

	// click event for customized radio
	$("div.radio input").click(function(){
		$(this).parents("label.radio").siblings("label.radio").each(function(){
			$(this).find("div.radio span").removeClass("checked");
		});
		var target = $(this).parent("span");
		target.addClass("checked");
	});



});