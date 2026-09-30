---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/
  description: Control how Worker subrequests appear in Logpush.
  full_title: Subrequests · Cloudflare Logs docs
  head_html: <title>Subrequests · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Control how Worker subrequests appear in Logpush."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/index.md"><meta property="og:title" content="Subrequests · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control how Worker subrequests appear in Logpush."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/#page","headline":"Subrequests \u00b7 Cloudflare Logs docs","description":"Control how Worker subrequests appear in Logpush.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/subrequests/
  schema: 1
---
<p>When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines for a single visitor-facing request.</p>
<p>Each request stage can be identified by its log fields. You can also opt in to subrequest merging, which aggregates subrequest log entries into their parent request so that your Logpush job delivers one log line per visitor request.</p>
<h2 id="identifying-log-types">Identifying log types</h2>
<p>Each request stage generates its own log line. You can distinguish between them using the following fields.</p>
<p><em>Visitor request</em> — the original request from the visitor to your zone:</p>
<ul>
<li>ClientRequestSource == &quot;eyeball&quot;</li>
</ul>
<p><em>Origin request</em> — a request forwarded from Cloudflare to your origin server:</p>
<ul>
<li>OriginIP != &quot;&quot;, or</li>
<li>OriginResponseStatus != 0 (for example, OriginResponseStatus == 200)</li>
</ul>
<p><em>Worker subrequest</em> — a fetch call dispatched by a Worker:</p>
<ul>
<li>WorkerSubrequest == true</li>
<li>ClientRequestSource == &quot;edgeWorkerFetch&quot;</li>
</ul>
<p>To correlate a subrequest log with its parent, match the subrequest's ParentRayID field to the RayID of the parent request.</p>
<h2 id="subrequest-merging">Subrequest merging</h2>
Subrequest merging is an opt-in feature on the http_requests dataset. With subrequest merging enabled, your Logpush job delivers one log line per visitor request, with subrequest data embedded as a nested array field on the parent log record.
<h2 id="merging-eligibility">Merging Eligibility</h2>
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10504.md")
</aside>
<h2 id="new-log-field">New log field</h2>
When subrequest merging is enabled, a `Subrequests` field (`array<object>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.
<p>The array only includes subrequests that qualify for merging based on the eligibility criteria above. Subrequests that do not qualify appear as separate log entries. The field will be empty ([]) if the request has no subrequests, or none qualify.</p>
<h2 id="enable-subrequest-merging">Enable subrequest merging</h2>
<p>Subrequest merging can be enabled via API or the Cloudflare dashboard.</p>
<h3 id="dashboard">Dashboard</h3>
1. In the Cloudflare dashboard, go to the Logpush page at the domain (also known as zone) level.
<div class="nb-dash-button"></div>
2. Select Create a Logpush job or select Edit next to an existing http_requests job.
3. Under Advanced Options, enable the Subrequest merging toggle.
4. Select Save.
<h3 id="api">API</h3>
1. To enable subrequest merging on a new job, set "merge_subrequests": true in the request body.
<h3 id="required-api-token-permissions">Required API token permissions</h3>
<p>At least one of the following token permissions is required:</p>
<ul>
<li>Logs Write</li>
</ul>
<p><strong>Create Logpush job</strong></p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs&quot; \&#10;  &#45;-request POST \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-json &#x27;{&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-east-1&quot;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&#10;        &quot;ClientIP&quot;,&#10;        &quot;ClientRequestHost&quot;,&#10;        &quot;ClientRequestMethod&quot;,&#10;        &quot;ClientRequestURI&quot;,&#10;        &quot;EdgeStartTimestamp&quot;,&#10;        &quot;EdgeResponseStatus&quot;,&#10;        &quot;RayID&quot;,&#10;        &quot;ParentRayID&quot;,&#10;        &quot;Subrequests&quot;&#10;      ],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;merge_subrequests&quot;: true,&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p><strong>To enable subrequest merging on an existing job:</strong></p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="schema-change">Schema change</h3>
@markup("md", "content/.markup/bodies/10503.md")
</aside>
<p><strong>Update Logpush job</strong></p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs/$JOB_ID&quot; \&#10;  &#45;-request PUT \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-json &#x27;{&#10;    &quot;merge_subrequests&quot;: true&#10;  }&#x27;&#10;</code></pre>
<h2 id="example-log-output">Example log output</h2>
<p>Without subrequest merging, a Worker that makes one subrequest produces two separate log records:</p>
<pre tabindex="0"><code class="language-json">{&quot;RayID&quot;:&quot;abc123&quot;,&quot;ParentRayID&quot;:&quot;&quot;,&quot;ClientIP&quot;:&quot;203.0.113.1&quot;,&quot;EdgeResponseStatus&quot;:200, ...}&#10;{&quot;RayID&quot;:&quot;def456&quot;,&quot;ParentRayID&quot;:&quot;abc123&quot;,&quot;ClientIP&quot;:&quot;203.0.113.1&quot;,&quot;EdgeResponseStatus&quot;:200, ...}&#10;</code></pre>
<p>With subrequest merging enabled, a single record is produced with the subrequest nested inside:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;RayID&quot;: &quot;abc123&quot;,&#10;  &quot;ParentRayID&quot;: &quot;&quot;,&#10;  &quot;ClientIP&quot;: &quot;203.0.113.1&quot;,&#10;  &quot;EdgeResponseStatus&quot;: 200,&#10;  &quot;Subrequests&quot;: [&#10;    {&#10;      &quot;RayID&quot;: &quot;def456&quot;,&#10;      &quot;ClientIP&quot;: &quot;203.0.113.1&quot;,&#10;      &quot;EdgeResponseStatus&quot;: 200&#10;    }&#10;  ]&#10;}&#10;</code></pre>
