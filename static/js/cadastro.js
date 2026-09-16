const registerForm = document.getElementById("registerForm");
const message = document.getElementById("message");

function IsValidEmail(email) {
    return email.includes("@") && email.includes(".");
}

function showMessage(text, type) {
    message.textContent = text;
    message.className = type;
}

async function registerUser(name, email, password){

    try {
        const response = await fetch("/api/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            showMessage(data.message, "error");
            return;
        }

        showMessage(data.message, "success");
    } catch (error) {

        showMessage("Erro ao conectar com o servidor.", "error");
        console.error(error);
    }
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

    registerUser(name, email, password);
});