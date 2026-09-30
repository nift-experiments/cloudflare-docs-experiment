---
cp9:
  canonical: https://developers.cloudflare.com/key-transparency/api/namespaces/
  description: Create and manage namespaces representing logs monitored by the Cloudflare Auditor.
  full_title: Namespaces · Cloudflare Key Transparency Auditor docs
  head_html: <title>Namespaces · Cloudflare Key Transparency Auditor docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage namespaces representing logs monitored by the Cloudflare Auditor."><link rel="canonical" href="https://developers.cloudflare.com/key-transparency/api/namespaces/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/key-transparency/api/namespaces/index.md"><meta property="og:title" content="Namespaces · Cloudflare Key Transparency Auditor docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage namespaces representing logs monitored by the Cloudflare Auditor."><meta property="og:url" content="https://developers.cloudflare.com/key-transparency/api/namespaces/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Key Transparency Auditor"><meta name="algolia_product_filter" content="Key Transparency Auditor"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Key Transparency Auditor"><meta name="pcx_tags" content="REST API,mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/key-transparency/api/namespaces/#page","headline":"Namespaces \u00b7 Cloudflare Key Transparency Auditor docs","description":"Create and manage namespaces representing logs monitored by the Cloudflare Auditor.","url":"https://developers.cloudflare.com/key-transparency/api/namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API","mTLS"]}</script>
  markdown: true
  noindex: false
  route: /key-transparency/api/namespaces/
  schema: 1
---
<p>The Cloudflare Key Transparency API is organized in namespaces, each one representing a Log monitored by Cloudflare Auditor. If you want to register a namespace, contact us.</p>
<h2 id="create-a-namespace">Create a namespace</h2>
<p>The following fields are required when making a <code>POST</code> request:</p>
<ul>
<li><code>name</code></li>
<li><code>public</code></li>
<li><code>root</code></li>
<li><code>signature_version</code>:
<ul>
<li>0x0001 for <a href="https://github.com/cloudflare/plexi/blob/main/plexi_core/src/proto/specs/types.proto">Protobuf serialisation</a> Ed25519 signature from the Auditor</li>
<li>0x0002 for <a href="https://github.com/bincode-org/bincode/blob/trunk/docs/spec.md">bincode serialisation</a> E25519 serialisation by the Auditor</li>
</ul>
</li>
</ul>
<p>The <code>log_directory</code> field is optional. If set, Cloudflare will use it to fetch audit proofs and validate them.</p>
<p>This API is authenticated via <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">mTLS</a>.</p>
<pre tabindex="0"><code class="language-sh">curl &#x27;https://plexi.key-transparency.cloudflare.com/namespaces&#x27; \&#10;        	&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;        	&#45;-data &#x27;{&#10; 	&quot;name&quot;: &quot;your.new.log.com&quot;,&#10; 	&quot;root&quot;: &quot;1/1111111111111111111111111111111111111111111111111111111111111111&quot;,&#10; 	&quot;log_directory&quot;: &quot;https://your.new.log.com/path/to/proofs&quot;,&#10;	&quot;signature_version&quot;: 1&#10;  }&#x27;&#10;{&#10;  &quot;name&quot;: &quot;your.new.log.com&quot;,&#10;  &quot;log_directory&quot;: &quot;https://your.new.log.com/path/to/proofs&quot;,&#10;  &quot;root&quot;: &quot;1/1111111111111111111111111111111111111111111111111111111111111111&quot;,&#10;  &quot;status&quot;: &quot;Initialization&quot;,&#10;  &quot;reports_uri&quot;: &quot;/namespaces/your.new.log.com/reports&quot;,&#10;  &quot;audits_uri&quot;: &quot;/namespaces/your.new.log.com/audits&quot;,&#10;  &quot;signature_version&quot;: 1&#10;}&#10;</code></pre>
<p>After publishing the first epoch, <code>status</code> will show <code>Online</code>. Possible statuses include:</p>
<ul>
<li><code>Online</code></li>
<li><code>Initialization</code></li>
<li><code>Disabled</code></li>
</ul>
<h2 id="list-all-namespaces">List all namespaces</h2>
<p>Refer to the example below to get information about all public namespaces.</p>
<pre tabindex="0"><code class="language-sh">curl &#x27;https://plexi.key-transparency.cloudflare.com/namespaces&#x27;&#10;{&#10;   &quot;namespaces&quot;: [&#10;       { &quot;name&quot;: &quot;your.new.log.com&quot;, &quot;root&quot;: &quot;1/abc&quot;, &quot;reports_uri&quot;: &quot;/namespaces/your.new.log.com/reports&quot;, &quot;audits_uri&quot;: &quot;/namespaces/your.new.log.com/audits&quot;, &quot;log_directory&quot;: &quot;https://your.new.log.com/path/to/proofs&quot;, &quot;status&quot;: &quot;online&quot; },&#10;       { &quot;name&quot;: &quot;my.new.log.com&quot;, &quot;reports_uri&quot;: &quot;/namespaces/meta-bt-2024/reports&quot;, &quot;audits_uri&quot;: &quot;/namespaces/meta-bt-2024/audits&quot;, &quot;status&quot;: &quot;initialization&quot; }&#10;   ]&#10;}&#10;</code></pre>
<h2 id="disable-a-namespace">Disable a namespace</h2>
<p>If a log state has been corrupted, lost, or needs to be sharded to be maintainable, the Auditor allows the Log operator to mark a namespace as <code>Disabled</code>.</p>
<p>This API is authenticated via <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">mTLS</a>.</p>
<pre tabindex="0"><code class="language-sh">curl -X PATCH &#x27;https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}&#x27; \&#10;        	&#45;H &#x27;Content-Type: application/json&#x27; \&#10;        	&#45;d &#x27;{&#10; 	&quot;status&quot;: &quot;Disabled&quot;&#10;  }&#x27;&#10;{&#10;  &quot;name&quot;: &quot;your.new.log.com&quot;,&#10;  &quot;log_directory&quot;: &quot;https://your.new.log.com/path/to/proofs&quot;,&#10;  &quot;root&quot;: &quot;1/1111111111111111111111111111111111111111111111111111111111111111&quot;,&#10;  &quot;status&quot;: &quot;Disabled&quot;,&#10;  &quot;reports_uri&quot;: &quot;/namespaces/your.new.log.com/reports&quot;,&#10;  &quot;audits_uri&quot;: &quot;/namespaces/your.new.log.com/audits&quot;,&#10;  &quot;signature_version&quot;: 1&#10;}&#10;</code></pre>
