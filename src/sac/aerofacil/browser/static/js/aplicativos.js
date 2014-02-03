$(document).ready(function () {
  $('#topo').load('topo.html', function(){
      $(".menu-mobile").on( "click", function() {
          $(".menu").toggleClass( "hover" );
          $(".menu-mobile").toggleClass( "hover" );
        });
    });  
  $('#rodape').load('rodape.html');

  // carrossel de aplicativos
  $('.aplicativos-interna').flexslider({
    animation: "slide",
    controlNav: false  
  });


});