

const loginButton = document.getElementById('login-btn');
loginButton.addEventListener('click', (evt)=>{
    evt.preventDefault()
    window.location.href = 'http://127.0.0.1:5000/login';
})

function showErrorMessage(error){
    const errorMessage = document.querySelector('.error-message');
    errorMessage.innerText = error;
}

async function registerUser(name, password) {

    const response = await fetch("http://127.0.0.1:5000/register", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        password: password
    })
     
    });

    const data = await response.json()
    if (data.success){
        window.location.href = data.redirect;
    } else {
        showErrorMessage(data.message)
    }
}

const registerButton = document.getElementById('register-btn');
registerButton.addEventListener('click', (evt)=>{
    evt.preventDefault()
    const name = document.getElementById('name').value;
    const password = document.getElementById('password').value;
    
    registerUser(name, password)
})