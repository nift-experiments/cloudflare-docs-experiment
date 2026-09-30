---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/concepts/namespaces/
  description: Group AI Search instances into namespaces and manage them dynamically from a Workers binding.
  full_title: Namespaces · Cloudflare AI Search docs
  head_html: <title>Namespaces · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Group AI Search instances into namespaces and manage them dynamically from a Workers binding."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/concepts/namespaces/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/concepts/namespaces/index.md"><meta property="og:title" content="Namespaces · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Group AI Search instances into namespaces and manage them dynamically from a Workers binding."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/concepts/namespaces/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/concepts/namespaces/#page","headline":"Namespaces \u00b7 Cloudflare AI Search docs","description":"Group AI Search instances into namespaces and manage them dynamically from a Workers binding.","url":"https://developers.cloudflare.com/ai-search/concepts/namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/concepts/namespaces/
  schema: 1
---
<p>Every AI Search instance belongs to a <strong>namespace</strong>. A namespace is a logical grouping of instances within your account.</p>
<div class="nb-interactive-component" data-cf-component="AiSearchNamespacesDiagram"></div>
<h2 id="why-use-namespaces">Why use namespaces</h2>
<p>Common reasons to use namespaces include:</p>
<ul>
<li><strong>Domain separation</strong>: Separate instances by product area, for example <code>blog</code>, <code>support</code>, and <code>docs</code>.</li>
<li><strong>Tenant isolation</strong>: Assign each tenant their own namespace so that instance names do not collide across tenants.</li>
<li><strong>Agent isolation</strong>: Give each agent its own namespace for independent context management.</li>
</ul>
<p>For a step-by-step guide to isolating search per tenant, see <a href="/ai-search/how-to/per-tenant-search/">Multitenancy</a>.</p>
<h2 id="requirements">Requirements</h2>
<p>The namespace binding requires the following minimum package versions for TypeScript types and local development support.</p>
<table>
<thead>
<tr>
<th>Package</th>
<th>Minimum version</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/workers-types</code></td>
<td><code>4.20260304.0</code></td>
</tr>
<tr>
<td><code>wrangler</code></td>
<td><code>4.68.1</code></td>
</tr>
</tbody>
</table>
<h2 id="how-namespaces-work">How namespaces work</h2>
<p>When you add an <code>ai_search_namespaces</code> binding to your Wrangler configuration, you specify which namespace the binding has access to. The binding grants full access to all instances within that namespace. You can get, list, create, and delete instances at runtime.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3051.md")
</div>
<p>At runtime, <code>env.AI_SEARCH</code> is the namespace handle. Use <code>env.AI_SEARCH.get(&quot;my-instance&quot;)</code> to get a handle to a specific instance:</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;How does caching work?&quot; }],&#10;});&#10;</code></pre>
<p>The <code>get()</code> method is synchronous and does not make a network call. The instance is resolved lazily when you call a method like <code>search()</code> or <code>chatCompletions()</code>.</p>
<h2 id="default-namespace">Default namespace</h2>
<p>A <code>default</code> namespace is automatically created for every account. If you do not need multiple namespaces, use <code>default</code> for all your instances.</p>
<p>You can also bind directly to specific instances in the default namespace using the <code>ai_search</code> binding. This binds each entry to a single pre-existing instance without needing to call <code>get()</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3052.md")
</div>
<p>The <code>ai_search</code> binding provides the same instance methods (<code>search()</code>, <code>chatCompletions()</code>, <code>info()</code>, <code>stats()</code>, <code>items</code>) but does not support namespace-level operations like <code>list()</code>, <code>create()</code>, or <code>delete()</code>.</p>
<h2 id="multiple-namespaces">Multiple namespaces</h2>
<p>You can declare multiple namespace bindings in the same Worker. Each binding maps to a different namespace and provides isolated access to its instances.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3053.md")
</div>
<h2 id="namespace-public-endpoints">Namespace public endpoints</h2>
<p>A namespace can expose its own public <code>/search</code>, <code>/chat/completions</code>, and <code>/mcp</code> endpoints. One URL then searches across the instances you choose in that namespace and merges the results.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">Namespace public endpoints</a>.</p>
<h2 id="namespaces-and-instance-uniqueness">Namespaces and instance uniqueness</h2>
<p>An instance name must be unique within a namespace. This means you can have an instance named <code>docs</code> in both the <code>blog</code> and <code>support</code> namespaces without conflict.</p>
