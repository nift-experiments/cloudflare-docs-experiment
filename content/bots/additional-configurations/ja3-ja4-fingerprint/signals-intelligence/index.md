---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/
  description: View aggregate intelligence data for JA4 fingerprints across Cloudflare traffic.
  full_title: Signals Intelligence · Cloudflare bot solutions docs
  head_html: <title>Signals Intelligence · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="View aggregate intelligence data for JA4 fingerprints across Cloudflare traffic."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/index.md"><meta property="og:title" content="Signals Intelligence · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View aggregate intelligence data for JA4 fingerprints across Cloudflare traffic."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/#page","headline":"Signals Intelligence \u00b7 Cloudflare bot solutions docs","description":"View aggregate intelligence data for JA4 fingerprints across Cloudflare traffic.","url":"https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/ja3-ja4-fingerprint/signals-intelligence/
  schema: 1
---
<p>Bot Management customers can view aggregate intelligence data for each <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA4 fingerprint</a> based on traffic across the Cloudflare network. Use this data to understand why a request received a specific bot score or to feed into your own machine learning models running in <a href="/workers/">Cloudflare Workers</a> or at your origin.</p>
<p>Specifically, for each JA4 fingerprint, you will be able to access the following information:</p>
<ul>
<li>The percentage of traffic associated with browsers that Cloudflare sees.</li>
<li>The percentage of traffic associated with known bots that Cloudflare sees.</li>
<li>The number of networks Cloudflare sees actively using this fingerprint.</li>
<li>The number of Cloudflare sites that see traffic from this fingerprint.</li>
<li>The frequency that fingerprint requests caches content and generates errors.</li>
</ul>
<p>You can also use these fields with <a href="/workers-ai/">Workers AI</a> to build custom machine learning models.</p>
<h2 id="signals-intelligence-fields">Signals Intelligence fields</h2>
<p>Signals Intelligence fields show observations about a particular JA4 that Cloudflare has seen globally over the last hour.</p>
<table>
<thead>
<tr>
<th><span style="width:170px">Field name</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>h2h3_ratio_1h</code></td>
<td>The ratio of HTTP/2 and HTTP/3 requests combined with the total number of requests for the JA4 fingerprint in the last hour. Higher values indicate a higher proportion of HTTP/2 and HTTP/3 requests compared to other protocol versions.</td>
</tr>
<tr>
<td><code>heuristic_ratio_1h</code></td>
<td>The ratio of requests with a <code>scoreSrc</code> value of &quot;heuristics&quot; for the JA4 fingerprint in the last hour. Higher values suggest a larger proportion of requests being flagged by heuristic-based scoring.</td>
</tr>
<tr>
<td><code>reqs_quantile_1h</code></td>
<td>The quantile position of the JA4 fingerprint based on the number of requests across all fingerprints in the last hour. Higher values indicate a relatively higher number of requests compared to other fingerprints.</td>
</tr>
<tr>
<td><code>uas_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of distinct user agents across all fingerprints in the last hour. Lower values indicate a higher diversity of user agents associated with the fingerprint.</td>
</tr>
<tr>
<td><code>browser_ratio_1h</code></td>
<td>The ratio of requests originating from browser-based user agents for the JA4 fingerprint in the last hour. Higher values suggest a higher proportion of browser-based requests.</td>
</tr>
<tr>
<td><code>paths_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of unique request paths across all fingerprints in the last hour. Lower values indicate a higher diversity of request paths associated with the fingerprint.</td>
</tr>
<tr>
<td><code>reqs_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of requests across all fingerprints in the last hour. Lower values indicate a higher number of requests associated with the fingerprint.</td>
</tr>
<tr>
<td><code>cache_ratio_1h</code></td>
<td>The ratio of cacheable responses for the JA4 fingerprint in the last hour. Higher values suggest a higher proportion of responses that can be cached.</td>
</tr>
<tr>
<td><code>ips_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of unique client IP addresses across all fingerprints in the last hour. Lower values indicate a higher number of distinct client IPs associated with the fingerprint.</td>
</tr>
<tr>
<td><code>ips_quantile_1h</code></td>
<td>The quantile position of the JA4 fingerprint based on the number of unique client IP addresses across all fingerprints in the last hour. Higher values indicate a relatively higher number of distinct client IPs compared to other fingerprints.</td>
</tr>
</tbody>
</table>
<p>If you want to use JA4 fingerprints and Signals Intelligence, your Workers script should be able to handle missing fields when Bot Management isn't able to calculate or populate JA4 Signals (for example, non-TLS traffic or when Bot Management is skipped). For Orange-to-Orange (O2O) scenarios where Bot Management is in effect, JA4 Signals correspond to the eyeball (end-user) connection and are preserved through the O2O chain, including O2O zone requests and any corresponding subrequests.</p>
<ul>
<li>The possibility that the JA4 fingerprint could be missing.</li>
<li>The possibility that the <code>ja4Signals</code> array could be missing (for example, if JA4 isn't available for the request).</li>
<li>Results with <code>NaN</code> or <code>Infinity</code> values will be excluded from the array.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3542.md")
</aside>
