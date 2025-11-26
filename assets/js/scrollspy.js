(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var content = document.querySelector('.post-content.numbered');
    if (!content) return;

    var headings = Array.from(content.querySelectorAll('h2, h3'));
    if (!headings.length) return;

    var tocContainer = document.querySelector('.post-toc .toc-inner') ||
                       document.querySelector('.page-toc .toc-inner');
    if (!tocContainer) return;

    // The TOC links might be generated dynamically.
    // We need to wait for them to be present.
    // We can use a MutationObserver or a simple timer.
    // Let's try a timer first.
    var initScrollspy = function() {
      var tocLinks = Array.from(tocContainer.querySelectorAll('a'));
      if (!tocLinks.length) {
        // If no links, TOC might not be built yet. Retry shortly.
        setTimeout(initScrollspy, 100);
        return;
      }

      var throttleTimeout;
      function throttle(callback, limit) {
        if (!throttleTimeout) {
          throttleTimeout = setTimeout(function() {
            callback();
            throttleTimeout = null;
          }, limit);
        }
      }

      function onScroll() {
        var scrollPosition = window.scrollY;
        var activeHeading = null;

        // An offset to account for sticky header or other elements at the top.
        // 1.75rem (margin) + a bit more. Let's say 50px.
        var offset = 50; 

        headings.forEach(function(h) {
          if (h.offsetTop - offset <= scrollPosition) {
            activeHeading = h;
          }
        });
        
        tocLinks.forEach(function(a) {
          a.classList.remove('active');
        });

        if (activeHeading) {
          var activeLink = tocLinks.find(function(a) {
            return a.getAttribute('href') === '#' + activeHeading.id;
          });
          if (activeLink) {
            activeLink.classList.add('active');
          }
        }
      }

      window.addEventListener('scroll', function() {
        throttle(onScroll, 100);
      });

      // Initial check
      onScroll();
    };

    initScrollspy();
  });
})();
