---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/
  description: Bulk Redirects work through a combination of URL redirects, a Bulk Redirect list, and a Bulk Redirect rule.
  full_title: Bulk Redirects concepts · Cloudflare Rules docs
  head_html: <title>Bulk Redirects concepts · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Bulk Redirects work through a combination of URL redirects, a Bulk Redirect list, and a Bulk Redirect rule."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/index.md"><meta property="og:title" content="Bulk Redirects concepts · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bulk Redirects work through a combination of URL redirects, a Bulk Redirect list, and a Bulk Redirect rule."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/#page","headline":"Bulk Redirects concepts \u00b7 Cloudflare Rules docs","description":"Bulk Redirects work through a combination of URL redirects, a Bulk Redirect list, and a Bulk Redirect rule.","url":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/bulk-redirects/concepts/
  schema: 1
---
<p>Bulk Redirects involve the following elements:</p>
<ul>
<li>
<p><strong>URL redirect</strong>: An entry with a source URL, a target URL, a status code, and redirect parameters. URL redirects are the individual items in Bulk Redirect Lists.</p>
</li>
<li>
<p><strong>Bulk Redirect List</strong>: A named collection containing one or more URL redirects. To activate all the URL redirects in a Bulk Redirect List, reference the list in a Bulk Redirect Rule. Different Bulk Redirect Rules can reference the same Bulk Redirect List.</p>
</li>
<li>
<p><strong>Bulk Redirect Rule</strong>: A rule powered by the <a href="/ruleset-engine/">Ruleset Engine</a>, which is the system Cloudflare uses to evaluate and execute rules. A Bulk Redirect Rule has an associated Bulk Redirect List.</p>
</li>
</ul>
<p>A Bulk Redirect Rule enables a Bulk Redirect List, which contains one or more URL redirects.</p>
<p><img src="/assets/upstream/images/rules/bulk-redirects/concepts-diagram.png" alt="Diagram outlining the hierarchy relationship between Bulk Redirect Rules, Bulk Redirect Lists, and URL redirects" /></p>
<p>The following example defines a Bulk Redirect List named <code>list_b</code> with two URL redirects:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13229.md")
</div>
<p>The following Bulk Redirect Rule, named <code>Rule 2</code>, enables the URL redirects in the <code>list_b</code> Bulk Redirect List:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/13230.md")
</div>
<h2 id="url-redirects">URL redirects</h2>
<p>A URL redirect allows you to configure a source URL, a target URL, a status code, and redirect parameters.</p>
<p>When specifying the source URL, use the available redirect parameters instead of wildcards, which are not supported. For example, the <strong>Include subdomains</strong> parameter allows you to configure a single URL redirect that applies both to subdomains (for example, <code>https://b.example.com</code> and <code>https://a.b.example.com</code>) and to the apex domain (the root domain with no subdomain – for example, <code>https://example.com</code>). Other parameters allow you to specify how the source URL’s path and query string are handled. For more information, refer to <a href="/rules/url-forwarding/bulk-redirects/how-it-works/">How Bulk Redirects work</a>.</p>
<p>URL redirects are the list items of Bulk Redirect Lists.</p>
<h2 id="bulk-redirect-lists">Bulk Redirect Lists</h2>
<p>Bulk Redirect Lists allow you to create distinct groups of URL redirects for different purposes. You can use a Bulk Redirect List in one or more Bulk Redirect Rules.</p>
<p>A Bulk Redirect List does not perform any redirects on its own — you must reference the list in a Bulk Redirect Rule to enable the redirects in the list.</p>
<p>A Bulk Redirect List cannot contain several URL redirects with the exact same source URL.</p>
<p>For details on the CSV format for importing items to a Bulk Redirect List, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/csv-file-format/">CSV file format for Bulk Redirects</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13228.md")
</aside>
<h2 id="bulk-redirect-rules">Bulk Redirect Rules</h2>
<p>Bulk Redirect Rules are rules powered by the Ruleset Engine that enable one or more URL redirects through a Bulk Redirect List.</p>
<p>When you configure a Bulk Redirect Rule, you associate a Bulk Redirect List to it, which enables all the URL redirects in that list. You can create a rule for each list, or have many Bulk Redirect Rules referencing the same Bulk Redirect List.</p>
<p>A Bulk Redirect Rule, like all rules powered by the Ruleset Engine, has an action (what happens when the rule triggers) and an <a href="#expression">expression</a> (the conditions that must be met). Besides these two properties, it also has a name, an optional description, an associated Bulk Redirect List, and a <a href="#key">key</a>.</p>
<h3 id="expression">Expression</h3>
<p>The rule expression, or filter expression, specifies the conditions that must be met for the rule to run. By default, all URL redirects of the specified list will apply.</p>
<p>The default expression of a Bulk Redirect Rule is the following:</p>
<pre tabindex="0"><code class="language-txt">http.request.full_uri in $&lt;LIST_NAME&gt;&#10;</code></pre>
<p>This expression means that the request URL, after some basic <span class="nb-glossary-tooltip" title="URL normalization">normalization</span> (if <a href="/rules/normalization/">URL normalization</a> is enabled), should match the source URL of a URL redirect in the list <code>&lt;LIST_NAME&gt;</code> for the redirect to be applied.</p>
<p>You can use an expression different from the default one to increase the specificity of URL redirect matches. For example, if you set the expression of a Bulk Redirect Rule to the following expression, there will only be a match for requests coming from the United Kingdom:</p>
<pre tabindex="0"><code class="language-txt">ip.src.country == &quot;GB&quot; and http.request.full_uri in $&lt;LIST_NAME&gt;&#10;</code></pre>
<p>For more information on the available fields, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/fields-functions/">Available fields and functions</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13227.md")
</aside>
<h3 id="key">Key</h3>
<p>The rule key specifies which request field Cloudflare uses to look up a matching URL redirect in the associated Bulk Redirect List.</p>
<p>When there is a match for the rule expression, Cloudflare compares the value of the rule key against the source URL of each URL redirect in the associated Bulk Redirect List, searching for a match.</p>
<p>The key should be either <code>http.request.full_uri</code> or <code>raw.http.request.full_uri</code>. Use <code>raw.http.request.full_uri</code> to compare the URI received by the web server, before normalization, with the source URLs in the Bulk Redirect List.</p>
<p>The URI field used in the key must be the same as the URI field used in the expression. Otherwise, you may have a match for the rule expression, but no match for any of the source URLs in the list. For example, if you set the key to <code>http.request.full_uri</code>, the field used in the rule expression must also be <code>http.request.full_uri</code>. Conversely, if you set the key to <code>raw.http.request.full_uri</code>, the field used in the expression must be <code>raw.http.request.full_uri</code>.</p>
