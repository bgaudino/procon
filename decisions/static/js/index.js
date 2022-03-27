const formToggleButton = document.getElementById("form-toggle-button");
const form = document.getElementById("form");
const formToggle = createToggle(formToggleButton, form);
formToggleButton.addEventListener("click", formToggle);

