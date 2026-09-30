---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/
  description: Configurable parameters for HTTP DDoS Attack Protection rule overrides.
  full_title: HTTP DDoS Attack Protection parameters · Cloudflare DDoS Protection docs
  head_html: <title>HTTP DDoS Attack Protection parameters · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Configurable parameters for HTTP DDoS Attack Protection rule overrides."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/index.md"><meta property="og:title" content="HTTP DDoS Attack Protection parameters · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configurable parameters for HTTP DDoS Attack Protection rule overrides."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/#page","headline":"HTTP DDoS Attack Protection parameters \u00b7 Cloudflare DDoS Protection docs","description":"Configurable parameters for HTTP DDoS Attack Protection rule overrides.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/http/override-parameters/
  schema: 1
---
<p>Configure the HTTP DDoS Attack Protection managed ruleset to change the action applied to a given attack or modify the sensitivity level of the detection mechanism. You can <a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">configure the managed ruleset in the Cloudflare dashboard</a> or <a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/">define overrides via Rulesets API</a>.</p>
<p>The available parameters are the following:</p>
<ul>
<li><a href="#action">Action</a></li>
<li><a href="#sensitivity-level">Sensitivity Level</a></li>
</ul>
<h2 id="action">Action</h2>
<p>API property name: <code>&quot;action&quot;</code>.</p>
<p>The action that will be performed for requests that match specific rules of Cloudflare's DDoS mitigation services. The available actions are:</p>
<ul>
<li>
<p><strong>Block</strong></p>
<ul>
<li>API value: <code>&quot;block&quot;</code>.</li>
<li>Blocks HTTP requests that match the rule expression.</li>
</ul>
</li>
<li>
<p><strong>Managed Challenge</strong></p>
<ul>
<li>API value: <code>&quot;managed_challenge&quot;</code>.</li>
<li><a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenges</a> help reduce the lifetimes of human time spent solving CAPTCHAs across the Internet. Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge based on specific criteria.</li>
</ul>
</li>
<li>
<p><strong>Interactive Challenge</strong></p>
<ul>
<li>API value: <code>&quot;challenge&quot;</code>.</li>
<li>Presents an interactive challenge to the clients making HTTP requests that match a rule expression.</li>
</ul>
</li>
<li>
<p><strong>Log</strong></p>
<ul>
<li>API value: <code>&quot;log&quot;</code>.</li>
<li>Only available on Enterprise plans with the Advanced DDoS Protection subscription. Logs requests that match the expression of a rule detecting HTTP DDoS attacks. Recommended for validating a rule before committing to a more severe action.</li>
</ul>
</li>
<li>
<p><strong>Connection Close</strong></p>
<ul>
<li>API value: <em>N/A</em> (internal rule action that you cannot use in overrides).</li>
<li>The client is instructed to establish a new connection (by disabling <code>keep-alive</code>) instead of reusing the existing connection. Existing requests are not affected.</li>
</ul>
</li>
<li>
<p><strong>Force Connection Close</strong></p>
<ul>
<li>API value: <em>N/A</em> (internal rule action that you cannot use in overrides).</li>
<li>Closes ongoing HTTP connections. This action does not block a request, but it forces the client to reconnect. For HTTP/2 and HTTP/3 connections, the connection will be closed even if it breaks other requests running on the same connection.</li>
<li>The performed action depends on the HTTP version:
<ul>
<li>HTTP/1: set the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Connection#directives"><code>Connection</code> header</a> to <code>close</code>.</li>
<li>HTTP/2: send a <a href="https://datatracker.ietf.org/doc/html/rfc7540#section-6.8"><code>GOAWAY</code> frame</a> to the client.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>DDoS Dynamic</strong></p>
<ul>
<li>API value: <em>N/A</em> (internal rule action that you cannot use in overrides).</li>
<li>Performs a specific action according to a set of internal guidelines defined by Cloudflare. The executed action can be one of the above or an undisclosed mitigation action.</li>
</ul>
</li>
</ul>
<h2 id="sensitivity-level">Sensitivity Level</h2>
<p>API property name: <code>&quot;sensitivity_level&quot;</code>.</p>
<p>Defines how sensitive a rule is. Affects the thresholds used to determine if an attack should be mitigated. A higher sensitivity level means having a lower threshold, while a lower sensitivity level means having a higher threshold.</p>
<p>The available sensitivity levels are:</p>
<table>
<thead>
<tr>
<th>UI value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>High</em></td>
<td><code>&quot;default&quot;</code></td>
</tr>
<tr>
<td><em>Medium</em></td>
<td><code>&quot;medium&quot;</code></td>
</tr>
<tr>
<td><em>Low</em></td>
<td><code>&quot;low&quot;</code></td>
</tr>
<tr>
<td><em>Essentially Off</em></td>
<td><code>&quot;eoff&quot;</code></td>
</tr>
</tbody>
</table>
<p>The default sensitivity level is <em>High</em>.</p>
<p>In most cases, when you select the <em>Essentially Off</em> sensitivity level the rule will not trigger for any of the selected actions, including <em>Log</em>. However, if the attack is extremely large, Cloudflare's protection systems will still trigger the rule's mitigation action to protect Cloudflare's network.</p>
<p><em>Essentially Off</em> means that we have set an exceptionally low sensitivity level so in most cases traffic will not be mitigated for you. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.</p>
<p><strong>Log</strong> means that requests will not be mitigated but only logged and shown on the dashboard. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.</p>
