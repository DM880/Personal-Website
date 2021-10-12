$(document).on('click', '#links', function(e){
    e.preventDefault();
    var url = $(this).attr('href');
    window.open(url, '_blank');
});

 $(window).width(function(d) {
  if ($(window).width() < 950) {
     $(".odd").addClass("proj-d").removeClass("proj-d-odd");
     $(".odd-img").addClass("img-cont").removeClass("img-cont-odd");
  }
  else{
     $(".odd").removeClass("proj-d").addClass("proj-d-odd");
     $(".odd-img").removeClass("img-cont").addClass("img-cont-odd");
  }
});

 $(window).resize(function(f) {
  if ($(window).width() < 950) {
     $(".odd").addClass("proj-d").removeClass("proj-d-odd");
     $(".odd-img").addClass("img-cont").removeClass("img-cont-odd");
  }
  else{
     $(".odd").removeClass("proj-d").addClass("proj-d-odd");
     $(".odd-img").removeClass("img-cont").addClass("img-cont-odd");
  }
});