(function ($) {
  "use strict";

  /* ---- CUSTOM CURSOR ---- */
  var dot = document.getElementById('cursor-dot');
  var ring = document.getElementById('cursor-ring');
  if (dot && ring) {
    document.addEventListener('mousemove', function (e) {
      dot.style.left = e.clientX + 'px';
      dot.style.top = e.clientY + 'px';
      setTimeout(function () {
        ring.style.left = e.clientX + 'px';
        ring.style.top = e.clientY + 'px';
      }, 60);
    });
    document.querySelectorAll('a, button, .bizwheel-btn, .single-team').forEach(function (el) {
      el.addEventListener('mouseenter', function () { dot.classList.add('hover-state'); ring.classList.add('hover-state'); });
      el.addEventListener('mouseleave', function () { dot.classList.remove('hover-state'); ring.classList.remove('hover-state'); });
    });
  }

  $(document).ready(function () {

    /* ---- STICKY HEADER ---- */
    $(window).on('scroll', function () {
      if ($(this).scrollTop() > 1) {
        $('.header').addClass('sticky');
      } else {
        $('.header').removeClass('sticky');
      }
    });

    /* ---- MOBILE MENU ---- */
    if ($('.main-menu').length) {
      $('.main-menu').slicknav({
        prependTo: ".mobile-nav",
        label: '',
        duration: 300,
        easingOpen: "easeOutBounce"
      });
    }

    /* ---- HOME SLIDER (autoplay ON) ---- */
    if ($('.home-slider').length) {
      $('.home-slider').owlCarousel({
        items: 1,
        autoplay: true,
        autoplayTimeout: 4500,
        smartSpeed: 800,
        autoplayHoverPause: true,
        loop: true,
        nav: true,
        dots: true,
        animateOut: 'fadeOut',
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>']
      });
    }

    /* ---- SCROLL REVEAL ---- */
    function revealOnScroll() {
      var scrollTop = $(window).scrollTop();
      var windowHeight = $(window).height();
      $('.reveal, .reveal-left, .reveal-right').each(function (i) {
        var elemTop = $(this).offset().top;
        if (elemTop < scrollTop + windowHeight - 60) {
          var self = this;
          setTimeout(function () {
            $(self).addClass('visible');
          }, i * 60);
        }
      });
    }
    revealOnScroll();
    $(window).on('scroll', revealOnScroll);

    /* ---- VIDEO POPUP ---- */
    if ($('.video-popup').length) {
      $('.video-popup').magnificPopup({ type: 'iframe', removalDelay: 300, mainClass: 'mfp-fade' });
    }

    /* ---- SCROLL UP ---- */
    if (typeof $.scrollUp === 'function') {
      $.scrollUp({
        scrollDistance: 300,
        scrollSpeed: 900,
        animationSpeed: 200,
        scrollText: "<i class='fa fa-angle-up'></i>"
      });
    }

    /* ---- PRELOADER ---- */
    // Hide immediately after DOM is parsed so users don't wait for heavy images
    setTimeout(function () {
      $(".preeloader").fadeOut(200, function () { $(this).remove(); });
    }, 50);
    
    $(window).on('load', function () {
      $(".preeloader").fadeOut(100, function () { $(this).remove(); });
    });

    /* ---- TEAM CARD CLICK ---- */
    $('.single-team').on('click', function () { $(this).toggleClass('active'); });

    /* ---- STAT NUMBER COUNTER ---- */
    if ($('.number').length && typeof $.fn.counterUp === 'function') {
      $('.number').counterUp({ time: 1500 });
    }

    /* ---- SMOOTH INTERNAL LINK SCROLL ---- */
    $('a[href^="#"]').on('click', function (e) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: target.offset().top - 70 }, 600);
      }
    });

    /* ---- PAGE TRANSITION ON LINK CLICK ---- */
    var $pt = $('.page-transition');
    if ($pt.length) {
      $(document).on('click', 'a:not([href^="#"]):not([target="_blank"]):not([href^="mailto"]):not([href^="tel"]):not([href^="javascript"])', function (e) {
        var href = $(this).attr('href');
        if (!href || href === '#') return;
        e.preventDefault();
        $pt.addClass('active');
        setTimeout(function () { window.location = href; }, 400);
      });
    }

    /* ---- HOVER LIFT on cards ---- */
    $('.single-team, .contact-form-area, .contact-box-main').on('mouseenter', function () {
      $(this).css('transform', 'translateY(-6px)');
    }).on('mouseleave', function () {
      $(this).css('transform', '');
    });

  });

})(jQuery);
