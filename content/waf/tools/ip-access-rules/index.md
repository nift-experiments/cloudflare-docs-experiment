---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/ip-access-rules/
  description: Control access based on IP address, range, country, or ASN.
  full_title: IP Access rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>IP Access rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Control access based on IP address, range, country, or ASN."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/index.md"><meta property="og:title" content="IP Access rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control access based on IP address, range, country, or ASN."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/ip-access-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/ip-access-rules/#page","headline":"IP Access rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Control access based on IP address, range, country, or ASN.","url":"https://developers.cloudflare.com/waf/tools/ip-access-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/ip-access-rules/
  schema: 1
---
<p>Use IP Access rules to <span class="nb-glossary-tooltip" title="allowlist">allowlist</span>, block, and challenge traffic based on the visitor's IP address, Autonomous System Number (ASN), or country.</p>
<p>IP Access rules are commonly used to block or challenge suspected malicious traffic. Another common use of IP Access rules is to allow services that regularly access your site, such as APIs, crawlers, and payment providers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15727.md")
</aside>
<h2 id="important-remarks-about-allowing-blocking-by-country">Important remarks about allowing/blocking by country</h2>
<p>Block by country is only available on Enterprise plans.</p>
<p>IP addresses globally allowed by Cloudflare will override an IP Access rule country block, but they will not override a country block via <a href="/waf/custom-rules/">custom rules</a>.</p>
<p>Allowing a country will:</p>
<ul>
<li>Bypass any configured <a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, and firewall rules (deprecated).</li>
<li>Not bypass <a href="/waf/managed-rules/">WAF Managed Rules</a> or <a href="/waf/reference/legacy/old-waf-managed-rules/">WAF managed rules (previous version)</a>.</li>
</ul>
<h2 id="recommendation-use-custom-rules-instead">Recommendation: Use custom rules instead</h2>
<p>Cloudflare recommends that you create <a href="/waf/custom-rules/">custom rules</a> instead of IP Access rules to perform IP-based or geography-based blocking (geoblocking):</p>
<ul>
<li>For IP-based blocking, use an <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a> in the custom rule expression. Refer to <a href="/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/">Allow traffic from IP addresses in allowlist only</a> for an example.</li>
<li>For geoblocking, use fields such as <em>AS Num</em>, <em>Country</em>, and <em>Continent</em> in the custom rule expression. Refer to <a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">Block traffic from specific countries</a> for an example.</li>
</ul>
<p>When upgrading to custom rules, consider replacing the <em>Allow</em> action supported by IP Access rules with the <a href="/waf/custom-rules/skip/"><em>Skip</em> action</a>. Note that the <em>Skip</em> action does not bypass all of Cloudflare's app security features.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>IP Access rules are available to all customers.</p>
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
<td>50,000</td>
<td>50,000</td>
<td>50,000</td>
<td>50,000, but can purchase more</td>
</tr>
<tr>
<td>Block by country</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Each Cloudflare account can have a maximum of 50,000 rules. If you are an Enterprise customer and need more rules, contact your account team.</p>
<p>Block by country is only available on Enterprise plans. Other customers may perform country blocking using <a href="/waf/custom-rules/">WAF custom rules</a>.</p>
<h2 id="final-remarks">Final remarks</h2>
<ul>
<li>
<p>By design, IP Access rules configured to <em>Allow</em> traffic do not show up in <a href="/waf/analytics/security-events/">Security Events</a>.</p>
</li>
<li>
<p>Requests containing certain attack patterns in the <code>User-Agent</code> field are checked before being processed by the general firewall pipeline. Therefore, such requests are blocked before any allowlist logic takes place. When this occurs, security events downloaded from the API show <code>rule_id</code> as <code>security_level</code> and action as <code>drop</code>.</p>
</li>
<li>
<p>Cloudflare supports use of <code>fail2ban</code> to block IPs on your server. However, to prevent <code>fail2ban</code> from inadvertently blocking Cloudflare IPs and causing errors for some visitors, ensure you restore original visitor IP in your origin server logs. For details, refer to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restoring original visitor IPs</a>.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p>To learn more about protection options provided by Cloudflare to protect your website against malicious traffic and bad actors, refer to <a href="/learning-paths/application-security/account-security/">Account security</a>.</p>
