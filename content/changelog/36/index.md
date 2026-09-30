---
cp9:
  canonical: https://developers.cloudflare.com/changelog/36/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 36 | Cloudflare Docs
  head_html: <title>Changelog - page 36 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/36/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 36"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/36/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/36/#page","headline":"Changelog - page 36 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/36/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/36/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-09-09">Sep 9, 2025</time><div>
<h2 id="post-2025-09-09-interactive-wrangler-assets"><a href="/changelog/post/2025-09-09-interactive-wrangler-assets/">Deploy static sites to Workers without a configuration file</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Deploying static site to Workers is now easier. When you run <code>wrangler deploy [directory]</code> or <code>wrangler deploy --assets [directory]</code> without an existing <a href="/workers/wrangler/configuration/">configuration file</a>, <a href="/workers/wrangler/">Wrangler CLI</a> now guides you through the deployment process with interactive prompts.</p>
<h4 id="2025-09-09-interactive-wrangler-assets-before-and-after">Before and after</h4>
<p><strong>Before:</strong> Required remembering multiple flags and parameters</p>
<pre tabindex="0"><code class="language-bash">wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project&#10;</code></pre>
<p><strong>After:</strong> Simple directory deployment with guided setup</p>
<pre tabindex="0"><code class="language-bash">wrangler deploy dist&#10;&#35; Interactive prompts handle the rest as shown in the example flow below&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-what-s-new">What's new</h4>
<p><strong>Interactive prompts for missing configuration:</strong></p>
<ul>
<li>Wrangler detects when you're trying to deploy a directory of static assets</li>
<li>Prompts you to confirm the deployment type</li>
<li>Asks for a project name (with smart defaults)</li>
<li>Automatically sets the compatibility date to today</li>
</ul>
<p><strong>Automatic configuration generation:</strong></p>
<ul>
<li>Creates a <code>wrangler.jsonc</code> file with your deployment settings</li>
<li>Stores your choices for future deployments</li>
<li>Eliminates the need to remember complex command-line flags</li>
</ul>
<h4 id="2025-09-09-interactive-wrangler-assets-example-workflow">Example workflow</h4>
<pre tabindex="0"><code class="language-bash">&#35; Deploy your built static site&#10;wrangler deploy dist&#10;&#10;&#35; Wrangler will prompt:&#10;✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes&#10;✔ What do you want to name your project? … my-astro-site&#10;&#10;&#35; Automatically generates a wrangler.jsonc file and adds it to your project:&#10;{&#10;  &quot;name&quot;: &quot;my-astro-site&quot;,&#10;  &quot;compatibility_date&quot;: &quot;2025-09-09&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;directory&quot;: &quot;dist&quot;&#10;  }&#10;}&#10;&#10;&#35; Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file&#10;wrangler deploy&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-requirements">Requirements</h4>
<ul>
<li>You must use Wrangler version 4.24.4 or later in order to use this feature</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-08">Sep 8, 2025</time><div>
<h2 id="post-2025-09-08-custom-ike-id-ipsec-tunnels"><a href="/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/">Custom IKE ID for IPsec Tunnels</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span></div><div class="changelog-body"><p>Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.</p>
<p>This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the <a href="/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/">Custom IKE ID feature and the API call to configure it</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-08">Sep 8, 2025</time><div>
<h2 id="post-2025-09-08-reminders-about-two-factor-authentication-backup-codes"><a href="/changelog/post/2025-09-08-reminders-about-two-factor-authentication-backup-codes/">Reminders about two-factor authentication backup codes</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Two-factor authentication is the best way to help protect your account from account takeovers, but if you lose your second factor, you could be locked out of your account. Lock outs are one of the top reasons customers contact Cloudflare support, and our policies often don't allow us to bypass two-factor authentication for customers that are locked out. Today we are releasing an improvement where Cloudflare will periodically remind you to securely save your backup codes so you don't get locked out in the future.</p>
<h4 id="2025-09-08-reminders-about-two-factor-authentication-backup-codes-for-more-information">For more information</h4>
- [Two-factor authentication](/fundamentals/user-profiles/2fa/)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-08">Sep 8, 2025</time><div>
<h2 id="post-2025-09-08-waf-release"><a href="/changelog/post/2025-09-08-waf-release/">WAF Release - 2025-09-08</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week’s focus highlights newly disclosed vulnerabilities in web frameworks, enterprise applications, and widely deployed CMS plugins. The vulnerabilities include SSRF, authentication bypass, arbitrary file upload, and remote code execution (RCE), exposing organizations to high-impact risks such as unauthorized access, system compromise, and potential data exposure. In addition, security rule enhancements have been deployed to cover general command injection and server-side injection attacks, further strengthening protections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Next.js (CVE-2025-57822): Improper handling of redirects in custom middleware can lead to server-side request forgery (SSRF) when user-supplied headers are forwarded. Attackers could exploit this to access internal services or cloud metadata endpoints. The issue has been resolved in versions 14.2.32 and 15.4.7. Developers using custom middleware should upgrade and verify proper redirect handling in <code>next()</code> calls.</p>
</li>
<li>
<p>ScriptCase (CVE-2025-47227, CVE-2025-47228): In the Production Environment extension in Netmake ScriptCase through 9.12.006 (23), two vulnerabilities allow attackers to reset admin accounts and execute system commands, potentially leading to full compromise of affected deployments.</p>
</li>
<li>
<p>Sar2HTML (CVE-2025-34030): In Sar2HTML version 3.2.2 and earlier, insufficient input sanitization of the plot parameter allows remote, unauthenticated attackers to execute arbitrary system commands. Exploitation could compromise the underlying server and its data.</p>
</li>
<li>
<p>Zhiyuan OA (CVE-2025-34040): An arbitrary file upload vulnerability exists in the Zhiyuan OA platform. Improper validation in the <code>wpsAssistServlet</code> interface allows unauthenticated attackers to upload crafted files via path traversal, which can be executed on the web server, leading to remote code execution.</p>
</li>
<li>
<p>WordPress:Plugin:InfiniteWP Client (CVE-2020-8772): A vulnerability in the InfiniteWP Client plugin allows attackers to perform restricted actions and gain administrative control of connected WordPress sites.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities could allow attackers to gain unauthorized access, execute malicious code, or take full control of affected systems. The Next.js SSRF flaw may expose internal services or cloud metadata endpoints to attackers. Exploitations of ScriptCase and Sar2HTML could result in remote code execution, administrative takeover, and full server compromise. In Zhiyuan OA, the arbitrary file upload vulnerability allows attackers to execute malicious code on the web server, potentially exposing sensitive data and applications. The authentication bypass in WordPress InfiniteWP Client enables attackers to gain administrative access, risking data exposure and unauthorized control of connected sites.</p>
<p>Administrators are strongly advised to apply vendor patches immediately, remove unsupported software, and review authentication and access controls to mitigate these risks.</p>
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
        <code class="nb-rule-id" title="7c5812a31fd94996b3299f7e963d7afc">963d7afc</code>
