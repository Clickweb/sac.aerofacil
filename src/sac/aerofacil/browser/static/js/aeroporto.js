$(document).ready(function () {
  $('#topo').load('topo.html', function(){
      $(".menu-mobile").on( "click", function() {
          $(".menu").toggleClass( "hover" );
          $(".menu-mobile").toggleClass( "hover" );
        });
    });  
  $('#rodape').load('rodape.html');
  
  // carrossel de aplicativos
  $('.box-apps').flexslider({
    animation: "slide",
    directionNav: false,
    selector: ".slides > div"
  });
 

  $(".overflow-aero").mCustomScrollbar({
    advanced: {
      updateOnContentResize: true
    }
  });

  $('.item-aero a').click(function() {    
    if(!$(this).hasClass('externo')) {
      $(this).parent().find('span').slideToggle();
      return false;
    }    
  });

  var hash = $(location).attr('href');
  hash = hash.split('#');
  var aero = hash[1];  
  if(aero) {
    $('#aeroporto').load('aeroportos/'+aero+'.html', function () {
      $('.item-aero a').click(function() {
        if(!$(this).hasClass('externo')) {
          $(this).parent().find('span').slideToggle();
          return false;
        }
      });
      $(".overflow-aero").mCustomScrollbar({
        advanced: {
          updateOnContentResize: true
        }
      });
    });    
  }

  $('.lk-outro-aero').click(function() {
    $(this).hide();
    $('.select-aeroporto').fadeIn();
    return false;
  });

  $('.marcadores-apps a').click(function () {
    if(!$(this).hasClass('ativo')){
      var id = $(this).html();
      id = parseInt(id);
      console.log(id);
      $('.box-apps-aero').fadeOut();
      $('#app-'+id).fadeIn();
      $('.ativo').removeClass('ativo');
      $(this).addClass('ativo');
    }
    return false;
  });

  $('.select-aeroporto').change(function () {
    var val = $(this).val();
    $('#aeroporto').load('aeroportos/'+val+'.html', function () {
      $('.item-aero a').click(function() {
       if(!$(this).hasClass('externo')) {
          $(this).parent().find('span').slideToggle();
          return false;
        }
      });
      $(".overflow-aero").mCustomScrollbar({
        advanced: {
          updateOnContentResize: true
        }
      });
    });
    location.href = "#"+val;
    
  });



});