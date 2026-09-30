---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/
  description: The best sampling rate recommendations for your network's traffic volume.
  full_title: Recommended sampling rate · Cloudflare Network Flow docs
  head_html: <title>Recommended sampling rate · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="The best sampling rate recommendations for your network&#x27;s traffic volume."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/index.md"><meta property="og:title" content="Recommended sampling rate · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The best sampling rate recommendations for your network&#x27;s traffic volume."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Network Flow"><meta name="pcx_tags" content="NetFlow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/#page","headline":"Recommended sampling rate \u00b7 Cloudflare Network Flow docs","description":"The best sampling rate recommendations for your network's traffic volume.","url":"https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["NetFlow"]}</script>
  markdown: true
  noindex: false
  route: /network-flow/routers/recommended-sampling-rate/
  schema: 1
---
<p>Your router <span class="nb-glossary-tooltip" title="sampling">samples</span> the traffic that passes through it to create <span class="nb-glossary-tooltip" title="NetFlow">NetFlow</span> or <span class="nb-glossary-tooltip" title="sFlow">sFlow</span> data. The sampling rate determines how frequently your router captures a packet — for example, a rate of 1 in 100 means your router captures one out of every 100 packets.</p>
<p>Sampling more frequently (lower ratios like 1 in 100) produces more accurate flow data but uses more router memory and CPU. Sampling less frequently (higher ratios like 1 in 4,000) reduces resource usage and is suitable for networks with larger traffic volumes.</p>
<p>The following table provides general recommendations based on your traffic volume. Test different sampling rates to find the best option for your network.</p>
<table>
<thead>
<tr>
<th>Traffic Volume</th>
<th>Router sampling recommendation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Low</td>
<td>Between 1 in 100 packets - 1 in 500 packets</td>
</tr>
<tr>
<td>Medium</td>
<td>Between 1 in 1,000 - 1 in 2,000 packets</td>
</tr>
<tr>
<td>High</td>
<td>Between 1 in 2,000 - 1 in 4,000 packets</td>
</tr>
</tbody>
</table>
<p>As a general rule, you may notice a loss in data accuracy (depending on your network volume) when your network flow sampling rate exceeds 1 in 5,000 packets.</p>
