(function() {
  var STORAGE_KEY = 'bagelquant.language';
  var DEFAULT_LANG = 'en';
  var CHINESE_COUNTRIES = ['CN', 'HK', 'MO', 'TW', 'SG'];

  var dictionary = {
    en: {
      'nav.home': 'Home',
      'nav.quick_start': 'Quick Start',
      'nav.learn': 'Learn',
      'nav.research': 'Research',
      'nav.projects': 'Projects',
      'nav.docs': 'Docs',
      'nav.app': 'App',
      'nav.about': 'About Me',
      'nav.search_label': 'Search site',
      'nav.theme_label': 'Toggle dark mode',
      'nav.lang_label': 'Switch language',
      'layout.navigation': 'Navigation',
      'layout.home': 'Home',
      'toc.title': 'In this article',
      'home.title': 'BagelQuant',
      'home.subtitle': 'Quantitative equity research, from first principles to investable portfolios.',
      'home.cta': 'Start here',
      'home.what_title': 'What is BagelQuant?',
      'home.what_body_1': 'BagelQuant is a knowledge base, open-source software ecosystem, and future research platform for quantitative equity portfolio management.',
      'home.what_body_2': 'The goal is practical: understand how investment ideas become signals, how signals become forecasts, and how forecasts become portfolios that can be tested honestly. The site connects financial theory, statistics, machine learning, optimization, and research engineering around that workflow.',
      'home.workflow_title': 'The Quant Equity Workflow',
      'home.workflow_spine': 'Data -> Factor -> Prediction -> Portfolio -> Backtest',
      'home.workflow_body': 'This simple sequence is the spine of BagelQuant. Each step has its own questions: point-in-time data quality, signal design, predictive modeling, portfolio constraints, turnover, transaction costs, and reproducibility.',
      'home.start_title': 'Start Here',
      'home.projects_title': 'Projects and Docs',
      'home.app_title': 'Future App',
      'home.about_title': 'About Me'
    },
    zh: {
      'nav.home': '首页',
      'nav.quick_start': '快速开始',
      'nav.learn': '学习',
      'nav.research': '研究',
      'nav.projects': '项目',
      'nav.docs': '文档',
      'nav.app': '应用',
      'nav.about': '关于我',
      'nav.search_label': '搜索网站',
      'nav.theme_label': '切换深色模式',
      'nav.lang_label': '切换语言',
      'layout.navigation': '导航',
      'layout.home': '首页',
      'toc.title': '本文目录',
      'home.title': 'BagelQuant',
      'home.subtitle': '从基础原理到可投资组合的量化股票研究。',
      'home.cta': '从这里开始',
      'home.what_title': 'BagelQuant 是什么？',
      'home.what_body_1': 'BagelQuant 是一个面向量化股票组合管理的知识库、开源软件生态，以及未来的研究平台。',
      'home.what_body_2': '目标很务实：理解投资想法如何变成信号，信号如何变成预测，预测又如何变成可以被诚实检验的组合。本网站围绕这一流程，把金融理论、统计学、机器学习、优化和研究工程连接起来。',
      'home.workflow_title': '量化股票研究流程',
      'home.workflow_spine': '数据 -> 因子 -> 预测 -> 组合 -> 回测',
      'home.workflow_body': '这条简单的链路是 BagelQuant 的主线。每一步都有自己的关键问题：时点数据质量、信号设计、预测建模、组合约束、换手率、交易成本和可复现性。',
      'home.start_title': '从这里开始',
      'home.projects_title': '项目与文档',
      'home.app_title': '未来应用',
      'home.about_title': '关于我'
    }
  };

  var textMap = {
    'What is BagelQuant?': 'home.what_title',
    'The Quant Equity Workflow': 'home.workflow_title',
    'Data â†’ Factor â†’ Prediction â†’ Portfolio â†’ Backtest': 'home.workflow_spine',
    'Data → Factor → Prediction → Portfolio → Backtest': 'home.workflow_spine',
    'Start Here': 'home.start_title',
    'Projects and Docs': 'home.projects_title',
    'Future App': 'home.app_title',
    'About Me': 'home.about_title',
    'BagelQuant is a knowledge base, open-source software ecosystem, and future research platform for quantitative equity portfolio management.': 'home.what_body_1',
    'The goal is practical: understand how investment ideas become signals, how signals become forecasts, and how forecasts become portfolios that can be tested honestly. The site connects financial theory, statistics, machine learning, optimization, and research engineering around that workflow.': 'home.what_body_2',
    'This simple sequence is the spine of BagelQuant. Each step has its own questions: point-in-time data quality, signal design, predictive modeling, portfolio constraints, turnover, transaction costs, and reproducibility.': 'home.workflow_body'
  };

  function normalizeLang(lang) {
    return lang === 'zh' || /^zh\b/i.test(lang || '') ? 'zh' : 'en';
  }

  function getSavedLanguage() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
  }

  function saveLanguage(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
  }

  function applyLanguage(lang, persist) {
    lang = normalizeLang(lang);
    var labels = dictionary[lang] || dictionary[DEFAULT_LANG];
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.documentElement.dataset.lang = lang;

    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      if (labels[key]) el.textContent = labels[key];
    });

    document.querySelectorAll('[data-i18n-aria-label]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-aria-label');
      if (labels[key]) el.setAttribute('aria-label', labels[key]);
    });

    document.querySelectorAll('[data-i18n-title]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-title');
      if (labels[key]) el.setAttribute('title', labels[key]);
    });

    document.querySelectorAll('.home-content h2, .home-content p, .home-content strong').forEach(function(el) {
      var key = el.getAttribute('data-i18n-detected') || textMap[(el.textContent || '').trim()];
      if (key) el.setAttribute('data-i18n-detected', key);
      if (key && labels[key]) el.textContent = labels[key];
    });

    var toggle = document.getElementById('language-toggle');
    if (toggle) {
      toggle.setAttribute('aria-pressed', lang === 'zh' ? 'true' : 'false');
      toggle.querySelectorAll('[data-lang-option]').forEach(function(option) {
        option.classList.toggle('is-active', option.getAttribute('data-lang-option') === lang);
      });
    }

    window.dispatchEvent(new CustomEvent('bagelquant:languagechange', { detail: { language: lang } }));
    if (persist) saveLanguage(lang);
  }

  function guessLanguageFromBrowser() {
    var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language];
    return langs.some(function(lang) { return /^zh\b/i.test(lang || ''); }) ? 'zh' : DEFAULT_LANG;
  }

  function guessLanguageFromIp() {
    return fetch('https://ipapi.co/json/', { cache: 'no-store' })
      .then(function(response) {
        if (!response.ok) throw new Error('Locale lookup failed');
        return response.json();
      })
      .then(function(data) {
        return CHINESE_COUNTRIES.indexOf((data && data.country_code || '').toUpperCase()) >= 0 ? 'zh' : DEFAULT_LANG;
      });
  }

  document.addEventListener('DOMContentLoaded', function() {
    var saved = getSavedLanguage();
    if (saved) {
      applyLanguage(saved, false);
    } else {
      applyLanguage(guessLanguageFromBrowser(), false);
      guessLanguageFromIp().then(function(lang) {
        if (!getSavedLanguage()) applyLanguage(lang, false);
      }).catch(function() {});
    }

    var toggle = document.getElementById('language-toggle');
    if (toggle) {
      toggle.addEventListener('click', function() {
        var current = document.documentElement.dataset.lang || DEFAULT_LANG;
        applyLanguage(current === 'zh' ? 'en' : 'zh', true);
      });
    }
  });

  window.BagelQuantI18n = {
    applyLanguage: applyLanguage
  };
})();
