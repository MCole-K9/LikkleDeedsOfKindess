
function goToLocation(url) { 
    location.href = url;
}

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

     //>=, not <=
    if (scroll >= 80) {
        
        $("nav").addClass("bg-white");
        $("nav").removeClass("navbar-dark")
        $("nav").addClass("navbar-light");
        $("nav").addClass("sticky-top");

    }else{

        $("nav").removeClass("bg-white");
        $("nav").addClass("navbar-dark")
        $("nav").removeClass("sticky-top");
        $("nav").removeClass("navbar-light");
    }
});