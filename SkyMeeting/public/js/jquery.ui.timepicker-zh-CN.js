jQuery(function($){  
	$.timepicker.regional['zh-CN'] = {
		timeOnlyTitle: '选择时间',
		timeText: '时间',
		hourText: '时',
		minuteText: '分',
		secondText: '秒',
		millisecText: '微秒',
		timezoneText: '时区',
		currentText: '现在时间',
		closeText: '完成',
		timeFormat: 'hh:mm',
		amNames: ['AM', 'A'],
		pmNames: ['PM', 'P'],
		ampm: false
	};
	$.timepicker.setDefaults($.timepicker.regional['zh-CN']);
});  