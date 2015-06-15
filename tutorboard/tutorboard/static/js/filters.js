var selectedSubject = "";

function updateMagicSort() {
    $isotopeItems = $('div.filter');
    $('div.filter').each(function(index){
        // This block runs for each tutor after filtering takes place.
        // Tutors that were filtered out may still have old sortRank values
        // but Isotope will ignore them anyway.
        
        // Each catagory in the magic sort is weighted and then added to the sortRank
        var sortRank = 0;
        $sortField = $(this).find('.magic-sort-rank');
        
        // Availability
        var availabilityWeight = 1;
        var availability = parseInt($(this).find('.availability-number').text());
        sortRank += availability * availabilityWeight;
        
        // Subjects and subject levels
        $activeSubjectField = $(this).find('h3.active-subject');
        if ($activeSubjectField.hasClass('endorsed')){
            sortRank += 1000;   // Endorsed should appear at the top of the list
        }
        $sortField.text(sortRank);
    });
    
    var $container = $('#tutorboard');
    $container.isotope( 'updateSortData', $('div.tutor') );
}

$( document ).ready(function(){

	$(function() {                         // set up accordion filtering menu using accordion jquery-ui 
    $("#filtering-list").accordion({
        collapsible: true,
        heightStyle: "content"
    	});  
	});

	(function($){

		$.fn.clickFilter = function() {
			var active = $( "#filtering-list" ).accordion( "option", "active" ) + 1;        // get the current open accordion # and advance by one
    		clicked = $(this).html();                                                       // get the label of what was clicked
    		$(this).parent().parent().prev().html(clicked).addClass('selected-filter');     // set that to the text of the header
    		$( "#filtering-list" ).accordion( "option", "active", active );                 // switch to the next accordion
		};

		$.fn.selectFilter = function() {
			if ($(this).hasClass('reset-btn')) {
				$(this).siblings('.filter-select').removeClass('filter-select');
				if ($(this).hasClass('subject-btn')){
					$(this).parent().siblings().children().removeClass('filter-select')
				}
				$(this).removeClass('filter-select');
			}
			else {
				$(this).siblings('.filter-select').removeClass('filter-select');
				$(this).addClass('filter-select');	
			}
		};

		$.fn.limitFilter = function() {

			if ($(this).hasClass('area-btn')) {
				var area_id = $(this).attr('id');
				var area_filter = '.' + area_id.toLowerCase() + '-list';
				$('.subject-list').hide();
				$(area_filter).show();
				if (area_filter == '.area-reset-list') {
					$('.subject-list').show();
				}
			}

			if ($(this).hasClass('program-btn')) {
				var program_id = $(this).attr('id');
				var program_filter = '.' + program_id.toLowerCase() + '-list';
				$('.subject-list').hide();
				$(program_filter).show();
				if (program_filter == '.program-reset-list') {
					$('.subject-list').show();
				}
			}
		};

		$.fn.addFilter = function(value) {
			$(this).parent().parent().addClass('filter');
		};

		$.fn.typeFilter = function(id, type) {
			$(this).each(function(){												// Do we need this each here?
				if (type == 'area') {
					if (!($(this).find('.area').hasClass(id.toLowerCase()))) {
						$(this).removeClass('filter');
					}
				}
				if (type == 'program') {
					if (!($(this).find('.capability').hasClass(id))) {
						$(this).removeClass('filter');
					}
				}
				if (type == 'subject') {
					selectedSubject = id
				    $(this).find('.active-subject').removeClass('active-subject');
				    $(this).find('.' + id).addClass('active-subject');
					if (!($(this).find('.capability').hasClass(id))) {
						$(this).removeClass('filter');
					}
				}
				if (type == 'level') { // Level == Expert should show expert and director tutors
				    if (id.toLowerCase() == 'expert')
				    {
				        if (!($(this).find('.capability').hasClass('expert')) && !($(this).find('.capability').hasClass('director'))) {
						    $(this).removeClass('filter');
					    }
				    }
				    else
				    {
				        if (!($(this).find('.capability').hasClass(id.toLowerCase()))) {
	    					$(this).removeClass('filter');
    					}            				    
				    }
					
				}
				if (type == 'availability') {
					var anum_object = $(this).find('.availability-number').attr('id');
					if (anum_object != undefined) {
						var anum = parseInt(anum_object.split('-')[1]);
						if (id == 'one') {
							if (anum < 1) {
								$(this).removeClass('filter');
							}
						}
						if (id == 'five') {
							if ((anum < 5)) {
								$(this).removeClass('filter');
							}
						}
						if (id == 'ten') {
							if ((anum < 10)) {
								$(this).removeClass('filter');
							}
						}
						if (id == 'fifteen') {
							if (anum < 15) {
								$(this).removeClass('filter');
							}
						}
					}
				}
				if (type == 'gender') {
					if (!($(this).find('.gender').hasClass(id.toLowerCase()))) {
						$(this).removeClass('filter');
					}
				}
				if (type == 'modifier') {
					if (selectedSubject == "") {
						if (!($(this).find('.cap-mod').hasClass(id.toLowerCase()))) {
						$(this).removeClass('filter');
					}
					}
					else
					{
						if (!($(this).find('.cap-mod').hasClass(selectedSubject + '-' + id.toLowerCase()))) {
						$(this).removeClass('filter');
					}
					}
					
				}
			})
		};

		$.fn.matchFilter = function() {
			$(this).each(function(){
				var filter_id = $(this).attr('id');
				var filter_type = $(this).parent().attr('class').split('-');
				$('.tutor').typeFilter(filter_id, filter_type[0]);
			})
		};

		$.fn.resetHeaders = function() {
			$(this).each(function(){
			    var header_name = $(this).data('name');
			    $(this).html(header_name);
			})
		};

	})(jQuery);

	$('body').on('click','.filter-btn',function() {
		$(this).clickFilter();
		$(this).selectFilter();
		$(this).limitFilter();
		$('.tutor').addClass('filter');
		$('.filter-select').matchFilter();	
	    $('#tutorboard').isotope({ filter: '.filter' });
	    updateMagicSort();
	});

	$(".reset-all").click(function() {
		selectedSubject = "";
		$('.filter-select').removeClass('filter-select');
		$('.selected-filter').removeClass('selected-filter');
		$('.ui-accordion-header').resetHeaders();
		$('#filtering-list').accordion('destroy').accordion({
       		collapsible: true,
        	heightStyle: "content"
    	})
		$('.tutor').addClass('filter');
	    $('#tutorboard').isotope({ filter: '.filter' });
	    updateMagicSort();
	})
	
	updateMagicSort();
	
});
