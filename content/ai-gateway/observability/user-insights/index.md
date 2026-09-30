---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/observability/user-insights/
  description: Track organization-wide AI spend, attribute usage to identities, and detect anomalous sessions in AI Gateway.
  full_title: User Insights · Cloudflare AI Gateway docs
  head_html: <title>User Insights · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Track organization-wide AI spend, attribute usage to identities, and detect anomalous sessions in AI Gateway."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/observability/user-insights/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/observability/user-insights/index.md"><meta property="og:title" content="User Insights · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track organization-wide AI spend, attribute usage to identities, and detect anomalous sessions in AI Gateway."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/observability/user-insights/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/observability/user-insights/#page","headline":"User Insights \u00b7 Cloudflare AI Gateway docs","description":"Track organization-wide AI spend, attribute usage to identities, and detect anomalous sessions in AI Gateway.","url":"https://developers.cloudflare.com/ai-gateway/observability/user-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/observability/user-insights/
  schema: 1
---
<p>The User Insights dashboard shows how much your organization spends on AI, which identities are responsible for that spend, and which users deviate from their typical usage. It uses the traffic already flowing through your gateway, so there is no additional setup.</p>
<h2 id="attribute-usage-to-identities">Attribute usage to identities</h2>
<p>User Insights is available to all AI Gateway customers at no additional cost and works on any traffic through your gateway. Without an identity or custom metadata on your requests, all usage is grouped under a single anonymous identifier, and User Insights cannot distinguish between individual users.</p>
<p>To attribute usage to individual users, add a user identifier with <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a>, or put your gateway behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>. With Access, each authenticated request carries a verified identity you can filter spend and analytics by.</p>
<h2 id="key-metrics">Key metrics</h2>
<p>At the top of the User Insights page, you can view the following organization-wide metrics for the selected time range:</p>
<ul>
<li><strong>Active users</strong>: Identities with gateway usage.</li>
<li><strong>Total requests</strong>: Gateway requests in this range.</li>
<li><strong>Adoption rate</strong>: IdP identities with at least one request.</li>
<li><strong>Tokens per active user</strong>: Median over this time range.</li>
<li><strong>Median spend / active user</strong>: Observed spend per attributed identity.</li>
<li><strong>Top 10% request activity</strong>: Share of attributed requests made by the most active users.</li>
<li><strong>Users to review</strong>: Users whose cost is at least 2x the median spend.</li>
<li><strong>Identity coverage</strong>: Share of requests attributed to users.</li>
</ul>
<h2 id="anomaly-detection">Anomaly detection</h2>
<p>User Insights baselines each user's normal usage and flags sessions that fall outside it, which can indicate a compromised credential or a misbehaving agent.</p>
<p>Baselines are calculated per session, not per request. For each user, User Insights uses the 95th percentile (p95) session cost over the last 30 days. The baseline is rolling and updates as usage changes.</p>
<p>A session is flagged when it exceeds both of the following thresholds:</p>
<ul>
<li><strong>Relative</strong>: More than 2x the user's own p95 session cost.</li>
<li><strong>Absolute</strong>: Above the organization-level p99 session cost across all users.</li>
</ul>
<p>Both thresholds must be met. This avoids flagging small spikes from low-usage users and routine high-cost sessions from heavy users.</p>
<p>Flagged users appear in a filtered view with the sessions that triggered the flag and their cost. User Insights does not block requests.</p>
<h2 id="user-view">User view</h2>
<p>Select a user to see their usage in detail:</p>
<ul>
<li><strong>Spend</strong>: Total observed spend for the user in this range.</li>
<li><strong>Requests</strong>: Total gateway requests made by the user.</li>
<li><strong>Tokens</strong>: Total tokens consumed by the user.</li>
<li><strong>Gateway cached requests</strong>: Number of requests served from cache.</li>
<li><strong>Errored requests</strong>: Number of requests that returned an error.</li>
<li><strong>Cache hit rate</strong>: Share of requests served from cache.</li>
<li><strong>Sessions</strong>: Approximate session count from request metadata.</li>
<li><strong>Top model</strong>: The model the user sent the most requests to.</li>
<li><strong>Top provider</strong>: The provider the user sent the most requests to.</li>
<li><strong>Last seen</strong>: Most recent activity, from the daily spend trend.</li>
<li><strong>Active days</strong>: Number of days the user sent traffic in this range.</li>
<li><strong>Identity coverage</strong>: Share of the user's requests attributed to an identity.</li>
</ul>
