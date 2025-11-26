(function() {
  document.addEventListener('DOMContentLoaded', function() {
    const targets = document.querySelectorAll('.fade-in-on-scroll');
    if (!targets.length) return;

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
