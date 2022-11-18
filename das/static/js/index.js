
let inboxList = []

function get_inbox(account_idx, folder_name, page_num) {
  // TEMPORARY VALUES
  account_idx = call_get_accounts()[1][1] // may need to swap this with 0
  folder_name = "Inbox"
  page_num = 0
  console.log(account_idx);
  console.log(folder_name);
  let xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", `api/getfolder/${account_idx}/${folder_name}?page=${page_num}`, false);
  xmlHttp.send(null);
  let response = JSON.parse(xmlHttp.responseText);
  let inboxDiv = document.getElementById("inbox");
  inboxList = response
  selected = response[0];
  for (let i = 0; i <= response.length - 1; i++) {

    inboxDiv.innerHTML = inboxDiv.innerHTML + `<div id = ${i} class="card  msg_cards">
        <div  class="card-body ">
          <i class="bi bi-person-fill "></i>
          <span class="">
            ${response[i].sender.name.substring(0, 24)} ${response[i].sender.name.length > 25 ? '...' : ''}
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

function call_get_accounts() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", `/api/getaccounts`, false); // false for synchronous request
  xmlHttp.send(null);
  resp = JSON.parse(xmlHttp.responseText);
  console.log(resp);
  return resp;
}

window.addEventListener('DOMContentLoaded', (event) => {
  get_inbox("veronica");
});

