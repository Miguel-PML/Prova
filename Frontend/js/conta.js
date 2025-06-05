// Script JavaScript para alternar o tema
document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;
    const themeIcon = themeToggleBtn.querySelector('.material-icons');

    // Verifica a preferência de tema salva no localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.setAttribute('data-theme', savedTheme);
        // Atualiza o ícone com base no tema salvo
        themeIcon.textContent = savedTheme === 'dark' ? 'light_mode' : 'dark_mode';
    } else {
        // Define o tema padrão como 'dark' e o ícone de 'sol'
        body.setAttribute('data-theme', 'dark');
        themeIcon.textContent = 'light_mode';
    }

    themeToggleBtn.addEventListener('click', () => {
        let currentTheme = body.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            body.setAttribute('data-theme', 'light');
            themeIcon.textContent = 'dark_mode'; // Mudar para ícone de lua
            localStorage.setItem('theme', 'light');
        } else {
            body.setAttribute('data-theme', 'dark');
            themeIcon.textContent = 'light_mode'; // Mudar para ícone de sol
            localStorage.setItem('theme', 'dark');
        }
    });
});