</td>
<td>100007D</td>
<td>Command Injection - Common Attack Commands Args</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "Command Injection - Common Attack Commands" (ID: <code class="nb-rule-id" title="89557ce9b26e4d4dbf29e90c28345b9b">28345b9b</code>) for New WAF customers only.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cd528243d6824f7ab56182988230a75b">8230a75b</code>
</td>      
<td>100617</td>
<td>Next.js - SSRF - CVE:CVE-2025-57822</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="503b337dac5c409d8f833a6ba22dabf1">a22dabf1</code>
</td>
<td>100659_BETA</td>
<td>Common Payloads for Server-Side Template Injection - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Common Payloads for Server-Side Template Injection" (ID: <code class="nb-rule-id" title="21c7a963e1b749e7b1753238a28a42c4">a28a42c4</code>)</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6d24266148f24f5e9fa487f8b416b7ca">b416b7ca</code>
</td>
<td>100824B</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 3</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="154b217c43d04f11a13aeff05db1fa6b">5db1fa6b</code>
</td>
<td>100848</td>
<td>ScriptCase - Auth Bypass - CVE:CVE-2025-47227</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cad6f1c8c6d44ef59929e6532c62d330">2c62d330</code>
</td>
<td>100849</td>
<td>ScriptCase - Command Injection - CVE:CVE-2025-47228</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e7464139fd3e44938b56716bef971afd">ef971afd</code>
</td>
<td>100872</td>
<td>WordPress:Plugin:InfiniteWP Client - Missing Authorization - CVE:CVE-2020-8772</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0181ebb2cc234f2d863412e1bab19b0b">bab19b0b</code>
</td>
<td>100873</td>
<td>Sar2HTML - Command Injection - CVE:CVE-2025-34030</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="34d5c7c7b08b40eaad5b2bb3f24c0fbe">f24c0fbe</code>
</td>
<td>100875</td>
<td>Zhiyuan OA - Remote Code Execution - CVE:CVE-2025-34040</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>    
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-05">Sep 5, 2025</time><div>
<h2 id="post-2025-09-05-bidirectional-health-check-any-on-ramp"><a href="/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/">Bidirectional tunnel health checks are compatible with all Magic on-ramps</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span></div><div class="changelog-body"><p>All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.</p>
<p>Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.</p>
<p>There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.</p>
<p>Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-05">Sep 5, 2025</time><div>
<h2 id="post-2025-09-05-embeddinggemma"><a href="/changelog/post/2025-09-05-embeddinggemma/">Introducing EmbeddingGemma from Google on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to be a launch partner alongside <a href="https://developers.googleblog.com/en/introducing-embeddinggemma/">Google</a> to bring their newest embedding model, <strong>EmbeddingGemma</strong>, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.</p>
<p><a href="/workers-ai/models/embeddinggemma-300m/"><code>@cf/google/embeddinggemma-300m</code></a> is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.</p>
<p><strong>Using EmbeddingGemma in AI Search:</strong>
Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.</p>
<p>To use EmbeddingGemma for your AI Search projects:</p>
<ol>
<li>Go to <strong>Create</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/ai/ai-search">AI Search dashboard</a></li>
<li>Follow the setup flow for your new RAG instance</li>
<li>In the <strong>Generate Index</strong> step, open up <strong>More embedding models</strong> and select <code>@cf/google/embeddinggemma-300m</code> as your embedding model</li>
<li>Complete the setup to create an AI Search</li>
</ol>
<p>Try it out and let us know what you think!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-04">Sep 4, 2025</time><div>
<h2 id="post-2025-09-04-emergency-waf-release"><a href="/changelog/post/2025-09-04-emergency-waf-release/">WAF Release - 2025-09-04 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Sitecore’s Sitecore Experience Manager (XM), Sitecore Experience Platform (XP), specifically versions 9.0 through 9.3, and 10.0 through 10.4.
These flaws are caused by unsafe data deserialization and code reflection, leaving affected systems at high risk of exploitation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-53690: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53691: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53693: HTML Cache Poisoning through Unsafe Reflections</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could allow attackers to execute arbitrary code remotely on the affected system and conduct cache poisoning attacks, potentially leading to further compromise. Applying the latest vendor-released solution without delay is strongly recommended.</p>
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
        <code class="nb-rule-id" title="588edc74df1f4609b3c2f7ef0ee2c15e">0ee2c15e</code>
