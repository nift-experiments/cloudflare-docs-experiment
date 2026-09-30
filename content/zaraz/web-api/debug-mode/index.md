---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/web-api/debug-mode/
  description: Enable Zaraz debug mode to inspect events in the browser console.
  full_title: Debug mode · Cloudflare Zaraz docs
  head_html: <title>Debug mode · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Zaraz debug mode to inspect events in the browser console."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/web-api/debug-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/web-api/debug-mode/index.md"><meta property="og:title" content="Debug mode · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Zaraz debug mode to inspect events in the browser console."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/web-api/debug-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/web-api/debug-mode/#page","headline":"Debug mode \u00b7 Cloudflare Zaraz docs","description":"Enable Zaraz debug mode to inspect events in the browser console.","url":"https://developers.cloudflare.com/zaraz/web-api/debug-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/web-api/debug-mode/
  schema: 1
---
<p>Zaraz offers a debug mode to troubleshoot the events and triggers systems. To activate debug mode you need to create a special debug cookie (<code>zarazDebug</code>) containing your debug key.
You can set this cookie manually or via the <code>zaraz.debug</code> helper function available in your console.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Copy your **Debug Key**.
3. Open a web browser and access its Developer Tools. For example, to access Developer Tools in Google Chrome, select **View** > **Developer** > **Developer Tools**.
4. Select the **Console** pane and enter the following command to create a debug cookie:
<pre tabindex="0"><code class="language-js">zaraz.debug(&quot;YOUR_DEBUG_KEY&quot;)&#10;</code></pre>
<p>Zaraz’s debug mode is now enabled. A pop-up window will show up with the debugger information. To exit debug mode, remove the cookie by typing <code>zaraz.debug()</code> in the console pane of the browser.</p>
