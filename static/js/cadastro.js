const registerForm = document.getElementById("registerForm");
const message = document.getElementById("message");

function IsValidEmail(email) {
    return email.includes("@") && email.includes(".");
}

function showMessage(text, type) {
    message.textContent = text;
    message.className = type;
}

registerForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirm_password = document.getElementById("confirmPassword").value;

    message.textContent = "";
    message.className = "";

    if (name === "" || email === "" || password === "" || confirm_password === "") {
        showMessage("Preenche todos os campos.", "error");
        return;
    }

    if (!IsValidEmail(email)) {
        showMessage("Digite um e-mail válido.", "error");
        return;
    }

    if (password.length < 6) {
        showMessage("A senha deve contar pelo menos 6 caracteres.", "error");
        return;
    }

    if (password !== confirm_password) {
        showMessage("As senhas não coincidem.", "error");
        return;
    }

    showMessage("Cadastro válido!", "success");
});