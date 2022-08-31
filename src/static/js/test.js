alert( 'Hello, from javascript!' );
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