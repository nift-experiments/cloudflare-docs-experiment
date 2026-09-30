---
cp9:
  canonical: https://developers.cloudflare.com/flagship/reference/evaluation-reasons/
  description: Flagship evaluation reason values and error codes returned by binding details methods and the OpenFeature SDK.
  full_title: Evaluation reasons and error codes · Cloudflare Flagship docs
  head_html: <title>Evaluation reasons and error codes · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Flagship evaluation reason values and error codes returned by binding details methods and the OpenFeature SDK."><link rel="canonical" href="https://developers.cloudflare.com/flagship/reference/evaluation-reasons/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/reference/evaluation-reasons/index.md"><meta property="og:title" content="Evaluation reasons and error codes · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Flagship evaluation reason values and error codes returned by binding details methods and the OpenFeature SDK."><meta property="og:url" content="https://developers.cloudflare.com/flagship/reference/evaluation-reasons/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/reference/evaluation-reasons/#page","headline":"Evaluation reasons and error codes \u00b7 Cloudflare Flagship docs","description":"Flagship evaluation reason values and error codes returned by binding details methods and the OpenFeature SDK.","url":"https://developers.cloudflare.com/flagship/reference/evaluation-reasons/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/reference/evaluation-reasons/
  schema: 1
---
<p>When you evaluate a flag using the binding's <code>*Details</code> methods or the OpenFeature SDK, the response includes a <code>reason</code> field that explains why a particular value was returned. If an error occurs, the response includes an <code>errorCode</code> field.</p>
<h2 id="evaluation-reasons">Evaluation reasons</h2>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TARGETING_MATCH</code></td>
<td>A targeting rule's conditions matched the evaluation context, and the rule's variant was returned.</td>
</tr>
<tr>
<td><code>SPLIT</code></td>
<td>A targeting rule with a percentage rollout matched. The user fell within the rollout percentage and received the rule's variant.</td>
</tr>
<tr>
<td><code>DEFAULT</code></td>
<td>No targeting rule matched the evaluation context. The flag's default variant was returned.</td>
</tr>
<tr>
<td><code>DISABLED</code></td>
<td>The flag is disabled. The default variant was returned regardless of targeting rules.</td>
</tr>
<tr>
<td><code>CACHED</code></td>
<td>The SDK returned a cached evaluation result.</td>
</tr>
<tr>
<td><code>ERROR</code></td>
<td>Evaluation failed and the default value was returned.</td>
</tr>
</tbody>
</table>
<h2 id="error-codes">Error codes</h2>
<p>When an evaluation error occurs, the method returns the default value you provided. The <code>*Details</code> methods include additional metadata about the error.</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TYPE_MISMATCH</code></td>
<td>The flag's variant type does not match the requested type. For example, calling <code>getBooleanValue</code> on a flag whose variant is a string. The default value is returned.</td>
</tr>
<tr>
<td><code>FLAG_NOT_FOUND</code></td>
<td>The specified flag key does not exist in the app. The default value is returned.</td>
</tr>
<tr>
<td><code>INVALID_CONTEXT</code></td>
<td>The evaluation context contains unsupported values, such as objects or arrays in HTTP evaluation. The default value is returned.</td>
</tr>
<tr>
<td><code>PARSE_ERROR</code></td>
<td>The SDK received an invalid evaluation response. The default value is returned.</td>
</tr>
<tr>
<td><code>GENERAL</code></td>
<td>An unexpected error occurred during evaluation, such as a timeout or network failure. The default value is returned.</td>
</tr>
</tbody>
</table>
<h2 id="example">Example</h2>
<p>The following example inspects evaluation details returned by <code>getBooleanDetails</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8731.md")
</div>
