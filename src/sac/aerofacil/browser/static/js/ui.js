(function($) {
    "use strict";
    $(document).ready(function() {

        $(".menu-mobile").on("click", function() {
            $(".menu").toggleClass("hover");
            $(".menu-mobile").toggleClass("hover");
        });

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

        var lista_noticias = $(".lista-noticias");
        if (lista_noticias.length) {
          lista_noticias.flexslider({
            animation: "slide",
            controlNav: false  
          });
        }

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
})(jQuery);
