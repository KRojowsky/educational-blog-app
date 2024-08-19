document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("theme-toggle-btn");
    const currentTheme = localStorage.getItem("theme") || "light";

    if (currentTheme === "dark") {
        document.body.classList.add("dark-mode");
    }

    toggleButton.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");
        const theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
        localStorage.setItem("theme", theme);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const categoryMenuBtn = document.getElementById('category-menu-btn');
    const filterMenuBtn = document.getElementById('filter-menu-btn');
    const categoryMenu = document.getElementById('category-menu');
    const filterMenu = document.getElementById('filter-menu');

    function toggleMenu(menu) {
        menu.classList.toggle('hidden');
    }

    function hideMenu(menu) {
        menu.classList.add('hidden');
    }

    function showMenu(menu) {
        menu.classList.remove('hidden');
    }

    hideMenu(categoryMenu);
    hideMenu(filterMenu);

    categoryMenuBtn.addEventListener('click', function() {
        toggleMenu(categoryMenu);
    });

    filterMenuBtn.addEventListener('click', function() {
        toggleMenu(filterMenu);
    });

    document.addEventListener('click', function(event) {
        if (!categoryMenuBtn.contains(event.target) && !categoryMenu.contains(event.target)) {
            hideMenu(categoryMenu);
        }

        if (!filterMenuBtn.contains(event.target) && !filterMenu.contains(event.target)) {
            hideMenu(filterMenu);
        }
    });
});
