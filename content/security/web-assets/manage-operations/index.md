---
cp9:
  canonical: https://developers.cloudflare.com/security/web-assets/manage-operations/
  description: Manage operations and start profile learning in Web Assets.
  full_title: Manage operations · Security dashboard docs
  head_html: <title>Manage operations · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage operations and start profile learning in Web Assets."><link rel="canonical" href="https://developers.cloudflare.com/security/web-assets/manage-operations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/web-assets/manage-operations/index.md"><meta property="og:title" content="Manage operations · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage operations and start profile learning in Web Assets."><meta property="og:url" content="https://developers.cloudflare.com/security/web-assets/manage-operations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/web-assets/manage-operations/#page","headline":"Manage operations \u00b7 Security dashboard docs","description":"Manage operations and start profile learning in Web Assets.","url":"https://developers.cloudflare.com/security/web-assets/manage-operations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/web-assets/manage-operations/
  schema: 1
---
<h2 id="operation-states">Operation states</h2>
<p>Each operation has one of the following states:</p>
<table>
<thead>
<tr>
<th>State</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>full</code></td>
<td>An operation that you selected, added manually, or created from a schema. Full operations are used for matching, logging, detections, and rules.</td>
</tr>
<tr>
<td><code>candidate</code></td>
<td>An operation that Cloudflare discovered from traffic. Candidate operations are used for matching, logging, detections, and rules before you manually review them.</td>
</tr>
<tr>
<td><code>shadow</code></td>
<td>An operation that exists in Web Assets but is not used for matching, logging, detections, or rules.</td>
</tr>
</tbody>
</table>
<p>You do not need to move every discovered operation to the <code>full</code> state. Candidate operations provide operation context automatically. Profile learning starts only when you select <strong>Learn profile</strong>.</p>
<h2 id="discovery-requirements">Discovery requirements</h2>
<p>If an operation does not appear in Web Assets, Cloudflare may not have observed enough valid requests over a continuous period. Discovery only processes requests that satisfy all of the following requirements:</p>
<ul>
<li>The request must return a <code>2xx</code> response code from the Cloudflare edge.</li>
<li>The request must not come directly from Cloudflare Workers.</li>
<li>The operation must receive at least 500 requests within a 10-day period.</li>
</ul>
<h2 id="discovered-operations">Discovered operations</h2>
<p>Discovery continuously identifies operations from proxied HTTP traffic. Discovery groups similar request paths together by using path normalization.</p>
<p>For example, discovery can group these requests:</p>
<pre tabindex="0"><code class="language-txt">GET https://api.example.com/profile/238&#10;GET https://api.example.com/profile/392&#10;</code></pre>
<p>Discovery can group them into one operation:</p>
<pre tabindex="0"><code class="language-txt">GET api.example.com/profile/{var1}&#10;</code></pre>
<p>Discovered operations are used for matching before you manually refine them. This provides operation context without requiring a state change first.</p>
<p>Discovery-backed matching is subject to plan availability and system limits. Cloudflare currently sends up to 3,000 operations per zone to the edge for matching. Operations in the <code>full</code> state are prioritized first, followed by operations in the <code>candidate</code> state.</p>
<h2 id="start-profile-learning">Start profile learning</h2>
<p>Select <strong>Learn profile</strong> to start intentional profile learning. Discovery, manual creation, and editing do not start profiling.</p>
<p>Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.</p>
<p>For a candidate or shadow operation, this action also moves the operation into the <code>full</code> state. An operation already in the <code>full</code> state remains there. Cloudflare then learns expected request structure from qualifying traffic.</p>
<p>For API endpoints, API Shield also collects data for other context:</p>
<ul>
<li>Request structures through <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">schema learning</a></li>
<li>Normal request volume through <a href="/api-shield/security/volumetric-abuse-detection/">rate limit recommendations</a></li>
<li>Authentication usage through <a href="/api-shield/security/authentication-posture/">Authentication Posture</a></li>
<li>Persisted security findings through <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">API endpoint risk labels</a></li>
</ul>
<p>Each feature has separate data and timing requirements. For Schema Profiles, refer to <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a>.</p>
<p>Full operations can also use protections that require a known API endpoint, including <a href="/api-shield/security/schema-validation/">Schema Validation</a>, <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">fallthrough rules</a>, and <a href="/api-shield/security/sequence-mitigation/">sequence mitigation</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13832.md")
</div>
<p>After the profile becomes available, select <strong>View details</strong>. Review the learned schema under <strong>Security overview</strong>.</p>
<h2 id="traffic-matching-behavior">Traffic matching behavior</h2>
<p>Cloudflare matches each request to one operation at the edge. When more than one operation pattern could match the same request, the more specific operation wins.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="matching-priority">Matching priority</h3>
@markup("md", "content/.markup/bodies/13831.md")
</aside>
<p>For example, these operations could both match <code>GET https://example.com/checkout/pay</code>:</p>
<pre tabindex="0"><code class="language-txt">GET example.com/checkout/pay&#10;GET example.com/checkout/{var1}&#10;</code></pre>
<p>Cloudflare uses <code>GET example.com/checkout/pay</code> because it is more specific.</p>
<p>For the same method, hostname pattern, and path pattern, Cloudflare generates the same operation UUID. This keeps operation identity stable when the same operation is found again.</p>
<h2 id="add-operations-manually">Add operations manually</h2>
<p>Add an operation manually when traffic you want to protect has not been discovered, or when you want to define the operation structure yourself.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13833.md")
</div>
<p>Manual creation only adds the operation to inventory. Select <strong>Learn profile</strong> separately to start profiling.</p>
<h2 id="use-variables-in-operation-patterns">Use variables in operation patterns</h2>
<p>When you add an operation manually, use variables to match similar traffic with one operation.</p>
<p>For path variables, enclose the variable in braces:</p>
<pre tabindex="0"><code class="language-txt">/api/users/{var1}/details&#10;</code></pre>
<p>For hostname variables, the variable must occupy a complete hostname label. Cloudflare supports patterns such as:</p>
<pre tabindex="0"><code class="language-txt">{hostVar1}.example.com&#10;foo.{hostVar1}.example.com&#10;{hostVar2}.{hostVar1}.example.com&#10;</code></pre>
<p>Do not combine a hostname variable with other characters in the same label. The following pattern is not supported:</p>
<pre tabindex="0"><code class="language-txt">foo-{hostVar1}.example.com&#10;</code></pre>
<h2 id="add-operations-from-schemas">Add operations from schemas</h2>
<p>If you already maintain OpenAPI schemas, you can continue uploading them to create operations.</p>
<p>Schema upload is also used by <a href="/api-shield/">API Shield</a> for schema validation. For more information, refer to <a href="/api-shield/security/schema-validation/">Schema Validation</a> and <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">schema learning</a>.</p>
<h2 id="refine-operations">Refine operations</h2>
<p>Refine operations when the current grouping does not match how the traffic should be grouped or protected.</p>
<p>For example, you may want separate operations for login and password reset traffic, even if both routes share part of the same path structure. You may also want to replace several narrow operations with one broader operation when they represent the same application behavior.</p>
<p>Review overlapping operations before making changes. Cloudflare matches a request to one operation. A broad operation can change how similar requests are grouped, while a narrow operation can isolate one flow from related traffic.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13834.md")
</div>
<p>Editing updates the operation inventory entry. It does not start profile learning.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="editing-this-operation-will-change-its-id">Editing this operation will change its ID</h3>
@markup("md", "content/.markup/bodies/13830.md")
</aside>
<h2 id="delete-operations">Delete operations</h2>
<p>You can delete operations one at a time or in bulk.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13835.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13829.md")
</aside>
<h2 id="use-the-cloudflare-api">Use the Cloudflare API</h2>
<p>You can interact with operations through the Cloudflare API. For more information, refer to <a href="/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/list/">operations API documentation</a>.</p>
