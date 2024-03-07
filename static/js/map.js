console.log(theatresList)
const url = window.location.href
const movieID = url.split("/")[4]

let map;
let infoWindows = []

const pes = {lat:12.934833162232344, lng:77.53507211285884}

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    mapTypeId: "roadmap",
    zoom: 11,
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
  let svg = `<svg version="1.0" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="40px" height="40px" viewBox="0 0 64 64" enable-background="new 0 0 64 64" xml:space="preserve" fill="#000000">

  <g id="SVGRepo_bgCarrier" stroke-width="0"/>
  
  <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
  
  <g id="SVGRepo_iconCarrier"> <g> <polygon fill="#f02d2d" points="52,56 36,56 36,44 28,44 28,56 12,56 12,8 52,8 "/> <path fill="#1b1d1d" d="M56,0H8C5.789,0,4,1.789,4,4v56c0,2.211,1.789,4,4,4h48c2.211,0,4-1.789,4-4V4C60,1.789,58.211,0,56,0z M52,56H36V44h-8v12H12V8h40V56z"/> <rect x="36" y="16" fill="#1b1d1d" width="8" height="8"/> <rect x="20" y="16" fill="#1b1d1d" width="8" height="8"/> <rect x="20" y="32" fill="#1b1d1d" width="8" height="8"/> <rect x="36" y="32" fill="#1b1d1d" width="8" height="8"/> </g> </g>
  
  </svg>`
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
  <a href='/shows?theatre=${theatre['ID']}&movie=${movieID}' class="btn btn-primary" style="margin-bottom:5px; margin-right:5px">Book tickets here</a>
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
