$(function(){
	$('#btnUrlCheck').click(function(){
		
		$.ajax({
			url: '/url-check',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});