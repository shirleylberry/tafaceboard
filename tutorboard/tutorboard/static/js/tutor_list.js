
$(document).ready(function () {
    if($('html').is('.tutor_list')) {
        var $body = $('body');

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

        $('.lazy-img').imageloader();


        var $container = $('#tutorboard');
        $container.isotope({
            itemSelector: '.tutor',
            layoutMode: 'masonry',
            masonry: {
                columnWidth: 212
            },
            getSortData: {
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

                if (sortName == 'magic') {

                    // Sort Decending First
                    $container.isotope({
                        sortBy: sortName, // first click case:ascending
                        sortAscending: false
                    });
                }
                else {

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

                if (sortName == 'magic') {

                    // Sort Decending on second click
                    $container.isotope({
                        sortBy: sortName, // first click case:ascending
                        sortAscending: true
                    });
                }
                else {

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

        // Search Submit
        $('#search-form').submit(function (e) {
            var formData = $(this).serialize();
            console.log(formData);
            $.post(window.location, formData, function (data) {
                $('#tutorboard').html(data);
                $container.isotope('destroy');
                $container.isotope({
                    itemSelector: '.tutor',
                    layoutMode: 'masonry',
                    masonry: {
                        columnWidth: 212
                    },
                    getSortData: {
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

        /* filtering hacks */
        $('.update-bio').parent().css('display', 'block');

        // Expand extra info
        $body.on('click', '.picture-area', function () {
            var currentTutor = $(this).closest(".tutor");
            $(currentTutor).children(".info-extra").toggle();
            $(currentTutor).toggleClass("expand");
            $("#tutorboard").isotope('reLayout');
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
    }
}); // End of jQuery Ready
