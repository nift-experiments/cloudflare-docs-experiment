---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/
  description: How Authenticated Origin Pulls use mTLS to verify Cloudflare connections.
  full_title: How Authenticated Origin Pulls works · Cloudflare SSL/TLS docs
  head_html: <title>How Authenticated Origin Pulls works · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="How Authenticated Origin Pulls use mTLS to verify Cloudflare connections."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/index.md"><meta property="og:title" content="How Authenticated Origin Pulls works · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Authenticated Origin Pulls use mTLS to verify Cloudflare connections."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/#page","headline":"How Authenticated Origin Pulls works \u00b7 Cloudflare SSL/TLS docs","description":"How Authenticated Origin Pulls use mTLS to verify Cloudflare connections.","url":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/authenticated-origin-pull/explanation/
  schema: 1
---
<h2 id="simple-explanation">Simple explanation</h2>
<p>When visitors request content from your domain, Cloudflare first attempts to serve content from the cache. If this attempt fails, Cloudflare sends a request — or an <code>origin pull</code> — back to your origin web server to get the content.</p>
<p>Authenticated Origin Pulls makes sure that all of these <code>origin pulls</code> come from Cloudflare. Put another way, Authenticated Origin Pulls ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.</p>
<p>This block also applies for requests to <a href="/dns/proxy-status/#dns-only-records">unproxied DNS records</a> in Cloudflare.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14284.md")
</aside>
<h2 id="detailed-explanation">Detailed explanation</h2>
<p>Cloudflare enforces authenticated origin pulls by adding an extra layer of TLS client certificate authentication when establishing a connection between Cloudflare and the origin web server.</p>
<p>For more details, refer to the <a href="https://blog.cloudflare.com/protecting-the-origin-with-tls-authenticated-origin-pulls/">introductory blog post</a>.</p>
<hr />
<h3 id="types-of-handshakes">Types of handshakes</h3>
<p>For more details, refer to <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">What is a TLS handshake?</a>.</p>
<p><strong>Standard TLS handshake</strong></p>
<p><img src="/assets/upstream/images/ssl/client-auth-tls-standard.png" alt="Diagram showing the Standard TLS handshake" /></p>
<p><strong>Client authenticated TLS handshake</strong></p>
<p><img src="/assets/upstream/images/ssl/client-auth-tls-handshake.png" alt="Diagram showing the client authenticated TLS handshake" /></p>
<h3 id="comparison-diagrams">Comparison diagrams</h3>
<p>Without Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare and Cloudflare and your origin.
This is true even if you have <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong></a> encryption modes enabled.</p>
<pre tabindex="0"><code class="language-mermaid">    flowchart TD&#10;      accTitle: Connection diagram without Authenticated Origin Pulls&#10;      A[End user query for &lt;code&gt;example.com&lt;/code&gt;] --Standard TLS Handshake--&gt; B[Cloudflare network]&#10;      B --Standard TLS Handshake--&gt; C[Origin server]&#10;      D[External device] --Standard TLS Handshake ----&gt; C&#10;</code></pre>
<br />
<p>This lack of authentication means that - even if your origin is <a href="/fundamentals/concepts/how-cloudflare-works/">protected behind Cloudflare</a> - attackers with your origin's IP address will still receive a response from your origin for HTTPS requests.</p>
<p>With Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare, but a client-authenticated TLS handshake between Cloudflare and your origin.</p>
<pre tabindex="0"><code class="language-mermaid">    flowchart TD&#10;      accTitle: Connection diagram with Authenticated Origin Pulls&#10;      A[End user query for &lt;code&gt;example.com&lt;/code&gt;] --Standard TLS Handshake--&gt; B[Cloudflare network]&#10;      B --Client authenticated TLS Handshake--&gt; C[Origin server]&#10;      D[External device] --Standard TLS Handshake -----x C&#10;</code></pre>
<br />
<p>This additional layer of authentication ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.</p>
