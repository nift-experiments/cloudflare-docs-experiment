---
cp9:
  canonical: https://developers.cloudflare.com/time-services/roughtime/usage/
  description: Connect to Cloudflare's Roughtime server.
  full_title: Get the Roughtime from Cloudflare · Cloudflare Time Services docs
  head_html: <title>Get the Roughtime from Cloudflare · Cloudflare Time Services docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to Cloudflare&#x27;s Roughtime server."><link rel="canonical" href="https://developers.cloudflare.com/time-services/roughtime/usage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/time-services/roughtime/usage/index.md"><meta property="og:title" content="Get the Roughtime from Cloudflare · Cloudflare Time Services docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to Cloudflare&#x27;s Roughtime server."><meta property="og:url" content="https://developers.cloudflare.com/time-services/roughtime/usage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Time Services"><meta name="algolia_product_filter" content="Time Services"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Time Services"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/time-services/roughtime/usage/#page","headline":"Get the Roughtime from Cloudflare \u00b7 Cloudflare Time Services docs","description":"Connect to Cloudflare's Roughtime server.","url":"https://developers.cloudflare.com/time-services/roughtime/usage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /time-services/roughtime/usage/
  schema: 1
---
<p>The &quot;Hello, world!&quot; of Roughtime is very simple: the client sends a request over UDP to the server and the server responds with a signed timestamp.</p>
<p>You just need the server's address and public key to run the protocol:</p>
<ul>
<li><strong>Server address</strong>: <code>roughtime.cloudflare.com:2003</code> (resolves to an IP address in our <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast IP range</a>). You can use either IPv4 or IPv6.</li>
<li><strong>Public key</strong>: <code>0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=</code></li>
</ul>
<p>To get started, download and run Cloudflare's <a href="https://github.com/cloudflare/roughtime">Go client</a>:</p>
<pre tabindex="0"><code class="language-go">go install github.com/cloudflare/roughtime/cmd/getroughtime@latest&#10;getroughtime -ping roughtime.cloudflare.com:2003 -pubkey 0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=&#10;</code></pre>
<h2 id="beta-notice">Beta notice</h2>
<p>Cloudflare Roughtime is currently in beta. As such, our root public key may
change in the future. We will keep this page up-to-date with the most current public key.</p>
<p>You can also obtain it programmatically using DNS. For example:</p>
<pre tabindex="0"><code class="language-sh">dig TXT roughtime.cloudflare.com | grep -oP &#x27;TXT\s&quot;\K.*?(?=&quot;)&#x27;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Beyond just getting the Roughtime from Cloudflare, you may want to use it to <a href="/time-services/roughtime/recipes/">keep your clock in sync</a>.</p>
