// videos youtube
var tag = document.createElement('script');
tag.src = "//www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var videoDepoimento;

function trocaVideo(id) {
  $("#video").remove();
  $(".float").prepend('<div id="video"></div>');

  videoDepoimento = new YT.Player('video', {
        videoId: id
    });
}



$(function(){

    // carrega menu
    $('#topo').load('topo.html', function(){
      $(".menu-mobile").on( "click", function() {
          $(".menu").toggleClass( "hover" );
          $(".menu-mobile").toggleClass( "hover" );
        });
    });

    $('#rodape').load('rodape.html');
        
    $('#tabs li a').click(function(e){
        $('#tabs li, #tabs-content .current').removeClass('current').removeClass('fadeInLeft');
        $(this).parent().addClass('current');
	    var currentTab = $(this).attr('href');
	    $(currentTab).addClass('current fadeInLeft');
	    e.preventDefault();
    });



	$(window).load(function(){
        $(".tabs-content-scrool").mCustomScrollbar({
    		advanced: {
                    updateOnContentResize: true
                }
        });
    });    


  $(".guia-conteudo #tabs li a").on( "click", function() {
      $(".guia-conteudo #tabs").toggleClass( "hover" );
    });



  $('.depoimentos a').click(function() {
    var dataid = $(this).attr('data-id-video');
    $('.overlay').show();
    $('.float').css('left','50%');
    trocaVideo(dataid);
    return false;
  });
  $('.overlay, .fechar-float').click(function () {
    $('.overlay').hide();
    $('.float').css('left','-100%');
    $("#video").remove();
    $(".float").prepend('<div id="video"></div>');
    return false;
  });
  $(".lista-miniaturas-float").jCarouselLite({
      btnNext: ".next",
      btnPrev: ".prev",
      visible: 4,
      speed: 800,
      vertical: true
  });
  $('.miniaturas-float li a').click(function () {
    var dataid = $(this).attr('data-id-video');
    trocaVideo(dataid);
    return false;
  });



});
