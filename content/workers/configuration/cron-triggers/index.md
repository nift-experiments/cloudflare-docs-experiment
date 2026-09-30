---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/cron-triggers/
  description: Enable your Worker to be executed on a schedule.
  full_title: Cron Triggers · Cloudflare Workers docs
  head_html: <title>Cron Triggers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable your Worker to be executed on a schedule."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/cron-triggers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/cron-triggers/index.md"><meta property="og:title" content="Cron Triggers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable your Worker to be executed on a schedule."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/cron-triggers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/cron-triggers/#page","headline":"Cron Triggers \u00b7 Cloudflare Workers docs","description":"Enable your Worker to be executed on a schedule.","url":"https://developers.cloudflare.com/workers/configuration/cron-triggers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/cron-triggers/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Cron Triggers allow users to map a cron expression to a Worker using a <a href="/workers/runtime-apis/handlers/scheduled/"><code>scheduled()</code> handler</a> that enables Workers to be executed on a schedule.</p>
<p>Cron Triggers are ideal for running periodic jobs, such as for maintenance or calling third-party APIs to collect up-to-date data. Workers scheduled by Cron Triggers will run on underutilized machines to make the best use of Cloudflare's capacity and route traffic efficiently.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16639.md")
</aside>
<p>Cron Triggers execute on UTC time.</p>
<h2 id="add-a-cron-trigger">Add a Cron Trigger</h2>
<h3 id="1-define-a-scheduled-event-listener"><ol>
<li>Define a scheduled event listener</li>
</ol></h3>
<p>To respond to a Cron Trigger, you must add a <a href="/workers/runtime-apis/handlers/scheduled/"><code>&quot;scheduled&quot;</code> handler</a> to your Worker.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16643.md")
</div></div>
<p>Refer to the following additional examples to write your code:</p>
<ul>
<li><a href="/workers/examples/cron-trigger/">Setting Cron Triggers</a></li>
<li><a href="/workers/examples/multiple-cron-triggers/">Multiple Cron Triggers</a></li>
</ul>
<h3 id="2-update-configuration"><ol start="2">
<li>Update configuration</li>
</ol></h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cron-trigger-changes-take-time-to-propagate">Cron Trigger changes take time to propagate.</h3>
@markup("md", "content/.markup/bodies/16638.md")
</aside>
<p>After you have updated your Worker code to include a <code>&quot;scheduled&quot;</code> event, you must update your Worker project configuration.</p>
<h4 id="via-the-wrangler-configuration-file-workers-wrangler-configuration">Via the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></h4>
<p>If a Worker is managed with Wrangler, Cron Triggers should be exclusively managed through the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>Refer to the example below for a Cron Triggers configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16644.md")
</div>
<p>You also can set a different Cron Trigger for each <a href="/workers/wrangler/environments/">environment</a> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. You need to put the <code>triggers</code> array under your chosen environment. For example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16645.md")
</div>
<h4 id="via-the-dashboard">Via the dashboard</h4>
<p>To add Cron Triggers in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker &gt; <strong>Settings</strong> &gt; <strong>Triggers</strong> &gt; <strong>Cron Triggers</strong>.</li>
</ol>
<h2 id="supported-cron-expressions">Supported cron expressions</h2>
<p>Cloudflare supports cron expressions with five fields, along with most <a href="http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html#introduction">Quartz scheduler</a>-like cron syntax extensions:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Values</th>
<th>Characters</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minute</td>
<td>0-59</td>
<td>* , - /</td>
</tr>
<tr>
<td>Hours</td>
<td>0-23</td>
<td>* , - /</td>
</tr>
<tr>
<td>Days of Month</td>
<td>1-31</td>
<td>* , - / L W</td>
</tr>
<tr>
<td>Months</td>
<td>1-12, case-insensitive 3-letter abbreviations (&quot;JAN&quot;, &quot;aug&quot;, etc.)</td>
<td>* , - /</td>
</tr>
<tr>
<td>Weekdays</td>
<td>1-7, case-insensitive 3-letter abbreviations (&quot;MON&quot;, &quot;fri&quot;, etc.)</td>
<td>* , - / L #</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16637.md")
</aside>
<h3 id="examples">Examples</h3>
<p>Some common time intervals that may be useful for setting up your Cron Trigger:</p>
<ul>
<li>
<p><code>* * * * *</code></p>
<ul>
<li>At every minute</li>
</ul>
</li>
<li>
<p><code>*/30 * * * *</code></p>
<ul>
<li>At every 30th minute</li>
</ul>
</li>
<li>
<p><code>45 * * * *</code></p>
<ul>
<li>On the 45th minute of every hour</li>
</ul>
</li>
<li>
<p><code>0 17 * * sun</code> or <code>0 17 * * 1</code></p>
<ul>
<li>17:00 (UTC) on Sunday</li>
</ul>
</li>
<li>
<p><code>10 7 * * mon-fri</code> or <code>10 7 * * 2-6</code></p>
<ul>
<li>07:10 (UTC) on weekdays</li>
</ul>
</li>
<li>
<p><code>0 15 1 * *</code></p>
<ul>
<li>15:00 (UTC) on first day of the month</li>
</ul>
</li>
<li>
<p><code>0 18 * * 6L</code> or <code>0 18 * * friL</code></p>
<ul>
<li>18:00 (UTC) on the last Friday of the month</li>
</ul>
</li>
<li>
<p><code>59 23 LW * *</code></p>
<ul>
<li>23:59 (UTC) on the last weekday of the month</li>
</ul>
</li>
</ul>
<h2 id="test-cron-triggers-locally">Test Cron Triggers locally</h2>
<p>Test Cron Triggers using Wrangler with <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>, or using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>. This exposes a <code>/cdn-cgi/local/scheduled</code> route, which can be used to test using an HTTP request. If you are using the Cloudflare Vite Plugin, ensure that you use the correct vite port for the following commands (Vite defaults to 5173).</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/cdn-cgi/local/scheduled&quot;&#10;</code></pre>
<p>By default, the endpoint returns the scheduled handler outcome as text. To return the
structured scheduled handler result as JSON, pass <code>?format=json</code>.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?format=json&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;outcome&quot;: &quot;ok&quot;,&#10;  &quot;noRetry&quot;: false&#10;}&#10;</code></pre>
<p>The <code>noRetry</code> field is <code>true</code> when the scheduled handler calls
<code>controller.noRetry()</code>.</p>
<p>To simulate different cron patterns, a <code>cron</code> query parameter can be passed in.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Optionally, you can also pass a <code>time</code> query parameter to override <code>controller.scheduledTime</code> in your scheduled event listener.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&amp;time=1745856238000&quot;&#10;</code></pre>
<h2 id="view-past-events">View past events</h2>
<p>To view the execution history of Cron Triggers, view <strong>Cron Events</strong>:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your <strong>Worker</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Under <strong>Trigger Events</strong>, select <strong>View events</strong>.</li>
</ol>
<p>Cron Events stores the 100 most recent invocations of the Cron scheduled event. <a href="/workers/observability/logs/workers-logs">Workers Logs</a> also records invocation logs for the Cron Trigger with a longer retention period and a filter &amp; query interface. If you are interested in an API to access Cron Events, use Cloudflare's <a href="/analytics/graphql-api">GraphQL Analytics API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16636.md")
</aside>
<p>Refer to <a href="/workers/observability/metrics-and-analytics/">Metrics and Analytics</a> for more information.</p>
<h2 id="remove-a-cron-trigger">Remove a Cron Trigger</h2>
<h3 id="via-the-dashboard-1">Via the dashboard</h3>
<p>To delete a Cron Trigger on a deployed Worker via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Go to <strong>Triggers</strong> &gt; select the three dot icon next to the Cron Trigger you want to remove &gt; <strong>Delete</strong>.</li>
</ol>
<h4 id="via-the-wrangler-configuration-file-workers-wrangler-configuration-1">Via the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></h4>
<p>If a Worker is managed with Wrangler, Cron Triggers should be exclusively managed through the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>When deploying a Worker with Wrangler any previous Cron Triggers are replaced with those specified in the <code>triggers</code> array.</p>
<ul>
<li>If the <code>crons</code> property is an empty array then all the Cron Triggers are removed.</li>
<li>If the <code>triggers</code> or <code>crons</code> property are <code>undefined</code> then the currently deploy Cron Triggers are left in-place.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16646.md")
</div>
<h2 id="limits">Limits</h2>
<p>Refer to <a href="/workers/platform/limits/">Limits</a> to track the maximum number of Cron Triggers per Worker.</p>
<h2 id="green-compute">Green Compute</h2>
<p>With Green Compute enabled, your Cron Triggers will only run on Cloudflare points of presence that are located in data centers that are powered purely by renewable energy. Organizations may claim that they are powered by 100 percent renewable energy if they have procured sufficient renewable energy to account for their overall energy use.</p>
<p>Renewable energy can be purchased in a number of ways, including through on-site generation (wind turbines, solar panels), directly from renewable energy producers through contractual agreements called Power Purchase Agreements (PPA), or in the form of Renewable Energy Credits (REC, IRECs, GoOs) from an energy credit market.</p>
<p>Green Compute can be configured at the account level:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>Account details</strong> section, find <strong>Compute Setting</strong>.</li>
<li>Select <strong>Change</strong>.</li>
<li>Select <strong>Green Compute</strong>.</li>
<li>Select <strong>Confirm</strong>.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/wrangler/configuration/#triggers">Triggers</a> - Review Wrangler configuration file syntax for Cron Triggers.</li>
<li>Learn how to access Cron Triggers in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a> for an optimized experience.</li>
</ul>
