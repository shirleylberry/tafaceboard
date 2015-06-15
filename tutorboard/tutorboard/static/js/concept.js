// jQuery ajax set up from django docs for 1.5
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {

    (function ($) {
        $.fn.clickToggle = function (func1, func2) {
            var funcs = [func1, func2];
            this.data('toggleclicked', 0);
            this.on('click',function () {
                var data = $(this).data();
                var tc = data.toggleclicked;
                $.proxy(funcs[tc], this)();
                data.toggleclicked = (tc + 1) % 2;
            });
            return this;
        };
    }(jQuery));

    var $container = $('#tutorboard');

    $container.isotope({
        itemSelector: '.tutor',
        layoutMode: 'masonry',
        masonry: {
            columnWidth: 212
        },
        getSortData:{
            subject: function ($elem) {
                return $elem.find('.subject').text();
            },
            name: function ($elem) {
                return $elem.find('.name').text();
            },
            availability: function ($elem) {
                return parseInt($elem.find('.availability').text());
            },
            magic: function ($elem) {
                return parseInt($elem.find('.magic-sort-rank').text());
            },
            level: function ($elem) {
                return $elem.find('.level').text();
            }
        }
    });

    $('a.header-button').clickToggle(function () { // handle sort button function actions and css changes
            // get href attribute, minus the '#'
            var sortName = $(this).attr('href').slice(1);

            if (sortName == 'magic'){

                // Sort Decending First
                $container.isotope({
                sortBy: sortName, // first click case:ascending
                sortAscending: false
                });
            }
            else{

                // Sort Ascending First
                $container.isotope({
                sortBy: sortName, // first click case:ascending
                sortAscending: true
                });
            }
            
            $('.header-button').css('border-width', '0');
            $(this).css('border', '1px solid black');
            $('.arrowUp, .arrowDown').hide();
            $(this).find('.arrowUp').show();
            return false;
        },
        function () {
            // get href attribute, minus the '#'
            var sortName = $(this).attr('href').slice(1);
            
            if (sortName == 'magic'){

                // Sort Decending on second click
                $container.isotope({
                sortBy: sortName, // first click case:ascending
                sortAscending: true
                });
            }
            else{

                // Sort Ascending on second click
                $container.isotope({
                sortBy: sortName, // first click case:ascending
                sortAscending: false
                });
            }

            $('.header-button').css('border-width', '0');
            $(this).css('border', '1px solid black');
            $('.arrowUp, .arrowDown').hide();
            $(this).find('.arrowDown').show();
            return false;
        });

    $('#search-form').submit(function (e) {
        var formData = $(this).serialize();
        console.log(formData);
        $.post(window.location, formData, function(data) {
              $('#tutorboard').html(data);
              $container.isotope('destroy');
              $container.isotope({
                    itemSelector: '.tutor',
                    layoutMode: 'masonry',
                    masonry: {
                        columnWidth: 212
                    },
                    getSortData:{
                        subject: function ($elem) {
                            return $elem.find('.subject').text();
                        },
                        name: function ($elem) {
                            return $elem.find('.name').text();
                        },
                        availability: function ($elem) {
                            return parseInt($elem.find('.availability').text());
                        },
                        magic: function ($elem) {
                            return parseInt($elem.find('.magic-sort-rank').text());
                        },
                        level: function ($elem) {
                            return $elem.find('.level').text();
                        }
                    }
                });
        });
        e.preventDefault();
    });

    // show subject decsriptions over icons when clicked
    $('body').on('click','.subject img.icon',function(){
        var $description = $(this).next('.subject-description-container');
        $description.addClass('subject-description-visible');
        $description.show();
    });

    // If the user clicks outside of a subject description, hide visible descriptions
    $(document).mouseup(function (e)
    {
        var $descriptionBox = $(".subject-description-visible");

        if ($descriptionBox.length > 0){
            if (!$descriptionBox.is(e.target) // if the target of the click isn't the container...
                && $descriptionBox.has(e.target).length === 0) // ... nor a descendant of the container
            {
                $descriptionBox.hide();
                $descriptionBox.removeClass('subject-description-visible');
            }
        }
    });
    
    /* filtering hacks */
    $('.update-bio').parent().css('display', 'block');

}); // End of jQuery Ready
