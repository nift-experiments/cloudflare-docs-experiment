---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/speed/
  description: '2026-06-23'
  full_title: speed changelog | Cloudflare Docs
  head_html: <title>speed changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/speed/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="speed changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/speed/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/speed/#page","headline":"speed changelog | Cloudflare Docs","description":"2026-06-23","url":"https://developers.cloudflare.com/changelog/product/speed/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/speed/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-amp-sxg-is-now-end-of-life"><a href="/changelog/post/2026-06-23-amp-sxg-end-of-life/">Cloudflare AMP/SXG is now end of life.</a></h2>
<p><em>2026-06-23</em></p>
<p>Cloudflare Accelerated Mobile Pages (AMP) and Signed Exchanges (SXG) support has reached end of life. The features have been disabled since October 2025, so customers who had them configured should see no change to their traffic.</p>
<p>Customers will no longer be able to configure AMP/SXG through API or rulesets. The Zone API will start throwing errors. Rulesets with the SXG configuration will fail to save until SXG has been removed.</p>


<h2 id="cloudflare-fonts-error-handling-and-security-improvements"><a href="/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/">Cloudflare Fonts error handling and security improvements</a></h2>
<p><em>2026-06-18</em></p>
<p>Cloudflare Fonts now forwards <code>/cf-fonts</code> requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.</p>


<h2 id="shared-dictionaries-passthrough-now-in-open-beta"><a href="/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/">Shared dictionaries passthrough now in open beta</a></h2>
<p><em>2026-04-30</em></p>
<p><a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a> (<a href="https://www.rfc-editor.org/rfc/rfc9842.html">RFC 9842</a>) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.</p>
<h4 id="2026-04-30-shared-dictionaries-passthrough-beta-what-changed">What changed</h4>
<p>In passthrough mode, Cloudflare:</p>
<ul>
<li>Forwards the <code>Use-As-Dictionary</code> and <code>Available-Dictionary</code> headers between client and origin without modification.</li>
<li>Treats <code>dcb</code> (Dictionary-Compressed Brotli) and <code>dcz</code> (Dictionary-Compressed Zstandard) as valid <code>Content-Encoding</code> values end to end, without recompressing them.</li>
<li>Extends the cache key to vary on <code>Available-Dictionary</code> and <code>Accept-Encoding</code> so each delta-compressed variant is cached correctly.</li>
</ul>
<p>Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching <code>Use-As-Dictionary</code> headers, and producing deltas in response to <code>Available-Dictionary</code> requests. Cloudflare handles the transport and the cache.</p>
<p>In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.</p>
<p>Shared dictionaries work with browsers that advertise <code>dcb</code> or <code>dcz</code> in <code>Accept-Encoding</code>. Today, this includes Chrome 130 or later and Edge 130 or later.</p>
<h4 id="2026-04-30-shared-dictionaries-passthrough-beta-get-started">Get started</h4>
<p>Turn on passthrough for your zone with a single API call:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH --url https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode</code></pre>
<p>You can also turn it on under <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Content Optimization</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization">Cloudflare dashboard</a>. For full origin setup instructions and a working test recipe, refer to <a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a>, or try the live demo at <a href="https://canicompress.com/">canicompress.com</a>.</p>



