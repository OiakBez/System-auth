const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

loginForm.addEventListener("submit", function (event){

    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    message.textContent = "";
    message.className = "";

    if (email === "" || password === "") {
        showMessage("Preencha corretamente todos os campos.", "error");
        return;
    }

    if (!isValidEmail(email)) {
        showMessage("Digite em e-mail válido.", "error");
        return;
    }

    if (password.length < 6) {
        showMessage("A senha deve ter pelo menos 6 caracteres.", "error");
        return;
    }

    showMessage("Dados válidos! Pronto para enviar.", "sucess");
});

function isValidEmail(email) {
    return email.includes("@") && email.includes(".");
}

function showMessage(text, type) {
    message.textContent = text;
    message.className = type;
}