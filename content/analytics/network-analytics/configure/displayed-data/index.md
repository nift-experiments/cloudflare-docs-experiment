---
cp9:
  canonical: https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/
  description: Filter and configure Network Analytics dashboard data.
  full_title: Adjust the data displayed in Network Analytics · Cloudflare Analytics docs
  head_html: <title>Adjust the data displayed in Network Analytics · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Filter and configure Network Analytics dashboard data."><link rel="canonical" href="https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/index.md"><meta property="og:title" content="Adjust the data displayed in Network Analytics · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Filter and configure Network Analytics dashboard data."><meta property="og:url" content="https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/#page","headline":"Adjust the data displayed in Network Analytics \u00b7 Cloudflare Analytics docs","description":"Filter and configure Network Analytics dashboard data.","url":"https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/network-analytics/configure/displayed-data/
  schema: 1
---
<h2 id="select-the-appropriate-tab">Select the appropriate tab</h2>
<p>To perform a broad analysis of layer 3/4 traffic and DDoS attacks, use the <strong>All traffic</strong> tab.</p>
<p>To focus on a specific mitigation system, select one of the <a href="/analytics/network-analytics/understand/main-dashboard/#available-tabs">other available tabs</a>. The tabs displayed in the dashboard depend on your Cloudflare services.</p>
<h2 id="select-high-level-metric">Select high-level metric</h2>
<p>To toggle your view of the data, select the <strong>Total packets</strong> or <strong>Total bytes</strong> side panels.</p>
<p><img src="/assets/upstream/images/analytics/network-analytics/high-level-metrics.png" alt="Network Analytics side panels allowing you to use packets or bits/bytes as the base unit for the dashboard." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>The selected metric will determine the base units (packets or bits/bytes) used in the several dashboard analytics panels.</p>
<h2 id="select-a-dimension">Select a dimension</h2>
<p>Under <strong>Packets summary</strong> or <strong>Bits summary</strong>, select one of the <a href="/analytics/network-analytics/understand/main-dashboard/#available-dimensions">available dimensions</a> to view the data along that dimension. The default dimension is <strong>Action</strong>.</p>
<h2 id="apply-filters">Apply filters</h2>
<p>You can apply multiple filters and exclusions to adjust the scope of the data displayed in Network Analytics.
Filters affect all the data displayed in the dashboard.</p>
<p>There are two ways to filter Network Analytics data: select <strong>Add filter</strong> or select one of the stat filters.</p>
<h3 id="select-add-filter">Select Add filter</h3>
<p>Select <strong>Add filter</strong> to open the <strong>New filter</strong> popover. Specify a field, an operator, and a value to complete your filter expression. Select <strong>Apply</strong> to update the view.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes-about-filtering">Notes about filtering</h3>
@markup("md", "content/.markup/bodies/3186.md")
</aside>
<h3 id="select-a-stat-filter">Select a stat filter</h3>
<p>To filter based on the type of data associated with one of the Network Analytics stats, use the <strong>Filter</strong> and <strong>Exclude</strong> buttons that display when you hover over the stat.</p>
<h2 id="create-a-network-firewall-rule-from-the-applied-filters">Create a Network Firewall rule from the applied filters</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3185.md")
</aside>
<p>Select <strong>Create Network Firewall rule</strong> to create a <a href="/cloudflare-network-firewall/">Network Firewall</a> rule that will block all traffic matching the selected filters in Network Analytics.</p>
<p>Note that some filters will not be added to the new Network Firewall rule definition. However, you can further configure the rule in Network Firewall.</p>
<h2 id="show-ip-prefix-events">Show IP prefix events</h2>
<p>Enable the <strong>Show annotations</strong> toggle to show or hide annotations for advertised/withdrawn IP prefix events in the <strong>Network Analytics</strong> view. Select each annotation to get more details.</p>
<p><img src="/assets/upstream/images/analytics/network-analytics/view-annotations.png" alt="Network Analytics chart displaying IP prefix-related annotations." /></p>
<h2 id="view-logged-or-monitored-traffic">View logged or monitored traffic</h2>
<p><a href="/ddos-protection/managed-rulesets/network/">Network DDoS managed rules</a> and <a href="/ddos-protection/advanced-ddos-systems/overview/">Advanced DDoS Protection systems</a> provide a <code>log</code> or <code>monitoring</code> mode that does not drop traffic. These <code>log</code> and <code>monitoring</code> mode events are based on <strong>Verdict</strong> and <strong>Outcome</strong>/<strong>Action</strong> fields.</p>
<p>To filter for these traffic events:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>DDoS managed rules</strong> tab.</li>
<li>Select <strong>Add filter</strong>.
<ul>
<li>Set <code>Verdict equals drop</code>.</li>
<li>Set <code>Action equals pass</code>.</li>
</ul>
</li>
<li>Select <strong>Apply</strong>.</li>
</ol>
<p>By setting <code>verdict</code> to <code>drop</code> and <code>outcome</code> as <code>pass</code>, we are filtering for traffic that was marked as a detection (that is, verdict was <code>drop</code>) but was not dropped (for example, outcome was <code>pass</code>).</p>
