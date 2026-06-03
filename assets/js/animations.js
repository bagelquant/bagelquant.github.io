(function() {
  document.addEventListener('DOMContentLoaded', function() {
    const autoTargets = document.querySelectorAll(
      '.home-content > *, .post-content > *, .page-sidebar, .post-sidebar-left, .page-toc, .post-toc, .author-profile'
    );
    autoTargets.forEach((target, index) => {
      if (!target.classList.contains('fade-in-on-scroll')) {
        target.classList.add('fade-in-on-scroll');
        target.style.transitionDelay = `${Math.min(index * 35, 280)}ms`;
      }
    });

    const targets = document.querySelectorAll('.fade-in-on-scroll');
    if (!targets.length) return;

    if (!('IntersectionObserver' in window)) {
      targets.forEach(target => target.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          // Optional: stop observing the element once it's visible
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1 // Trigger when at least 10% of the element is visible
    });

    targets.forEach(target => {
      observer.observe(target);
    });
  });
})();
