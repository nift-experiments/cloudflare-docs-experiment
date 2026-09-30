---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/pricing/
  description: Dynamic Workers pricing is based on requests, CPU time, and the number of unique Dynamic Workers created per day.
  full_title: Pricing · Cloudflare Dynamic Workers docs
  head_html: <title>Pricing · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Dynamic Workers pricing is based on requests, CPU time, and the number of unique Dynamic Workers created per day."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Dynamic Workers pricing is based on requests, CPU time, and the number of unique Dynamic Workers created per day."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/pricing/#page","headline":"Pricing \u00b7 Cloudflare Dynamic Workers docs","description":"Dynamic Workers pricing is based on requests, CPU time, and the number of unique Dynamic Workers created per day.","url":"https://developers.cloudflare.com/dynamic-workers/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/pricing/
  schema: 1
---
<p>Dynamic Workers pricing is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.</p>
<p>Dynamic Workers are currently only available on the <a href="/workers/platform/pricing/">Workers Paid plan</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Included</th>
<th>Additional usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dynamic Workers created daily</strong></td>
<td>1,000 unique Dynamic Workers per month</td>
<td>+$0.002 per Dynamic Worker per day</td>
</tr>
<tr>
<td><strong>Requests</strong> ¹</td>
<td>10 million per month</td>
<td>+$0.30 per million requests</td>
</tr>
<tr>
<td><strong>CPU time</strong> ¹</td>
<td>30 million CPU milliseconds per month</td>
<td>+$0.02 per million CPU milliseconds</td>
</tr>
</tbody>
</table>
<p>¹ Uses <a href="/workers/platform/pricing/#workers">Workers Standard rates</a> and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="billing">Billing</h3>
@markup("md", "content/.markup/bodies/1071.md")
</aside>
<h2 id="dynamic-workers-created-daily">Dynamic Workers created daily</h2>
<p>You are billed for each unique Dynamic Worker created in a day. A Dynamic Worker is uniquely identified by its <strong>Worker ID</strong> and <strong>code</strong> — if either changes, it counts as a new Dynamic Worker. The count resets daily.</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Counted as</th>
</tr>
</thead>
<tbody>
<tr>
<td>Same code, same ID, invoked multiple times</td>
<td>1 Dynamic Worker</td>
</tr>
<tr>
<td>Same code, different IDs</td>
<td>1 Dynamic Worker per ID</td>
</tr>
<tr>
<td>Same ID, different code versions</td>
<td>1 Dynamic Worker per code version</td>
</tr>
<tr>
<td>No ID provided or <code>.load(code)</code> used</td>
<td>1 Dynamic Worker per invocation</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1070.md")
</aside>
<h2 id="view-dynamic-workers-usage">View Dynamic Workers usage</h2>
<p>To view the number of billable Dynamic Workers invoked during your billing period, go to <strong>Workers &amp; Pages</strong> &gt; <strong>Overview</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<p>Dynamic Workers usage data only goes back to June 1, 2026.</p>
<p>You can also query this count through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> by using <code>workersInvocationsByOwnerAndScriptGroups</code> and selecting <code>distinctDynamicWorkerCount</code>:</p>
<pre tabindex="0"><code class="language-graphql">query getDynamicWorkersCount(&#10;	$accountTag: string!&#10;	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {&#10;				uniq {&#10;					distinctDynamicWorkerCount&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use variables to set the account and billing-period date range:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;date_geq&quot;: &quot;2026-06-01&quot;,&#10;		&quot;date_leq&quot;: &quot;2026-06-30&quot;&#10;	}&#10;}&#10;</code></pre>
<p>The <code>distinctDynamicWorkerCount</code> field returns the unique Dynamic Workers count for the selected period.</p>
<h2 id="requests">Requests</h2>
<p>Dynamic Workers reuse <a href="/workers/platform/pricing/">Workers Standard request pricing</a>.</p>
<p>A request is counted each time a Dynamic Worker is invoked:</p>
<ul>
<li>Each <code>fetch()</code> call into a Dynamic Worker</li>
<li>Each RPC method call on a Dynamic Worker stub (billed the same way as <a href="/durable-objects/platform/pricing/">Durable Objects</a>)</li>
</ul>
<p>If an RPC method returns a stub (an object that extends <code>RpcTarget</code>), those returned stubs share the same RPC session as the original call. Subsequent calls on the returned stub are not billed as separate requests.</p>
<h2 id="cpu-time">CPU time</h2>
<p>CPU time is billed at the same rate as <a href="/workers/platform/pricing/">Workers Standard</a>.</p>
<p>Unlike standard Workers (where only execution time is billed), Dynamic Workers bill for two components of CPU time:</p>
<ul>
<li><strong>Startup time</strong>: The compute required to initialize the isolate and parse your code.</li>
<li><strong>Execution time</strong>: The compute time your code spends actively processing logic, excluding time spent waiting on I/O.</li>
</ul>
