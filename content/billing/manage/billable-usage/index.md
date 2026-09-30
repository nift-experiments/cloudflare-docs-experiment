---
cp9:
  canonical: https://developers.cloudflare.com/billing/manage/billable-usage/
  description: Track daily usage-based costs across products.
  full_title: Monitor billable usage · Cloudflare Billing docs
  head_html: <title>Monitor billable usage · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Track daily usage-based costs across products."><link rel="canonical" href="https://developers.cloudflare.com/billing/manage/billable-usage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/manage/billable-usage/index.md"><meta property="og:title" content="Monitor billable usage · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track daily usage-based costs across products."><meta property="og:url" content="https://developers.cloudflare.com/billing/manage/billable-usage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/manage/billable-usage/#page","headline":"Monitor billable usage \u00b7 Cloudflare Billing docs","description":"Track daily usage-based costs across products.","url":"https://developers.cloudflare.com/billing/manage/billable-usage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/manage/billable-usage/
  schema: 1
---
<p>The billable usage dashboard gives you daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard shows usage-based overage charges only. Fixed-fee plan subscriptions (for example, a Pro plan) are not included.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3443.md")
</aside>
<h2 id="access-the-dashboard">Access the dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3444.md")
</div>
<h2 id="cost-breakdown-chart">Cost breakdown chart</h2>
<p>The bar chart at the top of the dashboard displays your daily usage charges for the selected billing period. Each bar is stacked by product, so you can identify which products are driving spend and when spending patterns change.</p>
<p>Hover over any bar to see the per-product cost breakdown for that day.</p>
<h2 id="product-usage-table">Product usage table</h2>
<p>Below the chart, a sortable table breaks down usage by product for the full billing period.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Product</strong></td>
<td>The Cloudflare product or service generating the usage charge. Products with a free tier show the included allowance (for example, &quot;First 1M included&quot;).</td>
</tr>
<tr>
<td><strong>Total usage</strong></td>
<td>Total metered usage for the billing period, including any free-tier allowance.</td>
</tr>
<tr>
<td><strong>Billable usage</strong></td>
<td>Usage that exceeds the free tier and will be charged.</td>
</tr>
<tr>
<td><strong>Usage cost</strong></td>
<td>Cumulative cost for the product in the selected billing period.</td>
</tr>
</tbody>
</table>
<h2 id="filter-usage-by-product-family-or-product">Filter usage by product family or product</h2>
<p>Use the filters sidebar to narrow the dashboard to a subset of products.</p>
<ul>
<li><strong>Product family</strong> — Group products by family (for example, Workers or R2) to compare costs across related usage metrics.</li>
<li><strong>Product</strong> — Filter to specific usage metrics. The list of available products narrows based on the families you select.</li>
</ul>
<p>Applied filters scope the cost breakdown chart, product usage table, and summary totals to your selection. On mobile, the sidebar opens as a drawer with an <strong>Apply</strong> action. Select <strong>Reset</strong> to clear all filters.</p>
<h2 id="select-a-billing-period">Select a billing period</h2>
<p>By default, the dashboard shows data for your current billing period. Use the date picker to view a previous billing period.</p>
<p>Usage data is aligned to your billing cycle, not the calendar month. Your billing period start date is determined by the first purchase date on your account.</p>
<h2 id="switch-between-subscriptions">Switch between subscriptions</h2>
<p>In rare cases, an account has more than one usage-based subscription — usually because a previous subscription was replaced. If this applies to your account, a <strong>Subscription</strong> filter appears in the sidebar, with each subscription labeled by its start date.</p>
<p>Selecting a different subscription scopes the chart, product usage table, and available billing periods to that subscription's data. Each subscription has its own billing cycle.</p>
<h2 id="data-alignment-with-your-invoice">Data alignment with your invoice</h2>
<p>The dashboard reads from the same data source that generates your monthly invoice.</p>
<ul>
<li>Costs reflect the published rate card for your account.</li>
<li>The total usage cost shown at the end of a completed billing period matches the usage overage charges on the corresponding invoice.</li>
</ul>
<h2 id="set-up-budget-alerts">Set up budget alerts</h2>
<p>To get notified when your spend crosses a dollar threshold, you can create budget alerts directly from the dashboard. For detailed instructions, refer to <a href="/billing/manage/budget-alerts/">Budget alerts</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/budget-alerts/">Budget alerts</a> — Get notified when spend crosses a threshold</li>
<li><a href="/billing/understand/usage-based-billing/">Usage-based billing</a> — Which products use metered billing</li>
<li><a href="/billing/understand/how-charges-accrue/">How charges accrue</a> — How a request generates charges across products</li>
</ul>
