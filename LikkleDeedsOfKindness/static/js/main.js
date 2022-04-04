
function goToLocation(url) { 
    location.href = url;
}

// $(window).scroll(function() {    
//     var scroll = $(window).scrollTop();

//      //>=, not <=
//     if (scroll >= 80) {
        
//         $("nav").addClass("bg-white");
//         $("nav").removeClass("navbar-dark")
//         $("nav").addClass("navbar-light");
//         $("nav").addClass("sticky-top");

//     }else{

//         $("nav").removeClass("bg-white");
//         $("nav").addClass("navbar-dark")
//         $("nav").removeClass("sticky-top");
//         $("nav").removeClass("navbar-light");
//     }
// });

// $("#collapse-other").;


let radioBtns = document.querySelectorAll('input[type="radio"]');



radioBtns.forEach(radioBtn =>{

    radioBtn.addEventListener("change", ()=>{

    
        
        if(radioBtn.checked && radioBtn.value == 0){

            console.log(radioBtn.value);
            document.getElementById("collapse-other").classList.add("d-block");
            document.getElementById("collapse-other").classList.remove("d-none");

        }else{
            
            document.getElementById("collapse-other").classList.add("d-none");
            document.getElementById("collapse-other").classList.remove("d-block");
        }
    })

    
});