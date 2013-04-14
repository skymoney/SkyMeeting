$(function(){
	// js for language change
	$("#langList").find("a").click(function(){
		var langCode = $(this).attr("data-lang-code");
		var form = $("#langForm");
		form.find("input[name='language']").val(langCode);
		form.submit();
	});
});