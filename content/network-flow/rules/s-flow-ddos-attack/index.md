---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/
  description: Create sFlow DDoS attack detection rules.
  full_title: sFlow DDoS attack rule · Cloudflare Network Flow docs
  head_html: <title>sFlow DDoS attack rule · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Create sFlow DDoS attack detection rules."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/index.md"><meta property="og:title" content="sFlow DDoS attack rule · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create sFlow DDoS attack detection rules."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Flow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/#page","headline":"sFlow DDoS attack rule \u00b7 Cloudflare Network Flow docs","description":"Create sFlow DDoS attack detection rules.","url":"https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-flow/rules/s-flow-ddos-attack/
  schema: 1
---
<p>An sFlow DDoS attack rule (beta) alerts you when a DDoS attack is detected in your network traffic. Network Flow (formerly Magic Network Monitoring) uses the same DDoS detection rules that protect Cloudflare's global network to identify these attacks.</p>
<p>To use sFlow DDoS attack rules, you must send sFlow data to Cloudflare. You can only configure these rules through the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Network Flow Rules API</a> — they are not available in the dashboard.</p>
<h2 id="send-sflow-data-from-your-network-to-cloudflare">Send sFlow data from your network to Cloudflare</h2>
<p>To send sFlow data to Cloudflare, your router must support sFlow exports. Refer to <a href="/network-flow/routers/supported-routers/">Supported routers</a> to verify compatibility, and <a href="/network-flow/routers/sflow-config/">Configure sFlow</a> for setup instructions.</p>
<h2 id="rule-configuration-fields">Rule configuration fields</h2>
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Rule name</strong></td>
<td align="left">Must be unique and cannot contain spaces. Supports characters <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, underscore (<code>_</code>), dash (<code>-</code>), period (<code>.</code>), and tilde (<code>~</code>). Maximum of 256 characters.</td>
</tr>
<tr>
<td align="left"><strong>Rule type</strong></td>
<td align="left">advanced_ddos</td>
</tr>
<tr>
<td align="left"><strong>Prefix Match</strong></td>
<td align="left">The field <code>prefix_match</code> determines how IP matches are handled. <br/><br/><strong>Subnet</strong> (recommended): Automatically advertise if the attacked IPs are within a subnet of a public IP prefix that can be advertised by Magic Transit.<br/><br/><strong>Exact</strong>: Automatically advertise if the attacked IPs are an exact match with a public IP prefix that can be advertised by Magic Transit.<br/><br/><strong>Supernet</strong>: Automatically advertise if the attacked IPs are a supernet of a public IP prefix that can be advertised by Magic Transit.</td>
</tr>
<tr>
<td align="left"><strong>Auto-advertisement</strong></td>
<td align="left">If you are a <a href="/magic-transit/on-demand">Magic Transit On Demand</a> customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. To learn more, refer to <a href="/network-flow/rules/#rule-auto-advertisement">Auto-advertisement</a>.</td>
</tr>
<tr>
<td align="left"><strong>Rule IP prefix</strong></td>
<td align="left">The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as <code>160.168.0.1/24</code>. The maximum is 5,000 unique CIDR entries. To learn more and see an example, refer to <a href="/network-flow/rules/#rule-ip-prefixes">Rule IP prefixes</a>.</td>
</tr>
</tbody>
</table>
<h2 id="api-documentation">API documentation</h2>
<p>Refer to the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Rules API documentation</a> to review an example API configuration call using CURL and the expected output for a successful response.</p>
<h2 id="tune-the-sflow-ddos-alert-thresholds">Tune the sFlow DDoS alert thresholds</h2>
<p>You can tune the thresholds of your sFlow DDoS alerts in the dashboard and via the Cloudflare API by following the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a> guide.</p>
