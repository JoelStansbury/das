ACCOUNTS = []
FOLDERS = []
EMAILS_LIST = []
SELECTED_ACCOUNT = 0
SELECTED_FOLDER = ""

function select_account() {
  account_selector = document.getElementById("account_selector");
  if (account_selector.value) {
    SELECTED_ACCOUNT = account_selector.value;
    console.log(SELECTED_ACCOUNT);
    FOLDERS = get_folders();
    populate_folder_menus();
    SELECTED_FOLDER = FOLDERS[0];
    populate_email_list();
  }
  
}

function get_emails(page_num=0) {
  try {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", `api/getfolder/${SELECTED_ACCOUNT}/${SELECTED_FOLDER}?page=${page_num}`, false);
    xmlHttp.send(null);
    console.log(xmlHttp.responseText);
    EMAILS_LIST = JSON.parse(xmlHttp.responseText);
  } catch(err) {
    console.log(err);
    EMAILS_LIST = [];
  }
}

function get_accounts() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", `/api/getaccounts`, false); // false for synchronous request
  xmlHttp.send(null);
  resp = JSON.parse(xmlHttp.responseText);
  console.log(resp);
  return resp;
}

function get_folders() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", `/api/getfolders/${SELECTED_ACCOUNT}`, false); // false for synchronous request
  xmlHttp.send(null);
  resp = JSON.parse(xmlHttp.responseText);
  return resp;
}

window.addEventListener('DOMContentLoaded', (event) => {
  ACCOUNTS = get_accounts();
  populate_accounts_dropdown();
  FOLDERS = get_folders();
  populate_folder_menus();
  SELECTED_FOLDER = FOLDERS[0];
  populate_email_list();


  // AUTOFILL COMPOSE MODAL
  var replyBtn = document.getElementById("replyBtnID");
  if (replyBtn) {
    replyBtn.addEventListener('click', (event) => {
      replyBtnOnclick();
    }
    );
  }

  var composeBtn = document.getElementById("composeBtnID");
  if (composeBtn) {
    composeBtn.addEventListener('click', (event) => {
      composeBtnOnclick();
    }
    );
  }
});
