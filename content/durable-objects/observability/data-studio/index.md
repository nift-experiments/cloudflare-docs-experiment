---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/observability/data-studio/
  description: View and edit SQLite-backed Durable Object storage data through the Cloudflare dashboard UI.
  full_title: Data Studio · Cloudflare Durable Objects docs
  head_html: <title>Data Studio · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="View and edit SQLite-backed Durable Object storage data through the Cloudflare dashboard UI."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/observability/data-studio/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/observability/data-studio/index.md"><meta property="og:title" content="Data Studio · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View and edit SQLite-backed Durable Object storage data through the Cloudflare dashboard UI."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/observability/data-studio/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/observability/data-studio/#page","headline":"Data Studio \u00b7 Cloudflare Durable Objects docs","description":"View and edit SQLite-backed Durable Object storage data through the Cloudflare dashboard UI.","url":"https://developers.cloudflare.com/durable-objects/observability/data-studio/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/observability/data-studio/
  schema: 1
---
<p>Each Durable Object can access private storage using <a href="/durable-objects/api/sqlite-storage-api/">Storage API</a> available on <code>ctx.storage</code>. To view and write to an object's stored data, you can use Durable Objects Data Studio as a UI editor available on the Cloudflare dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="data-studio-only-supported-for-sqlite-backed-objects">Data Studio only supported for SQLite-backed objects</h3>
@markup("md", "content/.markup/bodies/8175.md")
</aside>
<h2 id="view-data-studio">View Data Studio</h2>
<p>You need at least <code>Editor</code> access to the Worker that implements the Durable Object to access Data Studio. Refer to <a href="/workers/authorization/durable-objects/">Durable Objects roles and permissions</a> for more information.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8176.md")
</div>
<ul>
<li>Queries executed by Data Studio send requests to your remote, deployed objects and incur <a href="/durable-objects/platform/pricing/">usage billing</a> for requests, duration, rows read, and rows written. You should use Data Studio as you would handle your production, running objects.</li>
<li>In the <strong>Query</strong> tab when running all statements, each SQL statement is sent as a separate Durable Object request.</li>
</ul>
<h2 id="audit-logging">Audit logging</h2>
<p>All queries issued by the Data Studio are logged with <a href="/fundamentals/account/account-security/review-audit-logs/">audit logging v1</a> for your security and compliance needs.</p>
<ul>
<li>Each query emits two audit logs, a <code>query executed</code> action and a <code>query completed</code> action indicating query success or failure. <code>query_id</code> in the log event can be used to correlate the two events per query.</li>
</ul>
