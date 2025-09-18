document.addEventListener('DOMContentLoaded', function() {
    const storyEditor = document.getElementById('story-editor');
    const fontSelector = document.getElementById('font-selector');
    const fontSizeSelector = document.getElementById('font-size-selector');
    const applyFontButton = document.getElementById('apply-font-button');
    const shareButton = document.getElementById('share-button');
    const saveButton = document.getElementById('save-button');
    const themeToggle = document.getElementById('theme-toggle'); // Novo: botão de alternar tema

    let activeFont = fontSelector.value;
    let activeFontSize = fontSizeSelector.value;

    // --- Lógica do Modo Escuro ---
    // Verifica a preferência do usuário no localStorage ou no sistema
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.body.classList.add('dark-mode');
    }

    // Adiciona evento ao botão de alternar tema
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode'); // Adiciona/remove a classe 'dark-mode'
        const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
        localStorage.setItem('theme', currentTheme); // Salva a preferência no localStorage
    });
    // --- Fim da Lógica do Modo Escuro ---


    fontSelector.addEventListener('change', function() {
        activeFont = fontSelector.value;
    });

    fontSizeSelector.addEventListener('change', function() {
        activeFontSize = fontSizeSelector.value;
    });

    applyFontButton.addEventListener('click', function() {
        const selection = window.getSelection();
        if (selection.rangeCount === 0) return;

        const range = selection.getRangeAt(0);

        if (!storyEditor.contains(range.commonAncestorContainer)) {
            return;
        }

        try {
            document.execCommand('styleWithCSS', false, true);
            document.execCommand('fontSize', false, activeFontSize);
            document.execCommand('fontName', false, activeFont);
            document.execCommand('styleWithCSS', false, false);

        } catch (e) {
            console.error("Erro ao aplicar estilo com execCommand:", e);
            alert("Não foi possível aplicar o estilo ao texto selecionado ou para digitação.");
        }
    });

    saveButton.addEventListener('click', function() {
        const storyContent = storyEditor.innerText;
        const filename = 'minha_historia.txt';

        const blob = new Blob([storyContent], { type: 'text/plain;charset=utf-8' });

        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = filename;

        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        URL.revokeObjectURL(a.href);

        alert('Sua história foi baixada como "minha_historia.txt"!');
    });

    shareButton.addEventListener('click', function() {
        const fullStoryText = storyEditor.innerText;
        navigator.clipboard.writeText(fullStoryText)
            .then(() => {
                alert('Texto da história (sem formatação) copiado para a área de transferência! Você pode colar onde quiser.');
            })
            .catch(err => {
                console.error('Erro ao copiar a história: ', err);
                alert('Não foi possível copiar o texto da história. Por favor, copie manualmente.');
            });
    });

    if (storyEditor.innerHTML.trim() === '<p>Comece a escrever sua história aqui!</p>') {
        storyEditor.addEventListener('focus', function handler() {
            if (storyEditor.innerHTML.trim() === '<p>Comece a escrever sua história aqui!</p>') {
                storyEditor.innerHTML = '';
            }
            storyEditor.removeEventListener('focus', handler);
        });
    }
});