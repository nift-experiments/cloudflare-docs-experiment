---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/
  description: Explore HTTP DDoS Attack Protection rule categories, including botnets, unusual requests, and advanced features, to enhance your Cloudflare security.
  full_title: HTTP DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs
  head_html: <title>HTTP DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore HTTP DDoS Attack Protection rule categories, including botnets, unusual requests, and advanced features, to enhance your Cloudflare security."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/index.md"><meta property="og:title" content="HTTP DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore HTTP DDoS Attack Protection rule categories, including botnets, unusual requests, and advanced features, to enhance your Cloudflare security."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/#page","headline":"HTTP DDoS Attack Protection managed ruleset \u00b7 Cloudflare DDoS Protection docs","description":"Explore HTTP DDoS Attack Protection rule categories, including botnets, unusual requests, and advanced features, to enhance your Cloudflare security.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/http/
  schema: 1
---
<p>The Cloudflare HTTP DDoS Attack Protection managed ruleset is a set of pre-configured rules used to match <a href="/ddos-protection/about/attack-coverage/">known DDoS attack vectors</a> at layer 7 (application layer) on the Cloudflare global network. The rules match known attack patterns and tools, suspicious patterns, protocol violations, requests causing large amounts of origin errors, excessive traffic hitting the origin/cache, and additional attack vectors at the application layer.</p>
<p>Cloudflare updates the list of rules in the managed ruleset on a regular basis. Refer to the <a href="/ddos-protection/change-log/http/">changelog</a> for more information on recent and upcoming changes.</p>
<p>The HTTP DDoS Attack Protection managed ruleset is always enabled — you can only customize its behavior.</p>
<p>The HTTP DDoS Attack Protection managed ruleset provides users with increased observability into L7 DDoS attacks mitigated by Cloudflare, informing users of ongoing or past attacks. The <a href="/waf/analytics/security-events/">Security Events dashboard</a>, available at <strong>Security</strong> &gt; <strong>Events</strong>, will display information about the top HTTP DDoS managed rules.</p>
<h2 id="ruleset-configuration">Ruleset configuration</h2>
<p>If you are expecting large spikes of legitimate traffic, consider customizing your DDoS protection settings to avoid <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">false positives</a>, where legitimate traffic is falsely identified as attack traffic and blocked/challenged.</p>
<p>You can adjust the behavior of the rules in the managed ruleset by modifying the following parameters:</p>
<ul>
<li>The performed <strong>action</strong> when an attack is detected.</li>
<li>The <strong>sensitivity level</strong> of attack detection mechanisms.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/7518.md")
</aside>
<p>To adjust rule behavior, do one of the following:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">Configure the managed ruleset in the Cloudflare dashboard</a>.</li>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/">Configure the managed ruleset via API</a>.</li>
<li><a href="/terraform/additional-configurations/ddos-managed-rulesets/#example-configure-http-ddos-attack-protection">Configure the managed ruleset using Terraform</a>.</li>
</ul>
<p>For more information on the available configuration parameters, refer to <a href="/ddos-protection/managed-rulesets/http/override-parameters/">Managed ruleset parameters</a>.</p>
<h2 id="origin-protect-rules">Origin Protect rules</h2>
<p>Cloudflare HTTP DDoS Protection can also initiate mitigation based on the origin health. <a href="/ddos-protection/managed-rulesets/adaptive-protection/">Adaptive DDoS Protection for Origins</a> detects and mitigates traffic that deviates from your site's origin errors profile. Floods of requests that cause a high number of zone errors (default sensitivity level is 1,000 errors per second) can initiate mitigation to alleviate the strain on the zone.</p>
<table>
<thead>
<tr>
<th>Rule ID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dd42da7baabe4e518eaf11c393596a9d</code></td>
<td>HTTP requests causing a high number of origin errors.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7517.md")
</aside>
<p>While Cloudflare's network is built to automatically monitor and mitigate large DDoS attacks, Cloudflare also helps mitigate smaller DDoS attacks, based on the following general rules:</p>
<ul>
<li>
<p>For zones on any plan, Cloudflare will apply mitigations when the HTTP error rate is above the <em>High</em> (default) sensitivity level of 1,000 errors-per-second rate threshold. You can decrease the sensitivity level by configuring the HTTP DDoS Attack Protection managed ruleset.</p>
</li>
<li>
<p>For zones on Pro, Business, and Enterprise plans, Cloudflare performs an additional check for better detection accuracy: the errors-per-second rate must also be at least five times the normal origin traffic levels before applying DDoS mitigations.</p>
</li>
</ul>
<p>All HTTP errors in the <code>52x</code> range (Internal Server Error) and all errors in the <code>53x</code> range excluding <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-530"><code>530</code></a> are considered when factoring in the error rate. For DDoS mitigations based on HTTP error rate, you cannot exclude specific HTTP error codes.</p>
<p>For more information on the types of DDoS attacks covered by Cloudflare's DDoS protection, refer to <a href="/ddos-protection/about/attack-coverage/">DDoS attack coverage</a>.</p>
<h2 id="availability">Availability</h2>
<p>The HTTP DDoS Attack Protection managed ruleset protects Cloudflare customers on all plans for zones <a href="/dns/zone-setups/full-setup/">onboarded to Cloudflare</a>. All customers can customize the ruleset both at the zone level and at the account level.</p>
<p>Customers on Enterprise plans with the Advanced DDoS Protection subscription can create up to 10 overrides (or up to 10 rules, for API users) with custom <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/">expressions</a>, to customize the DDoS protection for different incoming requests.</p>
<p>Other customers can only create one override (or rule) and they cannot customize the rule expression. In this case, the single override, containing one or more configurations, will always apply to all incoming traffic.</p>
<h2 id="related-cloudflare-products">Related Cloudflare products</h2>
<p>To block additional L7 attacks you can use other Cloudflare products like the <a href="/waf/">Cloudflare WAF</a>.</p>
