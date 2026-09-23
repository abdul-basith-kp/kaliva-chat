
const loginButton = document.getElementById("login-btn");
const registerButton = document.getElementById("register-btn");

loginButton.addEventListener('click', ()=>{
    window.location.href = 'http://127.0.0.1:5000/login'
})

registerButton.addEventListener('click', ()=>{
    window.location.href = 'http://127.0.0.1:5000/register'
})