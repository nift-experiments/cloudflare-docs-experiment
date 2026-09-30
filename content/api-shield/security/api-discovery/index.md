---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/api-discovery/
  description: Map out and understand your API attack surface with API Discovery.
  full_title: API Discovery · Cloudflare API Shield docs
  head_html: <title>API Discovery · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Map out and understand your API attack surface with API Discovery."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/api-discovery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/api-discovery/index.md"><meta property="og:title" content="API Discovery · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map out and understand your API attack surface with API Discovery."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/api-discovery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/api-discovery/#page","headline":"API Discovery \u00b7 Cloudflare API Shield docs","description":"Map out and understand your API attack surface with API Discovery.","url":"https://developers.cloudflare.com/api-shield/security/api-discovery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/api-discovery/
  schema: 1
---
<p>Most development teams struggle to keep track of their APIs. Cloudflare API Discovery helps you map out and understand your API attack surface — the full set of endpoints that could be targeted by attackers.</p>
<h2 id="process">Process</h2>
<p>Cloudflare produces a map of <span class="nb-glossary-tooltip" title="API endpoint">API endpoints</span> by grouping similar request paths together (path normalization).</p>
<p>For example, you might have thousands of APIs, but a lot of the calls look similar, such as:</p>
<ul>
<li><code>api.example.com/profile/238</code></li>
<li><code>api.example.com/profile/392</code></li>
</ul>
<p>Both paths serve a similar purpose — retrieving user profiles — but they are not identical. To simplify your endpoints, these examples might both map to <code>api.example.com/profile/*</code>.</p>
<p>API Discovery runs this process across all your traffic, generating a simple map of endpoints that might look like:</p>
<pre tabindex="0"><code>/api/login/{customer_identifier}&#10;/api/auth&#10;/api/account/{customer_identifier}&#10;/api/password_reset&#10;/api/logout&#10;</code></pre>
<p>Similarly, if you have multiple subdomains that share the same set of endpoints, Cloudflare consolidates subdomains:</p>
<pre tabindex="0"><code class="language-txt">us-api.example.com/api/v1/users/{var1}&#10;de-api.example.com/api/v1/users/{var1}&#10;fr-api.example.com/api/v1/users/{var1}&#10;jp-api.example.com/api/v1/users/{var1}&#10;</code></pre>
<p>Cloudflare consolidates these to <code>{hostVar1}.example.com/api/v1/users/{var1}</code>.</p>
<p>For more technical details, refer to the <a href="https://blog.cloudflare.com/ml-api-discovery-and-schema-learning/">blog post</a>.</p>
<h3 id="discovered-operations">Discovered operations</h3>
<p>Web Assets adds discovered API endpoints to the operation inventory as candidate operations. Candidate operations provide context for matching, logging, detections, and rules before you manually review them.</p>
<p>You do not need to promote every discovered operation. Promote an operation to move it to the <code>full</code> state and start profile learning. Full operations support persisted API profiles, risk findings, and protections that require a known API endpoint.</p>
<p>To promote a discovered operation:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3201.md")
</div>
<p>Cloudflare moves the operation to the <code>full</code> state. The row action then changes to <strong>Profile learned</strong>. For more information, refer to <a href="/security/web-assets/manage-operations/#promote-an-operation">Promote an operation</a>.</p>
<h3 id="machine-learning-based-discovery">Machine learning-based discovery</h3>
<p>Your API endpoints are discovered with both session identifier-based discovery and machine learning-based discovery.</p>
<p>To access machine learning-based discovery:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3202.md")
</div>
<p>If all of your zone's API traffic contains the <span class="nb-glossary-tooltip" title="session identifier">session identifier</span> that you have configured, both sources may deliver the same results due to similarities between their underlying methodology. Machine learning-based discovery can identify API traffic regardless of whether your API uses a session identifier.</p>
<p>You can direct any feedback about your API Discovery results to your account team.</p>
<h2 id="requirements">Requirements</h2>
<p>API Discovery requires an active API Shield subscription at both the account and zone level. If your subscription is active at the account level but not assigned to the zone, Discovery will not run for that zone.</p>
<p>For an endpoint to appear in Discovery results, every request must meet the following conditions:</p>
<ul>
<li>The request must return a <code>2xx</code> response code from the Cloudflare edge.</li>
<li>The request must not originate directly from a Cloudflare Worker. Traffic sent through the Cloudflare traffic simulator or other Worker-based test harnesses will not be counted toward Discovery thresholds.</li>
<li>The endpoint must receive at least 500 requests within a continuous 10-day period.</li>
</ul>
<p>For more information, refer to <a href="/security/web-assets/manage-operations/#discovery-requirements/">Discovery requirements</a>.</p>
<h2 id="availability">Availability</h2>
<p>API Discovery is only available for Enterprise customers. If you are an Enterprise customer interested in this product, contact your account team.</p>
