elements = document.getElementsByClassName("movies")

for (let i =0; i<elements.length; i++){
    console.log(elements[i])
    elements[i].addEventListener("click", ()=>{
        console.log(elements[i].id)
    })
}