/* Global Functions */
// click event for customized checkbox
var checkerClickFunc = function(){
	var target = $(this).parent("span");
	if(target.hasClass("checked"))
	{
		target.removeClass("checked");
	}
	else
	{
		target.addClass("checked");
	}
};

// click event for customized radio
var radioClickFunc = function(){
	$(this).parents("label.radio").siblings("label.radio").each(function(){
		$(this).find("div.radio span").removeClass("checked");
	});
	var target = $(this).parent("span");
	target.addClass("checked");
};


// ====================================
$(function() {
	// bind click event
	$("div.checker input").bind("click", checkerClickFunc);
	$("div.radio input").bind("click", radioClickFunc);
	
});