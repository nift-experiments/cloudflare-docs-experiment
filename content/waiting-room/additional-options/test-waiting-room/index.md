---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/
  description: Follow this tutorial to test your waiting room behavior in response to load. To accurately simulate traffic, run your test script or planner for a period of time longer than a minute, ideally more than 2-3 minutes.
  full_title: Test a waiting room · Cloudflare Waiting Room docs
  head_html: <title>Test a waiting room · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Follow this tutorial to test your waiting room behavior in response to load. To accurately simulate traffic, run your test script or planner for a period of time longer than a minute, ideally more than 2-3 minutes."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/index.md"><meta property="og:title" content="Test a waiting room · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Follow this tutorial to test your waiting room behavior in response to load. To accurately simulate traffic, run your test script or planner for a period of time longer than a minute, ideally more than 2-3 minutes."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/#page","headline":"Test a waiting room \u00b7 Cloudflare Waiting Room docs","description":"Follow this tutorial to test your waiting room behavior in response to load. To accurately simulate traffic, run your test script or planner for a period of time longer than a minute, ideally more than 2-3 minutes.","url":"https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/additional-options/test-waiting-room/
  schema: 1
---
<p>Follow this tutorial to test your waiting room behavior in response to load. To accurately simulate traffic through your waiting room with a load test, run your test script or planner for a period of time longer than a minute, ideally more than 2-3 minutes. You can run a load test using a variety of tools including <a href="http://loader.io">loader.io</a>, <a href="http://jmeter.apache.org">jmeter</a>, and <a href="http://postman.com">postman.com</a>. You can also write a plain shell script to simulate user requests (each representing a distinct user).</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/15754.md")
</aside>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you start this tutorial, ensure you have:</p>
<ul>
<li>Reviewed the <a href="/waiting-room/about/">About</a> Waiting Room page.</li>
<li>For this tutorial, we will use an open source tool from Apache, <a href="https://jmeter.apache.org/">JMeter</a>. You can download the binary from <a href="https://jmeter.apache.org/download_jmeter.cgi">JMeter's website</a>.</li>
</ul>
<hr />
<h2 id="1-download-sample-script"><ol>
<li>Download sample script</li>
</ol></h2>
<p>First, download the <a href="https://github.com/yj7o5/cf-waiting-room-testing/blob/main/plan.jmx">sample</a> JMeter plan (configuration file) from GitHub.</p>
<p>This sample plan simulates 200 active users visiting the site, slowly ramping up traffic within the first minute and then maintaining 200 active users for the next three minutes. The test plan for this tutorial follows the setup outlined in the next steps.</p>
<h2 id="2-edit-and-run-the-sample-plan"><ol start="2">
<li>Edit and run the sample plan</li>
</ol></h2>
<p>Before running the sample plan, edit the waiting room in the test plan to point to your own waiting room.</p>
<ol>
<li>Select <strong>Waiting Room Simulation</strong> to expand the test plan and then select <strong>Request origin with waiting room</strong> to update the test configuration.</li>
</ol>
<p><img src="/assets/upstream/images/waiting-room/simulation-panel.png" alt="Select Request origin with waiting room in the Waiting Room Simulation panel" /></p>
<ol start="2">
<li>In the <strong>HTTP Request</strong> section update the <strong>Protocol</strong>, <strong>Server Name or IP</strong>, and <strong>Path</strong> fields to point to your test URL with waiting room enabled. For example, if your full URL looks like <code>https://www.example.com/deals/summer</code>, then the fields should match as the following:</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Protocol</td>
<td>https</td>
</tr>
<tr>
<td>Server Name or IP</td>
<td><a href="http://www.example.com">www.example.com</a></td>
</tr>
<tr>
<td>Path</td>
<td>deals/summer</td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/waiting-room/http-request-section.png" alt="Update the HTTP Request section" /></p>
<p>Then, select the <strong>play</strong> button to get the test started. This should take roughly around 3-4 minutes.</p>
<p><img src="/assets/upstream/images/waiting-room/navigation.png" alt="Select the play button" /></p>
<ul>
<li>Each simulated user has the following attributes:
<ul>
<li>Contains a Cookie jar for cookies persistence.</li>
<li>Repeats for 20 times.
<ul>
<li>Makes a request to the origin site with waiting room enabled.</li>
<li>Logs request details.</li>
<li>Pauses for 10 seconds before refreshing the page to make another request to the origin site.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/waiting-room/user-attributes.png" alt="User attributes" /></p>
<p>Per the plan above, each <a href="https://jmeter.apache.org/usermanual/test_plan.html#thread_group">Thread Group</a> performs the above action once. The user traffic ramps up within the first minute and keeps a sustained traffic for the next three minutes before users leave the site. You can send more or less traffic than what is being sent in this example by updating these properties.</p>
<p><img src="/assets/upstream/images/waiting-room/threads.png" alt="Visualizing number of threads" /></p>
<h2 id="3-analyze-results"><ol start="3">
<li>Analyze results</li>
</ol></h2>
<p>To analyze the results of your test, you can query Waiting Room Analytics (Beta) via Cloudflare’s GraphQL API to check Total Active Users and Queued Users for each minute of your load test.</p>
<details class="nb-details"><summary>Example Curl Statement</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15755.md")
</div></details>
<p>From our test, we got the following results (these are extracted from results of the query for readability):</p>
<ul>
<li>
<p>15:35:00 UTC</p>
<ul>
<li><code>&quot;totalActiveUsers&quot;: 137,</code></li>
<li><code>&quot;totalActiveUsersConfig&quot;: 300,</code></li>
<li><code>&quot;totalQueuedUsers&quot;: 0</code></li>
</ul>
</li>
<li>
<p>15:36:00 UTC</p>
<ul>
<li><code>&quot;totalActiveUsers&quot;: 200,</code></li>
<li><code>&quot;totalActiveUsersConfig&quot;: 300,</code></li>
<li><code>&quot;totalQueuedUsers&quot;: 0</code></li>
</ul>
</li>
<li>
<p>15:37:00 UTC</p>
<ul>
<li><code>&quot;totalActiveUsers&quot;: 200,</code></li>
<li><code>&quot;totalActiveUsersConfig&quot;: 300,</code></li>
<li><code>&quot;totalQueuedUsers&quot;: 0</code></li>
</ul>
</li>
<li>
<p>15:38:00 UTC</p>
<ul>
<li><code>&quot;totalActiveUsers&quot;: 200,</code></li>
<li><code>&quot;totalActiveUsersConfig&quot;: 300,</code></li>
<li><code>&quot;totalQueuedUsers&quot;: 0</code></li>
</ul>
</li>
</ul>
<p>The first minute mark, 15:35:00 UTC, shows 137 active users past the waiting room. This is because our traffic was set to gradually ramp up within the first minute and the test did not start exactly at the minute mark. When data was aggregated for the following minute, 15:36:00 UTC, the waiting room reported the total 200 users active we expected on the site as each “user” made subrequests. The active user count remained stable at 200 as long as it received subrequests from the traffic sent by the load test.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15753.md")
</aside>
