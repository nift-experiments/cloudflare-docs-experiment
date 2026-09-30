---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/
  description: JSON object structure for Programmable Flow Protection API requests and responses.
  full_title: Programmable Flow Protection API - JSON objects · Cloudflare DDoS Protection docs
  head_html: <title>Programmable Flow Protection API - JSON objects · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="JSON object structure for Programmable Flow Protection API requests and responses."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/index.md"><meta property="og:title" content="Programmable Flow Protection API - JSON objects · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="JSON object structure for Programmable Flow Protection API requests and responses."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="JSON"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/#page","headline":"Programmable Flow Protection API - JSON objects \u00b7 Cloudflare DDoS Protection docs","description":"JSON object structure for Programmable Flow Protection API requests and responses.","url":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/
  schema: 1
---
<p>This page contains examples of the JSON objects used in the Programmable Flow Protection API.</p>
<h2 id="program">Program</h2>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;id&quot;: &quot;31c70c65-9f81-4669-94ed-1e1e041e7b06&quot;,&#10;  &quot;name&quot;: &quot;rate-limiter&quot;,&#10;  &quot;status&quot;: &quot;success&quot;,&#10;  &quot;created_on&quot;: &quot;2024-01-01T13:06:04.721954+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2024-01-01T13:06:04.721954+01:00&quot;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Unique identifier for the program.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>Name of the program, derived from the uploaded filename.</td>
</tr>
<tr>
<td><code>status</code></td>
<td>Compilation and verification status. One of <code>success</code> or <code>failed</code>. Programs with <code>failed</code> status are automatically deleted after 30 days of inactivity.</td>
</tr>
<tr>
<td><code>created_on</code></td>
<td>Timestamp when the program was created.</td>
</tr>
<tr>
<td><code>modified_on</code></td>
<td>Timestamp when the program was last modified.</td>
</tr>
</tbody>
</table>
<h2 id="rule">Rule</h2>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;id&quot;: &quot;20b99eb6-8b48-48dd-a5b9-a995a0843b57&quot;,&#10;  &quot;program_id&quot;: &quot;31c70c65-9f81-4669-94ed-1e1e041e7b06&quot;,&#10;  &quot;scope&quot;: &quot;region&quot;,&#10;  &quot;name&quot;: &quot;WEUR&quot;,&#10;  &quot;mode&quot;: &quot;enabled&quot;,&#10;  &quot;expression&quot;: &quot;ip.dst in { 192.0.2.0/24 }&quot;,&#10;  &quot;created_on&quot;: &quot;2024-01-01T13:10:38.762503+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2024-01-01T13:10:38.762503+01:00&quot;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Unique identifier for the rule.</td>
</tr>
<tr>
<td><code>program_id</code></td>
<td>The ID of the program this rule executes.</td>
</tr>
<tr>
<td><code>scope</code></td>
<td>The scope of the rule. Must be one of <code>global</code>, <code>region</code>, or <code>datacenter</code>.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>For <code>global</code> scope, use <code>global</code>. For <code>region</code> or <code>datacenter</code> scope, provide the region code or datacenter code.</td>
</tr>
<tr>
<td><code>mode</code></td>
<td>The rule mode. Must be one of <code>enabled</code>, <code>disabled</code>, or <code>monitoring</code>.</td>
</tr>
<tr>
<td><code>expression</code></td>
<td>A <a href="/ruleset-engine/rules-language/expressions/">Rules language expression</a> to filter which packets the rule applies to. Optional.</td>
</tr>
<tr>
<td><code>created_on</code></td>
<td>Timestamp when the rule was created.</td>
</tr>
<tr>
<td><code>modified_on</code></td>
<td>Timestamp when the rule was last modified.</td>
</tr>
</tbody>
</table>
<h3 id="scope">Scope</h3>
<p>The <code>scope</code> field determines where the rule executes:</p>
<ul>
<li><code>global</code> — The rule executes at all Cloudflare locations. You can only create one global rule per account.</li>
<li><code>region</code> — The rule executes at all Cloudflare locations within the specified region.</li>
<li><code>datacenter</code> — The rule executes only at the specified Cloudflare datacenter.</li>
</ul>
<p>When multiple rules match a packet, the rule with the most specific scope executes. A datacenter-scoped rule takes precedence over a region-scoped rule, which takes precedence over a global rule.</p>
<h3 id="mode">Mode</h3>
<p>The <code>mode</code> field determines how the rule behaves:</p>
<ul>
<li><code>enabled</code> — The program runs and its verdict (pass or drop) is applied to packets.</li>
<li><code>disabled</code> — The rule is inactive and the program does not run.</li>
<li><code>monitoring</code> — The program runs but packets are never dropped, regardless of the program's verdict. Use this mode to test a program before enabling it.</li>
</ul>
<h3 id="expression">Expression</h3>
<p>The <code>expression</code> field is a <a href="/ruleset-engine/rules-language/expressions/">Rules language expression</a> up to 8,192 characters. The expression filters which packets the rule applies to. Only packets matching the expression are processed by the program.</p>
<p>Supported fields:</p>
<ul>
<li><code>ip.src</code></li>
<li><code>ip.dst</code></li>
<li><code>udp.srcport</code></li>
<li><code>udp.dstport</code></li>
</ul>
<p>If the expression is empty or omitted, the rule applies to all UDP packets within its scope.</p>
<p>For more information on rule settings, refer to <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule-settings">Rule settings</a>.</p>
