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

    body_form_input = document.getElementById("message-text");
    body_form_input.value = null;
}

function send() {
    recipient = document.getElementById("compose-email-recipient").value;
    subject = document.getElementById("subject-text").value;
    body = document.getElementById("message-text").value;
    console.log(body);

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", `api/send/${SELECTED_ACCOUNT}`, false ); // false for synchronous request
    xmlHttp.send( 
        JSON.stringify({
            "to":recipient,
            "body":body,
            "subject":subject,
        })
     );
    resp = xmlHttp.responseText;
}