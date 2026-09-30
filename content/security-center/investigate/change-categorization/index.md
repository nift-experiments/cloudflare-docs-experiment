---
cp9:
  canonical: https://developers.cloudflare.com/security-center/investigate/change-categorization/
  description: Request domain categorization changes via the dashboard, Radar, or the API.
  full_title: Change categorization · Cloudflare Security Center docs
  head_html: <title>Change categorization · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Request domain categorization changes via the dashboard, Radar, or the API."><link rel="canonical" href="https://developers.cloudflare.com/security-center/investigate/change-categorization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/investigate/change-categorization/index.md"><meta property="og:title" content="Change categorization · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Request domain categorization changes via the dashboard, Radar, or the API."><meta property="og:url" content="https://developers.cloudflare.com/security-center/investigate/change-categorization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security-center/investigate/change-categorization/#page","headline":"Change categorization \u00b7 Cloudflare Security Center docs","description":"Request domain categorization changes via the dashboard, Radar, or the API.","url":"https://developers.cloudflare.com/security-center/investigate/change-categorization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/investigate/change-categorization/
  schema: 1
---
<p>Cloudflare sorts domains into categories based on their content and security type. You can request categorization changes via the <a href="#via-the-cloudflare-dashboard">dashboard</a>, <a href="#via-cloudflare-radar">Cloudflare Radar</a>, or the <a href="#via-the-api">API</a>.</p>
<p>For a detailed list of categories, refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Domain categories</a>.</p>
<h2 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h2>
<p>To request a categorization change via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Search for the domain you want to change.</p>
</li>
<li>
<p>In <strong>Domain overview</strong>, select <strong>Request to change categorization</strong>.</p>
</li>
<li>
<p>Choose whether to change a <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security category</a> or a <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">content category</a>.</p>
</li>
<li>
<p>Choose which categories you want to add or remove from the domain.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-category-limit">Content category limit</h3>
@markup("md", "content/.markup/bodies/13811.md")
</aside>
<ol start="6">
<li>Select <strong>Submit</strong> to submit your request for review.</li>
</ol>
<p>Requesting a security category change will trigger a deeper investigation by Cloudflare to confirm that the submission is valid. Requesting a content category change also requires Cloudflare validation, but the turnaround time for these submissions is usually shorter as it requires less investigation.</p>
<p>Your category change requests will be revised by the Cloudflare team depending on the type of change. If your requests have been reviewed and applied by the Cloudflare team, the new categories will be visible in the Cloudflare dashboard in <strong>Security Center</strong> &gt; <strong>Investigate</strong>, as well as in <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13810.md")
</aside>
<h2 id="via-cloudflare-radar">Via Cloudflare Radar</h2>
<p>To request recategorization via Cloudflare Radar, submit feedback in <a href="https://radar.cloudflare.com/domains/feedback">Radar Domain Categorization</a>.</p>
<h2 id="via-the-api">Via the API</h2>
<p>To request a categorization change via the API:</p>
<ol>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> with permission to edit your Intel account.</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Permissions</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>Intel</td>
<td>Edit</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><strong>Account Resources</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>All accounts</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Make a call to the <a href="/api/resources/intel/subresources/miscategorizations/methods/create/">miscategorization endpoint</a> including the domain name and any categories you would like to add or remove. For example:</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/intel/miscategorization \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;content_adds&quot;: [&#10;    82&#10;  ],&#10;  &quot;content_removes&quot;: [&#10;    155&#10;  ],&#10;  &quot;indicator_type&quot;: &quot;domain&quot;,&#10;  &quot;ip&quot;: null,&#10;  &quot;security_adds&quot;: [&#10;    117,&#10;    131&#10;  ],&#10;  &quot;security_removes&quot;: [&#10;    83&#10;  ],&#10;  &quot;url&quot;: &quot;example.com&quot;&#10;}&#x27;&#10;</code></pre>
