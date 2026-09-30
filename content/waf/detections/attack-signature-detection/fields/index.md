---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/
  description: Reference Attack Signature Detection fields, example values, Security Rules usage, and Logpush mappings.
  full_title: Fields · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Fields · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference Attack Signature Detection fields, example values, Security Rules usage, and Logpush mappings."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/index.md"><meta property="og:title" content="Fields · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference Attack Signature Detection fields, example values, Security Rules usage, and Logpush mappings."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/#page","headline":"Fields \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Reference Attack Signature Detection fields, example values, Security Rules usage, and Logpush mappings.","url":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/attack-signature-detection/fields/
  schema: 1
---
<p>Attack Signature Detection populates these request fields when signatures match:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Categories associated with all matching signatures. A signature can have more than one category.</td>
</tr>
<tr>
<td><code>cf.waf.signature.request.confidence</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Confidence values associated with matching signatures. Supported values are <code>high</code> and <code>low</code>.</td>
</tr>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Refs for matching signatures, up to 10 per request. Each Ref matches the corresponding Managed Rule public Rule ID.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15541.md")
</aside>
<p>All three fields are available in Security Analytics and Security Rules. You can reference them in rules created in the dashboard or through the API.</p>
<h2 id="example-values">Example values</h2>
<p>The fields can contain values like these:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><code>[&quot;sqli&quot;, &quot;cve-2025-55182&quot;]</code></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.confidence</code></td>
<td><code>[&quot;high&quot;]</code></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><code>[&quot;d68f8101f6e14e25aefcaea69c530a29&quot;]</code></td>
</tr>
</tbody>
</table>
<h2 id="rules-language-examples">Rules language examples</h2>
<p>Use <code>any()</code> to test array elements:</p>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.categories[*] eq &quot;sqli&quot;)&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.confidence[*] eq &quot;high&quot;)&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.refs[*] eq &quot;d68f8101f6e14e25aefcaea69c530a29&quot;)&#10;</code></pre>
<p>For rollout guidance, refer to <a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Use attack signatures in Security Rules</a>.</p>
<h2 id="logpush-fields">Logpush fields</h2>
<p>Signature Refs and categories are available in Logpush:</p>
<table>
<thead>
<tr>
<th>Rules field</th>
<th>Logpush field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturerefs"><code>wafRequestSignatureRefs</code></a></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturecategories"><code>wafRequestSignatureCategories</code></a></td>
</tr>
</tbody>
</table>
<p>Only signature Ref and category mappings are available in Logpush.</p>
