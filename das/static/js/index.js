
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
    inboxList=response
    display_message_list(1,4)
    
}

function set_reply_modal(recipientAddress){
  let fromInput = document.getElementById("fromEmail");
  let toInput = document.getElementById("toEmail");

  fromInput.value="Hello@gmail.com"
  toInput.value=recipientAddress
}
function display_message_list(pagenumber, pagesize){
  let inboxDiv = document.getElementById("inbox");
   inboxDiv.innerHTML = ''
  selected=inboxList[(pagenumber-1)*pagesize];
  document.querySelectorAll('.bi-reply')[0].id=(pagenumber-1)*pagesize
    for(let i = (pagenumber-1)*pagesize; i < ((pagenumber-1)*pagesize)+pagesize; i++) {

        inboxDiv.innerHTML= inboxDiv.innerHTML + `<div id = ${i} class="card  msg_cards">
        <div  class="card-body ">
          <i class="bi bi-person-fill "></i>
          <span class="">
            ${inboxList[i].sender.name.substring(0,24)} ${inboxList[i].sender.name.length > 25?'...':''}
          </span> 
          <p class="card-text ">${inboxList[i].subject}</p>
        </div>`
        
    }
    display_message(selected);
    document.querySelectorAll('.msg_cards').forEach((item) => {
        item.addEventListener('click', (event) => {
          document.querySelectorAll('.bi-reply')[0].id=event.currentTarget.id;
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
    document.querySelectorAll('.page-item').forEach((item) => {
      item.addEventListener('click', (event) => {
        event.preventDefault();
       display_message_list(event.currentTarget.id,4)
      });
    });


    document.querySelectorAll('.bi-reply')[0].addEventListener('click', (event) => {

     set_reply_modal(inboxList[event.currentTarget.id].sender.email)
    });
  
});


