---
cp9:
  canonical: https://developers.cloudflare.com/logs/reference/pathing-status/
  description: Understand edge pathing status fields in logs.
  full_title: Pathing status · Cloudflare Logs docs
  head_html: <title>Pathing status · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand edge pathing status fields in logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/reference/pathing-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/reference/pathing-status/index.md"><meta property="og:title" content="Pathing status · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand edge pathing status fields in logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/reference/pathing-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/reference/pathing-status/#page","headline":"Pathing status \u00b7 Cloudflare Logs docs","description":"Understand edge pathing status fields in logs.","url":"https://developers.cloudflare.com/logs/reference/pathing-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/reference/pathing-status/
  schema: 1
---
<h2 id="understand-pathing">Understand pathing</h2>
<p>Cloudflare issues the following <strong>Edge Pathing Statuses</strong>:</p>
<ul>
<li><strong>EdgePathingSrc</strong> (pathing source): The stage that made the routing decision.</li>
<li><strong>EdgePathingOp</strong> (pathing operation): The specific action or operation taken.</li>
<li><strong>EdgePathingStatus</strong> (pathing status): Additional information complementing the <strong>EdgePathingOp</strong>.</li>
</ul>
<h3 id="edgepathingsrc">EdgePathingSrc</h3>
<p><strong>EdgePathingSrc</strong> refers to the system that last handled the request before an error occurred or the request was passed to the cache server. Typically, this will be the macro/reputation list. Possible pathing sources include:</p>
<ul>
<li><code>err</code></li>
<li><code>sslv</code> (SSL verification checker)</li>
<li><code>bic</code> (browser integrity check)</li>
<li><code>hot</code> (hotlink protection)</li>
<li><code>macro</code> (the reputation list)</li>
<li><code>skip</code> (Always Online or cdnjs resources)</li>
<li><code>user</code> (user firewall rule)</li>
</ul>
<p>For example:</p>
<pre tabindex="0"><code class="language-bash">jq -r .EdgePathingSrc logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 err&#10;5 user&#10;93 macro&#10;</code></pre>
<h3 id="edgepathingop">EdgePathingOp</h3>
<p><strong>EdgePathingOp</strong> indicates how the request was handled. <code>wl</code> is a request that passed all security checks in the cn. Other possible values are:</p>
<ul>
<li><code>errHost</code> (host header mismatch, DNS errors, etc.)</li>
<li><code>ban</code> (blocked by IP address, range, etc.)</li>
</ul>
<p>For example:</p>
<pre tabindex="0"><code class="language-bash">jq -r .EdgePathingOp logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 errHost&#10;97 wl&#10;</code></pre>
<h3 id="edgepathingstatus">EdgePathingStatus</h3>
<p><strong>EdgePathingStatus</strong> is the value <strong>EdgePathingSrc</strong> returns. With a pathing source of <code>macro</code>, <code>user</code>, or <code>err</code>, the pathing status indicates the list where the IP address was found. <code>nr</code> is the most common value and it means that the request was not flagged by a security check. Some values indicate the class of user; for example, <code>se</code> means search engine.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-bash">jq -r .EdgePathingStatus logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 dnsErr&#10;5 ip&#10;92 nr&#10;</code></pre>
<h2 id="how-does-pathing-map-to-threat-analytics">How does pathing map to Threat Analytics?</h2>
<p>Certain combinations of pathing have been labeled in the Cloudflare <strong>Threat Analytics</strong> feature (in the <strong>Analytics</strong> app in the Cloudflare dashboard). The mapping is as follows:</p>
<table>
<thead>
<tr>
<th>Pathing</th>
<th>Label</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>bic.ban.unknown</code></td>
<td>Bad browser</td>
</tr>
<tr>
<td><code>hot.ban.unknown</code></td>
<td>Blocked hotlink</td>
</tr>
<tr>
<td><code>hot.ban.ip</code></td>
<td></td>
</tr>
<tr>
<td><code>macro.ban.ip</code></td>
<td>Bad IP</td>
</tr>
<tr>
<td><code>user.ban.ctry</code></td>
<td>Country block</td>
</tr>
<tr>
<td><code>user.ban.ip</code></td>
<td>IP block (user)</td>
</tr>
<tr>
<td><code>user.ban.ipr16</code></td>
<td>IP range block (/16)</td>
</tr>
<tr>
<td><code>user.ban.ipr24</code></td>
<td>IP range block (/24)</td>
</tr>
</tbody>
</table>
<h2 id="understand-response-fields">Understand response fields</h2>
<p>The response status appears in three places in a request:</p>
<ul>
<li><strong>edgeResponse</strong></li>
<li><strong>cacheResponse</strong></li>
<li><strong>originResponse</strong></li>
</ul>
<p>In your logs, the edge is what first accepts a visitor's request. The cache then accepts the request and either forwards it to your origin or responds from the cache. It is possible to have a request that has only an <strong>edgeResponse</strong> or a request that has an <strong>edgeResponse</strong> and a <strong>cacheResponse</strong>, but no <strong>originResponse</strong>.</p>
<p>This is how you can see where a request terminates. Requests with only an <strong>edgeResponse</strong> likely hit a security check or processing error. Requests with an <strong>edgeResponse</strong> and a <strong>cacheResponse</strong> either were served from the cache or saw an error contacting your origin server. Requests that have an <strong>originResponse</strong> went all the way to your origin server and errors seen would have been served directly from there.</p>
<p>For example, the following query shows the status code and pathing information for all requests that terminated at the Cloudflare edge:</p>
<pre tabindex="0"><code class="language-bash">jq -r &#x27;select(.OriginResponseStatus == null) | select(.CacheResponseStatus == null) |&quot;\(.EdgeResponseStatus) / \(.EdgePathingSrc) / \(.EdgePathingStatus) / \(.EdgePathingOp)&quot;&#x27; logs.json | sort -n | uniq -c | sort -n&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 403 / macro / nr / wl&#10;1 409 / err / dnsErr / errHost&#10;</code></pre>
<p>The information stored is broken down based on the following categories:</p>
<h2 id="errors">Errors</h2>
<p>These occur for requests that did not pass any of the validation performed by the Cloudflare network. Example cases include:</p>
<ul>
<li>Whenever Cloudflare is unable to look up a domain or zone.</li>
<li>An attempt to improperly use the IP for an origin server.</li>
<li>Domain ownership is unclear (for example, the domain is not in Cloudflare).</li>
</ul>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>Status Code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cyclic</code></td>
<td>Cloudflare loop.</td>
<td><code>err_host</code></td>
<td><code>403</code></td>
</tr>
<tr>
<td><code>dns_err</code></td>
<td>Unable to resolve.</td>
<td><code>err_host</code></td>
<td><code>409</code></td>
</tr>
<tr>
<td><code>reserved_ip</code></td>
<td>DNS points to local or disallowed IP.</td>
<td><code>err_host</code></td>
<td><code>403</code></td>
</tr>
<tr>
<td><code>reserved_ip6</code></td>
<td>DNS points to local or disallowed IPv6 address.</td>
<td><code>err_host</code></td>
<td><code>403</code></td>
</tr>
<tr>
<td><code>bad_host</code></td>
<td>Bad or no Host header.</td>
<td><code>err_host</code></td>
<td><code>403</code></td>
</tr>
<tr>
<td><code>no_existing_host</code></td>
<td>Ownership lookup failed: host possibly not on Cloudflare.</td>
<td><code>err_host</code></td>
<td><code>409</code></td>
</tr>
</tbody>
</table>
<h2 id="user-based-actions">User-based actions</h2>
<p>These occur for actions triggered from users based on the configuration for a specific IP (or IP range).</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
<th>Status Code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Asnum</code><br/> <code>ip</code><br/> <code>ipr24</code><br/> <code>ipr16</code><br/> <code>ip6</code><br/> <code>ip6r64</code><br/> <code>ip6r48</code><br/> <code>ip6r32</code><br/> <code>ctry</code><br/></td>
<td>The request was blocked.</td>
<td><code>ban</code></td>
<td><code>user</code></td>
<td><code>403</code></td>
</tr>
<tr>
<td><code>Asnum</code><br/> <code>ip</code><br/> <code>ipr24</code><br/> <code>ipr16</code><br/> <code>ip6</code><br/> <code>ip6r64</code><br/> <code>ip6r48</code><br/> <code>ip6r32</code><br/> <code>ctry</code><br/></td>
<td><ul><li>The request was allowed.</li><li>WAF will not execute.</li></ul></td>
<td><code>wl</code></td>
<td><code>user</code></td>
<td>n/a</td>
</tr>
</tbody>
</table>
<h2 id="firewall-rules">Firewall Rules</h2>
<p>Cloudflare Firewall Rules (deprecated) triggers actions based on matching customer-defined rules.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>filter_based_firewall</code></td>
<td>The request was blocked.</td>
<td><code>ban</code></td>
</tr>
<tr>
<td><code>filter_based_firewall</code></td>
<td>The request was allowed.</td>
<td><code>wl</code></td>
</tr>
</tbody>
</table>
<h2 id="zone-lockdown">Zone Lockdown</h2>
<p><strong>Zone Lockdown</strong> blocks visitors to particular URIs where the visitor's IP is not allowlisted.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>zl</code></td>
<td>Lock down applied.</td>
<td><code>ban</code></td>
<td><code>user</code></td>
</tr>
</tbody>
</table>
<h2 id="firewall-user-agent-block">Firewall User-Agent Block</h2>
<p>Challenge (Interactive or Non-Interactive) or block visitors who use a browser for which the User-Agent name matches a specific string.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ua</code></td>
<td>Blocked User-Agent.</td>
<td><code>ban</code></td>
<td><code>user</code></td>
</tr>
</tbody>
</table>
<h2 id="browser-integrity-check">Browser Integrity Check</h2>
<p>Assert whether the source of the request is illegitimate or the request itself is malicious.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight: 400;">empty</span></td>
<td>Blocked request.</td>
<td><code>ban</code></td>
<td><code>bic</code></td>
</tr>
</tbody>
</table>
<h2 id="hot-linking">Hot Linking</h2>
<p>Prevent hot linking from other sites.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight: 400;">empty</span></td>
<td>Blocked request.</td>
<td><code>ban</code></td>
<td><code>hot</code></td>
</tr>
</tbody>
</table>
<h2 id="l7-to-l7-ddos-mitigation">L7-to-L7 DDoS mitigation</h2>
<p>Drop DDoS attacks through L7 mitigation.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight: 400;"><code>l7ddos</code></span></td>
<td>Blocked request.</td>
<td><code>ban</code></td>
<td><code>protect</code></td>
</tr>
</tbody>
</table>
<h2 id="ip-reputation-macro">IP Reputation (MACRO)</h2>
<p>The macro stage is comprised of many different paths. They are categorized by the reputation of the visitor IP.</p>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>nr</code></td>
<td>There is no reputation data for the IP and no action is being taken.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>wl</code></td>
<td>IP is explicitly allowlisted.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>scan</code></td>
<td>IP is explicitly allowlisted and categorized as a security scanner.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>mon</code></td>
<td>IP is explicitly allowlisted and categorized as a Monitoring Service.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>bak</code></td>
<td>IP is explicitly allowlisted and categorized as a Backup Service.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>mob</code></td>
<td>IP is explicitly allowlisted and categorized as Mobile Proxy Service.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>se</code></td>
<td>IP is explicitly allowlisted as it belongs to a search engine crawler and no action is taken.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>grey</code></td>
<td>IP is greylisted (suspected to be bad) but the request was either for a favicon or security is turned off and as such, it is allowlisted.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>bad_ok</code></td>
<td>The reputation score of the IP is bad but the request was either for a favicon or security is turned off and as such, it is allowlisted.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
<tr>
<td><code>unknown</code></td>
<td>The <code>pathing_status</code> is unknown and the request is being processed as normal.</td>
<td><code>wl</code></td>
<td><code>macro</code></td>
</tr>
</tbody>
</table>
<h2 id="rate-limiting">Rate Limiting</h2>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rate_limit</code></td>
<td>Dropped request.</td>
<td><code>ban</code></td>
<td><code>user</code></td>
</tr>
<tr>
<td><code>rate_limit</code></td>
<td>IP is explicitly allowlisted.</td>
<td><code>simulate</code></td>
<td><code>user</code></td>
</tr>
</tbody>
</table>
<h2 id="special-cases">Special cases</h2>
<table>
<thead>
<tr>
<th>EdgePathingStatus</th>
<th>Description</th>
<th>EdgePathingOp</th>
<th>EdgePathingSrc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ao_crawl</code></td>
<td>AO (Always Online) crawler request.</td>
<td><code>wl</code></td>
<td><code>skip</code></td>
</tr>
<tr>
<td><code>cdnjs</code></td>
<td>Request to a cdnjs resource.</td>
<td><code>wl</code></td>
<td><code>skip</code></td>
</tr>
<tr>
<td></td>
<td>Certain challenge forced by Cloudflare's special headers.</td>
<td></td>
<td><code>forced</code></td>
</tr>
</tbody>
</table>
