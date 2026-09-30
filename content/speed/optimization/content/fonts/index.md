---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/fonts/
  description: Serve Google Fonts from your domain to improve privacy and performance.
  full_title: Cloudflare Fonts · Cloudflare Speed docs
  head_html: <title>Cloudflare Fonts · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve Google Fonts from your domain to improve privacy and performance."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/fonts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/fonts/index.md"><meta property="og:title" content="Cloudflare Fonts · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve Google Fonts from your domain to improve privacy and performance."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/fonts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Speed"><meta name="pcx_tags" content="Google"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/speed/optimization/content/fonts/#page","headline":"Cloudflare Fonts \u00b7 Cloudflare Speed docs","description":"Serve Google Fonts from your domain to improve privacy and performance.","url":"https://developers.cloudflare.com/speed/optimization/content/fonts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google"]}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/fonts/
  schema: 1
---
<p>Cloudflare Fonts is a feature designed for websites that use <a href="https://fonts.google.com/">Google Fonts</a>. It rewrites Google Fonts to be delivered from a website’s own origin, eliminating the need to rely on third-party font providers. Cloudflare Fonts is tailored to improve website performance and user privacy without the need for any code changes or self-hosting of fonts.</p>
<h2 id="how-cloudflare-fonts-works">How Cloudflare Fonts works</h2>
<p>Cloudflare Fonts works by rewriting your webpage’s HTML. It removes Google Fonts links and replaces them with inline CSS. This CSS includes links to fonts from your own Cloudflare zone rather than from Google servers. This ensures that font files are served from your domain through Cloudflare's infrastructure, optimizing performance and enhancing user privacy.</p>
<h3 id="browser-support">Browser support</h3>
<p>Cloudflare Fonts is compatible with browsers that support Unicode-range subsetting and WOFF or WOFF2 formats, including:</p>
<pre tabindex="0"><code>Chrome 36+&#10;Edge 16+&#10;Safari 10+&#10;Firefox 44+&#10;Opera 22+&#10;IE 9+&#10;Chrome for Android 115+&#10;Safari on iOS 10+&#10;Samsung Internet 5+&#10;</code></pre>
<h2 id="get-started">Get started</h2>
<p>To enable Cloudflare Fonts for your entire domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Speed</strong> &gt; <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Content Optimization</strong>.</li>
<li>For <strong>Cloudflare Fonts</strong>, switch the toggle to <strong>On</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13952.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>While Cloudflare Fonts offers powerful font optimization capabilities, it is important to be aware of its limitations:</p>
<ul>
<li><strong>Font transformation</strong>: Currently, Cloudflare Fonts exclusively supports Google Fonts transformation.</li>
<li><strong>APO compatibility</strong>: Cloudflare Fonts does not operate when <a href="/automatic-platform-optimization/">Automatic Platform Optimization</a> (APO) is enabled. Cloudflare APO automatically optimizes Google Fonts in a similar way.</li>
<li><strong>CSS import</strong>: Cloudflare Fonts is compatible only with the <code>&lt;link&gt;</code> setup for Google Fonts and does not support the CSS <code>@import</code> method.</li>
<li><strong>CSP headers</strong>: Cloudflare Fonts does not modify <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> headers. Certain CSP configurations may make Cloudflare Fonts stop working, such as restrictions on inline styles through <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/style-src"><code>style-src</code></a>, or restriction of fonts originating from the site's own origin via <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/font-src"><code>font-src</code></a>.</li>
<li><strong>Fallback mechanism</strong>: In cases where Cloudflare Fonts does not support a specific page, it will gracefully fallback to using Google Fonts.</li>
</ul>
