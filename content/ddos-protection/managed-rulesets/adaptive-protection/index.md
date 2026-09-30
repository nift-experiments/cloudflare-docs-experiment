---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/
  description: Explore Cloudflare's Adaptive DDoS Protection, which learns traffic patterns to defend against sophisticated DDoS attacks on layers 3/4 and 7.
  full_title: Adaptive DDoS Protection · Cloudflare DDoS Protection docs
  head_html: <title>Adaptive DDoS Protection · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore Cloudflare&#x27;s Adaptive DDoS Protection, which learns traffic patterns to defend against sophisticated DDoS attacks on layers 3/4 and 7."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/index.md"><meta property="og:title" content="Adaptive DDoS Protection · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore Cloudflare&#x27;s Adaptive DDoS Protection, which learns traffic patterns to defend against sophisticated DDoS attacks on layers 3/4 and 7."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/#page","headline":"Adaptive DDoS Protection \u00b7 Cloudflare DDoS Protection docs","description":"Explore Cloudflare's Adaptive DDoS Protection, which learns traffic patterns to defend against sophisticated DDoS attacks on layers 3/4 and 7.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/adaptive-protection/
  schema: 1
---
<p>Adaptive DDoS Protection learns your unique traffic patterns and adapts to them to provide better protection against sophisticated DDoS attacks on layer 7 and layers 3/4, depending on your subscribed Cloudflare services.</p>
<p>Adaptive DDoS Protection provides the following types of protection:</p>
<ul>
<li><strong>Adaptive DDoS Protection for Origins</strong>: Detects and mitigates traffic that deviates from your site's origin errors profile.</li>
<li><strong>Adaptive DDoS Protection for User-Agents</strong>: Detects and mitigates traffic that deviates from the top User Agents seen by Cloudflare on the network. The User Agent profile is built from the entire Cloudflare network and not only from the customer's zone.</li>
<li><strong>Adaptive DDoS Protection for Locations</strong>: Detects and mitigates traffic that deviates from your site's geo-distribution profile. The profile is calculated from the rate for every client country and region, using the rates from the past seven days.</li>
<li><strong>Adaptive DDoS Protection for Protocols</strong>: Detects and mitigates traffic that deviates from your traffic's IP protocol profile. The profile is calculated as a global rate for each of your prefixes.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>Cloudflare Adaptive DDoS Protection is available to Enterprise customers according to the following table:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Profiling dimension</th>
<th align="center">WAF/CDN<sup>1</sup></th>
<th align="center">Magic Transit /<br/>Spectrum BYOIP<sup>2</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP Adaptive DDoS Protection</strong></td>
<td></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td>For Origins</td>
<td>Origin errors</td>
<td align="center">Yes</td>
<td align="center">—</td>
</tr>
<tr>
<td>For User-Agents</td>
<td>User Agent<br/>(entire Cloudflare network)</td>
<td align="center">Yes</td>
<td align="center">—</td>
</tr>
<tr>
<td>For Locations</td>
<td>Client IP country and region</td>
<td align="center">Yes</td>
<td align="center">—</td>
</tr>
<tr>
<td><strong>L3/4 Adaptive DDoS Protection</strong></td>
<td></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td>For Protocols</td>
<td>IP protocol</td>
<td align="center">—</td>
<td align="center">Yes</td>
</tr>
<tr>
<td>For Protocols</td>
<td>Client IP country and Region for UDP</td>
<td align="center">—</td>
<td align="center">Yes</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> <em>WAF/CDN customers on the Enterprise plan with the Advanced DDoS
Protection subscription.</em>
<br />
<sup>2</sup> <em>Magic Transit and Spectrum BYOIP customers on an Enterprise plan.</em></p>
<h2 id="how-it-works">How it works</h2>
<p>Adaptive DDoS Protection creates a traffic profile by looking at the maximum rates of traffic every day, for the past seven days. These profiles are recalculated every day, keeping the seven-day time window. Adaptive DDoS Protection stores the maximal traffic rates seen for every predefined dimension value (the profiling dimension varies for each rule). Every profile uses one dimension, such as the source country of the request, the user agent, and the IP protocol. Incoming traffic that deviates from your profile may be malicious.</p>
<p>To eliminate outliers, rate calculations only consider the 95th percentile rates (discarding the top 5% of the highest rates). Cloudflare requires a minimum amount of requests per second (rps) to build traffic profiles. HTTP Adaptive DDoS Protection rules also take into account Cloudflare's <a href="/bots/concepts/bot-score/#machine-learning">Machine Learning (ML) models</a> to identify traffic that is likely automated.</p>
<p>Cloudflare may change the logic of these protection rules from time to time to improve them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7461.md")
</aside>
<hr />
<h2 id="view-flagged-traffic">View flagged traffic</h2>
<p>To view traffic flagged by HTTP Adaptive DDoS Protection rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7462.md")
</div>
<p>To view traffic flagged by L3/4 Adaptive DDoS Protection rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7463.md")
</div>
<p>You may also obtain information about flagged traffic through <a href="/logs/logpush/">Logpush</a> or the <a href="/analytics/graphql-api/">GraphQL API</a>.</p>
<p>To determine if an adaptive rule fits your traffic in a way that will only mitigate attack traffic and will not cause false positives, review the traffic that is <em>Logged</em> by the adaptive rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7460.md")
</aside>
<p>If you do see traffic that was <em>Logged</em> by the adaptive rules, use the dashboard to determine if the traffic matches the characteristics of legitimate users or that of attack traffic. As each Internet property is unique, understanding if the traffic is legitimate requires your understanding of how your legitimate traffic looks. For example, the user agent, source country, headers, query string for HTTP requests, and protocols and ports for L3/4 traffic.</p>
<ul>
<li>In cases where you are certain that the rule is only flagging attack traffic, you should consider creating an override and enabling that rule with a <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> or <code>Block</code> action.</li>
<li>In cases where you see legitimate traffic being flagged, you should lower the sensitivity level of the rule and observe the flagged traffic. You can continue reducing the sensitivity level until you reach a point where legitimate traffic is not flagged. Then, you should create an override to enable the rule with a mitigation action.</li>
<li>If the rule is still flagging legitimate traffic you can consider using the expression filters to condition the rules to exclude certain types of traffic.</li>
</ul>
<p>The default rule action for <code>log</code> with a sensitivity set to <code>high</code> will only show packets or requests with suspected attack traffic over internal <code>high</code> thresholds in your logs. For instance, if you set the threshold to <code>medium</code> or <code>low</code>, then only packets over those thresholds will be logged.</p>
<h2 id="configure-the-rules">Configure the rules</h2>
<p>You can adjust the action and sensitivity of the Adaptive DDoS Protection rules. The default action is <em>Log</em>. Use this action to first observe what traffic is flagged before deciding on a mitigation action.</p>
<p>To configure a rule, refer to the instructions in the following pages:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">Configure HTTP DDoS Attack Protection in the dashboard</a> (for L7 rules)</li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">Configure Network-layer DDoS Attack Protection in the dashboard</a> (for L3/4 rules)</li>
</ul>
<p>For more information on the available configuration parameters, refer to the following pages:</p>
<ul>
<li>For the (L7) DDoS protection rules for Origins, User-Agents, and Locations:<br/>
<a href="/ddos-protection/managed-rulesets/http/override-parameters/">HTTP DDoS Attack Protection parameters</a></li>
<li>For the (L3/4) DDoS protection rules for Protocols:<br/>
<a href="/ddos-protection/managed-rulesets/network/override-parameters/">Network-layer DDoS Attack Protection parameters</a></li>
</ul>
