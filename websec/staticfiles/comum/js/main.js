// Variáveis
window.__admin_media_prefix__ = "/static/admin/";

function open_menu_item(menu_item_id) {
    elem = jQuery("#menu-item-" + menu_item_id);
    elem.addClass("active");
    elem.parents("li").addClass("active").toggleClass("opened");
    elem.parents("ul,li").show();
}

function mode_responsive() {
    if ($(window).width() < 940) {
        $("body").addClass("hideSidebar");
    }
}

function initAll() {
    
    /* Menu principal: Toggle Sidebar */
    menu_hide_sidebar = function(){
        jQuery("nav > ul > li").removeClass("hint--right");
        jQuery("nav > ul > li").removeAttr("data-hint");
    };
    
    /* Menu principal */
    jQuery("nav li.has-child > a").click(function(e){
        e.preventDefault();
        if (jQuery("body").hasClass("hideSidebar")) {
            menu_hide_sidebar();
            jQuery("body").removeClass("hideSidebar");
        }
        $(this).parent("li").toggleClass("opened");
        $(this).next("ul").toggle(); 
    });
    
    /* Menu principal: Toggle Sidebar */
    jQuery("#acoes.toggleSidebar").click(function(e){
        e.preventDefault();
        if (jQuery("body").hasClass("hideSidebar")) {
            jQuery("html, body").animate({scrollTop: "0px"}, 'slow');
            menu_hide_sidebar();
            jQuery("nav li.opened > ul").show("slow");
        } else {
            jQuery("nav > ul > li").addClass("hint--right");
            jQuery("nav > ul > li").each(function(){
                var texto = jQuery(this).find("> a").text();
                jQuery(this).attr("data-hint", texto);
                $(this).find("ul").hide();
            });
        }
        jQuery("body").toggleClass("hideSidebar");
    });
    
    /* Menu principal: Para dispositivos moveis */
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        $("body").addClass("hideSidebar");
    }
    
    // Responsive mode
    mode_responsive();
    $(window).resize(function() {
        mode_responsive();
    });

	/* Action Bar */
    jQuery(".action-bar .has-child > a").click(function() {
        jQuery(this).next("ul").toggle();
        return false;
    });
    jQuery(".action-bar .has-child ul").hover(function() {
	}, function () {
		jQuery(this).hide("fast");
	});

	/* Box */
    jQuery(".box h3").click(function() {
        jQuery(this).parent().find("> div").animate({
            height: 'toggle'
        });
        jQuery(this).parent().toggleClass("hideInfo");
        var atributo = jQuery(this).attr("title");
        if (atributo == "Mostrar informações") {
            jQuery(this).attr("title", "Esconder informações");
        } else {
            jQuery(this).attr("title", "Mostrar informações");
        }
        return false;
    });

    /* Action Links */
    jQuery(".action-print a").click(function() {
	    print();
        return false;
    });
    jQuery("#topodapagina").click(function(){
		jQuery('html, body').animate({scrollTop:0}, 'slow');
	});

	/* Âncoras */
	jQuery(".ancoras").click(function() {
		jQuery(this).toggleClass("hideInfo");
		jQuery(".com_ancora").toggleClass("hideInfo");
	});
	jQuery(".ancoras a").click(function() {
		var link = jQuery(this).attr("href");
		var destino = jQuery(link).offset().top;
		jQuery("html, body").animate({scrollTop: destino}, 'slow');
        return false;
	});
	jQuery(".ancoras-telefones a").click(function() {
		var link = jQuery(this).attr("href");
		jQuery(".ancoras-telefones li").removeClass("selected");
		jQuery(this).parent("li").addClass("selected");
		jQuery("div.container").hide();
		jQuery(link).parent("div.container").show();
		var destino = jQuery(link).offset().top;
		jQuery("html, body").animate({scrollTop: destino}, 'slow');
        return false;
	});

    /* Barra de progresso */
    jQuery(".progress p").each(function() {
        var texto = jQuery(this).text();
        var porcentagem = texto.indexOf("%");
        if (porcentagem==-1) {
            var split = texto.split('/');
            texto = split[0]*100/split[1] + "%";
        }
        jQuery(this).css("width", texto);
        jQuery(this).parent().attr("title", texto);
    });
    
    jQuery(".confirm, .danger, .icon-trash").not(".no-confirm").click(function() {
        return confirm(jQuery(this).attr("data-confirm") || "Tem certeza que deseja continuar?");
    });
    
    jQuery(".voltar").click(function() {
        window.history.back();
    });

	jQuery("#menu-device a").click(function(){
		jQuery('nav > ul').toggle();
	});
    
    // Mapeamento de classes e title's
    mapeamento_class_title = {
        csv: "Exportar para CSV",
        pdf: "Exportar para PDF",
        editar16: "Editar",
        remover16: "Remover",
        detalhar16: "Detalhar",
        upload16: "Enviar Arquivo",
        cracha16: "Gerar crachá",
        carteira16: "Gerar carteira"
    };
    for (key in mapeamento_class_title) {
        jQuery.each(jQuery("a."+key), function(index, value) {
            elem = jQuery(value);
            if (elem.attr("title") == "") {
                elem.attr("title", mapeamento_class_title[key]);
            }
        });
    }
    
    // Caso a div#action-bar não tenha conteúdo, ela é removida
    if (jQuery("div#action-bar").html() == "") {
        jQuery("div#action-bar").remove();
    }
	
	// Expandir
	jQuery(".action-bar .normalscreen").hide();
	jQuery(".action-bar .fullscreen").click(function() {
		jQuery(this).hide();
		jQuery("header, footer, h2").hide();
		jQuery(".action-bar .normalscreen").show();
		jQuery("#content").addClass("fullscreen");
	});
	jQuery(".action-bar .normalscreen").click(function() {
		jQuery(this).hide();
		jQuery("header, footer, h2").show();
		jQuery(".action-bar .fullscreen").show();
		jQuery("#content").removeClass("fullscreen");
	});
    
    // Remove o ícone padrão do Django por um do estilo
    jQuery(".selector-chosen .selector-filter img").attr("src", "/static/comum/img/selector-choosen.png");
    
    // Módulo de Abas da página inicial
    function moduloAbas(aba) {
        if (!jQuery(aba).hasClass("active")) {
            jQuery(aba).parent().find("h4").removeClass("active");
            jQuery(aba).addClass("active");   
        }
    }
    jQuery(".modulo-abas h4").click(function() {
        moduloAbas(this);
    });
    
}
jQuery(document).ready(function() {initAll()});