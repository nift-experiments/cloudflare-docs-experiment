---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/zone-lockdown/
  description: Restrict access to specific URLs by allowlisted IP addresses.
  full_title: Zone Lockdown · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Zone Lockdown · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict access to specific URLs by allowlisted IP addresses."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/zone-lockdown/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/zone-lockdown/index.md"><meta property="og:title" content="Zone Lockdown · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict access to specific URLs by allowlisted IP addresses."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/zone-lockdown/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/zone-lockdown/#page","headline":"Zone Lockdown \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Restrict access to specific URLs by allowlisted IP addresses.","url":"https://developers.cloudflare.com/waf/tools/zone-lockdown/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/zone-lockdown/
  schema: 1
---
<p>Zone Lockdown specifies a list of one or more IP addresses, CIDR ranges, or networks that are the only IPs allowed to access a domain, subdomain, or URL. You can configure multiple destinations, including IPv4/IPv6 addresses, in a single zone lockdown rule.</p>
<p>All IP addresses not specified in the zone lockdown rule will not have access to the specified resources. Requests from those IP addresses will receive an <code>Access Denied</code> response.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15322.md")
</aside>
<h2 id="availability">Availability</h2>
<p>Cloudflare Zone Lockdown is available on paid plans. The <strong>Zone lockdown rules</strong> option appears only if you have configured at least one zone lockdown rule.</p>
<p>The number of available zone lockdown rules depends on your Cloudflare plan.</p>
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
<td>Number of rules</td>
<td>0</td>
<td>3</td>
<td>10</td>
<td>200</td>
</tr>
</tbody>
</table>
<h2 id="create-a-zone-lockdown-rule">Create a zone lockdown rule</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15327.md")
</div></div>
<h3 id="example-rule">Example rule</h3>
<p>The following example rule will only allow visitors connecting from a company’s headquarters or branch offices to access the staging environment and the wiki:</p>
<ul>
<li>Name:</li>
</ul>
<pre tabindex="0"><code class="language-txt">Block all traffic to staging and wiki unless it comes from HQ or branch offices&#10;</code></pre>
<ul>
<li>URLs:</li>
</ul>
<pre tabindex="0"><code class="language-txt">staging.example.com/*&#10;example.com/wiki/*&#10;</code></pre>
<ul>
<li>IP Range:</li>
</ul>
<pre tabindex="0"><code class="language-txt">192.0.2.0/24&#10;2001:DB8::/64&#10;203.0.133.1&#10;</code></pre>
<p>This example would not protect an internal wiki located on a different directory path such as <code>example.com/internal/wiki</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15320.md")
</aside>
<h2 id="access-denied-example">Access denied example</h2>
<p>A visitor from an unauthorized IP will get the following error when there is a match for a zone lockdown rule:</p>
<p><img src="/assets/upstream/images/waf/tools/zone-lockdown-rule-error-1106-access-denied.png" alt="Example of Error 1106 (access denied) received by a user accessing the zone from an unauthorized IP address" /></p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/learning-paths/application-security/account-security/">Secure your application</a></li>
<li><a href="/waf/tools/user-agent-blocking/">User Agent Blocking</a></li>
<li><a href="/health-checks/how-to/zone-lockdown/">Allow Health Checks to bypass Zone Lockdown</a></li>
</ul>
