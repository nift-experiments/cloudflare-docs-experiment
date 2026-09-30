---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/example-rules/
  description: Example custom error rules for common error handling scenarios.
  full_title: Example custom error rules · Cloudflare Rules docs
  head_html: <title>Example custom error rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Example custom error rules for common error handling scenarios."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/example-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/example-rules/index.md"><meta property="og:title" content="Example custom error rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example custom error rules for common error handling scenarios."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/example-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/example-rules/#page","headline":"Example custom error rules \u00b7 Cloudflare Rules docs","description":"Example custom error rules for common error handling scenarios.","url":"https://developers.cloudflare.com/rules/custom-errors/example-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/example-rules/
  schema: 1
---
<p>The provided examples use the following fields in their rule expressions:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/fields/reference/http.response.code/"><code>http.response.code</code></a> (Response Status Code): Represents the HTTP status code returned to the client, either set by a Cloudflare product or returned by the origin server. Use this field to customize the response for error codes returned by the origin server or by a Cloudflare product such as a Worker.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/"><code>cf.response.1xxx_code</code></a>: Contains the specific error code for Cloudflare-generated errors. This field will only work for Cloudflare-generated errors such as <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">52X</a> and <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">1XXX</a>.</p>
</li>
</ul>
<h3 id="custom-json-response-for-all-5xx-errors">Custom JSON response for all 5XX errors</h3>
<p>This example configures a custom JSON error response for all 5XX errors (<code>500</code>-<code>599</code>) in a zone. The HTTP status code of the custom error response will be set to <code>530</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12981.md")
</div></div>
<h3 id="custom-html-response-with-updated-status-code">Custom HTML response with updated status code</h3>
<p>This example configures a custom HTML error response for responses with a <code>500</code> HTTP status code, and redefines the response status code to <code>503</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12984.md")
</div></div>
<h3 id="custom-html-response-for-cloudflare-1020-errors">Custom HTML response for Cloudflare 1020 errors</h3>
<p>This example configures a custom HTML error response for <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/">Cloudflare error 1020</a> (Access Denied).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12987.md")
</div></div>
<h3 id="custom-error-asset-created-from-a-url">Custom error asset created from a URL</h3>
<p>This example configures a custom error rule returning a previously created custom error asset named <code>500_error_template</code> for responses with a <code>500</code> HTTP status code.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12990.md")
</div></div>
