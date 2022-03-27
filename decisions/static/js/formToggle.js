function createToggle(button, form, content = null) {
  let isVisible = false;
  const originalText = button.innerText;
  function toggle() {
    if (isVisible) {
      if (content) {
        content.classList.remove("is-hidden");
      }
      form.classList.add("is-hidden");
      button.innerText = originalText;
      button.classList.remove("is-danger");
      button.classList.add("is-primary");
      isVisible = false;
    } else {
      if (content) {
        content.classList.add("is-hidden");
      }
      form.classList.remove("is-hidden");
      inputs = Array.from(form.querySelectorAll("input")).filter(
        (input) => input.type !== "hidden"
      );
      if (inputs.length > 0) inputs[0].focus();
      form.querySelector("input").focus();
      button.innerText = "Cancel";
      button.classList.remove("is-primary");
      button.classList.add("is-danger");
      isVisible = true;
    }
  }
  return toggle;
}

const toggles = document.querySelectorAll(".toggle");

toggles.forEach((toggle) => {
  const modal = document.querySelector(`#${toggle.dataset.target}`);
  const content = document.querySelector(`#${toggle.dataset.content}`);
  const modalToggle = createToggle(toggle, modal, content);
  toggle.addEventListener("click", modalToggle);
});
