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

	// role change
	$("#roleList").find("a.role").click(function(){
		var rid = $(this).attr("data-rid");
		var cid = $(this).attr("data-cid");
		var form = $("#roleForm")
		form.find("input[name='rid']").val(rid);
		form.find("input[name='cid']").val(cid);
		form.submit();
	});
});