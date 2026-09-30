---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/
  description: Manage tunnel authentication tokens for remote and local tunnels.
  full_title: Tunnel tokens · Cloudflare Docs
  head_html: <title>Tunnel tokens · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage tunnel authentication tokens for remote and local tunnels."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/index.md"><meta property="og:title" content="Tunnel tokens · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage tunnel authentication tokens for remote and local tunnels."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/#page","headline":"Tunnel tokens \u00b7 Cloudflare Docs","description":"Manage tunnel authentication tokens for remote and local tunnels.","url":"https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/reference/tunnel-tokens/
  schema: 1
---
<p>A <span class="nb-glossary-tooltip" title="remotely-managed tunnel">remotely-managed tunnel</span> only requires a token to run. Anyone with the token can run the tunnel.</p>
<h2 id="get-the-token">Get the token</h2>
<p>To get the token for a remotely-managed tunnel:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14863.md")
</div></div>
<h2 id="rotate-a-token">Rotate a token</h2>
<p>Rotate tokens regularly to reduce the risk of compromise. For tunnels with multiple <a href="/tunnel/configuration/#replicas-and-high-availability">replicas</a>, rotate outside working hours and update replicas in batches.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your tunnel.</li>
<li>Select <strong>Rotate token</strong>.
After rotating the token, <code>cloudflared</code> cannot establish new connections with the old token. Existing connectors remain active until restarted.</li>
<li>Select <strong>Add replica</strong> and copy the new <code>cloudflared</code> installation command.</li>
<li>On each replica, reinstall the <code>cloudflared</code> service using the new token:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<details class="nb-details"><summary>Rotate a compromised token</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14864.md")
</div></details>
