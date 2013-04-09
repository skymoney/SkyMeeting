/* Global Functions */
// ========== enhanced checkbox ==========
// NOTE: shouble fetch by "input[name='xxx'][checked='checked']"
var isCheckboxChecked = function(inputCheckbox){
	if(inputCheckbox.parent("span").hasClass("checked"))
	{
		return true;
	}
	return false;
}
var checkboxCheck = function(inputCheckbox){
	if(isCheckboxChecked(inputCheckbox) == false)
	{
		inputCheckbox.attr("checked", "checked");
		inputCheckbox.parent("span").addClass("checked");
	}
};
var checkboxCancel = function(inputCheckbox){
	if(isCheckboxChecked(inputCheckbox) == true)
	{
		inputCheckbox.removeAttr("checked");
		inputCheckbox.parent("span").removeClass("checked");
	}
};
var checkerCheck = function(checkerElement){
	checkboxCheck(checkerElement.find("input[type='checkbox']"));
};
var checkerCancel = function(checkerElement){
	checkboxCancel(checkerElement.find("input[type='checkbox']"));
};

// click event for customized checkbox
var checkerClickFunc = function(){
	var target = $(this).parent("span");
	if(target.hasClass("checked"))
	{
		target.removeClass("checked");
		$(this).removeAttr("checked");
	}
	else
	{
		target.addClass("checked");
		$(this).attr("checked", "checked");
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