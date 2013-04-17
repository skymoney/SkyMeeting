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



	// constants
	var AJAX_IDLE = 0;
	var AJAX_BUSY = 0;

	// ajax flags
	var ajaxDeleteMeetingFlag = AJAX_IDLE;
	var ajaxChangeStatusFlag = AJAX_IDLE;



	// ===============================
	// delete meeting
	// ===============================
	var deleteMeetingShowFunc = function(){
		// get data
		var target = $(this).parents("tr").find("input[type='hidden']");
		var deleteMeetingId = target.attr("data-mid");
		var deleteMeetingTitle = target.attr("data-title");

		// init delteGroupDiv
		$("#deleteMeetingId").attr("data-value", deleteMeetingId);
		$("#deleteMeetingTitle").text(deleteMeetingTitle);

		// get position
		var offset = $(this).offset();
		// get popup div width
		var width = $("#deleteMeetingDiv").width();

		$("#deleteMeetingDiv").css({
			"display":"inline-block", 
			"position":"absolute",
			"top":offset.top + 20, 
			"left":offset.left - width + 10
		});
	};
	$("a.delete-meeting").click(deleteMeetingShowFunc);

	$("#deleteMeetingOk").click(function(){
		var deleteMeetingId = $("#deleteMeetingId").attr("data-value");

		// ajax flag
		if(ajaxDeleteMeetingFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDeleteMeetingFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/deletemeeting/",
				{
					"mid": deleteMeetingId
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						$("#meetingTable").find("input[type='hidden'][data-mid='" + deleteMeetingId + "']").parent("tr").remove();
					}
					else
					{
						// error message
					}
				}
			);
		}

		$("#deleteMeetingDiv").hide();
	});
	$("#deleteMeetingCancel").click(function(){
		$("#deleteMeetingDiv").hide();
	});
	$("#deleteMeetingHeader").find("a.close").click(function(){
		$("#deleteMeetingDiv").hide();
	});
	// ===============================



	// ===============================
	// delete meeting
	// ===============================

	// ===============================
});