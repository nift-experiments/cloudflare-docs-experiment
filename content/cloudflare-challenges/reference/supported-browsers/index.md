---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/
  description: Browser compatibility for challenge pages, Turnstile, and JavaScript detections.
  full_title: Supported browsers · Cloudflare challenges docs
  head_html: <title>Supported browsers · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Browser compatibility for challenge pages, Turnstile, and JavaScript detections."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/index.md"><meta property="og:title" content="Supported browsers · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browser compatibility for challenge pages, Turnstile, and JavaScript detections."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Challenges"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/#page","headline":"Supported browsers \u00b7 Cloudflare challenges docs","description":"Browser compatibility for challenge pages, Turnstile, and JavaScript detections.","url":"https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/reference/supported-browsers/
  schema: 1
---
<p>Cloudflare uses browser-based challenges across <a href="/cloudflare-challenges/challenge-types/challenge-pages/">Challenge Pages</a>, <a href="/turnstile/">Turnstile</a>, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections (JSD) in Bot Management</a>, and <a href="/cloudflare-challenges/precursor/">Precursor</a>. This page describes the browser environments that support these checks.</p>
<h2 id="browser-support">Browser support</h2>
<p>Cloudflare challenges support major desktop and mobile browsers.</p>
<h3 id="limited-browser-support">Limited browser support</h3>
<p>The following browsers and environments have limited support and may experience issues.</p>
<ul>
<li>Browsers or operating systems that are more than five years old or have not received security updates in over two years.</li>
<li>Custom or heavily modified browser engines and embedded browsers.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4028.md")
</aside>
<h3 id="unsupported-environments">Unsupported environments</h3>
<p>The following environments are not supported.</p>
<ul>
<li>Internet Explorer browser.</li>
<li>Command-line tools such as <code>wget</code>, <code>curl</code>, or others that lack JavaScript execution capabilities required for Cloudflare Challenges.</li>
<li>Automated browsers are not supported for solving production challenges.</li>
<li>Browser automation frameworks, such as Selenium, Puppeteer, Playwright, and Cypress, are not supported for solving production challenges. For automated Turnstile testing, use <a href="/turnstile/troubleshooting/testing/">Turnstile test keys</a>.</li>
</ul>
<h2 id="common-issues">Common issues</h2>
<h3 id="browser-extensions">Browser extensions</h3>
<p>Browser extensions can interfere with challenges in several ways.</p>
<ul>
<li>Ad blockers and content blockers may prevent challenge scripts from loading properly or block communication with Cloudflare's validation servers.</li>
<li>Privacy-focused extensions like script blockers, fingerprinting protection, or canvas blockers can interfere with the challenge verification process.</li>
<li>Virtual private network (VPN) or proxy extensions might trigger additional security checks or cause IP address inconsistencies.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4027.md")
</aside>
<h3 id="device-emulation-and-developer-tools">Device emulation and developer tools</h3>
<p>Device emulation settings can alter browser signals used by challenges. Results from emulated devices may differ from results on physical devices.</p>
<ul>
<li>Mobile emulation in desktop browsers does not reproduce every characteristic of a physical mobile device.</li>
<li>Browser developer tools can apply network, user-agent, viewport, or JavaScript overrides. Disable these overrides when troubleshooting challenge behavior.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4026.md")
</aside>
<h3 id="webviews-and-in-app-browsers">WebViews and in-app browsers</h3>
<p>Challenges may behave differently depending on embedded browser contexts.</p>
<ul>
<li>WebViews in mobile applications may have limited functionality compared to full browsers</li>
<li>In-app browsers often have restricted JavaScript capabilities</li>
<li>Email client preview windows typically cannot complete Interactive Challenges</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If your visitors consistently experience challenge issues, refer to <a href="/cloudflare-challenges/troubleshooting/challenge-solve-issues/">Challenge solve issues</a> for additional troubleshooting information.</p>
