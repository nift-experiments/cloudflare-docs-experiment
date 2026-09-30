---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/
  description: Control which hostnames can serve your Turnstile widget.
  full_title: Hostname management · Cloudflare Turnstile docs
  head_html: <title>Hostname management · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Control which hostnames can serve your Turnstile widget."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/index.md"><meta property="og:title" content="Hostname management · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control which hostnames can serve your Turnstile widget."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Turnstile"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/#page","headline":"Hostname management \u00b7 Cloudflare Turnstile docs","description":"Control which hostnames can serve your Turnstile widget.","url":"https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /turnstile/additional-configuration/hostname-management/
  schema: 1
---
<p>Hostname management controls where your Turnstile widgets can be used by specifying which domains are authorized to load and execute your widgets. This security measure prevents unauthorized use of your widgets on domains that you do not control.</p>
<p>You can associate hostnames with your widget to control where it can be used via Hostname Management. Managing your hostnames ensures that Turnstile works seamlessly with your setup, whether you add standalone hostnames or leverage zones registered to your Cloudflare account.</p>
<hr />
<h2 id="hostname-requirements">Hostname requirements</h2>
<h3 id="standard-configuration">Standard configuration</h3>
<p>By default, every widget requires at least one hostname to be configured. You cannot create a widget without specifying at least one authorized hostname.</p>
<h3 id="hostname-format-requirements">Hostname format requirements</h3>
<p>When adding hostnames, follow these requirements:</p>
<ul>
<li>The hostname must be fully qualified domain names (FQDNs): <code>example.com</code> or <code>subdomain.example.com</code></li>
<li>Wildcard characters (such as <code>*</code>) are not supported in the hostname field. However, adding a hostname automatically authorizes all of its subdomains.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="invalid-formats">Invalid formats</h3>
@markup("md", "content/.markup/bodies/15034.md")
</aside>
<h3 id="subdomain-behavior">Subdomain behavior</h3>
<p>When you add a hostname, the widget will work on that exact hostname and all of its subdomains. This means adding a root domain covers all subdomains beneath it, while adding a specific subdomain restricts the widget to only that subdomain and its children.</p>
<h4 id="example-root-domain">Example: Root domain</h4>
<p>Adding <code>example.com</code> as a hostname will allow the widget to work on:</p>
<ul>
<li><code>example.com</code></li>
<li><code>www.example.com</code></li>
<li><code>shop.example.com</code></li>
<li><code>any.sub.example.com</code></li>
</ul>
<h4 id="example-specific-subdomain">Example: Specific subdomain</h4>
<p>Adding <code>www.example.com</code> as a hostname provides more restrictive control. The widget will work on:</p>
<ul>
<li><code>www.example.com</code></li>
<li><code>abc.www.example.com</code> (subdomains of the specified hostname)</li>
</ul>
<p>However, it will <strong>not</strong> work on:</p>
<ul>
<li><code>example.com</code> (parent domain)</li>
<li><code>dash.example.com</code> (sibling subdomain)</li>
<li><code>cloudflare.com</code> (unrelated domain)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15033.md")
</aside>
<h2 id="add-hostnames">Add hostnames</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15041.md")
</div></div>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Free users are entitled to a maximum of 10 hostnames per widget.</p>
<p>Enterprise customers can have up to 200 hostnames per widget.</p>
