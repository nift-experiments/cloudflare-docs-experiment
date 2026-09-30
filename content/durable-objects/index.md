---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/
  description: Build stateful serverless applications with Durable Objects, including AI agents, real-time chat, and collaborative apps.
  full_title: Overview · Cloudflare Durable Objects docs
  head_html: <title>Overview · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Build stateful serverless applications with Durable Objects, including AI agents, real-time chat, and collaborative apps."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/index.md"><meta property="og:title" content="Overview · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build stateful serverless applications with Durable Objects, including AI agents, real-time chat, and collaborative apps."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/durable-objects/#page","headline":"Overview \u00b7 Cloudflare Durable Objects docs","description":"Build stateful serverless applications with Durable Objects, including AI agents, real-time chat, and collaborative apps.","url":"https://developers.cloudflare.com/durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1081.md")
</div>
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>Durable Objects provide a building block for stateful applications and distributed systems.</p>
<p>Use Durable Objects to build applications that need coordination among multiple clients, like collaborative editing tools, interactive chat, multiplayer games, live notifications, and deep distributed systems, without requiring you to build serialization and coordination primitives on your own.</p>
<p><a class="nb-link-button" href="/durable-objects/get-started/">Get started</a></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1080.md")
</aside>
<h3 id="what-are-durable-objects">What are Durable Objects?</h3>
<p>A Durable Object is a special kind of <a href="/workers/">Cloudflare Worker</a> which uniquely combines compute with storage. Like a Worker, a Durable Object is automatically provisioned geographically close to where it is first requested, starts up quickly when needed, and shuts down when idle. You can have millions of them around the world. However, unlike regular Workers:</p>
<ul>
<li>Each Durable Object has a <strong>globally-unique name</strong>, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together.</li>
<li>Each Durable Object has some <strong>durable storage</strong> attached. Since this storage lives together with the object, it is strongly consistent yet fast to access.</li>
</ul>
<p>Therefore, Durable Objects enable <strong>stateful</strong> serverless applications.</p>
<p>For more information, refer to the full <a href="/durable-objects/concepts/what-are-durable-objects/">What are Durable Objects?</a> page.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1083.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1084.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1085.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1086.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1087.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1088.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1089.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1095.md")
</div>
