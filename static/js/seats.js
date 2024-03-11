// elements = document.getElementsByClassName("seats");
// for (let i = 0; i < elements.length; i++) {
//   console.log(elements[i]);
//   elements[i].addEventListener("click", () => {
//     console.log(elements[i].id);

//     // window.location.href = "/bookTicket/" + elements[i].id;
//   });
// }
document.addEventListener("DOMContentLoaded", function () {
  const elements = document.getElementsByClassName("seats");
  const url = window.location.href;
  const showID = url.split("/")[4];
  console.log(showID);

  for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", () => {
      const seatId = elements[i].id;
      const [_, row, col] = seatId.split("-").map(Number);
      let x = Math.random() * 100;
      bookTicket(showID, row, col, x);
    });
  }

  function bookTicket(showID, row, col, x) {
    fetch("/book_ticket", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ showID: showID, row: row, col: col }),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Failed to book ticket");
        }
      })
      .then((data) => {
        alert(
          "Ticket booked! Your ticket id is " +
            showID +
            "-" +
            x +
            "" +
            row +
            "-" +
            col
        ); // Display a popup notification
        window.location.reload()
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});
