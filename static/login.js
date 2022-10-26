var btnEl=document.querySelector(".btn");
// var signinEl=document.querySelector(".signin");
var buttonsEl=document.querySelectorAll(".btn-1");
var containerEl=document.querySelector(".container");
var bigContainerEl=document.querySelector(".bigcontainer");

btnEl.addEventListener("click",()=>{
    containerEl.classList.remove("active");
    bigContainerEl.classList.add("active-1");
})

buttonsEl[0].addEventListener("click",()=>{
    containerEl.classList.add("active");
    bigContainerEl.classList.remove("active-1");
})