const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");



function isValidEmail(email) {
    return email.includes("@") && email.includes(".");
}

function showMessage(text, type) {
    message.textContent = text;
    message.className = type;
}


loginForm.addEventListener("submit", async function (event){

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

    try {

        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
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
    }catch (error) {

        showMessage(
            "Erro ao conectar com o servidor.",
            "error"
        );

        console.error(error);
    }
});
