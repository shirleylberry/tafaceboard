$( document ).ready(function(){
	
	//Shirley's expand extra info
	$( 'body' ).on('click','.picture-area', function(){
		var currentTutor = $(this).closest(".tutor");
		$(currentTutor).children( ".info-extra" ).toggle();
		$(currentTutor).toggleClass( "expand" );
		$( "#tutorboard" ).isotope('reLayout');
	});
	//Cameron's unexpand all tutors reset button
	$('body').on('click', '.reset-all',function(){
        $(".info-extra").hide();
        $(".expand").removeClass("expand")
	}); 
	//Thomas' hide tutors button
	$('body').on('click', '.hide-button img', function(e) {
        var $tutorElement = $(this).closest(".tutor");
        $( "#tutorboard" ).isotope('remove',$tutorElement,function(){});
    }); 
	
	 
});

