


const registerButton = document.getElementById('register-btn');

registerButton.addEventListener('click', (evt)=>{
    evt.preventDefault()
    window.location.href = 'http://127.0.0.1:5000/register'
})


const loginButton = document.querySelector('#login-btn');
loginButton.addEventListener('click', (evt)=>{
    evt.preventDefault();
    const name = document.querySelector('#name').value;
    const password = document.querySelector('#password').value;
    if (name && password){
        loginUser(name, password)
    }

})


function showErrorMessage(error){
    const errorMessage = document.querySelector('.error-message');
    errorMessage.innerText = error;
}

async function loginUser(name, password) {
    const response = await fetch('/login',{
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        password: password
    })
     
    })
    const data = await response.json()
    
    if (data.success){
        window.location.href = data.redirect;

    } else {
        showErrorMessage(data.message)
    }
    
}

