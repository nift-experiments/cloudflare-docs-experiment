---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/
  description: Fields available for threat intelligence detection in rule expressions.
  full_title: Threat intelligence fields · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Threat intelligence fields · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Fields available for threat intelligence detection in rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/index.md"><meta property="og:title" content="Threat intelligence fields · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fields available for threat intelligence detection in rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Threat Intelligence"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/#page","headline":"Threat intelligence fields \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Fields available for threat intelligence detection in rule expressions.","url":"https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Threat Intelligence"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/threat-intelligence/fields/
  schema: 1
---
<p>The threat intelligence detection populates the following fields when the client IP address is found in the threat intelligence database. If the IP address is not found, the fields are empty.</p>
<p>All fields are arrays. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match values.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15487.md")
</aside>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Threat intelligence datasets <br/> <code>cf.intel.ip.datasets</code> <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Dataset that flagged the IP address. Values: <code>ddos</code>, <code>waf</code>.</td>
</tr>
<tr>
<td>Target industries <br/> <code>cf.intel.ip.target_industries</code> <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Industries this IP address has targeted. Refer to <a href="#target-industries">target industries</a> for valid values.</td>
</tr>
<tr>
<td>Attacker names <br/> <code>cf.intel.ip.attacker_names</code> <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Threat actor names associated with this IP address (for example, <code>CONVOLUTEDKRILL</code>).</td>
</tr>
<tr>
<td>Attacker countries <br/> <code>cf.intel.ip.attacker_countries</code> <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Source countries of the threat activity, as <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> codes.</td>
</tr>
<tr>
<td>Target countries <br/> <code>cf.intel.ip.target_countries</code> <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Countries this IP address has targeted, as <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> codes.</td>
</tr>
</tbody>
</table>
<h2 id="case-sensitivity">Case sensitivity</h2>
<p>Values are case-sensitive. Use the casing shown in the examples: <code>ddos</code> (lowercase), <code>FR</code> (uppercase country codes), <code>Banking &amp; Financial Services</code> (title case), <code>BLACKBASTA</code> (uppercase attacker names).</p>
<p>To discover valid values for your traffic, use the <a href="/security-center/cloudforce-one/">Threat Events</a> dashboard.</p>
<h2 id="matching-behavior">Matching behavior</h2>
<p>Fields reflect all threat activity for an IP address over the past seven days, flattened into a single set of values per field.</p>
<p>A value in one field does not have to come from the same threat event as a value in another field. For example, this expression matches if the IP has <em>any</em> China-origin activity <strong>and</strong> <em>any</em> banking-targeted activity — even from separate events:</p>
<pre tabindex="0"><code class="language-txt">any(cf.intel.ip.attacker_countries[*] == &quot;CN&quot;) and any(cf.intel.ip.target_industries[*] == &quot;Banking &amp; Financial Services&quot;)&#10;</code></pre>
<p>Combining fields across dimensions produces broader matches than you might expect. Test combined rules with the <em>Log</em> action first.</p>
<h2 id="target-industries">Target industries</h2>
<p>The <code>cf.intel.ip.target_industries</code> field uses a fixed set of industry names. Examples:</p>
<ul>
<li><code>Automotive</code></li>
<li><code>Banking &amp; Financial Services</code></li>
<li><code>Cryptocurrency</code></li>
<li><code>Telecommunications</code></li>
</ul>
<p>For the complete list, refer to <a href="/security-center/cloudforce-one/">Threat Events</a>.</p>
