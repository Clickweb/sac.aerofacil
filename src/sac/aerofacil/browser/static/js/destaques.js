$(document).ready(function () {
  $('#topo').load('topo.html', function(){
      $(".menu-mobile").on( "click", function() {
          $(".menu").toggleClass( "hover" );
          $(".menu-mobile").toggleClass( "hover" );
        });
    });  
  $('#rodape').load('rodape.html');
  
$(".aplicativos-interna").jCarouselLite({
  btnNext: ".next",
  btnPrev: ".prev",
  visible: 1,
  speed: 800
});


});