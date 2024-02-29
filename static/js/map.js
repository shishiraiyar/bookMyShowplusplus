console.log(theatresList)
const url = window.location.href
const movieID = url.split("/")[4]

let map;
let infoWindows = []

const pes = {lat:12.934833162232344, lng:77.53507211285884}

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    mapTypeId: "roadmap",
    zoom: 13,
    center: pes,
    mapId: "6d77c92efad4c954"
  });
  map.setTilt(45); 

  for (let theatre of theatresList){
    addTheatre(theatre)
  }

  map.addListener("click", ()=>{
    for (let infowindow of infoWindows)
      infowindow.close()
  })

  
}
  
window.initMap = initMap;

function addTheatre(theatre){
  let location = {'lat':theatre['latitude'],  'lng': theatre['longitude']}
  console.log(location)

  let colour = "#FFF1DC"
  let svg = `<svg width="30px" height="30px" viewBox="0 0 1024 1024" class="icon"  version="1.1" xmlns="http://www.w3.org/2000/svg">
  <path d="M729.6 870.4c0 28.16-23.04 51.2-51.2 51.2H345.6c-28.16 0-51.2-23.04-51.2-51.2V179.2c0-28.16 23.04-51.2 51.2-51.2h332.8c28.16 0 51.2 23.04 51.2 51.2v691.2z" fill="${colour}" />
  <path d="M678.4 934.4H345.6c-35.84 0-64-28.16-64-64V179.2c0-35.84 28.16-64 64-64h332.8c35.84 0 64 28.16 64 64v691.2c0 35.84-28.16 64-64 64zM345.6 140.8c-21.76 0-38.4 16.64-38.4 38.4v691.2c0 21.76 16.64 38.4 38.4 38.4h332.8c21.76 0 38.4-16.64 38.4-38.4V179.2c0-21.76-16.64-38.4-38.4-38.4H345.6z" fill="#231C1C" />
  <path d="M691.2 744.96c0 12.8-11.52 23.04-25.6 23.04H358.4c-14.08 0-25.6-10.24-25.6-23.04V253.44c0-12.8 11.52-23.04 25.6-23.04h307.2c14.08 0 25.6 10.24 25.6 23.04v491.52z" fill="${colour}" />
  <path d="M665.6 780.8H358.4c-21.76 0-38.4-16.64-38.4-35.84V253.44c0-20.48 16.64-35.84 38.4-35.84h307.2c21.76 0 38.4 16.64 38.4 35.84v491.52c0 19.2-16.64 35.84-38.4 35.84zM358.4 243.2c-7.68 0-12.8 5.12-12.8 10.24v491.52c0 5.12 5.12 10.24 12.8 10.24h307.2c7.68 0 12.8-5.12 12.8-10.24V253.44c0-5.12-5.12-10.24-12.8-10.24H358.4z" fill="#231C1C" />
  <path d="M512 844.8m-38.4 0a38.4 38.4 0 1 0 76.8 0 38.4 38.4 0 1 0-76.8 0Z" fill="#231C1C" />
  <path d="M512 896c-28.16 0-51.2-23.04-51.2-51.2s23.04-51.2 51.2-51.2 51.2 23.04 51.2 51.2-23.04 51.2-51.2 51.2z m0-76.8c-14.08 0-25.6 11.52-25.6 25.6s11.52 25.6 25.6 25.6 25.6-11.52 25.6-25.6-11.52-25.6-25.6-25.6z" fill="#231C1C" />
  <path d="M460.8 166.4h102.4v25.6h-102.4z" fill="#231C1C" /></svg>`
  const svgMarker = {
    url: 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg),
    fillColor: "#FC2947",
    fillOpacity: 1.0,
    strokeWeight: 1,
    rotation: 0,
    anchor: new google.maps.Point(15, 15),
  }
  
const marker = new google.maps.Marker({
  icon: svgMarker,
  position: location,
  map: map,
  // animation: google.maps.Animation.DROP
});

  createInfoWindow(marker, theatre)

// makeInfoWindow(marker, "HELLO")
// id, name, address, since

}

function createInfoWindow(marker, theatre){
  let htmlString = `
  <div>
  <p>Name: ${theatre['name']}</p>
  <p>Address: ${theatre['address']}</p>
  <p>Op since: ${theatre['operatingSince']}</p>
  <a href='/shows?theatre=${theatre['ID']}&movie=${movieID}'>Book tickets here</a>
  </div>`

  const infoWindow = new google.maps.InfoWindow({
    content: htmlString,
    map: map,
    width: 500,
  });
  infoWindows.push(infoWindow)

  marker.addListener("click", ()=>{
    infoWindow.open(
      {anchor: marker,}
    )
  });
}
