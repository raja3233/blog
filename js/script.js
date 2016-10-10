$(document).ready(function(){
	run_slides();
})
function run_slides(){
	var slide_index = 1;
	
	setInterval(function(){
	var slides_length = $('.slides').length;
	if (slide_index > slides_length){
		slide_index = 1;
	}
	if (slide_index < -1){
		slide_index = slides_length;
	}
	$.each($('.slides'),function(){
		 $(this).hide();
	});
	var img = $('.slides').get(slide_index - 1);
	$(img).show(2000);
	slide_index = slide_index + 1;
}, 3000);
	
}