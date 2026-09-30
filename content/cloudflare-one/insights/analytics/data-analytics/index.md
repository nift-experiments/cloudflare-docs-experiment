---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/
  description: Reference information for Data security analytics in Zero Trust analytics.
  full_title: Data security analytics · Cloudflare One docs
  head_html: <title>Data security analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Data security analytics in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/index.md"><meta property="og:title" content="Data security analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Data security analytics in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/#page","headline":"Data security analytics \u00b7 Cloudflare One docs","description":"Reference information for Data security analytics in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics/data-analytics/
  schema: 1
---
<p>The Data security analytics dashboard reports security issues and sensitive data found within your SaaS applications, cloud environments, and HTTP traffic. It combines Cloud Access Security Broker (CASB) findings with activity from Data Loss Prevention (DLP) policies. If neither DLP policies nor CASB integrations are configured in your account, the dashboard appears empty.</p>
<p>To view the Data security analytics dashboard:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select <strong>Data security analytics</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To populate this dashboard with partial data, you need at least one of the following:</p>
<ul>
<li>At least one HTTP policy that references a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">DLP profile</a>.</li>
<li>At least one SaaS integration enrolled in <a href="/cloudflare-one/integrations/cloud-and-saas/">CASB</a>.</li>
<li>At least one Cloud integration enrolled in <a href="/cloudflare-one/integrations/cloud-and-saas/">CASB</a>.</li>
<li>At least one SaaS or Cloud integration enrolled in <a href="/cloudflare-one/integrations/cloud-and-saas/">CASB</a> and a DLP profile applied to it.</li>
</ul>
<p>To learn which sensitive data types appear in your Gateway traffic before creating a DLP policy, use <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection</a>. It shows sampled detections separately from the policy activity on this dashboard.</p>
<h2 id="available-insights">Available insights</h2>
<p>The dashboard includes the following panels and metrics:</p>
<ul>
<li><a href="/cloudflare-one/insights/analytics/data-analytics/#saas-and-cloud-findings-by-count">SaaS and Cloud findings by count</a></li>
<li><a href="/cloudflare-one/insights/analytics/data-analytics/#posture-findings-by-severity">Posture findings by Severity</a></li>
<li><a href="/cloudflare-one/insights/analytics/data-analytics/#dlp-matches-in-http-requests-over-time">DLP matches in HTTP requests over time</a></li>
<li>Top integrations by posture findings</li>
<li>Top integrations by content findings</li>
<li>Top cloud resources by findings</li>
<li>Top users by DLP policies triggered</li>
</ul>
<h3 id="saas-and-cloud-findings-by-count">SaaS and Cloud findings by count</h3>
<p>The SaaS and Cloud findings by count chart shows a time series view of Posture and Content findings. <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#posture-findings">Posture findings</a> are configuration and access issues detected by CASB, such as misconfigurations, unauthorized user activity, and other data security issues. <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#content-findings">Content findings</a> are instances of potential data exposure as identified by <a href="/cloudflare-one/data-loss-prevention/">DLP</a>.</p>
<p>Each bar represents the total number of findings detected within a given time interval. You can use this view to observe patterns or spikes in findings over time. Hover over any bar to view the exact count of Posture and Content findings for that period.</p>
<p>To review findings in detail, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong> or <strong>Content Findings</strong>.</p>
<h3 id="posture-findings-by-severity">Posture findings by Severity</h3>
<p>The Posture findings by severity chart displays the distribution of CASB findings based on their <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity levels</a>. Each segment of the circle represents the number of posture issues classified as <code>Critical</code>, <code>High</code>, <code>Medium</code>, or <code>Low</code>.</p>
<p>To review findings in detail, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</p>
<h3 id="dlp-matches-in-http-requests-over-time">DLP matches in HTTP requests over time</h3>
<p>The DLP matches in HTTP requests over time chart displays when <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">DLP policies</a> were triggered by users over a specified period of time.</p>
<p>Unlike the SaaS and Cloud findings by count chart, which shows CASB findings from data at rest (files already stored in your connected SaaS applications), the DLP matches in HTTP requests over time chart shows DLP detections in HTTP traffic — data actively moving through your network.</p>
<p>To review DLP detections in detail, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP request logs</strong>. Use the <strong>DLP profiles</strong> or <strong>DLP match data</strong> filters to view HTTP requests that triggered a DLP policy.</p>
