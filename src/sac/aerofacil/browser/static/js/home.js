$(document).ready(function () {
  $('#topo').load('topo.html', function () {
    $('.menu a').on('click', function() {
      var rel = $(this).attr('rel');
      var dist = $('.'+rel).offset().top;    
      $('html, body').animate({
        scrollTop: dist
      }, 1000);
      return false;
    });  

    $(".menu-mobile").on( "click", function() {
        $(".menu").toggleClass( "hover" );
        $(".menu-mobile").toggleClass( "hover" );
      });

  });
  $('#rodape').load('rodape.html');
  $('.menu-flutuante a').on('click', function() {
    var rel = $(this).attr('rel');
    var dist = $('.'+rel).offset().top;    
    $('html, body').animate({
      scrollTop: dist
    }, 1000);
    return false;
  });

  $(window).scroll(function () {
    var scr = $(window).scrollTop();
    if(scr < 400) {
      $('.menu-flutuante').hide();
    } else {
      $('.menu-flutuante').show();
    }
  });

  $('.bloco-informacoes .lk-seta-left').click(function () {
    $('.bloco-informacoes .lk-seta-left').removeClass('open');
    $('.texto-info').slideUp();
    $(this).addClass('open');
    $(this).parent().find('.texto-info').slideDown();
    return false;
  });

  // carrossel de noticias
  $('.lista-noticias').flexslider({
    animation: "slide",
    controlNav: false  
  });


  $('.menu a').on('click', function() {
    var rel = $(this).attr('rel');
    var dist = $('.'+rel).offset().top;    
    $('html, body').animate({
      scrollTop: dist
    }, 1000);
    return false;
  });
  $('.lk-aeroporto-home').click(function (){
    $(this).hide();
    $('.select-aeroporto-home').fadeIn();    
    return false;
  });

  $('.select-aeroporto-home').change(function () {
    var val = $(this).val();
    $('#aeroporto').load('aeroportos/'+val+'.html', function () {
      $('.item-aero a').click(function() {
        $(this).parent().find('span').slideToggle();
        return false;
      });
      $(".overflow-aero").mCustomScrollbar({
        advanced: {
          updateOnContentResize: true
        }
      });
    });
    location.href = "aeroporto.html#"+val;
    
  });

});