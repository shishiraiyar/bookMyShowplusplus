elements = document.getElementsByClassName("theatres");
for (let i = 0; i < elements.length; i++) {
  console.log(elements[i]);
  elements[i].addEventListener("click", () => {
    console.log(elements[i].id);
    url = window.location.href;
    console.log(url);
    console.log(url.split("/")[4]);
    window.location.href =
      "/shows?theatre=" + elements[i].id + "&movie=" + url.split("/")[4];
  });
}
