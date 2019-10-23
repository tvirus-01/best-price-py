$('.list_pr').hide();
var show_all = "<?php echo $show_all ?>";
if (show_all == true) {	
	$('.list_pr').hide();
	x = 3;
	$('.list_pr:lt('+x+')').show();
}else{
	$('.list_pr').show();
}