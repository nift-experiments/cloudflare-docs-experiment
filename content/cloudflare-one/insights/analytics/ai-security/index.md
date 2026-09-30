---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/
  description: Reference information for AI security in Zero Trust analytics.
  full_title: AI security · Cloudflare One docs
  head_html: <title>AI security · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for AI security in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/index.md"><meta property="og:title" content="AI security · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for AI security in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/#page","headline":"AI security \u00b7 Cloudflare One docs","description":"Reference information for AI security in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics/ai-security/
  schema: 1
---
<p>The AI security report dashboard summarizes your organization's AI usage and potential security risks.</p>
<p>To view the AI security report dashboard:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select <strong>AI security report</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To populate the AI security report dashboard, you must have:</p>
<ul>
<li><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> enabled to inspect outbound HTTP and DNS traffic.</li>
<li>User traffic to SaaS AI applications (for example, ChatGPT or Gemini) sent through Cloudflare Gateway.</li>
<li><a href="/cloudflare-one/access-controls/ai-controls/">Model Context Protocol (MCP) servers</a> behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> policies.</li>
</ul>
<h2 id="available-insights">Available insights</h2>
<p>The AI security report dashboard includes the following panels and metrics:</p>
<ul>
<li><a href="#top-5-visited-ai-applications-by-user-count">Top 5 visited AI applications by user count</a></li>
<li><a href="#statuses-applied-to-ai-applications-by-application-count">Statuses applied to AI applications by application count</a></li>
<li><a href="#data-uploaded-to-artificial-intelligence-applications-by-status">Data uploaded to Artificial Intelligence applications by status</a></li>
<li><a href="#mcp-servers-behind-access-over-time">MCP servers behind Access over time</a></li>
<li><a href="#access-login-events-to-mcp-servers">Access login events to MCP servers</a></li>
</ul>
<h3 id="top-5-visited-ai-applications-by-user-count">Top 5 visited AI applications by user count</h3>
<p>Displays the most accessed AI tools in your organization and the number of users visiting each application in a time-series graph.<br />
Each bar represents user activity for a specific AI application (for example, ChatGPT or Gemini) over time.</p>
<p>Use this chart to monitor adoption trends and detect new or unauthorized AI tools being accessed.</p>
<h3 id="statuses-applied-to-ai-applications-by-application-count">Statuses applied to AI applications by application count</h3>
<p>Reports the total number of AI applications identified and their review statuses.<br />
Statuses include:</p>
<ul>
<li>Unreviewed — Applications not yet evaluated by administrators.</li>
<li>In Review — Applications currently under review for approval.</li>
<li>Unapproved — Applications that are restricted or blocked.</li>
<li>Approved — Applications explicitly permitted for organizational use.</li>
</ul>
<h3 id="data-uploaded-to-artificial-intelligence-applications-by-status">Data uploaded to Artificial Intelligence applications by status</h3>
<p>Reports the amount of data transferred to AI tools, broken down by review status (Unreviewed, In Review, Unapproved, Approved).<br />
Use this report to understand whether sensitive data is being sent to unapproved or unreviewed AI applications.</p>
<h3 id="mcp-servers-behind-access-over-time">MCP servers behind Access over time</h3>
<p>Displays the number of Model Context Protocol (MCP) servers protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> policies over time. Use this panel to verify that newly deployed MCP servers are protected.</p>
<h3 id="access-login-events-to-mcp-servers">Access login events to MCP servers</h3>
<p>Reports the number of login events to MCP servers protected by Access policies. Use this panel to identify unusual login patterns, such as spikes in access from unexpected users.</p>
