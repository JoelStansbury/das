function populate_folder_menus() {

    folders_div = document.getElementById("folder_selection_div");
    folders_div.innerHTML = "";
    FOLDERS.forEach(element => {
        folders_div.innerHTML += `
            <div class="card folder_cards" value="${element}">
                <div class="card-body">${element}</div>
            </div>
        `
    });
    document.querySelectorAll('.folder_cards').forEach(
        (item) => {
            item.addEventListener(
                'click', 
                (event) => {
                    event.preventDefault();
                    clear_email_viewer();
                    SELECTED_FOLDER = item.getAttribute("value")
                    populate_email_list();
                }
            );
        }
    );
}


function populate_email_list() {
    get_emails();
    inboxDiv = document.getElementById("inbox");
    inboxDiv.innerHTML = "";
    console.log(EMAILS_LIST);
    i = 0
    EMAILS_LIST.forEach(e => {
        inboxDiv.innerHTML += `
            <div id = ${i} class="card  msg_cards">
                <div  class="card-body ">
                    <i class="bi bi-person-fill "></i>
                    <span class="">
                        ${e.sender.name.substring(0, 24)} ${e.sender.name.length > 25 ? '...' : ''}
                    </span> 
                <p class="card-text ">${e.subject}</p>
            </div>
        `
        i+=1
    });

    document.querySelectorAll('.msg_cards').forEach((item) => {
        item.addEventListener('click', (event) => {
            event.preventDefault();
            console.log(EMAILS_LIST);
            display_message(EMAILS_LIST[item.id]);
        });
    });
}


function display_message(msgObject) {
    if (msgObject) {
      let name = document.getElementById("senderName");
      let email = document.getElementById("senderEmail");
      let subject = document.getElementById("messageSubject");
      let messageBody = document.getElementById("messageBody");
  
      name.innerText = msgObject.sender.name;
      email.innerText = msgObject.sender.email;
      subject.innerText = msgObject.subject;
      messageBody.innerText = msgObject.body;
    }
}


function clear_email_viewer() {
    let name = document.getElementById("senderName");
    let email = document.getElementById("senderEmail");
    let subject = document.getElementById("messageSubject");
    let messageBody = document.getElementById("messageBody");

    name.innerText = "";
    email.innerText = "";
    subject.innerText = "";
    messageBody.innerText = "";
}

function populate_accounts_dropdown() {
    account_selector = document.getElementById("account_selector");
    account_selector.innerHTML = ""
    ACCOUNTS.forEach(acc => {
        account_selector.innerHTML += `
            <option value=${acc}>${acc}</option>
        `
    });
}