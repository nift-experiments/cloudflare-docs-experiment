---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/
  description: Example rules for handling detected malicious file uploads.
  full_title: Example rules checking uploaded content objects · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Example rules checking uploaded content objects · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Example rules for handling detected malicious file uploads."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/index.md"><meta property="og:title" content="Example rules checking uploaded content objects · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example rules for handling detected malicious file uploads."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/#page","headline":"Example rules checking uploaded content objects \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Example rules for handling detected malicious file uploads.","url":"https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/malicious-uploads/example-rules/
  schema: 1
---
<h2 id="log-requests-with-an-uploaded-content-object">Log requests with an uploaded content object</h2>
<p>This <a href="/waf/custom-rules/">custom rule</a> example logs all requests with at least one uploaded content object:</p>
<ul>
<li><strong>When incoming requests match:</strong></li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Has content object</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>If you are using the Expression Editor:<br/>
<code>(cf.waf.content_scan.has_obj)</code></p>
<ul>
<li><strong>Action:</strong> <em>Log</em></li>
</ul>
<h2 id="block-requests-to-uri-path-with-a-malicious-content-object">Block requests to URI path with a malicious content object</h2>
<p>This custom rule example blocks requests addressed at <code>/upload.php</code> that contain at least one uploaded content object considered malicious:</p>
<ul>
<li><strong>When incoming requests match:</strong></li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Has malicious content object</td>
<td>equals</td>
<td>True</td>
<td>And</td>
</tr>
<tr>
<td>URI Path</td>
<td>equals</td>
<td><code>/upload.php</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the Expression Editor:<br/>
<code>(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq &quot;/upload.php&quot;)</code></p>
<ul>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="block-requests-with-non-pdf-file-uploads">Block requests with non-PDF file uploads</h2>
<p>This custom rule example blocks requests addressed at <code>/upload</code> with uploaded content objects that are not PDF files:</p>
<ul>
<li><strong>When incoming requests match:</strong><br/>
<code>any(cf.waf.content_scan.obj_types[*] != &quot;application/pdf&quot;) and http.request.uri.path eq &quot;/upload&quot;</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="block-requests-with-uploaded-files-over-500-kb">Block requests with uploaded files over 500 KB</h2>
<p>This custom rule example blocks requests addressed at <code>/upload</code> with uploaded content objects over 500 KB (512,000 bytes) in size:</p>
<ul>
<li><strong>When incoming requests match:</strong><br/>
<code>any(cf.waf.content_scan.obj_sizes[*] &gt; 512000) and http.request.uri.path eq &quot;/upload&quot;</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<h2 id="block-requests-with-uploaded-files-over-the-content-scanning-limit-50-mb">Block requests with uploaded files over the content scanning limit (50 MB)</h2>
<p>This custom rule example blocks requests with uploaded content objects over 50 MB in size (the current content scanning limit):</p>
<ul>
<li><strong>When incoming requests match:</strong><br/>
<code>any(cf.waf.content_scan.obj_sizes[*] &gt;= 52428800)</code></li>
<li><strong>Action:</strong> <em>Block</em></li>
</ul>
<p>In this example, you must also test for equality because currently any file over 50 MB will be handled internally as if it had a size of 50 MB (52,428,800 bytes). This means that using the <code>&gt;</code> (greater than) <a href="/ruleset-engine/rules-language/operators/#comparison-operators">comparison operator</a> would not work for this particular rule — you should use <code>&gt;=</code> (greater than or equal) instead.</p>
