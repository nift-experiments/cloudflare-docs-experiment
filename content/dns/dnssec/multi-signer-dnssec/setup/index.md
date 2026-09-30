---
cp9:
  canonical: https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/
  description: Configure multi-signer DNSSEC for your zone.
  full_title: Set up multi-signer DNSSEC · Cloudflare DNS docs
  head_html: <title>Set up multi-signer DNSSEC · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure multi-signer DNSSEC for your zone."><link rel="canonical" href="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/index.md"><meta property="og:title" content="Set up multi-signer DNSSEC · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure multi-signer DNSSEC for your zone."><meta property="og:url" content="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/#page","headline":"Set up multi-signer DNSSEC \u00b7 Cloudflare DNS docs","description":"Configure multi-signer DNSSEC for your zone.","url":"https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dnssec/multi-signer-dnssec/setup/
  schema: 1
---
<p>This page explains how you can enable <a href="/dns/dnssec/multi-signer-dnssec/about/">multi-signer DNSSEC</a> with Cloudflare, using the <a href="/dns/dnssec/multi-signer-dnssec/about/#model-2">model 2</a> as described in <a href="https://www.rfc-editor.org/rfc/rfc8901.html">RFC 8901</a>.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Note that:</p>
<ul>
<li>This process requires that your other DNS provider(s) also support multi-signer DNSSEC.</li>
<li>Although you can complete a few steps via the dashboard, currently the whole process can only be completed using the API.</li>
<li>Enabling <strong>DNSSEC</strong> and <strong>Multi-signer DNSSEC</strong> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page only replaces the first step in <a href="#1-set-up-cloudflare-zone">1. Set up Cloudflare zone</a>. You still have to follow the rest of this tutorial to complete the setup.</li>
</ul>
<h2 id="1-set-up-cloudflare-zone"><ol>
<li>Set up Cloudflare zone</li>
</ol></h2>
<h3 id="cloudflare-as-primary-full-setup">Cloudflare as Primary (full setup)</h3>
<p>If you use Cloudflare as a primary DNS provider, meaning that you manage your DNS records in Cloudflare, do the following:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7743.md")
</div></div>
<h3 id="cloudflare-as-secondary">Cloudflare as Secondary</h3>
<p>If you use Cloudflare as a secondary DNS provider, do the following:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7746.md")
</div></div>
<h2 id="2-set-up-external-provider"><ol start="2">
<li>Set up external provider</li>
</ol></h2>
<ol>
<li>Get Cloudflare's ZSK using either the API or a query from one of the assigned Cloudflare nameservers.</li>
</ol>
<p>API example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec/zsk&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>Command line query example:</p>
<pre tabindex="0"><code class="language-sh">$ dig &lt;ZONE_NAME&gt; dnskey @&lt;CLOUDFLARE_NAMESERVER&gt; +noall +answer | grep 256&#10;</code></pre>
<ol start="2">
<li>Add Cloudflare's ZSK that you fetched in the previous step to the DNSKEY record set of your external provider(s).</li>
<li>Add Cloudflare's nameservers to the NS record set at your external provider(s).</li>
</ol>
<h2 id="3-set-up-registrar"><ol start="3">
<li>Set up registrar</li>
</ol></h2>
<ol>
<li>
<p>Add DS records to your registrar, one for each provider. You can see your Cloudflare DS record on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, under <strong>DS Record</strong>.</p>
</li>
<li>
<p>Update the nameserver settings at your registrar to include the nameservers of all providers you will be using for your multi-signer DNSSEC setup.</p>
</li>
</ol>
