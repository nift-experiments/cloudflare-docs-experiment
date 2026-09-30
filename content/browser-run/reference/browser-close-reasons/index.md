---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/
  description: Identify why a Browser Run session closed and review common close reason codes in the dashboard.
  full_title: Browser close reasons · Cloudflare Browser Run docs
  head_html: <title>Browser close reasons · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Identify why a Browser Run session closed and review common close reason codes in the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/index.md"><meta property="og:title" content="Browser close reasons · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identify why a Browser Run session closed and review common close reason codes in the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/#page","headline":"Browser close reasons \u00b7 Cloudflare Browser Run docs","description":"Identify why a Browser Run session closed and review common close reason codes in the dashboard.","url":"https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/reference/browser-close-reasons/
  schema: 1
---
<p>A browser session may close for a variety of reasons, including normal completion, inactivity, connection errors, or errors in the headless browser instance. As a best practice, wrap <code>puppeteer.connect</code> or <code>puppeteer.launch</code> in a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"><code>try...catch</code></a> statement to handle unexpected closures gracefully.</p>
<p>To find the reason that a browser closed:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Browser Run</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Runs</strong> tab.</li>
</ol>
<p>Browser Run sessions are billed based on <a href="/browser-run/pricing/">usage</a>. We do not charge for sessions that error due to underlying Browser Run infrastructure.</p>
<h2 id="close-reasons">Close reasons</h2>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Normal closure</strong></td>
<td>Your code called <code>browser.close()</code> and the session ended normally. No action needed.</td>
</tr>
<tr>
<td><strong>Browser idle</strong></td>
<td>The session received no commands for the configured inactivity timeout (60 seconds by default, up to 10 minutes with <a href="/browser-run/puppeteer/#keep-alive"><code>keep_alive</code></a>). To prevent idle closures, send commands within the inactivity window or increase the <code>keep_alive</code> value.</td>
</tr>
<tr>
<td><strong>Chromium crashed</strong></td>
<td>The Chromium instance inside the session crashed, often because the page consumed too much memory (large DOMs, heavy JavaScript, or many concurrent pages). Try reducing page complexity, closing unused pages, or breaking work into smaller tasks.</td>
</tr>
<tr>
<td><strong>Connection error</strong></td>
<td>The connection between the client and Browser Run was interrupted. This can be caused by network issues, your Worker reaching its CPU time limit, or a WebSocket disconnection. Retry the operation with a <code>try...catch</code> block.</td>
</tr>
<tr>
<td><strong>Session evicted</strong></td>
<td>Browser Run recycled the session due to infrastructure maintenance or a new release deployment. This is not caused by your code. Retry the operation with a <code>try...catch</code> block and reconnection logic.</td>
</tr>
</tbody>
</table>
<h2 id="handling-unexpected-closures">Handling unexpected closures</h2>
<p>Sessions can close at any time due to infrastructure events, network issues, or browser crashes. Design your code to handle these cases by wrapping browser operations in a <code>try...catch</code> block and reconnecting when needed.</p>
<pre tabindex="0"><code class="language-js">async function runBrowser(env) {&#10;  let browser;&#10;  try {&#10;    browser = await puppeteer.launch(env.MYBROWSER);&#10;    const page = await browser.newPage();&#10;    await page.goto(&quot;https://example.com&quot;);&#10;    // Your browser automation logic&#10;  } catch (error) {&#10;    console.error(&quot;Browser session ended unexpectedly:&quot;, error.message);&#10;    // Retry or return an error response&#10;  } finally {&#10;    await browser?.close();&#10;  }&#10;}&#10;</code></pre>
<p>For long-running or critical workflows, consider adding retry logic:</p>
<pre tabindex="0"><code class="language-js">async function runWithRetry(env, maxRetries = 3) {&#10;  for (let attempt = 1; attempt &lt;= maxRetries; attempt++) {&#10;    try {&#10;      return await runBrowser(env);&#10;    } catch (error) {&#10;      if (attempt === maxRetries) throw error;&#10;      console.log(`Attempt ${attempt} failed, retrying...`);&#10;    }&#10;  }&#10;}&#10;</code></pre>
