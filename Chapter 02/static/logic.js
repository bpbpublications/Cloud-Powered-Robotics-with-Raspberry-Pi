$('#forward').on('mousedown', function(){
	$.get('/forward');
	});
$('#forward').on('mouseup', function(){
	$.get('/stop');
	});
$('#backward').on('mousedown', function(){
	$.get('/backward');
	});
$('#backward').on('mouseup', function(){
	$.get('/stop');
	});
$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});
$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});

var slider = document.getElementById("pwm");
var output = document.getElementById("speed");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
};
