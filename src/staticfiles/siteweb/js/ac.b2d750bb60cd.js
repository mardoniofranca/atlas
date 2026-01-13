function fazerLogin() {
    const login = document.getElementById("login").value;
    const senha = document.getElementById("senha").value;

    if (login === "adm" && senha === "123") {
        window.location.href = MENU_URL;
        return false;
    } else {
        alert("Login ou senha incorretos!");
        return false;
    }
}
