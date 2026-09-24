

const socketio = io();
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
    currentUserId = data.user_id;
}

const messageContainer = document.querySelector('.message-container');
function createMessage(userId, name, message){
    const messageBox = document.createElement('div');
    messageBox.classList.add('message-box')

    const nameTag = document.createElement('p');
    nameTag.classList.add('name')
    nameTag.innerText = name;

    if (userId == currentUserId){
        messageBox.classList.add('you')
        nameTag.innerText = ''
    }

   

    const messageTag = document.createElement('p');
    messageTag.classList.add('message')
    messageTag.innerText = message;

    messageBox.appendChild(nameTag);
    messageBox.appendChild(messageTag);

    messageContainer.appendChild(messageBox);
    
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    })
}

async function loadMessages(){
    await getCurrentUserId()
    for (const msg of messages){
        createMessage(msg.user_id, msg.name, msg.message)
    }
}

const sendButton = document.getElementById('send-btn');
const inputBar = document.querySelector('.input-bar');
sendButton.addEventListener('click', ()=>{
    let text = inputBar.value.trim();
    
    if (text){
        inputBar.value = '';
        socketio.emit('send-message', text)
    }
})

window.addEventListener('keypress',(evt)=>{
    if (evt.key === 'Enter'){
        let text = inputBar.value.trim();
    
        if (text){
            inputBar.value = '';
            socketio.emit('send-message', text)
        }
    }
})
socketio.on('connected', (data)=>{
    const tag = document.createElement('p');
    tag.innerText = data;
    tag.classList.add('connected')
    messageContainer.appendChild(tag);

        
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    })
})

socketio.on('disconnected', (data)=>{
    const tag = document.createElement('p');
    tag.innerText = data;
    tag.classList.add('disconnected')
    messageContainer.appendChild(tag);
        
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    })
})

socketio.on('message-created', (data)=>{
    console.log(data);
    createMessage(data.user_id, data.name, data.message)
})

socketio.on('error', (data)=>{
    console.log(data);
})

async function run() {
    await getMessages();
    loadMessages();
}

run()

