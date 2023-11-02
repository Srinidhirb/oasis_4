document.querySelector('.cross').style.display = 'none'
document.querySelector('.ham').addEventListener("click",()=>{
    document.querySelector('.sidenavbar').classList.toggle("sidebargo")
    if(document.querySelector('.sidenavbar').classList.contains("sidebargo")){
        document.querySelector('.menu').style.display = 'inline'
        document.querySelector('.cross').style.display = 'none'
    }
    else{
        document.querySelector('.menu').style.display = 'none'
        document.querySelector('.cross').style.display = 'inline'
        
    }
})
