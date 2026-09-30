---
cp9:
  canonical: https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/
  description: This tutorial shows you how to modify both the URI path and the Host header of incoming requests using Transform Rules and Origin Rules.
  full_title: Change URI path and Host header · Cloudflare Rules docs
  head_html: <title>Change URI path and Host header · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial shows you how to modify both the URI path and the Host header of incoming requests using Transform Rules and Origin Rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/index.md"><meta property="og:title" content="Change URI path and Host header · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial shows you how to modify both the URI path and the Host header of incoming requests using Transform Rules and Origin Rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Transform Rules,Origin Rules"><meta name="pcx_tags" content="Headers,URL rewrite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/#page","headline":"Change URI path and Host header \u00b7 Cloudflare Rules docs","description":"This tutorial shows you how to modify both the URI path and the Host header of incoming requests using Transform Rules and Origin Rules.","url":"https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","URL rewrite"]}</script>
  markdown: true
  noindex: false
  route: /rules/origin-rules/tutorials/change-uri-path-and-host-header/
  schema: 1
---
<p>This tutorial will instruct you how to modify both the URI path and the <code>Host</code> header of incoming requests using <a href="/rules/transform/">Transform Rules</a> and Origin Rules.</p>
<p>Your website visitors will be routed from <code>https://&lt;YOUR_SOURCE_HOSTNAME&gt;/uploads/*</code> to <code>https://&lt;YOUR_TARGET_HOSTNAME&gt;/*</code>.</p>
<p>In this tutorial you will do the following:</p>
<ol>
<li>Create a URL rewrite to remove <code>/uploads</code> from the path.</li>
<li>Create an origin rule to modify the <code>Host</code> header to desired hostname.</li>
</ol>
<p>By following these steps, you can effectively manage both URI paths and <code>Host</code> headers to route traffic appropriately and optimize request handling.</p>
<h2 id="1-create-a-url-rewrite"><ol>
<li>Create a URL rewrite</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13078.md")
</div>
<h2 id="2-create-an-origin-rule"><ol start="2">
<li>Create an origin rule</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13075.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13082.md")
</div>
<h2 id="final-remarks">Final remarks</h2>
<p>After completing this tutorial, incoming traffic for <code>https://&lt;YOUR_SOURCE_HOSTNAME&gt;/uploads/*</code> will be routed to <code>https://&lt;YOUR_TARGET_HOSTNAME&gt;/*</code>.</p>
<p>Ensure the filters for the <a href="/rules/transform/url-rewrite/">URL rewrite</a> and the <a href="/rules/origin-rules/">origin rule</a> (or <a href="/rules/cloud-connector/">Cloud Connector</a> rule) are precise to avoid unintended rule executions.</p>
<p>Remember that rules are evaluated <a href="/ruleset-engine/reference/phases-list/">in sequence</a>, so Transform Rules (including URL rewrites) run before Origin Rules or Cloud Connector.</p>
