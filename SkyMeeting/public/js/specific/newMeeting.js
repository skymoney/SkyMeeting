$(function() {
	// ===============================
	// initialization
	// ===============================
	selectNavItem("meetings");

	// init datetime picker
	$("#startDatetime").datetimepicker({
		showMonthAfterYear: true,
        // changeMonth: true, 
        // changeYear: true, 
		minDate: '-2y', maxDate: '+2y', 
		dateFormat: 'yy/mm/dd',

        // showSecond: true,
        timeFormat: 'hh:mm',
        stepHour: 1,
        stepMinute: 1,
        stepSecond: 1
    });

    // init KindEditor
    var editor;
	KindEditor.ready(function(K) {
		editor = K.create('textarea[id="inputDetail"]', {
			resizeType : 1,
			allowPreviewEmoticons : false,
			allowImageUpload : false,
			items : [
				'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
				'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
				'insertunorderedlist', '|', 'emoticons', 'image', 'link']
		});
	});

	// init KindEditor content when edit-mode
	// lazy load
	setTimeout(function(){
		var dataElem = $("#detailDiv");
		// if in edit-mode
		if(dataElem.length != 0)
		{
			$("#inputDetail").siblings(".ke-container").find("iframe").contents().find("body").html(dataElem.html());
		}
	}, 500);


    // 有问题???阻止点击背景关闭
    /*$("#participantModal").on("show", function(){
    	// alert("a");
    	$(".modal-backdrop fade in").unbind("click");
    });*/

    // 表单验证框架 略弱!!!
    // $.fn.validations.options.validateOn = "";
    $("#meetingForm").validations();
	// ===============================





	// constants
	var AJAX_IDLE = 0;
	var AJAX_BUSY = 0;

	// ajax flags
	var ajaxQueryPersonFlag = AJAX_IDLE;

	// global storage
	// format: [{id, name}, ...]
	var globalSelectedPersons = new Array();
	// format: [{fileId, fileName}, ...]
	var globalBindedFiles = new Array();

	// util functions of global storage
	/* return true if not duplicate and add successfully */
	var addToGlobalSelectedPersons = function(id, name){
		var found = false;
		for(var i=0; i<globalSelectedPersons.length; i++)
		{
			if(globalSelectedPersons[i].id == id)
			{
				found = true;
				break;
			}
		}

		if(found == false)
		{
			globalSelectedPersons.push((eval("({\"id\":" + id + ",\"name\":\"" + name + "\"})")));
			return true;
		}
		return false;
	};
	var removeFromGlobalSelectedPersons = function(id){
		for(var i=0; i<globalSelectedPersons.length; i++)
		{
			if(globalSelectedPersons[i].id == id)
			{
				globalSelectedPersons.splice(i, 1);
				break;
			}
		}
	}
	var addToGlobalBindedFiles = function(fileId, fileName){
		globalBindedFiles.push((eval("({\"fileId\":" + fileId + ",\"fileName\":\"" + fileName + "\"})")));
	};
	var removeFromGlobalBindedFiles = function(fileId){
		for(var i=0; i<globalBindedFiles.length; i++)
		{
			if(globalBindedFiles[i].fileId == fileId)
			{
				globalBindedFiles.splice(i, 1);
				break;
			}
		}
	}

	// ************************************
	// init global storage when edit-mode
	// ************************************
	$("#personList").children(".person").each(function(){
		var dataElem = $(this).find("input[type='hidden']");
		addToGlobalSelectedPersons(dataElem.attr("data-id"), dataElem.attr("data-name"));
	});
	$("#uploadMsg").children(".file").each(function(){
		var dataElem = $(this).find("input[type='hidden']");
		addToGlobalBindedFiles(dataElem.attr("data-fid"), dataElem.attr("data-fname"));
	});
	// ************************************





	// ===============================
	// participants modal
	// ===============================
	/*
		return value:
			"" if no tags selected,
			"1+2+3" etc.
	*/
	var getSelectedTagIds = function(){
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
		return tagIds;
	};

	/*
		query persons with group, tags and page number
	*/
	var queryPersonList = function(gid, tid, page){
		// alert(gid + " " + tid);
		// ajax flag
		if(ajaxQueryPersonFlag == AJAX_IDLE)
		{
			// set ajax flag
			ajaxQueryPersonFlag = AJAX_BUSY;

			// ajax submit
			$.get(
				"/members/queryperson/",
				{
					"gid": gid,
					"tid": tid,
					"pn": page
				},
				function(data)
				{
					var result = eval("(" + data + ")");

					// deal with persons
					var persons = result.roleList;
					var personsTarget = $("#personAjaxDiv");
					personsTarget.empty();

					for(var i=0; i<persons.length; i++)
					{
						var code = "<label class=\"checkbox\">";
						code += "<div class=\"checker\">";
						code += "<span>";
						code += "<input type=\"checkbox\" name=\"selectPerson\" value=\"" + persons[i].id + "\" />";
						code += "</span></div>";
						code += persons[i].name;
						code += "</label>";
						personsTarget.append(code);
					}

					// bind checkbox event
					personsTarget.find("div.checker input").bind("click", checkerClickFunc);
					personsTarget.find("div.checker input").bind("click", notAllClickFunc);



					// deal with pagination
					var pn = result.pn;
					var tpn = result.tpn;
					var paginationTarget = $(".pagination").find("ul");
					paginationTarget.empty();
					
				    // previous page
				    var code = "";
				    if(pn == 1)
				    {
				    	code += "<li class=\"disabled\">";
				    }
				    else
				    {
				    	code += "<li>";
				    }
				    code += "<a href=\"javascript:void(0);\" id=\"prePage\">←&nbsp;" + gettext("Previous") + "</a>";
				    code += "</li>";
				    paginationTarget.append(code);

				    // page number list
				    for(var i=1; i<=tpn; i++)
				    {
				    	code = "";
				    	if(i == pn)
				    	{
				    		code += "<li class=\"active\">";
				    	}
				    	else
				    	{
				    		code += "<li>";
				    	}
				    	code += "<a href=\"javascript:void(0);\" class=\"page\" data-page=\"" + i + "\">" + i + "</a>";
				    	code += "</li>";
				    	paginationTarget.append(code);
				    }

				    // next page
				    code = "";
				    if(pn == tpn)
				    {
				    	code += "<li class=\"disabled\">";
				    }
				    else
				    {
				    	code += "<li>";
				    }
				    code += "<a href=\"javascript:void(0);\" id=\"nextPage\">" + gettext("Next") + "&nbsp;→</a>";
				    code += "</li>";
				    paginationTarget.append(code);

				    // bind pagination event
				    // NOTE: 代码不够好，有递归嫌疑!!!
				    $(".pagination").find("a.page").click(function(){
		    			// only when page changed
						if($(this).parent("li").hasClass("active") == false)
						{
							var thisPage = $(this).attr("data-page");
							queryPersonList(gid, tid, thisPage);
						}
				    });
			    	$("#prePage").click(function(){
						$(".pagination").find("li.active").prev().find("a.page").click();
					});
					$("#nextPage").click(function(){
						$(".pagination").find("li.active").next().find("a.page").click();
					});



				    // all done
					// reset ajax flag
					ajaxQueryPersonFlag = AJAX_IDLE;
				}
			);
		}
	};

	// ========== refresh person list ==========
	$("a.group").click(function(){
		// toggle class
		$(this).parent("li").siblings("li").each(function(){
			$(this).removeClass("active");
		});
		$(this).parent("li").addClass("active");

		// clear all selected tags
		$("a.tag-selected").each(function(){
			$(this).removeClass("tag-selected");
		});

		// get params
		var gid = $(this).attr("data-gid");
		var tagIds = getSelectedTagIds();

		queryPersonList(gid, tagIds, 1);
	});

	$("a.tag").click(function(){
		// toggle class
		if($(this).hasClass("tag-selected"))
		{
			$(this).removeClass("tag-selected");
		}
		else
		{
			$(this).addClass("tag-selected");
		}

		// get params
		var gid = $("#groupList").find("li.active").find("a.group").attr("data-gid");
		var tagIds = getSelectedTagIds();

		queryPersonList(gid, tagIds, 1);
	});


	// ========== checkbox event ==========
	var notAllClickFunc = function(){
		if(isCheckboxChecked($(this)) == false)
		{
			checkboxCancel($("#selectAllPerson"));
		}
	}

	$("#selectAllPerson").click(function(){
		if(isCheckboxChecked($(this)))
		{
			// check all persons
			$("#personAjaxDiv").find(".checker").each(function(){
				checkerCheck($(this));
			});
		}
		else
		{
			// cancel all persons
			$("#personAjaxDiv").find(".checker").each(function(){
				checkerCancel($(this));
			});
		}
	});


	// ========== modal submission ==========
	var removePersonFunc = function(){
		var id = $(this).attr("data-id");
		$(this).parent(".person").remove();

		// update global storage
		removeFromGlobalSelectedPersons(id);
	};
	$("a.remove-person").click(removePersonFunc);

	$("#addParticipantLink").click(function(){
		// back to default page
		// NOTE: extra query!!!
		$("#groupList").children("li").first().find("a.group").click();

		// clear checkAll
		if(isCheckboxChecked($("#selectAllPerson")))
		{
			$("#selectAllPerson").click();
		}

		$("#participantModal").modal("show");
	});

	$("#participantModalOk").click(function(){
		// flag only if select any one person
		var isChecked = false;

		$("#personAjaxDiv").find("input[name='selectPerson'][checked='checked']").each(function(){
			isChecked = true;

			// get data
			var id = $(this).val();
			var name = $(this).parents("label").text();

			// update global storage
			var result = addToGlobalSelectedPersons(id, name);
			if(result == true)
			{
				// add to personList
				$("#personList").append(
					"<div class=\"person\">" + 
						"<span class=\"person-name\">" + name + "</span>" + 
						"<a href=\"javascript:void(0);\" class=\"remove-person\" data-id=\"" + id + "\">&nbsp;x</a>" + 
					"</div>");

				// bind event
				$("#personList").children(".person").last().find("a.remove-person").bind("click", removePersonFunc);
			}
		});

		if(isChecked)
		{
			// clear error message
			$("#participantsError").hide();
		}

		$("#participantModal").modal("hide");
	});
	// ===============================





	// ===============================
	// file upload
	// ===============================
	var removeFileFunc = function(){
		var fid = $(this).attr("data-fid");
		$(this).parent(".file").remove();

		// update global storage
		removeFromGlobalBindedFiles(fid);
		// ajax to delete file in server???
	}
	$("a.remove-file").click(removeFileFunc);

    $fub = $('#fineUploader');
    $messages = $('#uploadMsg');
 
    var uploader = new qq.FineUploaderBasic({
    	multiple: false,
		button: $fub[0],
		request: {
     		endpoint: '/upfile/'
      	},
      	/*validation: {
      		allowedExtensions: ['jpeg', 'jpg', 'gif', 'png', 'pdf', 'docx', 'doc', 'pptx', 'ppt', 'xlsx', 'xls', 'txt', 'rar'],
        	sizeLimit: 104857600 // 100 MB = 100 * 1024 * 1024 bytes
      	},*/
        /*deleteFile: {
            enabled: true,
            endpoint: '/upfile/',
            forceConfirm: true
        },*/
      	callbacks: {
        	onSubmit: function(id, fileName) {
	          	$messages.append('<div id="file-' + id + '" class="file alert"></div>');
	          	// disable form submit button
	          	disableButton($("#meetingFormOk"));
	        },
        	onUpload: function(id, fileName) {
          		$('#file-' + id).addClass('alert-info')
               		.html('<img src="../public/img/loading.gif" alt=' + gettext("Initializing. Please hold.") + '/> <span>' + gettext("Initializing") + ' “' + fileName + '”</span>');
       		},
        	onProgress: function(id, fileName, loaded, total) {
          		if (loaded < total) {
            		progress = Math.round(loaded / total * 100) + '% of ' + Math.round(total / 1024) + ' kB';
            		$('#file-' + id).removeClass('alert-info')
                            .html('<img src="../public/img/loading.gif" alt=' + gettext("In progress. Please hold.") + '/> <span>' + gettext("Uploading") + ' “' + fileName + '” ' + progress + '</span>');
          		} else {
            		$('#file-' + id).addClass('alert-info')
                            .html('<img src="../public/img/loading.gif" alt=' + gettext("Saving. Please hold.") + '/> <span>' + gettext("Saving") + ' “' + fileName + '”</span>');
          		}
        	},
        	onComplete: function(id, fileName, responseJSON) {
        		var result = responseJSON[0];
          		if(result.success == "true")
          		{
            		$('#file-' + id).removeClass('alert-info')
                            .addClass('alert-success')
                            .html('<i class="icon-ok"></i> <span>' + gettext("Successfully saved") + ' “' + fileName + '”</span>' + 
                            		'<a href="javascript:void(0);" class="remove-file pull-right" data-fid="' + result.fileId + '">' + gettext("Remove") + '</a>');

                	// bind event
                	$('#file-' + id).find("a.remove-file").bind("click", removeFileFunc);
               		// update global storage
               		addToGlobalBindedFiles(result.fileId, fileName);
          		}
          		else
          		{
            		$('#file-' + id).removeClass('alert-info')
                            .addClass('alert-error')
                            .html('<i class="icon-exclamation-sign"></i> <span>' + gettext("Error with") + ' “' + fileName + '”</span>');
          		}

          		enableButton($("#meetingFormOk"));
        	}
      	}
    });

	// upload cancel and file cancel???
	// ===============================





	// ===============================
	// form submission
	// ===============================
	$("#typeSct").change(function(){
		/*if($(this).find("option:selected").val() == -1)
		{
			$("#typeSctError").show();
		}
		else
		{
			$("#typeSctError").hide();
		}*/
		$("#typeSctError").hide();
	});

	/*$(".ke-container").find("iframe").contents().find("body").keypress(function(){
		alert("A");
		if($(this).html().length != 0)
		{
			$("#inputDetailError").hide();
		}
	});*/

	$("#meetingFormCancel").click(function(){
		// redirect to meetings page
		location.href = "/meetings/";
	});

	$("#meetingFormOk").click(function(){
		// clear all errors
		$("#meetingForm").find(".alert-error").each(function(){
			$(this).hide();
		});
		
		// $("#inputTitle").parents(".control-group").addClass("error");
		// $("#inputTitle").focus();
		// $("#inputTitleError").removeClass("hide");

		// basic info
		var title = $("#inputTitle").val().trim();
		var type = $("#typeSct").find("option:selected").val();
		var startTime = $("#startDatetime").val();
		var place = $("#inputPlace").val().trim();
		var tel = $("#inputTel").val().trim();
		var email = $("#inputEmail").val().trim();

		if(type == -1)
		{
			$("#typeSctError").show();
			$("#typeSct").focus();
			return false;
		}

		// detail info
		var detail = $("#inputDetail").siblings(".ke-container").find("iframe").contents().find("body").html();
		// NOTE: length == 0 很不精确，比如按一个回车!!!
		if(detail.length == 0)
		{
			$("#inputDetailError").css("display", "inline-block");
			$(".ke-container").find("iframe").contents().find("body").focus();
			return false;
		}

		// participants
		if(globalSelectedPersons.length == 0)
		{
			$("#participantsError").css("display", "inline-block");
			return false;
		}

		var participants = globalSelectedPersons[0].id;
		for(var i=1; i<globalSelectedPersons.length; i++)
		{
			participants += "+" + globalSelectedPersons[i].id;
		}

		// files
		var files = "";
		for(var i=0; i<globalBindedFiles.length; i++)
		{
			if(i != 0)
			{
				files += "+";
			}
			files += globalBindedFiles[i].fileId;
		}


		// ajax flag!!! disable button
		disableButton($("#meetingFormOk"));
		$("#meetingFormOk").val(gettext("Saving..."));

		// ajax params
		var params = {
				"title": title,
				"type": type,
				"startTime": startTime,
				"place": place,
				"tel": tel,
				"email": email,
				"detail": detail,
				"participants": participants,
				"files": files
			};

		// meeting id not empty when edit-mode
		var mid = $("#meetingData").attr("data-mid");
		if(mid.length > 0)
		{
			params["mid"] = mid
		}

		// ajax submit
		$.post(
			"/savemeeting/",
			params,
			function(data)
			{
				var result = eval("(" + data + ")");
				if(result.success == "true")
				{
					// redirect to meeting page
					location.href = "/meeting/?mid=" + result.mid;
				}
				else
				{
					// error message
				}

				// reset ajax flag!!! enable button
				enableButton($("#meetingFormOk"));
				$("#meetingFormOk").val(gettext("Save"));
			}
		);

	});
	// ===============================

});