---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing Billable Usage dashboard and Budget alerts · Changelog
  head_html: <title>Introducing Billable Usage dashboard and Budget alerts · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing Billable Usage dashboard and Budget alerts · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/#page","headline":"Introducing Billable Usage dashboard and Budget alerts \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 21, 2026</time><h2 id="post-title">Introducing Billable Usage dashboard and Budget alerts</h2>
<div class="changelog-badges"><span>fundamentals</span><span>workers</span></div><div class="changelog-body"><p>Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.</p>
<h4 id="billable-usage-dashboard">Billable Usage dashboard</h4>
<p>The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard displays:</p>
<ul>
<li>A bar chart showing daily usage charges for your billing period</li>
<li>A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs</li>
<li>Ability to view previous billing periods</li>
</ul>
<p>Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.</p>
<p>To access the dashboard, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-billable-usage-dashboard.png" alt="Screenshot of the Billable Usage dashboard in the Cloudflare dashboard" /></p>
<h4 id="budget-alerts">Budget alerts</h4>
<p>Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.</p>
<p>To configure a budget alert:</p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</li>
<li>Select <strong>Set Budget Alert</strong>.</li>
<li>Enter a budget threshold amount greater than $0.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>Alternatively, configure alerts via <strong>Notifications</strong> &gt; <strong>Add</strong> &gt; <strong>Budget Alert</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-budget-alert-modal.png" alt="Create Budget Alert modal in the Cloudflare dashboard" /></p>
<p>You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.</p>
<p>Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.</p>
<p>For more information, refer to the <a href="/billing/understand/usage-based-billing/">Usage based billing documentation</a>.</p>
</div></article></div>
