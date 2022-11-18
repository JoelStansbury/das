function replyBtnOnclick() {
    senderEmail = document.getElementById("senderEmail");
    recipient_form_input = document.getElementById("compose-email-recipient");
    recipient_form_input.value = senderEmail.innerHTML;

    subject = document.getElementById("messageSubject");
    subject_form_input = document.getElementById("subject-text");
    subject_form_input.value = `RE ${subject.innerHTML}`;
}

function composeBtnOnclick() {
    recipient_form_input = document.getElementById("compose-email-recipient");
    recipient_form_input.value = null;

    subject_form_input = document.getElementById("subject-text");
    subject_form_input.value = null;

    subject_form_input = document.getElementById("message-text");
    subject_form_input.value = null;
}
