---
cp9:
  canonical: https://developers.cloudflare.com/waf/analytics/security-events/
  description: Review individual security events triggered by WAF rules.
  full_title: Security Events · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Security Events · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Review individual security events triggered by WAF rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/analytics/security-events/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/analytics/security-events/index.md"><meta property="og:title" content="Security Events · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review individual security events triggered by WAF rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/analytics/security-events/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Logging,SIEM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/analytics/security-events/#page","headline":"Security Events \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Review individual security events triggered by WAF rules.","url":"https://developers.cloudflare.com/waf/analytics/security-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging","SIEM"]}</script>
  markdown: true
  noindex: false
  route: /waf/analytics/security-events/
  schema: 1
---
<p>Security Events allows you to review <span class="nb-glossary-tooltip" title="mitigated request">mitigated requests</span> and helps you tailor your security configurations. Use Security Events to investigate requests that Cloudflare security products acted on or flagged, identify false positives, and fine-tune your security rules.</p>
<p>If you want to analyze all incoming traffic, including requests that Cloudflare did not act on, refer to <a href="/waf/analytics/security-analytics/">Security Analytics</a> instead.</p>
<p>The main elements of the dashboard are the following:</p>
<ul>
<li><a href="#events-summary">Events summary</a>: Provides the number of security events on traffic during the selected time period, grouped according to the selected dimension (for example, Action, Host, Country).</li>
<li><a href="#events-by-service">Events by service</a>: Lists the security-related activity per security feature (for example, WAF, API Shield).</li>
<li><a href="#top-events-by-source">Top events by source</a>: Provides details of the traffic flagged or actioned by a Cloudflare security feature (for example, IP addresses, User Agents, Paths, Countries, Hosts, ASNs).</li>
<li><a href="#sampled-logs">Sampled logs</a>: Summarizes security events by date to show the action taken and the applied Cloudflare security product.</li>
</ul>
<p>Security Events displays information about requests actioned or flagged by Cloudflare security products, including features such as <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a>. A single HTTP request can generate one or more security events when it triggers security features. The Security Events dashboard shows these individual events, not the HTTP requests themselves.</p>
<h2 id="availability">Availability</h2>
<p>Available features vary according to your Cloudflare plan:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Dashboard features</td>
<td>Sampled logs only</td>
<td>All</td>
<td>All</td>
<td>All</td>
</tr>
<tr>
<td>Account-level dashboard</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Historical time (data retention)</td>
<td>Up to the last 24 hours</td>
<td>Up to the last 24 hours</td>
<td>Up to the last 3 days</td>
<td>Up to the last 30 days</td>
</tr>
<tr>
<td>Max query window</td>
<td>24 hours</td>
<td>24 hours</td>
<td>3 days</td>
<td>31 days</td>
</tr>
<tr>
<td>Export report</td>
<td>No</td>
<td>No</td>
<td>Up to 500 events</td>
<td>Up to 500 events</td>
</tr>
<tr>
<td>Print report</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="location-in-the-dashboard">Location in the dashboard</h2>
<p>To open Security Events for a given zone:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Events</strong> tab.</li>
</ol>
<p>Additionally, Enterprise customers have access to the account-level dashboard:</p>
<div class="nb-dash-button"></div>
<h2 id="adjust-displayed-data">Adjust displayed data</h2>
<p>You can apply multiple filters and exclusions to narrow the scope of Security Events and adjust the report duration. Modifying the duration, filters, or exclusions affects the analytics data displayed on the entire page including <strong>Sampled logs</strong> and all graphs.</p>
<p><img src="/assets/upstream/images/waf/events-add-filter.png" alt="Example of adding a new filter in Security Events for the Block action" /></p>
<h3 id="add-filters">Add filters</h3>
<p>You can adjust the scope of analytics by manually entering filter conditions. Alternatively, select <strong>Filter</strong> or <strong>Exclude</strong> to filter by a field value. These buttons appear when you hover the analytics data legend.</p>
<p>To manually add a filter:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15403.md")
</div>
<p>Take the following into account when entering filter values:</p>
<ul>
<li>Do not add quotes around values.</li>
<li>Do not enter the <code>AS</code> prefix when entering ASN numbers. For example, enter <code>1423</code> instead of <code>AS1423</code>.</li>
<li>Wildcards are not supported.</li>
</ul>
<h3 id="adjust-report-duration">Adjust report duration</h3>
<p>To adjust report duration, select the desired duration from the dropdown. The default value is <code>Last 24 hours</code>.</p>
<p>The available report duration values depend on your Cloudflare plan. Refer to <a href="#availability">Availability</a> for details.</p>
<h2 id="create-security-rule-from-current-filters">Create security rule from current filters</h2>
<p>To create a <a href="/waf/custom-rules/create-dashboard/">custom rule</a> based on your current filters and exclusions, select <strong>Create custom security rule</strong>.</p>
<h2 id="events-summary">Events summary</h2>
<p>The <strong>Events summary</strong> section provides the number of security events on traffic during the selected time period, grouped according to the selected dimension (for example, <strong>Action</strong>, <strong>Host</strong>, <strong>Country</strong>, or <strong>ASN</strong>).</p>
<p><img src="/assets/upstream/images/waf/events-summary.png" alt="Filter by action by selecting Filter when hovering the desired action in Events summary" /></p>
<p>You can adjust the displayed data according to one of the values by selecting <strong>Filter</strong> or <strong>Exclude</strong> when hovering the legend.</p>
<h2 id="events-by-service">Events by service</h2>
<p>The <strong>Events by service</strong> section lists the activity per Cloudflare security feature (for example, <strong>Managed rules</strong> or <strong>Rate limiting rules</strong>).</p>
<p>You can adjust the scope of Security Events to one of the displayed services by selecting <strong>Filter</strong> or <strong>Exclude</strong> when hovering the legend or by selecting the corresponding graph bar.</p>
<h2 id="top-events-by-source">Top events by source</h2>
<p>In <strong>Top events by source</strong> you can find details of the traffic flagged or actioned by a security feature — for example, <strong>IP Addresses</strong>, <strong>User Agents</strong>, <strong>Paths</strong>, and <strong>Countries</strong>.</p>
<p>You can adjust the scope of Security Events to one of the listed source values by selecting <strong>Filter</strong> or <strong>Exclude</strong> when hovering the value.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15401.md")
</aside>
<h2 id="sampled-logs">Sampled logs</h2>
<p><strong>Sampled logs</strong> shows a subset of security events for the selected time period, listed by date with the action taken and the applied Cloudflare security feature. For large volumes of traffic, Cloudflare uses <a href="/analytics/graphql-api/sampling/">sampling</a> to return results faster. This means that not every individual event may appear in the list.</p>
<p><img src="/assets/upstream/images/waf/events-sampled-logs.png" alt="Example list of events in Sampled logs, with one of the events expanded to show its details" /></p>
<p>Security events are shown by individual event rather than by request. For example, if a single request triggers three different security features, the security events will show three individual events in <strong>Sampled logs</strong>.</p>
<p>Expand each event to check its details, and define filters and exclusions based on the event's field values. Select the <strong>Filter</strong> or <strong>Exclude</strong> button when hovering a field to add the field value to the filters or exclusions list of the displayed analytics. To download the event data in JSON format, select <strong>Export event JSON</strong>.</p>
<h3 id="displayed-columns">Displayed columns</h3>
<p>To configure the columns displayed in <strong>Sampled logs</strong>, select <strong>Edit columns</strong>. This gives you flexibility depending on the type of analysis that you need to perform.</p>
<p>For example, if you are diagnosing a bot-related issue, you may want to display the <strong>User agent</strong> and the <strong>Country</strong> columns. On the other hand, if you are trying to identify a DDoS attack, you may want to display the <strong>IP address</strong>, <strong>ASN</strong>, and <strong>Path</strong> columns.</p>
<h3 id="event-actions">Event actions</h3>
<p>For details on most actions that appear in <strong>Sampled logs</strong>, refer to <a href="/ruleset-engine/rules-language/actions/">Actions</a>.</p>
<p>Besides the actions you can select when configuring rules in Cloudflare security products, you may also find events with the following associated actions:</p>
<ul>
<li><em>Connection Close</em></li>
<li><em>Force Connection Close</em></li>
<li><em>AI Labyrinth Served</em></li>
<li><em>AI Labyrinth Crawls</em></li>
</ul>
<p>For details on <em>Connection Close</em> and <em>Force Connection Close</em>, refer to <a href="/ddos-protection/managed-rulesets/http/override-parameters/#action">HTTP DDoS Attack Protection parameters</a>. For details on <em>AI Labyrinth Served</em> and <em>AI Labyrinth Crawls</em>, refer to <a href="/bots/additional-configurations/ai-labyrinth/#ai-labyrinth-in-security-analytics">AI Labyrinth</a>.</p>
<p>The <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge"><em>Managed Challenge</em></a> action that may appear in <strong>Sampled logs</strong> is available in the following security features and products: WAF custom rules, rate limiting rules, Bot Fight Mode, IP Access rules, User Agent Blocking rules, and firewall rules (deprecated).</p>
<h3 id="export-event-log-data">Export event log data</h3>
<p>You can export a set of up to 500 raw events from <strong>Sampled logs</strong> in JSON format. Export event data to combine and analyze Cloudflare data with your own stored in a separate system or database, such as a <span class="nb-glossary-tooltip" title="SIEM">SIEM system</span>. The data you export will reflect any filters you have applied.</p>
<p>To export the displayed events (up to 500), select <strong>Export</strong> in <strong>Sampled logs</strong>.</p>
<h2 id="share-security-events-filters">Share Security Events filters</h2>
<p>When you add a filter and specify a report duration (time window) in Security Events, the Cloudflare dashboard URL changes to reflect the parameters you configured. You can share that URL with other users so that they can analyze the same information that you see.</p>
<p>For example, after adding a filter for <code>Action equals Managed Challenge</code> and setting the report duration to <code>Last 3 days</code>, the URL should look like the following:</p>
<p><code>https://dash.cloudflare.com/{account_id}/example.net/security/analytics/events?action=managed_challenge&amp;time-window=4320</code></p>
<h2 id="print-or-download-pdf-report">Print or download PDF report</h2>
<p>To print or download a snapshot report, select the three dots &gt; <strong>Print report</strong>.</p>
<p>Your web browser's printing interface will present you with options for printing or downloading the PDF report.</p>
<p>The generated report will reflect all applied filters.</p>
<h2 id="known-limitations">Known limitations</h2>
<p>Security Events currently has these limitations:</p>
<ul>
<li>Security Events may use sampled data to improve performance. Refer to <a href="#sampling">Sampling</a> for more information.</li>
<li>The Cloudflare dashboard may show an inaccurate number of events per page. Data queries are highly optimized, but this means that pagination may not always work because the source data may have been sampled. The GraphQL Analytics API does not have this pagination issue.</li>
<li>Triggered <a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP rules</a> appear in the Security Events page under <strong>Additional logs</strong>, but they are not included in exported JSON files.</li>
</ul>
<h2 id="sampling">Sampling</h2>
<p>Security Events may use <a href="/analytics/graphql-api/sampling/">sampled data</a>. If your search uses sampled data, Security Events might not display all events and filters might not return the expected results. To display more events, select a smaller time frame (a narrower time range reduces the volume of data, which reduces or eliminates sampling).</p>
<h2 id="query-using-graphql">Query using GraphQL</h2>
<p>If you query Security Events data through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, the underlying dataset is <code>firewallEventsAdaptive</code>. For more information, refer to <a href="/analytics/graphql-api/features/data-sets/">Datasets (tables)</a>.</p>
<p>For more information on querying the <code>firewallEventsAdaptive</code> dataset, refer to <a href="/analytics/graphql-api/tutorials/querying-firewall-events/">Querying Firewall Events with GraphQL</a>.</p>
<h2 id="limits">Limits</h2>
<p>The retention and query window for the <code>firewallEventsAdaptive</code> dataset differ from the datasets that power <a href="/waf/analytics/security-analytics/#sampling">Security Analytics</a>.</p>
<p>The following tables show the different limits per Cloudflare plan:</p>
<table>
<thead>
<tr>
<th>Data retention (historical time) for...</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Events (<code>firewallEventsAdaptive</code>)</td>
<td>24 hours</td>
<td>24 hours</td>
<td>3 days</td>
<td>30 days</td>
</tr>
<tr>
<td>Security Analytics (<code>httpRequestsAdaptive</code>)</td>
<td>7 days</td>
<td>7 days</td>
<td>31 days</td>
<td>90 days</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Maximum query window for...</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Events (<code>firewallEventsAdaptive</code>)</td>
<td>24 hours</td>
<td>24 hours</td>
<td>3 days</td>
<td>31 days</td>
</tr>
<tr>
<td>Security Analytics (<code>httpRequestsAdaptive</code>)</td>
<td>24 hours</td>
<td>7 days</td>
<td>31 days</td>
<td>31 days</td>
</tr>
</tbody>
</table>
