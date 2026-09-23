
let messages = []
async function getMessages() {
    const response = await fetch('/get-messages')
    const data = await response.json()
    messages = data;
}

let currentUserId = null;
async function getCurrentUserId(){
    const response = await fetch('/current-user');
    const data = await response.json();
    console.log(data);
    currentUserId = data.user_id;
}

const messageContainer = document.querySelector('.message-container');
function createMessage(userId, name, message){
    const messageBox = document.createElement('div');
    messageBox.classList.add('message-box')
    if (userId == currentUserId){
        messageBox.classList.add('you')
    }

    const nameTag = document.createElement('p');
    nameTag.classList.add('name')
    nameTag.innerText = name;

    const messageTag = document.createElement('p');
    messageTag.classList.add('message')
    messageTag.innerText = message;

    messageBox.appendChild(nameTag);
    messageBox.appendChild(messageTag);

    messageContainer.appendChild(messageBox);
    
}

async function loadMessages(){
    await getCurrentUserId()
    for (const msg of messages){
        createMessage(msg.user_id, msg.name, msg.message)
    }
}
getMessages();
loadMessages();
