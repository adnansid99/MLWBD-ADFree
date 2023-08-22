const loading = () => {
  const el = document.createElement("div");
  el.classList.add("loader");
  const form = document.getElementsByTagName("form")[0];
  form.lastElementChild.remove();
  form.appendChild(el);
  document.myForm.submit();
};
const goToBypass = () => {
  let hrefValue = event.target.getAttribute("value");
  window.open("/bypass/" + hrefValue, "_blank");
};

const aboutbtn = () => {
  window.open("https://adnan.eu.org", "_blank");
};
