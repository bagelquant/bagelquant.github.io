(function() {
  function setupTopNavToggle() {
    var mq = window.matchMedia('(max-width: 720px)');
    var nav = document.querySelector('.site-nav');
    if (!nav) return;

    var btn = nav.querySelector('.nav-toggle');
    var list = nav.querySelector('.nav-list');
    if (!btn || !list) return;

    function closeMenu() {
      list.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    }

    btn.addEventListener('click', function() {
      var isOpen = list.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    list.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', closeMenu);
    });

    mq.addEventListener('change', function(e) {
      if (!e.matches) closeMenu();
    });
  }

  function setupSidebarToggle() {
    var mq = window.matchMedia('(max-width: 960px)');
    var initialized = false;

    function setupToggle() {
      if (!mq.matches || initialized) return;
      initialized = true;

      var sidebar = document.querySelector('.page-sidebar') || document.querySelector('.post-sidebar-left');
      if (!sidebar) return;
      if (!sidebar.querySelector('a, li')) return;

      var layout = document.querySelector('.layout-three-column');
      if (!layout || layout.querySelector('.sidebar-toggle')) return;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'sidebar-toggle';
      btn.setAttribute('aria-label', 'Toggle navigation');
      btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        + '<path d="M3 6h18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<path d="M3 12h18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<path d="M3 18h18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        + '</svg>';
      btn.addEventListener('click', function() {
        sidebar.classList.toggle('is-open');
      });

      layout.insertBefore(btn, layout.firstElementChild);
    }

    setupToggle();
    mq.addEventListener('change', function(e) {
      if (e.matches) setupToggle();
    });
  }

  function setupToc() {
    var content = document.querySelector('.post-content.numbered');
    var layout = document.querySelector('.layout-three-column');
    var tocContainer = document.querySelector('.post-toc .toc-inner') ||
                       document.querySelector('.page-toc .toc-inner');
    var tocAside = tocContainer ? tocContainer.closest('.post-toc, .page-toc') : null;

    function removeEmptyToc() {
      if (tocAside) tocAside.remove();
      if (layout) layout.classList.remove('has-toc');
    }

    if (!content) {
      removeEmptyToc();
      return;
    }

    var pageOptions = window.BagelQuantPage || {};
    if (pageOptions.toc === false) {
      removeEmptyToc();
      return;
    }

    var headings = content.querySelectorAll('h2, h3');
    if (!headings.length) {
      removeEmptyToc();
      return;
    }

    if (!tocContainer) return;

    tocContainer.innerHTML = '';

    var headingEl = document.createElement('h2');
    var isZh = document.documentElement.dataset.lang === 'zh' ||
      document.documentElement.lang.toLowerCase().indexOf('zh') === 0;
    headingEl.textContent = isZh ? '本文目录' : 'In this article';
    headingEl.setAttribute('data-i18n', 'toc.title');

    var ul = document.createElement('ul');
    var h2Count = 0;
    var h3Count = 0;

    headings.forEach(function(h) {
      var headingText = getHeadingText(h);
      if (!h.id) {
        h.id = headingText.toLowerCase()
          .replace(/[^\w\- ]+/g, '')
          .replace(/\s+/g, '-');
      }

      var li = document.createElement('li');
      li.className = 'toc-level-' + h.tagName.toLowerCase();

      var a = document.createElement('a');
      a.href = '#' + h.id;

      var tag = h.tagName.toLowerCase();
      var numberText = '';
      if (tag === 'h2') {
        h2Count += 1;
        h3Count = 0;
        numberText = h2Count + '.\u00A0';
      } else if (tag === 'h3') {
        if (h2Count === 0) h2Count = 1;
        h3Count += 1;
        numberText = h2Count + '.' + h3Count + '.\u00A0';
      }

      a.textContent = (numberText ? numberText : '') + headingText;
      li.appendChild(a);
      ul.appendChild(li);
    });

    tocContainer.appendChild(headingEl);
    tocContainer.appendChild(ul);
  }

  function getHeadingText(heading) {
    var clone = heading.cloneNode(true);
    clone.querySelectorAll('.heading-number').forEach(function(number) {
      number.remove();
    });
    return clone.textContent.trim();
  }

  function setupHeadingNumbers() {
    var containers = document.querySelectorAll('.post-content.numbered');
    if (!containers.length) return;

    containers.forEach(function(container) {
      var headings = container.querySelectorAll('h2, h3');
      var h2Count = 0;
      var h3Count = 0;

      headings.forEach(function(h) {
        var tag = h.tagName.toLowerCase();
        if (h.querySelector('.heading-number')) return;

        if (tag === 'h2') {
          h2Count += 1;
          h3Count = 0;
          addNumber(h, h2Count + '.\u00A0');
        } else if (tag === 'h3') {
          if (h2Count === 0) h2Count = 1;
          h3Count += 1;
          addNumber(h, h2Count + '.' + h3Count + '.\u00A0');
        }
      });
    });
  }

  function addNumber(heading, text) {
    var span = document.createElement('span');
    span.className = 'heading-number';
    span.setAttribute('aria-hidden', 'true');
    span.textContent = text;
    heading.insertBefore(span, heading.firstChild);
  }

  function setupThemeToggle() {
    var STORAGE_KEY = 'theme';

    function applyTheme(theme) {
      if (theme === 'dark') document.documentElement.classList.add('dark');
      else document.documentElement.classList.remove('dark');

      var btn = document.getElementById('theme-toggle');
      if (btn) btn.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
    }

    var btn = document.getElementById('theme-toggle');
    if (!btn) return;

    var saved = null;
    try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) { saved = null; }

    if (saved === 'dark' || saved === 'light') {
      applyTheme(saved);
    } else {
      var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      applyTheme(prefersDark ? 'dark' : 'light');
    }

    btn.addEventListener('click', function() {
      var isDark = document.documentElement.classList.contains('dark');
      var next = isDark ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    setupTopNavToggle();
    setupSidebarToggle();
    setupHeadingNumbers();
    setupToc();
    setupThemeToggle();
  });
})();
