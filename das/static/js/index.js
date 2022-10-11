
let inboxList=[]
function call_encrypt()
{
    var path = "some path"
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", `api/encrypt/${path}`, false ); // false for synchronous request
    xmlHttp.send( null );
    resp = xmlHttp.responseText;
    el = document.getElementById("result section");
    el.innerHTML = resp
}



function get_inbox(username){
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", `api/${username}/inbox`, false ); 
    xmlHttp.send( null );
    let response = JSON.parse(xmlHttp.responseText);
    let inboxDiv = document.getElementById("inbox");
    inboxList=response
    selected=response[0];
    for(let i = 0; i <= 3; i++) {

        inboxDiv.innerHTML= inboxDiv.innerHTML + `<div id = ${i} class="card  msg_cards">
        <div  class="card-body ">
          <i class="bi bi-person-fill "></i>
          <span class="">
            ${response[i].sender.name.substring(0,24)} ${response[i].sender.name.length > 25?'...':''}
          </span> 
          <p class="card-text ">${response[i].subject}</p>
        </div>`
        
    }
    display_message(selected);

    document.querySelectorAll('.msg_cards').forEach((item) => {
        item.addEventListener('click', (event) => {
    
          event.preventDefault();
         display_message(inboxList[event.currentTarget.id])
        });
      });
}

function display_message(msgObject) {
    let name = document.getElementById("senderName");
    let email = document.getElementById("senderEmail");
    let subject = document.getElementById("messageSubject");
    let messageBody = document.getElementById("messageBody");

    name.innerText = msgObject.sender.name;
    email.innerText = msgObject.sender.email;
    subject.innerText = msgObject.subject;
    messageBody.innerText = msgObject.body;

   
}
window.addEventListener('DOMContentLoaded', (event) => {
    get_inbox("veronica");
});

