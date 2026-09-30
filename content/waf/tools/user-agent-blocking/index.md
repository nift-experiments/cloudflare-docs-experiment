---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/user-agent-blocking/
  description: Block or challenge requests based on User-Agent header values.
  full_title: User Agent Blocking · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>User Agent Blocking · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block or challenge requests based on User-Agent header values."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/user-agent-blocking/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/user-agent-blocking/index.md"><meta property="og:title" content="User Agent Blocking · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block or challenge requests based on User-Agent header values."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/user-agent-blocking/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/user-agent-blocking/#page","headline":"User Agent Blocking \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block or challenge requests based on User-Agent header values.","url":"https://developers.cloudflare.com/waf/tools/user-agent-blocking/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/user-agent-blocking/
  schema: 1
---
<p>User Agent Blocking allows you to block specific browser or web application <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent"><code>User-Agent</code> request headers</a>. User agent rules apply to the entire domain instead of individual subdomains.</p>
<p>User agent rules are applied after <a href="/waf/tools/zone-lockdown/">zone lockdown rules</a>. If you allow an IP address via Zone Lockdown, it will skip any user agent rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15331.md")
</aside>
<h2 id="availability">Availability</h2>
<p>Cloudflare User Agent Blocking is available on all plans. The <strong>User agent rules</strong> option appears only if you have configured at least one user agent rule.</p>
<p>The number of available user agent rules depends on your Cloudflare plan.</p>
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
<td>50</td>
<td>250</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<h2 id="create-a-user-agent-blocking-rule">Create a User Agent Blocking rule</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15335.md")
</div></div>
<h2 id="challenge-actions">Challenge actions</h2>
<p>When a User Agent Blocking rule uses a challenge action such as <em>Managed Challenge</em>, the visitor must pass a challenge page. After passing the challenge, a <code>cf_clearance</code> cookie is set. The duration of this cookie is controlled by the <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a> setting.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/learning-paths/application-security/account-security/">Secure your application</a></li>
<li><a href="/waf/tools/zone-lockdown/">Cloudflare Zone Lockdown</a></li>
</ul>
