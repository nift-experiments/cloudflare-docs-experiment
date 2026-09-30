---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/request-header-modification/
  description: Learn how to modify HTTP request headers with Cloudflare's rules.
  full_title: Request Header Transform Rules · Cloudflare Rules docs
  head_html: <title>Request Header Transform Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to modify HTTP request headers with Cloudflare&#x27;s rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/request-header-modification/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/request-header-modification/index.md"><meta property="og:title" content="Request Header Transform Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to modify HTTP request headers with Cloudflare&#x27;s rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/request-header-modification/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Headers,Request modification"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/request-header-modification/#page","headline":"Request Header Transform Rules \u00b7 Cloudflare Rules docs","description":"Learn how to modify HTTP request headers with Cloudflare's rules.","url":"https://developers.cloudflare.com/rules/transform/request-header-modification/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","Request modification"]}</script>
  markdown: true
  noindex: false
  route: /rules/transform/request-header-modification/
  schema: 1
---
<p>Use Request Header Transform Rules to manipulate the headers of HTTP requests sent to your origin server (the server where your website or application is hosted).</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Header modifications diagram&#10;accDescr: Header transform rules can change the headers sent to your origin server (request header modifications) or sent your website visitors (response header modifications).&#10;&#10;A[Visitor]&#10;B((Cloudflare))&#10;C[(Origin server)]&#10;&#10;A -.-&gt; B == &quot;Includes request&lt;br&gt; header modifications&quot; ==&gt; C&#10;C -.-&gt; B -. &quot;Includes response&lt;br&gt; header modifications&quot; .-&gt; A&#10;&#10;style A stroke-width: 2px&#10;style B stroke: orange,fill: orange,color: black&#10;linkStyle 0,2,3 stroke-width: 1px&#10;linkStyle 1 stroke-width: 3px&#10;</code></pre>
<br />
<p>To modify HTTP headers in the <strong>response</strong> sent to website visitors, refer to <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a>.</p>
<p>Through Request Header Transform Rules you can:</p>
<ul>
<li>Set the value of an HTTP request header to a literal string value, overwriting its previous value or adding a new header to the request.</li>
<li>Set the value of an HTTP request header according to an expression (a formula that computes a value based on request properties), overwriting its previous value or adding a new header to the request.</li>
<li>Remove an HTTP header from the request.</li>
</ul>
<p>You can create a request header transform rule <a href="/rules/transform/request-header-modification/create-dashboard/">in the dashboard</a>, <a href="/rules/transform/request-header-modification/create-api/">via API</a>, or <a href="/terraform/additional-configurations/transform-rules/#create-a-request-header-transform-rule">using Terraform</a>.</p>
<p>For more complex request header modifications, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>You cannot modify or remove HTTP request headers whose name starts with <code>x-cf-</code> or <code>cf-</code> except for the <code>cf-connecting-ip</code> HTTP request header, which you can remove.</p>
</li>
<li>
<p>Due to protocol compliance reasons, modifying or removing request headers with <a href="https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name">forbidden header names</a> (such as <code>Accept-Encoding</code>) is generally not allowed in Request Header Transform Rules.</p>
</li>
<li>
<p>You cannot modify the value of any header commonly used to identify the website visitor's IP address or initial protocol, such as <code>x-forwarded-for</code>, <code>true-client-ip</code>, <code>x-real-ip</code>, or <code>x-forwarded-proto</code>. If your origin needs a custom value in a header like <code>x-real-ip</code> on requests reaching your origin server, use <a href="/rules/snippets/">Cloudflare Snippets</a> or <a href="/workers/">Cloudflare Workers</a> and set the header on a <code>fetch()</code> subrequest. The value must be a syntactically valid IP address. This workaround does not work for cross-zone subrequests, where Cloudflare unconditionally replaces the value with an internal Cloudflare address to prevent IP spoofing.</p>
</li>
<li>
<p>Although you can remove the <code>x-forwarded-for</code> header in a Request Header Transform Rule, Cloudflare's backend proxy re-adds it (with the visitor's IP address) before the request reaches your origin server, because the proxy runs after all rule phases. The same applies to <a href="/rules/transform/managed-transforms/">Managed Transforms</a>. However, if the request is handled by Cloudflare Workers — which <a href="/workers/reference/how-the-cache-works/">run before the cache</a> — the <code>x-forwarded-for</code> request header will be absent because the proxy has not yet re-added it.</p>
</li>
<li>
<p>You cannot set or modify the value of <code>cookie</code> HTTP request headers, but you can remove these headers. Configuring a rule that removes the <code>cookie</code> HTTP request header will remove all <code>cookie</code> headers in matching requests.</p>
</li>
<li>
<p>If you modify the value of an existing HTTP request header using an expression that evaluates to an empty string (<code>&quot;&quot;</code>) or an undefined value, the HTTP request header is <strong>removed</strong>.</p>
</li>
<li>
<p>The HTTP request header removal operation will remove all request headers with the provided name.</p>
</li>
<li>
<p>Currently, there is a limited number of HTTP request headers that you cannot modify. Cloudflare may remove restrictions for some of these HTTP request headers when presented with valid use cases. <a href="https://community.cloudflare.com">Create a post in the community</a> for consideration.</p>
</li>
<li>
<p>To use <a href="/api-shield/security/jwt-validation/transform-rules/">claims inside a JSON Web Token (JWT)</a>, you must first set up a token validation configuration in API Shield.</p>
</li>
<li>
<p>Request header transform rules run in order, and later rules can overwrite changes done by previous rules.</p>
</li>
<li>
<p>The values of request and response fields are immutable within each <a href="/ruleset-engine/about/phases/">phase</a>, such as the <code>http_request_late_transform</code> phase where request header transform rules are defined. This means that later request header transform rules will still use the original field values when evaluating their filter expressions, not the values changed by previous rules. Refer to <a href="/ruleset-engine/about/rules/#field-values-during-rule-evaluation">Field values during rule evaluation</a> for more information.</p>
</li>
</ul>
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
@markup("md", "content/.markup/bodies/13138.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Request Header Transform Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
