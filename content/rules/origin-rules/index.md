---
cp9:
  canonical: https://developers.cloudflare.com/rules/origin-rules/
  description: Override the origin server, host header, SNI, and DNS resolution for matching requests.
  full_title: Origin Rules · Cloudflare Rules docs
  head_html: <title>Origin Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Override the origin server, host header, SNI, and DNS resolution for matching requests."><link rel="canonical" href="https://developers.cloudflare.com/rules/origin-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/origin-rules/index.md"><meta property="og:title" content="Origin Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Override the origin server, host header, SNI, and DNS resolution for matching requests."><meta property="og:url" content="https://developers.cloudflare.com/rules/origin-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/origin-rules/#page","headline":"Origin Rules \u00b7 Cloudflare Rules docs","description":"Override the origin server, host header, SNI, and DNS resolution for matching requests.","url":"https://developers.cloudflare.com/rules/origin-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/origin-rules/
  schema: 1
---
<p>Origin Rules allow you to change the origin server that Cloudflare sends a request to, or modify how the request reaches that server. This is useful when you need to route specific requests to a different backend, such as a third-party service or a server on a non-standard port. You can perform the following overrides:</p>
<ul>
<li><a href="/rules/origin-rules/features/#host-header">Host header</a>: Overrides the <code>Host</code> header of incoming requests.</li>
<li><a href="/rules/origin-rules/features/#server-name-indication-sni">Server Name Indication (SNI)</a>: Overrides the Server Name Indication (SNI) value of incoming requests.</li>
<li><a href="/rules/origin-rules/features/#dns-record">DNS record</a>: Overrides the resolved hostname of incoming requests, sending the request to a different origin server.</li>
<li><a href="/rules/origin-rules/features/#destination-port">Destination port</a>: Overrides the resolved destination port of incoming requests.</li>
</ul>
<p>Each origin rule includes a <a href="/ruleset-engine/rules-language/expressions/">filter expression</a> that defines which requests the overrides apply to (for example, matching on hostname, path, or other request properties).</p>
<p>For more complex and customized modifications, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<br />
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12957.md")
</aside>
<h2 id="rules-templates">Rules templates</h2>
<p>Cloudflare provides you with rules templates for common use cases.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Templates</strong>, and then select one of the available templates.</li>
</ol>
<p>You can also refer to the <a href="/rules/examples/">Examples gallery</a> in the developer docs.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
<tr>
<td>Override Host header</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Override SNI</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Override DNS records</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Override destination port</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="execution-order">Execution order</h2>
<p>The execution order of Rules features is the following:</p>
<ul>
<li><a href="/rules/url-forwarding/single-redirects/">Single Redirects</a></li>
<li><a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a></li>
<li><a href="/rules/configuration-rules/">Configuration Rules</a></li>
<li><a href="/rules/origin-rules/">Origin Rules</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a></li>
<li><a href="/rules/transform/managed-transforms/">Managed Transforms</a></li>
<li><a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a></li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a></li>
<li><a href="/rules/snippets/">Snippets</a></li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a></li>
</ul>
<p>The different types of rules listed above will take precedence over <a href="/rules/page-rules/">Page Rules</a>. This means that Page Rules will be overridden if there is a match for both Page Rules and the Rules products listed above.</p>
<p>Generally speaking, for <a href="/ruleset-engine/rules-language/actions/">non-terminating actions</a> the last change made by rules in the same <a href="/ruleset-engine/about/phases/">phase</a> will win (later rules can overwrite changes done by previous rules). However, for terminating actions (<em>Block</em>, <em>Redirect</em>, or one of the challenge actions), rule evaluation will stop and the action will be executed immediately.</p>
<p>For example, if multiple rules with the <em>Redirect</em> action match, Cloudflare will always use the URL redirect of the first rule that matches. Also, if you configure URL redirects using different Cloudflare products (Single Redirects and Bulk Redirects), the product executed first will apply, if there is a rule match (in this case, Single Redirects).</p>
<p>Refer to the <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for the product execution order.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12956.md")
</aside>
<h2 id="important-remarks">Important remarks</h2>
<p>If you override the hostname with an origin rule (via <code>Host</code> header override or DNS record override) and add a header override to your load balancer configuration, the origin rule will take precedence over the load balancer configuration.</p>
<p>Like <a href="/rules/page-rules/">Page Rules</a>, an origin rule performing a <code>Host</code> header override will update the SNI value of the original request to the same value of the <code>Host</code> header. To set an SNI value different from the <code>Host</code> header override, add an SNI override in the same origin rule or create a separate origin rule for this purpose.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting origin rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
