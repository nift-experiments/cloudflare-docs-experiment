---
cp9:
  canonical: https://developers.cloudflare.com/changelog/30/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 30 | Cloudflare Docs
  head_html: <title>Changelog - page 30 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/30/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 30"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/30/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/30/#page","headline":"Changelog - page 30 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/30/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/30/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-12-04">Dec 4, 2025</time><div>
<h2 id="post-2025-12-03-reusable-access-policies"><a href="/changelog/post/2025-12-03-reusable-access-policies/">One-click Access protection for Workers now creates reusable Cloudflare Access policies</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers applications now use reusable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policies</a> to reduce duplication and simplify access management across multiple Workers.</p>
<p>Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:</p>
<ul>
<li>
<p><strong>Preview URLs</strong>: All Workers preview URLs share a single &quot;Cloudflare Workers Preview URLs&quot; policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.</p>
</li>
<li>
<p><strong>Production workers.dev URLs</strong>: When enabled, each Worker gets its own reusable policy (named <code>&lt;worker-name&gt; - Production</code>) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.</p>
</li>
</ul>
<p>This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.</p>
<p>To enable Cloudflare Access on your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, click <strong>Manage Cloudflare Access</strong> to customize the policy.</li>
</ol>
<p>For more information on configuring Cloudflare Access for Workers, refer to the <a href="/workers/configuration/routing/workers-dev/#manage-access-to-workersdev">Workers Access documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-04">Dec 4, 2025</time><div>
<h2 id="post-2025-12-03-submission-terminology-update"><a href="/changelog/post/2025-12-03-submission-terminology-update/">Reclassifications to Submissions</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.</p>
<p>Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassification-submission.png" alt="nav_example" /></p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-03">Dec 3, 2025</time><div>
<h2 id="post-2025-12-03-emergency-waf-release"><a href="/changelog/post/2025-12-03-emergency-waf-release/">WAF Release - 2025-12-03 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>The WAF rule deployed yesterday to block unsafe deserialization-based RCE has been updated. The rule description now reads “React – RCE – CVE-2025-55182”, explicitly mapping to the recently disclosed React Server Components vulnerability. Detection logic remains unchanged.</p>
<p><strong>Key Findings</strong></p>
<p>Rule description updated to reference React – RCE – CVE-2025-55182 while retaining existing unsafe-deserialization detection.</p>
<p><strong>Impact</strong></p>
<p>Improved classification and traceability with no change to coverage against remote code execution attempts.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-02">Dec 2, 2025</time><div>
<h2 id="post-2025-12-02-emergency-waf-release"><a href="/changelog/post/2025-12-02-emergency-waf-release/">WAF Release - 2025-12-02 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's emergency release introduces a new rule to block a critical RCE vulnerability in widely-used web frameworks through unsafe deserialization patterns.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for RCE Generic Framework to block malicious POST requests containing unsafe deserialization patterns. If successfully exploited, this vulnerability allows attackers with network access via HTTP to execute arbitrary code remotely.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation allows unauthenticated attackers to execute arbitrary code remotely through crafted serialization payloads, enabling complete system compromise, data exfiltration, and potential lateral movement within affected environments.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-01">Dec 1, 2025</time><div>
<h2 id="post-2025-12-01-waf-release"><a href="/changelog/post/2025-12-01-waf-release/">WAF Release - 2025-12-01</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for remote code execution attempts targeting Monsta FTP (CVE-2025-34299), alongside improvements to an existing XSS detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-34299 is a critical remote code execution flaw in Monsta FTP, arising from improper handling of user-supplied parameters within the file-handling interface. Certain builds allow crafted requests to bypass sanitization and reach backend PHP functions that execute arbitrary commands. Attackers can send manipulated parameters through the web panel to trigger command execution within the application’s runtime environment.</li>
</ul>
<p><strong>Impact</strong></p>
<p>If exploited, the vulnerability enables full remote command execution on the underlying server, allowing takeover of the hosting environment, unauthorized file access, and potential lateral movement. As the flaw can be triggered without authentication on exposed Monsta FTP instances, it represents a severe risk for publicly reachable deployments.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="480da5e7984542a6b8d8d88da4fcc8a8">a4fcc8a8</code>
</td>
<td>N/A</td>
<td>Monsta FTP - Remote Code Execution - CVE:CVE-2025-34299</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2380b125c53d42ac94479c42b7492846">b7492846</code>
</td>
<td>N/A</td>
<td>XSS - JS Context Escape - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS - JS Context Escape" (ID: <code class="nb-rule-id" title="c1ad1bc37caa4cbeb104f44f7a3769d3">7a3769d3</code>)</td>
</tr>  
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-26">Nov 26, 2025</time><div>
<h2 id="post-2025-11-26-agents-resumable-streaming"><a href="/changelog/post/2025-11-26-agents-resumable-streaming/">Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.</p>
<h4 id="2025-11-26-agents-resumable-streaming-resumable-streaming">Resumable streaming</h4>
<p><code>AIChatAgent</code> now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:</p>
<ul>
<li>Long-running AI responses</li>
<li>Users on unreliable networks</li>
<li>Users switching between devices mid-conversation</li>
<li>Background tasks where users navigate away and return</li>
<li>Real-time collaboration where multiple clients need to stay in sync</li>
</ul>
<p>Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.</p>
<h4 id="2025-11-26-agents-resumable-streaming-other-improvements">Other improvements</h4>
<ul>
<li>Default JSON schema validator added to MCP client</li>
<li><a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">Schedules</a> can now safely destroy the agent</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-mcp-client-api-improvements">MCP client API improvements</h4>
<p>The <code>MCPClientManager</code> API has been redesigned for better clarity and control:</p>
<ul>
<li><strong>New <code>registerServer()</code> method</strong>: Register MCP servers without immediately connecting</li>
<li><strong>New <code>connectToServer()</code> method</strong>: Establish connections to registered servers</li>
<li><strong>Improved reconnect logic</strong>: <code>restoreConnectionsFromStorage()</code> now properly handles failed connections</li>
</ul>
<pre tabindex="0"><code class="language-ts">// Register a server to Agent&#10;const { id } = await this.mcp.registerServer({&#10;	name: &quot;my-server&quot;,&#10;	url: &quot;https://my-mcp-server.example.com&quot;,&#10;});&#10;&#10;// Connect when ready&#10;await this.mcp.connectToServer(id);&#10;&#10;// Discover tools, prompts and resources&#10;await this.mcp.discoverIfConnected(id);&#10;</code></pre>
<p>The SDK now includes a formalized <code>MCPConnectionState</code> enum with states: <code>idle</code>, <code>connecting</code>, <code>authenticating</code>, <code>connected</code>, <code>discovering</code>, and <code>ready</code>.</p>
<h4 id="2025-11-26-agents-resumable-streaming-enhanced-mcp-discovery">Enhanced MCP discovery</h4>
<p>MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The <code>MCPClientConnection</code> class now includes a dedicated <code>discover()</code> method with improved reliability:</p>
<ul>
<li>Supports cancellation via AbortController</li>
<li>Configurable timeout (default 15s)</li>
<li>Discovery failures now throw errors immediately instead of silently continuing</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-bug-fixes">Bug fixes</h4>
<ul>
<li>Fixed a bug where <a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">schedules</a> meant to fire immediately with this.schedule(0, ...) or <code>this.schedule(new Date(), ...)</code> would not fire</li>
<li>Fixed an issue where schedules that took longer than 30 seconds would occasionally time out</li>
<li>Fixed SSE transport now properly forwards session IDs and request headers</li>
<li>Fixed AI SDK stream events conversion to UIMessageStreamPart</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-25">Nov 25, 2025</time><div>
<h2 id="post-2025-11-25-zombie-endpoint-risk-label"><a href="/changelog/post/2025-11-25-zombie-endpoint-risk-label/">New Zombie API detection for API Shield</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the <code>cf-risk-zombie</code> <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">risk label</a> is applied.</p>
<p>The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.</p>
<p>Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">fallthrough rule</a> to prevent communication with endpoints removed from Endpoint Management.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-25">Nov 25, 2025</time><div>
<h2 id="post-2025-11-25-audit-logs-for-cache-purge-events"><a href="/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/">Audit Logs for Cache Purge Events</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:</p>
<ul>
<li>Purge everything</li>
<li>List of prefixes</li>
<li>List of tags</li>
<li>List of hosts</li>
<li>List of files</li>
</ul>
<h4 id="2025-11-25-audit-logs-for-cache-purge-events-example">Example</h4>
<p>The detailed audit payload is visible within the Cloudflare Dashboard (under <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>) and via the API. Below is an example of the Audit Logs v2 payload structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;action&quot;: {&#10;    &quot;result&quot;: &quot;success&quot;,&#10;    &quot;type&quot;: &quot;create&quot;&#10;  },&#10;  &quot;actor&quot;: {&#10;    &quot;id&quot;: &quot;1234567890abcdef&quot;,&#10;    &quot;email&quot;: &quot;user@example.com&quot;,&#10;    &quot;type&quot;: &quot;user&quot;&#10;  },&#10;  &quot;resource&quot;: {&#10;    &quot;product&quot;: &quot;purge_cache&quot;,&#10;    &quot;request&quot;: {&#10;      &quot;files&quot;: [&#10;        &quot;https://example.com/images/logo.png&quot;,&#10;        &quot;https://example.com/css/styles.css&quot;&#10;      ]&#10;    }&#10;  },&#10;  &quot;zone&quot;: {&#10;    &quot;id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-11-25-audit-logs-for-cache-purge-events-get-started">Get started</h4>
<p>To get started, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-25">Nov 25, 2025</time><div>
<h2 id="post-2025-11-25-flux-2-dev-workers-ai"><a href="/changelog/post/2025-11-25-flux-2-dev-workers-ai/">Launching FLUX.2 [dev] on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 [dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.</p>
<p>Read the <a href="https://bfl.ai/flux2">BFL blog</a> to learn more about the model itself. Read our <a href="https://blog.cloudflare.com/flux-2-workers-ai">Cloudflare blog</a> to see the model in action, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-dev/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>. Note, we expect to drop pricing in the next few days after iterating on the model performance.</p>
<h4 id="2025-11-25-flux-2-dev-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form steps=25&#10;  &#45;-form width=1024&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">&#10;const form = new FormData();&#10;form.append(&#x27;prompt&#x27;, &#x27;a sunset with a dog&#x27;);&#10;form.append(&#x27;width&#x27;, &#x27;1024&#x27;);&#10;form.append(&#x27;height&#x27;, &#x27;1024&#x27;);&#10;&#10;//this dummy request is temporary hack&#10;//we&#x27;re pushing a change to address this soon&#10;const formRequest = new Request(&#x27;http://dummy&#x27;, {&#10;  method: &#x27;POST&#x27;,&#10;  body: form&#10;});&#10;const formStream = formRequest.body;&#10;const formContentType = formRequest.headers.get(&#x27;content-type&#x27;) || &#x27;multipart/form-data&#x27;;&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {&#10;  multipart: {&#10;    body: formStream,&#10;    contentType: formContentType&#10;  }&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
</details>
<pre tabindex="0"><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-dev">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form steps=25
--form width=1024
--form height=1024</p>
<pre tabindex="0"><code>Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1and style it like image 0')</p>
<p>//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('<a href="http://dummy">http://dummy</a>', {
method: 'POST',
body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {
multipart: {
body: form,
contentType: &quot;multipart/form-data&quot;
}
})</p>
<pre tabindex="0"><code>&#10;&#35;# JSON Prompting&#10;&#10;The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the &#x27;prompt&#x27; field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.&#10;&#10;&lt;details&gt;&#10;  &lt;summary&gt;JSON Prompting Schema&lt;/summary&gt;&#10;</code></pre>
<p>{
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;scene&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Overall scene setting or location&quot;
},
&quot;subjects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;type&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)&quot;
},
&quot;description&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Physical attributes, clothing, accessories&quot;
},
&quot;pose&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Action or stance&quot;
},
&quot;position&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;foreground&quot;, &quot;midground&quot;, &quot;background&quot;],
&quot;description&quot;: &quot;Depth placement in scene&quot;
}
},
&quot;required&quot;: [&quot;type&quot;, &quot;description&quot;, &quot;pose&quot;, &quot;position&quot;]
}
},
&quot;style&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)&quot;
},
&quot;color_palette&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;minItems&quot;: 3,
&quot;maxItems&quot;: 3,
&quot;description&quot;: &quot;Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])&quot;
},
&quot;lighting&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)&quot;
},
&quot;mood&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)&quot;
},
&quot;background&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Background environment details&quot;
},
&quot;composition&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [
&quot;rule of thirds&quot;,
&quot;circular arrangement&quot;,
&quot;framed by foreground&quot;,
&quot;minimalist negative space&quot;,
&quot;S-curve&quot;,
&quot;vanishing point center&quot;,
&quot;dynamic off-center&quot;,
&quot;leading leads&quot;,
&quot;golden spiral&quot;,
&quot;diagonal energy&quot;,
&quot;strong verticals&quot;,
&quot;triangular arrangement&quot;
],
&quot;description&quot;: &quot;Compositional technique&quot;
},
&quot;camera&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;angle&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;eye level&quot;, &quot;low angle&quot;, &quot;slightly low&quot;, &quot;bird's-eye&quot;, &quot;worm's-eye&quot;, &quot;over-the-shoulder&quot;, &quot;isometric&quot;],
&quot;description&quot;: &quot;Camera perspective&quot;
},
&quot;distance&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;close-up&quot;, &quot;medium close-up&quot;, &quot;medium shot&quot;, &quot;medium wide&quot;, &quot;wide shot&quot;, &quot;extreme wide&quot;],
&quot;description&quot;: &quot;Framing distance&quot;
},
&quot;focus&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;deep focus&quot;, &quot;macro focus&quot;, &quot;selective focus&quot;, &quot;sharp on subject&quot;, &quot;soft background&quot;],
&quot;description&quot;: &quot;Focus type&quot;
},
&quot;lens&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;14mm&quot;, &quot;24mm&quot;, &quot;35mm&quot;, &quot;50mm&quot;, &quot;70mm&quot;, &quot;85mm&quot;],
&quot;description&quot;: &quot;Focal length (wide to telephoto)&quot;
},
&quot;f-number&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Aperture (e.g., f/2.8, the smaller the number the more blurry the background)&quot;
},
&quot;ISO&quot;: {
&quot;type&quot;: &quot;number&quot;,
&quot;description&quot;: &quot;Light sensitivity value (comfortable range between 100 &amp; 6400, lower = less sensitivity)&quot;
}
}
},
&quot;effects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;description&quot;: &quot;Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')&quot;
}
},
&quot;required&quot;: [&quot;scene&quot;, &quot;subjects&quot;]
}</p>
<pre tabindex="0"><code>&lt;/details&gt;&#10;&#10;&#35;# Other features to try&#10;&#10;&#45; The model also supports the most common latin and non-latin character languages&#10;&#45; You can prompt the model with specific hex codes like `#2ECC71`&#10;&#45; Try creating digital assets like landing pages, comic strips, infographics too!&#10;&#10;&#10;</code></pre>
<h4 id="2025-11-25-flux-2-dev-workers-ai-json-prompting">JSON Prompting</h4><h4 id="2025-11-25-flux-2-dev-workers-ai-other-features-to-try">Other features to try</h4></div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-24">Nov 24, 2025</time><div>
<h2 id="post-2025-11-24-radar-cloud-observability"><a href="/changelog/post/2025-11-24-radar-cloud-observability/">Cloud Services Observability in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> introduces HTTP Origins insights, providing visibility into the status of traffic between Cloudflare's global network and cloud-based origin infrastructure.</p>
<p>The new <a href="/api/resources/radar/subresources/origins/"><code>Origins</code></a> API provides provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/origins/methods/list/"><code>/origins</code></a> - Lists all origins (cloud providers and associated regions).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/get/"><code>/origins/{origin}</code></a> - Retrieves information about a specific origin (cloud provider).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries/"><code>/origins/timeseries</code></a> - Retrieves normalized time series data for a specific origin, including the following metrics:
<ul>
<li><code>REQUESTS</code>: Number of requests</li>
<li><code>CONNECTION_FAILURES</code>: Number of connection failures</li>
<li><code>RESPONSE_HEADER_RECEIVE_DURATION</code>: Duration of the response header receive</li>
<li><code>TCP_HANDSHAKE_DURATION</code>: Duration of the TCP handshake</li>
<li><code>TCP_RTT</code>: TCP round trip time</li>
<li><code>TLS_HANDSHAKE_DURATION</code>: Duration of the TLS handshake</li>
</ul>
</li>
<li><a href="/api/resources/radar/subresources/origins/methods/summary/"><code>/origins/summary</code></a> - Retrieves HTTP requests to origins summarized by a dimension.</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries_groups/"><code>/origins/timeseries_groups</code></a> - Retrieves timeseries data for HTTP requests to origins grouped by a dimension.</li>
</ul>
<p>The following dimensions are available for the <code>summary</code> and <code>timeseries_groups</code> endpoints:</p>
<ul>
<li><code>region</code>: Origin region</li>
<li><code>success_rate</code>: Success rate of requests (2XX versus 5XX response codes)</li>
<li><code>percentile</code>: Percentiles of metrics listed above</li>
</ul>
<p>Additionally, the <a href="/api/resources/radar/subresources/annotations/"><code>Annotations</code></a> and <a href="/api/resources/radar/subresources/traffic_anomalies/"><code>Traffic Anomalies</code></a> APIs have been extended to support origin outages and anomalies, enabling automated detection and alerting for origin infrastructure issues.</p>
<p><img src="/assets/upstream/images/radar/cloud-service-status.png" alt="Screenshot of the cloud service status heatmap" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/cloud-observatory">new Radar page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-24">Nov 24, 2025</time><div>
<h2 id="post-2025-11-24-waf-release"><a href="/changelog/post/2025-11-24-waf-release/">WAF Release - 2025-11-24</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the <code>CGIINFO</code> header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.</p>
<p><strong>Impact</strong></p>
<ul>
<li>FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated <code>CGIINFO</code> header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b957ace6e9844bf29244401c4e2e1a2e">4e2e1a2e</code>
</td>
<td>N/A</td>
<td>FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e3871391a93248fa98a78e03b6c44ed5">b6c44ed5</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e6b1b66e0e3b46969102baed900f4015">900f4015</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>)</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-fuse-support-in-containers"><a href="/changelog/post/2025-11-21-fuse-support-in-containers/">Mount R2 buckets in Containers</a></h2>
<div class="changelog-badges"><span>containers</span><span>r2</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with <a href="/r2/">R2</a> using standard filesystem operations.</p>
<p>Common use cases include:</p>
<ul>
<li>Bootstrapping containers with datasets, models, or dependencies for <a href="/sandbox/">sandboxes</a> and <a href="/agents/">agent</a> environments</li>
<li>Persisting user configuration or application state without managing downloads</li>
<li>Accessing large static files without bloating container images or downloading at startup</li>
</ul>
<p>FUSE adapters like <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, <a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a>, and <a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> can be installed in your container image and configured to mount buckets at startup.</p>
<pre tabindex="0"><code class="language-dockerfile">FROM alpine:3.20&#10;&#10;&#35; Install FUSE and dependencies&#10;RUN apk update &amp;&amp; \&#10;    apk add --no-cache ca-certificates fuse curl bash&#10;&#10;&#35; Install tigrisfs&#10;RUN ARCH=$(uname -m) &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;x86_64&quot; ]; then ARCH=&quot;amd64&quot;; fi &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;aarch64&quot; ]; then ARCH=&quot;arm64&quot;; fi &amp;&amp; \&#10;    VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o &#x27;&quot;tag_name&quot;: &quot;[^&quot;]*&#x27; | cut -d&#x27;&quot;&#x27; -f4) &amp;&amp; \&#10;    curl -L &quot;https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz&quot; -o /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ &amp;&amp; \&#10;    rm /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    chmod +x /usr/local/bin/tigrisfs&#10;&#10;&#35; Create startup script that mounts bucket&#10;RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    mkdir -p /mnt/r2\n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;&#10;CMD [&quot;/startup.sh&quot;]&#10;</code></pre>
<p>See the <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a> example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-new-cpu-pricing"><a href="/changelog/post/2025-11-21-new-cpu-pricing/">New CPU Pricing for Containers and Sandboxes</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> pricing for CPU time is now based on active usage only, instead of provisioned resources.</p>
<p>This means that you now pay less for Containers and Sandboxes.</p>
<h4 id="2025-11-21-new-cpu-pricing-an-example-before-and-after">An Example Before and After</h4>
<p>Imagine running the <code>standard-2</code> instance type for one hour, which can use up to 1 vCPU,
but on average you use only 20% of your CPU capacity.</p>
<p>CPU-time is priced at <em>$0.00002 per vCPU-second</em>.</p>
<p>Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.</p>
<p>CPU cost would have been: <strong>$0.072</strong> — 1 vCPU * 3600 seconds * $0.00002</p>
<p>Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.</p>
<p>CPU cost is now: <strong>$0.0144</strong> — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization</p>
<p>This can significantly reduce costs for Containers and Sandboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17708.md")</aside>
<p>See the documentation to learn more about <a href="/containers/get-started/">Containers</a>, <a href="/sandbox/">Sandboxes</a>,
and <a href="/containers/platform/pricing">associated pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-Threat-Events-now-show-events-insights"><a href="/changelog/post/2025-11-21-Threat-Events-now-show-events-insights/">Threat insights are now available in the Threat Events platform</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>The threat events platform now has threat insights available for some relevant parent events. Threat intelligence analyst users can access these insights for their threat hunting activity.
Insights are also highlighted in the Cloudflare dashboard by a small <code>lightning icon</code> and the insights can refer to multiple, connected events, potentially part of the same attack or campaign and associated with the same threat actor.</p>
<p>For more information, refer to <a href="/security-center/cloudforce-one/#analyze-threat-events">Analyze threat events</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-emergency-waf-release"><a href="/changelog/post/2025-11-21-emergency-waf-release/">WAF Release - 2025-11-21</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces a critical detection for CVE-2025-61757, a vulnerability in the Oracle Identity Manager REST WebServices component.</p>
<p><strong>Key Findings</strong></p>
<p>This flaw allows unauthenticated attackers with network access over HTTP to fully compromise the Identity Manager, potentially leading to a complete takeover.</p>
<p><strong>Impact</strong></p>
<p>Oracle Identity Manager (CVE-2025-61757): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fa584616fe2241608cb8bd1339fdbe7e">39fdbe7e</code>
</td>
<td>N/A</td>
<td>Oracle Identity Manager - Pre-Auth RCE - CVE:CVE-2025-61757</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-builds-env-var-increase"><a href="/changelog/post/2025-11-21-builds-env-var-increase/">Environment variable limits increase for Workers Builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports up to 64 environment variables, and each environment variable can be up to 5 KB in size. The previous limit was 5 KB total across all environment variables.</p>
<p>This change enables better support for complex build configurations, larger application settings, and more flexible CI/CD workflows.</p>
<p>For more details, refer to the <a href="/workers/ci-cd/builds/limits-and-pricing/#definitions">build limits documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-21">Nov 21, 2025</time><div>
<h2 id="post-2025-11-21-wrangler-deploy-remote-config-management"><a href="/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/">Better local deployment flow for Cloudflare Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Until now, if a Worker had been previously deployed via the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>, a subsequent deployment done via the Cloudflare Workers CLI, <a href="/workers/wrangler/"><strong>Wrangler</strong></a>
(through the <a href="/workers/wrangler/commands/general/#deploy"><code>deploy</code> command</a>), would allow the user to override the Worker's dashboard settings without providing details on
what dashboard settings would be lost.</p>
<p>Now instead, <code>wrangler deploy</code> presents a helpful representation of the differences between the <a href="/workers/wrangler/configuration/">local configuration</a>
and the remote dashboard settings, and offers to update your local configuration file for you.</p>
<p>See example below showing a before and after for <code>wrangler deploy</code> when a local configuration is expected to override a Worker's dashboard settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-before">Before</h3>
@markup("md", "content/.markup/bodies/17791.md")</div>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-after">After</h3>
@markup("md", "content/.markup/bodies/17792.md")</div>
<p>Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.</p>
<p>Update to <a href="/workers/wrangler/">Wrangler</a> v4.50.0 or greater to take advantage of this improved deploy flow.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-20">Nov 20, 2025</time><div>
<h2 id="post-2025-11-20-terraform-v5.13.0-provider"><a href="/changelog/post/2025-11-20-terraform-v5.13.0-provider/">Terraform v5.13.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-breaking-change">Breaking Change</h4>
Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.
<p>For more specific information about the changes or the actions required, please see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0">detailed Repository changelog</a>.</p>
<h4 id="2025-11-20-terraform-v5.13.0-provider-features">Features</h4>
<ul>
<li><strong>New resources and data sources added</strong>
<ul>
<li>cloudflare_connectivity_directory</li>
<li>cloudflare_sso_connector</li>
<li>cloudflare_universal_ssl_setting</li>
</ul>
</li>
<li><strong>api_token+account_tokens:</strong> state upgrader and schema bump (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472">#6472</a>)</li>
<li><strong>docs:</strong> make docs explicit when a resource does not have import support</li>
<li><strong>magic_transit_connector:</strong> support self-serve license key (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398">#6398</a>)</li>
<li><strong>worker_version:</strong> add content_base64 support</li>
<li><strong>worker_version:</strong> boolean support for run_worker_first (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407">#6407</a>)</li>
<li><strong>workers_script_subdomains:</strong> add import support  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375">#6375</a>)</li>
<li><strong>zero_trust_access_application:</strong> add proxy_endpoint for ZT Access Application (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453">#6453</a>)</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> Switch DLP Predefined Profile endpoints, introduce enabled_entries attribute</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_token:</strong> token policy order and nested resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440">#6440</a>)</li>
<li>allow r2_bucket_event_notification to be applied twice without failing (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419">#6419</a>)</li>
<li><strong>cloudflare_worker+cloudflare_worker_version:</strong> import for the resources (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357">#6357</a>)</li>
<li><strong>dns_record:</strong> inconsistent apply error (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452">#6452</a>)</li>
<li><strong>pages_domain:</strong> resource tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338">#6338</a>)</li>
<li><strong>pages_project:</strong> unintended resource state drift (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377">#6377</a>)</li>
<li><strong>queue_consumer:</strong> id population (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181">#6181</a>)</li>
<li><strong>workers_kv:</strong> multipart request  (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367">#6367</a>)</li>
<li><strong>workers_kv:</strong> updating workers metadata attribute to be read from endpoint (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386">#6386</a>)</li>
<li><strong>workers_script_subdomain:</strong> add note to cloudflare_workers_script_subdomain about redundancy with cloudflare_worker (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383">#6383</a>)</li>
<li><strong>workers_script:</strong> allow config.run_worker_first to accept list input</li>
<li><strong>zero_trust_device_custom_profile_local_domain_fallback:</strong> drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365">#6365</a>)</li>
<li><strong>zero_trust_device_custom_profile:</strong> resolve drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364">#6364</a>)</li>
<li><strong>zero_trust_dex_test:</strong> correct configurability for 'targeted' attribute to fix drift</li>
<li><strong>zero_trust_tunnel_cloudflared_config:</strong> remove warp_routing from cloudflared_config (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471">#6471</a>)</li>
</ul>
<h4 id="2025-11-20-terraform-v5.13.0-provider-upgrading">Upgrading</h4>
We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-11-20-terraform-v5.13.0-provider-for-more-info">For more info</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-19">Nov 19, 2025</time><div>
<h2 id="post-2025-11-19-add-extra-headers-for-website-crawling"><a href="/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/">AI Search support for crawling login protected website content</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/authentication-headers/">custom HTTP headers</a> for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.</p>
<p>Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.</p>
<p>This is particularly useful for indexing content like:</p>
<ul>
<li><strong>Internal documentation</strong> behind corporate login systems</li>
<li><strong>Premium content</strong> that requires users to provide access to unlock</li>
<li><strong>Sites protected by Cloudflare Access</strong> using service tokens</li>
</ul>
<p>To add custom headers when creating an AI Search instance, select <strong>Parse options</strong>. In the <strong>Extra headers</strong> section, you can add up to five custom headers per Website data source.</p>
<p><img src="/assets/upstream/images/ai-search/ai-search-extra-headers.png" alt="Custom headers configuration in AI Search" /></p>
<p>For example, to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you can add service token credentials as custom headers:</p>
<pre tabindex="0"><code>CF-Access-Client-Id: your-token-id.access&#10;CF-Access-Client-Secret: your-token-secret&#10;</code></pre>
<p>The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.</p>
<p>Learn more about <a href="/ai-search/configuration/data-source/website/authentication-headers/">configuring custom headers for website crawling</a> in AI Search.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-18">Nov 18, 2025</time><div>
<h2 id="post-2025-11-18-temporary-adjustment-to-final-disposition-column"><a href="/changelog/post/2025-11-18-temporary-adjustment-to-final-disposition-column/">Adjustment to Final Disposition Column</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-adjustment-to-final-disposition-column">Adjustment to Final Disposition column</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-the-final-disposition-column-in-submissions-team-submissions-tab-is-changing-for-non-phishguard-customers">The <strong>Final Disposition</strong> column in <strong>Submissions</strong> &gt; <strong>Team Submissions</strong> tab is changing for non-Phishguard customers.</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-what-s-changing">What's Changing</h4>
<ul>
<li>Column will be called <strong>Status</strong> instead of <strong>Final Disposition</strong></li>
<li>Column status values will now be: <strong>Submitted</strong>, <strong>Accepted</strong> or <strong>Rejected</strong>.</li>
</ul>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-next-steps">Next Steps</h4>
<p>We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-17">Nov 17, 2025</time><div>
<h2 id="post-new-cloudflare-one-navigation-and-product-experience"><a href="/changelog/post/new-cloudflare-one-navigation-and-product-experience/">New Cloudflare One Navigation and Product Experience</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>The Zero Trust dashboard and navigation is receiving significant and exciting updates. The dashboard is being restructured to better support common tasks and workflows, and various pages have been moved and consolidated.</p>
<p>There is a new guided experience on login detailing the changes, and you can use the Zero Trust dashboard search to find product pages by both their new and old names, as well as your created resources. To replay the guided experience, you can find it in Overview &gt; Get Started.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-dash-changes.png" alt="Cloudflare One Dash Changes" /></p>
<p>Notable changes</p>
<ul>
<li>Product names have been removed from many top-level navigation items to help bring clarity to what they help you accomplish. For example, you can find Gateway policies under ‘Traffic policies' and CASB findings under ‘Cloud &amp; SaaS findings.'</li>
<li>You can view all analytics, logs, and real-time monitoring tools from ‘Insights.'</li>
<li>‘Networks' better maps the ways that your corporate network interacts with Cloudflare. Some pages like Tunnels, are now a tab rather than a full page as part of these changes. You can find them at Networks &gt; Connectors.</li>
<li>Settings are now located closer to the tools and resources they impact. For example, this means you'll find your WARP configurations at Team &amp; Resources &gt; Devices.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/new-cf1-navigation.png" alt="New Cloudflare One Navigation" /></p>
<p>No changes to our API endpoint structure or to any backend services have been made as part of this effort.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-17">Nov 17, 2025</time><div>
<h2 id="post-2025-11-17-waf-release"><a href="/changelog/post/2025-11-17-waf-release/">WAF Release - 2025-11-17</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in DELMIA Apriso, linked to CVE-2025-6205.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to gain privileged access to the application. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>DELMIA Apriso (CVE-2025-6205): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ec1e2aa190e64e7cb468e16dd256f4bc">d256f4bc</code>
</td>
<td>N/A</td>
<td>DELMIA Apriso - Auth Bypass - CVE:CVE-2025-6205</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-14">Nov 14, 2025</time><div>
<h2 id="post-2025-11-14-SSH-CA-enhancements"><a href="/changelog/post/2025-11-14-SSH-CA-enhancements/">Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>SSH with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Cloudflare Access for Infrastructure</a> allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.</p>
<p>Previously, users had to generate this certificate by using the <a href="https://developers.cloudflare.com/api/">Cloudflare API</a> directly. With this update, you can now create and manage this certificate in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a> from the <strong>Access controls</strong> &gt; <strong>Service credentials</strong> page.</p>
<p><img src="/assets/upstream/images/changelog/access/SSH-CA-generation.png" alt="Navigate to Access controls and then Service credentials to see where you can generate an SSH CA" /></p>
<p>For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca">Generate a Cloudflare SSH CA</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-14">Nov 14, 2025</time><div>
<h2 id="post-2025-11-14-casb-digest"><a href="/changelog/post/2025-11-14-casb-digest/">New SaaS Security weekly digests with API CASB</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>You can now stay on top of your SaaS security posture with the new <strong>CASB Weekly Digest</strong> notification. This opt-in email digest is delivered to your inbox every Monday morning and provides a high-level summary of your organization's Cloudflare API CASB findings from the previous week.</p>
<p>This allows security teams and IT administrators to get proactive, at-a-glance visibility into new risks and integration health without having to log in to the dashboard.</p>
<p>To opt in, navigate to <strong>Manage Account</strong> &gt; <strong>Notifications</strong> in the Cloudflare dashboard to configure the <strong>CASB Weekly Digest</strong> alert type.</p>
<h4 id="2025-11-14-casb-digest-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>At-a-glance summary</strong> — Review new high/critical findings, most frequent finding types, and new content exposures from the past 7 days.</li>
<li><strong>Integration health</strong> — Instantly see the status of all your connected SaaS integrations (Healthy, Unhealthy, or Paused) to spot API connection issues.</li>
<li><strong>Proactive alerting</strong> — The digest is sent automatically to all subscribed users every Monday morning.</li>
<li><strong>Easy to configure</strong> — Users can opt in by enabling the notification in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Notifications</strong>.</li>
</ul>
<h4 id="2025-11-14-casb-digest-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/notifications/">notification preferences</a> in Cloudflare.</li>
</ul>
<p>The CASB Weekly Digest notification is available to all Cloudflare users today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-13">Nov 13, 2025</time><div>
<h2 id="post-2025-11-13-fixed-custom-date"><a href="/changelog/post/2025-11-13-fixed-custom-date/">Fixed custom SQL date picker inconsistencies</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.</p>
<p>This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/29/">Previous</a><span>Page 30 of 50</span><a class="pagination-next" rel="next" href="/changelog/31/">Next</a></nav>
</div>
