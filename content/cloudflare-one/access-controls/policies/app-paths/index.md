---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/
  description: How Application paths works in Access.
  full_title: Application paths · Cloudflare One docs
  head_html: <title>Application paths · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Application paths works in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/index.md"><meta property="og:title" content="Application paths · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Application paths works in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/#page","headline":"Application paths \u00b7 Cloudflare One docs","description":"How Application paths works in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/app-paths/
  schema: 1
---
<p>Application paths define the URLs protected by an Access policy. When adding a self-hosted application to Access, you can choose to protect the entire website by entering its apex domain, or alternatively, protect specific subdomains and paths.</p>
<h2 id="policy-inheritance">Policy inheritance</h2>
<p>Cloudflare Zero Trust allows you to create unique rules for parts of an application that share a root path. Imagine an example application is deployed at <code>dashboard.com/eng</code> that anyone on the engineering team should be able to access. However, a tool deployed at <code>dashboard.com/eng/exec</code> should only be accessed by the executive team.</p>
<p>When multiple rules are set for a common root path, the more specific rule takes precedence. For example, when setting rules for <code>dashboard.com/eng</code> and <code>dashboard.com/eng/exec</code> separately, the more specific rule for <code>dashboard.com/eng/exec</code> takes precedence, and no rule is inherited from <code>dashboard.com/eng</code>. If no separate, specific rule is set for <code>dashboard.com/eng/exec</code>, it will inherit any rules set for <code>dashboard.com/eng</code>.</p>
<h2 id="wildcards">Wildcards</h2>
<p>When you create an application for a specific subdomain or path, you can use asterisks (<code>*</code>) as wildcards. Wildcards allow you to extend the application you are creating to multiple subdomains or paths in a given apex domain.</p>
<h3 id="examples">Examples</h3>
<h4 id="match-all-subdomains-of-an-apex-domain">Match all subdomains of an apex domain</h4>
<p>A wildcard in the <strong>Subdomain</strong> field only matches that specific subdomain level. It does not cover the apex domain or multiple levels of the subdomain. If you want to cover multiple subdomain levels, you can use multiple wildcards.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
<th>Does not cover</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*.example.com</code></td>
<td><code>alpha.example.com</code> <br/> <code>beta.example.com</code></td>
<td><code>example.com</code> <br/> <code>foo.bar.example.com</code></td>
</tr>
</tbody>
</table>
<h4 id="match-all-paths-of-an-apex-domain">Match all paths of an apex domain</h4>
<p>To protect an apex domain and all of the paths under it, leave the <strong>Path</strong> field empty. Alternatively, use a wildcard in the <strong>Path</strong> field.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
<th>Does not cover</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code> <br/> or <code>example.com/*</code></td>
<td><code>example.com</code> <br/> <code>example.com/alpha</code> <br/> <code>example.com/beta</code></td>
<td><code>alpha.example.com</code></td>
</tr>
</tbody>
</table>
<h4 id="match-multi-level-subdomains">Match multi-level subdomains</h4>
<p>Using a wildcard in the <strong>Subdomain</strong> field does not cover the parent subdomain nor the apex domain.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
<th>Does not cover</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*.test.example.com</code></td>
<td><code>alpha.test.example.com</code> <br/> <code>beta.test.example.com</code></td>
<td><code>test.example.com</code>  <br/> <code>example.com</code></td>
</tr>
</tbody>
</table>
<h4 id="partially-match-subdomains">Partially match subdomains</h4>
<p>Using a wildcard at the beginning or end of the <strong>Subdomain</strong> field does not cover multiple levels of the subdomain.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
<th>Does not cover</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*test.example.com</code></td>
<td><code>test.example.com</code> <br/> <code>alphatest.example.com</code></td>
<td><code>beta.test.example.com</code></td>
</tr>
</tbody>
</table>
<h4 id="match-multi-level-paths">Match multi-level paths</h4>
<p>Using a wildcard in the <strong>Path</strong> field does not cover the parent path nor the apex domain.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
<th>Does not cover</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com/alpha/*</code></td>
<td><code>example.com/alpha/one</code> <br/> <code>example.com/alpha/two</code></td>
<td><code>example.com/alpha</code> <br/> <code>example.com</code></td>
</tr>
</tbody>
</table>
<h4 id="partially-match-paths">Partially match paths</h4>
<p>Using a wildcard in the middle of the <strong>Path</strong> field covers multiple segments of the URL.</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Covers</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com/foo*/bar</code></td>
<td><code>example.com/foo/bar</code><br/> <code>example.com/food/bar</code> <br/> <code>example.com/food/stuff/bar</code></td>
</tr>
</tbody>
</table>
<h3 id="limitations">Limitations</h3>
<ul>
<li>At most one wildcard in between each dot in the <strong>Subdomain</strong>. For example, <code>foo*bar*baz.example.com</code> is not allowed.</li>
<li>At most one wildcard in between each slash in the <strong>Path</strong>. For example, <code>example.com/foo*bar*baz</code> is not allowed.</li>
</ul>
<h2 id="subdomain-setups">Subdomain setups</h2>
<p><a href="/dns/zone-setups/subdomain-setup/">Subdomain setups</a> allow you to manage a child domain separately from its parent domain. In Access application paths, your configured child domains will appear in the <strong>Domain</strong> dropdown menu. If you <a href="/dns/zone-setups/subdomain-setup/setup/">split out a subdomain</a> which already has an Access application, you will need to re-save the Access application to associate it with the new child domain.</p>
<h2 id="unsupported-urls">Unsupported URLs</h2>
<h3 id="port-numbers">Port numbers</h3>
<p>Port numbers are not supported in Access application paths. If a request includes a port number in the URL, Access will strip the port number and redirect the request to the default HTTP/HTTPS port.</p>
<h3 id="query-strings">Query strings</h3>
<p>Query strings (such as<code>?foo=bar</code>) are not supported in Access application paths.</p>
<h3 id="anchor-links">Anchor links</h3>
<p>Since anchor links are processed by the browser and not the server, Access applications do not support <code>#</code> characters in the URL. For example, requests to <code>dashboard.com/#settings</code> will redirect to <code>dashboard.com</code>.</p>
