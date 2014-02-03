$(document).ready(function () {
  $('#topo').load('topo.html', function(){
      $(".menu-mobile").on( "click", function() {
          $(".menu").toggleClass( "hover" );
          $(".menu-mobile").toggleClass( "hover" );
        });
    }); 
  $('#rodape').load('rodape.html');  

  var hash = $(location).attr('href');
  hash = hash.split('#');
  var noticia = hash[1]; 
  $('#miolo-noticias').load('noticias/'+noticia+'.html', function() {
    $("#miolo-noticias").mCustomScrollbar({
      advanced: {
        updateOnContentResize: true
      }
    });
  });

  $("#miolo-noticias").mCustomScrollbar({
    advanced: {
      updateOnContentResize: true
    }
  });

  $('.outras-noticias a').click(function () {
    var hash = $(this).attr('href');
    hash = hash.split('#');
    var noticia = hash[1]; 
    $('#miolo-noticias').load('noticias/'+noticia+'.html', function() {
      $("#miolo-noticias").mCustomScrollbar({
        advanced: {
          updateOnContentResize: true
        }
      });
      $('html, body').animate({
        scrollTop: 0
      });
    });    
  });
  $("#miolo-noticias").mCustomScrollbar({
    advanced: {
      updateOnContentResize: true
    }
  });

  $('.outras-noticias a:odd').addClass('amarelo');



});