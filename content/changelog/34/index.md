---
cp9:
  canonical: https://developers.cloudflare.com/changelog/34/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 34 | Cloudflare Docs
  head_html: <title>Changelog - page 34 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/34/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 34"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/34/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/34/#page","headline":"Changelog - page 34 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/34/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/34/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-10-03">Oct 3, 2025</time><div>
<h2 id="post-2025-10-03-waf-release"><a href="/changelog/post/2025-10-03-waf-release/">WAF Release - 2025-10-03</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>Managed Ruleset Updated</strong></p>
<p>This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.</p>
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
        <code class="nb-rule-id" title="0d02c2fb14eb4cec9c2e2b58d61fac74">d61fac74</code>
</td>
<td>100902</td>
<td>Generic Rules - Command Execution - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c3079865ce9a41368657026b514aeeb8">514aeeb8</code>
</td>
<td>100908</td>
<td>Generic Rules - Command Execution - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="107ae2922b654bb28df7ca978d46a6f4">8d46a6f4</code>
</td>
<td>100910</td>
<td>Generic Rules - Command Execution - 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68bdb75ae6d24e139a83e5731bd0a329">1bd0a329</code>
</td>
<td>100915</td>
<td>Generic Rules - Command Execution - 5</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ea04bb580f7d400386c7dc1d5e51450a">5e51450a</code>
</td>
<td>100899</td>
<td>Generic Rules - Content-Type Abuse</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="233364f656ff42b8acc41dcd7996012f">7996012f</code>
</td>
<td>100914</td>
<td>Generic Rules - Content-Type Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1aa695281c954513be3d003b93209312">93209312</code>
</td>
<td>100911</td>
<td>Generic Rules - Cookie Header Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d9f9e4f5bf11489da52dccb40f373b3f">0f373b3f</code>
</td>
<td>100905</td>
<td>Generic Rules - NoSQL Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5a1897b714e044a887c0f3f078a0ed04">78a0ed04</code>
</td>
<td>100913</td>
<td>Generic Rules - NoSQL Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4d6fd28df4f1494e95e70d2c5d649624">5d649624</code>
</td>
<td>100907</td>
<td>Generic Rules - Parameter Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="61181e3af5304f7396c7d01cfd1c674e">fd1c674e</code>
</td>
<td>100906</td>
<td>Generic Rules - PHP Object Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed5190bfbe1b45a6a645126334c88168">34c88168</code>
</td>
<td>100904</td>
<td>Generic Rules - Prototype Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3ec33bc5ac77495a9f55020e3ab43f7e">3ab43f7e</code>
</td>
<td>100897</td>
<td>Generic Rules - Prototype Pollution 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c6d752c4909e4b7e8eff6c780d94ee22">0d94ee22</code>
</td>
<td>100903</td>
<td>Generic Rules - Reverse Shell</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="caf37e7800bb4635bcc2eefcd5add8e3">d5add8e3</code>
</td>
<td>100909</td>
<td>Generic Rules - Reverse Shell - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="475d090baead467c88dfabbb565c78b0">565c78b0</code>
</td>
<td>100898</td>
<td>Generic Rules - SSJI NoSQL</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f4c7f98934264c9c937eec1212b837a0">12b837a0</code>
</td>
<td>100896</td>
<td>Generic Rules - SSRF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="efd01b814d144e90b36522b311c4fb00">11c4fb00</code>
</td>
<td>100895</td>
<td>Generic Rules - Template Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="00a9a0d663da4add95b863abd3ed0123">d3ed0123</code>
</td>
<td>100895A</td>
<td>Generic Rules - Template Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e58c0fffee4f4374bd37f2577501a1d9">7501a1d9</code>
</td>
<td>100912</td>
<td>Generic Rules - XXE</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab09ba8d00eb4cdbb7a6a65ddc55cdb6">dc55cdb6</code>
</td>
<td>100900</td>
<td>Relative Paths - Anomaly Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-03">Oct 3, 2025</time><div>
<h2 id="post-2025-10-03-one-click-access-for-workers"><a href="/changelog/post/2025-10-03-one-click-access-for-workers/">One-click Cloudflare Access for Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now enable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> for your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> in a single click.</p>
<p><img src="/assets/upstream/images/workers/changelog/workers-access.png" alt="Screenshot of the Enable/Disable Cloudflare Access button on the workers.dev route settings page" /></p>
<p>Access allows you to limit access to your Workers to specific users or groups. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your <a href="/cloudflare-one/access-controls/policies/">Access policy</a>.</p>
<p>To enable Cloudflare Access:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, to configure the Access application, click <strong>Manage Cloudflare Access</strong>. There, you can change the email addresses you want to authorize. View <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a> to learn about configuring alternate rules.</li>
</ol>
<p>To fully secure your application, it is important that you validate the JWT that Cloudflare Access adds to the <code>Cf-Access-Jwt-Assertion</code> header on the incoming request.</p>
<p>The following code will validate the JWT using the <a href="https://www.npmjs.com/package/jose">jose NPM package</a>:</p>
<pre tabindex="0"><code class="language-javascript">import { jwtVerify, createRemoteJWKSet } from &quot;jose&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Verify the POLICY_AUD environment variable is set&#10;		if (!env.POLICY_AUD) {&#10;			return new Response(&quot;Missing required audience&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		// Get the JWT from the request headers&#10;		const token = request.headers.get(&quot;cf-access-jwt-assertion&quot;);&#10;&#10;		// Check if token exists&#10;		if (!token) {&#10;			return new Response(&quot;Missing required CF Access JWT&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		try {&#10;			// Create JWKS from your team domain&#10;			const JWKS = createRemoteJWKSet(&#10;				new URL(`${env.TEAM_DOMAIN}/cdn-cgi/access/certs`),&#10;			);&#10;&#10;			// Verify the JWT&#10;			const { payload } = await jwtVerify(token, JWKS, {&#10;				issuer: env.TEAM_DOMAIN,&#10;				audience: env.POLICY_AUD,&#10;			});&#10;&#10;			// Token is valid, proceed with your application logic&#10;			return new Response(`Hello ${payload.email || &quot;authenticated user&quot;}!`, {&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		} catch (error) {&#10;			// Token verification failed&#10;			return new Response(`Invalid token: ${error.message}`, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-10-03-one-click-access-for-workers-required-environment-variables">Required environment variables</h4>
<p>Add these <a href="/workers/configuration/environment-variables/">environment variables</a> to your Worker:</p>
<ul>
<li><code>POLICY_AUD</code>: Your application's AUD tag</li>
<li><code>TEAM_DOMAIN</code>: <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
</ul>
<p>Both of these appear in the modal that appears when you enable Cloudflare Access.</p>
<p>You can set these variables by adding them to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, or via the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>your-worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-02">Oct 2, 2025</time><div>
<h2 id="post-2025-10-01-fine-grained-permissioning-beta"><a href="/changelog/post/2025-10-01-fine-grained-permissioning-beta/">Fine-grained Permissioning for Access for Apps, IdPs, &amp; Targets now in Public Beta</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>access</span></div><div class="changelog-body"><p>Fine-grained permissions for <strong>Access Applications, Identity Providers (IdPs), and Targets</strong> is now available in Public Beta. This expands our RBAC model beyond account &amp; zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2025-10-01-fine-grained-permissioning-beta-what-s-new">What's New</h4>
- **[Access Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-01-fine-grained-permissioning-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17728.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Get started with Cloudflare Permissioning</a></li>
<li><a href="/fundamentals/manage-members/manage">Manage Member Permissioning via the UI &amp; API</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-02">Oct 2, 2025</time><div>
<h2 id="post-2025-09-26-analytics-engine-sql-enhancements"><a href="/changelog/post/2025-09-26-analytics-engine-sql-enhancements/">Workers Analytics Engine adds supports for new SQL functions</a></h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>argMin()</code> - Returns the value associated with the minimum in a group</li>
<li><code>argMax()</code> - Returns the value associated with the maximum in a group</li>
<li><code>topK()</code> - Returns an array of the most frequent values in a group</li>
<li><code>topKWeighted()</code> - Returns an array of the most frequent values in a group using weights</li>
<li><code>first_value()</code> - Returns the first value in an ordered set of values within a partition</li>
<li><code>last_value()</code> - Returns the last value in an ordered set of values within a partition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><strong>New bit functions:</strong></a></p>
<ul>
<li><code>bitAnd()</code> - Returns the bitwise AND of two expressions</li>
<li><code>bitCount()</code> - Returns the number of bits set to one in the binary representation of a number</li>
<li><code>bitHammingDistance()</code> - Returns the number of bits that differ between two numbers</li>
<li><code>bitNot()</code> - Returns a number with all bits flipped</li>
<li><code>bitOr()</code> - Returns the inclusive bitwise OR of two expressions</li>
<li><code>bitRotateLeft()</code> - Rotates all bits in a number left by specified positions</li>
<li><code>bitRotateRight()</code> - Rotates all bits in a number right by specified positions</li>
<li><code>bitShiftLeft()</code> - Shifts all bits in a number left by specified positions</li>
<li><code>bitShiftRight()</code> - Shifts all bits in a number right by specified positions</li>
<li><code>bitTest()</code> - Returns the value of a specific bit in a number</li>
<li><code>bitXor()</code> - Returns the bitwise exclusive-or of two expressions</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><strong>New mathematical functions:</strong></a></p>
<ul>
<li><code>abs()</code> - Returns the absolute value of a number</li>
<li><code>log()</code> - Computes the natural logarithm of a number</li>
<li><code>round()</code> - Rounds a number to a specified number of decimal places</li>
<li><code>ceil()</code> - Rounds a number up to the nearest integer</li>
<li><code>floor()</code> - Rounds a number down to the nearest integer</li>
<li><code>pow()</code> - Returns a number raised to the power of another number</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/"><strong>New string functions:</strong></a></p>
<ul>
<li><code>lowerUTF8()</code> - Converts a string to lowercase using UTF-8 encoding</li>
<li><code>upperUTF8()</code> - Converts a string to uppercase using UTF-8 encoding</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><strong>New encoding functions:</strong></a></p>
<ul>
<li><code>hex()</code> - Converts a number to its hexadecimal representation</li>
<li><code>bin()</code> - Converts a string to its binary representation</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/"><strong>New type conversion functions:</strong></a></p>
<ul>
<li><code>toUInt8()</code> - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer</li>
</ul>
<h4 id="2025-09-26-analytics-engine-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-02">Oct 2, 2025</time><div>
<h2 id="post-2025-10-02-deepgram-flux"><a href="/changelog/post/2025-10-02-deepgram-flux/">New Deepgram Flux model available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Deepgram's newest Flux model <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out <a href="https://deepgram.com/flux">Deepgram's blog</a> for more details on the release.</p>
<p>The Flux model can be used in conjunction with Deepgram's speech-to-text model <a href="/workers-ai/models/nova-3/"><code>@cf/deepgram/nova-3</code></a> and text-to-speech model <a href="/workers-ai/models/aura-1/"><code>@cf/deepgram/aura-1</code></a> to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.</p>
<h4 id="2025-10-02-deepgram-flux-promotional-pricing">Promotional Pricing</h4>
For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](/workers-ai/models/flux/) for pricing details in the future.
<h4 id="2025-10-02-deepgram-flux-example-usage">Example Usage</h4>
<p>The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.</p>
<ol>
<li>Create a worker that establishes a websocket connection with <code>@cf/deepgram/flux</code></li>
</ol>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const resp = await env.AI.run(&quot;@cf/deepgram/flux&quot;, {&#10;      encoding: &quot;linear16&quot;,&#10;      sample_rate: &quot;16000&quot;&#10;    }, {&#10;      websocket: true&#10;    });&#10;    return resp;&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<ol start="2">
<li>Deploy your worker</li>
</ol>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<ol start="3">
<li>Write a client script to connect to your worker and start sending random audio bytes to it</li>
</ol>
<pre tabindex="0"><code class="language-js">const ws = new WebSocket(&#x27;wss://&lt;your-worker-url.com&gt;&#x27;);&#10;&#10;ws.onopen = () =&gt; {&#10;  console.log(&#x27;Connected to WebSocket&#x27;);&#10;&#10;  // Generate and send random audio bytes&#10;  // You can replace this part with a function&#10;  // that reads from your mic or other audio source&#10;  const audioData = generateRandomAudio();&#10;  ws.send(audioData);&#10;  console.log(&#x27;Audio data sent&#x27;);&#10;};&#10;&#10;ws.onmessage = (event) =&gt; {&#10;  // Transcription will be received here&#10;  // Add your custom logic to parse the data&#10;  console.log(&#x27;Received:&#x27;, event.data);&#10;};&#10;&#10;ws.onerror = (error) =&gt; {&#10;  console.error(&#x27;WebSocket error:&#x27;, error);&#10;};&#10;&#10;ws.onclose = () =&gt; {&#10;  console.log(&#x27;WebSocket closed&#x27;);&#10;};&#10;&#10;// Generate random audio data (1 second of noise at 44.1kHz, mono)&#10;function generateRandomAudio() {&#10;  const sampleRate = 44100;&#10;  const duration = 1;&#10;  const numSamples = sampleRate * duration;&#10;  const buffer = new ArrayBuffer(numSamples * 2);&#10;  const view = new Int16Array(buffer);&#10;&#10;  for (let i = 0; i &lt; numSamples; i++) {&#10;    view[i] = Math.floor(Math.random() * 65536 - 32768);&#10;  }&#10;&#10;  return buffer;&#10;}&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-10-01-confidence-intervals"><a href="/changelog/post/2025-10-01-confidence-intervals/">New Confidence Intervals in GraphQL Analytics API</a></h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-10-01-new-container-instance-types"><a href="/changelog/post/2025-10-01-new-container-instance-types/">Larger Container instance types</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>New instance types provide up to 4 vCPU, 12 GiB of memory, and 20 GB of disk per container instance.</p>
<table>
<thead>
<tr>
<th>Instance Type</th>
<th>vCPU</th>
<th>Memory</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td>lite</td>
<td>1/16</td>
<td>256 MiB</td>
<td>2 GB</td>
</tr>
<tr>
<td>basic</td>
<td>1/4</td>
<td>1 GiB</td>
<td>4 GB</td>
</tr>
<tr>
<td>standard-1</td>
<td>1/2</td>
<td>4 GiB</td>
<td>8 GB</td>
</tr>
<tr>
<td>standard-2</td>
<td>1</td>
<td>6 GiB</td>
<td>12 GB</td>
</tr>
<tr>
<td>standard-3</td>
<td>2</td>
<td>8 GiB</td>
<td>16 GB</td>
</tr>
<tr>
<td>standard-4</td>
<td>4</td>
<td>12 GiB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>The <code>dev</code> and <code>standard</code> instance types are preserved for backward compatibility and are aliases for <code>lite</code> and <code>standard-1</code>, respectively. The <code>standard-1</code> instance type now provides up to 8 GB of disk instead of only 4 GB.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-10-01-new-file-type-support"><a href="/changelog/post/2025-10-01-new-file-type-support/">Expanded File Type Controls for Executables and Disk Images</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.</p>
<p>We have expanded Gateway's file type controls to include:</p>
<ul>
<li>Apple Disk Image (dmg)</li>
<li>Microsoft Software Installer (msix, appx)</li>
<li>Apple Software Package (pkg)</li>
</ul>
<p>You can find these new options within the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types"><em>Upload File Types</em> and <em>Download File Types</em> selectors</a> when creating or editing an HTTP policy. The file types are categorized as follows:</p>
<ul>
<li><strong>System</strong>: <em>Apple Disk Image (dmg)</em></li>
<li><strong>Executable</strong>: <em>Microsoft Software Installer (msix)</em>, <em>Microsoft Software Installer (appx)</em>, <em>Apple Software Package (pkg)</em></li>
</ul>
<p>To ensure these file types are blocked effectively, please note the following behaviors:</p>
<ul>
<li>DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.</li>
<li>MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type <em>Unscannable</em>. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.</li>
</ul>
<p>To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#supported-file-types">supported file types</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-10-01-md-returned"><a href="/changelog/post/2025-10-01-md-returned/">Return markdown</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.</p>
<pre tabindex="0"><code class="language-sh">curl https://developers.cloudflare.com/workers/ -H &#x27;Accept: text/markdown&#x27;  -v&#10;</code></pre>
<p>If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example <a href="https://github.com/cloudflare/cloudflare-docs/pull/25493">here</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-09-30-warp-linux-ga"><a href="/changelog/post/2025-09-30-warp-linux-ga/">WARP client for Linux (version 2025.7.176.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-09-30-warp-macos-ga"><a href="/changelog/post/2025-09-30-warp-macos-ga/">WARP client for macOS (version 2025.7.176.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed a bug preventing the <code>warp-diag captive-portal</code> command from running successfully due to the client not parsing SSID on macOS.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
<li>The WARP client now supports macOS Tahoe (version 26.0).</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-01">Oct 1, 2025</time><div>
<h2 id="post-2025-09-30-warp-windows-ga"><a href="/changelog/post/2025-09-30-warp-windows-ga/">WARP client for Windows (version 2025.7.176.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvement to maintain TCP connections to reduce interruptions in long-lived connections such as RDP or SSH.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-30">Sep 30, 2025</time><div>
<h2 id="post-2025-09-25-new-granular-controls-for-saas-applications"><a href="/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/">Application granular controls for operations in SaaS applications</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Gateway users can now apply granular controls to their file sharing and AI chat applications through <a href="/cloudflare-one/traffic-policies/http-policies">HTTP policies</a>.</p>
<p>The new feature offers two methods of controlling SaaS applications:</p>
<ul>
<li><strong>Application Controls</strong> are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include <em>Upload</em>, <em>Download</em>, <em>Prompt</em>, <em>Voice</em>, and <em>Share</em> depending on the application.</li>
<li><strong>Operations</strong> are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.</li>
</ul>
<p>Get started using <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls">Application Granular Controls</a> and refer to the list of <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications">supported applications</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-29">Sep 29, 2025</time><div>
<h2 id="post-2025-09-29-radar-regional-data"><a href="/changelog/post/2025-09-29-radar-regional-data/">Regional Data in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/geolocations/methods/get/"><code>Get Geolocation</code></a> - Retrieves geolocation by <code>geoId</code>.</li>
<li><a href="/api/resources/radar/subresources/geolocations/methods/list/"><code>List Geolocations</code></a> - Lists geolocations.</li>
<li><a href="/api/resources/radar/subresources/netflows/methods/summary_v2/"><code>NetFlows Summary By Dimension</code></a> - Retrieves NetFlows summary by dimension.</li>
</ul>
<p>All <code>summary</code> and <code>timeseries_groups</code> endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> now include an <code>adm1</code> dimension for grouping data by first level administrative division (for example, state, province, etc.)</p>
<p>A new filter <code>geoId</code> was also added to all endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a>, allowing filtering by a specific administrative division.</p>
<p>Check out the new Regional traffic insights on a country specific traffic page <a href="https://radar.cloudflare.com/traffic/pt">new Radar page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-29">Sep 29, 2025</time><div>
<h2 id="post-2025-09-29-waf-release"><a href="/changelog/post/2025-09-29-waf-release/">WAF Release - 2025-09-29</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights four important vendor- and component-specific issues: an authentication bypass in SimpleHelp (CVE-2024-57727), an information-disclosure flaw in Flowise Cloud (CVE-2025-58434), an SSRF in the WordPress plugin Ditty (CVE-2025-8085), and a directory-traversal bug in Vite (CVE-2025-30208). These are paired with improvements to our generic detection coverage (SQLi, SSRF) to raise the baseline and reduce noisy gaps.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): Authentication bypass in SimpleHelp that can allow unauthorized access to management interfaces or sessions.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure vulnerability in Flowise Cloud that may expose sensitive configuration or user data to unauthenticated or low-privileged actors.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF in the Ditty WordPress plugin enabling server-side requests that could reach internal services or cloud metadata endpoints.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability in Vite allowing access to filesystem paths outside the intended web root.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities allow attackers to gain access, escalate privileges, or execute actions that were previously unavailable:</p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): An authentication bypass that can let unauthenticated attackers access management interfaces or hijack sessions — enabling lateral movement, credential theft, or privilege escalation within affected environments.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure flaw that can expose sensitive configuration, tokens, or user data; leaked secrets may be chained into account takeover or privileged access to backend services.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF that enables server-side requests to internal services or cloud metadata endpoints, potentially allowing attackers to retrieve credentials or reach otherwise inaccessible infrastructure, leading to privilege escalation or cloud resource compromise.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability that can expose filesystem contents outside the web root (configuration files, keys, source code), which attackers can use to escalate privileges or further compromise systems.</p>
</li>
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
        <code class="nb-rule-id" title="6fe90532af50427484a5275c8c2e30fb">8c2e30fb</code>
</td>
<td>100717</td>
<td>SimpleHelp - Auth Bypass - CVE:CVE-2024-57727</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged to 100717 in legacy WAF and <code class="nb-rule-id" title="498fcd81a62a4b5ca943e2de958094d3">958094d3</code> in new WAF</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="013ef5de3f074fd5a43cdd70d58b886b">d58b886b</code>
</td>
<td>100775</td>
<td>Flowise Cloud - Information Disclosure - CVE:CVE-2025-58434</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68fc5c086ccb4b40a35a63b19bce1ff4">9bce1ff4</code>
</td>
<td>100881</td>
<td>WordPress:Plugin:Ditty - SSRF - CVE:CVE-2025-8085</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9e1a56e6b3bc49b187bf6e35ddc329dd">ddc329dd</code>
</td>
<td>100887</td>
<td>Vite - Directory Traversal - CVE:CVE-2025-30208</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-28">Sep 28, 2025</time><div>
<h2 id="post-2025-09-28-emergency-waf-release"><a href="/changelog/post/2025-09-28-emergency-waf-release/">WAF Release - 2025-09-28 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.</p>
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
        <code class="nb-rule-id" title="a1bef4ada0b146d2862cad439ee0ab84">9ee0ab84</code>
</td>
<td>100788</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="51de6ce6596a40eb8200452ad30f768e">d30f768e</code>
</td>
<td>100788A</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-26">Sep 26, 2025</time><div>
<h2 id="post-2025-09-26-waf-release"><a href="/changelog/post/2025-09-26-waf-release/">WAF Release - 2025-09-26</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>Managed Ruleset Updated</strong></p>
<p>This update introduces 11 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.</p>
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
        <code class="nb-rule-id" title="3ffd242b4ba242ca965022d3a67d8561">a67d8561</code>
</td>
<td>100859A</td>
<td>SQLi - UNION - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="91d9cf56355b4ab88481b2fd4de80468">4de80468</code>
</td>
<td>100889</td>
<td>Command Injection - Generic 9</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c15ca8e8290f485287037665f2be3ddf">f2be3ddf</code>
</td>
<td>100890</td>
<td>Information Disclosure - Common Files - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="56669615f2984c2cac8c608980a252a8">80a252a8</code>
</td>
<td>100891</td>
<td>Anomaly:URL - Relative Paths</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c41789fb6370431d809567d17e7d3865">7e7d3865</code>
</td>
<td>100894</td>
<td>XSS - Inline Function</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b995d0b930604fa6b8d9b2a13792565c">3792565c</code>
</td>
<td>100895</td>
<td>XSS - DOM</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab8277e3f432400bbd9403dd42978e38">42978e38</code>
</td>
<td>100896</td>
<td>SQLi - MSSQL Length Enumeration</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3ec33bc5ac77495a9f55020e3ab43f7e">3ab43f7e</code>
</td>
<td>100897</td>
<td>Generic Rules - Code Injection - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4375dc90c7af4c55908f6b95c1686741">c1686741</code>
</td>
<td>100898</td>
<td>SQLi - Evasion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="945c5aa9f45141dd872d7ec920999be0">20999be0</code>
</td>
<td>100899</td>
<td>SQLi - Probing 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2c20b5e8684043f48620ff77b4026c88">b4026c88</code>
</td>
<td>100900</td>
<td>SQLi - Probing</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-26">Sep 26, 2025</time><div>
<h2 id="post-2025-09-26-ctx-exports"><a href="/changelog/post/2025-09-26-ctx-exports/">Automatic loopback bindings via ctx.exports</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a> contains automatically-configured bindings corresponding to your Worker's top-level exports. For each top-level export extending <code>WorkerEntrypoint</code>, <code>ctx.exports</code> will contain a <a href="/workers/runtime-apis/bindings/service-bindings">Service Binding</a> by the same name, and for each export extending <code>DurableObject</code> (and for which storage has been configured via a <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>), <code>ctx.exports</code> will contain a <a href="/durable-objects/api/namespace/">Durable Object namespace binding</a>. This means you no longer have to configure these bindings explicitly in <code>wrangler.jsonc</code>/<code>wrangler.toml</code>.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Greeter extends WorkerEntrypoint {&#10;  greet(name) {&#10;    return `Hello, ${name}!`;&#10;  }&#10;}&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    let greeting = await ctx.exports.Greeter.greet(&quot;World&quot;)&#10;    return new Response(greeting);&#10;  }&#10;}&#10;</code></pre>
<p>At present, you must use <a href="/workers/configuration/compatibility-flags#enable-ctxexports">the <code>enable_ctx_exports</code> compatibility flag</a> to enable this API, though it will be on by default in the future.</p>
<p><a href="/workers/runtime-apis/context/#exports">See the API reference for more information.</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-pipelines-sql"><a href="/changelog/post/2025-09-25-pipelines-sql/">Pipelines now supports SQL transformations and Apache Iceberg</a></h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p>Today, we're launching the new <a href="/pipelines/">Cloudflare Pipelines</a>: a streaming data platform that ingests events, transforms them with <a href="/pipelines/sql-reference/select-statements/">SQL</a>, and writes to <a href="/r2/">R2</a> as <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables or Parquet files.</p>
<p>Pipelines can receive events via <a href="/pipelines/streams/writing-to-streams/#send-via-http">HTTP endpoints</a> or <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Worker bindings</a>, transform them with SQL, and deliver to R2 with exactly-once guarantees. This makes it easy to build analytics-ready warehouses for server logs, mobile application events, IoT telemetry, or clickstream data without managing streaming infrastructure.</p>
<p>For example, here's a pipeline that ingests clickstream events and filters out bot traffic while extracting domain information:</p>
<pre tabindex="0"><code class="language-sql">INSERT into events_table&#10;SELECT&#10;  user_id,&#10;  lower(event) AS event_type,&#10;  to_timestamp_micros(ts_us) AS event_time,&#10;  regexp_match(url, &#x27;^https?://([^/]+)&#x27;)[1]  AS domain,&#10;  url,&#10;  referrer,&#10;  user_agent&#10;FROM events_json&#10;WHERE event = &#x27;page_view&#x27;&#10;  AND NOT regexp_like(user_agent, &#x27;(?i)bot|spider&#x27;);&#10;</code></pre>
<p>Get started by creating a pipeline in the dashboard or running a single command in <a href="/workers/wrangler/">Wrangler</a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<p>Check out our <a href="/pipelines/getting-started/">getting started guide</a> to learn how to create a pipeline that delivers events to an <a href="/r2-data-catalog/">Iceberg table</a> you can query with R2 SQL. Read more about today's announcement in our <a href="https://blog.cloudflare.com/cloudflare-data-platform">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-announcing-r2-sql-open-beta"><a href="/changelog/post/2025-09-25-announcing-r2-sql-open-beta/">Announcing R2 SQL</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>Today, we're launching the <strong>open beta</strong> for <a href="/r2-sql/">R2 SQL</a>: A serverless, distributed query engine that can efficiently analyze petabytes of data in <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from <a href="/pipelines/">Pipelines</a>, or clickstream and user behavior data.</p>
<p>If you already have a table in R2 Data Catalog, running queries is as simple as:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query YOUR_WAREHOUSE &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    value&#10;FROM events.user_events&#10;WHERE event_type = &#x27;CHANGELOG&#x27; or event_type = &#x27;BLOG&#x27;&#10;  AND __ingest_ts &gt; &#x27;2025-09-24T00:00:00Z&#x27;&#10;ORDER BY __ingest_ts DESC&#10;LIMIT 100&quot;&#10;</code></pre>
<p>To get started with R2 SQL, check out our <a href="/r2-sql/get-started/">getting started guide</a> or learn more about supported features in the <a href="/r2-sql/sql-reference/">SQL reference</a>. For a technical deep dive into how we built R2 SQL, read our <a href="https://blog.cloudflare.com/r2-sql-deep-dive/">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-br-playwright-ga-stagehand-limits"><a href="/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/">Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We’re shipping three updates to Browser Rendering:</p>
<ul>
<li>Playwright support is now Generally Available and synced with <a href="https://playwright.dev/docs/release-notes#version-155">Playwright v1.55</a>, giving you a stable foundation for critical automation and AI-agent workflows.</li>
<li>We’re also adding <a href="/browser-run/stagehand/">Stagehand support (Beta)</a> so you can combine code with natural language instructions to build more resilient automations.</li>
<li>Finally, we’ve tripled <a href="/browser-run/limits/#workers-paid">limits</a> for paid plans across both the <a href="/browser-run/quick-actions/">REST API</a> and <a href="/browser-run/#integration-methods">Browser Sessions</a> to help you scale.</li>
</ul>
<p>To get started with Stagehand, refer to the <a href="/browser-run/stagehand/">Stagehand</a> example that uses Stagehand and <a href="/workers-ai/">Workers AI</a> to search for a movie on this <a href="https://demo.playwright.dev/movies">example movie directory</a>, extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.</p>
<pre tabindex="0"><code class="language-ts">const stagehand = new Stagehand({&#10;	env: &quot;LOCAL&quot;,&#10;	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },&#10;	llmClient: new WorkersAIClient(env.AI),&#10;	verbose: 1,&#10;});&#10;&#10;await stagehand.init();&#10;const page = stagehand.page;&#10;&#10;await page.goto(&quot;https://demo.playwright.dev/movies&quot;);&#10;&#10;// if search is a multi-step action, stagehand will return an array of actions it needs to act on&#10;const actions = await page.observe(&#x27;Search for &quot;Furiosa&quot;&#x27;);&#10;for (const action of actions) await page.act(action);&#10;&#10;await page.act(&quot;Click the search result&quot;);&#10;&#10;// normal playwright functions work as expected&#10;await page.waitForSelector(&quot;.info-wrapper .cast&quot;);&#10;&#10;let movieInfo = await page.extract({&#10;	instruction: &quot;Extract movie information&quot;,&#10;	schema: z.object({&#10;		title: z.string(),&#10;		year: z.number(),&#10;		rating: z.number(),&#10;		genres: z.array(z.string()),&#10;		duration: z.number().describe(&quot;Duration in minutes&quot;),&#10;	}),&#10;});&#10;&#10;await stagehand.close();&#10;</code></pre>
<p><img src="/images/browser-run/speedystagehand.gif" alt="Stagehand video" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-ai-search-more-models"><a href="/changelog/post/2025-09-25-ai-search-more-models/">AI Search (formerly AutoRAG) now with More Models To Choose From</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.</p>
<p>With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.</p>
<p>To use AI Search with other <a href="/ai-search/configuration/models/">model providers</a>:</p>
<ol>
<li><strong>Add provider keys to AI Gateway</strong>
<ol>
<li>Go to AI &gt; AI Gateway in the dashboard.</li>
<li>Select or create an AI gateway.</li>
<li>In Provider Keys, choose your provider, click Add, and enter the key.</li>
</ol>
</li>
<li><strong>Connect a gateway to AI Search</strong>: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.</li>
<li><strong>Select models</strong>: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.</li>
</ol>
<p>Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a <code>/ai-search</code> request:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    &#10;    // Query your AI Search instance with a natural language question to an OpenAI model&#10;    const result = await env.AI.autorag(&quot;my-ai-search&quot;).aiSearch({&#10;      query: &quot;What&#x27;s new for Cloudflare Birthday Week?&quot;,&#10;      model: &quot;openai/gpt-5&quot;&#10;    });&#10;&#10;    // Return only the generated answer as plain text&#10;    return new Response(result.response, {&#10;      headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the <a href="/changelog/product/ai-search/">AI Search Changelog</a> and <a href="https://discord.cloudflare.com/">Discord</a> for more updates!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-24-higher-container-resource-limits"><a href="/changelog/post/2025-09-24-higher-container-resource-limits/">Run more Containers with higher resource limits</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now run more Containers concurrently with higher limits on CPU, memory, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>New Limit</th>
<th>Previous Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>40GiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>20</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>100GB</td>
</tr>
</tbody>
</table>
<p>You can now run 1000 instances of the <code>dev</code> instance type, 400 instances of <code>basic</code>, or 100 instances of <code>standard</code> concurrently.</p>
<p>This opens up new possibilities for running larger-scale workloads on Containers.</p>
<p>See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,
and the <a href="/containers/platform/limits/">limits documentation</a> for more details on the available instance types and limits.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-body-phase-selector"><a href="/changelog/post/2025-09-25-body-phase-selector/">Refine DLP Scans with New Body Phase Selector</a></h2>
<div class="changelog-badges"><span>gateway</span><span>dlp</span></div><div class="changelog-body"><p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-sign-in-with-github"><a href="/changelog/post/2025-09-25-sign-in-with-github/">Sign in with GitHub</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare has launched sign in with GitHub as a log in option. This feature is available to all users with a verified email address who are not using SSO. To use it, simply click on the <code>Sign in with GitHub</code> button on the dashboard login page. You will be logged in with your primary GitHub email address.</p>
<h4 id="2025-09-25-sign-in-with-github-for-more-information">For more information</h4>
- [Log in to Cloudflare](/fundamentals/user-profiles/login/)
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/33/">Previous</a><span>Page 34 of 50</span><a class="pagination-next" rel="next" href="/changelog/35/">Next</a></nav>
</div>
