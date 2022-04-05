
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

let toStep2Btn = document.getElementById("toStep2");

toStep2Btn.addEventListener("click", ()=>{

    let Step2TabTrigger = document.getElementById("pills-step2-tab");
    let tabTrigger = new bootstrap.Tab(Step2TabTrigger);
    tabTrigger.show();
});

let backToStep1Btn = document.getElementById("backToStep1");

backToStep1Btn.addEventListener("click", ()=>{

    let Step1TabTrigger = document.getElementById("pills-step1-tab");
    let tabTrigger = new bootstrap.Tab(Step1TabTrigger);
    tabTrigger.show();
});

let toStep3Btn = document.getElementById("toStep3");

toStep3Btn.addEventListener("click", ()=>{

    let Step3TabTrigger = document.getElementById("pills-step3-tab");
    let tabTrigger = new bootstrap.Tab(Step3TabTrigger);
    tabTrigger.show();
});

let backToStep2Btn = document.getElementById("backToStep2");

backToStep2Btn.addEventListener("click", ()=>{

    let Step2TabTrigger = document.getElementById("pills-step2-tab");
    let tabTrigger = new bootstrap.Tab(Step2TabTrigger);
    tabTrigger.show();
});
