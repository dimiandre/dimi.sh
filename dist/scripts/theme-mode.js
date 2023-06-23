document.addEventListener("DOMContentLoaded", (event) => {
    const body = document.querySelector("body");
    const themeToggle = document.querySelector("#theme-toggle");

    // Load saved theme from local storage
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        body.classList.add(savedTheme);
    } else {
        // If there's no saved theme, use the OS preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            body.classList.remove("light-theme");
        } else {
            body.classList.add("light-theme");
        }
    }

    themeToggle.addEventListener("click", function() {
        if (body.classList.contains("light-theme")) {
            body.classList.remove("light-theme");
            localStorage.setItem("theme", "");
        } else {
            body.classList.add("light-theme");
            localStorage.setItem("theme", "light-theme");
        }
    });
});