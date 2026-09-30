---
cp9:
  canonical: https://developers.cloudflare.com/d1/best-practices/remote-development/
  description: Develop against a D1 database remotely using the Cloudflare dashboard playground.
  full_title: Remote development · Cloudflare D1 docs
  head_html: <title>Remote development · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Develop against a D1 database remotely using the Cloudflare dashboard playground."><link rel="canonical" href="https://developers.cloudflare.com/d1/best-practices/remote-development/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/best-practices/remote-development/index.md"><meta property="og:title" content="Remote development · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Develop against a D1 database remotely using the Cloudflare dashboard playground."><meta property="og:url" content="https://developers.cloudflare.com/d1/best-practices/remote-development/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/best-practices/remote-development/#page","headline":"Remote development \u00b7 Cloudflare D1 docs","description":"Develop against a D1 database remotely using the Cloudflare dashboard playground.","url":"https://developers.cloudflare.com/d1/best-practices/remote-development/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/best-practices/remote-development/
  schema: 1
---
<p>D1 supports remote development using the <a href="/workers/playground/#use-the-playground">dashboard playground</a>. The dashboard playground uses a browser version of Visual Studio Code, allowing you to rapidly iterate on your Worker entirely in your browser.</p>
<h2 id="1-bind-a-d1-database-to-a-worker"><ol>
<li>Bind a D1 database to a Worker</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7378.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing Worker.
3. Go to the **Bindings** tab.
4. Select **Add binding**.
5. Select **D1 database** > **Add binding**.
6. Enter a variable name, such as `DB`, and select the D1 database you wish to access from this Worker.
7. Select **Add binding**.
<h2 id="2-start-a-remote-development-session"><ol start="2">
<li>Start a remote development session</li>
</ol></h2>
<ol>
<li>On the Worker's page on the Cloudflare dashboard, select <strong>Edit Code</strong> at the top of the page.</li>
<li>Your Worker now has access to D1.</li>
</ol>
<p>Use the following Worker script to verify that the Worker has access to the bound D1 database:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    const res = await env.DB.prepare(&quot;SELECT 1;&quot;).run();&#10;    return new Response(JSON.stringify(res, null, 2));&#10;  },&#10;};&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn <a href="/d1/observability/debug-d1/">how to debug D1</a>.</li>
<li>Understand how to <a href="/workers/observability/logs/">access logs</a> generated from your Worker and D1.</li>
</ul>
