/**
 * DANAE Chat → Studio Bridge
 *
 * Use this in your chat system to send generated HTML to the studio window.
 *
 * Example in your chat model handler:
 *   if (response.includes('<html') || response.includes('<div')) {
 *     window.sendToStudio(response);
 *   }
 */

(function() {
  "use strict";

  let studioWindow = null;

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
    } else {
      studioWindow.focus();
    }
    return studioWindow;
  };

  /**
   * Send HTML code to the studio window
   * @param {string} html - The HTML code to display
   */
  window.sendToStudio = function(html) {
    // Open window if not already open
    if (!studioWindow || studioWindow.closed) {
      studioWindow = window.openStudio();
    }

    // Give the window a moment to load before sending
    setTimeout(() => {
      if (studioWindow && !studioWindow.closed) {
        studioWindow.postMessage(
          {
            type: 'danae:html',
            html: html,
            timestamp: Date.now(),
            source: 'danae-chat'
          },
          'https://studio.axismundi.fun'
        );
        console.log('✓ Sent to studio:', html.length, 'chars');
      }
    }, 100);
  };

  /**
   * Helper: Extract HTML from model response
   * @param {string} response - The raw model response
   * @returns {string|null} - Extracted HTML or null
   */
  window.extractHTMLFromResponse = function(response) {
    // If response starts with HTML, use it directly
    if (response.trim().startsWith('<')) {
      return response.trim();
    }

    // Look for HTML code blocks
    const htmlMatch = response.match(/```html\n([\s\S]*?)\n```/);
    if (htmlMatch) return htmlMatch[1].trim();

    // Look for any HTML tags
    const tagMatch = response.match(/<(?:html|body|div|main)[\s\S]*<\/(?:html|body|div|main)>/i);
    if (tagMatch) return tagMatch[0].trim();

    return null;
  };

  /**
   * Intercept chat form submissions to detect HTML responses
   */
  window.setupChatInterception = function(chatFormSelector, messageDisplaySelector) {
    const form = document.querySelector(chatFormSelector);
    const messageDisplay = document.querySelector(messageDisplaySelector);

    if (!form || !messageDisplay) {
      console.warn('Chat selectors not found');
      return;
    }

    // Monitor for new messages
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType === Node.TEXT_NODE) return;

            const text = node.textContent || '';

            // Check if message contains HTML
            if (text.includes('<html') || text.includes('<body') || text.includes('<div')) {
              const html = window.extractHTMLFromResponse(text);
              if (html) {
                // Auto-open studio and send HTML
                window.openStudio();
                window.sendToStudio(html);

                // Add visual indicator
                const indicator = document.createElement('span');
                indicator.style.cssText = 'color: #aaff00; font-weight: bold; margin-left: 8px;';
                indicator.textContent = '[HTML → Studio]';
                node.parentNode.appendChild(indicator);
              }
            }
          });
        }
      });
    });

    observer.observe(messageDisplay, {
      childList: true,
      subtree: true,
      characterData: false
    });

    console.log('✓ Chat interception active');
  };

  /**
   * Manual trigger button to add to chat UI
   */
  window.createStudioButton = function() {
    const btn = document.createElement('button');
    btn.id = 'danae-studio-trigger';
    btn.textContent = '⬡ STUDIO';
    btn.style.cssText = `
      background: transparent;
      border: 1px solid #aaff00;
      color: #aaff00;
      padding: 6px 12px;
      font-family: 'Courier New', monospace;
      font-size: 10px;
      letter-spacing: 2px;
      cursor: pointer;
      border-radius: 2px;
      transition: all 0.15s;
    `;

    btn.onmouseover = () => {
      btn.style.background = '#aaff00';
      btn.style.color = '#080808';
    };

    btn.onmouseout = () => {
      btn.style.background = 'transparent';
      btn.style.color = '#aaff00';
    };

    btn.onclick = window.openStudio;

    return btn;
  };

  console.log('✓ DANAE Chat → Studio bridge loaded');
  console.log('Available functions:');
  console.log('  - window.openStudio()');
  console.log('  - window.sendToStudio(html)');
  console.log('  - window.extractHTMLFromResponse(response)');
  console.log('  - window.setupChatInterception(formSelector, displaySelector)');
  console.log('  - window.createStudioButton()');
})();
