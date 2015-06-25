function checkboxChange() {
    var $clickedCheckBox = $(this);
    var $parentLabel = $clickedCheckBox.parent();
    var $checkResult = $parentLabel.nextAll(".checkResult");
    var $subject_update_model = $parentLabel.parent(".subject-update-model");
    var $formContainer = $parentLabel.nextAll('.capability-form-container');

    var subID = $parentLabel.nextAll(".hiddenSub").val();
    if (!subID) {
        subID = -1;
    }
    var capID = $parentLabel.nextAll(".hiddenCap").val();
    if (!capID) {
        capID = -1;
    }

    var check_unchecked = ! $(this).is(":checked");

    if(check_unchecked){
        // ask if they want to delete the capability
        if(confirm('Do you want to remove this subject for this tutor?')){
            // Delete capability
            var capID = $formContainer.find('input.form-instance-id').val();
            $.post('/capability/' + capID + '/delete/', {}, function (data) {
                console.log(data);

            });
            $formContainer.html('');
        }

    }
    else{
        $.get("/capability/create/", function (data) {

            var subjectID = $clickedCheckBox.parent().next('.hiddenSub').val();

            $($formContainer).html(data);
            $formContainer.find("input[name='tutor']").val(django_context.tutor_id);
            $formContainer.find("input[name='subject']").val(subjectID);
        });
    }


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

function saveCapability(data){
    event.preventDefault();

    var $capabilityForm = $(this);
    var $formContainer = $capabilityForm.parent('.well').parent('.capability-form-container');
    var formData = {};
    $capabilityForm.serializeArray().map(function(x){formData[x.name] = x.value;}); // Converts the form data into a dictionary

    $formContainer.html('<img src="/static/img/spinner.gif"><div style="height:191px;"></div>');

    if (formData.id == 'None'){
        $.post("/capability/create/", formData, function (data) {
            console.log(data);
            $formContainer.html(data); // replace the form with the updated form provided by this view
        });
    }
    else{
        $.post("/capability/" + formData.id + "/", formData, function (data) {
            $formContainer.html(data); // replace the form with the updated form provided by this view
        });
    }

}

$(document).ready(function () {
    if($('html').is('.tutor_update')){
        $(document).on('change', '.checkboxSub', checkboxChange);
        $("#id_cell").blur(fixPhoneNumber);
        $("#id_altphone").blur(fixPhoneNumber);
        $( "body" ).on('submit', '.capability-form', saveCapability);
    }
});