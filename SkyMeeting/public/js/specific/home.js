$(function(){
	selectNavItem("home");

	$(".well").click(function(){
		$(this).addClass("selected");
		$(this).siblings().each(function(){
			$(this).removeClass("selected");
		});

		// ajax submit
		
	});
});