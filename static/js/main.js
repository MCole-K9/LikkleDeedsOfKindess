
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



let radioBtns = document.querySelectorAll('input[type="radio"]');



radioBtns.forEach(radioBtn =>{

    radioBtn.addEventListener("change", ()=>{

    
        
        if(radioBtn.checked && radioBtn.value == 0){

            //When Custom Amount is selected

            document.getElementById("collapse-other").classList.add("d-block");
            document.getElementById("collapse-other").classList.remove("d-none");

            document.getElementById("custom-amount").addEventListener("change", (event)=>{

                document.getElementById("donationAmount").innerText = event.target.value;

            });
            
            

        }else{
            
            document.getElementById("collapse-other").classList.add("d-none");
            document.getElementById("collapse-other").classList.remove("d-block");

            document.getElementById("donationAmount").innerText = radioBtn.value;
            
        }
    })

    
});

let toStep2Btn = document.getElementById("toStep2");

toStep2Btn.addEventListener("click", ()=> {


    //Donation Validation - Amount Selected

    let amountChecked = false;
    let amountEntered = false;

    radioBtns.forEach(radioBtn => {

        //console.log(radioBtn.checked);

        if(radioBtn.checked && radioBtn.value > 0){
            
            amountChecked = true;

        }
        
    })

    //amount input
    if (document.getElementById("custom-amount").value > 0 ){

        amountEntered = true;

    }


    if(amountChecked || amountEntered){

        
        let Step2TabTrigger = document.getElementById("pills-step2-tab");
        let tabTrigger = new bootstrap.Tab(Step2TabTrigger);
        tabTrigger.show();

    }else{

        alert("Please Select or Enter an Amount to Continue")
     
    }

    
});

let backToStep1Btn = document.getElementById("backToStep1");

backToStep1Btn.addEventListener("click", ()=>{

    let Step1TabTrigger = document.getElementById("pills-step1-tab");
    let tabTrigger = new bootstrap.Tab(Step1TabTrigger);
    tabTrigger.show();
});

let toStep3Btn = document.getElementById("toStep3");

toStep3Btn.addEventListener("click", ()=>{

    //biodata
    let bioValid = false;

    let firstName = document.getElementById("first-name").value;
    let lastName = document.getElementById("last-name").value;
    let email = document.getElementById("email-address").value;
    let phoneNumber = document.getElementById("phone-number").value;

    console.log(email);

    if (firstName == ""){

        alert("Please Enter First Name");

    }else if (lastName == ""){

        alert("Please Enter Last Name");

    }else if(!email.match(/^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/) || email == ""){

    
        alert("Blank or Invalid Email Format");

    }else if(!phoneNumber.match(/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im) || phoneNumber == ""){

        alert("Blank or Invalid Phone number Format");

    }else{

        bioValid = true;
    }


    if(bioValid){

        let Step3TabTrigger = document.getElementById("pills-step3-tab");
        let tabTrigger = new bootstrap.Tab(Step3TabTrigger);
        tabTrigger.show();
    }

    
});

let backToStep2Btn = document.getElementById("backToStep2");

backToStep2Btn.addEventListener("click", ()=>{

    let Step2TabTrigger = document.getElementById("pills-step2-tab");
    let tabTrigger = new bootstrap.Tab(Step2TabTrigger);
    tabTrigger.show();
});


let payWithCardBtn  = document.getElementById("pay-with-card");

payWithCardBtn.addEventListener("click", ()=>{
    

    $("#card-info").toggleClass("d-none");
    
});


let payWithPaypal = document.getElementById("pay-with-paypal");

payWithPaypal.addEventListener("click", ()=>{
    
    $("#paypal-btns").toggleClass("d-none");
    
});

function handleVolunteers(postUrl){

    document.getElementById("volunteer_form").setAttribute("action", postUrl)
}