---
cp9:
  canonical: https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/
  description: Consider an example use case and the main steps involved in CNAME flattening.
  full_title: CNAME flattening diagram · Cloudflare DNS docs
  head_html: <title>CNAME flattening diagram · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Consider an example use case and the main steps involved in CNAME flattening."><link rel="canonical" href="https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/index.md"><meta property="og:title" content="CNAME flattening diagram · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Consider an example use case and the main steps involved in CNAME flattening."><meta property="og:url" content="https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/#page","headline":"CNAME flattening diagram \u00b7 Cloudflare DNS docs","description":"Consider an example use case and the main steps involved in CNAME flattening.","url":"https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/cname-flattening/cname-flattening-diagram/
  schema: 1
---
<p>With CNAME flattening, Cloudflare returns an IP address instead of the target hostname that a CNAME record points to.
This process supports a few features and delivers better performance and flexibility, as mentioned in the <a href="/dns/cname-flattening/">CNAME flattening concept page</a>.</p>
<p>Consider the diagram below to have an overview of the steps that may be involved in CNAME flattening.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7720.md")
</aside>
<h2 id="example-use-case">Example use case</h2>
<ul>
<li><code>domain.test</code> is a zone on Cloudflare and has the following CNAME record:</li>
</ul>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7721.md")
</div>
<ul>
<li><code>external-origin.test</code> is a zone on a different DNS provider and has the following A record:</li>
</ul>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/7722.md")
</div>
<p>In this case, the process to respond to queries for <code>domain.test</code> directly with the IP address can be represented by the following diagram:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart BT&#10;accTitle: CNAME flattening diagram&#10;accDescr: Diagram of CNAME flattening process when there is a request for a domain in Cloudflare and the zone has a CNAME record at apex that points to an external A record.&#10;  A((User)) &lt;--query for &lt;code&gt;domain.test&lt;/code&gt;--&gt; B[Resolver] --&gt; C&#10;  C[&quot;Question:&#10;  &lt;code&gt;domain.test IN A&lt;/code&gt;&quot;]&#10; subgraph Y[Cloudflare DNS]&#10; direction RL&#10;  D{{Look up record}} --&gt; G[&quot;Answer:&#10;  &lt;code&gt;domain.test 3600 CNAME external-origin.test&lt;/code&gt;&#10;&#10;  This means that &lt;code&gt;domain.test&lt;/code&gt; is a &lt;code&gt;CNAME&lt;/code&gt; at the zone apex.&#10;  Forced &lt;code&gt;CNAME&lt;/code&gt; flattening is enabled.&quot;] --- H{{Resolve &lt;code&gt;external-origin.test&lt;/code&gt;}}&#10;  K{{Append answer with overwritten query name}} --&gt; L[&quot;Answer:&#10;  &lt;code&gt;domain.test 7200 IN A 192.0.2.1&lt;/code&gt;&quot;] --- M{Proxy status}&#10;  M --Proxied--&gt; O[&quot;Answer:&#10;  &lt;code&gt;domain.test 300 IN A {$Cloudflare IP 1}&lt;/code&gt;&#10;  &lt;code&gt;domain.test 300 IN A {$Cloudflare IP 2}&lt;/code&gt;&quot;]&#10;  M --DNS only--&gt; N[&quot;Answer:&#10;  &lt;code&gt;domain.test 3600 IN A 192.0.2.1&lt;/code&gt;&quot;]&#10; end&#10;&#10; subgraph Z [External DNS provider]&#10;  J[&quot;Answer:&#10;  &lt;code&gt;external-origin.test 7200 IN A 192.0.2.1&lt;/code&gt;&quot;]&#10; end&#10;&#10; C --&gt; D&#10; H --- J --- K&#10; O --&gt; B&#10; N --&gt; B&#10;</code></pre>
<h2 id="aspects-to-consider">Aspects to consider</h2>
<ul>
<li>If the CNAME record is proxied in Cloudflare, the answer is made up of multiple <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a> and its Time to Live (TTL) is set to <code>300</code>.</li>
<li>If the CNAME record in Cloudflare is not proxied, the flattened answer consists of the IP address from the external DNS provider and its TTL corresponds to the lower value between the external record and the Cloudflare CNAME record.</li>
</ul>
