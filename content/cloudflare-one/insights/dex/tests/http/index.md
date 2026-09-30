---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/
  description: Reference information for HTTP test in Zero Trust analytics.
  full_title: HTTP test · Cloudflare One docs
  head_html: <title>HTTP test · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for HTTP test in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/index.md"><meta property="og:title" content="HTTP test · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for HTTP test in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Windows,MacOS,Linux,Android"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/#page","headline":"HTTP test \u00b7 Cloudflare One docs","description":"Reference information for HTTP test in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Windows","MacOS","Linux","Android"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/tests/http/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4974.md")
</div></details>
<p>An HTTP test sends a <code>GET</code> request from an end-user device to a specific web application. You can use the response metrics to troubleshoot connectivity issues. For example, you can check whether the application is inaccessible for all users in your organization, or only certain ones.</p>
<p>HTTP tests run periodically from devices that have the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> installed and turned on. You can use them to verify that an internal application is reachable after a configuration change or to monitor a SaaS application for outages that affect your organization.</p>
<h2 id="create-a-test">Create a test</h2>
<p>To set up an HTTP test for an application:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select <strong>Add a Test</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Name</strong>: Enter any name for the test.</li>
<li><strong>Target</strong>: Enter the URL of the website or application that you want to test (for example, <code>https://jira.site.com</code>). Both public and private hostnames are supported. If testing a private hostname, ensure that the domain is on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> list.</li>
<li><strong>Source device profiles</strong>: (Optional) Select the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> that you want to run the test on. If no profiles are selected, the test will run on all supported devices connected to your Zero Trust organization.</li>
<li><strong>Test type</strong>: Select <em>HTTP Get</em>.</li>
<li><strong>Test frequency</strong>: Specify how often the test will run. Input a minute value between 5 and 60.</li>
</ul>
</li>
<li>Select <strong>Add test</strong>.</li>
<li>After the test is created and running, you can <a href="/cloudflare-one/insights/dex/tests/view-results/">view the results</a> of your test.</li>
</ol>
<h2 id="test-results">Test results</h2>
<p>An HTTP test measures the following data:</p>
<table>
<thead>
<tr>
<th>Data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Resource fetch time</td>
<td>Total time of all steps of the request, measured from <a href="https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing"><code>startTime</code> to <code>responseEnd</code></a>.</td>
</tr>
<tr>
<td>Server response time</td>
<td>Round-trip time for the device to receive a response from the target.</td>
</tr>
<tr>
<td>DNS response time</td>
<td>Round-trip time for the DNS query to resolve.</td>
</tr>
<tr>
<td>HTTP status codes</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status">Status code</a> returned by the target.</td>
</tr>
</tbody>
</table>
<p>Use these metrics together to identify where in the connection a problem occurs. For example, a high DNS response time with a normal server response time points to a DNS resolution issue rather than a problem with the target server.</p>
<h2 id="export-dex-application-test-logs">Export DEX application test logs</h2>
<p>You can use <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX application test</a> data to <a href="/r2/">R2</a> (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the <a href="/cloudflare-one/insights/logs/#log-retention">7-day log retention period</a> or correlate DEX data with other log sources.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/rules/">DEX rules</a> - Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.</li>
</ul>
