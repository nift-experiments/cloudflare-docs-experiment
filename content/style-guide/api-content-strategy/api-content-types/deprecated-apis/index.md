---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/
  description: Document deprecated API versions.
  full_title: Deprecated APIs · Cloudflare Style Guide
  head_html: <title>Deprecated APIs · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Document deprecated API versions."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/index.md"><meta property="og:title" content="Deprecated APIs · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Document deprecated API versions."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/#page","headline":"Deprecated APIs \u00b7 Cloudflare Style Guide","description":"Document deprecated API versions.","url":"https://developers.cloudflare.com/style-guide/api-content-strategy/api-content-types/deprecated-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/api-content-strategy/api-content-types/deprecated-apis/
  schema: 1
---
<h2 id="purpose">Purpose</h2>
<p>The purpose of Deprecated API content is to communicate that Cloudflare no longer supports an endpoint and to provide users with an alternative option.</p>
<h2 id="tone">Tone</h2>
<p>instructional, straightforward</p>
<h2 id="content-type">content_type</h2>
<p><code>reference</code></p>
<h2 id="structure">Structure</h2>
<h3 id="required-components">Required components</h3>
<p><strong>Deprecated endpoint name</strong>: Must match what existed in the non-deprecated <a href="/style-guide/api-content-strategy/api-content-types/endpoints/">Endpoint</a>.</p>
<p><strong>Context</strong>:  Brief description of what is happening, why Cloudflare is deprecating this endpoint, and any other important information. Avoid using time-bound descriptors (today, tomorrow, in one week, etc). Instead, be specific when including dates.</p>
<p><strong>Replacement</strong>: A description of and/or link to the alternative endpoint OR an explanation as to why Cloudflare is removing the capability of that endpoint.</p>
<p><strong>End of life date</strong>: The date by which users will no longer be able to use that endpoint. Format full month name, date, and year (May 10, 2021).</p>
<h3 id="optional-components">Optional components</h3>
<p>A complete list of endpoints or related APIs that are being deprecated</p>
<h2 id="additional-information">Additional information</h2>
<p>Add API deprecation notices to the API deprecations page by deprecation date and not alphabetically by endpoint.</p>
<p>When an endpoint will be deprecated in a specified timeframe but is still available, add a note to the endpoint description about the upcoming deprecation (&quot;<code>&lt;name of endpoint&gt;</code> will be deprecated on <code>&lt;full month name, date, year&gt;</code>. Use the <code>&lt;alternative endpoint&gt;</code> instead.&quot;).</p>
<h2 id="examples">Examples</h2>
<p>Cloudflare Images - Create authenticated direct upload URL v1</p>
<p>End of life date: July 1, 2022</p>
<p>This endpoint is deprecated in favor of using v2, which allows you to control metadata, define an access policy, and get the image ID.</p>
<p>Deprecated API:</p>
<p><code>POST accounts/:account_identifier/images/v1/direct_upload</code></p>
<p>Replacement:</p>
<p><code>POST accounts/:account_identifier/images/v2/direct_upload</code></p>
