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

					// reset ajax flag
					ajaxDeleteMeetingFlag = AJAX_IDLE;
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
	// change status
	// ===============================
	$(".status-menu a.status").click(function(){
		// get data
		var mid = $(this).attr("data-mid");
		var status = $(this).attr("data-status");

		var curStatus = $(this).parents(".dropdown").find(".status-drop").attr("data-cur-status");
		// 优化：only submit when status changed
		// 问题："Active" status其实包含了status 1和5
		// ......

		// ajax flag
		if(ajaxChangeStatusFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxChangeStatusFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/meeting/changestatus/",
				{
					"mid": mid,
					"status": status
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						var target = $("#meetingTable").find("input[type='hidden'][data-mid='" + mid + "']").parent("tr").find("a.status-drop");
						target.attr("data-cur-status", status);
						target.removeClass("label-info").removeClass("label-inverse");

						// NOTE: 代码矬比!!!
						if(status == 1)
						{
							target.addClass("label-info");
							target.find("span").text(gettext("Active"));
						}
						else if(status == 11)
						{
							target.addClass("label-inverse");
							target.find("span").text(gettext("End"));
						}
						else if(status == 15)
						{
							target.find("span").text(gettext("Closed"));
						}
						else
						{
							// undefined
						}
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxChangeStatusFlag = AJAX_IDLE;
				}
			);
		}
	});
	// ===============================
});