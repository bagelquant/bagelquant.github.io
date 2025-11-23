// Adds a "Copy" button to code blocks and handles clipboard copying.
(function() {
  function createButton() {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'copy-code-button';
    btn.setAttribute('aria-label', 'Copy code to clipboard');
    btn.textContent = 'Copy';
    return btn;
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }

    return new Promise(function(resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'absolute';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      var sel = document.getSelection();
      var originalRange = null;
      if (sel.rangeCount > 0) originalRange = sel.getRangeAt(0);
      ta.select();
      try {
        var ok = document.execCommand('copy');
        document.body.removeChild(ta);
        if (originalRange) { sel.removeAllRanges(); sel.addRange(originalRange); }
        if (ok) resolve(); else reject(new Error('copy command failed'));
      } catch (err) {
        document.body.removeChild(ta);
        if (originalRange) { sel.removeAllRanges(); sel.addRange(originalRange); }
        reject(err);
      }
    });
  }

  function attachButtons() {
    var selectors = [
      '.post-content pre',
      '.page-content pre',
      'pre.highlight',
      'pre'
    ];

    var pres = document.querySelectorAll(selectors.join(', '));
    if (!pres || !pres.length) return;

    pres.forEach(function(pre) {
      if (pre.dataset.copyButton === 'true') return;

      var computed = window.getComputedStyle(pre);
      if (computed.position === 'static') pre.style.position = 'relative';

      var btn = createButton();
      pre.appendChild(btn);
      pre.dataset.copyButton = 'true';

      btn.addEventListener('click', function() {
        var code = pre.querySelector('code');
        var text = code ? code.innerText : pre.innerText;
        text = text.replace(/^\n+|\n+$/g, '');

        copyText(text).then(function() {
          btn.classList.add('copied');
          var original = btn.textContent;
          btn.textContent = 'Copied!';
          setTimeout(function() {
            btn.classList.remove('copied');
            btn.textContent = original;
          }, 1500);
        }).catch(function() {
          btn.classList.add('copied');
          var original = btn.textContent;
          btn.textContent = 'Copy failed';
          setTimeout(function() {
            btn.classList.remove('copied');
            btn.textContent = original;
          }, 1500);
        });
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    attachButtons();

    if (window.MutationObserver) {
      var obs = new MutationObserver(function(mutations) {
        var shouldAttach = false;
        mutations.forEach(function(m) {
          if (m.addedNodes && m.addedNodes.length) shouldAttach = true;
        });
        if (shouldAttach) attachButtons();
      });
      obs.observe(document.body, { childList: true, subtree: true });
    }
  });
})();
