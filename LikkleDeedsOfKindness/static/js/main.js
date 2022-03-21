


$("#donate-now").click(()=>{
    location.href = "/"
});

$("#join-us").click(()=>{
    location.href = "/"
});

$("#get-involved").click(()=>{
    location.href = "/"
});

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

     //>=, not <=
    if (scroll >= 300) {
        
        $("nav").addClass("bg-white");
        $("nav").removeClass("navbar-dark")
        $("nav").addClass("navbar-light");
        $("nav").addClass("sticky-top");

    }else{

        $("nav").removeClass("bg-white");
        $("nav").addClass("navbar-dark")
        $("nav").removeClass("sticky-top");
        $("nav").RemoveClass("navbar-light");
    }
});