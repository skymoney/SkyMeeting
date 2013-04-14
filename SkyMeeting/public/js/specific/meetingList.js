$(function() {
	selectNavItem("meetings");

	// redirect by select
	var redirectFunc = function(){
		var type = $("#meetingTypeSct").find("option:selected").val();
		var ad = $("#meetingAdSct").find("option:selected").val();
		location.href = "/meetings/?type=" + type + "&ad=" + ad;
	};
	$("#meetingTypeSct").change(redirectFunc);
	$("#meetingAdSct").change(redirectFunc);
});