---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/
  description: Investigate profile conformance and sampled violation details.
  full_title: Analyze profile detections · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Analyze profile detections · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Investigate profile conformance and sampled violation details."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/index.md"><meta property="og:title" content="Analyze profile detections · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Investigate profile conformance and sampled violation details."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/#page","headline":"Analyze profile detections \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Investigate profile conformance and sampled violation details.","url":"https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/application-profiles/analyze-profile-detections/
  schema: 1
---
<p>Use <strong>Profile Analysis</strong> in <a href="/waf/analytics/security-analytics/">Security Analytics</a> to investigate profile detections.</p>
<h2 id="understand-request-statuses">Understand request statuses</h2>
<p>Profile Analysis classifies requests with these statuses:</p>
<ul>
<li><strong>Conforms:</strong> The evaluated request matched its applicable profile.</li>
<li><strong>Violates:</strong> The evaluated request did not match its applicable profile.</li>
<li><strong>Not evaluated:</strong> No applicable profile is available, or the profile does not apply.</li>
</ul>
<h2 id="understand-violation-details">Understand violation details</h2>
<p>Sampled violations include structured details about the first detected validation failure:</p>
<table>
<thead>
<tr>
<th>Detail</th>
<th>Meaning</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Location</td>
<td>The request component containing the violation.</td>
<td><code>body</code></td>
</tr>
<tr>
<td>Error class</td>
<td>A stable, broad category for grouping similar violations.</td>
<td><code>constraint_violation</code></td>
</tr>
<tr>
<td>Error detail</td>
<td>An optional, specific reason within the error class.</td>
<td><code>number_not_in_range</code></td>
</tr>
<tr>
<td>Target</td>
<td>An optional parameter, header, cookie, or JSON body path associated with the violation.</td>
<td><code>$.items[0].quantity</code></td>
</tr>
</tbody>
</table>
<p>The error detail or target can be empty when the other fields fully describe the violation. For example, a missing request body has the <code>missing_required</code> error class without a target.</p>
<p>For all possible error classes and details, refer to <a href="/waf/detections/application-profiles/fields/#violation-details">Fields</a>.</p>
<h2 id="review-detections">Review detections</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15548.md")
</div>
<h2 id="interpret-violations">Interpret violations</h2>
<p>A non-conforming request is not necessarily malicious. Releases, new clients, and valid edge cases can produce violations.</p>
<p>Cloudflare runs an <strong>always-on detection</strong> after a profile becomes available. Detection does not block requests by itself.</p>
<p>After reviewing representative traffic, refer to <a href="/waf/detections/application-profiles/enforce-profiles-with-custom-rules/">Enforce profiles with Custom Rules</a>.</p>
