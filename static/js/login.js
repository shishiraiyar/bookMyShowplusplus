document.getElementById("btn").addEventListener("click", async () => {
  console.log("hjdbjdv");
  const response = await fetch("/getMovieInfo/123");
  data = await response.json();
  console.log(data);
  //   document.getElementById("demo").innerHTML = response;
});

// document.getElementById("signUp").addEventListener("click", async () => {
//   console.log("hjdbjdv");
//   window.location.href = "/signUp";
// });
