document.addEventListener('DOMContentLoaded', function() {
    // Pegando os elementos exatamente pelos IDs do seu HTML
    const btnMenu = document.getElementById('btnMenu');
    const btnFechar = document.getElementById('btnFechar');
    const sidebar = document.getElementById('mySidebar');
    const links = document.querySelectorAll('.menu-link');

    // Função para Abrir
    if (btnMenu && sidebar) {
        btnMenu.addEventListener('click', function() {
            sidebar.classList.add('active');
        });
    }

    // Função para Fechar (no X)
    if (btnFechar && sidebar) {
        btnFechar.addEventListener('click', function() {
            sidebar.classList.remove('active');
        });
    }

    // Fecha o menu ao clicar em qualquer link (bom para navegação interna)
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (sidebar) {
                sidebar.classList.remove('active');
            }
        });
    });
});