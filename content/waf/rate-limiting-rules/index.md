---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/
  description: Define rate limits for requests matching an expression and the action when limits are reached.
  full_title: Rate limiting rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate limiting rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Define rate limits for requests matching an expression and the action when limits are reached."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/rate-limiting-rules/index.md"><meta property="og:title" content="Rate limiting rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define rate limits for requests matching an expression and the action when limits are reached."><meta property="og:url" content="https://developers.cloudflare.com/waf/rate-limiting-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rate limiting"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/#page","headline":"Rate limiting rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Define rate limits for requests matching an expression and the action when limits are reached.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/rate-limiting-rules/
  schema: 1
---
<p>Rate limiting rules allow you to define rate limits for requests matching an expression, and the action to perform when those rate limits are reached. Use rate limiting rules to prevent abuse of your websites and APIs — for example, to protect a login endpoint from brute-force attacks or to cap how many API calls a single client can make in a given time window.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="were-you-blocked-from-accessing-a-website">Were you blocked from accessing a website?</h3>
@markup("md", "content/.markup/bodies/15361.md")
</aside>
<p>In the <a href="/security/">new security dashboard</a>, rate limiting rules are one of the available types of <a href="/security/rules/">security rules</a>. Security rules perform security-related actions on incoming requests that match specified filters.</p>
<p>Some Enterprise customers can create <a href="/waf/account/rate-limiting-rulesets/">rate limiting rulesets</a> at the account level that they can deploy to multiple Enterprise zones.</p>
<h2 id="rule-parameters">Rule parameters</h2>
<p>Like other rules evaluated by Cloudflare's <a href="/ruleset-engine/">Ruleset Engine</a>, rate limiting rules have the following basic parameters:</p>
<ul>
<li>An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that specifies the criteria you are matching traffic on using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</li>
<li>An <a href="/ruleset-engine/rules-language/actions/">action</a> that specifies what to perform when there is a match for the rule and any additional conditions are met. In the case of rate limiting rules, the action occurs when the rate reaches the specified limit.</li>
</ul>
<p>Besides these two parameters, rate limiting rules require the following additional parameters:</p>
<ul>
<li><strong>Characteristics</strong>: The set of parameters that define how Cloudflare tracks the rate for this rule.</li>
<li><strong>Period</strong>: The period of time to consider (in seconds) when evaluating the rate.</li>
<li><strong>Requests per period</strong>: The number of requests over the period of time that will trigger the rate limiting rule.</li>
<li><strong>Duration</strong> (or mitigation timeout): Once the rate is reached, the rate limiting rule blocks further requests for the period of time defined in this field.</li>
<li><strong>Action behavior</strong>: By default, Cloudflare will apply the rule action for the configured duration (or mitigation timeout), regardless of the request rate during this period. Some Enterprise customers can configure the rule to <a href="/waf/rate-limiting-rules/parameters/#with-the-following-behavior">throttle requests</a> over the maximum rate, allowing incoming requests when the rate is lower than the configured limit.</li>
</ul>
<p>Refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a> for more information on mandatory and optional parameters.</p>
<p>Refer to <a href="/waf/rate-limiting-rules/request-rate/">How Cloudflare determines the request rate</a> to learn how Cloudflare uses the parameters above when determining the rate of incoming requests.</p>
<h2 id="interaction-with-other-app-security-features">Interaction with other app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>Rate limiting rules are evaluated in order, and some actions like <em>Block</em> will stop the evaluation of other rules. For more details on actions and their behavior, refer to <a href="/ruleset-engine/rules-language/actions/">Actions</a>.</p>
</li>
<li>
<p>Rate limiting rules are not designed to allow a precise number of requests to reach your origin server. There may be a delay of up to a few seconds between detecting a request and updating rate counters. Due to this delay, excess requests could still reach the origin before Cloudflare enforces a mitigation action such as blocking or challenging. For more information on how counters work, including their per-data-center scope, refer to <a href="/waf/rate-limiting-rules/request-rate/">Request rate calculation</a>.</p>
</li>
<li>
<p>Applying rate limiting rules to verified bots might affect Search Engine Optimization (SEO). For more information, refer to <a href="/fundamentals/performance/improve-seo/">Improve SEO</a>.</p>
</li>
</ul>
<hr />
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise with app security</th>
<th>Enterprise with Advanced Rate Limiting</th>
</tr>
</thead>
<tbody>
<tr>
<td>Available fields<br/>in rule expression</td>
<td>Path, <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/">Verified Bot</a></td>
<td>Host, URI, Path, Full URI, Query, Verified Bot</td>
<td>Host, URI, Path, Full URI, Query, Method, Source IP, User Agent, Verified Bot</td>
<td>General request fields, request header fields, Verified Bot, Bot Management fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup></td>
<td>General request fields, request header fields, Verified Bot, Bot Management fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup>, request body fields<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup></td>
</tr>
<tr>
<td>Cache exclusion</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Counting characteristics</td>
<td>IP</td>
<td>IP</td>
<td>IP, IP with NAT support</td>
<td>IP, IP with NAT support</td>
<td>IP, IP with NAT support, Query, Host, Headers, Cookie, ASN, Country, Path, JA3/JA4 Fingerprint<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-1">1</a></sup>, JSON field value<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Body<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Form input value<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-2">2</a></sup>, Custom</td>
</tr>
<tr>
<td>Custom counting expression</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Available fields<br/>in counting expression</td>
<td>N/A</td>
<td>N/A</td>
<td>All rule expression fields, Response code, Response headers</td>
<td>All rule expression fields, Response code, Response headers</td>
<td>All rule expression fields, Response code, Response headers</td>
</tr>
<tr>
<td>Counting model</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests</td>
<td>Number of requests, <a href="/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting">complexity score</a></td>
</tr>
<tr>
<td>Rate limiting<br/>action behavior</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period</td>
<td>Perform action during mitigation period, Throttle requests above rate with block action</td>
<td>Perform action during mitigation period, Throttle requests above rate with block action</td>
</tr>
<tr>
<td>Counting periods</td>
<td>10 s</td>
<td>All supported values up to 1 min<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 10 min<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 65,535 s<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 65,535 s<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
</tr>
<tr>
<td>Mitigation timeout periods</td>
<td>10 s</td>
<td>All supported values up to 1 h<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup> <sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-4">4</a></sup></td>
<td>All supported values up to 1 day<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-3">3</a></sup> <sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-4">4</a></sup></td>
</tr>
<tr>
<td>Number of rules</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>100<sup><a href="#footnote-waf-rate-limiting-availability-by-plan-mdx-5">5</a></sup></td>
<td>100</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15362.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-waf-rate-limiting-availability-by-plan-mdx-1">Only available to Enterprise customers who have purchased [Bot Management](/bots/plans/bm-subscription/).</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-2">Availability depends on your WAF plan.</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-3">Supported period values in seconds:<br/> 10, 15, 20, 30, 40, 45, 60 (1 min), 90, 120 (2 min), 180 (3 min), 240 (4 min), 300 (5 min), 480, 600 (10 min), 900, 1200 (20 min), 1800, 2400, 3600 (1 h), 65535, 86400 (1 day).</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-4">Enterprise customers can specify a custom mitigation timeout period via API.</li>
<li id="footnote-waf-rate-limiting-availability-by-plan-mdx-5">Enterprise customers must have application security on their contract to get access to rate limiting rules. The number of rules depends on the exact contract terms.</li></ol></section>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15360.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Refer to the following resources:</p>
<ul>
<li><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Create a rate limiting rule in the dashboard for a zone</a></li>
<li><a href="/waf/rate-limiting-rules/create-api/">Create a rate limiting rule via API for a zone</a></li>
</ul>
<p>For Terraform examples, refer to <a href="/terraform/additional-configurations/rate-limiting-rules/">Rate limiting rules configuration using Terraform</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li>
<p><a href="https://www.cloudflare.com/learning/bots/what-is-rate-limiting/">Learning Center: What is rate limiting?</a></p>
</li>
<li>
<p><a href="/waf/reference/legacy/old-rate-limiting/">Cloudflare Rate Limiting (previous version, no longer available)</a>: Documentation for the previous version of rate limiting rules (billed based on usage).</p>
</li>
</ul>
