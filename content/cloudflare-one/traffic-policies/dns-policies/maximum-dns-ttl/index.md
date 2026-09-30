---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/
  description: Set a maximum time-to-live (TTL) for DNS responses returned by Gateway to ensure policy changes propagate faster.
  full_title: Maximum DNS TTL · Cloudflare One docs
  head_html: <title>Maximum DNS TTL · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Set a maximum time-to-live (TTL) for DNS responses returned by Gateway to ensure policy changes propagate faster."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/index.md"><meta property="og:title" content="Maximum DNS TTL · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set a maximum time-to-live (TTL) for DNS responses returned by Gateway to ensure policy changes propagate faster."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/#page","headline":"Maximum DNS TTL \u00b7 Cloudflare One docs","description":"Set a maximum time-to-live (TTL) for DNS responses returned by Gateway to ensure policy changes propagate faster.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/
  schema: 1
---
<p>Set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps the TTL to the value you specify. Lower values ensure that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients, at the cost of increased query volume from reduced caching.</p>
<p>The maximum TTL cap only applies to upstream-derived DNS answers for allowed queries. Gateway-generated responses (blocks, overrides, safe-search answers) are not affected because they already use a short default TTL.</p>
<h2 id="how-it-works">How it works</h2>
<p>Gateway applies a tiered TTL hierarchy. The most specific setting takes precedence:</p>
<ol>
<li>If the DNS location has a per-location override, that value is used.</li>
<li>If the location inherits its setting, the account-level maximum TTL is used.</li>
<li>If no maximum TTL is configured at any level, upstream TTL values pass through unchanged.</li>
</ol>
<p>The valid range for any maximum TTL value is <strong>60 to 36,000 seconds</strong> (1 minute to 10 hours).</p>
<h2 id="configure-the-account-level-maximum-ttl">Configure the account-level maximum TTL</h2>
<p>The account-level setting applies to all DNS locations that do not have a per-location override.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6647.md")
</div></div>
<h2 id="configure-a-per-location-maximum-ttl">Configure a per-location maximum TTL</h2>
<p>Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can override the account-level setting. The per-location setting supports three modes:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Respect account-level setting</strong> (<code>inherit</code>)</td>
<td>Uses whatever value is configured at the account level. This is the default for new locations.</td>
</tr>
<tr>
<td><strong>Do not set max value</strong> (<code>disabled</code>)</td>
<td>Disables the maximum TTL cap for this location, even if one is configured at the account level. Upstream TTL values pass through unchanged.</td>
</tr>
<tr>
<td><strong>Custom</strong> (<code>override</code>)</td>
<td>Sets a location-specific maximum TTL that overrides the account-level value. Requires a <code>ttl_secs</code> value between 60 and 36,000.</td>
</tr>
</tbody>
</table>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6650.md")
</div></div>
<h2 id="dns-log-fields">DNS log fields</h2>
<p>When a maximum TTL is active, two additional fields appear in Gateway DNS logs:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>upstream_record_ttls</code></td>
<td>The original TTL values from the upstream DNS response, before any cap was applied.</td>
</tr>
<tr>
<td><code>applied_max_ttl</code></td>
<td>The maximum TTL value that Gateway applied to the response. If no cap was applied, this field is absent.</td>
</tr>
</tbody>
</table>
<p>These fields are visible in the DNS logs column picker under the <strong>DNS Response Details</strong> group in the dashboard, and in Logpush datasets.</p>
