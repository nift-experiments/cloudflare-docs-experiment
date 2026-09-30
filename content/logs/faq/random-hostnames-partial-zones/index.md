---
cp9:
  canonical: https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/
  description: Why unexpected hostnames appear in HTTP logs for partial zones.
  full_title: Random hostnames · Cloudflare Logs docs
  head_html: <title>Random hostnames · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Why unexpected hostnames appear in HTTP logs for partial zones."><link rel="canonical" href="https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/index.md"><meta property="og:title" content="Random hostnames · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Why unexpected hostnames appear in HTTP logs for partial zones."><meta property="og:url" content="https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/#page","headline":"Random hostnames \u00b7 Cloudflare Logs docs","description":"Why unexpected hostnames appear in HTTP logs for partial zones.","url":"https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/faq/random-hostnames-partial-zones/
  schema: 1
---
<p><a href="/logs/faq/">❮ Back to FAQ</a></p>
<h3 id="why-do-i-see-hostnames-in-my-http-logs-that-i-did-not-configure">Why do I see hostnames in my HTTP logs that I did not configure?</h3>
<p>If you use a <a href="/dns/zone-setups/partial-setup/">partial (CNAME) zone setup</a>, you may see hundreds of random hostnames in your HTTP request logs despite only proxying a few DNS records. This is caused by Host header manipulation attacks, not a bug in Cloudflare logging.</p>
<h3 id="what-causes-this">What causes this?</h3>
<p>Attackers use a technique called Host header injection:</p>
<ol>
<li>They discover the Cloudflare IP addresses serving your proxied hostname (for example, via DNS lookup of a known proxied subdomain).</li>
<li>They send HTTP requests directly to those IPs with forged <code>Host</code> headers containing random subdomain guesses.</li>
<li>Cloudflare logs the <code>Host</code> header value as-is in the <code>ClientRequestHost</code> field.</li>
<li>The requests reach Cloudflare because they target valid Cloudflare IPs — but the attacker controls the <code>Host</code> header content.</li>
</ol>
<p>The <a href="/ruleset-engine/rules-language/fields/reference/http.host/"><code>http.host</code> field</a> contains the <code>Host</code> header from the original request, which means attacker-controlled values appear in your logs.</p>
<h3 id="why-are-partial-zones-susceptible">Why are partial zones susceptible?</h3>
<p>With partial (CNAME) zones:</p>
<ul>
<li>Only specific hostnames point to Cloudflare via CNAME at your authoritative DNS provider.</li>
<li>Cloudflare does not control the full zone, so it cannot validate that incoming <code>Host</code> headers match configured records.</li>
<li>Attackers can enumerate subdomains by sending requests to known-good IPs with guessed <code>Host</code> headers.</li>
</ul>
<h3 id="how-do-i-identify-this-pattern">How do I identify this pattern?</h3>
<table>
<thead>
<tr>
<th>Indicator</th>
<th>What to look for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Request count distribution</strong></td>
<td>Legitimate hostnames have thousands of requests. Suspicious hostnames have exactly two to five requests each.</td>
</tr>
<tr>
<td><strong>Hostname patterns</strong></td>
<td>Sequential numbers (<code>0-0</code>, <code>0-56</code>, <code>007</code>), common words (<code>admin</code>, <code>api</code>, <code>test</code>, <code>staging</code>), or internal service names (<code>airflow</code>, <code>consul</code>, <code>prometheus</code>).</td>
</tr>
<tr>
<td><strong>Source IPs</strong></td>
<td>Suspicious requests often come from a small set of IPs (scanner infrastructure).</td>
</tr>
<tr>
<td><strong>Response codes</strong></td>
<td>Many 4xx responses (hostname not found, SSL mismatch).</td>
</tr>
<tr>
<td><strong>DNS correlation</strong></td>
<td>Suspicious hostnames do not appear in DNS query logs.</td>
</tr>
</tbody>
</table>
<h3 id="example-data-pattern">Example data pattern</h3>
<pre tabindex="0"><code class="language-txt">&quot;ClientRequestHost&quot;,&quot;_count&quot;&#10;&quot;legitimate-proxied.example.com&quot;,&quot;12498&quot;    # Real traffic&#10;&quot;another-proxied.example.com&quot;,&quot;6082&quot;        # Real traffic&#10;&quot;0-0.example.com&quot;,&quot;2&quot;                       # Scanner&#10;&quot;admin.example.com&quot;,&quot;2&quot;                     # Scanner&#10;&quot;api-staging.example.com&quot;,&quot;2&quot;               # Scanner&#10;&quot;1234567890.example.com&quot;,&quot;2&quot;                # Scanner&#10;</code></pre>
<h3 id="how-do-i-block-these-requests">How do I block these requests?</h3>
<p>Create a <a href="/waf/custom-rules/">WAF custom rule</a> that only allows requests with valid <code>Host</code> headers:</p>
<pre tabindex="0"><code class="language-txt">Expression:&#10;(http.host ne &quot;proxied-hostname-1.example.com&quot; and&#10; http.host ne &quot;proxied-hostname-2.example.com&quot; and&#10; http.host ne &quot;proxied-hostname-3.example.com&quot;)&#10;&#10;Action: Block&#10;</code></pre>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/10493.md")
</aside>
<h3 id="can-i-filter-these-from-my-logs-instead">Can I filter these from my logs instead?</h3>
<p>Yes. If you prefer cleaner logs without blocking traffic:</p>
<ul>
<li><strong>At Logpush level</strong> — Filter the job to include only known-good hostnames using <a href="/logs/logpush/logpush-job/filters/">Logpush filters</a>.</li>
<li><strong>At SIEM level</strong> — Filter or exclude hostnames with request counts below a threshold during log analysis.</li>
</ul>
<h3 id="are-these-requests-reaching-my-origin">Are these requests reaching my origin?</h3>
<p>Possibly, if the <code>Host</code> header happens to match a configured hostname or if you have a default or catch-all origin. Check <code>EdgeResponseStatus</code> and <code>OriginResponseStatus</code> to see if origins were contacted.</p>
<h3 id="is-this-a-security-risk">Is this a security risk?</h3>
<p>The risk is low to moderate. The main concerns are:</p>
<ul>
<li>Information disclosure if error pages reveal internal details.</li>
<li>Resource consumption if requests reach your origin.</li>
<li>Log noise that makes real attacks harder to identify.</li>
</ul>
<h3 id="why-do-suspicious-hostnames-have-exactly-two-requests">Why do suspicious hostnames have exactly two requests?</h3>
<p>Automated scanners typically send one to two requests per subdomain guess — one initial probe and possibly one retry. This uniform distribution is a reliable indicator of scanning activity.</p>
<h3 id="how-do-i-verify-my-solution-is-working">How do I verify my solution is working?</h3>
<p>After implementing a WAF rule:</p>
<ol>
<li>Check <strong>Firewall Events</strong> for blocked requests matching your rule.</li>
<li>Compare log volume before and after — suspicious hostnames should disappear.</li>
<li>Verify legitimate traffic is unaffected by checking request counts for real hostnames.</li>
</ol>
