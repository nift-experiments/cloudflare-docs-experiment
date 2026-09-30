---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/
  description: Manage API operations through the Web Assets dashboard.
  full_title: Endpoint Management · Cloudflare API Shield docs
  head_html: <title>Endpoint Management · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage API operations through the Web Assets dashboard."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/index.md"><meta property="og:title" content="Endpoint Management · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage API operations through the Web Assets dashboard."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/#page","headline":"Endpoint Management \u00b7 Cloudflare API Shield docs","description":"Manage API operations through the Web Assets dashboard.","url":"https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/management-and-monitoring/endpoint-management/
  schema: 1
---
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Endpoint Management content uses the current <a href="/security/web-assets/">Web Assets</a> dashboard. Go to <strong>Web Assets</strong> &gt; <strong>Operations</strong> to manage <span class="nb-glossary-tooltip" title="API endpoint">API endpoints</span>.</p>
<p>An operation is Cloudflare's term for an endpoint identified by HTTP method, hostname pattern, and path pattern. Web Assets continuously discovers operations, and you can add them manually.</p>
<p>Cloudflare discovered operations are only added to the inventory. To start profiling, select <strong>Learn profile</strong> for the intended operation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="schema-profile-availability">Schema Profile availability</h3>
@markup("md", "content/.markup/bodies/3242.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3241.md")
</aside>
<h2 id="access">Access</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3244.md")
</div>
<h3 id="review-discovered-operations">Review discovered operations</h3>
<p>Web Assets continuously adds discovered operations to the inventory. Discovery does not start profile learning.</p>
<p>Candidate operations can provide context for matching, edge security detections, and <a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a>. You do not need to change every discovered operation.</p>
<a id="add-endpoints-from-schema-validation" />
<h3 id="add-operations-from-schema-validation">Add operations from Schema validation</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3245.md")
</div>
<p>API Shield looks for duplicate operations with the same hostname, method, and path. Duplicate operations are not added.</p>
<a id="add-endpoints-manually" />
<h3 id="add-operations-manually">Add operations manually</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3246.md")
</div>
<p>When adding an operation manually, you can specify variable fields in the path or hostname. Enclose variables in braces, such as <code>/api/user/{var1}/details</code> or <code>{hostVar1}.example.com</code>.</p>
<p>Cloudflare supports hostname variables in the following formats:</p>
<pre tabindex="0"><code class="language-txt">&#10;{hostVar1}.example.com&#10;&#10;foo.{hostVar1}.example.com&#10;&#10;{hostVar2}.{hostVar1}.example.com&#10;</code></pre>
<p>Hostname variables must comprise the entire domain field and must not be used with other text in the field.</p>
<p>The following format is not supported:</p>
<pre tabindex="0"><code class="language-txt">&#10;foo-{hostVar1}.example.com&#10;</code></pre>
<p>For more information on how Cloudflare uses variables in API Shield, refer to the examples from <a href="/api-shield/security/api-discovery/">API Discovery</a>.</p>
<h3 id="edit-operations">Edit operations</h3>
<p>You can edit the identity of an operation.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3247.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="editing-this-operation-will-change-its-id">Editing this operation will change its ID</h3>
@markup("md", "content/.markup/bodies/3240.md")
</aside>
<h3 id="start-profile-learning">Start profile learning</h3>
<p>Start profiling only after reviewing the operation identity.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3248.md")
</div>
<p>For learning requirements, analytics, and enforcement, refer to <a href="/waf/detections/application-profiles/">Application Profiles</a>.</p>
<h3 id="delete-operations-manually">Delete operations manually</h3>
<p>You can delete endpoints one at a time or in bulk.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3249.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3239.md")
</aside>
<a id="endpoint-analysis" />
<h2 id="operation-analysis">Operation analysis</h2>
<p>For each operation in the <code>full</code> state, you can view:</p>
<ul>
<li><strong>Request count</strong>: The total number of requests to the operation over time.</li>
<li><strong>Rate limiting recommendation</strong>: per 10 minutes. This is guided by the request count.</li>
<li><strong>Latency</strong>: The average origin response time in milliseconds (ms). This metric shows how long it takes from the moment a visitor makes a request to the moment the visitor gets a response back from the origin.</li>
<li><strong>Error rate</strong> vs. overall traffic: grouped by 4xx, 5xx, and their sum.</li>
<li><strong>Response size</strong>: The average size of the response (in bytes) returned to the request.</li>
<li><strong>Labels</strong>: The current <a href="/api-shield/management-and-monitoring/endpoint-labels/">labels</a> assigned to the operation.</li>
<li><strong><a href="/api-shield/security/authentication-posture/">Authentication status</a></strong>: The session identifiers observed on successful requests to this operation.</li>
<li><strong>Sequences</strong>: The number of <a href="/api-shield/security/sequence-analytics/">Sequence Analytics</a> sequences containing the operation.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3238.md")
</aside>
<h2 id="using-the-cloudflare-api">Using the Cloudflare API</h2>
<p>You can manage operations through the Cloudflare API. For more information, refer to the <a href="/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/list/">operations API documentation</a>.</p>
<h2 id="sensitive-data-detection">Sensitive Data Detection</h2>
<p>Sensitive data comprises various personally identifiable information and financial data. Cloudflare created this ruleset to address common data loss threats, and the WAF can search for this data in HTTP response bodies from your origin.</p>
<p>API Shield alerts you to sensitive data in responses from full operations. Your zone must also have the <a href="/waf/managed-rules/reference/sensitive-data-detection/">Sensitive Data Detection managed ruleset</a>.</p>
<p>Sensitive Data Detection is available to Enterprise customers on our Advanced application security plan.</p>
<p>After you turn on Sensitive Data Detection, API Shield queries WAF events from the last seven days. Web Assets marks operations that have matched sensitive responses.</p>
<p>Open the operation details to review the detected sensitive data types. Select <strong>Explore Events</strong> to view matched events in Security Events.</p>
<p>After you turn on Sensitive Data Detection for your zone, you can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/data/ruleset/e22d83c647c64a3eae91b71b499d988e/rules">browse the Sensitive Data Detection ruleset</a>. The link will not work if Sensitive Data Detection is not turned on.</p>
<h2 id="limitations">Limitations</h2>
<p>Certain performance metrics, such as latency, are not supported when a request is handled by a Cloudflare service in a way that prevents it from being passed directly to your origin server.</p>
<p>This limitation is specifically observed when:</p>
<ul>
<li>A Cloudflare Worker is running on the URL path.</li>
<li>Other products built on top of Workers, such as <a href="/waiting-room/">Waiting Room</a>, are active on the application.</li>
</ul>
<p>In these scenarios, the system is unable to accurately measure the origin response time, and the metric will not be populated in the dashboard.</p>
