/**
 * DANAE Chat → Instant Studio Display
 * 
 * When HTML artifact is DONE generating, instantly open studio and display it.
 * User says "make me X" → model finishes → artifact appears.
 */

(function() {
  "use strict";

  let studioWindow = null;

  /**
   * Open and display artifact in studio window
   * Call this when response generation is COMPLETE
   */
  window.displayArtifact = function(htmlCode) {
    // Open window
    if (!studioWindow || studioWindow.closed) {
      studioWindow = window.open(
        'https://studio.axismundi.fun/studio-stream-receiver.html',
        'danae-studio',
        'width=1400,height=900,resizable=yes,scrollbars=yes'
      );
      
      // Wait for window to be ready, then send
      setTimeout(() => {
        if (studioWindow && !studioWindow.closed) {
          studioWindow.postMessage(
            {
              type: 'danae:artifact',
              html: htmlCode,
              complete: true,
              timestamp: Date.now()
            },
            'https://studio.axismundi.fun'
          );
        }
      }, 200);
    } else {
      // Window already open, just send artifact
      studioWindow.postMessage(
        {
          type: 'danae:artifact',
          html: htmlCode,
          complete: true,
          timestamp: Date.now()
        },
        'https://studio.axismundi.fun'
      );
      studioWindow.focus();
    }

    console.log('✓ Artifact displayed:', htmlCode.length, 'chars');
  };

  /**
   * Detect if text is HTML
   */
  window.isHTML = function(text) {
    if (!text) return false;
    return /^<|<html|<body|<div|<main|<!DOCTYPE/i.test(text.trim());
  };

  /**
   * Hook into your chat completion handler
   * Call with the final response when generation is done
   * 
   * Example:
   *   async function onChatComplete(response) {
   *     // Model finished generating
   *     if (window.isHTML(response)) {
   *       window.displayArtifact(response);
   *     }
   *   }
   */

  console.log('✓ Instant Studio loaded');
  console.log('Usage:');
  console.log('  if (window.isHTML(response)) {');
  console.log('    window.displayArtifact(response);');
  console.log('  }');
})();
