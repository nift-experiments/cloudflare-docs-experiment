---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/
  description: Configure DNS over HTTPS in your browser.
  full_title: Configure DoH on your browser · Cloudflare 1.1.1.1 docs
  head_html: <title>Configure DoH on your browser · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure DNS over HTTPS in your browser."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/index.md"><meta property="og:title" content="Configure DoH on your browser · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure DNS over HTTPS in your browser."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/#page","headline":"Configure DoH on your browser \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure DNS over HTTPS in your browser.","url":"https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/
  schema: 1
---
<p>Several browsers support DNS over HTTPS (DoH), which encrypts your DNS queries to protect them from monitoring and tampering.</p>
<p>Some browsers might already have this setting enabled.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1821.md")
</aside>
<h2 id="mozilla-firefox">Mozilla Firefox</h2>
<ol>
<li>Select the menu button &gt; <strong>Settings</strong>.</li>
<li>In the <strong>Privacy &amp; Security</strong> menu, scroll down to the <strong>Enable secure DNS using:</strong> section.</li>
<li>Select <strong>Increased Protection</strong> or <strong>Max Protection</strong>. By default, it will use the <strong>Cloudflare</strong> provider.</li>
<li>If this is not the case, select <strong>Cloudflare</strong> in the <strong>Choose Provider</strong> dropdown.</li>
</ol>
<h2 id="google-chrome">Google Chrome</h2>
<ol>
<li>Select the three-dot menu in your browser &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Privacy and security</strong> &gt; <strong>Security</strong>.</li>
<li>Scroll down and enable <strong>Use secure DNS</strong>.</li>
<li>Select the <strong>With</strong> option, and from the drop-down menu choose <em>Cloudflare (1.1.1.1)</em>.</li>
</ol>
<h2 id="microsoft-edge">Microsoft Edge</h2>
<ol>
<li>Select the three-dot menu in your browser &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Privacy, Search, and Services</strong>, and scroll down to <strong>Security</strong>.</li>
<li>Enable <strong>Use secure DNS</strong>.</li>
<li>Select <strong>Choose a service provider</strong>.</li>
<li>Select the <strong>Enter custom provider</strong> drop-down menu and choose <em>Cloudflare (1.1.1.1)</em>.</li>
</ol>
<h2 id="brave">Brave</h2>
<ol>
<li>Select the menu button in your browser &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Privacy and security</strong> &gt; <strong>Security</strong>.</li>
<li>Under <strong>Advanced</strong>, enable <strong>Use secure DNS</strong>.</li>
<li>From the <strong>Select DNS provider</strong> drop-down menu, choose <em>Cloudflare (1.1.1.1)</em>.</li>
</ol>
<h2 id="check-if-the-browser-is-configured-correctly">Check if the browser is configured correctly</h2>
<p>Visit <a href="https://one.one.one.one/help">1.1.1.1 help page</a> and check if <code>Using DNS over HTTPS (DoH)</code> shows <code>Yes</code>.</p>
