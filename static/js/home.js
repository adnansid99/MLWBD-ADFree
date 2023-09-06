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

const dialogBtn2 = () => {
  window.open("https://adnan.eu.org", "_blank");
};

const dialogBtn1 = () => {
  const initDate1 = new Date();
  let savedDate = `${initDate1.getFullYear()}-${(initDate1.getMonth() + 1)
    .toString()
    .padStart(2, "0")}-${initDate1.getDate().toString().padStart(2, "0")}`;
  localStorage.setItem("dialogCheck", savedDate);
};

const daysDifference = (cD, sD) => {
  const timeDiff = new Date(cD) - new Date(sD);
  const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
  return daysDiff;
};

const modalView = () => {
  dialogView = document.getElementById("dialogView");
  if (localStorage.getItem("dialogCheck") == null) {
    dialogView.click();
  } else {
    const initDate2 = new Date();
    let currentDate = `${initDate2.getFullYear()}-${(initDate2.getMonth() + 1)
      .toString()
      .padStart(2, "0")}-${initDate2.getDate().toString().padStart(2, "0")}`;

    let savedDate = localStorage.getItem("dialogCheck");
    if (daysDifference(currentDate, savedDate) >= 1) {
      dialogView.click();
    }
  }
};
