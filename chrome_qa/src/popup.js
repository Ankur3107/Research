document.addEventListener("DOMContentLoaded", function () {
    //Get Reference to Functions
    chrome.runtime.sendMessage('pageActionClicked');
  });

document.getElementById("userinput")
        .addEventListener("keyup", function(event){
          event.preventDefault();
          if (event.key === 'Enter'){
            let question = document.getElementById("userinput").value;
            chrome.runtime.sendMessage(question);
          }
})


chrome.runtime.onMessage.addListener(function(msg, _, sendResponse){
  if (msg){
    let answers = document.getElementById("answers");
    while (answers.firstChild) {
      answers.removeChild(answers.lastChild);
    }
    let elem = document.createElement("div")
    elem.className = "box"
    let list_elem = document.createElement("ol");
    list_elem.className = "list"
    for (let i=0; i < msg.length; i++){
      let list_item = document.createElement("li");
      list_item.innerText = msg[i].text;
      list_elem.className = "list-item"
      list_elem.appendChild(list_item);
    }
    let heading = document.createElement("H2")
    heading.innerText = "Answers"
    elem.appendChild(heading)
    elem.appendChild(list_elem);
    answers.appendChild(elem);
  } else{
    msg = "Could not find answers"
    let answers = document.getElementById("answers");
    let elem = document.createElement("div")
    elem.className = "box"
    elem.appendChild(document.createTextNode(msg));
    answers.appendChild(elem);
  }
  
})