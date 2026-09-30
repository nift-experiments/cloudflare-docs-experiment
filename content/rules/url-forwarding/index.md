---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/
  description: Redirect visitors to different URLs with Single Redirects and Bulk Redirects.
  full_title: Redirects · Cloudflare Rules docs
  head_html: <title>Redirects · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Redirect visitors to different URLs with Single Redirects and Bulk Redirects."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/index.md"><meta property="og:title" content="Redirects · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Redirect visitors to different URLs with Single Redirects and Bulk Redirects."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/#page","headline":"Redirects \u00b7 Cloudflare Rules docs","description":"Redirect visitors to different URLs with Single Redirects and Bulk Redirects.","url":"https://developers.cloudflare.com/rules/url-forwarding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/
  schema: 1
---
<p>URL forwarding, also known as URL redirection, navigates the user from a source URL to a target URL with a specific HTTP status code.</p>
<p>Use the following Cloudflare products to perform URL redirects, according to your use case:</p>
<ul>
<li>
<p><a href="/rules/url-forwarding/single-redirects/"><strong>Single Redirects</strong></a>: Allow you to create static or dynamic redirects at the zone level (a single domain or subdomain). A <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard-based</a> interface allows you to define source and target URL patterns without complex functions or regular expressions, efficiently covering thousands of URLs with a single rule.</p>
</li>
<li>
<p><a href="/rules/url-forwarding/bulk-redirects/"><strong>Bulk Redirects</strong></a>: Allow you to define a large number of redirects at the account level, which can apply across domains in your account. These URL redirects are essentially static — they do not support string replacement operations or regular expressions. However, you can configure parameters that affect how source URLs are matched and how the redirect is performed.</p>
</li>
<li>
<p><a href="/rules/snippets/"><strong>Snippets</strong></a>: Use short pieces of JavaScript code for a more flexible way to define complex redirect functionality. Consider a few <a href="/rules/snippets/examples/?operation=Redirect">examples</a> to get started.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12771.md")
</aside>
<h2 id="redirect-rules-templates">Redirect Rules templates</h2>
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
<p>Single Redirects and Bulk Redirects are available on all Cloudflare plans. The exact quotas and features depend on your plan.</p>
<h3 id="bulk-redirects">Bulk redirects</h3>
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
<td>Bulk Redirect Rules</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>50</td>
</tr>
<tr>
<td>Bulk Redirect Lists</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>25</td>
</tr>
<tr>
<td>URL redirects across lists</td>
<td>10,000</td>
<td>25,000</td>
<td>50,000</td>
<td>1,000,000</td>
</tr>
</tbody>
</table>
<p>For <em>URL redirects across lists</em>, this table provides the default quota for the Enterprise plan. Bulk Redirects supports several million URL redirects — to get more redirects, contact your account team.</p>
<p>Bulk Redirects features and quotas are per account and they depend on the highest Cloudflare plan on your account.</p>
<h3 id="single-redirects">Single Redirects</h3>
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
<td>Wildcard support</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Regex support</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Single Redirects features and quotas are per zone and depend on the zone plan.</p>
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
@markup("md", "content/.markup/bodies/12770.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting URL redirects, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
