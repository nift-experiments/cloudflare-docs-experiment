---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/
  description: Monitor Logpush job health with alerts and analytics.
  full_title: Logpush alerts and analytics · Cloudflare Logs docs
  head_html: <title>Logpush alerts and analytics · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor Logpush job health with alerts and analytics."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/index.md"><meta property="og:title" content="Logpush alerts and analytics · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor Logpush job health with alerts and analytics."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/#page","headline":"Logpush alerts and analytics \u00b7 Cloudflare Logs docs","description":"Monitor Logpush job health with alerts and analytics.","url":"https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/alerts-and-analytics/
  schema: 1
---
<p>Logpush jobs may fail for a few reasons, for instance because the destination is unreachable, because of a change in permissions at the customers’ origin, or because a Logpush job did not complete at least one successful push in the last 24 hour.</p>
<p>With analytics and alerting, you can monitor your Logpush job health and find out for yourself when a job fails. You can get alerted and you can also get analytics about your Logpush jobs health via GraphQL.</p>
<p>Alerts are sent via the <a href="/notifications/">Cloudflare Notifications</a> system. They can be sent via email or webhook. When subscribed to job disablement notification, you will receive at most one alert per job per 24 hours. The notification email contains the job ID and destination configuration.</p>
<details><summary>Failing Logpush Job Disabled</summary><strong>Who is it for?</strong><p>Enterprise customers who use <a href="/logs/">Logpush</a> and want to monitor their job health.</p>
<strong>Other options / filters</strong><ul>
<li>Notification Name: A custom name for the notification.</li>
<li>Description (optional): A custom description for the notification.</li>
<li>Notification Email (can be multiple emails): The email address of the recipient for the notification.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>In the email for the notification, you can find the destination name for the failing Logpush job. With this destination name, you should be able to figure out which zone this relates to. There can be multiple reasons why a job fails, but it is best to test that the destination endpoint is healthy, and that necessary credentials are still working. You can also check that the destination has allowlisted <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>.</p>
</details>
<h2 id="enable-alerts">Enable alerts</h2>
<p>You can add an alert for <strong>Failing Logpush Job Disabled</strong> via the <strong>Notifications</strong> section of the dashboard. Note that alerts can be configured at the account level and apply to all jobs within an account.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next, select <strong>Add</strong>.</li>
<li>Select the alert <strong>Failing Logpush Job Disabled</strong>.</li>
<li>Configure the alert: choose a name, add a description (optional), select the notification services, Webhooks and enter the email where you want to be notified.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>When you complete these steps, you will receive an email alert if your Logpush job is disabled.</p>
<h2 id="enable-logpush-health-analytics">Enable Logpush health analytics</h2>
<p>Customers can query Logpush job health metrics via the <a href="/analytics/graphql-api/">GraphQL API</a>. The name of the dataset is <code>logpushHealthAdaptiveGroups</code> and the schema can be explored using the <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">GraphQL API</a>.</p>
<p>Here is a query to get the count of how many times jobs pushing to S3 failed.</p>
<pre tabindex="0"><code class="language-json">query&#10;{&#10;  viewer&#10;  {&#10;    zones(filter: { zoneTag: $zoneTag})&#10;    {&#10;      logpushHealthAdaptiveGroups(filter: {&#10;        datetime_gt:&quot;2022-08-15T00:00:00Z&quot;,&#10;        destinationType:&quot;s3&quot;,&#10;        status_neq:200&#10;      },&#10;      limit:10)&#10;      {&#10;        count,&#10;        dimensions {&#10;          jobId,&#10;          status,&#10;          destinationType&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10476.md")
</aside>
