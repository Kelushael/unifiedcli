/**
 * DANAE Chat → Studio Stream
 * 
 * Detects HTML in responses. Manual trigger to open studio.
 * Streams code in real-time as model generates it.
 */

(function() {
  "use strict";

  let studioWindow = null;
  let isStreaming = false;

  /**
   * Open the studio window
   */
  window.openStudio = function() {
    if (!studioWindow || studioWindow.closed) {
      studioWindow = window.open(
        'https://studio.axismundi.fun/studio-danae-bridge.html',
        'danae-studio',
        'width=1400,height=900,resizable=yes,scrollbars=yes'
      );
      return studioWindow;
    }
    studioWindow.focus();
    return studioWindow;
  };

  /**
   * Stream HTML to studio window in real-time
   * Call this as model generates each token/chunk
   * @param {string} htmlChunk - Incremental HTML being generated
   * @param {boolean} isComplete - Whether generation is finished
   */
  window.streamToStudio = function(htmlChunk, isComplete = false) {
    if (!studioWindow || studioWindow.closed) {
      console.warn('Studio window not open. Call openStudio() first.');
      return;
    }

    studioWindow.postMessage(
      {
        type: 'danae:stream',
        chunk: htmlChunk,
        complete: isComplete,
        timestamp: Date.now()
      },
      'https://studio.axismundi.fun'
    );

    isStreaming = !isComplete;
  };

  /**
   * Detect if response contains HTML
   * Returns true if HTML detected, false otherwise
   * @param {string} text - The response text to check
   * @returns {boolean}
   */
  window.detectHTML = function(text) {
    if (!text) return false;
    return /^<|<html|<body|<div|<main|<!DOCTYPE/i.test(text.trim());
  };

  /**
   * Get detection indicator button to add to UI
   * Shows when HTML is detected in current response
   */
  window.createDetectionIndicator = function() {
    const indicator = document.createElement('div');
    indicator.id = 'danae-html-indicator';
    indicator.style.cssText = `
      position: fixed;
      top: 10px;
      right: 10px;
      padding: 8px 12px;
      background: rgba(170, 255, 0, 0.1);
      border: 1px solid #aaff00;
      color: #aaff00;
      font-family: 'Courier New', monospace;
      font-size: 10px;
      border-radius: 2px;
      display: none;
      z-index: 9999;
      cursor: pointer;
      transition: all 0.15s;
    `;

    indicator.textContent = '⬡ HTML DETECTED — Click to preview';

    indicator.onmouseover = () => {
      indicator.style.background = 'rgba(170, 255, 0, 0.2)';
    };

    indicator.onmouseout = () => {
      indicator.style.background = 'rgba(170, 255, 0, 0.1)';
    };

    indicator.onclick = () => {
      window.openStudio();
      indicator.style.display = 'none';
    };

    return indicator;
  };

  /**
   * Hook into chat to detect and mark HTML responses
   * Call this once during chat initialization
   */
  window.setupHTMLDetection = function(messageDisplaySelector) {
    const display = document.querySelector(messageDisplaySelector);
    if (!display) {
      console.warn('Message display selector not found');
      return;
    }

    const indicator = window.createDetectionIndicator();
    document.body.appendChild(indicator);

    // Monitor for new message content
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType !== Node.TEXT_NODE) {
              const text = node.textContent || '';
              if (window.detectHTML(text)) {
                indicator.style.display = 'block';
                console.log('✓ HTML detected in response');
              }
            }
          });
        }
      });
    });

    observer.observe(display, {
      childList: true,
      subtree: true,
      characterData: false
    });

    console.log('✓ HTML detection active');
  };

  /**
   * For streaming responses: call this as each token arrives
   * 
   * Example in your streaming handler:
   *   let fullResponse = '';
   *   for await (let chunk of stream) {
   *     fullResponse += chunk;
   *     if (window.detectHTML(fullResponse)) {
   *       window.streamToStudio(fullResponse, false);
   *     }
   *   }
   *   window.streamToStudio(fullResponse, true); // Mark complete
   */
  window.initStreamHandler = function(onToken) {
    // This wraps your existing streaming handler
    // and injects HTML detection + streaming
    return function(token) {
      onToken(token);

      // Check if we should stream to studio
      // This assumes you're building up a fullResponse variable
      // You'll need to adapt based on your chat implementation
    };
  };

  console.log('✓ DANAE Stream → Studio loaded');
  console.log('Usage:');
  console.log('  1. window.setupHTMLDetection("[selector]") — detect HTML in responses');
  console.log('  2. window.openStudio() — open preview window');
  console.log('  3. window.streamToStudio(html, isComplete) — stream code in real-time');
})();
