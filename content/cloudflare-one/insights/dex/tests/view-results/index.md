---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/
  description: View test results in Zero Trust analytics.
  full_title: View test results · Cloudflare One docs
  head_html: <title>View test results · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="View test results in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/index.md"><meta property="og:title" content="View test results · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View test results in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/#page","headline":"View test results \u00b7 Cloudflare One docs","description":"View test results in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/tests/view-results/
  schema: 1
---
<p>Use the results of a Digital Experience Monitoring (DEX) test to monitor availability and performance for a specific application. DEX stores test results for 7 days on all plans, according to the <a href="/cloudflare-one/insights/logs/#log-retention">log retention policy</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>At least one <a href="/cloudflare-one/insights/dex/tests/">test</a> has been created under <strong>DEX</strong> &gt; <strong>Tests</strong>.</li>
<li>Admins must have at least the <a href="/cloudflare-one/roles-permissions/#zero-trust-roles">Cloudflare Zero Trust Reporting role</a>.</li>
</ul>
<h2 id="view-results-for-all-devices">View results for all devices</h2>
<p>To view an overview of test results for all devices:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select a test to view detailed results.</li>
</ol>
<h2 id="view-results-for-an-individual-device">View results for an individual device</h2>
<p>To view analytics on a per-device level:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select the device you want to view, and then select <strong>View details</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select a test to view detailed results.</li>
</ol>
<h2 id="export-dex-application-test-logs">Export DEX application test logs</h2>
<p>You can use <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX application test</a> data to <a href="/r2/">R2</a> (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the <a href="/cloudflare-one/insights/logs/#log-retention">7-day log retention period</a> or correlate DEX data with other log sources.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/tests/http/">DEX HTTP test</a> - Send a <code>GET</code> request from enrolled devices to a web application and measure response times.</li>
<li><a href="/cloudflare-one/insights/dex/tests/traceroute/">DEX Traceroute test</a> - Map the network route between a device and a server, showing each hop along the path.</li>
<li><a href="/cloudflare-one/insights/dex/rules/">DEX rules</a> - Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.</li>
</ul>
