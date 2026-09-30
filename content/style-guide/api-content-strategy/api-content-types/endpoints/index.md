---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/
  description: Document API endpoints clearly.
  full_title: Endpoints · Cloudflare Style Guide
  head_html: <title>Endpoints · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Document API endpoints clearly."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/index.md"><meta property="og:title" content="Endpoints · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Document API endpoints clearly."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/#page","headline":"Endpoints \u00b7 Cloudflare Style Guide","description":"Document API endpoints clearly.","url":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/api-content-strategy/api-content-types/endpoints/
  schema: 1
---
<h2 id="purpose">Purpose</h2>
<p>An endpoint is used to make HTTPS requests, and the <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>PATCH</code>, and <code>DELETE</code> methods dictate how to interact with the resource.</p>
<h2 id="structure">Structure</h2>
<h3 id="required-components">Required Components</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14613.md")
</aside>
<p><strong>Title</strong>: Title of the endpoint using sentence casing (first word capitalized). The titles do not use punctuation marks at the end of the title. Simple cases usually take one of the following forms:</p>
<p>Endpoints that act on/return a single item: verb + indefinite article + singular resource name.</p>
<ul>
<li>Example: Get a list item</li>
</ul>
<p>Endpoints that act on/return a collection of items: verb + plural resource name.</p>
<ul>
<li>Example: Get list items</li>
</ul>
<p><strong>Description</strong>: Describes what the endpoint does or how it should be used. Use punctuation at the end of the description.</p>
<p><strong>Plan availability</strong>: Lists the plan required to use the endpoint, such as Free, Pro, Business, or Enterprise.</p>
<p><strong>Method</strong>: Includes the type of method, such as <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>PATCH</code>, or <code>DELETE</code>.</p>
<p><strong>Endpoint</strong>: Lists the endpoint and should be stylized as code snippet.</p>
<p>When an endpoint will be deprecated in a specified timeframe but is still available, add a note to the endpoint description about the upcoming deprecation (&quot;<code>&lt;name of endpoint&gt;</code> will be deprecated on <code>&lt;full month name, date, year&gt;</code>. Use the <code>&lt;alternative endpoint&gt;</code> instead&quot;). Refer to <a href="/style-guide/api-content-strategy/api-content-types/deprecated-apis/">Deprecated APIs</a> for more information.</p>
<h3 id="optional-components">Optional components</h3>
<p><strong>Required permissions</strong>: Additional permissions at the user level that are required to use the endpoint.</p>
<h2 id="writing-guidelines">Writing guidelines</h2>
<p>When writing the titles and descriptions, keep our voice and tone in mind. Be concise and remember our users come from a variety of technical levels. Also, write in the active voice as much as possible to avoid sounding robotic and to make the information easier to understand.</p>
<p>Below are some examples of endpoint titles and descriptions for reference:</p>
<ul>
<li><strong>Get domain</strong>: Fetches a single domain.</li>
<li><strong>List workers</strong>: Fetches a list of uploaded workers.</li>
<li><strong>List pools</strong>: Lists configured pools.</li>
<li><strong>Create waiting room</strong>: Creates a new waiting room.</li>
<li><strong>Update health check</strong>: Updates configured health checks.</li>
</ul>
<h2 id="example">Example</h2>
<p><strong>Title</strong>: Get user audit logs</p>
<p><strong>Description</strong>: Gets a list of audit logs for a user account.</p>
<p><strong>Plan availability</strong>: Free, Pro, Business, Enterprise</p>
<p><strong>Method</strong>: <code>GET</code></p>
<p><strong>Endpoint</strong>: user/audit_logs</p>
