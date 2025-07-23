<<<<<<< HEAD
// Referências aos elementos HTML
const loginForm = document.getElementById("loginForm"); //
const emailInput = document.getElementById("emailInput"); //
const passwordInput = document.getElementById("passwordInput"); //
const loginMessage = document.getElementById("loginMessage"); //

// Simulação de usuários cadastrados (em um cenário real, isso viria de um backend/banco de dados)
// Usaremos localStorage para persistência frontend simples
let users = JSON.parse(localStorage.getItem('registeredUsers')) || {
    "teste@email.com": "12345", // Exemplo de usuário pré-cadastrado
    "admin@email.com": "admin123" // Outro exemplo
};

// Salva os usuários no localStorage
function saveUsers() {
    localStorage.setItem('registeredUsers', JSON.stringify(users)); //
}

// Inicializa para garantir que temos os usuários padrão se o localStorage estiver vazio
if (Object.keys(JSON.parse(localStorage.getItem('registeredUsers') || '{}')).length === 0) {
    saveUsers(); // Salva os usuários padrão na primeira execução se não houver nenhum
}

// Evento de submit do formulário de login
loginForm.addEventListener("submit", function(event) { //
    event.preventDefault(); // Impede o envio padrão do formulário (que recarregaria a página)

    const email = emailInput.value.trim(); //
    const password = passwordInput.value.trim(); //

    // Limpa mensagens anteriores
    loginMessage.textContent = ""; //
    loginMessage.classList.remove("error", "success"); //

    // Lógica de validação simples
    if (users[email] && users[email] === password) { //
        // Login bem-sucedido
        loginMessage.textContent = "Login bem-sucedido! Redirecionando..."; //
        loginMessage.classList.add("success"); //

        // Armazenar o estado de login (ex: qual usuário está logado)
        localStorage.setItem('loggedInUser', email); //

        // Redireciona para a página do Quadro Kanban
        // Certifique-se de que o caminho para o index.html está correto
        // Assumindo que index.html está na pasta 'teste' e login.html está em 'pages'
        // ou que index.html está na raiz e login.html está em 'pages' e você quer voltar uma pasta
        window.location.href = '../html/inicio.html'; // Ajuste este caminho se necessário
    } else {
        // Credenciais inválidas
        loginMessage.textContent = "E-mail ou senha inválidos. Tente novamente."; //
        loginMessage.classList.add("error"); //
    }
});

=======
// Referências aos elementos HTML
const loginForm = document.getElementById("loginForm"); //
const emailInput = document.getElementById("emailInput"); //
const passwordInput = document.getElementById("passwordInput"); //
const loginMessage = document.getElementById("loginMessage"); //

// Simulação de usuários cadastrados (em um cenário real, isso viria de um backend/banco de dados)
// Usaremos localStorage para persistência frontend simples
let users = JSON.parse(localStorage.getItem('registeredUsers')) || {
    "teste@email.com": "12345", // Exemplo de usuário pré-cadastrado
    "admin@email.com": "admin123" // Outro exemplo
};

// Salva os usuários no localStorage
function saveUsers() {
    localStorage.setItem('registeredUsers', JSON.stringify(users)); //
}

// Inicializa para garantir que temos os usuários padrão se o localStorage estiver vazio
if (Object.keys(JSON.parse(localStorage.getItem('registeredUsers') || '{}')).length === 0) {
    saveUsers(); // Salva os usuários padrão na primeira execução se não houver nenhum
}

// Evento de submit do formulário de login
loginForm.addEventListener("submit", function(event) { //
    event.preventDefault(); // Impede o envio padrão do formulário (que recarregaria a página)

    const email = emailInput.value.trim(); //
    const password = passwordInput.value.trim(); //

    // Limpa mensagens anteriores
    loginMessage.textContent = ""; //
    loginMessage.classList.remove("error", "success"); //

    // Lógica de validação simples
    if (users[email] && users[email] === password) { //
        // Login bem-sucedido
        loginMessage.textContent = "Login bem-sucedido! Redirecionando..."; //
        loginMessage.classList.add("success"); //

        // Armazenar o estado de login (ex: qual usuário está logado)
        localStorage.setItem('loggedInUser', email); //

        // Redireciona para a página do Quadro Kanban
        // Certifique-se de que o caminho para o index.html está correto
        // Assumindo que index.html está na pasta 'teste' e login.html está em 'pages'
        // ou que index.html está na raiz e login.html está em 'pages' e você quer voltar uma pasta
        window.location.href = '../html/inicio.html'; // Ajuste este caminho se necessário
    } else {
        // Credenciais inválidas
        loginMessage.textContent = "E-mail ou senha inválidos. Tente novamente."; //
        loginMessage.classList.add("error"); //
    }
});

>>>>>>> 21fc7ea20d00a27cb6667d4ce0582642e3d2240c
