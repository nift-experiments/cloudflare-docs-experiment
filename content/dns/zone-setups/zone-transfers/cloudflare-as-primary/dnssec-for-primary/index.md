---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/
  description: With outgoing zone transfers, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.
  full_title: Set up multi-signer DNSSEC with outgoing zone transfers · Cloudflare DNS docs
  head_html: <title>Set up multi-signer DNSSEC with outgoing zone transfers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="With outgoing zone transfers, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/index.md"><meta property="og:title" content="Set up multi-signer DNSSEC with outgoing zone transfers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With outgoing zone transfers, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/#page","headline":"Set up multi-signer DNSSEC with outgoing zone transfers \u00b7 Cloudflare DNS docs","description":"With outgoing zone transfers, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.","url":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/
  schema: 1
---
<p>With <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">outgoing zone transfers</a>, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.</p>
<p>If you want to use DNSSEC with outgoing zone transfers, you should configure <a href="/dns/dnssec/multi-signer-dnssec/">multi-signer DNSSEC</a>. After setting up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/">Cloudflare as primary</a>, follow the steps below to enable DNSSEC.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Note that:</p>
<ul>
<li>This process requires that your other DNS provider(s) also support multi-signer DNSSEC.</li>
<li>Although you can complete a few steps via the dashboard, currently the whole process can only be completed using the API.</li>
<li>Enabling <strong>DNSSEC</strong> and <strong>Multi-signer DNSSEC</strong> in <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> only replaces the first step below. You still have to follow the rest of this tutorial to complete the setup.</li>
</ul>
<h2 id="steps">Steps</h2>
<ol>
<li>Use the <a href="/api/resources/dns/subresources/dnssec/methods/edit/">Edit DNSSEC Status endpoint</a> to enable DNSSEC and activate multi-signer DNSSEC for your zone. This is done by setting <code>status</code> to <code>active</code> and <code>dnssec_multi_signer</code> to <code>true</code>, as in the following example.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;status&quot;: &quot;active&quot;,&#10;  &quot;dnssec_multi_signer&quot;: true&#10;}&#x27;</code></pre>
<ol start="2">
<li>Add the ZSK(s) of your external provider(s) to Cloudflare by creating a DNSKEY record on your zone.</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records&#x27; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;type&quot;: &quot;DNSKEY&quot;,&#10;  &quot;name&quot;: &quot;&lt;ZONE_NAME&gt;&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;flags&quot;: 256,&#10;    &quot;protocol&quot;: 3,&#10;    &quot;algorithm&quot;: 13,&#10;    &quot;public_key&quot;: &quot;&lt;PUBLIC_KEY&gt;&quot;&#10;  },&#10;  &quot;ttl&quot;: 3600&#10;}&#x27;&#10;</code></pre>
<ol start="3">
<li>
<p>Once the DNSKEY record is transferred out from Cloudflare to your secondary provider, get Cloudflare's ZSK and manually add it to the DNSKEY record.</p>
<p>Currently, the ZSK is not automatically transferred out. You can use either the API or a query from one of the assigned Cloudflare nameservers to obtain it.</p>
</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8079.md")
</div>
<ol start="4">
<li>Add DS records to your registrar, one for each provider. You can see your Cloudflare DS record on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, under <strong>DS Record</strong>.</li>
</ol>
<p>The nameserver settings at your registrar should include the nameservers of all providers you will be using for your multi-signer DNSSEC setup.</p>
