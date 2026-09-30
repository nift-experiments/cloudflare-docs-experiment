---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/
  description: Create dynamic threshold rules for anomaly detection.
  full_title: Dynamic threshold rule · Cloudflare Network Flow docs
  head_html: <title>Dynamic threshold rule · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Create dynamic threshold rules for anomaly detection."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/index.md"><meta property="og:title" content="Dynamic threshold rule · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create dynamic threshold rules for anomaly detection."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Flow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/#page","headline":"Dynamic threshold rule \u00b7 Cloudflare Network Flow docs","description":"Create dynamic threshold rules for anomaly detection.","url":"https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-flow/rules/dynamic-threshold/
  schema: 1
---
<p>A dynamic threshold rule (beta) monitors your network traffic patterns and automatically adjusts the Distributed Denial of Service (DDoS) threshold based on traffic history. Network Flow (formerly Magic Network Monitoring) compares total traffic across all IP prefixes and addresses in the rule against the dynamic threshold, measured in bits or packets per second. If traffic exceeds the threshold, Network Flow sends an alert.</p>
<p>To use dynamic threshold rules, you must send NetFlow or sFlow data to Cloudflare. You can only configure dynamic threshold rules through the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Network Flow Rules API</a> — they are not available in the dashboard.</p>
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
<td align="left">zscore</td>
</tr>
<tr>
<td align="left"><strong>Target</strong></td>
<td align="left">Can be defined in either bits per second or packets per second.</td>
</tr>
<tr>
<td align="left"><strong>Sensitivity</strong></td>
<td align="left">Controls how easily traffic anomalies trigger alerts. Available values: low, medium, and high. Higher sensitivity triggers alerts on smaller deviations from normal traffic.</td>
</tr>
<tr>
<td align="left"><strong>Auto-advertisement</strong></td>
<td align="left">If you are a <a href="/magic-transit/on-demand">Magic Transit On Demand</a> customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. Network Flow supports Magic Transit's supernet capability. To learn more refer to <a href="/network-flow/rules/#rule-auto-advertisement">Auto-Advertisement section</a>.</td>
</tr>
<tr>
<td align="left"><strong>Rule IP prefix</strong></td>
<td align="left">The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as <code>160.168.0.1/24</code>. The maximum is 5,000 unique CIDR entries. To learn more and review an example, refer to the <a href="/network-flow/rules/#rule-ip-prefixes">Rule IP prefixes</a> section.</td>
</tr>
</tbody>
</table>
<h2 id="api-documentation">API documentation</h2>
<p>To review an example API configuration call using CURL and the expected output for a successful response, go to the <a href="/api/resources/magic_network_monitoring/subresources/rules/">Rules</a> section in the Network Flow API documentation.</p>
<h2 id="how-the-dynamic-rule-threshold-is-calculated">How the dynamic rule threshold is calculated</h2>
<p>Z-score compares short-term traffic patterns (five-minute window) against long-term baselines (four-hour window) to detect anomalies. The threshold adjusts automatically as your traffic history grows.</p>
<p>Z-Score is calculated by using the following formula:</p>
<pre tabindex="0"><code class="language-txt">Z = (X - μ) / σ&#10;</code></pre>
<ul>
<li><code>X</code> = Current traffic value.</li>
<li><code>μ</code> = Mean traffic value over the long window.</li>
<li><code>σ</code> = Standard deviation over the long window.</li>
</ul>
