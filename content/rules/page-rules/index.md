---
cp9:
  canonical: https://developers.cloudflare.com/rules/page-rules/
  description: Trigger actions based on URL patterns with Page Rules (deprecated).
  full_title: Page Rules · Cloudflare Rules docs
  head_html: <title>Page Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Trigger actions based on URL patterns with Page Rules (deprecated)."><link rel="canonical" href="https://developers.cloudflare.com/rules/page-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/page-rules/index.md"><meta property="og:title" content="Page Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trigger actions based on URL patterns with Page Rules (deprecated)."><meta property="og:url" content="https://developers.cloudflare.com/rules/page-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/page-rules/#page","headline":"Page Rules \u00b7 Cloudflare Rules docs","description":"Trigger actions based on URL patterns with Page Rules (deprecated).","url":"https://developers.cloudflare.com/rules/page-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/page-rules/
  schema: 1
---
<p>Page Rules trigger one or more actions whenever a certain URL pattern is matched. Page Rules are available in <strong>Rules</strong> &gt; <strong>Page Rules</strong>.</p>
<h2 id="availability">Availability</h2>
<p>The default number of allowed page rules depends on the domain plan as shown below.</p>
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
<td>3</td>
<td>20</td>
<td>50</td>
<td>125</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="before-getting-started">Before getting started</h2>
<p>It is important to understand a few Page Rules behaviors.</p>
<h3 id="page-rules-require-proxied-dns-records">Page Rules require proxied DNS records</h3>
<p>Page Rules require a <a href="/dns/proxy-status/">proxied</a> DNS record for your page rule to work. Page Rules will not apply to hostnames that do not exist in DNS or are not being directed to Cloudflare.</p>
<p>If you are creating a Page Rule for a hostname that does not have a real origin server, you still need a proxied DNS record. You can use a reserved IP address or domain as a placeholder. The record only needs to exist so that Cloudflare proxies traffic for that hostname. Create one of the following:</p>
<pre tabindex="0"><code>www.example.com  A      192.0.2.1&#10;www.example.com  AAAA   2001:DB8::1&#10;www.example.com  CNAME  domain.example&#10;</code></pre>
<p>Cloudflare recommends using only reserved IP addresses or domain names for placeholder records to avoid accidentally routing traffic to infrastructure you do not own.</p>
<p>For more information on reserved IP addresses or top level domains, please refer to these RFCs:</p>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc5737">RFC 5737</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc3849">RFC 3849</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2606">RFC 2606</a></li>
</ul>
<h3 id="priority-order-matters">Priority order matters</h3>
<p>Only the highest priority matching page rule takes effect on a request.</p>
<p>Page Rules are prioritized in descending order in the Cloudflare dashboard, with the highest priority rule at the top. For this reason, Cloudflare recommends ordering your rules from most specific to least specific.</p>
<p>A page rule matches a URL pattern based on the following format (comprised of five segments):</p>
<pre tabindex="0"><code class="language-txt">&lt;SCHEME&gt;://&lt;HOSTNAME&gt;:&lt;PORT&gt;/&lt;PATH&gt;?&lt;QUERY_STRING&gt;&#10;</code></pre>
<p>An example URL with all the segments looks like the following:</p>
<pre tabindex="0"><code class="language-txt">https://www.example.com:443/image.png?parameter1=value1&#10;</code></pre>
<p>The <code>&lt;SCHEME&gt;</code> and <code>&lt;PORT&gt;</code> segments are optional. If omitted, <code>&lt;SCHEME&gt;</code> matches both <code>http://</code> and <code>https://</code> protocols. If no <code>&lt;PORT&gt;</code> is specified, the rule will match all ports.</p>
<h3 id="disabled-page-rules">Disabled page rules</h3>
<p>When a page rule is disabled, actions will not trigger, but the rule will:</p>
<ul>
<li>Still appear in the Cloudflare dashboard.</li>
<li>Be editable.</li>
<li>Count against the number of rules allowed for your domain.</li>
</ul>
