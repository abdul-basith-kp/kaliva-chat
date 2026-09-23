
const loginButton = document.getElementById("login-btn");
const registerButton = document.getElementById("register-btn");

loginButton.addEventListener('click', ()=>{
    window.location.href = '/login'
})

registerButton.addEventListener('click', ()=>{
    window.location.href = '/register'
})