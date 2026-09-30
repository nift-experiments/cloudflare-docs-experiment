---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/
  description: Understand custom hostname quotas, monitor usage with the API, and determine which hostnames count toward billing.
  full_title: Quotas and billing · Cloudflare for Platforms docs
  head_html: <title>Quotas and billing · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand custom hostname quotas, monitor usage with the API, and determine which hostnames count toward billing."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/index.md"><meta property="og:title" content="Quotas and billing · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand custom hostname quotas, monitor usage with the API, and determine which hostnames count toward billing."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/#page","headline":"Quotas and billing \u00b7 Cloudflare for Platforms docs","description":"Understand custom hostname quotas, monitor usage with the API, and determine which hostnames count toward billing.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/
  schema: 1
---
<p>Cloudflare for SaaS plans include a number of custom hostnames. Additional hostnames are billed according to your plan. For included hostnames, maximum hostnames, and current usage pricing, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/plans/">Plans</a>.</p>
<h2 id="quota-behavior">Quota behavior</h2>
<p>Custom hostname quotas apply at either the zone or account level. A zone-level quota includes hostnames in one zone. An account-level quota includes hostnames across every zone in the account.</p>
<p>The assigned quota is a soft limit. When usage reaches this limit, you can continue creating custom hostnames. The <a href="/api/resources/custom_hostnames/methods/create/">Create Custom Hostname</a> response then includes a billing warning.</p>
<p>Non-Enterprise plans also have an API enforcement threshold. After usage reaches this threshold, the API rejects requests to create custom hostnames. Enterprise plans can continue to create custom hostnames after reaching this threshold.</p>
<p>The quota API returns current usage, the soft quota, and the enforcement threshold for the applicable scope.</p>
<h2 id="check-quota-usage">Check quota usage</h2>
<p>Send a <code>GET</code> request to the custom hostname quota endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames/quota&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>The response contains these quota fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>allocated</code></td>
<td>The operational soft quota for the zone or account.</td>
</tr>
<tr>
<td><code>used</code></td>
<td>The custom hostnames counted toward the allocation.</td>
</tr>
<tr>
<td><code>exceeded</code></td>
<td>Whether usage has reached or exceeded the allocation.</td>
</tr>
<tr>
<td><code>hard_cap</code></td>
<td>The API enforcement threshold for non-Enterprise plans. Enterprise plans can exceed this value.</td>
</tr>
</tbody>
</table>
<p>Use <code>used</code> and <code>allocated</code> to monitor operational capacity. The <code>exceeded</code> field becomes <code>true</code> when <code>used</code> is greater than or equal to <code>allocated</code>.</p>
<h2 id="billable-hostnames">Billable hostnames</h2>
<p>Each custom hostname counts toward usage until you delete it. This includes hostnames that are pending validation or activation. Deleting an unused custom hostname removes it from the usage count.</p>