</td>
<td>100878</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53691</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>
</td>
<td>100631</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed94c7ce5301411a94a21a096c410240">6c410240</code>
</td>
<td>100879</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53690</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-04">Sep 4, 2025</time><div>
<h2 id="post-2025-09-02-increased-static-asset-limits"><a href="/changelog/post/2025-09-02-increased-static-asset-limits/">Increased static asset limits for Workers</a></h2>
<div class="changelog-badges"><span>workers</span><span>workers-for-platforms</span></div><div class="changelog-body"><p>You can now upload up to <strong>100,000 static assets</strong> per Worker version</p>
<ul>
<li>Paid and Workers for Platforms users can now upload up to <strong>100,000 static assets</strong> per Worker version, a 5x increase from the previous limit of 20,000.</li>
<li>Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker</li>
<li>The individual file size limit of 25 MiB remains unchanged for all customers.</li>
</ul>
<p>This increase allows you to build larger applications with more static assets without hitting limits.</p>
<h4 id="2025-09-02-increased-static-asset-limits-wrangler">Wrangler</h4>
<p>To take advantage of the increased limits, you must use <strong>Wrangler version 4.34.0 or higher</strong>.
Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.</p>
<h4 id="2025-09-02-increased-static-asset-limits-learn-more">Learn more</h4>
<p>For more information about Workers static assets, see the <a href="/workers/static-assets/">Static Assets documentation</a> and <a href="/workers/platform/limits/#static-assets">Platform Limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-04">Sep 4, 2025</time><div>
<h2 id="post-2025-09-03-new-workers-api"><a href="/changelog/post/2025-09-03-new-workers-api/">A new, simpler REST API for Cloudflare Workers (Beta)</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now manage <a href="/api/resources/workers/subresources/beta/subresources/workers/methods/create/"><strong>Workers</strong></a>, <a href="/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)"><strong>Versions</strong></a>, and <a href="/api/resources/workers/subresources/scripts/subresources/content/methods/update/"><strong>Deployments</strong></a> as separate resources with a new, resource-oriented API (Beta).</p>
<p>This new API is supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a> and the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare Typescript SDK</a>, allowing platform teams to manage a Worker's infrastructure in Terraform, while development teams handle code deployments from a separate repository or workflow. We also designed this API with AI agents in mind, as a clear, predictable structure is essential for them to reliably build, test, and deploy applications.</p>
<h4 id="2025-09-03-new-workers-api-try-it-out">Try it out</h4>
- [**New beta API endpoints**](/api/resources/workers/subresources/beta/)
- [**Cloudflare TypeScript SDK v5.0.0**](https://github.com/cloudflare/cloudflare-typescript)
- [**Cloudflare Go SDK v6.0.0**](https://github.com/cloudflare/cloudflare-go)
- [**Terraform provider v5.9.0**](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs): [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) , [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version), and [`cloudflare_workers_deployments`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_deployment) resources.
- See full examples in our [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
<h4 id="2025-09-03-new-workers-api-before-eight-endpoints-with-mixed-responsibilities">Before: Eight+ endpoints with mixed responsibilities</h4>
<img src="/assets/upstream/images/workers/platform/api-before.png" alt="Before">
<p>The existing API was originally designed for simple, one-shot script uploads:</p>
<pre tabindex="0"><code class="language-sh">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME&quot; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;    &#45;F &#x27;metadata={&#10;      &quot;main_module&quot;: &quot;worker.js&quot;,&#10;      &quot;compatibility_date&quot;: &quot;$today$&quot;&#10;    }&#x27; \&#10;    &#45;F &quot;worker.js=@worker.js;type=application/javascript+module&quot;&#10;</code></pre>
<p>This API worked for creating a basic Worker, uploading all of its code, and deploying it immediately — but came with challenges:</p>
<ul>
<li>
<p><strong>A Worker couldn't exist without code</strong>: To create a Worker, you had to upload its code in the same API request. This meant platform teams couldn't provision Workers with the proper settings, and then hand them off to development teams to deploy the actual code.</p>
</li>
<li>
<p><strong>Several endpoints implicitly created deployments</strong>: Simple updates like adding a secret or changing a script's content would implicitly create a new version and immediately deploy it.</p>
</li>
<li>
<p><strong>Updating a setting was confusing</strong>: Configuration was scattered across eight endpoints with overlapping responsibilities.  This ambiguity made it difficult for human developers (and even more so for AI agents) to reliably update a Worker via API.</p>
</li>
<li>
<p><strong>Scripts used names as primary identifiers</strong>: This meant simple renames could turn into a risky migration, requiring you to create a brand new Worker and update every reference. If you were using Terraform, this could inadvertently destroy your Worker altogether.</p>
</li>
</ul>
<h4 id="2025-09-03-new-workers-api-after-three-resources-with-clear-boundaries">After: Three resources with clear boundaries</h4>
<img src="/assets/upstream/images/workers/platform/api-after.png" alt="After">
The new API introduces cleaner resource management with three core resources: [**Worker**](/api/resources/workers/subresources/beta/subresources/workers/methods/create/), [**Versions**](/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)), and [**Deployment**](/api/resources/workers/subresources/scripts/subresources/content/methods/update/).
<p>All endpoints now use simple JSON payloads, with script content embedded as <code>base64</code>-encoded strings -- a more consistent and reliable approach than the previous <code>multipart/form-data</code> format.</p>
<ul>
<li>
<p><strong>Worker</strong>: The parent resource representing your application. It has a stable UUID and holds persistent settings like <code>name</code>, <code>tags</code>, and <code>logpush</code>. You can now create a Worker to establish its identity and settings <strong>before</strong> any code is uploaded.</p>
</li>
<li>
<p><strong>Version</strong>: An immutable snapshot of your code and its specific configuration, like bindings and <code>compatibility_date</code>. Creating a new version is a safe action that doesn't affect live traffic.</p>
</li>
<li>
<p><strong>Deployment</strong>: An explicit action that directs traffic to a specific version.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17786.md")</aside>
<h4 id="2025-09-03-new-workers-api-why-this-matters">Why this matters</h4>
<h4 id="2025-09-03-new-workers-api-you-can-now-create-workers-before-uploading-code">You can now create Workers before uploading code</h4>
<p>Workers are now standalone resources that can be created and configured without any code. Platform teams can provision Workers with the right settings, then hand them off to development teams for implementation.</p>
<h4 id="2025-09-03-new-workers-api-example-typescript-sdk">Example: Typescript SDK</h4>
<pre tabindex="0"><code class="language-ts">// Step 1: Platform team creates the Worker resource (no code needed)&#10;const worker = await client.workers.beta.workers.create({&#10;  name: &quot;payment-service&quot;,&#10;  account_id: &quot;...&quot;,&#10;  observability: {&#10;    enabled: true,&#10;  },&#10;});&#10;<p>// Step 2: Development team adds code and creates a version later&#10;const version = await client.workers.beta.workers.versions.create(worker.id, {&#10;account_id: &quot;...&quot;,&#10;main_module: &quot;worker.js&quot;,&#10;compatibility_date: &quot;$today&quot;,&#10;bindings: [ /<em>...</em>/ ],&#10;modules: [&#10;{&#10;name: &quot;worker.js&quot;,&#10;content_type: &quot;application/javascript+module&quot;,&#10;content_base64: Buffer.from(scriptContent).toString(&quot;base64&quot;),&#10;},&#10;],&#10;});</p>&#10;<p>// Step 3: Deploy explicitly when ready&#10;const deployment = await client.workers.scripts.deployments.create(worker.name, {&#10;account_id: &quot;...&quot;,&#10;strategy: &quot;percentage&quot;,&#10;versions: [&#10;{&#10;percentage: 100,&#10;version_id: version.id,&#10;},&#10;],&#10;});&#10;</code></pre></p>
<h4 id="2025-09-03-new-workers-api-example-terraform">Example: Terraform</h4>
If you use Terraform, you can now declare the Worker in your Terraform configuration and manage configuration outside of Terraform in your Worker's [`wrangler.jsonc` file](/workers/wrangler/configuration/) and deploy code changes using [Wrangler](/workers/wrangler/).
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = &quot;...&quot;&#10;  name = &quot;my-important-service&quot;&#10;}&#10;&#35; Manage Versions and Deployments here or outside of Terraform&#10;&#35; resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {}&#10;&#35; resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-deployments-are-always-explicit-never-implicit">Deployments are always explicit, never implicit</h4>
<p>Creating a version and deploying it are now always explicit, separate actions - never implicit side effects. To update version-specific settings (like bindings), you create a new version with those changes. The existing deployed version remains unchanged until you explicitly deploy the new one.</p>
<pre tabindex="0"><code class="language-sh">&#35; Step 1: Create a new version with updated settings (doesn&#x27;t affect live traffic)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;MY_NEW_ENV_VAR&quot;,&#10;      &quot;text&quot;: &quot;new_value&quot;,&#10;      &quot;type&quot;: &quot;plain_text&quot;&#10;    }&#10;  ],&#10;  &quot;modules&quot;: [...]&#10;}&#10;&#10;&#35; Step 2: Explicitly deploy when ready (now affects live traffic)&#10;POST /workers/scripts/{script_name}/deployments&#10;{&#10;  &quot;strategy&quot;: &quot;percentage&quot;,&#10;  &quot;versions&quot;: [&#10;    {&#10;      &quot;percentage&quot;: 100,&#10;      &quot;version_id&quot;: &quot;new_version_id&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-settings-are-clearly-organized-by-scope">Settings are clearly organized by scope</h4>
Configuration is now logically divided: [**Worker settings**](/api/resources/workers/subresources/beta/subresources/workers/) (like `name` and `tags`) persist across all versions, while [**Version settings**](/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) (like `bindings` and `compatibility_date`) are specific to each code snapshot.
<pre tabindex="0"><code class="language-sh">&#35; Worker settings (the parent resource)&#10;PUT /workers/workers/{id}&#10;{&#10;  &quot;name&quot;: &quot;payment-service&quot;,&#10;  &quot;tags&quot;: [&quot;production&quot;],&#10;  &quot;logpush&quot;: true,&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Version settings (the &quot;code&quot;)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [...],&#10;  &quot;modules&quot;: [...]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-workers-api-endpoints-now-support-uuids-in-addition-to-names"><code>/workers</code> API endpoints now support UUIDs (in addition to names)</h4>
<p>The <code>/workers/workers/</code> path now supports addressing a Worker by both its immutable UUID and its mutable name.</p>
<pre tabindex="0"><code class="language-sh">&#35; Both work for the same Worker&#10;GET /workers/workers/29494978e03748669e8effb243cf2515  # UUID (stable for automation)&#10;GET /workers/workers/payment-service                  # Name (convenient for humans)&#10;</code></pre>
<p>This dual approach means:</p>
<ul>
<li>Developers can use readable names for debugging.</li>
<li>Automation can rely on stable UUIDs to prevent errors when Workers are renamed.</li>
<li>Terraform can rename Workers without destroying and recreating them.</li>
</ul>
<h4 id="2025-09-03-new-workers-api-learn-more">Learn more</h4>
- [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
- [API documentation](/api/resources/workers/subresources/beta/)
- [Versions and Deployments overview](/workers/versions-and-deployments/)
<h4 id="2025-09-03-new-workers-api-technical-notes">Technical notes</h4>
<ul>
<li>The pre-existing Workers REST API remains fully supported. Once the new API exits beta, we'll provide a migration timeline with ample notice and comprehensive migration guides.</li>
<li>Existing Terraform resources and SDK methods will continue to be fully supported through the current major version.</li>
<li>While the Deployments API currently remains on the <code>/scripts/</code> endpoint, we plan to introduce a new Deployments endpoint under <code>/workers/</code> to match the new API structure.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-03">Sep 3, 2025</time><div>
<h2 id="post-2025-09-03-rate-limiting-improvement"><a href="/changelog/post/2025-09-03-rate-limiting-improvement/">Introducing new headers for rate limiting on Cloudflare's API</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare's API now supports rate limiting headers using the pattern developed by the <a href="https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html">IETF draft on rate limiting</a>. This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.</p>
<p>Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.</p>
<p>As always, if you need any help with rate limits, please contact Support.</p>
<h4 id="2025-09-03-rate-limiting-improvement-changes">Changes</h4>
<h4 id="2025-09-03-rate-limiting-improvement-new-headers">New Headers</h4>
<p><strong>Headers that are always returned:</strong></p>
<ul>
<li><code>Ratelimit</code>: List of service limit items, composed of the limit name, the remaining quota (<code>r</code>) and the time next window resets (<code>t</code>). For example: <code>&quot;default&quot;;r=50;t=30</code></li>
<li><code>Ratelimit-Policy</code>: List of quota policy items, composed of the policy name, the total quota (<code>q</code>) and the time window the quota applies to (<code>w</code>). For example: <code>&quot;burst&quot;;q=100;w=60</code></li>
</ul>
<p><strong>Returned only when a rate limit has been reached (error code: 429):</strong></p>
<ul>
<li>Retry-After: Number of Seconds until more capacity is available, rounded up</li>
</ul>
<h4 id="2025-09-03-rate-limiting-improvement-sdk-back-offs">SDK Back offs</h4>
- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached. 
<h4 id="2025-09-03-rate-limiting-improvement-graphql-and-edge-apis">GraphQL and Edge APIs</h4>
These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL. 
<h4 id="2025-09-03-rate-limiting-improvement-for-more-information">For more information</h4>
* [Rate limits at Cloudflare](https://developers.cloudflare.com/fundamentals/api/reference/limits/)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-03">Sep 3, 2025</time><div>
<h2 id="post-2025-09-03-log-headers-and-cookies"><a href="/changelog/post/2025-09-03-log-headers-and-cookies/">Logging headers and cookies using custom fields</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p><a href="/log-explorer/">Log Explorer</a> now supports logging and filtering on header or cookie fields in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code> dataset</a>.</p>
<p>Create a custom field to log desired header or cookie values into the <code>http_requests</code> dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/edit-custom-fields.png" alt="Edit Custom fields" /></p>
<p>For more details, refer to <a href="/log-explorer/log-search/#headers-and-cookies">Headers and cookies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-02">Sep 2, 2025</time><div>
<h2 id="post-2025-09-02-tunnel-networks-list-endpoints-new-default"><a href="/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-02">Sep 2, 2025</time><div>
<h2 id="post-2025-09-01-updated-new-roles"><a href="/changelog/post/2025-09-01-updated-new-roles/">Updated Email security roles</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>To provide more granular controls, we refined the <a href="/cloudflare-one/roles-permissions/#email-security-roles">existing roles</a> for Email security and launched a new Email security role as well.</p>
<p>All Email security roles no longer have read or write access to any of the other Zero Trust products:</p>
<ul>
<li><strong>Email Configuration Admin</strong></li>
<li><strong>Email Integration Admin</strong></li>
<li><strong>Email security Read Only</strong></li>
<li><strong>Email security Analyst</strong></li>
<li><strong>Email security Policy Admin</strong></li>
<li><strong>Email security Reporting</strong></li>
</ul>
<p>To configure <a href="/cloudflare-one/email-security/outbound-dlp/">Data Loss Prevention (DLP)</a> or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation">Remote Browser Isolation (RBI)</a>, you now need to be an admin for the Zero Trust dashboard with the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>Also through customer feedback, we have created a new additive role to allow <strong>Email security Analyst</strong> to create, edit, and delete Email security policies, without needing to provide access via the <strong>Email Configuration Admin</strong> role. This role is called <strong>Email security Policy Admin</strong>, which can read all settings, but has write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-01">Sep 1, 2025</time><div>
<h2 id="post-2025-09-01-waf-release"><a href="/changelog/post/2025-09-01-waf-release/">WAF Release - 2025-09-01</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, a critical vulnerability was disclosed in Fortinet FortiWeb (versions 7.6.3 and below, versions 7.4.7 and below, versions 7.2.10 and below, and versions 7.0.10 and below), linked to improper parameter handling that could allow unauthorized access.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Fortinet FortiWeb (CVE-2025-52970): A vulnerability may allow an unauthenticated remote attacker with access to non-public information to log in as any existing user on the device via a specially crafted request.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could allow an unauthenticated attacker to impersonate any existing user on the device, potentially enabling them to modify system settings or exfiltrate sensitive information, posing a serious security risk. Upgrading to the latest vendor-released version is strongly recommended.</p>
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
        <code class="nb-rule-id" title="636b145a49a84946b990d4fac49b7cf8">c49b7cf8</code>
</td>
<td>100586</td>
<td>Fortinet FortiWeb - Auth Bypass - CVE:CVE-2025-52970</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b5ef1ace353841a0856b5e07790c9dde">790c9dde</code>
</td>
<td>100136C</td>
<td>XSS - JavaScript - Headers and Body</td>
<td>N/A</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-29">Aug 29, 2025</time><div>
<h2 id="post-2025-08-29-smart-tiered-cache-fallback-to-generic"><a href="/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/">Smart Tiered Cache Fallback to Generic</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p><a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a> now falls back to <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Tiered Cache</a> when the origin location cannot be determined, improving cache precision for your content.</p>
<p>Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.</p>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-how-it-works">How it works</h4>
<p>When Smart Tiered Cache falls back to Generic Tiered Cache:</p>
<ol>
<li><strong>Multiple upper-tiers</strong>: Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.</li>
<li><strong>Distributed cache requests</strong>: Lower-tier data centers can query any available upper-tier for cached content.</li>
<li><strong>Improved global coverage</strong>: Provides better cache hit ratios across geographically distributed visitors.</li>
<li><strong>Automatic fallback</strong>: Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.</li>
</ol>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-benefits">Benefits</h4>
<ul>
<li><strong>Preserves high performance during fallback</strong>: Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.</li>
<li><strong>Minimizes latency impact</strong>: Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.</li>
<li><strong>Seamless experience</strong>: No configuration changes or intervention required when fallback occurs.</li>
<li><strong>Improved resilience</strong>: Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.</li>
</ul>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-get-started">Get started</h4>
<p>This improvement is automatically applied to all zones using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. No action is required on your part.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-29">Aug 29, 2025</time><div>
<h2 id="post-2025-08-29-warp-AI-diag-analyzer"><a href="/changelog/post/2025-08-29-warp-AI-diag-analyzer/">Cloudflare One WARP Diagnostic AI Analyzer</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>We're excited to share a new AI feature, the <a href="https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/">WARP diagnostic analyzer</a>, to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the <a href="https://dash.cloudflare.com/one/">Cloudflare One dashboard</a> to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">remote captures</a> of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">WARP diagnostic logs</a>. The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta">WARP diagnostics analyzer (beta)</a> to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-29">Aug 29, 2025</time><div>
<h2 id="post-2025-08-29-dex-mcp-server"><a href="/changelog/post/2025-08-29-dex-mcp-server/">DEX MCP Server</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device connectivity and performance across your Cloudflare SASE deployment.</p>
<p>We've released an MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for DEX.</p>
<p>The DEX MCP server is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.</p>
<p>Customers can test the new DEX MCP server in less than one minute. To learn more, read the <a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-29">Aug 29, 2025</time><div>
<h2 id="post-2025-08-29-terrform-v5.9-provider"><a href="/changelog/post/2025-08-29-terrform-v5.9-provider/">Terraform v5.9 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0">changelog</a> in GitHub.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-issues-closed">Issues Closed</h4>
- [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare_zero_trust_access_application is not idempotent](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare_workers_script) Durable Object migrations not applied](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare_zone suddenly started showing drift](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare_dns_records is always updated in-place](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare_zero_trust_access_application type warp diff on every apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare_account_member invalid type 'string' for field 'roles'](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new issue if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-29">Aug 29, 2025</time><div>
<h2 id="post-2025-08-29-emergency-waf-release"><a href="/changelog/post/2025-08-29-emergency-waf-release/">WAF Release - 2025-08-29 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2025-55173: Arbitrary file download from the server via image optimization.</p>
</li>
<li>
<p>CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.</p>
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
        <code class="nb-rule-id" title="ea55f8aac44246cc9b827eea9ff4bfe3">9ff4bfe3</code>
</td>
<td>100613</td>
<td>Next.js - Dangerous File Download - CVE:CVE-2025-55173</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e2b2d77a79cc4a76bf7ba53d69b9ea7d">69b9ea7d</code>
</td>
<td>100616</td>
<td>Next.js - Information Disclosure - CVE:CVE-2025-57752</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-27">Aug 27, 2025</time><div>
<h2 id="post-2025-08-27-ai-crawl-control-launch"><a href="/changelog/post/2025-08-27-ai-crawl-control-launch/">Enhanced crawler insights and custom 402 responses</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre tabindex="0"><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-27">Aug 27, 2025</time><div>
<h2 id="post-2025-08-27-shadow-it-analytics"><a href="/changelog/post/2025-08-27-shadow-it-analytics/">Shadow IT - SaaS analytics dashboard</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-27">Aug 27, 2025</time><div>
<h2 id="post-2025-08-27-partner-models"><a href="/changelog/post/2025-08-27-partner-models/">Deepgram and Leonardo partner models now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>New state-of-the-art models have landed on Workers AI! This time, we're introducing new <strong>partner models</strong> trained by our friends at <a href="https://deepgram.com">Deepgram</a> and <a href="https://leonardo.ai">Leonardo</a>, hosted on Workers AI infrastructure.</p>
<p>As well, we're introuding a new turn detection model that enables you to detect when someone is done speaking — useful for building voice agents!</p>
<p>Read the <a href="https://blog.cloudflare.com/workers-ai-partner-models">blog</a> for more details and check out some of the new models on our platform:</p>
<ul>
<li><a href="/workers-ai/models/aura-1"><code>@cf/deepgram/aura-1</code></a> is a text-to-speech model that allows you to input text and have it come to life in a customizable voice</li>
<li><a href="/workers-ai/models/nova-3"><code>@cf/deepgram/nova-3</code></a> is speech-to-text model that transcribes multilingual audio at a blazingly fast speed</li>
<li><a href="/workers-ai/models/smart-turn-v2"><code>@cf/pipecat-ai/smart-turn-v2</code></a> helps you detect when someone is done speaking</li>
<li><a href="/workers-ai/models/lucid-origin"><code>@cf/leonardo/lucid-origin</code></a> is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction</li>
<li><a href="/workers-ai/models/phoenix-1.0"><code>@cf/leonardo/phoenix-1.0</code></a> is a text-to-image model with exceptional prompt adherence and coherent text</li>
</ul>
<p>You can filter out new partner models with the <code>Partner</code> capability on our <a href="/workers-ai/models">Models</a> page.</p>
<p>As well, we're introducing WebSocket support for some of our audio models, which you can filter though the <code>Realtime</code> capability on our <a href="/workers-ai/models">Models</a> page. WebSockets allows you to create a bi-directional connection to our inference server with low latency — perfect for those that are building voice agents.</p>
<p>An example python snippet on how to use WebSockets with our new Aura model:</p>
<pre tabindex="0"><code>import json&#10;import os&#10;import asyncio&#10;import websockets&#10;&#10;uri = f&quot;wss://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/deepgram/aura-1&quot;&#10;&#10;input = [&#10;    &quot;Line one, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line two, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line three, out of three lines that will be provided to the aura model. This is a last line.&quot;,&#10;]&#10;&#10;&#10;async def text_to_speech():&#10;    async with websockets.connect(uri, additional_headers={&quot;Authorization&quot;: os.getenv(&quot;CF_TOKEN&quot;)}) as websocket:&#10;        print(&quot;connection established&quot;)&#10;        for line in input:&#10;            print(f&quot;sending `{line}`&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Speak&quot;, &quot;text&quot;: line}))&#10;&#10;            print(&quot;line was sent, flushing&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Flush&quot;}))&#10;            print(&quot;flushed, recving&quot;)&#10;            resp = await websocket.recv()&#10;            print(f&quot;response received {resp}&quot;)&#10;&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    asyncio.run(text_to_speech())&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-26">Aug 26, 2025</time><div>
<h2 id="post-2025-08-26-casb-ai-integrations"><a href="/changelog/post/2025-08-26-casb-ai-integrations/">New CASB integrations for ChatGPT, Claude, and Gemini</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p><a href="https://www.cloudflare.com/zero-trust/products/casb/">Cloudflare CASB</a> now supports three of the most widely used GenAI platforms — <strong>OpenAI ChatGPT</strong>, <strong>Anthropic Claude</strong>, and <strong>Google Gemini</strong>. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.</p>
<p><img src="/assets/upstream/images/casb/changelog/casb-ai-integrations-preview.png" alt="Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations." /></p>
<h4 id="2025-08-26-casb-ai-integrations-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Agentless connections</strong> — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required</li>
<li><strong>Posture management</strong> — detect insecure settings and misconfigurations that could lead to data exposure</li>
<li><strong>DLP detection</strong> — identify sensitive data in uploaded chat attachments or files</li>
<li><strong>GenAI-specific insights</strong> — surface risks unique to each provider’s capabilities</li>
</ul>
<h4 id="2025-08-26-casb-ai-integrations-learn-more">Learn more</h4>
<ul>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/">ChatGPT integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/">Claude integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/">Gemini integration docs</a></li>
</ul>
<p>These integrations are available to all Cloudflare One customers today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-26">Aug 26, 2025</time><div>
<h2 id="post-2025-08-26-access-mcp-oauth"><a href="/changelog/post/2025-08-26-access-mcp-oauth/">Manage and restrict access to internal MCP servers with Cloudflare Access</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p><a href="/cloudflare-one/access-controls/ai-controls/linked-apps/">Self-hosted applications</a> in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.</p>
<p>For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog post</a> on the Cloudflare Blog.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-26">Aug 26, 2025</time><div>
<h2 id="post-2025-08-26-mcp-server-portals"><a href="/changelog/post/2025-08-26-mcp-server-portals/">MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/access/mcp-server-portal.png" alt="MCP server portal" /></p>
<p>An <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:</p>
<ul>
<li><strong>Streamlined access to multiple MCP servers</strong>: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.</li>
<li><strong>Customized tools per portal</strong>: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.</li>
<li><strong>Observability</strong>: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.</li>
</ul>
<p>This is available in an open beta for all customers across all plans! For more information check out our <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog</a> for this release.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/35/">Previous</a><span>Page 36 of 50</span><a class="pagination-next" rel="next" href="/changelog/37/">Next</a></nav>
</div>
