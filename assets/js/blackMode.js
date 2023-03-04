const checkbox = document.getElementById('toggleTheme');

document.body.onload = () => {
    if (window.localStorage.getItem("theme") === null && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        checkbox.checked = true;
        toggleBlackMode()
        window.localStorage.setItem('theme', 'dark');
    }

    const theme = window.localStorage.getItem("theme");

    (theme === "dark")
        ? setDarkMode()
        : removeDarkMode()
}

checkbox.onchange = () => toggleBlackMode();

const toggleBlackMode = () => {
    document.body.classList.toggle("black-mode");
    window.localStorage.setItem('theme', document.body.classList.contains("black-mode") ? "dark" : "light");
}

const setDarkMode = () => {
    checkbox.checked = true;
    document.body.classList.add("black-mode");
}

const removeDarkMode = () => {
    document.body.classList.remove("black-mode");
}