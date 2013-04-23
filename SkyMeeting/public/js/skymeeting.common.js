/* common util functions */
var disableButton = function(btn){
	btn.addClass("disabled");
	btn.attr("disabled", "disabled");
};
var enableButton = function(btn){
	btn.removeClass("disabled");
	btn.removeAttr("disabled");
}