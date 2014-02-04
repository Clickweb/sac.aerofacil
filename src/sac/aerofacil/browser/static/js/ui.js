(function($) {
    "use strict";
    $(document).ready(function() {

        // GERAL

        $('.menu a').on('click', function() {
            var rel = $(this).attr('rel');
            var dist = $('.' + rel).offset().top;
            $('html, body').animate({
                scrollTop: dist
            }, 1000);
            return false;
        });

        $(".menu-mobile").on("click", function() {
            $(".menu").toggleClass("hover");
            $(".menu-mobile").toggleClass("hover");
        });

        $('.menu-flutuante a').on('click', function() {
            var rel = $(this).attr('rel');
            var dist = $('.' + rel).offset().top;
            $('html, body').animate({
                scrollTop: dist
            }, 1000);
            return false;
        });

        $(window).scroll(function () {
            var scr = $(window).scrollTop();
            if (scr < 400) {
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

        var lista_noticias = $(".lista-noticias");
        if (lista_noticias.length) {
            lista_noticias.flexslider({
                animation: "slide",
                controlNav: false
            });
        }

        $('.menu a').on('click', function() {
            var rel = $(this).attr('rel');
            var dist = $('.' + rel).offset().top;
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
            $('#aeroporto').load('aeroportos-brasileiros/' + val, function () {
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
            location.href = "aeroportos-brasileiros/" + val;
        });

        // APLICATIVOS

        $('.aplicativos-interna').flexslider({
            animation: "slide",
            controlNav: false
        });

        // AEROPORTOS

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
            if (!$(this).hasClass('externo')) {
                $(this).parent().find('span').slideToggle();
                return false;
            }
        });

        // TODO: Criar browser view que entregue somente o miolo da página
        var aero = $(location).attr('href');
        aero = aero.split('/');
        aero = aero[aero.length - 1];
        if (aero) {
            $('#aeroporto').load('aeroportos/' + aero + ' #aeroporto', function () {
                $('.item-aero a').click(function() {
                    if (!$(this).hasClass('externo')) {
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
            if (!$(this).hasClass('ativo')) {
                var id = $(this).html();
                id = parseInt(id);
                console.log(id);
                $('.box-apps-aero').fadeOut();
                $('#app-' + id).fadeIn();
                $('.ativo').removeClass('ativo');
                $(this).addClass('ativo');
            }
            return false;
        });

        // DESTAQUES

        $(".aplicativos-interna").jCarouselLite({
            btnNext: ".next",
            btnPrev: ".prev",
            visible: 1,
            speed: 800
        });

        // NOTÍCIAS

        var noticia = $(location).attr('href');
        noticia = noticia.split('/');
        noticia = noticia[noticia.length - 1];
        $('#miolo-noticias').load('noticias/' + noticia, function() {
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
            var noticia = $(this).attr('href');
            noticia = noticia.split('/');
            noticia = noticia[noticia.length - 1];
            $('#miolo-noticias').load('noticias/' + noticia, function() {
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

        // GUIA DO PASSAGEIRO

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

        $('#tabs li a').click(function(e) {
            $('#tabs li, #tabs-content .current').removeClass('current').removeClass('fadeInLeft');
            $(this).parent().addClass('current');
            var currentTab = $(this).attr('href');
            $(currentTab).addClass('current fadeInLeft');
            e.preventDefault();
        });

      $(window).load(function() {
          $(".tabs-content-scrool").mCustomScrollbar({
              advanced: {
                  updateOnContentResize: true
              }
          });
      });    

      $(".guia-conteudo #tabs li a").on("click", function() {
          $(".guia-conteudo #tabs").toggleClass("hover");
      });

      $('.depoimentos a').click(function() {
          var dataid = $(this).attr('data-id-video');
          $('.overlay').show();
          $('.float').css('left', '50%');
          trocaVideo(dataid);
          return false;
      });

      $('.overlay, .fechar-float').click(function() {
          $('.overlay').hide();
          $('.float').css('left', '-100%');
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

      $('.miniaturas-float li a').click(function() {
        var dataid = $(this).attr('data-id-video');
        trocaVideo(dataid);
        return false;
      });

    });
})(jQuery);
