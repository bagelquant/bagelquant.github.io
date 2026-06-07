(function() {
  var STORAGE_KEY = 'bagelquant.language';
  var SCROLL_STORAGE_KEY = 'bagelquant.languageScroll';
  var DEFAULT_LANG = 'en';

  function normalizeLang(lang) {
    return lang === 'zh' || /^zh\b/i.test(lang || '') ? 'zh' : DEFAULT_LANG;
  }

  function pageLang() {
    return normalizeLang(document.documentElement.dataset.pageLang || document.documentElement.lang);
  }

  function savedLanguage() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      return saved ? normalizeLang(saved) : null;
    } catch (e) {
      return null;
    }
  }

  function preferredLanguage() {
    return savedLanguage() || pageLang();
  }

  function saveLanguage(lang) {
    try { localStorage.setItem(STORAGE_KEY, normalizeLang(lang)); } catch (e) {}
  }

  function scrollMax() {
    return Math.max(
      document.documentElement.scrollHeight,
      document.body ? document.body.scrollHeight : 0
    ) - window.innerHeight;
  }

  function saveScrollPosition() {
    var max = scrollMax();
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    var payload = {
      path: window.location.pathname,
      ratio: max > 0 ? y / max : 0,
      y: y,
      savedAt: Date.now()
    };

    try {
      sessionStorage.setItem(SCROLL_STORAGE_KEY, JSON.stringify(payload));
    } catch (e) {}
  }

  function readScrollPosition() {
    try {
      var raw = sessionStorage.getItem(SCROLL_STORAGE_KEY);
      if (!raw) return null;
      sessionStorage.removeItem(SCROLL_STORAGE_KEY);
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  function restoreScrollPosition() {
    var payload = readScrollPosition();
    if (!payload || Date.now() - payload.savedAt > 10000) return;

    var restore = function() {
      var max = scrollMax();
      var savedY = typeof payload.y === 'number' ? payload.y : payload.ratio * max;
      var y = max > 0 ? Math.min(max, Math.max(0, savedY)) : 0;
      window.scrollTo(0, y);
    };

    restore();
    window.requestAnimationFrame(function() {
      restore();
      window.setTimeout(restore, 120);
      window.setTimeout(restore, 320);
      window.setTimeout(restore, 700);
    });
  }

  function isSkippableHref(href) {
    if (!href) return true;
    if (href.charAt(0) === '#') return true;
    if (/^(https?:|mailto:|tel:|javascript:)/i.test(href)) return true;
    if (/^\/?(assets|favicon\.ico|favicon\.svg|site\.webmanifest|apple-touch-icon\.png|search\.json)\b/.test(href)) return true;
    return false;
  }

  function localizePath(path, lang) {
    if (isSkippableHref(path)) return path;

    var hash = '';
    var hashIndex = path.indexOf('#');
    if (hashIndex !== -1) {
      hash = path.slice(hashIndex);
      path = path.slice(0, hashIndex);
    }

    var query = '';
    var queryIndex = path.indexOf('?');
    if (queryIndex !== -1) {
      query = path.slice(queryIndex);
      path = path.slice(0, queryIndex);
    }

    if (lang === 'zh') {
      if (path === '/' || path === '') return '/zh/' + query + hash;
      if (path.indexOf('/zh/') === 0) return path + query + hash;
      return '/zh' + path + query + hash;
    }

    if (path === '/zh/' || path === '/zh') return '/' + query + hash;
    if (path.indexOf('/zh/') === 0) return path.slice(3) + query + hash;
    return path + query + hash;
  }

  function rewriteLinks(lang) {
    Array.prototype.forEach.call(document.querySelectorAll('a[href]'), function(a) {
      if (a.matches('[data-language-toggle], [target="_blank"]')) return;
      var href = a.getAttribute('href');
      if (isSkippableHref(href)) return;
      a.setAttribute('href', localizePath(href, lang));
    });
  }

  function prefersReducedMotion() {
    return window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function isPlainLeftClick(event) {
    return event.button === 0 &&
      !event.defaultPrevented &&
      !event.metaKey &&
      !event.ctrlKey &&
      !event.shiftKey &&
      !event.altKey;
  }

  function isSameWindowNavigation(link) {
    var target = link.getAttribute('target');
    return !target || target.toLowerCase() === '_self';
  }

  function handleLanguageToggle(event) {
    saveLanguage(pageLang() === 'zh' ? 'en' : 'zh');

    if (!isPlainLeftClick(event) || !isSameWindowNavigation(this)) return;

    var href = this.href;
    if (!href) return;

    saveScrollPosition();

    if (prefersReducedMotion()) return;

    event.preventDefault();
    document.documentElement.classList.add('is-language-switching');

    window.setTimeout(function() {
      window.location.href = href;
    }, 180);
  }

  document.addEventListener('DOMContentLoaded', function() {
    var lang = preferredLanguage();
    document.documentElement.dataset.lang = lang;
    if (lang === 'zh') document.documentElement.lang = 'zh-CN';

    if (!savedLanguage()) saveLanguage(lang);

    var toggle = document.getElementById('language-toggle');
    if (toggle) {
      toggle.addEventListener('click', handleLanguageToggle);
    }

    rewriteLinks(lang);
    restoreScrollPosition();

    window.dispatchEvent(new CustomEvent('bagelquant:languagechange', {
      detail: { language: lang }
    }));
  });

  window.BagelQuantI18n = {
    currentLanguage: preferredLanguage,
    saveLanguage: saveLanguage,
    localizePath: localizePath,
    rewriteLinks: rewriteLinks
  };

  window.addEventListener('pageshow', function() {
    document.documentElement.classList.remove('is-language-switching');
  });
})();
