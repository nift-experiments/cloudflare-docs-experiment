---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/
  description: Document API parameters effectively.
  full_title: Parameters · Cloudflare Style Guide
  head_html: <title>Parameters · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Document API parameters effectively."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/index.md"><meta property="og:title" content="Parameters · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Document API parameters effectively."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/#page","headline":"Parameters \u00b7 Cloudflare Style Guide","description":"Document API parameters effectively.","url":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/api-content-strategy/api-content-types/parameters/
  schema: 1
---
<h2 id="purpose">Purpose</h2>
<p>A parameter is an option passed with the endpoint to receive specific information or values.</p>
<h2 id="values">Values</h2>
<p>default, minimum, and maximum</p>
<h2 id="structure">Structure</h2>
<h3 id="required-components">Required Components</h3>
<p><strong>Name</strong>: Name of the parameter formatted as code snippet.</p>
<p><strong>Data type</strong>: Indicates if the parameter is a string, integer, boolean, object, or array.</p>
<p><strong>Description</strong>: Describes what the parameter does. Use a noun phrase for strings, integers, objects, and arrays. Use a verb for booleans. End description with a period.</p>
<p><strong>Required status</strong>: Indicates whether the parameter is required</p>
<h3 id="optional-components">Optional components</h3>
<p><strong>Constraints</strong>: Lists default, minimum, or maximum values for the parameter.</p>
<h2 id="writing-guidelines">Writing guidelines</h2>
<p>When writing the titles and descriptions, keep our voice and tone in mind. Be concise and remember our users come from a variety of technical levels.</p>
<p>Some parameter descriptions are more factual, like <strong>deviceName</strong>, and do not make sense to start with a verb. Other parameters will lend well to beginning with a verb, and this difference is okay.</p>
<p>Try to avoid the passive voice and aim to describe what the parameter does or what it is used for in a concise sentence users can understand.</p>
<p>Below are some examples of parameter descriptions for reference:</p>
<p><strong>deviceName</strong>: The device name.</p>
<p><strong>version</strong>: The Cloudflare One Client version.</p>
<p><strong>per_page</strong>: Sets the maximum number of requested results.</p>
<p><strong>enabled</strong>: Enables or disable a load balancer.</p>
<p><strong>ASN</strong>: The Autonomous System Number (ASN) used to advertise a prefix.</p>
<h2 id="example">Example</h2>
<p><strong>Name</strong>: <code>actor.ip</code></p>
<p><strong>Data type</strong>: <code>string</code></p>
<p><strong>Description</strong>: Filters a request by specific IP address or valid CIDR range.</p>
<p><strong>Required status</strong>: Not required</p>
<p><strong>Values</strong>: No listed default, minimum, or maximum, values.</p>
