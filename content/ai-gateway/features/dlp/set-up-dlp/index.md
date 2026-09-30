---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/
  description: Enable and configure DLP policies on your AI Gateway to scan prompts and responses for sensitive data.
  full_title: Set up Data Loss Prevention (DLP) · Cloudflare AI Gateway docs
  head_html: <title>Set up Data Loss Prevention (DLP) · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable and configure DLP policies on your AI Gateway to scan prompts and responses for sensitive data."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/index.md"><meta property="og:title" content="Set up Data Loss Prevention (DLP) · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable and configure DLP policies on your AI Gateway to scan prompts and responses for sensitive data."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/#page","headline":"Set up Data Loss Prevention (DLP) \u00b7 Cloudflare AI Gateway docs","description":"Enable and configure DLP policies on your AI Gateway to scan prompts and responses for sensitive data.","url":"https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/features/dlp/set-up-dlp/
  schema: 1
---
<p>Add Data Loss Prevention (DLP) to any AI Gateway to start scanning AI prompts and responses for sensitive data.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An existing <a href="/ai-gateway/get-started/">AI Gateway</a></li>
</ul>
<h2 id="enable-dlp-for-ai-gateway">Enable DLP for AI Gateway</h2>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select a gateway where you want to enable DLP.</li>
<li>Go to the <strong>Firewall</strong> tab.</li>
<li>Toggle <strong>Data Loss Prevention (DLP)</strong> to <strong>On</strong>.</li>
</ol>
<h2 id="add-dlp-policies">Add DLP policies</h2>
<p>After enabling DLP, you can create policies to define how sensitive data should be handled:</p>
<ol>
<li>Under the DLP section, click <strong>Add Policy</strong>.</li>
<li>Configure the following fields for each policy:
<ul>
<li><strong>Policy ID</strong>: Enter a unique name for this policy (e.g., &quot;Block-PII-Requests&quot;)</li>
<li><strong>DLP Profiles</strong>: Select the DLP profiles to check against. AI requests/responses will be checked against each of the selected profiles. Available profiles include:
<ul>
<li><strong>Financial Information</strong> - Credit cards, bank accounts, routing numbers</li>
<li><strong>Personal Identifiable Information (PII)</strong> - Names, addresses, phone numbers</li>
<li><strong>Government Identifiers</strong> - SSNs, passport numbers, driver's licenses</li>
<li><strong>Healthcare Information</strong> - Medical record numbers, patient data</li>
<li><strong>Custom Profiles</strong> - Organization-specific data patterns</li>
</ul>
</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2897.md")
</aside>
<ul>
<li>
<p><strong>Action</strong>: Choose the action to take when any of the selected profiles match:</p>
<ul>
<li><strong>Flag</strong> - Record the detection for audit purposes without blocking</li>
<li><strong>Block</strong> - Prevent the request/response from proceeding</li>
</ul>
</li>
<li>
<p><strong>Check</strong>: Select what to scan:</p>
<ul>
<li><strong>Request</strong> - Scan user prompts sent to AI providers</li>
<li><strong>Response</strong> - Scan AI model responses before returning to users</li>
<li><strong>Both</strong> - Scan both requests and responses</li>
</ul>
</li>
</ul>
<ol start="3">
<li>Click <strong>Save</strong> to save your policy configuration.</li>
</ol>
<h2 id="manage-dlp-policies">Manage DLP policies</h2>
<p>You can create multiple DLP policies with different configurations:</p>
<ul>
<li><strong>Add multiple policies</strong>: Click <strong>Add Policy</strong> to create additional policies with different profile combinations or actions</li>
<li><strong>Enable/disable policies</strong>: Use the toggle next to each policy to individually enable or disable them without deleting the configuration</li>
<li><strong>Edit policies</strong>: Click on any existing policy to modify its settings</li>
<li><strong>Save changes</strong>: Always click <strong>Save</strong> after making any changes to apply them</li>
</ul>
<h2 id="test-your-configuration">Test your configuration</h2>
<p>After configuring DLP settings:</p>
<ol>
<li>Make a test AI request through your gateway that contains sample sensitive data.</li>
<li>Check the <strong>AI Gateway Logs</strong> to verify DLP scanning is working.</li>
<li>Review the detection results and adjust profiles or actions as needed.</li>
</ol>
<h2 id="monitor-dlp-events">Monitor DLP events</h2>
<h3 id="viewing-dlp-logs-in-ai-gateway">Viewing DLP logs in AI Gateway</h3>
<p>DLP events are integrated into your AI Gateway logs. When a DLP policy matches, the log entry includes details about the match alongside standard log fields like provider, model, tokens, and cost.</p>
<ol>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong> &gt; your gateway &gt; <strong>Logs</strong>.</li>
<li>Select any log entry to view detailed information. For requests where DLP policies were triggered, the log entry includes additional DLP fields:</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Action</td>
<td>The action taken by the DLP policy: <code>FLAG</code> or <code>BLOCK</code></td>
</tr>
<tr>
<td>DLP Policies Matched</td>
<td>The IDs of the DLP policies that matched</td>
</tr>
<tr>
<td>DLP Profiles Matched</td>
<td>The IDs of the DLP profiles that triggered within each matched policy</td>
</tr>
<tr>
<td>DLP Entries Matched</td>
<td>The specific detection entry IDs that matched within each profile</td>
</tr>
<tr>
<td>DLP Check</td>
<td>Whether the match occurred in the <code>REQUEST</code>, <code>RESPONSE</code>, or both</td>
</tr>
</tbody>
</table>
<h3 id="dlp-fields-in-the-logs-api">DLP fields in the Logs API</h3>
<p>When you retrieve logs through the <a href="/api/resources/ai_gateway/subresources/logs/methods/list/">Logs API</a>, log entries for requests where DLP policies matched include DLP-specific fields in the response. These fields contain the same match data surfaced in the dashboard and in the <code>cf-aig-dlp</code> response header, including the action taken, matched policy IDs, matched profile IDs, and entry IDs.</p>
<p>For more information on log fields, refer to the <a href="/ai-gateway/observability/logging/">Logging documentation</a>.</p>
<h3 id="filter-dlp-events">Filter DLP events</h3>
<p>To view only DLP-related requests:</p>
<ol>
<li>On the <strong>Logs</strong> tab, select <strong>Add Filter</strong>.</li>
<li>Select <strong>DLP Action</strong> from the filter options.</li>
<li>Choose to filter by:
<ul>
<li><strong>FLAG</strong> - Show only requests where sensitive data was flagged</li>
<li><strong>BLOCK</strong> - Show only requests that were blocked due to DLP policies</li>
</ul>
</li>
</ol>
<h2 id="error-handling">Error handling</h2>
<p>When DLP policies are triggered, your application will receive additional information through response headers and error codes.</p>
<h3 id="dlp-response-header">DLP response header</h3>
<p>When a request matches DLP policies (whether flagged or blocked), an additional <code>cf-aig-dlp</code> header is returned containing detailed information about the match:</p>
<h4 id="header-schema">Header schema</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;findings&quot;: [&#10;    {&#10;      &quot;profile&quot;: {&#10;        &quot;context&quot;: {},&#10;        &quot;entry_ids&quot;: [&quot;string&quot;],&#10;        &quot;profile_id&quot;: &quot;string&quot;&#10;      },&#10;      &quot;policy_ids&quot;: [&quot;string&quot;],&#10;      &quot;check&quot;: &quot;REQUEST&quot; | &quot;RESPONSE&quot;&#10;    }&#10;  ],&#10;  &quot;action&quot;: &quot;BLOCK&quot; | &quot;FLAG&quot;&#10;}&#10;</code></pre>
<h4 id="example-header-value">Example header value</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;findings&quot;: [&#10;		{&#10;			&quot;profile&quot;: {&#10;				&quot;context&quot;: {},&#10;				&quot;entry_ids&quot;: [&#10;					&quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;					&quot;f7e8d9c0-b1a2-3456-789a-bcdef0123456&quot;&#10;				],&#10;				&quot;profile_id&quot;: &quot;12345678-90ab-cdef-1234-567890abcdef&quot;&#10;			},&#10;			&quot;policy_ids&quot;: [&quot;block_financial_data&quot;],&#10;			&quot;check&quot;: &quot;REQUEST&quot;&#10;		}&#10;	],&#10;	&quot;action&quot;: &quot;BLOCK&quot;&#10;}&#10;</code></pre>
<p>Use this header to programmatically detect which DLP profiles and entries were matched, which policies triggered, and whether the match occurred in the request or response.</p>
<h3 id="error-codes-for-blocked-requests">Error codes for blocked requests</h3>
<p>When DLP blocks a request, your application will receive structured error responses:</p>
<ul>
<li>
<p><strong>Request blocked by DLP</strong></p>
<ul>
<li><code>&quot;code&quot;: 2029</code></li>
<li><code>&quot;message&quot;: &quot;Request content blocked due to DLP policy violations&quot;</code></li>
</ul>
</li>
<li>
<p><strong>Response blocked by DLP</strong></p>
<ul>
<li><code>&quot;code&quot;: 2030</code></li>
<li><code>&quot;message&quot;: &quot;Response content blocked due to DLP policy violations&quot;</code></li>
</ul>
</li>
</ul>
<p>Handle these errors in your application:</p>
<pre tabindex="0"><code class="language-js">try {&#10;  const res = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: userInput&#10;  }, {&#10;    gateway: {id: &#x27;your-gateway-id&#x27;}&#10;  })&#10;  return Response.json(res)&#10;} catch (e) {&#10;  if ((e as Error).message.includes(&#x27;2029&#x27;)) {&#10;    return new Response(&#x27;Request contains sensitive data and cannot be processed.&#x27;)&#10;  }&#10;  if ((e as Error).message.includes(&#x27;2030&#x27;)) {&#10;    return new Response(&#x27;AI response was blocked due to sensitive content.&#x27;)&#10;  }&#10;  return new Response(&#x27;AI request failed&#x27;)&#10;}&#10;</code></pre>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Start with flagging</strong>: Begin with &quot;Flag&quot; actions to understand what data is being detected before implementing blocking</li>
<li><strong>Tune confidence levels</strong>: Adjust detection sensitivity based on your false positive tolerance</li>
<li><strong>Use appropriate profiles</strong>: Select DLP profiles that match your data protection requirements</li>
<li><strong>Monitor regularly</strong>: Review DLP events to ensure policies are working as expected</li>
<li><strong>Test thoroughly</strong>: Validate DLP behavior with sample sensitive data before production deployment</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For general AI Gateway troubleshooting, refer to <a href="/ai-gateway/reference/troubleshooting/">Troubleshooting</a>.</p>
<h3 id="dlp-not-triggering">DLP not triggering</h3>
<ul>
<li>Verify DLP toggle is enabled for your gateway</li>
<li>Ensure selected DLP profiles are appropriate for your test data</li>
<li>Confirm confidence levels aren't set too high</li>
</ul>
<h3 id="unexpected-blocking">Unexpected blocking</h3>
<ul>
<li>Review DLP logs to see which profiles triggered</li>
<li>Consider lowering confidence levels for problematic profiles</li>
<li>Test with different sample data to understand detection patterns</li>
<li>Adjust profile selections if needed</li>
</ul>
<p>For additional support with DLP configuration, refer to the <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention documentation</a> or contact your Cloudflare support team.</p>
