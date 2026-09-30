---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/
  description: Discover sensitive data in sampled Gateway HTTP traffic before you create a DLP policy.
  full_title: Passive Detection · Cloudflare One docs
  head_html: <title>Passive Detection · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Discover sensitive data in sampled Gateway HTTP traffic before you create a DLP policy."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/index.md"><meta property="og:title" content="Passive Detection · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Discover sensitive data in sampled Gateway HTTP traffic before you create a DLP policy."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One,Data Loss Prevention"><meta name="pcx_tags" content="Analytics,Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/#page","headline":"Passive Detection \u00b7 Cloudflare One docs","description":"Discover sensitive data in sampled Gateway HTTP traffic before you create a DLP policy.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics","Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/passive-detection/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4514.md")
</aside>
<p>Before you create a Data Loss Prevention (DLP) policy, you may not know which sensitive data types appear in your traffic or where they are going. Passive Detection gives you a place to start. It helps you answer those questions before you decide what to log or block.</p>
<p>Passive Detection scans a randomly sampled subset of Gateway HTTP request and response bodies and brings the findings into one dashboard. You can see which detection entries matched, trace where they appeared, and identify where a policy could help. Use what you learn to build a focused policy or review gaps in an existing one.</p>
<p>Passive Detection works without a Gateway DLP policy. It does not change how Gateway handles traffic, and existing policies continue to apply.</p>
<h2 id="get-started">Get started</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>To collect Passive Detection results:</p>
<ul>
<li>Route HTTP traffic through Cloudflare Gateway.</li>
<li>Turn on <a href="/cloudflare-one/traffic-policies/get-started/http/">Gateway HTTP filtering</a>.</li>
<li>Turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> for HTTPS traffic.</li>
<li>Make sure each detection entry you want to scan is enabled in at least one <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profile</a> in your account. Passive Detection scans entries enabled in any profile in your account, not just profiles selected for a policy.</li>
</ul>
<p>For uploaded or downloaded files, refer to the <a href="/cloudflare-one/data-loss-prevention/#supported-file-types">supported file types</a>. Traffic that bypasses Gateway or matches a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policy cannot produce findings.</p>
<h3 id="view-passive-detection">View Passive Detection</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4515.md")
</div>
<p>Use <strong>Request</strong> to see data sent to destinations and <strong>Response</strong> to see data received from them. <strong>Unknown</strong> includes HTTP bodies without a recorded traffic direction. Remove the filter to include all traffic directions. Request and response bodies are counted separately.</p>
<p>The selected time range and traffic direction also apply when you open an entry to investigate it.</p>
<h2 id="learn-from-the-data">Learn from the data</h2>
<p>Start with the account summary for the broad picture. From there, select a detection entry to see where it appeared, the matching profiles, and whether policy enforcement was applied.</p>
<h3 id="start-with-the-account-summary">Start with the account summary</h3>
<p>The summary cards describe detections within your selected time range and traffic direction:</p>
<ul>
<li><strong>Total detections</strong>: Each entry counts once per HTTP body.</li>
<li><strong>Unique traffic with detections</strong>: HTTP bodies with at least one detection, counted once.</li>
<li><strong>Entries detected</strong>: Unique DLP entries matched in the selected scope.</li>
</ul>
<p>For example, one request body that matches two different entries contributes two detections to <strong>Total detections</strong> and one body to <strong>Unique traffic with detections</strong>. These counts do not tell you how many individual sensitive values the body contains.</p>
<p>Use <strong>Detections by data type</strong> to see which entries account for the most detections. Use <strong>Policy coverage</strong> to find entries that may need policy review.</p>
<h3 id="find-sensitive-data">Find sensitive data</h3>
<p>Next, use the detection table to decide what to investigate. Compare entries, then inspect their profiles and destinations. The table contains one row per detection entry found in sampled traffic. Entries without detections do not appear.</p>
<p>Use these fields to compare entries:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Entry</td>
<td>The DLP detection entry found in sampled traffic.</td>
</tr>
<tr>
<td>Profiles</td>
<td>The profiles associated with the detection.</td>
</tr>
<tr>
<td>Detections</td>
<td>HTTP bodies where this entry was detected at least once. Multiple occurrences of the same entry in one body count once.</td>
</tr>
<tr>
<td>URL destinations</td>
<td>The number of distinct destinations associated with the entry.</td>
</tr>
<tr>
<td>Confidence (H/M/L)</td>
<td>Observed detections grouped by high, medium, and low confidence.</td>
</tr>
<tr>
<td>Policy coverage</td>
<td>Whether matching profiles were selected for policy enforcement when the bodies were scanned. Refer to <a href="#find-policy-coverage-gaps">Find policy coverage gaps</a>.</td>
</tr>
<tr>
<td>Last seen</td>
<td>When the entry was most recently observed during the selected time range.</td>
</tr>
</tbody>
</table>
<p>All times are reported in UTC.</p>
<p>The same body can contribute confidence counts through more than one matching profile. Confidence counts can therefore add up to more than the number of detected bodies, even within a single confidence level.</p>
<h3 id="trace-where-data-goes">Trace where data goes</h3>
<p>After you choose an entry, select it to see where it appeared. The detail view shows detections and confidence over time, followed by the destinations and applications associated with that entry.</p>
<p>Destinations group URLs by host and a normalized path. For example, paths such as <code>/users/12345</code> can be grouped under <code>/users/{id}</code>. Each destination includes detection counts, confidence, traffic direction, and the last detection time.</p>
<p>Expand a destination to review a selection of matched URLs, their detection counts, and when they were last observed. Use these details to check whether the activity involves an expected application or a destination that needs further investigation.</p>
<p>For example, a detection associated with an unfamiliar file-sharing destination may warrant a closer look. Check whether that destination is approved for the data involved before deciding whether to create a policy.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4513.md")
</aside>
<p>The dashboard shows detection metadata. Original request and response bodies are not stored.</p>
<h3 id="find-policy-coverage-gaps">Find policy coverage gaps</h3>
<p>Policy coverage helps you find detections that may need a closer look. A detection counts as covered when at least one matching DLP profile was selected for policy enforcement when the HTTP body was scanned.</p>
<p>Coverage does not confirm that the complete Gateway policy matched or that Gateway logged or blocked the traffic. The dashboard groups coverage into three statuses:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>Covered</td>
<td>Each detection had at least one matching profile selected for enforcement.</td>
</tr>
<tr>
<td>Partly covered</td>
<td>Some detections had a matching profile selected for enforcement and some did not.</td>
</tr>
<tr>
<td>Not covered</td>
<td>No detections had a matching profile selected for enforcement.</td>
</tr>
</tbody>
</table>
<p>Start with entries that are <strong>Not covered</strong> or <strong>Partly covered</strong>, then review their destinations and the relevant policies. A coverage gap is a reason to investigate, not a recommendation to block every detection.</p>
<h2 id="create-a-dlp-policy">Create a DLP policy</h2>
<p>Once you understand what data was detected and where it appeared, turn those findings into a policy that fits your traffic. Focus on the data types and destinations that need protection, rather than applying the same action to every detection.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4516.md")
</div>
<p>For an existing policy, use your findings to review its scope and detection settings. <a href="/cloudflare-one/insights/analytics/data-analytics/">Data security analytics</a> shows activity from DLP policies after they are configured.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Passive Detection scans a random sample of eligible Gateway HTTP traffic, not every request or response body.</li>
<li>Counts may be estimated for high-volume detections due to analytics sampling. They describe sampled traffic, not all eligible Gateway traffic.</li>
<li>The dashboard does not report total sampled traffic or detection rates.</li>
<li>Destinations are scoped to one detection entry. Passive Detection does not provide an account-wide destination inventory.</li>
<li>Results do not include user identity.</li>
</ul>
<p>An empty dashboard does not confirm that sensitive data is absent.</p>
<p>For help with missing results, refer to <a href="/cloudflare-one/data-loss-prevention/troubleshoot-dlp/#passive-detection-shows-no-results">Troubleshoot DLP</a>.</p>
