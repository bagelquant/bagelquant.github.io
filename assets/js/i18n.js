(function() {
  var STORAGE_KEY = 'bagelquant.language';
  var DEFAULT_LANG = 'en';

  function normalizeLang(lang) {
    return lang === 'zh' || /^zh\b/i.test(lang || '') ? 'zh' : DEFAULT_LANG;
  }

  function currentLang() {
    return normalizeLang(document.documentElement.lang || DEFAULT_LANG);
  }

  function saveLanguage(lang) {
    try { localStorage.setItem(STORAGE_KEY, normalizeLang(lang)); } catch (e) {}
  }

  document.addEventListener('DOMContentLoaded', function() {
    var lang = currentLang();
    document.documentElement.dataset.lang = lang;
    saveLanguage(lang);

    var toggle = document.getElementById('language-toggle');
    if (toggle) {
      toggle.addEventListener('click', function() {
        saveLanguage(lang === 'zh' ? 'en' : 'zh');
      });
    }

    window.dispatchEvent(new CustomEvent('bagelquant:languagechange', {
      detail: { language: lang }
    }));
  });

  window.BagelQuantI18n = {
    currentLanguage: currentLang,
    saveLanguage: saveLanguage
  };
})();
