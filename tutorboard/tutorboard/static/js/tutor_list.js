var $body, $container;
var currentPage = 1;
var loadReady = false;

function loadTutors(){
    $('#scroller .scroller-message').html('Loading tutors');
    $('#scroller .scroller-image').show();
    var getURL = '/list/page' + currentPage +'/';
    $.ajax({
        url: getURL,
        data: $('#filter-form').serialize(),
        type: 'get',
        error: function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Error while loading tutors:');
            console.log(textStatus);
            console.log(errorThrown);
            if (errorThrown.trim() == "NOT FOUND"){
                $('#scroller .scroller-message').html('End of tutor list');
                $('#scroller .scroller-image').hide();
            }
        },
        success: function(data){
            currentPage++;

            var $items = $(data);
            $container.append($items)
                .isotope('appended', $items);

            $('.lazy-img').imageloader();
            loadReady = true;

            $('#scroller .scroller-message').html('Scroll to load more tutors');
            $('#scroller .scroller-image').hide();
        }
    });
}

$(document).ready(function () {
    if($('html').is('.tutor_list')) {
        $body = $('body');

        $container = $('#tutorboard');
        $container.isotope({
            itemSelector: '.tutor',
            layoutMode: 'masonry',
            masonry: {
                columnWidth: 212
            }
        });

        $.fn.clickToggle = function (func1, func2) {
            var funcs = [func1, func2];
            this.data('toggleclicked', 0);
            this.on('click', function () {
                var data = $(this).data();
                var tc = data.toggleclicked;
                $.proxy(funcs[tc], this)();
                data.toggleclicked = (tc + 1) % 2;
            });
            return this;
        };

        // show subject decsriptions over icons when clicked
        $body.on('click', '.subject img.icon', function () {
            var $description = $(this).next('.subject-description-container');
            $description.addClass('subject-description-visible');
            $description.show();
        });

        // If the user clicks outside of a subject description, hide visible descriptions
        $(document).mouseup(function (e) {
            var $descriptionBox = $(".subject-description-visible");

            if ($descriptionBox.length > 0) {
                if (!$descriptionBox.is(e.target) // if the target of the click isn't the container...
                    && $descriptionBox.has(e.target).length === 0) // ... nor a descendant of the container
                {
                    $descriptionBox.hide();
                    $descriptionBox.removeClass('subject-description-visible');
                }
            }
        });

        // filtering hacks
        $('.update-bio').parent().css('display', 'block');

        // Expand extra info
        $body.on('click', '.picture-area', function () {
            var currentTutor = $(this).closest(".tutor");
            $(currentTutor).children(".info-extra").toggle();
            $(currentTutor).toggleClass("expand");
            $container.isotope('layout');
        });
        // Unexpand all tutors reset button
        $body.on('click', '.reset-all', function () {
            $(".info-extra").hide();
            $(".expand").removeClass("expand")
        });

        // Hide tutors button
        $body.on('click', '.hide-button img', function (e) {
            var $tutorElement = $(this).closest(".tutor");
            $("#tutorboard").isotope('remove', $tutorElement, function () {
            });
        });

        $(window).scroll($.throttle( 250, function() {
            if(loadReady){
                if (document.documentElement.clientHeight +
                    $(document).scrollTop() >= document.body.offsetHeight )
                {
                    loadReady = false;
                    loadTutors();
                }
            }

        }));

        loadTutors();
    }
}); // End of jQuery Ready
