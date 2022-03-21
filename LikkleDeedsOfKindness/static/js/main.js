


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
    if (scroll >= 50) {
        
        $("nav").addClass("bg-white");
        $("nav").removeClass("navbar-dark")
        $("nav").addClass("navbar-light");
        $("nav").addClass("fixed-top");

    }else{

        $("nav").removeClass("bg-white");
        $("nav").addClass("navbar-dark")
        $("nav").removeClass("fixed-top");
        $("nav").RemoveClass("navbar-light");
    }
});