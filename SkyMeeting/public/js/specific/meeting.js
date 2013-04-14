/* extend functions */
$.fn.setCursorPosition = function(position) {
    if(this.length == 0) return this;
    return $(this).setSelection(position, position);
}
$.fn.setSelection = function(selectionStart, selectionEnd) {
    if(this.length == 0) return this;
    input = this[0];

    if (input.createTextRange) {
        var range = input.createTextRange();
        range.collapse(true);
        range.moveEnd('character', selectionEnd);
        range.moveStart('character', selectionStart);
        range.select();
    } else if (input.setSelectionRange) {
        input.focus();
        input.setSelectionRange(selectionStart, selectionEnd);
    }

    return this;
}
$.fn.focusEnd = function() {
    this.setCursorPosition(this.val().length);
}



$(function() {
	selectNavItem("meetings");

	// constants
	var TEXT_REPLY = gettext("Reply");
	var TEXT_REPLY_SEPERATOR = ": ";

	var AJAX_IDLE = 0;
	var AJAX_BUSY = 0;

	// ajax flags
	var ajaxAddCommentFlag = AJAX_IDLE;



	var replyClickFunc = function(){
		var dataElement = $(this).parents("li.comment").find("input[type='hidden']");
		var commentId = dataElement.attr("data-comment-id");
		var authorId = dataElement.attr("data-author-id");
		var authorName = dataElement.attr("data-author-name");

		$("#replyToData").attr("data-comment-id", commentId);
		$("#replyToData").attr("data-author-id", authorId);
		$("#replyToData").attr("data-author-name", authorName);

		// 简单粗暴!!!
		$("#inputComment").val(TEXT_REPLY + authorName + TEXT_REPLY_SEPERATOR);

		$("#inputComment").focusEnd();
		$.scrollTo("#inputComment");
		// $.scrollTo( '#inputComment', 800, {easing:'elasout'} );
		// !!!
	};
	$("a.reply").click(replyClickFunc);


	$("#addCommentOk").click(function(){
		// clear errors
		$("#addCommentError").hide();
		
		var meetingId = $("#meetingData").attr("data-meeting-id");
		// meetingId被改怎么破???
		
		var content = $("#inputComment").val();
		content = content.trim();
		
		// validation
		// too young too simple, what if injected code???
		if(!(content.length > 0 && content.length < 1000))
		{
			// error message
			$("#addCommentError").show();
			return false;
		}


		var replyToCommentId = $("#replyToData").attr("data-comment-id");
		var replyToAuthorId = $("#replyToData").attr("data-author-id");
		var replyToAuthorName = $("#replyToData").attr("data-author-name");

		// check reply content
		if(content.indexOf(TEXT_REPLY + replyToAuthorName) != 0)
		{
			// reset empty
			replyToCommentId = "";
			replyToAuthorId = "";
			replyToAuthorName = "";
		}
		

		// ajax flag
		if(ajaxAddCommentFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxAddCommentFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/meeting/addcomment/",
				{
					"meetingId": meetingId,
					"content": content,
					"replyToUser": replyToAuthorId,
					"replyToComment": replyToCommentId
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						var curFloor = $("#commentList").children("li").last().find(".floor").text();
						var nextFloor = Number(curFloor) + 1;
						
						$("#commentList").append(
							"<li class=\"comment\">" + 
								"<div class=\"author\">" + 
									"<div class=\"pic\">" + 
										"<img src=\"../public/img/head_48x48.png\" class=\"img-polaroid\" />" + 
									"</div>" + 
									"<div class=\"name\">" + 
										"<a href=\"javascript:void(0);\">" + result.authorName + "</a>" + 
									"</div>" + 
								"</div>" + 
								"<div class=\"info\">" + 
									"<div class=\"basic\">" + 
										"<span class=\"time\">" + result.createTime + "</span>" + 
										"&nbsp;|&nbsp;" + 
										"<a>" + "#" + "<span class=\"floor\">" + nextFloor + "</span></a>" + 
									"</div>" + 
									"<div class=\"act\">" + 
										"<a href=\"javascript:void(0);\" class=\"reply\">" + TEXT_REPLY + "</a>" + 
									"</div>" + 
									"<div class=\"clearfix\"></div>" + 
									"<div class=\"content\">" + content + "</div>" + 
								"</div>" + 
								"<input type=\"hidden\" data-comment-id=\"" + result.commentId + "\" data-author-id=\"" + result.authorId + "\" data-author-name=\"" + result.authorName + "\" />" + 
								"<div class=\"clearfix\"></div>" + 
							"</li>");
						
						// 自己可以回复自己吗???
						// bind event
						$("#commentList").children("li").last().find("a.reply").click(replyClickFunc);

						// clear input comment
						$("#inputComment").val("");
						$("#replyToData").attr("data-comment-id", "");
						$("#replyToData").attr("data-author-id", "");
						$("#replyToData").attr("data-author-name", "");
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxAddCommentFlag = AJAX_IDLE;
				}
			);
		}

	});

});