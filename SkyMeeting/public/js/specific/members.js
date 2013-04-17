$(function() {
	// ===============================
	// initialization
	// ===============================
	selectNavItem("members");

    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#inviteForm").validations();
    $("#memberForm").validations();
    // ===============================



	// constants
	var KEY_SPACE = 32;
	var KEY_BACKSPACE = 8;

	var AJAX_IDLE = 0;
	var AJAX_BUSY = 0;

	// ajax flags
	var ajaxDynAddGroupFlag = AJAX_IDLE;
	var ajaxDynAddTagFlag = AJAX_IDLE;
	var ajaxInviteMemberFlag = AJAX_IDLE;
	var ajaxEditMemberFlag = AJAX_IDLE;
	var ajaxDeleteMemberFlag = AJAX_IDLE;
	var ajaxAddTagFlag = AJAX_IDLE;
	var ajaxDeleteTagFlag = AJAX_IDLE;
	var ajaxAddGroupFlag = AJAX_IDLE;
	var ajaxEditGroupFlag = AJAX_IDLE;
	var ajaxDeleteGroupFlag = AJAX_IDLE;


	// json storage, for editModal initializaion
	// format: [{gid, gname, cid, count}, ...]
	var globalGroups = eval($("#globalGroupString").attr("data-value"));
	// format: [{tid, tname, cid}, ...]
	var globalTags = eval($("#globalTagString").attr("data-value"));

	// util functions of gloabl storage
	var addToGlobalGroups = function(newGroupId, newGroupName){
		globalGroups.push(eval("({\"gid\":" + newGroupId + ",\"gname\":\"" + newGroupName + "\"})"));
	}
	var addToGlobalTags = function(newTagId, newTagName){
		globalTags.push(eval("({\"tid\":" + newTagId + ",\"tname\":\"" + newTagName + "\"})"));
	}
	var removeFromGlobalGroups = function(deleteGroupId){
		for(var i=0; i<globalGroups.length; i++)
		{
			if(globalGroups[i].gid == deleteGroupId)
			{
				globalGroups.splice(i, 1);
				break;
			}
		}
	}
	var removeFromGlobalTags = function(deleteTagId){
		for(var i=0; i<globalTags.length; i++)
		{
			if(globalTags[i].tid == deleteTagId)
			{
				globalTags.splice(i, 1);
				break;
			}
		}
	}
	var updateGlobalGroups = function(groupId, newGroupName){
		for(var i=0; i<globalGroups.length; i++)
		{
			if(globalGroups[i].gid == groupId)
			{
				globalGroups[i].gname = newGroupName;
				break;
			}
		}
	}



	/* used in modal popup */
	var scrollToFormEndFunc = function(){
		$(this).parents(".modal-body").scrollTo(".form-end");
	};





	// ====================================
	// tooltips
	// ====================================
	// tooltip for tags omited
    $(document).tooltip({
        selector: "a[data-toggle=tooltip]"
    });
    $(document).tooltip();

    // tooltip patch
    $("a[data-toggle=tooltip]").click(function(){
    	$(this).tooltip("toggle");
    });
    $("a[data-toggle=tooltip]").mouseleave(function(){
    	$(this).tooltip("hide");
    });
    // ====================================





	// ====================================
	// groups
	// ====================================
	var appendGroupNavList = function(newGroupId, newGroupName){
		// update nav, append
		$("#groupList").append(
			"<li>" + 
				"<a href=\"?gid=" + newGroupId + "\">" + 
					"<span class=\"group-name\">" + newGroupName + "&nbsp;</span>" + 
					"<span class=\"group-size\">(0)</span>" + 
					"<i class=\"icon-chevron-right\"></i>" + 
				"</a>" + 
				"<div class=\"group-action hide\">" + 
					"<a href=\"javascript:void(0);\" class=\"edit-group\" title=\"" + gettext("Edit group") + "\">" + 
						"<i class=\"icon-edit\"></i>" + 
					"</a>" + 
					"<a href=\"javascript:void(0);\" class=\"delete-group\" title=\"" + gettext("Delete group") + "\">" + 
						"<i class=\"icon-trash\"></i>" + 
					"</a>" + 
					"<input type=\"hidden\" data-gid=\"" + newGroupId + "\" data-gname=\"" + newGroupName + "\" />" +
			"</li>");
		
		// bind event for new item of groupList
		var newItem = $("#groupList").children("li").last();
		newItem.find("a.edit-group").click(editGroupShowFunc);
		newItem.find("a.delete-group").click(deleteGroupShowFunc);
		newItem.mouseenter(function(){
			$(this).find(".group-action").show();
		});
		newItem.mouseleave(function(){
			$(this).find(".group-action").hide();
		});
	};


	$("#addGroupLink").click(function(){
		if($("#addGroupDiv").css("display") == "none")
		{
			$("#addGroupDiv").slideDown("fast");
			// clear and hide
			$("#newGroupName").val("");
			$("#addGroupErr").empty();
		}
		else
		{
			$("#addGroupDiv").slideUp("fast");
		}
	});
	$("#addGroupHeader").find("a.close").click(function(){
		$("#addGroupDiv").slideUp("fast");
	});
	$("#addGroupOk").click(function(){
		var newGroupName = $("#newGroupName").val();
		newGroupName = newGroupName.trim();

		// validation
		// should use Reg search
		if(newGroupName.indexOf(",") > -1 || newGroupName.indexOf("，") > -1)
		{
			// error message
			$("#addGroupErr").text(gettext("Cannot contain punctuation"));
			return false;
		}
		if(!(newGroupName.length > 0 && newGroupName.length <= 20))
		{
			// error message
			$("#addGroupErr").text(gettext("Length should be between 1 to 20"));
			return false;
		}


		// ajax flag
		if(ajaxAddGroupFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxAddGroupFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/addgroup/",
				{
					"groupName": newGroupName
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						var newGroupId = result.gid;

						// update group nav
						appendGroupNavList(newGroupId, newGroupName);

						// update global groups storage
						addToGlobalGroups(newGroupId, newGroupName);

						// clear and hide
						$("#addGroupDiv").slideUp("fast");
					}
					else
					{
						// error message
						$("#addGroupErr").text(gettext("Failed because of server problem."));
					}

					// reset ajax flag
					ajaxAddGroupFlag = AJAX_IDLE;
				}
			);
		}

	});


	// group actions mouse event
	$("#groupList").find("li").not($("#groupList").children("li").first()).mouseenter(function(){
		$(this).find(".group-action").show();
	});
	$("#groupList").find("li").not($("#groupList").children("li").first()).mouseleave(function(){
		$(this).find(".group-action").hide();
	});


	// edit group
	var editGroupShowFunc = function(){
		// get data
		var target = $(this).siblings("input[type='hidden']");
		var editGroupId = target.attr("data-gid");
		var editGroupName = target.attr("data-gname");

		// init editGroupDiv
		$("#editGroupId").attr("data-value", editGroupId);
		$("#editGroupName").val(editGroupName);

		// clear error message
		$("#editGroupErr").empty();

		// get position
		var offset = $(this).offset();

		$("#editGroupDiv").css({
			"display": "inline-block",
			"position": "absolute",
			"top": offset.top,
			"left": offset.left
		});
	};
	$("a.edit-group").click(editGroupShowFunc);

	$("#editGroupOk").click(function(){
		var editGroupId = $("#editGroupId").attr("data-value");
		var editGroupName = $("#editGroupName").val();
		editGroupName = editGroupName.trim();

		// validation
		// should use Reg search
		if(editGroupName.indexOf(",") > -1 || editGroupName.indexOf("，") > -1)
		{
			// error message
			$("#editGroupErr").text(gettext("Cannot contain punctuation"));
			return false;
		}
		if(!(editGroupName.length > 0 && editGroupName.length <= 20))
		{
			// error message
			$("#editGroupErr").text(gettext("Length should be between 1 to 20"));
			return false;
		}


		// ajax flag
		if(ajaxEditGroupFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxEditGroupFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/editgroup/",
				{
					"gid": editGroupId,
					"gname": editGroupName
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// update group nav item
						$("#groupList").find("a[href='?gid=" + editGroupId + "']").find(".group-name").text(editGroupName);

						// update global groups storage
						updateGlobalGroups(editGroupId, editGroupName);
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxEditGroupFlag = AJAX_IDLE;
				}
			);
		}

		$("#editGroupDiv").hide();
	});
	$("#editGroupHeader").find("a.close").click(function(){
		$("#editGroupDiv").hide();
	});


	// delete group
	var deleteGroupShowFunc = function(){
		// get data
		var target = $(this).siblings("input[type='hidden']");
		var deleteGroupId = target.attr("data-gid");
		var deleteGroupName = target.attr("data-gname");

		// init delteGroupDiv
		$("#deleteGroupId").attr("data-value", deleteGroupId);
		$("#deleteGroupName").text(deleteGroupName);

		// get position
		var offset = $(this).offset();

		$("#deleteGroupDiv").css({
			"display": "inline-block",
			"position": "absolute",
			"top": offset.top,
			"left": offset.left
		});
	};
	$("a.delete-group").click(deleteGroupShowFunc);

	$("#deleteGroupOk").click(function(){
		var deleteGroupId = $("#deleteGroupId").attr("data-value");

		// ajax flag
		if(ajaxDeleteGroupFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDeleteGroupFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/deletegroup/",
				{
					"gid": deleteGroupId
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// update group nav
						$("#groupList").find("a[href='?gid=" + deleteGroupId + "']").parent("li").remove();

						// update global groups storage
						removeFromGlobalGroups(deleteGroupId);
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxDeleteGroupFlag = AJAX_IDLE;
				}
			);
		}

		$("#deleteGroupDiv").hide();
	});
	$("#deleteGroupCancel").click(function(){
		$("#deleteGroupDiv").hide();
	});
	$("#deleteGroupHeader").find("a.close").click(function(){
		$("#deleteGroupDiv").hide();
	});


	// ====================================







	// ====================================
	// tags
	// ====================================
	// tag click function
	var tagClickFunc = function(){
		// toggle class
		if($(this).hasClass("tag-selected"))
		{
			$(this).removeClass("tag-selected");
		}
		else
		{
			$(this).addClass("tag-selected");
		}

		// redirect
		var tagIds = "";
		$("a.tag-selected").each(function(){
			if(tagIds.length == 0)
			{
				tagIds += $(this).attr("data-tid");
			}
			else
			{
				tagIds += ("+" + $(this).attr("data-tid"));
			}
		});

		var groupId = $("#curGroupId").attr("data-value");
		location.href = "/members/?gid=" + groupId + "&tid=" + tagIds;
	};
	$("a.tag").click(tagClickFunc);


	// edit tags
	$("#editTagsLink").click(function(){
		$("#editTagsLink").hide();
		$("#editTagsOk").show();

		$("#tagList").hide();
		$("#editTagsDiv").show();

		$("#editNewTag").focus();
	});
	$("#tagsArea").click(function(){
		$("#editNewTag").focus();
	});
	$("#editTagsOk").click(function(){
		$("#editTagsOk").hide();
		$("#editTagsLink").show();

		$("#editTagsDiv").hide();
		$("#tagList").show();

		$("#editNewTag").val("");

		// refresh???
		var gid = $("#curGroupId").attr("data-value");
		var tid = $("#curTagId").attr("data-value");

		// if multiple tags, remove square brackets
		if(tid.indexOf("[") > -1)
		{
			tid = tid.substr(1, tid.length);
		}
		if(tid.indexOf("]") > -1)
		{
			tid = tid.substr(0, tid.length-1);
		}

		// replace sperator
		if(tid.indexOf(",") > -1)
		{
			var reg = new RegExp(", ", "g");
			tid = tid.replace(reg, "+");
		}
		
		// redirect
		location.href = "/members/?gid=" + gid + "&tid=" + tid;
	});


	// delete tag function
	var deleteTagFunc = function(){
		var deleteTagId = $(this).attr("data-tid");

		// ajax flag
		if(ajaxDeleteTagFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDeleteTagFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/deletetag/",
				{
					"tid": deleteTagId
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// var tid = result.tid;
						$("#tagsArea").find("a[data-tid='" + deleteTagId + "']").parent(".tag").remove();

						// update tag nav list???

						// update global tags storage
						removeFromGlobalTags(deleteTagId);
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxDeleteTagFlag = AJAX_IDLE;
				}
			);
		}

	};
	$("a.delete-tag").click(deleteTagFunc);


	// update tagsArea function
	var appendTagsArea = function(newTagId, newTagName){
		$("#tagsArea").children(".tag").last().after("<div class=\"tag\"><span>" + newTagName + "&nbsp;</span><a href=\"javascript:void(0);\" class=\"delete-tag\" data-tid=\"" + newTagId + "\">x</a></div>");
		// bind delete tag click event
		$("#tagsArea").children(".tag").last().find("a.delete-tag").click(deleteTagFunc);
	};

	// update tagList function
	var appendTagNavList = function(newTagId, newTagName){
		$("#tagList").append("<li><a class=\"tag\" data-tid=\"" + newTagId + "\">" + newTagName + "</a></li>");
		// bind tag click event
		$("#tagList").children("li").last().find("a.tag").click(tagClickFunc);
	}


	// input length restriction
	var inputLengthRestrictFunc = function(){
		var maxLen = parseInt($(this).attr("maxlength"));
		// maxLen = 3;
		var curLen = $(this).val().length;
		if(curLen >= maxLen)
		{
			$(this).val($(this).val().substr(0, maxLen));
		}
	};
	// $("#editNewTag").keydown(inputLengthRestrictFunc);


	var showAddTagHint = function(){
		var offset = $("#editNewTag").offset();
		
		$("#addTagHintDiv").css({
			"display": "inline-block",
			"position": "absolute",
			"top": offset.top + 28,
			"left": offset.left + 6
		});
	};

	var clearAndHideAddTagHint = function(){
		$("#addTagHintDiv").hide();
		$("#addTagErr").empty();
	}

	// add tag and delete tag by key
	$("#editNewTag").keydown(function(event){
		var newTagName = $("#editNewTag").val();

		if(event.which == KEY_SPACE)
		{
			var newTagName = newTagName.trim();

			// validation
			// should use Reg search
			if(newTagName.indexOf(",") > -1 || newTagName.indexOf("，") > -1)
			{
				$("#addTagErr").text(gettext("Illegal characters detected"));
				return false;
			}

			if(newTagName.length > 0)
			{
				// ajax flag
				if(ajaxAddTagFlag == AJAX_IDLE)
				{
					// set ajax flag
					ajaxAddTagFlag = AJAX_BUSY;

					// ajax submit
					$.post(
						"/members/addtag/",
						{
							"tagName": newTagName
						},
						function(data)
						{
							var result = eval("(" + data + ")");
							if(result.success == "true")
							{
								var newTagId = result.tid;

								// update tag nav list???

								// update tagsArea
								appendTagsArea(newTagId, newTagName);

								// update global tags storage
								addToGlobalTags(newTagId, newTagName);

								// clear input
								$("#editNewTag").val("");
								clearAndHideAddTagHint();
							}
							else
							{
								// error message
							}

							// reset ajax flag
							ajaxAddTagFlag = AJAX_IDLE;
						}
					);
				}

			}
		}
		else if(event.which == KEY_BACKSPACE)
		{
			if(newTagName.length == 0)
			{
				// the last char is already deleted
				// delete the last tag
				$(this).parent().prev(".tag").find("a.delete-tag").click();
			}
			else if(newTagName.length == 1)
			{
				// the last char would be deleted
				// hide hint
				clearAndHideAddTagHint();
			}
		}
		else
		{
			// if other input char, show hint, or even show tag recommendation if possible in future
			showAddTagHint();
		}

	});

	// ====================================







	// ====================================
	// invite member modal
	// ====================================
	// validation patch
	$("#inputQuestion").change(function(){
		if($(this).val().trim().length > 0)
		{
			$("#inputQuestionError").hide();
		}
	});
	$("#inputAnswer").change(function(){
		if($(this).val().trim().length > 0)
		{
			$("#inputAnswerError").hide();
		}
	});

	// toggle
	$("#checkOther").change(function(){
		$("#otherQuestionDiv").toggle("fast");
	});

	$("#inviteModalOk").click(function(){
		// clear all errors
		$("#inviteForm").find(".alert-msg").each(function(){
			$(this).hide();
		});

		// get form input
		var name = $("#inputName").val().trim();
		var idcard = $("#inputIDno").val().trim();
		var phone = $("#inputPhone").val().trim();
		var email = $("#inputEmail").val().trim();
		var verifyQuestion = $("#inputQuestion").val().trim();
		var verifyAnswer = $("#inputAnswer").val().trim();

		var verifyMode = "";
		$("input[name='verifyMode']:checked").each(function(){
			if(verifyMode.length == 0)
			{
				verifyMode += $(this).val();
			}
			else
			{
				verifyMode += ("+" + $(this).val());
			}
		});

		var authority = $("input[name='authority']:checked").val();
		// alert("name:" + name + "; idcard:" + idcard + "; phone:" + phone + "; email:" + email + "; verifyMode:" + verifyMode + "; verifyQuestion:" + verifyQuestion + "; verifyAnswer:" + verifyAnswer);

		// validation
		if($("#checkOther").attr("checked") == "checked")
		{
			if(verifyQuestion.length == 0)
			{
				$("#inputQuestionError").show();
				return false;
			}
			if(verifyAnswer.length == 0)
			{
				$("#inputAnswerError").show();
				return false;
			}
		}
		

		// ajax flag
		if(ajaxInviteMemberFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxInviteMemberFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/inviteuser/",
				{
					"name": name,
					"idcard": idcard,
					"phone": phone,
					"email": email,
					"verifyMode": verifyMode,
					"verifyQuestion": verifyQuestion,
					"verifyAnswer": verifyAnswer,
					"authority": authority
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// clear and hide
						$("#inputName").val("");
						$("#inputIDno").val("");
						$("#inputPhone").val("");
						$("#inputEmail").val("");
						$("#inputQuestion").val("");
						$("#inputAnswer").val("");

						// clear checkbox checked
						$("input[name='verifyMode']:checked").each(function(){
							$(this).click();
						});
						// default radio checked
						$("#authParticipant").click();

						$("#inviteModal").modal("hide");
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxInviteMemberFlag = AJAX_IDLE;
				}
			);
		}

	});
	// ====================================







	// ====================================
	// edit member modal
	// ====================================
	// init modal function
	var initEditMemberFunc = function(dataElement){
		// hide dynAdd divs
		$("#dynAddGroupDiv").hide();
		$("#dynAddTagDiv").hide();

		// init text
		$("#editId").attr("data-value", dataElement.attr("data-id"));
		$("#editName").val(dataElement.attr("data-name"));
		$("#editIDno").val(dataElement.attr("data-idcard"));
		$("#editPhone").val(dataElement.attr("data-phone"));
		$("#editEmail").val(dataElement.attr("data-email"));

		// init gender radio
		var genderVal = dataElement.attr("data-sex");
		var genderElement = $("input[name='editGender'][value='" + genderVal + "']");
		// invalid genderVal, element not found
		if(genderElement.length == 0)
		{
			$("#genderSecret").click();
		}
		else
		{
			genderElement.click();
		}


		//============ init groups ============
		var groupCbxDiv = $("#groupCbxDiv");
		groupCbxDiv.empty();

		var curGroups = eval(dataElement.attr("data-groups"));

		for(var i=0; i<globalGroups.length; i++)
		{
			var cbxCode = "<label class=\"checkbox\">";
			cbxCode += "<div class=\"checker\">";

			var found = false;
			for(var j=0; j<curGroups.length; j++)
			{
				if(globalGroups[i].gid == curGroups[j].gid)
				{
					found = true;
					break;
				}
			}

			if(found)
			{
				cbxCode += "<span class=\"checked\">";
				cbxCode += "<input type=\"checkbox\" name=\"editGroup\" value=\"" + globalGroups[i].gid + "\" checked=\"checked\" />";
			}
			else
			{
				cbxCode += "<span>";
				cbxCode += "<input type=\"checkbox\" name=\"editGroup\" value=\"" + globalGroups[i].gid + "\" />";
			}

			cbxCode += "</span>";
			cbxCode += "</div>";
			cbxCode += globalGroups[i].gname;
			cbxCode += "</label>";

			groupCbxDiv.append(cbxCode);
			// clear dynGroups
			$("#dynGroups").empty();
		}

		// bind checkbox event
		groupCbxDiv.find("div.checker input").bind("click", checkerClickFunc);

		//========== init groups ends ==========



		//============== init tags ==============
		var tagSelector = $("#tagSect");
		tagSelector.remove();
		$("#tagSect_chzn").remove();

		var selectorCode = "<select id=\"tagSect\" multiple=\"multiple\" data-rel=\"chosen\" >";

		var curTags = eval(dataElement.attr("data-tags"));

		for(var i=0; i<globalTags.length; i++)
		{
			var found = false;
			for(var j=0; j<curTags.length; j++)
			{
				if(globalTags[i].tid == curTags[j].tid)
				{
					found = true;
					break;
				}
			}

			if(found)
			{
				selectorCode += "<option value=\"" + globalTags[i].tid + "\" selected=\"selected\">" + globalTags[i].tname + "</option>";
			}
			else
			{
				selectorCode += "<option value=\"" + globalTags[i].tid + "\">" + globalTags[i].tname + "</option>";
			}
		}

		selectorCode += "</select>";
		$("#tagSectDiv").append(selectorCode);

		// re-init chosen selector
		$("#tagSect").chosen();
		// my scroll patch
		$("#tagSect_chzn").bind("click", scrollToFormEndFunc);
		//============= init tags ends =============


		// finished, show modal
		$("#editModal").modal("show");
	};

	// bind event for showing modal
	$(".edit-member").click(function(){
		var target = $(this).parents("tr").find("input[type='hidden']");
		initEditMemberFunc(target);
	});
	// double click needed???
	/*$("#membersTable").find("tbody").find("tr").dblclick(function(){
		var target = $(this).find("input[type='hidden']");
		initEditMemberFunc(target);
	});*/



	// add new group
	$("#dynAddGroup").click(function(){
		$("#dynAddGroupDiv").toggle("fast");
		// clear and hide
		$("#dynNewGroupName").val("");
		$("#dynAddGroupErr").empty();
	});
	$("#dynAddGroupCancel").click(function(){
		$("#dynAddGroupDiv").hide("fast");
		$("#dynAddGroupErr").empty();
	});
	$("#dynAddGroupOk").click(function(){
		var newGroupName = $("#dynNewGroupName").val();
		newGroupName = newGroupName.trim();

		// validation
		// should use Reg search
		if(newGroupName.indexOf(",") > -1 || newGroupName.indexOf("，") > -1)
		{
			// error message
			$("#dynAddGroupErr").text(gettext("Cannot contain punctuation"));
			return false;
		}
		if(!(newGroupName.length > 0 && newGroupName.length <= 20))
		{
			// error message
			$("#dynAddGroupErr").text(gettext("Length should be between 1 to 20"));
			return false;
		}


		// ajax flag
		if(ajaxDynAddGroupFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDynAddGroupFlag = AJAX_BUSY;

			//=========== ajax begins ===========
			$.post(
				"/members/addgroup/",
				{
					"groupName": newGroupName
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						var newGroupId = result.gid;

						// append element
						$("#dynGroups").append(
							"<label class=\"checkbox\">" + 
								"<div class=\"checker\">" + 
									"<span class=\"checked\">" + 
										"<input type=\"checkbox\" name=\"editGroup\" value=\"" + newGroupId + "\" checked=\"checked\" />" + 
									"</span>" + 
								"</div>" + 
								newGroupName + 
							"</label>");

						// bind event for new element
						$("#dynGroups").children("label.checkbox").last().find("div.checker input").bind("click", checkerClickFunc);


						// update group nav
						appendGroupNavList(newGroupId, newGroupName);

						// update global groups storage
						addToGlobalGroups(newGroupId, newGroupName);

						// clear and hide
						$("#dynAddGroupDiv").hide("fast");
					}
					else
					{
						// error message
						$("#dynAddGroupErr").text(gettext("Failed because of server problem."));
					}

					// reset ajax flag
					ajaxDynAddGroupFlag = AJAX_IDLE;
				}
			);
			//=========== ajax ends ===========
		}

	});



	// patched function for chosen selector
	var searchChoiceCloseFunc = function(){
		var index = $(this).attr("rel");
		$(this).parent("li").hide();  //still a little bug if hiden directly rather than removed
		$("#tagSect_chzn_o_" + index).removeClass("result-selected").addClass("active-result");

		//sync option in selector
		$("#tagSect option:eq(" + index + ")").removeAttr("selected");
	};

	var searchResultClickFunc = function(){
		var selfId = $(this).attr("id");
		var index = selfId.substring(selfId.lastIndexOf("_")+1, selfId.length);
		$("#tagSect_chzn_c_" + index).show();
		$("#tagSect_chzn_o_" + index).removeClass("active-result").addClass("result-selected");

		//patch
		// $("#tagSect_chzn").find(".chzn-drop").css("left", "-9000px");  //problem
		//sync option in selector
		$("#tagSect option:eq(" + index + ")").attr("selected","selected");
	};


	// add new tag
	$("#dynAddTag").click(function(){
		$("#dynAddTagDiv").toggle("fast", function(){
			// my scroll patch
			$(this).parents(".modal-body").scrollTo(".form-end");
		});
		// clear and hide
		$("#dynNewTagName").val("");
		$("#dynAddTagErr").empty();
	});
	$("#dynAddTagCancel").click(function(){
		$("#dynAddTagDiv").hide("fast");
		$("#dynAddTagErr").empty();
	});
	$("#dynAddTagOk").click(function(){
		var newTagName = $("#dynNewTagName").val();
		newTagName = newTagName.trim();

		// validation
		// should use Reg search
		if(newTagName.indexOf(",") > -1 || newTagName.indexOf("，") > -1)
		{
			// error message
			$("#dynAddTagErr").text(gettext("Cannot contain punctuation"));
			return false;
		}
		if(!(newTagName.length > 0 && newTagName.length <= 20))
		{
			// error message
			$("#dynAddTagErr").text(gettext("Length should be between 1 to 20"));
			return false;
		}


		// ajax flag
		if(ajaxDynAddTagFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDynAddTagFlag = AJAX_BUSY;

			//=========== ajax begins ===========
			$.post(
				"/members/addtag/",
				{
					"tagName": newTagName
				},
				function(data)
				{
			    	var result = eval("(" + data + ")");
			    	if(result.success == "true")
			    	{
			    		var newTagId = result.tid;

			    		// append element
						$("#tagSect").append("<option value=\"" + newTagId + "\" selected=\"selected\">" + newTagName + "</option>");
						var tagSectIndex = $("#tagSect option").length - 1;

						$("#tagSect_chzn").find("ul.chzn-choices").find(".search-field").
							before("<li class=\"search-choice\" id=\"tagSect_chzn_c_" + tagSectIndex + "\">" + 
										"<span>" + newTagName + "</span>" + 
										"<a href=\"javascript:void(0);\" class=\"search-choice-close\" rel=\"" + tagSectIndex + "\"></a>" + 
									"</li>");

						$("#tagSect_chzn").find("ul.chzn-results").
							append("<li id=\"tagSect_chzn_o_" + tagSectIndex + "\" class=\"result-selected\">" + newTagName + "</li>");

						// bind event for new element
						$("#tagSect_chzn_c_" + tagSectIndex).find(".search-choice-close").click(searchChoiceCloseFunc);
						$("#tagSect_chzn_o_" + tagSectIndex).click(searchResultClickFunc);


						// update tag list nav, append
						appendTagNavList(newTagId, newTagName);

						// update tag edition nav, append
						appendTagsArea(newTagId, newTagName);

						// update global tags storage
						addToGlobalTags(newTagId, newTagName);

						// clear and hide
						$("#dynAddTagDiv").hide("fast");
			    	}
			    	else
			    	{
			    		// error message
						$("#dynAddTagErr").text(gettext("Failed because of server problem."));
			    	}

			    	// reset ajax flag
			    	ajaxDynAddTagFlag = AJAX_IDLE;
				}
			);
			//=========== ajax ends ===========
		}

	});
	


	// edit member submit
	$("#editModalOk").click(function(){
		// get form input
		var id = $("#editId").attr("data-value");
		var name = $("#editName").val().trim();
		var sex = $("input[name='editGender']:checked").val();
		var idcard = $("#editIDno").val().trim();
		var phone = $("#editPhone").val().trim();
		var email = $("#editEmail").val().trim();

		var groupIds = "";
		$("input[name='editGroup']:checked").each(function(){
			if(groupIds.length == 0)
			{
				groupIds += $(this).val();
			}
			else
			{
				groupIds += ("+" + $(this).val());
			}
		});

		var tagIds = "";
		$("#tagSect option:selected").each(function(){
			if(tagIds.length == 0)
			{
				tagIds += $(this).val();
			}
			else
			{
				tagIds += ("+" + $(this).val());
			}
		});

		// alert("id:" + id + "; name:" + name + "; sex:" + sex + "; idcard:" + idcard + "; phone:" + phone + "; email:" + email + "; groupIds:" + groupIds + "; tagIds:" + tagIds);

		// validation
		// ......


		// ajax flag
		if(ajaxEditMemberFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxEditMemberFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/edituser/",
				{
					"id": id,
					"name": name,
					"sex": sex,
					"idcard": idcard,
					"phone": phone,
					"email": email,
					// "location": "",  // unused now
					"groupIds": groupIds,
					"tagIds": tagIds
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// redirect
						// var curGid = $("#curGroupId").attr("data-value");
						// var curTid = $("#curTagId").attr("data-value");
						location.href = "/members/";
						// should return the page number of the person edited
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxEditMemberFlag = AJAX_IDLE;
				}
			);
		}

	});
	// ====================================
	






	// ====================================
	// delete user modal
	// ====================================
	$("a.delete-member").click(function(){
		// get data
		var target = $(this).parents("tr").find("input[type='hidden']");
		var id = target.attr("data-id");
		var name = target.attr("data-name");

		// init deleteUserDiv
		$("#deleteUserId").attr("data-value", id);
		$("#deleteUserName").text(name);

		// get current element position
		var offset = $(this).offset();
		var curTop = offset.top;
		var curLeft = offset.left;

		// get popup div width
		var width = $("#deleteUserDiv").width();

		// $(this).parents("tr").addClass("delete-alert");
		// $("#deleteUserDiv").show("fast");
		$("#deleteUserDiv").css({
			"display":"inline-block", 
			"position":"absolute",
			"top":curTop + 20, 
			"left":curLeft - width + 10
		});
		// animate......
	});
	$("#deleteUserOk").click(function(){
		var deleteUserId = $("#deleteUserId").attr("data-value");

		// ajax flag
		if(ajaxDeleteMemberFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxDeleteMemberFlag = AJAX_BUSY;

			// ajax submit
			$.post(
				"/members/deleteuser/",
				{
					"id": deleteUserId
				},
				function(data)
				{
					var result = eval("(" + data + ")");
					if(result.success == "true")
					{
						// var userId = result.id;
						$("#membersTable").find("input[type='hidden'][data-id='" + deleteUserId + "']").parent("tr").remove();

						// delete current tr or refresh???
						// update group size......
					}
					else
					{
						// error message
					}

					// reset ajax flag
					ajaxDeleteMemberFlag = AJAX_IDLE;
				}
			);

		}

		$("#deleteUserDiv").hide();
	});
	$("#deleteUserCancel").click(function(){
		$("#deleteUserDiv").hide();
	});
	$("#deleteUserHeader").find("a.close").click(function(){
		$("#deleteUserDiv").hide();
	});
	// ====================================

});