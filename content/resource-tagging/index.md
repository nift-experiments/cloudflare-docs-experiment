---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/
  description: Available on all plans
  full_title: Overview · Cloudflare Resource Tagging docs
  head_html: <title>Overview · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Available on all plans"><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/index.md"><meta property="og:title" content="Overview · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available on all plans"><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/resource-tagging/#page","headline":"Overview \u00b7 Cloudflare Resource Tagging docs","description":"Available on all plans","url":"https://developers.cloudflare.com/resource-tagging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/443.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Resource Tagging lets you attach key-value pairs to a wide range of <a href="/resource-tagging/reference/resource-types/">Cloudflare resource types</a> — including zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, and more. Tags are stored separately from the resources themselves, enabling cross-resource queries and policy enforcement without modifying underlying resource configurations.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="public-beta">Public beta</h3>
@markup("md", "content/.markup/bodies/442.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Tags are simple key-value string pairs stored as a JSON object:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;environment&quot;: &quot;production&quot;,&#10;  &quot;team&quot;: &quot;platform&quot;,&#10;  &quot;region&quot;: &quot;us-west-1&quot;&#10;}&#10;</code></pre>
<p>You manage tags through the Tagging API using <code>GET</code>, <code>PUT</code>, and <code>DELETE</code> operations. The API supports <a href="/resource-tagging/how-to/filter-resources/">filtering resources by tags</a> with AND/OR logic, negation, and key-only matching.</p>
<p>Authentication uses <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens (AOTs)</a>, which are account-level tokens independent of individual users.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>The dashboard is in beta. You can view and manage tags in the dashboard under <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong>, but the API remains the recommended interface for automation workflows.</li>
<li><code>PUT</code> replaces all tags. There is no <code>PATCH</code> endpoint. The <code>PUT</code> operation replaces all tags on a resource. Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag"><code>GET</code>, merge, <code>PUT</code> workflow</a> to modify individual tags.</li>
<li><code>DELETE</code> removes all tags. There is no way to delete a single tag. Use <code>PUT</code> with the remaining tags instead.</li>
<li>Querying tags for a resource that has never been tagged returns a <code>500</code> error instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>Follow the <a href="/resource-tagging/get-started/">Get started guide</a> to set up authentication and make your first API calls.</p>
