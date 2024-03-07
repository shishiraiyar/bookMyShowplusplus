elements = document.getElementsByClassName("bookticket");

for (let i = 0; i < elements.length; i++) {
  console.log(elements[i]);
  elements[i].addEventListener("click", () => {
    console.log(elements[i].id);
    window.location.href = "/map/" + elements[i].id;
  });
}
