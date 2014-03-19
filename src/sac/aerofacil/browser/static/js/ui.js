;(function($) {
    "use strict";
    $(document).ready(function() {


        // GERAL

        $(".menu-mobile").on("click", function() {
            $(".menu").toggleClass("hover");
            $(".menu-mobile").toggleClass("hover");
        });


        // HOME

        var current_url = location.protocol + '//' + location.host + location.pathname;
        if ((current_url === portal_url) || (current_url.slice(0, -1) === portal_url)) {

            $('.menu a').on('click', function() {
                var rel = $(this).data('rel');
                var dist = $('.' + rel).offset().top;
                $('html, body').animate({
                    scrollTop: dist
                }, 1000);
                return false;
            });

            $('.menu-flutuante a').on('click', function() {
                var rel = $(this).data('rel');
                var dist = $('.' + rel).offset().top;
                $('html, body').animate({
                    scrollTop: dist
                }, 1000);
                return false;
            });

            $(window).scroll(function() {
                var scr = $(window).scrollTop();
                if (scr < 400) {
                    $('.menu-flutuante').hide();
                } else {
                    $('.menu-flutuante').show();
                }
            });

            $('.bloco-informacoes .lk-seta-left').click(function() {
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

            $('.lk-aeroporto-home').click(function() {
                $(this).hide();
                $('.select-aeroporto-home').fadeIn();
                return false;
            });

            $('.select-aeroporto-home').change(function() {
                var aero = $(this).val();
                if (aero !== "") {
                    location.href = portal_url + "/aeroportos-brasileiros/" + aero;
                }
            });

        }


        // APLICATIVOS

        else if (location.href.indexOf("/aplicativos-e-ferramentas") != -1) {

            $('.aplicativos-interna').flexslider({
                animation: "slide",
                controlNav: false
            });

        }


        // AEROPORTOS

        else if (location.href.indexOf("/aeroportos-brasileiros") != -1) {

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

            $('.lk-outro-aero').click(function() {
                $(this).hide();
                $('.select-aeroporto').fadeIn();
                return false;
            });

            $('.marcadores-apps a').click(function() {
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

            $('.select-aeroporto').change(function() {
                var val = $(this).val();
                if (val === "") {
                    return false;
                }
                var new_url = portal_url + '/aeroportos-brasileiros/' + val;
                var new_title = document.title.split(" | ");
                new_title[0] = $(':selected', this).text();
                new_title = new_title.join(" | ");
                $('#aeroporto').load(new_url + ' #aeroporto', function(html) {
                    var new_html = $("#aeroporto", html).html();
                    var new_options = $(".select-aeroporto", $(html)).children();
                    document.title = new_title + " | Aeroportos brasileiros | Aerofácil";
                    window.history.pushState({"html": new_html, "pageTitle": new_title}, '', new_url);
                    $(".select-aeroporto").fadeOut("fast", function() {
                        $(this).html(new_options).fadeIn("fast");
                    });
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
            });

            window.onpopstate = function(e) {
                if (e.state) {
                    document.getElementById("aeroporto").innerHTML = e.state.html;
                    document.title = e.state.pageTitle;
                }
            };

        }


        // DESTAQUES

        else if (location.href.indexOf("/destaques") != -1) {

            $(".aplicativos-interna").jCarouselLite({
                btnNext: ".next",
                btnPrev: ".prev",
                visible: 1,
                speed: 800
            });

            $("#miolo-noticias").mCustomScrollbar({
                advanced: {
                    updateOnContentResize: true
                }
            });

        }


        // NOTÍCIAS

        else if (location.href.indexOf("/noticias") != -1) {

            $("#miolo-noticias").mCustomScrollbar({
                advanced: {
                    updateOnContentResize: true
                }
            });

            $('.outras-noticias a').click(function(e) {
                e.preventDefault();
                var noticia = $(this).attr('href').split('/');
                noticia = noticia[noticia.length - 1];
                var new_url = portal_url + '/noticias/' + noticia;
                var new_title = document.title.split(" — ");
                new_title[0] = $(this).text();
                new_title = new_title.join(" — ");
                $('#miolo-noticias').load(new_url + ' #content', function(html) {
                    var new_html = $("#miolo-noticias", html).html();
                    document.title = new_title;
                    window.history.pushState({"html": new_html, "pageTitle": new_title}, '', new_url);
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

            window.onpopstate = function(e) {
                if (e.state) {
                    document.getElementById("miolo-noticias").innerHTML = e.state.html;
                    document.title = e.state.pageTitle;
                }
            };


        }


        // GUIA DO PASSAGEIRO

        else if (location.href.indexOf("/guia-do-passageiro") != -1) {

            var tag = document.createElement('script');
            tag.src = "//www.youtube.com/player_api";
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

            var videoDepoimento;

            $('#tabs li a').click(function(e) {
                $('#tabs .current, #tabs-content .current').removeClass('current').removeClass('fadeInLeft');
                $(this).parent().addClass('current');
                var currentTab = $(this).attr('href');
                $(currentTab).addClass('current fadeInLeft');
                e.preventDefault();
            });

            $(".tabs-content-scroll").mCustomScrollbar({
                advanced: {
                    updateOnContentResize: true
                }
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

            $('.section-guia-do-passageiro').prepend($('.overlay, .float'));

            $('.section-guia-do-passageiro .overlay, .fechar-float').click(function() {
                $('.overlay').hide();
                $('.float').css('left', '-100%');
                $("#video").remove();
                $(".float").prepend('<div id="video"></div>');
                return false;
            });

            var miniaturas = $(".lista-miniaturas-float");

            if ($('li', miniaturas).length > 4) {
                miniaturas.jCarouselLite({
                    btnNext: ".next",
                    btnPrev: ".prev",
                    visible: 4,
                    speed: 800,
                    vertical: true
                });
            }

            $('a', miniaturas).click(function() {
                var dataid = $(this).attr('data-id-video');
                trocaVideo(dataid);
                return false;
            });

        }

        function trocaVideo(id) {
            $("#video").remove();
            $(".float").prepend('<div id="video"></div>');
            videoDepoimento = new YT.Player('video', {
                videoId: id
            });
        }

    });
})(jQuery);
