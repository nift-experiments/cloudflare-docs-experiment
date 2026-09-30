---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/reference/parameters/
  description: Configurable parameters for custom error rules.
  full_title: Custom Errors parameters · Cloudflare Rules docs
  head_html: <title>Custom Errors parameters · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Configurable parameters for custom error rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/reference/parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/reference/parameters/index.md"><meta property="og:title" content="Custom Errors parameters · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configurable parameters for custom error rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/reference/parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/reference/parameters/#page","headline":"Custom Errors parameters \u00b7 Cloudflare Rules docs","description":"Configurable parameters for custom error rules.","url":"https://developers.cloudflare.com/rules/custom-errors/reference/parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/reference/parameters/
  schema: 1
---
<h2 id="custom-error-rules">Custom error rules</h2>
<p><a href="/rules/custom-errors/#custom-error-rules">Custom error rules</a> define when a custom error gets triggered and the content that is served to visitors. Rule parameters are the following:</p>
<h3 id="response-type">Response type</h3>
<p>API name: <em>N/A</em> (handled via <a href="#asset"><code>asset_name</code></a> and <a href="#response"><code>content_type</code></a> parameters)</p>
<p>The content type of the inline response to send to the website visitor (JSON, HTML, Text, or XML), or <strong>Custom error asset</strong> if sending the content of a custom error asset.</p>
<p>When using the API you must either set the <code>asset_name</code> or set both the <code>content_type</code> and <code>content</code> parameters. Refer to <a href="#response">JSON response / HTML response / Text response / XML response</a>.</p>
<h3 id="response-code">Response code</h3>
<p>API name: <strong><code>status_code</code></strong> <span class="nb-type">Integer</span> <span class="nb-metainfo">Optional</span></p>
<p>The HTTP status code of the response. If provided, this value will override the current response status code.</p>
<p>The status code must be between <code>400</code> and <code>999</code>.</p>
<h3 id="asset">Asset</h3>
<p>API name: <strong><code>asset_name</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Optional</span></p>
<p>The name of the <a href="#custom-error-assets">custom error asset</a> you previously uploaded (in the dashboard, you can create an asset when creating the rule). The asset may include <a href="/rules/custom-errors/reference/error-tokens/">error tokens</a> that will be replaced with real values before sending the error response to the visitor.</p>
<p>A custom error rule can only reference an asset defined in the same scope as the rule (that is, in the same zone or account).</p>
<p>In the dashboard, this parameter is only available when you select <code>Custom error asset</code> in <strong>Response type</strong>.</p>
<p>When using the API, you must provide either the <code>asset_name</code> or the <code>content</code> parameter.</p>
<h3 id="json-response-html-response-text-response-xml-response-response">JSON response / HTML response / Text response / XML response </h3>
<p>API names: <strong><code>content</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Optional</span> and <strong><code>content_type</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Required</span></p>
<p>The response body to return. It can include <a href="/rules/custom-errors/reference/error-tokens/">error tokens</a> that will be replaced with real values before sending the error response to the visitor.</p>
<p>You must provide either the <code>asset_name</code> or the <code>content</code> parameter.</p>
<p>The maximum content size is 10 KB.</p>
<p>When using the API you must also set the <code>content_type</code> parameter, which defines the content type of the returned response. The value must be one of the following:</p>
<ul>
<li><code>text/html</code></li>
<li><code>text/plain</code></li>
<li><code>application/json</code></li>
<li><code>text/xml</code></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13065.md")
</aside>
<h2 id="custom-error-assets">Custom error assets</h2>
<p>A <a href="/rules/custom-errors/#custom-error-assets">custom error asset</a> corresponds to a web resource such as an HTML web page (including any referenced images, CSS, and JavaScript code) that Cloudflare fetches and saves based on a URL you provide, to be served to visitors as an error page.</p>
<p>Custom error assets have the following parameters:</p>
<h3 id="asset-name">Asset name</h3>
<p>API name: <strong><code>name</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Required</span></p>
<p>The name of the custom error asset. Example value: <code>&quot;500_error_template&quot;</code>.</p>
<p>An asset name can contain the following characters:</p>
<pre tabindex="0"><code>- Uppercase and lowercase letters (`A-Z` and `a-z`)&#10;- Numbers (`0-9`)&#10;- The underscore (`_`) character&#10;</code></pre>
<p>The maximum length is 200 characters.</p>
<h3 id="description">Description</h3>
<p>API name: <strong><code>description</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Optional</span></p>
<p>A string describing the custom error asset. Example value: <code>&quot;Standard 5xx error template page&quot;</code>.</p>
<h3 id="asset-address">Asset address</h3>
<p>API name: <strong><code>url</code></strong> <span class="nb-type">String</span> <span class="nb-metainfo">Required</span></p>
<p>The URL of the page you want Cloudflare to fetch and store, to be served later to visitors as error pages according to the configured <a href="#custom-error-rules">custom error rules</a>. Example value: <code>&quot;https://example.com/errors/500.html&quot;</code>.</p>
<p>When you create or update an asset and provide a URL, Cloudflare collects any images, CSS, and JavaScript code used in the page, minifies the content, and saves it internally.</p>
<p>The content of the page at the specified URL may include <a href="/rules/custom-errors/reference/error-tokens/">error tokens</a> that will be replaced with real values before sending the error response to the visitor.</p>
<p>When using the dashboard, you can later trigger another fetch to get the latest version of the page along with its resources, and store it internally.</p>
<p>When using the API, if you update an asset and provide the same URL, Cloudflare will fetch the URL again, along with its resources, and store it internally.</p>
<p>The maximum asset size is 1.5 MB.</p>
