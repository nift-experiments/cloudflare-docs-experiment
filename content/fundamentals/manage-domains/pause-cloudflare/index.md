---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/
  description: Temporarily pause Cloudflare on your domain to send traffic directly to your origin server for troubleshooting.
  full_title: Pause Cloudflare · Cloudflare Fundamentals docs
  head_html: <title>Pause Cloudflare · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Temporarily pause Cloudflare on your domain to send traffic directly to your origin server for troubleshooting."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/index.md"><meta property="og:title" content="Pause Cloudflare · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Temporarily pause Cloudflare on your domain to send traffic directly to your origin server for troubleshooting."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/#page","headline":"Pause Cloudflare \u00b7 Cloudflare Fundamentals docs","description":"Temporarily pause Cloudflare on your domain to send traffic directly to your origin server for troubleshooting.","url":"https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-domains/pause-cloudflare/
  schema: 1
---
<p>To troubleshoot your site, you can pause Cloudflare globally. This will send traffic directly to your origin web server instead of Cloudflare's reverse proxy. Paused domains also cannot use Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>. Consider turning on <a href="/fundamentals/manage-domains/pause-cloudflare/#enable-development-mode">Development Mode</a> to bypass caching while preserving protection.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and domain.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Within <strong>Overview</strong>, choose <strong>Advanced Actions</strong> &gt; <strong>Pause Cloudflare on Site</strong>.</li>
</ol>
<p>The process of pausing Cloudflare takes five minutes or less. This approach is preferable to <a href="/dns/zone-setups/full-setup/setup/">changing nameservers</a>, which can cause propagation delays of several hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8902.md")
</aside>
<hr />
<h2 id="alternatives-to-global-pause">Alternatives to global pause</h2>
<h3 id="disable-proxy-on-dns-records">Disable proxy on DNS records</h3>
<p>Instead of pausing Cloudflare globally, you can disable the proxy on individual records:</p>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</p>
</li>
<li>
<p>Go to <strong>DNS</strong> &gt; <strong>Records</strong>. Choose the record and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Toggle <strong>Proxy Status</strong> to <strong>Off</strong>.</p>
</li>
</ol>
<p>Adjusting the proxy status will prevent that record from using Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>.</p>
<h3 id="enable-development-mode">Enable Development Mode</h3>
<p>To troubleshoot caching issues, you could <a href="/cache/reference/development-mode/">enable Development Mode</a>. This will bypass Cloudflare's cache while still preserving Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>.</p>
