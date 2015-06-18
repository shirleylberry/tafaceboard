function checkboxChange() {
    var $clickedCheckBox = $(this);
    var $parentLabel = $clickedCheckBox.parent();
    var $checkResult = $parentLabel.nextAll(".checkResult");
    var $subject_update_model = $parentLabel.parent(".subject-update-model");

    var subID = $parentLabel.nextAll(".hiddenSub").val();
    if (!subID) {
        subID = -1;
    }
    var capID = $parentLabel.nextAll(".hiddenCap").val();
    if (!capID) {
        capID = -1;
    }

    var checkedAction = '';

    if ($(this).is(":checked")) {
        checkedAction = 'checked';
    }
    else {
        checkedAction = 'unchecked';
    }

    $($clickedCheckBox).replaceWith('<img src="/static/img/spinner.gif">');

    var postData = {subjectID: subID, capabilityID: capID, checked: checkedAction};

    $.post("/tutorboard/"+ django_context.tutor_id +"/update/ajax/subjectlist/", postData, function (data) {
        $($subject_update_model).replaceWith(data);
        //$('.checkboxSub').off();
        //$('.checkboxSub').change(checkboxChange);
        //$('.subUpdateSubmit').off();
        //$('.subUpdateSubmit').click(subjectUpdateSubmit);
    });
}

function subjectUpdateSubmit(event) {
    // Do ajax submit
    var $form = $(this).parent("form");

    var subID = $form.parent(".capability-form").prevAll(".hiddenSub").val();
    if (!subID) {
        subID = -1;
    }

    var capID = $form.parent(".capability-form").prevAll(".hiddenCap").val();
    if (!capID) {
        capID = -1;
    }

    var checkedAction = '';

    $(this).replaceWith('<img src="/media/images/spinner.gif">');

    $.post("/tutorboard/"+ django_context.tutor_id +"/update/ajax/subjectlist/", $form.serialize(), function (data) {
        $form.parent('.capability-form').parent('.subject_update_model').replaceWith(data);
        $('.checkboxSub').off().change(checkboxChange);
        $('.subUpdateSubmit').off().click(subjectUpdateSubmit);
    });
    event.preventDefault();
    return false;
}

function fixPhoneNumber() {
    var newnum = new String();
    var rawnum = $(this).val();
    rawnum = rawnum.replace(/[\D]/g, '');
    if (rawnum.length != 10) {
        alert("Please enter a 10-digit phone number")
    }
    else {
        newnum = newnum.concat(rawnum.substr(0, 3), ".", rawnum.substr(3, 3), ".", rawnum.substr(6, 4));
        $(this).val(newnum);
    }
}

$(document).ready(function () {
    if($('html').is('.tutor_update')){
        $.get("/tutorboard/"+ django_context.tutor_id +"/update/ajax/subjectlist/", function (data) {
            $("#subjectList").html(data);
            $(document).on('change', '.checkboxSub', checkboxChange);
            $('.subUpdateSubmit').click(subjectUpdateSubmit);
        });

        $("#id_cell").blur(fixPhoneNumber);
        $("#id_altphone").blur(fixPhoneNumber);
    }
});