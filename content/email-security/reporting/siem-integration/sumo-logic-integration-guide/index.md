---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/siem-integration/sumo-logic-integration-guide/
  description: Sumo Logic integration guide
  full_title: Sumo Logic · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Sumo Logic · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Sumo Logic integration guide"><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/sumo-logic-integration-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/siem-integration/sumo-logic-integration-guide/index.md"><meta property="og:title" content="Sumo Logic · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sumo Logic integration guide"><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/siem-integration/sumo-logic-integration-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/siem-integration/sumo-logic-integration-guide/
  schema: 1
---
<p>When Email security detects a <span class="nb-glossary-tooltip" title="phishing">phishing</span> email, the metadata of the detection can be sent directly into your instance of Sumo Logic. This document outlines the steps required to integrate Email security with Sumo Logic.</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/opening-sumo-logic.png" alt="A diagram outlining what happens when Email security detects a phishing email and sends it to Sumo Logic." /></p>
<h2 id="1-configure-the-sumologic-collector"><ol>
<li>Configure the Sumologic Collector</li>
</ol></h2>
<ol>
<li>
<p>Log in to <a href="https://service.sumologic.com/ui/">Sumo Logic</a> with an administrator account.</p>
</li>
<li>
<p>Go to <strong>Manage Data</strong> &gt; <strong>Collection</strong> to open the collector configuration pane.</p>
</li>
<li>
<p>Select <strong>Add Collector</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step3-collector.png" alt="Add collector." /></p>
<ol start="4">
<li>In <strong>Select Collector Type</strong>, select <strong>Hosted Collector</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step4-hosted.png" alt="Select Hosted Collector." /></p>
<ol start="5">
<li>In <strong>Add Hosted Collector</strong>, enter the following settings:
<ul>
<li><strong>Name</strong>: <code>Email security Collector</code></li>
<li><strong>Description</strong>: <code>Email security Security Collectors</code></li>
<li><strong>Category</strong>: Anti-Phishing</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step5-hosted-collector.png" alt="Enter the settings above to configure your collector." /></p>
<ol start="6">
<li>
<p>Select <strong>Save</strong> &gt; <strong>OK</strong> to confirm the addition of the new Collector.</p>
</li>
<li>
<p>In <strong>Cloud APIs</strong>, select <strong>HTTP Logs and Metrics</strong> to start the configuration of the data source.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step7-http-logs.png" alt="Select HTTP Logs and Metrics." /></p>
<ol start="8">
<li>Enter a descriptive <strong>Name</strong> and <strong>Description</strong>, and select <strong>Save</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step8-name.png" alt="Enter a name and description." /></p>
<ol start="9">
<li>The system will present you a dialog box with the HTTP endpoint. Save it, as this will be required to configure Email security later.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/step9-endpoint.png" alt="Take note of the endpoint to use it later." /></p>
<h2 id="2-configure-email-security"><ol start="2">
<li>Configure Email security</li>
</ol></h2>
<p>The next step is to configure Email security to push the Email Detection Events to the Sumologic HTTP Collector.</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Alert Webhooks</strong>, and select <strong>New Webhook</strong>.</li>
<li>In the Add Webhooks page, enter the following settings:
<ul>
<li><strong>App type</strong>: Select <strong>SIEM</strong> &gt; <strong>Splunk</strong>. In <strong>Auth code</strong>, enter <code>Sumologic</code>.</li>
<li><strong>Target</strong>: Enter the HTTP endpoint you saved in the previous section.</li>
<li>For the <span class="nb-glossary-tooltip" title="disposition">dispositions</span> (<code>MALICIOUS</code>, <code>SUSPICIOUS</code>, <code>SPOOF</code>, <code>SPAM</code>, <code>BULK</code>) choose which (if any) you want to send to the webhook. Sending <code>SPAM</code> and <code>BULK</code> dispositions will generate a high number of events.</li>
</ul>
</li>
<li>Select <strong>Publish Webhook</strong>.</li>
</ol>
<p>Your Sumo Logic integration will now show up in the All Webhooks panel.</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/all-webhooks.png" alt="Your Sumo Logic webhook will display in the All Webhooks panel." /></p>
<p>It will take about ten minutes for the configuration to fully propagate through the infrastructure of Email security, and for events to start to appear in your searches. Once the configuration is propagated, events will start to appear in your instance of Sumo Logic.</p>
<p>To view logs, hover your mouse over the Email security Collector, and select <strong>Open in Log Search</strong>.</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/open-log.png" alt="View logs in Sumo Logic." /></p>
<p>Once events start to flow, select <strong>New</strong> &gt; <strong>Log search</strong> to search for the detection events with your search criteria (for example, <code>_collector=&quot;Email security Collector&quot;</code>).</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/sumo-logic/search-events.png" alt="Search for events." /></p>
