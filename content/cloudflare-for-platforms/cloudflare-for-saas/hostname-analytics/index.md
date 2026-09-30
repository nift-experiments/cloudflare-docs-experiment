---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/
  description: View per-hostname analytics for traffic, bots, cache, and security events.
  full_title: Analytics · Cloudflare for Platforms docs
  head_html: <title>Analytics · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="View per-hostname analytics for traffic, bots, cache, and security events."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/index.md"><meta property="og:title" content="Analytics · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View per-hostname analytics for traffic, bots, cache, and security events."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="Analytics,GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/#page","headline":"Analytics \u00b7 Cloudflare for Platforms docs","description":"View per-hostname analytics for traffic, bots, cache, and security events.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics","GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/
  schema: 1
---
<p>You can use custom hostname analytics for two general purposes: exploring how your customers use your product and sharing the benefits provided by Cloudflare with your customers.</p>
<p>These analytics include <strong>Site Analytics</strong>, <strong>Bot Analytics</strong>, <strong>Cache Analytics</strong>, <strong>Security Events</strong>, and <a href="/analytics/graphql-api/features/data-sets/">any other datasets</a> with the <code>clientRequestHTTPHost</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4069.md")
</aside>
<h2 id="explore-customer-usage">Explore customer usage</h2>
<p>Use custom hostname analytics to help your organization with billing and infrastructure decisions, answering questions like:</p>
<ul>
<li>&quot;How many total requests is your service getting?&quot;</li>
<li>&quot;Is one customer transferring significantly more data than the others?&quot;</li>
<li>&quot;How many global customers do you have and where are they distributed?&quot;</li>
</ul>
<p>If you see one customer is using more data than another, you might increase their bill. If requests are increasing in a certain geographic region, you might want to increase the origin servers in that region.</p>
<p>To access custom hostname analytics, either <a href="/analytics/faq/about-analytics/">use the dashboard</a> and filter by the <code>Host</code> field or <a href="/analytics/graphql-api/">use the GraphQL API</a> and filter by the <code>clientRequestHTTPHost</code> field. For more details, refer to our tutorial on <a href="/analytics/graphql-api/tutorials/end-customer-analytics/">Querying HTTP events by hostname with GraphQL</a>.</p>
<h2 id="share-cloudflare-data-with-your-customers">Share Cloudflare data with your customers</h2>
<p>With custom hostname analytics, you can also share site information with your customers, including data about:</p>
<ul>
<li>How many pageviews their site is receiving.</li>
<li>Whether their site has a large percentage of bot traffic.</li>
<li>How fast their site is.</li>
</ul>
<p>Build custom dashboards to share this information by specifying an individual custom hostname in <code>clientRequestHTTPHost</code> field of <a href="/analytics/graphql-api/features/data-sets/">any dataset</a> that includes this field.</p>
<h2 id="logpush">Logpush</h2>
<p><a href="/logs/logpush/">Logpush</a> sends metadata from Cloudflare products to your cloud storage destination or SIEM.</p>
<p>Using <a href="/logs/logpush/logpush-job/filters/">filters</a>, you can send set sample rates (or not include logs altogether) based on filter criteria. This flexibility allows you to maintain selective logs for custom hostnames without massively increasing your log volume.</p>
<p>Filtering is available for <a href="/logs/logpush/logpush-job/datasets/zone/">all Cloudflare datasets</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/4068.md")
</aside>
