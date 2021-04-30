function tog(){
  document.getElementById('ngo').classList.toggle("a")
}
let ngo=document.querySelector("#ngo");
let home=document.querySelector("#home"); 
ngo.addEventListener("click", ()=>{
  this.classList.toggle("active");
})
home.addEventListener("click",()=>{
  this.classList.toggle("active");
})
