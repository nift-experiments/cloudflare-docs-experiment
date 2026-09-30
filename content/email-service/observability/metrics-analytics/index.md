---
cp9:
  canonical: https://developers.cloudflare.com/email-service/observability/metrics-analytics/
  description: Query Email Service sending metrics and delivery rates via the dashboard or GraphQL Analytics API.
  full_title: Metrics and analytics · Cloudflare Email Service docs
  head_html: <title>Metrics and analytics · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Email Service sending metrics and delivery rates via the dashboard or GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/email-service/observability/metrics-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/observability/metrics-analytics/index.md"><meta property="og:title" content="Metrics and analytics · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Email Service sending metrics and delivery rates via the dashboard or GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/email-service/observability/metrics-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/observability/metrics-analytics/#page","headline":"Metrics and analytics \u00b7 Cloudflare Email Service docs","description":"Query Email Service sending metrics and delivery rates via the dashboard or GraphQL Analytics API.","url":"https://developers.cloudflare.com/email-service/observability/metrics-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/observability/metrics-analytics/
  schema: 1
---
<p>Email Service exposes analytics that allow you to inspect email sending performance and delivery rates across all your domains.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>Email Service currently exposes the below metrics:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>GraphQL Dataset Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sending (aggregated)</td>
<td><code>emailSendingAdaptiveGroups</code></td>
<td>Aggregated email sending counts grouped by dimensions such as status, date, sending domain, and authentication results.</td>
</tr>
<tr>
<td>Sending (events)</td>
<td><code>emailSendingAdaptive</code></td>
<td>Individual email sending events with full detail including sender, recipient, subject, message ID, and error information.</td>
</tr>
<tr>
<td>Routing (aggregated)</td>
<td><code>emailRoutingAdaptiveGroups</code></td>
<td>Aggregated email routing counts grouped by dimensions such as status, date, recipient domain, and authentication results.</td>
</tr>
<tr>
<td>Routing (events)</td>
<td><code>emailRoutingAdaptive</code></td>
<td>Individual email routing events with full detail including sender, recipient, subject, message ID, and processing decisions.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-domain analytics for Email Service are available in the Cloudflare dashboard. To view current and historical metrics:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> and select <strong>Email Sending</strong> or <strong>Email Routing</strong>.</li>
<li>Select an existing domain or view account-wide metrics.</li>
<li>Select the <strong>Analytics</strong> tab.</li>
</ol>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your Email Service domains via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>To get started using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, follow the documentation to setup <a href="/analytics/graphql-api/getting-started/authentication/">Authentication for the GraphQL Analytics API</a>. Your API token must include the <strong>Analytics Read</strong> permission.</p>
<p>These are <strong>zone-level</strong> datasets. To query them, provide your zone ID (not account ID) as the <code>zoneTag</code> filter. The GraphQL datasets for Email Service include:</p>
<ul>
<li><code>emailSendingAdaptiveGroups</code> — aggregated email sending counts with groupable dimensions</li>
<li><code>emailSendingAdaptive</code> — individual email sending events</li>
<li><code>emailRoutingAdaptiveGroups</code> — aggregated email routing counts with groupable dimensions</li>
<li><code>emailRoutingAdaptive</code> — individual email routing events</li>
</ul>
<h3 id="email-sending-dimensions">Email Sending dimensions</h3>
<p>The <code>emailSendingAdaptiveGroups</code> dataset supports the following dimensions for grouping and filtering:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>date</code></td>
<td>Date</td>
<td>Day-level grouping</td>
</tr>
<tr>
<td><code>datetime</code></td>
<td>Time</td>
<td>Exact event timestamp</td>
</tr>
<tr>
<td><code>datetimeMinute</code></td>
<td>Time</td>
<td>Minute-level grouping</td>
</tr>
<tr>
<td><code>datetimeFiveMinutes</code></td>
<td>Time</td>
<td>5-minute interval grouping</td>
</tr>
<tr>
<td><code>datetimeFifteenMinutes</code></td>
<td>Time</td>
<td>15-minute interval grouping</td>
</tr>
<tr>
<td><code>datetimeHour</code></td>
<td>Time</td>
<td>Hour-level grouping</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>Delivery status (for example, <code>delivered</code>, <code>deliveryFailed</code>)</td>
</tr>
<tr>
<td><code>eventType</code></td>
<td>string</td>
<td>Origin of email (<code>incoming</code>, <code>forward</code>, <code>reply</code>, <code>newEmail</code>)</td>
</tr>
<tr>
<td><code>sendingDomain</code></td>
<td>string</td>
<td>The domain used to send the email</td>
</tr>
<tr>
<td><code>envelopeTo</code></td>
<td>string</td>
<td>Recipient envelope address</td>
</tr>
<tr>
<td><code>errorCause</code></td>
<td>string</td>
<td>Error cause for failed sends</td>
</tr>
<tr>
<td><code>arc</code></td>
<td>string</td>
<td>ARC authentication result</td>
</tr>
<tr>
<td><code>dkim</code></td>
<td>string</td>
<td>DKIM authentication result</td>
</tr>
<tr>
<td><code>dmarc</code></td>
<td>string</td>
<td>DMARC authentication result</td>
</tr>
<tr>
<td><code>spf</code></td>
<td>string</td>
<td>SPF authentication result</td>
</tr>
<tr>
<td><code>isSpam</code></td>
<td>uint8</td>
<td>Whether the email was flagged as spam</td>
</tr>
<tr>
<td><code>isNDR</code></td>
<td>uint8</td>
<td>Whether the email is a non-delivery report</td>
</tr>
<tr>
<td><code>isLastEvent</code></td>
<td>uint8</td>
<td>Whether this is the last event for this email</td>
</tr>
</tbody>
</table>
<p>The <code>emailSendingAdaptive</code> dataset includes all of the above plus per-event fields: <code>from</code>, <code>to</code>, <code>subject</code>, <code>messageId</code>, <code>sessionId</code>, <code>errorDetail</code>.</p>
<h3 id="email-routing-dimensions">Email Routing dimensions</h3>
<p>The <code>emailRoutingAdaptiveGroups</code> dataset supports the following dimensions for grouping and filtering:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>date</code></td>
<td>Date</td>
<td>Day-level grouping</td>
</tr>
<tr>
<td><code>datetime</code></td>
<td>Time</td>
<td>Exact event timestamp</td>
</tr>
<tr>
<td><code>datetimeMinute</code></td>
<td>Time</td>
<td>Minute-level grouping</td>
</tr>
<tr>
<td><code>datetimeFiveMinutes</code></td>
<td>Time</td>
<td>5-minute interval grouping</td>
</tr>
<tr>
<td><code>datetimeFifteenMinutes</code></td>
<td>Time</td>
<td>15-minute interval grouping</td>
</tr>
<tr>
<td><code>datetimeHour</code></td>
<td>Time</td>
<td>Hour-level grouping</td>
</tr>
<tr>
<td><code>status</code></td>
<td>string</td>
<td>Resulting outcome for the email</td>
</tr>
<tr>
<td><code>eventType</code></td>
<td>string</td>
<td>Origin of email (<code>incoming</code>, <code>forward</code>, <code>reply</code>, <code>newEmail</code>)</td>
</tr>
<tr>
<td><code>action</code></td>
<td>string</td>
<td>Action applied by the routing rule</td>
</tr>
<tr>
<td><code>ruleMatched</code></td>
<td>string</td>
<td>UUID of the routing rule matched by the email</td>
</tr>
<tr>
<td><code>arc</code></td>
<td>string</td>
<td>ARC authentication result</td>
</tr>
<tr>
<td><code>dkim</code></td>
<td>string</td>
<td>DKIM authentication result</td>
</tr>
<tr>
<td><code>dmarc</code></td>
<td>string</td>
<td>DMARC authentication result</td>
</tr>
<tr>
<td><code>spf</code></td>
<td>string</td>
<td>SPF authentication result</td>
</tr>
<tr>
<td><code>isSpam</code></td>
<td>uint8</td>
<td>Whether the email was flagged as spam</td>
</tr>
<tr>
<td><code>isNDR</code></td>
<td>uint8</td>
<td>Whether the email is a non-delivery report</td>
</tr>
<tr>
<td><code>isLastEvent</code></td>
<td>uint8</td>
<td>Whether this is the last event for this email</td>
</tr>
</tbody>
</table>
<p>The <code>emailRoutingAdaptive</code> dataset includes all of the above plus per-event fields: <code>from</code>, <code>to</code>, <code>subject</code>, <code>messageId</code>, <code>sessionId</code>, <code>errorDetail</code>, <code>ruleMatched</code>.</p>
<h3 id="examples">Examples</h3>
<p>The following are common GraphQL queries that you can use to retrieve information about Email Service analytics. These queries use the variable <code>$zoneTag</code>, which should be set to your Cloudflare Zone ID. You can find this in the Cloudflare dashboard under your domain's <strong>Overview</strong> page.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;zoneTag&quot;: &quot;&lt;YOUR_ZONE_ID&gt;&quot;,&#10;	&quot;start&quot;: &quot;2024-07-15&quot;,&#10;	&quot;end&quot;: &quot;2024-07-30&quot;&#10;}&#10;</code></pre>
<h4 id="email-sending-operations">Email sending operations</h4>
<p>To query the count of emails for a given date range, grouped by <code>date</code> and <code>status</code> (for example, <code>delivered</code>, <code>deliveryFailed</code>):</p>
<pre tabindex="0"><code class="language-graphql">query EmailSendingByStatus($zoneTag: string!, $start: Date!, $end: Date!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailSendingAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date&#10;					status&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="delivery-failure-analysis">Delivery failure analysis</h4>
<p>To investigate delivery failure causes for a specific date range, grouped by <code>errorCause</code> and <code>sendingDomain</code>:</p>
<pre tabindex="0"><code class="language-graphql">query EmailDeliveryFailures($zoneTag: string!, $start: Date!, $end: Date!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailSendingAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end, status: &quot;deliveryFailed&quot; }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date&#10;					errorCause&#10;					sendingDomain&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="hourly-volume">Hourly volume</h4>
<p>To query email sending volume grouped by hour, useful for identifying traffic patterns:</p>
<pre tabindex="0"><code class="language-graphql">query EmailSendingHourlyVolume($zoneTag: string!, $start: Time!, $end: Time!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailSendingAdaptiveGroups(&#10;				filter: { datetimeHour_geq: $start, datetimeHour_leq: $end }&#10;				limit: 10000&#10;				orderBy: [datetimeHour_ASC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					datetimeHour&#10;					status&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="individual-email-events">Individual email events</h4>
<p>To query individual email events for troubleshooting specific delivery issues. This uses the <code>emailSendingAdaptive</code> dataset and filters by <code>datetime</code> (Time type):</p>
<pre tabindex="0"><code class="language-graphql">query RecentEmailEvents($zoneTag: string!, $start: Time!, $end: Time!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailSendingAdaptive(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 50&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				datetime&#10;				from&#10;				to&#10;				subject&#10;				status&#10;				eventType&#10;				sendingDomain&#10;				messageId&#10;				errorCause&#10;				errorDetail&#10;				dkim&#10;				dmarc&#10;				spf&#10;				isSpam&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="email-routing-operations">Email routing operations</h4>
<p>To query the count of routed emails for a given date range, grouped by <code>date</code> and <code>status</code>:</p>
<pre tabindex="0"><code class="language-graphql">query EmailRoutingByStatus($zoneTag: string!, $start: Date!, $end: Date!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailRoutingAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date&#10;					status&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="routing-rule-activity">Routing rule activity</h4>
<p>To see which routing rules are matching emails, grouped by <code>ruleMatched</code> and <code>action</code>:</p>
<pre tabindex="0"><code class="language-graphql">query EmailRoutingRuleActivity($zoneTag: string!, $start: Date!, $end: Date!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailRoutingAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date&#10;					ruleMatched&#10;					action&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="individual-routing-events">Individual routing events</h4>
<p>To query individual routing events for troubleshooting:</p>
<pre tabindex="0"><code class="language-graphql">query RecentRoutingEvents($zoneTag: string!, $start: Time!, $end: Time!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			emailRoutingAdaptive(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 50&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				datetime&#10;				from&#10;				to&#10;				subject&#10;				status&#10;				action&#10;				ruleMatched&#10;				messageId&#10;				errorDetail&#10;				dkim&#10;				dmarc&#10;				spf&#10;				isSpam&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8589.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/observability/logs/">Email logs</a> — view individual email activity in the dashboard.</li>
<li><a href="/email-service/observability/audit-logs/">Audit logs</a> — track configuration changes.</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a> — full GraphQL API reference.</li>
</ul>
