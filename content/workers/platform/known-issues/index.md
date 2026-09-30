---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/known-issues/
  description: Known issues and bugs to be aware of when using Workers.
  full_title: Known issues · Cloudflare Workers docs
  head_html: <title>Known issues · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Known issues and bugs to be aware of when using Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/known-issues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/known-issues/index.md"><meta property="og:title" content="Known issues · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Known issues and bugs to be aware of when using Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/known-issues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/known-issues/#page","headline":"Known issues \u00b7 Cloudflare Workers docs","description":"Known issues and bugs to be aware of when using Workers.","url":"https://developers.cloudflare.com/workers/platform/known-issues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/known-issues/
  schema: 1
---
<p>Below are some known bugs and issues to be aware of when using Cloudflare Workers.</p>
<h2 id="route-specificity">Route specificity</h2>
<ul>
<li>When defining route specificity, a trailing <code>/*</code> in your pattern may not act as expected.</li>
</ul>
<p>Consider two different Workers, each deployed to the same zone. Worker A is assigned the <code>example.com/images/*</code> route and Worker B is given the <code>example.com/images*</code> route pattern. With these in place, here are how the following URLs will be resolved:</p>
<pre tabindex="0"><code>// (A) example.com/images/*&#10;// (B) example.com/images*&#10;&#10;&quot;example.com/images&quot;&#10;// -&gt; B&#10;&quot;example.com/images123&quot;&#10;// -&gt; B&#10;&quot;example.com/images/hello&quot;&#10;// -&gt; B&#10;</code></pre>
<p>You will notice that all examples trigger Worker B. This includes the final example, which exemplifies the unexpected behavior.</p>
<p>When adding a wildcard on a subdomain, here are how the following URLs will be resolved:</p>
<pre tabindex="0"><code>// (A) *.example.com/a&#10;// (B) a.example.com/*&#10;&#10;&quot;a.example.com/a&quot;&#10;// -&gt; B&#10;</code></pre>
<h2 id="wrangler-dev">wrangler dev</h2>
<ul>
<li>When running <code>wrangler dev --remote</code>, all outgoing requests are given the <code>cf-workers-preview-token</code> header, which Cloudflare recognizes as a preview request. This applies to the entire Cloudflare network, so making HTTP requests to other Cloudflare zones is currently discarded for security reasons. To enable a workaround, insert the following code into your Worker script:</li>
</ul>
<pre tabindex="0"><code class="language-js">const request = new Request(url, incomingRequest);&#10;request.headers.delete(&#x27;cf-workers-preview-token&#x27;);&#10;return await fetch(request);&#10;</code></pre>
<h2 id="fetch-api-in-cname-setup">Fetch API in CNAME setup</h2>
<p>When you make a subrequest using <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> from a Worker, the Cloudflare DNS resolver is used. When a zone has a <a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup</a>, all hostnames that the Worker needs to be able to resolve require a dedicated DNS entry in Cloudflare's DNS setup. Otherwise the Fetch API call will fail with status code <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/">530 (1016)</a>.</p>
<p>Setup with missing DNS records in Cloudflare DNS</p>
<pre tabindex="0"><code>// Zone in partial setup: example.com&#10;// DNS records at Authoritative DNS: sub1.example.com, sub2.example.com, ...&#10;// DNS records at Cloudflare DNS: sub1.example.com&#10;&#10;&quot;sub1.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;&quot;sub2.example.com/&quot;&#10;// -&gt; Cannot be resolved by Fetch API, will lead to 530 status code&#10;</code></pre>
<p>After adding <code>sub2.example.com</code> to Cloudflare DNS</p>
<pre tabindex="0"><code>// Zone in partial setup: example.com&#10;// DNS records at Authoritative DNS: sub1.example.com, sub2.example.com, ...&#10;// DNS records at Cloudflare DNS: sub1.example.com, sub2.example.com&#10;&#10;&quot;sub1.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;&quot;sub2.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;</code></pre>
<h2 id="fetch-to-ip-addresses">Fetch to IP addresses</h2>
<p>For Workers subrequests, requests can only be made to URLs, not to IP addresses directly. To overcome this limitation <a href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/">add a A or AAAA name record to your zone</a> and then fetch that resource.</p>
<p>For example, in the zone <code>example.com</code> create a record of type <code>A</code> with the name <code>server</code> and value <code>192.0.2.1</code>, and then use:</p>
<pre tabindex="0"><code class="language-js">await fetch(&#x27;http://server.example.com&#x27;)&#10;</code></pre>
<p>Do not use:</p>
<pre tabindex="0"><code class="language-js">await fetch(&#x27;http://192.0.2.1&#x27;)&#10;</code></pre>
