---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/reference/limits/
  description: Review AI Gateway limits for gateways, log storage, cache size, metadata entries, and Logpush jobs.
  full_title: Limits · Cloudflare AI Gateway docs
  head_html: <title>Limits · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Review AI Gateway limits for gateways, log storage, cache size, metadata entries, and Logpush jobs."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/reference/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/reference/limits/index.md"><meta property="og:title" content="Limits · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review AI Gateway limits for gateways, log storage, cache size, metadata entries, and Logpush jobs."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/reference/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/reference/limits/#page","headline":"Limits \u00b7 Cloudflare AI Gateway docs","description":"Review AI Gateway limits for gateways, log storage, cache size, metadata entries, and Logpush jobs.","url":"https://developers.cloudflare.com/ai-gateway/reference/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/reference/limits/
  schema: 1
---
<p>The following limits apply to gateway configurations, logs, and related features in Cloudflare's platform.</p>
<h2 id="gateway-and-log-limits">Gateway and log limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-gateway/features/caching/">Cacheable request size</a></td>
<td>25 MB per request</td>
</tr>
<tr>
<td><a href="/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl">Cache TTL</a></td>
<td>1 month</td>
</tr>
<tr>
<td><a href="/ai-gateway/observability/custom-metadata/">Custom metadata</a></td>
<td>5 entries per request</td>
</tr>
<tr>
<td><a href="/ai-gateway/evaluations/set-up-evaluations/">Datasets</a></td>
<td>10 per gateway</td>
</tr>
<tr>
<td>Gateways free plan</td>
<td>10 per account</td>
</tr>
<tr>
<td>Gateways paid plan</td>
<td>20 per account</td>
</tr>
<tr>
<td>Gateway name length</td>
<td>64 characters</td>
</tr>
<tr>
<td>Log storage rate limit</td>
<td>500 logs per second per gateway</td>
</tr>
<tr>
<td><a href="/ai-gateway/features/unified-billing/">Unified Billing</a> request rate</td>
<td>200 requests per 60 seconds per gateway <sup>4</sup></td>
</tr>
<tr>
<td>Logs stored <a href="/ai-gateway/reference/pricing/">paid plan</a></td>
<td>10 million per gateway <sup>1</sup></td>
</tr>
<tr>
<td>Logs stored <a href="/ai-gateway/reference/pricing/">free plan</a></td>
<td>100,000 per account <sup>2</sup></td>
</tr>
<tr>
<td><a href="/ai-gateway/observability/logging/">Log size stored</a></td>
<td>10 MB per log <sup>3</sup></td>
</tr>
<tr>
<td><a href="/ai-gateway/observability/logging/logpush/">Logpush jobs</a></td>
<td>4 per account</td>
</tr>
<tr>
<td><a href="/ai-gateway/observability/logging/logpush/">Logpush size limit</a></td>
<td>1MB per log</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> When you reach the log storage limit for a gateway, you can
configure your gateway to either automatically delete the oldest logs to make
room for new ones, or stop saving new logs. You can also use
<a href="/ai-gateway/observability/logging/logpush/">Logpush</a> to export logs to
external storage. Refer to <a href="/ai-gateway/observability/logging/#automatic-log-deletion">Automatic log deletion</a>
for more details.</p>
<p><sup>2</sup> On the free plan, the log storage limit applies to total logs across all gateways in your account. Same auto-delete or stop-saving behavior as <sup>1</sup>.</p>
<p><sup>3</sup> Logs larger than 10 MB will not be stored.</p>
<p><sup>4</sup> This rate limit applies to requests that use Cloudflare-managed credentials through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>. When the limit is exceeded, AI Gateway returns a <code>429</code> error. This limit does not apply to requests that use your own provider keys through <a href="/ai-gateway/configuration/bring-your-own-keys/">bring your own keys (BYOK)</a>.</p>
<h2 id="dlp-limits">DLP limits</h2>
<p><a href="/ai-gateway/features/dlp/">DLP</a> for AI Gateway uses shared <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Cloudflare One DLP profiles</a>. The following limits apply to DLP profiles and detection entries at the account level:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Custom entries</td>
<td>25</td>
</tr>
<tr>
<td>Exact Data Match cells per spreadsheet</td>
<td>100,000</td>
</tr>
<tr>
<td>Custom Wordlist keywords per spreadsheet</td>
<td>200</td>
</tr>
<tr>
<td>Custom Wordlist keywords per account</td>
<td>1,000</td>
</tr>
<tr>
<td>Dataset cells per account</td>
<td>1,000,000</td>
</tr>
</tbody>
</table>
<p>DLP profiles are shared with Cloudflare One and are not coupled to individual gateways. You can apply the same DLP profiles across multiple gateways without additional profile limits. There is no separate limit on the number of DLP policies per gateway.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/2797.md")
</aside>
