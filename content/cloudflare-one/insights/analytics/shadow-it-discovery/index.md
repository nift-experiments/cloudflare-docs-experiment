---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/
  description: Reference information for Shadow IT SaaS analytics in Zero Trust analytics.
  full_title: Shadow IT SaaS analytics · Cloudflare One docs
  head_html: <title>Shadow IT SaaS analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Shadow IT SaaS analytics in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/index.md"><meta property="og:title" content="Shadow IT SaaS analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Shadow IT SaaS analytics in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/#page","headline":"Shadow IT SaaS analytics \u00b7 Cloudflare One docs","description":"Reference information for Shadow IT SaaS analytics in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics/shadow-it-discovery/
  schema: 1
---
<p>Shadow IT SaaS analytics provides visibility into the SaaS applications your users are visiting. The dashboard aggregates data from Gateway HTTP traffic to track application usage across your organization. This information allows you to create identity and device-driven Cloudflare One policies to secure your users and data.</p>
<p>To access Shadow IT SaaS analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select <strong>Shadow IT: SaaS analytics</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To allow Cloudflare to discover shadow IT in your traffic, you must set up <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>
<h2 id="use-shadow-it-saas-analytics">Use Shadow IT SaaS analytics</h2>
<h3 id="1-review-applications"><ol>
<li>Review applications</li>
</ol></h3>
<p>The first step in using the Shadow IT SaaS analytics dashboard is to review applications in the <a href="/cloudflare-one/team-and-resources/app-library/">Application Library</a>. The App Library synchronizes application review statuses with approval statuses from the Shadow IT Discovery SaaS analytics dashboard.</p>
<p>To organize applications into their approval status for your organization, you can mark them as <strong>Unreviewed</strong> (default), <strong>In review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong>.</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>API value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Approved</td>
<td><code>approved</code></td>
<td>Applications that have been marked as sanctioned by your organization.</td>
</tr>
<tr>
<td>Unapproved</td>
<td><code>unapproved</code></td>
<td>Applications that have been marked as unsanctioned by your organization.</td>
</tr>
<tr>
<td>In review</td>
<td><code>in review</code></td>
<td>Applications in the process of being reviewed by your organization.</td>
</tr>
<tr>
<td>Unreviewed</td>
<td><code>unreviewed</code></td>
<td>Unknown applications that are neither sanctioned nor being reviewed by your organization at this time.</td>
</tr>
</tbody>
</table>
<p>To set the status of an application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the card for the application.</li>
<li>In the three-dot menu, select the option to mark your desired status.</li>
</ol>
<p>Once you mark the status of an application, its badge will change. You can filter applications by their status to review each application in the list for your organization. The review status for an application in the App Library and Shadow IT Discovery will update within one hour.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4972.md")
</aside>
<h3 id="2-monitor-usage"><ol start="2">
<li>Monitor usage</li>
</ol></h3>
<p>Review the Shadow IT SaaS analytics dashboard for application usage. Filter the view based on:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>SaaS application's name and logo.</td>
</tr>
<tr>
<td>Application type</td>
<td><a href="/cloudflare-one/traffic-policies/application-app-types/#app-types">Application type</a> assigned by Cloudflare One.</td>
</tr>
<tr>
<td>Application status</td>
<td>Application's approval status.</td>
</tr>
<tr>
<td>Hostname</td>
<td>Hostname of the requested SaaS application.</td>
</tr>
<tr>
<td>Country</td>
<td>Country code associated with the user's source IP address.</td>
</tr>
</tbody>
</table>
<p>To manage application statuses in bulk, select <strong>Set Application Statuses</strong> to review applications your users commonly visit and update their approval statuses.</p>
<h3 id="3-create-policies"><ol start="3">
<li>Create policies</li>
</ol></h3>
<p>After marking applications, you can create <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> based on application review status. For example, you can create policies that:</p>
<ul>
<li>Launch all <strong>Unreviewed</strong> and <strong>In review</strong> applications in an <a href="/cloudflare-one/traffic-policies/http-policies/common-policies/#1-isolate-unreviewed-or-in-review-applications">isolated browser</a>.</li>
<li><a href="/cloudflare-one/traffic-policies/http-policies/common-policies/#2-block-unapproved-applications">Block access</a> to all <strong>Unapproved</strong> applications.</li>
<li>Limit file upload capabilities for specific application statuses.</li>
</ul>
<p>To create an HTTP status policy directly from Shadow IT Discovery:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Select <strong>Dashboards</strong> &gt; <strong>Shadow IT: SaaS analytics</strong>.</li>
<li>Select <strong>Set application statuses</strong>.</li>
<li>Select <strong>Manage HTTP status policies</strong>, then choose an application status and select <strong>Create policy</strong>.</li>
</ol>
<h2 id="available-insights">Available insights</h2>
<p>The Shadow IT SaaS analytics dashboard includes several insights to help you monitor and manage SaaS application usage.</p>
<ul>
<li><strong>Number of applications by status</strong>: A breakdown of how many applications have been categorized into each <a href="#1-review-applications">approval status</a>. The list of applications is available in the <a href="/cloudflare-one/team-and-resources/app-library/">App Library</a>.</li>
<li><strong>Data uploaded per application status</strong>: A time-series graph showing the amount of data uploaded to applications in the given status.</li>
<li><strong>Data downloaded per application status</strong>: A time-series graph showing the amount of data downloaded from applications in the given status.</li>
<li><strong>User count per application status</strong>: A time-series graph showing the number of unique users who have interacted with at least one application in a given status. A single user can appear in multiple status categories if they access applications with different statuses. For example, a user who accesses both an <strong>Approved</strong> application and an <strong>Unapproved</strong> application will be counted in both status categories.</li>
<li><strong>Top-N metrics</strong>: A collection of metrics providing insights into top applications, users, devices, and countries.</li>
</ul>
<h3 id="understanding-user-counts">Understanding user counts</h3>
<p>The user count chart displays unique users in two ways:</p>
<ul>
<li><strong>Time-series bars</strong>: Show unique users per time interval (for example, per hour or per day). The same user can appear in multiple time intervals if they were active during those periods.</li>
<li><strong>Legend totals</strong>: Show unique users across the entire selected time range, deduplicated. Each user is counted only once per status, regardless of how many time intervals they appeared in.</li>
</ul>
<p>For example, if User A accesses an Approved application every hour for three hours, they will appear in each hourly bar but will only be counted once in the legend total.</p>
