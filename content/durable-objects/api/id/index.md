---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/api/id/
  description: API reference for DurableObjectId, the 64-digit hex identifier used to address a Durable Object.
  full_title: Durable Object ID · Cloudflare Durable Objects docs
  head_html: <title>Durable Object ID · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for DurableObjectId, the 64-digit hex identifier used to address a Durable Object."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/api/id/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/api/id/index.md"><meta property="og:title" content="Durable Object ID · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for DurableObjectId, the 64-digit hex identifier used to address a Durable Object."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/api/id/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/api/id/#page","headline":"Durable Object ID \u00b7 Cloudflare Durable Objects docs","description":"API reference for DurableObjectId, the 64-digit hex identifier used to address a Durable Object.","url":"https://developers.cloudflare.com/durable-objects/api/id/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/api/id/
  schema: 1
---
<h2 id="description">Description</h2>
<p>A Durable Object ID is a 64-digit hexadecimal number used to identify a <span class="nb-glossary-tooltip" title="Durable Object">Durable Object</span>. Not all 64-digit hex numbers are valid IDs. Durable Object IDs are constructed indirectly via the <a href="/durable-objects/api/namespace"><code>DurableObjectNamespace</code></a> interface.</p>
<p>The <code>DurableObjectId</code> interface refers to a new or existing Durable Object. This interface is most frequently used by <a href="/durable-objects/api/namespace/#get"><code>DurableObjectNamespace::get</code></a> to obtain a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> for submitting requests to a Durable Object. Note that creating an ID for a Durable Object does not create the Durable Object. The Durable Object is created lazily after creating a stub from a <code>DurableObjectId</code>. This ensures that objects are not constructed until they are actually accessed.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="logging">Logging</h3>
@markup("md", "content/.markup/bodies/8387.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="tostring"><code>toString</code></h3>
<p><code>toString</code> converts a <code>DurableObjectId</code> to a 64 digit hex string. This string is useful for logging purposes or storing the <code>DurableObjectId</code> elsewhere, for example, in a session cookie. This string can be used to reconstruct a <code>DurableObjectId</code> via <code>DurableObjectNamespace::idFromString</code>.</p>
<pre tabindex="0"><code class="language-js">// Create a new unique ID&#10;const id = env.MY_DURABLE_OBJECT.newUniqueId();&#10;// Convert the ID to a string to be saved elsewhere, e.g. a session cookie&#10;const session_id = id.toString();&#10;&#10;...&#10;// Recreate the ID from the string&#10;const id = env.MY_DURABLE_OBJECT.idFromString(session_id);&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>A 64 digit hex string.</li>
</ul>
<h3 id="equals"><code>equals</code></h3>
<p><code>equals</code> is used to compare equality between two instances of <code>DurableObjectId</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8391.md")
</div></div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>A required <code>DurableObjectId</code> to compare against.</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li>A boolean. True if equal and false otherwise.</li>
</ul>
<h2 id="properties">Properties</h2>
<h3 id="name"><code>name</code></h3>
<p><code>name</code> is an optional property of a <code>DurableObjectId</code>, which returns the name that was used to create the <code>DurableObjectId</code> via <a href="/durable-objects/api/namespace/#idfromname"><code>DurableObjectNamespace::idFromName</code></a>. This value is undefined if the <code>DurableObjectId</code> was constructed using <a href="/durable-objects/api/namespace/#newuniqueid"><code>DurableObjectNamespace::newUniqueId</code></a>.</p>
<p>The <code>name</code> property is also available on <code>ctx.id</code> inside the Durable Object when the caller uses <code>idFromName()</code> or <code>getByName()</code>. <code>ctx.id.name</code> will be <code>undefined</code> in the following cases:</p>
<ul>
<li>The caller accesses the Durable Object using <code>idFromString()</code>, even if the ID was originally created with <code>idFromName()</code>.</li>
<li>Names longer than 1,024 bytes are not passed through to <code>ctx.id</code>.</li>
<li>The Durable Object was created with <code>newUniqueId()</code>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="alarms">Alarms</h3>
@markup("md", "content/.markup/bodies/8386.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8395.md")
</div></div>
<p>The same <code>name</code> is available inside the Durable Object via <code>ctx.id.name</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8399.md")
</div></div>
<h3 id="jurisdiction"><code>jurisdiction</code></h3>
<p><code>jurisdiction</code> is an optional property of a <code>DurableObjectId</code>, which returns the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the ID is restricted to, such as <code>&quot;eu&quot;</code> or <code>&quot;fedramp&quot;</code>. The same value is available inside the Durable Object via <code>ctx.id.jurisdiction</code>, including in <a href="/durable-objects/api/alarms/">alarm handlers</a> and objects accessed via <code>idFromString()</code>, so you can make region-aware decisions without passing the jurisdiction as an argument or persisting it in storage.</p>
<p><code>jurisdiction</code> is preserved across every ID-construction path, including:</p>
<ul>
<li>IDs created from a jurisdiction-restricted subnamespace, for example <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).idFromName(&quot;foo&quot;)</code> or <code>.newUniqueId()</code>.</li>
<li>IDs created via <code>env.MY_DURABLE_OBJECT.newUniqueId({ jurisdiction: &quot;eu&quot; })</code>.</li>
<li>IDs restored from a string via <code>idFromString()</code> — the jurisdiction is encoded in the string itself, so it works on any namespace binding.</li>
</ul>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> in two cases:</p>
<ul>
<li>The Durable Object was not created in a jurisdiction-restricted namespace.</li>
<li>The Durable Object's alarm was scheduled before 2026-03-15. To backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8402.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct – Choose Three</a>.</li>
</ul>
