---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/
  description: Override HTTP Host headers sent to origin servers.
  full_title: Override HTTP Host headers · Cloudflare Load Balancing docs
  head_html: <title>Override HTTP Host headers · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Override HTTP Host headers sent to origin servers."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/index.md"><meta property="og:title" content="Override HTTP Host headers · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Override HTTP Host headers sent to origin servers."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/#page","headline":"Override HTTP Host headers \u00b7 Cloudflare Load Balancing docs","description":"Override HTTP Host headers sent to origin servers.","url":"https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/override-http-host-headers/
  schema: 1
---
<p>When your application needs specialized routing (<code>CNAME</code> setup or custom hosts like Heroku), you can customize the <code>Host</code> header used in health monitors on a per-endpoint or per-monitor level.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/10428.md")
</aside>
<h2 id="per-endpoint-host-header-override">Per endpoint Host header override</h2>
<p>To balance traffic across multiple hosts, add <code>Host</code> headers to individual endpoints within the same pool.</p>
<p>For example, you might have a pool with endpoints hosted in multiple AppEngine projects or Amazon S3 buckets. You also might want to set up specific failover endpoints within a pool.</p>
<p>Since these examples require specific hostnames per endpoint, your load balancer will not properly route traffic <em>without</em> a <code>Host</code> header override.</p>
<p>If you need an endpoint <code>Host</code> header override, add it when <a href="/load-balancing/pools/create-pool/">creating</a> or editing a pool. For security reasons, this header must meet one of the following criteria:</p>
<ul>
<li>Is a subdomain of a zone associated with this account</li>
<li>Matches the endpoint address</li>
<li>Publicly resolves to the endpoint address</li>
</ul>
<h2 id="host-header-prioritization">Host header prioritization</h2>
<p>If you set a header override on an individual endpoint, it will take precedence over a header override set on a monitor during health monitor requests.</p>
<p>For example, you might have a load balancer for <code>www.example.com</code> with the following setup:</p>
<ul>
<li>
<p>Pools:</p>
<ul>
<li>
<p>Pool 1:</p>
<ul>
<li>Endpoint 1 (<code>Host</code> header set to <code>lb-app-a.example.com</code>)</li>
<li>Endpoint 2</li>
</ul>
</li>
<li>
<p>Pool 2:</p>
<ul>
<li>Endpoint 3</li>
<li>Endpoint 4 (<code>Host</code> header set to <code>lb-app-b.example.com</code>)</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Monitor (<code>Host</code> header set to <code>www.example.com</code>)</p>
</li>
</ul>
<p>In this scenario, health monitor requests for <strong>Endpoint 1</strong> would use <code>lb-app-a.example.com</code>, health monitor requests for <strong>Endpoint 4</strong> would use <code>lb-app-b.example.com</code>, and all other health monitor requests would default to <code>www.example.com</code>. For more information on updating your custom host configuration to be compatible with Cloudflare, see <a href="/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/">Configure Cloudflare and Heroku over HTTPS</a>.</p>
<p>For a list of endpoints that override a monitor's <code>Host</code> header:</p>
<ol>
<li>On a monitor, select <strong>Edit</strong>.</li>
<li>Select <strong>Advanced health monitor settings</strong>.</li>
<li>If you have endpoint overrides, you will see <strong>Endpoint host header overrides</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/load-balancing/origin-host-header-override.png" alt="Example configuration of endpoint host header overrides" /></p>
