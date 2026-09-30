---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/
  description: Run lightweight JavaScript at the edge to modify requests and responses.
  full_title: Cloudflare Snippets · Cloudflare Rules docs
  head_html: <title>Cloudflare Snippets · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Run lightweight JavaScript at the edge to modify requests and responses."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/index.md"><meta property="og:title" content="Cloudflare Snippets · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run lightweight JavaScript at the edge to modify requests and responses."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Request modification,Response modification,Middleware"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/#page","headline":"Cloudflare Snippets \u00b7 Cloudflare Rules docs","description":"Run lightweight JavaScript at the edge to modify requests and responses.","url":"https://developers.cloudflare.com/rules/snippets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Request modification","Response modification","Middleware"]}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/
  schema: 1
---
<p>Cloudflare Snippets allow you to run short pieces of JavaScript code on Cloudflare's network to customize how requests and responses are handled for your website or application. With Snippets, you can modify HTTP response headers, implement <span class="nb-glossary-tooltip" title="JSON web token (JWT)">JWT</span> validation, perform complex <span class="nb-glossary-tooltip" title="redirect">redirects</span>, and more.</p>
<p>For code samples addressing common use cases, refer to the <a href="/rules/snippets/examples/">Examples</a> section.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12780.md")
</aside>
<h2 id="snippets-elements">Snippets elements</h2>
<p>To create and deploy a snippet, you need to define the following elements:</p>
<ul>
<li><strong>Snippet rule</strong>: A <a href="/ruleset-engine/rules-language/expressions/">filter expression</a> that determines which requests the Snippet will be applied to. Each snippet can only be associated with one snippet rule.</li>
<li><strong>Code snippet</strong>: JavaScript code that runs on the Cloudflare network when a request matches the associated snippet rule.</li>
</ul>
<p>For more information, refer to <a href="/rules/snippets/how-it-works/">How Snippets work</a> and <a href="/rules/snippets/create-dashboard/">Create a snippet in the dashboard</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12779.md")
</aside>
<h2 id="templates">Templates</h2>
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
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of snippets</td>
<td>0</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
<tr>
<td>Number of snippet subrequests</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>5</td>
</tr>
</tbody>
</table>
<p>Each <span class="nb-glossary-tooltip" title="Snippets subrequest">subrequest</span> in a redirect chain counts against the subrequest limit. This means that if a subrequest was redirected it would count as two subrequests. To avoid issues, ensure that you make a subrequest to the end location of the redirect chain.</p>
<p>Currently, <a href="/version-management/">Version Management</a> does not support Snippets.</p>
<h2 id="limits">Limits</h2>
<p>Cloudflare Snippets are designed for fast, lightweight logic that runs on the Cloudflare network. The following limits apply:</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>All plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum execution time</td>
<td>5 ms</td>
</tr>
<tr>
<td>Maximum memory</td>
<td>2 MB</td>
</tr>
<tr>
<td>Maximum total package size</td>
<td>32 KB</td>
</tr>
</tbody>
</table>
<div class="nb-card"><h3 class="nb-component-title" id="need-guidance-on-choosing-between-snippets-and-workers">Need guidance on choosing between Snippets and Workers?</h3>
@markup("md", "content/.markup/bodies/12784.md")
</div>
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
@markup("md", "content/.markup/bodies/12778.md")
</aside>
