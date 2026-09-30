---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/routing/routes/
  description: Map URL patterns to Cloudflare Workers to run your code on matching requests.
  full_title: Routes · Cloudflare Workers docs
  head_html: <title>Routes · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Map URL patterns to Cloudflare Workers to run your code on matching requests."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/routing/routes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/routing/routes/index.md"><meta property="og:title" content="Routes · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map URL patterns to Cloudflare Workers to run your code on matching requests."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/routing/routes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/routing/routes/#page","headline":"Routes \u00b7 Cloudflare Workers docs","description":"Map URL patterns to Cloudflare Workers to run your code on matching requests.","url":"https://developers.cloudflare.com/workers/configuration/routing/routes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/routing/routes/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Routes allow users to map a URL pattern to a Worker. When a request comes in to the Cloudflare network that matches the specified URL pattern, your Worker will execute on that route.</p>
<p>Routes are a set of rules that evaluate against a request's URL. Routes are recommended for you if you have a designated application server you always need to communicate with. Calling <code>fetch()</code> on the incoming <code>Request</code> object will trigger a subrequest to your application server, as defined in the <strong>DNS</strong> settings of your Cloudflare zone.</p>
<p>Routes add Workers functionality to your existing proxied hostnames, in front of your application server. These allow your Workers to act as a proxy and perform any necessary work before reaching out to an application server behind Cloudflare.</p>
<p><img src="/assets/upstream/images/workers/learning/routes-diagram.png" alt="Routes work with your applications defined in Cloudflare DNS" /></p>
<p>Routes can <code>fetch()</code> Custom Domains and take precedence if configured on the same hostname. If you would like to run a logging Worker in front of your application, for example, you can create a Custom Domain on your application Worker for <code>app.example.com</code>, and create a Route for your logging Worker at <code>app.example.com/*</code>. Calling <code>fetch()</code> will invoke the application Worker on your Custom Domain. Note that Routes cannot be the target of a same-zone <code>fetch()</code> call.</p>
<h2 id="set-up-a-route">Set up a route</h2>
<p>To add a route, you must have:</p>
<ol>
<li>An <a href="/dns/zone-setups/">active Cloudflare zone</a>.</li>
<li>A Worker to invoke.</li>
<li>A DNS record set up for the <a href="/dns/manage-dns-records/how-to/create-zone-apex/">domain</a> or <a href="/dns/manage-dns-records/how-to/create-subdomain/">subdomain</a> proxied by Cloudflare (also known as <a href="/dns/proxy-status/#benefits">orange-clouded</a>) you would like to route to.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16829.md")
</aside>
<p>If your Worker is not your application's origin, follow the instructions below to set up a route.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16828.md")
</aside>
<h3 id="set-up-a-route-in-the-dashboard">Set up a route in the dashboard</h3>
<p>Before you set up a route, make sure you have a DNS record set up for the <a href="/dns/manage-dns-records/how-to/create-zone-apex/">domain</a> or <a href="/dns/manage-dns-records/how-to/create-subdomain/">subdomain</a> you would like to route to.</p>
<p>To set up a route in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16830.md")
</div>
<h3 id="set-up-a-route-in-the-wrangler-configuration-file">Set up a route in the Wrangler configuration file</h3>
<p>Before you set up a route, make sure you have a DNS record set up for the <a href="/dns/manage-dns-records/how-to/create-zone-apex/">domain</a> or <a href="/dns/manage-dns-records/how-to/create-subdomain/">subdomain</a> you would like to route to.</p>
<p>To configure a route using your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, refer to the following example.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16831.md")
</div>
<p>Add the <code>zone_name</code> or <code>zone_id</code> option after each route. The <code>zone_name</code> and <code>zone_id</code> options are interchangeable. If using <code>zone_id</code>, find your zone ID by:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16832.md")
</div>
<p>To add multiple routes:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16833.md")
</div>
<h2 id="matching-behavior">Matching behavior</h2>
<p>Route patterns look like this:</p>
<pre tabindex="0"><code class="language-txt">https://*.example.com/images/*&#10;</code></pre>
<p>This pattern would match all HTTPS requests destined for a subhost of
example.com and whose paths are prefixed by <code>/images/</code>.</p>
<p>A pattern to match all requests looks like this:</p>
<pre tabindex="0"><code class="language-txt">&#42;example.com/*&#10;</code></pre>
<p>While they look similar to a <a href="https://en.wikipedia.org/wiki/Regular_expression">regex</a> pattern, route patterns follow specific rules:</p>
<ul>
<li>
<p>The only supported operator is the wildcard (<code>*</code>), which matches zero or more of any character.</p>
</li>
<li>
<p>Route patterns may not contain infix wildcards or query parameters. For example, neither <code>example.com/*.jpg</code> nor <code>example.com/?foo=*</code> are valid route patterns.</p>
</li>
<li>
<p>When more than one route pattern could match a request URL, the most specific route pattern wins. For example, the pattern <code>www.example.com/*</code> would take precedence over <code>*.example.com/*</code> when matching a request for <code>https://www.example.com/</code>. The pattern <code>example.com/hello/*</code> would take precedence over <code>example.com/*</code> when matching a request for <code>example.com/hello/world</code>.</p>
</li>
<li>
<p>Route pattern matching considers the entire request URL, including the query parameter string. Since route patterns may not contain query parameters, the only way to have a route pattern match URLs with query parameters is to terminate it with a wildcard, <code>*</code>.</p>
</li>
<li>
<p>The path component of route patterns is case sensitive, for example, <code>example.com/Images/*</code> and <code>example.com/images/*</code> are two distinct routes.</p>
</li>
<li>
<p>For routes created before October 15th, 2023, the host component of route patterns is case sensitive, for example, <code>example.com/*</code> and <code>Example.com/*</code> are two distinct routes.</p>
</li>
<li>
<p>For routes created on or after October 15th, 2023, the host component of route patterns is not case sensitive, for example, <code>example.com/*</code> and <code>Example.com/*</code> are equivalent routes.</p>
</li>
</ul>
<p>A route can be specified without being associated with a Worker. This will act to negate any less specific patterns. For example, consider this pair of route patterns, one with a Workers script and one without:</p>
<pre tabindex="0"><code class="language-txt">&#42;example.com/images/cat.png -&gt; &lt;no script&gt;&#10;&#42;example.com/images/*       -&gt; worker-script&#10;</code></pre>
<p>In this example, all requests destined for example.com and whose paths are prefixed by <code>/images/</code> would be routed to <code>worker-script</code>, <em>except</em> for <code>/images/cat.png</code>, which would bypass Workers completely. Requests with a path of <code>/images/cat.png?foo=bar</code> would be routed to <code>worker-script</code>, due to the presence of the query string.</p>
<h2 id="validity">Validity</h2>
<p>The following set of rules govern route pattern validity.</p>
<h4 id="route-patterns-must-include-your-zone">Route patterns must include your zone</h4>
<p>If your zone is <code>example.com</code>, then the simplest possible route pattern you can have is <code>example.com</code>, which would match <code>http://example.com/</code> and <code>https://example.com/</code>, and nothing else. As with a URL, there is an implied path of <code>/</code> if you do not specify one.</p>
<h4 id="route-patterns-may-not-contain-any-query-parameters">Route patterns may not contain any query parameters</h4>
<p>For example, <code>https://example.com/?anything</code> is not a valid route pattern.</p>
<h4 id="route-patterns-may-optionally-begin-with-http-or-https">Route patterns may optionally begin with <code>http://</code> or <code>https://</code></h4>
<p>If you omit a scheme in your route pattern, it will match both <code>http://</code> and <code>https://</code> URLs. If you include <code>http://</code> or <code>https://</code>, it will only match HTTP or HTTPS requests, respectively.</p>
<ul>
<li>
<p><code>https://*.example.com/</code> matches <code>https://www.example.com/</code> but not <code>http://www.example.com/</code>.</p>
</li>
<li>
<p><code>*.example.com/</code> matches both <code>https://www.example.com/</code> and <code>http://www.example.com/</code>.</p>
</li>
</ul>
<h4 id="hostnames-may-optionally-begin-with">Hostnames may optionally begin with <code>*</code></h4>
<p>If a route pattern hostname begins with <code>*</code>, then it matches the host and all subhosts. If a route pattern hostname begins with <code>*.</code>, then it only matches all subhosts.</p>
<ul>
<li>
<p><code>*example.com/</code> matches <code>https://example.com/</code> and <code>https://www.example.com/</code>.</p>
</li>
<li>
<p><code>*.example.com/</code> matches <code>https://www.example.com/</code> but not <code>https://example.com/</code>.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16827.md")
</aside>
<p>The following examples illustrate the difference between <code>*example.com/*</code> and <code>*.example.com/*</code>:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th><code>*example.com/*</code></th>
<th><code>*.example.com/*</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/</code></td>
<td>Matches</td>
<td>Does not match</td>
</tr>
<tr>
<td><code>https://www.example.com/path</code></td>
<td>Matches</td>
<td>Matches</td>
</tr>
<tr>
<td><code>https://myexample.com/</code></td>
<td>Matches</td>
<td>Does not match</td>
</tr>
<tr>
<td><code>https://not-example.com/</code></td>
<td>Does not match</td>
<td>Does not match</td>
</tr>
</tbody>
</table>
<h4 id="paths-may-optionally-end-with">Paths may optionally end with <code>*</code></h4>
<p>If a route pattern path ends with <code>*</code>, then it matches all suffixes of that path.</p>
<ul>
<li><code>https://example.com/path*</code> matches <code>https://example.com/path</code> and <code>https://example.com/path2</code> and <code>https://example.com/path/readme.txt</code></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16826.md")
</aside>
<h4 id="domains-and-subdomains-must-have-a-dns-record">Domains and subdomains must have a DNS Record</h4>
<p>All domains and subdomains must have a <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS record</a> to be proxied on Cloudflare and used to invoke a Worker. For example, if you want to put a Worker on <code>myname.example.com</code>, and you have added <code>example.com</code> to Cloudflare but have not added any DNS records for <code>myname.example.com</code>, any request to <code>myname.example.com</code> will result in the error <code>ERR_NAME_NOT_RESOLVED</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16825.md")
</aside>
