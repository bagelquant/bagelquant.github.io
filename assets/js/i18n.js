(function() {
  var STORAGE_KEY = 'bagelquant.language';
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

  document.addEventListener('DOMContentLoaded', function() {
    var lang = preferredLanguage();
    document.documentElement.dataset.lang = lang;
    if (lang === 'zh') document.documentElement.lang = 'zh-CN';

    if (!savedLanguage()) saveLanguage(lang);

    var toggle = document.getElementById('language-toggle');
    if (toggle) {
      toggle.addEventListener('click', function() {
        saveLanguage(pageLang() === 'zh' ? 'en' : 'zh');
      });
    }

    rewriteLinks(lang);

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
})();
