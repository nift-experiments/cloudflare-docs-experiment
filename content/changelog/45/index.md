---
cp9:
  canonical: https://developers.cloudflare.com/changelog/45/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 45 | Cloudflare Docs
  head_html: <title>Changelog - page 45 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/45/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 45"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/45/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/45/#page","headline":"Changelog - page 45 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/45/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/45/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-04-04">Apr 4, 2025</time><div>
<h2 id="post-2025-04-04-workers-fetch-api-override-cache-rules"><a href="/changelog/post/2025-04-04-workers-fetch-api-override-cache-rules/">Workers Fetch API can override Cache Rules</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now programmatically override Cache Rules using the <code>cf</code> object in the <code>fetch()</code> command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.</p>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-how-it-works">How it works</h4>
<p>Using the <code>cf</code> object in <code>fetch()</code>, you can override specific Cache Rules settings by:</p>
<ol>
<li><strong>Setting custom cache options</strong>: Pass cache properties in the <code>cf</code> object as the second argument to <code>fetch()</code> to override default Cache Rules.</li>
<li><strong>Dynamic cache control</strong>: Apply different caching strategies based on request headers, cookies, or other runtime conditions.</li>
<li><strong>Per-request customization</strong>: Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.</li>
<li><strong>Programmatic cache management</strong>: Implement complex caching logic that adapts to your application's needs.</li>
</ol>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-what-can-be-configured">What can be configured</h4>
<p>Workers can override the following Cache Rules settings through the <code>cf</code> object:</p>
<ul>
<li><strong><code>cacheEverything</code></strong>: Treat all content as static and cache all file types beyond the default cached content.</li>
<li><strong><code>cacheTtl</code></strong>: Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.</li>
<li><strong><code>cacheTtlByStatus</code></strong>: Set different TTLs based on the response status code (for example, <code>{ &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 }</code>).</li>
<li><strong><code>cacheKey</code></strong>: Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).</li>
<li><strong><code>cacheTags</code></strong>: Append additional cache tags for targeted cache purging operations.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Enhanced flexibility</strong>: Customize cache behavior without modifying zone-level Cache Rules.</li>
<li><strong>Dynamic optimization</strong>: Adjust caching strategies in real-time based on request context.</li>
<li><strong>Simplified configuration</strong>: Reduce the number of Cache Rules needed by handling edge cases programmatically.</li>
<li><strong>Improved performance</strong>: Fine-tune cache behavior for specific use cases to maximize hit rates.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-get-started">Get started</h4>
<p>To get started, refer to the <a href="/workers/runtime-apis/fetch/">Workers Fetch API documentation</a> and the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties">cf object properties documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-03">Apr 3, 2025</time><div>
<h2 id="post-2025-04-01-purge-for-all"><a href="/changelog/post/2025-04-01-purge-for-all/">All cache purge methods now available for all plans</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now access all Cloudflare cache purge methods — no matter which plan you’re on. Whether you need to update a single asset or instantly invalidate large portions of your site’s content, you now have the same powerful tools previously reserved for Enterprise customers.</p>
<p><strong>Anyone on Cloudflare can now:</strong></p>
<ol>
<li><a href="/cache/how-to/purge-cache/purge-everything/">Purge Everything</a>: Clears all cached content associated with a website.</li>
<li><a href="/cache/how-to/purge-cache/purge_by_prefix/">Purge by Prefix</a>: Targets URLs sharing a common prefix.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-hostname/">Purge by Hostname</a>: Invalidates content by specific hostnames.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-single-file/">Purge by URL (single-file purge)</a>: Precisely targets individual URLs.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-tags/">Purge by Tag</a>: Uses Cache-Tag response headers to invalidate grouped assets, offering flexibility for complex cache management scenarios.</li>
</ol>
<p>Want to learn how each purge method works, when to use them, or what limits apply to your plan? Dive into our <a href="/cache/how-to/purge-cache/">purge cache documentation</a> and <a href="https://developers.cloudflare.com/api/resources/cache/methods/purge/">API reference</a> for all the details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-02">Apr 2, 2025</time><div>
<h2 id="post-2025-04-02-waf-release"><a href="/changelog/post/2025-04-02-waf-release/">WAF Release - 2025-04-02</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="8b8074e73b7d4aba92fc68f3622f0483">622f0483</code>
</td>
<td>100732</td>
<td>Sitecore - Code Injection - CVE:CVE-2025-27218</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8350947451a1401c934f5e660f101cca">0f101cca</code>
</td>
<td>100733</td>
<td>
				Angular-Base64-Upload - Remote Code Execution - CVE:CVE-2024-42640
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a9ec9cf625ff42769298671d1bbcd247">1bbcd247</code>
</td>
<td>100734</td>
<td>Apache Camel - Remote Code Execution - CVE:CVE-2025-29891</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3d6bf99039b54312a1a2165590aea1ca">90aea1ca</code>
</td>
<td>100735</td>
<td>
				Progress Software WhatsUp Gold - Remote Code Execution -
				CVE:CVE-2024-4885
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d104e3246dc14ac7851b4049d9d8c5f2">d9d8c5f2</code>
</td>
<td>100737</td>
<td>Apache Tomcat - Remote Code Execution - CVE:CVE-2025-24813</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="21c7a963e1b749e7b1753238a28a42c4">a28a42c4</code>
</td>
<td>100659</td>
<td>Common Payloads for Server-side Template Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="887843ffbe90436dadd1543adaa4b037">daa4b037</code>
</td>
<td>100659</td>
<td>Common Payloads for Server-side Template Injection - Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3565b80fc5b541b4832c0fc848f6a9cf">48f6a9cf</code>
</td>
<td>100642</td>
<td>LDAP Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="44d7bf9bf0fa4898b8579573e0713e9f">e0713e9f</code>
</td>
<td>100642</td>
<td>LDAP Injection Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e35c9a670b864a3ba0203ffb1bc977d1">1bc977d1</code>
</td>
<td>100005</td>
<td>
				DotNetNuke - File Inclusion - CVE:CVE-2018-9126, CVE:CVE-2011-1892,
				CVE:CVE-2022-31474
</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="cd8db44032694fdf8d6e22c1bb70a463">bb70a463</code>
</td>
<td>100527</td>
<td>Apache Struts - CVE:CVE-2021-31805</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0d838d9ab046443fa3f8b3e50c99546a">0c99546a</code>
</td>
<td>100702</td>
<td>Command Injection - CVE:CVE-2022-24108</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="533fbad558ce4c5ebcf013f09a5581d0">9a5581d0</code>
</td>
<td>100622C</td>
<td>
				Ivanti - Command Injection - CVE:CVE-2023-46805, CVE:CVE-2024-21887,
				CVE:CVE-2024-22024
</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04176552f62f4b75bf65981206d0b009">06d0b009</code>
</td>
<td>100536C</td>
<td>GraphQL Command Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="25883bf28575433c952b830c1651d0c8">1651d0c8</code>
</td>
<td>100536</td>
<td>GraphQL Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7b70da1bb8d243bd80cd7a73af00f61d">af00f61d</code>
</td>
<td>100536A</td>
<td>GraphQL Introspection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58c4853c250946359472b7eaa41e5b67">a41e5b67</code>
</td>
<td>100536B</td>
<td>GraphQL SSRF</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c241ed5f5bd44b19e17476b433e5b3d">433e5b3d</code>
</td>
<td>100559A</td>
<td>Prototype Pollution - Common Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="af748489e1c2411d80d855954816b26f">4816b26f</code>
</td>
<td>100559A</td>
<td>Prototype Pollution - Common Payloads - Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ccc47ab7e34248c09546c284fcea5ed2">fcea5ed2</code>
</td>
<td>100734</td>
<td>Apache Camel - Remote Code Execution - CVE:CVE-2025-29891</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-02">Apr 2, 2025</time><div>
<h2 id="post-2025-04-01-casb-email-security"><a href="/changelog/post/2025-04-01-casb-email-security/">CASB and Email security</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>With Email security, you get two free CASB integrations.</p>
<p>Use one SaaS integration for Email security to sync with your directory of users, take actions on delivered emails, automatically provide EMLs for reclassification requests for clean emails, discover CASB findings and more.</p>
<p>With the other integration, you can have a separate SaaS integration for CASB findings for another SaaS provider.</p>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/">Add an integration</a> to learn more about this feature.</p>
<p><img src="/assets/upstream/images/changelog/email-security/CASB-EmailSecurity.png" alt="CASB-EmailSecurity" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-27">Mar 27, 2025</time><div>
<h2 id="post-2025-03-27-ai-domains-available"><a href="/changelog/post/2025-03-27-ai-domains-available/">Register and renew .ai and .shop domains at cost</a></h2>
<div class="changelog-badges"><span>registrar</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/registrar/2025-03-27-ai-domains-available.png" alt="Example search for .ai domains" /></p>
<p>Cloudflare Registrar now supports <code>.ai</code> and <code>.shop</code> domains. These are two of our most highly-requested top-level domains (TLDs) and are great additions to the <a href="https://domains.cloudflare.com/tlds">300+ other TLDs we support</a>.</p>
<p>Starting today, customers can:</p>
<ul>
<li>Register and renew these domains <em>at cost</em> without any markups or add-on fees</li>
<li>Enjoy best-in-class security and performance with native integrations with Cloudflare DNS, CDN, and SSL services like one-click DNSSEC</li>
<li>Combat domain hijacking with <a href="https://www.cloudflare.com/products/registrar/custom-domain-protection/">Custom Domain Protection</a> (available on enterprise plans)</li>
</ul>
<p>We can't wait to see what AI and e-commerce projects you deploy on Cloudflare. To get started, transfer your domains to Cloudflare or <a href="https://domains.cloudflare.com/">search for new ones to register</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-27">Mar 27, 2025</time><div>
<h2 id="post-2025-03-25-pause-purge-queues"><a href="/changelog/post/2025-03-25-pause-purge-queues/">New Pause &amp; Purge APIs for Queues</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/">Queues</a> now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:</p>
<ul>
<li>Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug</li>
<li>You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog</li>
<li>Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed</li>
</ul>
<p>To pause a queue using <a href="/workers/wrangler/">Wrangler</a>, run the <code>pause-delivery</code> command. Paused queues continue to receive messages. And you can easily unpause a queue using the <code>resume-delivery</code> command.</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues pause-delivery my-queue&#10;Pausing message delivery for queue my-queue.&#10;Paused message delivery for queue my-queue.&#10;&#10;$ wrangler queues resume-delivery my-queue&#10;Resuming message delivery for queue my-queue.&#10;Resumed message delivery for queue my-queue.&#10;</code></pre>
<p>Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues purge my-queue&#10;✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue&#10;Purged queue &#x27;my-queue&#x27;&#10;</code></pre>
<p>You can also do these operations using the <a href="/api/resources/queues/">Queues REST API</a>, or the dashboard page for a queue.</p>
<p><img src="/assets/upstream/images/queues/pause-purge.png" alt="Pause and purge using the dashboard" /></p>
<p>This feature is available on all new and existing queues. Head over to the <a href="/queues/configuration/pause-purge">pause and purge documentation</a> to learn more. And if you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-27">Mar 27, 2025</time><div>
<h2 id="post-2025-03-27-automatic-audit-logs-beta-release"><a href="/changelog/post/2025-03-27-automatic-audit-logs-beta-release/">Audit logs (version 2) - Beta Release</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.</p>
<p>Availability: Audit logs (version 2) is now in Beta, with support limited to <strong>API access</strong>.</p>
<p>Use the following API endpoint to retrieve audit logs:</p>
<pre tabindex="0"><code class="language-js">GET https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/logs/audit?since=&lt;date&gt;&amp;before=&lt;date&gt;&#10;</code></pre>
<p>You can access detailed documentation for audit logs (version 2) Beta API release <a href="https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/">here</a>.</p>
<p><strong>Key Improvements in the Beta Release:</strong></p>
<ul>
<li>
<p><strong>Automated &amp; standardized logging</strong>: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.</p>
</li>
<li>
<p><strong>Expanded product coverage</strong>: Increased audit log coverage from 75% to 95%. Key API endpoints such as <code>/accounts</code>, <code>/zones</code>, and <code>/organizations</code> are now included.</p>
</li>
<li>
<p><strong>Granular filtering</strong>: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.</p>
</li>
<li>
<p><strong>Enhanced context and traceability</strong>: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.</p>
</li>
<li>
<p><strong>Comprehensive activity capture</strong>: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.</p>
</li>
</ul>
<p><strong>Known Limitations in Beta</strong></p>
<ul>
<li>Error handling for the API is not implemented.</li>
<li>There may be gaps or missing entries in the available audit logs.</li>
<li>UI is unavailable in this Beta release.</li>
<li>System-level logs and User-Activity logs are not included.</li>
</ul>
<p>Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: <a href="https://blog.cloudflare.com/introducing-automatic-audit-logs/">Introducing Automatic Audit Logs</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-26">Mar 26, 2025</time><div>
<h2 id="post-2025-03-26-account-home-updates"><a href="/changelog/post/2025-03-26-account-home-updates/">Updates to Account Home - Quick actions, traffic insights, Workers projects, and more</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/fundamentals/2025-03-26-account-home-updates.png" alt="Updated Account Home" /></p>
<p>Recently, Account Home has been updated to streamline your workflows:</p>
<ul>
<li>
<p><strong>Recent Workers projects</strong>: You'll now find your projects readily accessible from a new <code>Developer Platform</code> tab on Account Home. See recently-modified projects and explore what you can work our developer-focused products.</p>
</li>
<li>
<p><strong>Traffic and security insights</strong>: Get a snapshot of domain performance at a glance with key metrics and trends.</p>
</li>
<li>
<p><strong>Quick actions</strong>: You can now perform common actions for your account, domains, and even Workers in just 1-2 clicks from the 3-dot menu.</p>
</li>
<li>
<p><strong>Keep starred domains front and center</strong>: Now, when you filter for starred domains on Account Home, we'll save your preference so you'll continue to only see starred domains by default.</p>
</li>
</ul>
<p>We can't wait for you to take the new Account Home for a spin.</p>
<p>For more info:</p>
<ul>
<li><a href="https://dash.cloudflare.com/">Try the updated Account Home</a></li>
<li><a href="/fundamentals/manage-domains/star-zones/">Documentation on starred domains</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-26">Mar 26, 2025</time><div>
<h2 id="post-2025-03-25-higher-cpu-limits"><a href="/changelog/post/2025-03-25-higher-cpu-limits/">Run Workers for up to 5 minutes of CPU-time</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now run a Worker for up to 5 minutes of CPU time for each request.</p>
<p>Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This
meant that some compute-intensive tasks were impossible to do with a Worker. For instance,
you might want to take the cryptographic hash of a large file from R2. If
this computation ran for over 30 seconds, the Worker request would have timed out.</p>
<p>By default, Workers are still limited to 30 seconds of CPU time. This protects developers
from incurring accidental cost due to buggy code.</p>
<p>By changing the <code>cpu_ms</code> value in your Wrangler configuration, you can opt in to
any value up to 300,000 (5 minutes).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17770.md")</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17769.md")</aside>
<p>For more information on the updates limits, see the documentation on <a href="/workers/wrangler/configuration/#limits">Wrangler configuration for <code>cpu_ms</code></a>
and on <a href="/workers/platform/limits/#cpu-time">Workers CPU time limits</a>.</p>
<p>For building long-running tasks on Cloudflare, we also recommend checking out <a href="/workflows/">Workflows</a> and <a href="/queues/">Queues</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-25">Mar 25, 2025</time><div>
<h2 id="post-2025-03-25-gzip-source-maps"><a href="/changelog/post/2025-03-25-gzip-source-maps/">Source Maps are Generally Available</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB.
Previously, the maximum size limit was 15 MB uncompressed.</p>
<p>Source maps help map between the original source code and the transformed/minified code that gets deployed
to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions
onto the original source code making it easier to debug.</p>
<p><img src="/assets/upstream/images/workers-observability/without-source-map.png" alt="Stack Trace without Source Map remapping" /></p>
<p>With <strong>no source maps uploaded</strong>: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references <code>js</code> instead of <code>ts</code>.</p>
<p><img src="/assets/upstream/images/workers-observability/with-source-map.png" alt="Stack Trace with Source Map remapping" /></p>
<p>With <strong>source maps uploaded</strong>: all methods reference the correct files and line numbers.</p>
<p>Uploading source maps and stack trace remapping happens out of band from the Worker execution,
so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack
traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.</p>
<p>To enable source maps, add the following to your
<a href="/pages/functions/source-maps/">Pages Function's</a> or <a href="/workers/observability/source-maps/">Worker's</a> wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17768.md")</div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-22">Mar 22, 2025</time><div>
<h2 id="post-2025-03-22-emergency-waf-release"><a href="/changelog/post/2025-03-22-emergency-waf-release/">WAF Release - 2025-03-22 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="34583778093748cc83ff7b38f472013e">f472013e</code>
</td>
<td>100739</td>
<td>Next.js - Auth Bypass - CVE:CVE-2025-29927</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-22">Mar 22, 2025</time><div>
<h2 id="post-2025-03-22-next-js-vulnerability-waf"><a href="/changelog/post/2025-03-22-next-js-vulnerability-waf/">New Managed WAF rule for Next.js CVE-2025-29927.</a></h2>
<div class="changelog-badges"><span>workers</span><span>pages</span><span>waf</span></div><div class="changelog-body"><p><strong>Update: Mon Mar 24th, 11PM UTC</strong>: Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions <code>15.2.4</code>, <code>14.2.26</code>, <code>13.5.10</code> or <code>12.3.6</code>. <strong>If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation</strong>.</p>
<p><strong>Update: Mon Mar 24th, 8PM UTC</strong>: Next.js has now <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">backported the patch for this vulnerability</a> to cover Next.js v12 and v13. Users on those versions will need to patch to <code>13.5.9</code> and <code>12.3.5</code> (respectively) to mitigate the vulnerability.</p>
<p><strong>Update: Sat Mar 22nd, 4PM UTC</strong>: We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.</p>
<p><strong>We strongly recommend updating your version of Next.js (if eligible)</strong> to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-enable-the-managed-rule-strongly-recommended">Enable the Managed Rule (strongly recommended)</h4>
<p>This rule is opt-in only for sites on the Pro plan or above in the <a href="/waf/managed-rules/">WAF managed ruleset</a>.</p>
<p>To enable the rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Click the three dots next to <strong>Cloudflare Managed Ruleset</strong> and choose <strong>Edit</strong></li>
<li>Scroll down and choose <strong>Browse Rules</strong></li>
<li>Search for <strong>CVE-2025-29927</strong> (ruleId: <code>34583778093748cc83ff7b38f472013e</code>)</li>
<li>Change the <strong>Status</strong> to <strong>Enabled</strong> and the <strong>Action</strong> to <strong>Block</strong>. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.</li>
<li>Click <strong>Next</strong></li>
<li>Scroll down and choose <strong>Save</strong></li>
</ol>
<p>This will enable the WAF rule and block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-create-a-waf-rule-manual">Create a WAF rule (manual)</h4>
<p>For users on the Free plan, or who want to define a more specific rule, you can create a <a href="/waf/custom-rules/create-dashboard/">Custom WAF rule</a> to block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<p>To create a custom rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Give the rule a name - e.g. <code>next-js-CVE-2025-29927</code></li>
<li>Set the matching parameters for the rule match any request where the <code>x-middleware-subrequest</code> header <code>exists</code> per the rule expression below.</li>
</ol>
<pre tabindex="0"><code class="language-sh">(len(http.request.headers[&quot;x-middleware-subrequest&quot;]) &gt; 0)&#10;</code></pre>
<ol start="4">
<li>Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).</li>
<li><strong>Deploy</strong> the rule.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/workers/waf-rule-cve-2025-29927.png" alt="Next.js CVE-2025-29927 WAF rule" /></p>
<h4 id="2025-03-22-next-js-vulnerability-waf-next-js-cve-2025-29927">Next.js CVE-2025-29927</h4>
<p>We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">Next.js authentication bypass vulnerability</a> (<code>CVE-2025-29927</code>) published on March 21st, 2025.</p>
<p><strong>Note</strong>: This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.</p>
<ul>
<li>This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.</li>
<li>This rule has been made available (but not enabled by default) to all sites as part of our <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">WAF Managed Ruleset</a> and blocks requests that attempt to bypass authentication in Next.js applications.</li>
<li>The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js <code>14.2.26</code> and <code>15.2.4</code>. Earlier, interim releases did not fully patch this vulnerability.</li>
<li><strong>Users on older versions of Next.js (<code>11.1.4</code> to <code>13.5.6</code>) did not originally have a patch available</strong>, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions <code>12.3.6</code> and <code>13.5.10</code> as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.</li>
</ul>
<p>The managed WAF rule mitigates this by blocking <em>external</em> user requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-22">Mar 22, 2025</time><div>
<h2 id="post-2025-03-22-smart-placement-stablization"><a href="/changelog/post/2025-03-22-smart-placement-stablization/">Smart Placement is smarter about running Workers and Pages Functions in the best locations</a></h2>
<div class="changelog-badges"><span>workers</span><span>pages</span></div><div class="changelog-body"><p><a href="/workers/configuration/placement/">Smart Placement</a> is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.</p>
<p>Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.</p>
<p>Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-21">Mar 21, 2025</time><div>
<h2 id="post-2025-03-20-websockets"><a href="/changelog/post/2025-03-20-websockets/">AI Gateway launches Realtime WebSockets API</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>We are excited to announce that <a href="/ai-gateway/">AI Gateway</a> now supports real-time AI interactions with the new <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a>.</p>
<p>This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.</p>
<p>The Realtime WebSockets API works with the <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI Realtime API</a>, <a href="https://ai.google.dev/gemini-api/docs/multimodal-live">Google Gemini Live API</a>, and supports real-time text and speech interactions with models from <a href="https://docs.cartesia.ai/api-reference/tts/tts">Cartesia</a>, and <a href="https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket">ElevenLabs</a>.</p>
<p>Here's how you can connect AI Gateway to <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI's Realtime API</a> using WebSockets:</p>
<pre tabindex="0"><code class="language-javascript">import WebSocket from &quot;ws&quot;;&#10;&#10;const url =&#10;	&quot;wss://gateway.ai.cloudflare.com/v1/&lt;account_id&gt;/&lt;gateway&gt;/openai?model=gpt-4o-realtime-preview-2024-12-17&quot;;&#10;const ws = new WebSocket(url, {&#10;	headers: {&#10;		&quot;cf-aig-authorization&quot;: process.env.CLOUDFLARE_API_KEY,&#10;		Authorization: &quot;Bearer &quot; + process.env.OPENAI_API_KEY,&#10;		&quot;OpenAI-Beta&quot;: &quot;realtime=v1&quot;,&#10;	},&#10;});&#10;&#10;ws.on(&quot;open&quot;, () =&gt; console.log(&quot;Connected to server.&quot;));&#10;ws.on(&quot;message&quot;, (message) =&gt; console.log(JSON.parse(message.toString())));&#10;&#10;ws.send(&#10;	JSON.stringify({&#10;		type: &quot;response.create&quot;,&#10;		response: { modalities: [&quot;text&quot;], instructions: &quot;Tell me a joke&quot; },&#10;	}),&#10;);&#10;</code></pre>
<p>Get started by checking out the <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-21">Mar 21, 2025</time><div>
<h2 id="post-2025-03-21-pdns-user-locations-role"><a href="/changelog/post/2025-03-21-pdns-user-locations-role/">Secure DNS Locations Management User Role</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>We're excited to introduce the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations"><strong>Cloudflare Zero Trust Secure DNS Locations Write role</strong></a>, designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.</p>
<p>Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.</p>
<p><strong>Secure DNS Location Requirements:</strong></p>
<ul>
<li>
<p>Mandate usage of <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">Bring your own DNS resolver IP addresses</a> if available on the account.</p>
</li>
<li>
<p>Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.</p>
</li>
</ul>
<p>You can assign the new role via Cloudflare Dashboard (<code>Manage Accounts &gt; Members</code>) or via API. For more information, refer to the <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations">Secure DNS Locations documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-21">Mar 21, 2025</time><div>
<h2 id="post-2025-03-21-resource-force-replacement-bug"><a href="/changelog/post/2025-03-21-resource-force-replacement-bug/">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-21">Mar 21, 2025</time><div>
<h2 id="post-2025-03-21-sensitive-values-redacted"><a href="/changelog/post/2025-03-21-sensitive-values-redacted/">Cloudflare Terraform Provider now properly redacts sensitive values</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-20">Mar 20, 2025</time><div>
<h2 id="post-2025-03-20-markdown-conversion"><a href="/changelog/post/2025-03-20-markdown-conversion/">Markdown conversion in Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the <code>toMarkdown</code> utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.</p>
<p>You can call this new tool using a binding by calling <code>env.AI.toMarkdown()</code> or the using the <a href="/api/resources/ai/">REST API</a> endpoint.</p>
<p>In this example, we fetch a PDF document and an image from R2 and feed them both to <code>env.AI.toMarkdown()</code>. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.</p>
<pre tabindex="0"><code class="language-typescript">import { Env } from &quot;./env&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf&#10;		const pdf = await env.R2.get(&quot;somatosensory.pdf&quot;);&#10;&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg&#10;		const cat = await env.R2.get(&quot;cat.jpeg&quot;);&#10;&#10;		return Response.json(&#10;			await env.AI.toMarkdown([&#10;				{&#10;					name: &quot;somatosensory.pdf&quot;,&#10;					blob: new Blob([await pdf.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;				{&#10;					name: &quot;cat.jpeg&quot;,&#10;					blob: new Blob([await cat.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;			]),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>This is the result:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;name&quot;: &quot;somatosensory.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase...&quot;&#10;	},&#10;	{&#10;		&quot;name&quot;: &quot;cat.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat&#x27;s eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat&#x27;s facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people.&quot;&#10;	}&#10;]&#10;</code></pre>
<p>See <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> for more information on supported formats, REST API and pricing.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-19">Mar 19, 2025</time><div>
<h2 id="post-2025-03-19-emergency-waf-release"><a href="/changelog/post/2025-03-19-emergency-waf-release/">WAF Release - 2025-03-19 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="470b477e27244fddb479c4c7a2cafae7">a2cafae7</code>
</td>
<td>100736</td>
<td>Generic HTTP Request Smuggling</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-18">Mar 18, 2025</time><div>
<h2 id="post-2025-03-18-npm-i-agents"><a href="/changelog/post/2025-03-18-npm-i-agents/">npm i agents</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><img src="/assets/upstream/images/agents/npm-i-agents.apng" alt="npm i agents" width="1000" height="541" />
<h4 id="2025-03-18-npm-i-agents-agents-sdk-agents"><code>agents-sdk</code> -&gt; <code>agents</code> <span class="nb-badge">Updated</span></h4>
<p>📝 <strong>We've renamed the Agents package to <code>agents</code></strong>!</p>
<p>If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to <code>agents-sdk</code> with <code>agents</code>:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install the new package&#10;npm i agents&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Remove the old (deprecated) package&#10;npm uninstall agents-sdk&#10;&#10;&#35; Find instances of the old package name in your codebase&#10;grep -r &#x27;agents-sdk&#x27; .&#10;&#35; Replace instances of the old package name with the new one&#10;&#35; (or use find-replace in your editor)&#10;sed -i &#x27;s/agents-sdk/agents/g&#x27; $(grep -rl &#x27;agents-sdk&#x27; .)&#10;</code></pre>
<p>All future updates will be pushed to the new <code>agents</code> package, and the older package has been marked as deprecated.</p>
<h4 id="2025-03-18-npm-i-agents-agents-sdk-updates">Agents SDK updates <span class="nb-badge">New</span></h4>
<p>We've added a number of big new features to the Agents SDK over the past few weeks, including:</p>
<ul>
<li>You can now set <code>cors: true</code> when using <code>routeAgentRequest</code> to return permissive default CORS headers to Agent responses.</li>
<li>The regular client now syncs state on the agent (just like the React version).</li>
<li><code>useAgentChat</code> bug fixes for passing headers/credentials, including properly clearing cache on unmount.</li>
<li>Experimental <code>/schedule</code> module with a prompt/schema for adding scheduling to your app (with evals!).</li>
<li>Changed the internal <code>zod</code> schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.</li>
</ul>
<p>We've also fixed a number of bugs with state synchronization and the React hooks.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17621.md")</div>
<h4 id="2025-03-18-npm-i-agents-call-agent-methods-from-your-client-code">Call Agent methods from your client code <span class="nb-badge">New</span></h4>
<p>We've added a new <a href="/agents/runtime/agents-api/"><code>@unstable_callable()</code></a> decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17622.md")</div>
<h4 id="2025-03-18-npm-i-agents-agents-starter">agents-starter <span class="nb-badge">Updated</span></h4>
<p>We've fixed a number of small bugs in the <a href="https://github.com/cloudflare/agents-starter"><code>agents-starter</code></a> project — a real-time, chat-based example application with tool-calling &amp; human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest <a href="/changelog/2025-03-13-wrangler-v4/">wrangler v4</a> release.</p>
<p>If you're new to Agents, you can install and run the <code>agents-starter</code> project in two commands:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install it&#10;$ npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; Run it&#10;$ npm run start&#10;</code></pre>
<p>You can use the starter as a template for your own Agents projects: open up <code>src/server.ts</code> and <code>src/client.tsx</code> to see how the Agents SDK is used.</p>
<h4 id="2025-03-18-npm-i-agents-more-documentation">More documentation <span class="nb-badge">Updated</span></h4>
<p>We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:</p>
<ul>
<li>Expanded <a href="/agents/runtime/">API reference documentation</a>, covering the methods and properties exposed by the Agents SDK, as well as more usage examples.</li>
<li>More <a href="/agents/runtime/agents-api/#client-api">Client API</a> documentation that documents <code>useAgent</code>, <code>useAgentChat</code> and the new <code>@unstable_callable</code> RPC decorator exposed by the SDK.</li>
<li>New documentation on how to <a href="/agents/runtime/communication/routing/">route requests to agents</a> and (optionally) authenticate clients before they connect to your Agents.</li>
</ul>
<p>Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the <code>agents</code> package.</p>
<p>If you're still wondering what Agents are, <a href="https://blog.cloudflare.com/build-ai-agents-on-cloudflare/">read our blog on building AI Agents on Cloudflare</a> and/or visit the <a href="/agents/">Agents documentation</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-18">Mar 18, 2025</time><div>
<h2 id="post-2025-03-18-api-posture-management"><a href="/changelog/post/2025-03-18-api-posture-management/">New API Posture Management for API Shield</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Now, API Shield <strong>automatically</strong> labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.</p>
<p>View these risks in <a href="/api-shield/management-and-monitoring/">Endpoint Management</a> by label:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/endpoint-management-label.png" alt="A list of endpoint management labels" /></p>
<p>...or in <a href="/security/security-insights/">Security Center Insights</a>:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/posture-management-insight.png" alt="An example security center insight" /></p>
<p>API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:</p>
<ul>
<li><strong>cf-risk-sensitive</strong>: applied if the customer is subscribed to the <a href="/waf/managed-rules/reference/sensitive-data-detection/">sensitive data detection ruleset</a> and the WAF detects sensitive data returned on an endpoint in the last seven days.</li>
<li><strong>cf-risk-missing-auth</strong>: applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.</li>
<li><strong>cf-risk-mixed-auth</strong>: applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.</li>
<li><strong>cf-risk-missing-schema</strong>: added when a learned schema is available for an endpoint that has no active schema.</li>
<li><strong>cf-risk-error-anomaly</strong>: added when an endpoint experiences a recent increase in response errors over the last 24 hours.</li>
<li><strong>cf-risk-latency-anomaly</strong>: added when an endpoint experiences a recent increase in response latency over the last 24 hours.</li>
<li><strong>cf-risk-size-anomaly</strong>: added when an endpoint experiences a spike in response body size over the last 24 hours.</li>
</ul>
<p>In addition, API Shield has two new 'beta' scans for <strong>Broken Object Level Authorization (BOLA) attacks</strong>. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:</p>
<ul>
<li><strong>cf-risk-bola-enumeration</strong>: added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.</li>
<li><strong>cf-risk-bola-pollution</strong>: added when an endpoint experiences successful responses where parameters are found in multiple places in the request.</li>
</ul>
<p>We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/cloudflare-security-posture-management/">blog post</a> for more information about Cloudflare's expanded posture management capabilities.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-18">Mar 18, 2025</time><div>
<h2 id="post-2025-03-18-radar-leaked-credentials-insights"><a href="/changelog/post/2025-03-18-radar-leaked-credentials-insights/">Leaked Credentials Insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its security insights, providing visibility into aggregate trends in authentication requests,
including the detection of leaked credentials through <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> scans.</p>
<p>We have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/summary/"><code>/leaked_credential_checks/summary/{dimension}</code></a>: Retrieves summaries of HTTP authentication requests distribution across two different dimensions.</li>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/"><code>/leaked_credential_checks/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.</li>
</ul>
<p>The following dimensions are available, displaying the distribution of HTTP authentication requests based on:</p>
<ul>
<li><code>compromised</code>: Credential status (clean vs. compromised).</li>
<li><code>bot_class</code>: <a href="/radar/concepts/bot-classes">Bot class</a> (human vs. bot).</li>
</ul>
<p>Dive deeper into leaked credential detection in this <a href="https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/">blog post</a> and learn more about the expanded Radar security insights in our <a href="https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-warp-ga-android"><a href="/changelog/post/2025-03-17-warp-ga-android/">Cloudflare One Agent for Android (version 2.4)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-warp-ga-ios"><a href="/changelog/post/2025-03-17-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.10)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Bug fixes and performance improvements.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-waf-release"><a href="/changelog/post/2025-03-17-waf-release/">WAF Release - 2025-03-17</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="28b2a12993a04e62a98abcd9e59ec18a">e59ec18a</code>
</td>
<td>100725</td>
<td>
				Fortinet FortiManager - Remote Code Execution - CVE:CVE-2023-42791,
				CVE:CVE-2024-23666
</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f253d755910e4998bd90365d1dbf58df">1dbf58df</code>
</td>
<td>100726</td>
<td>Ivanti - Remote Code Execution - CVE:CVE-2024-8190</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="19ae0094a8d845a1bb1997af0ad61fa7">0ad61fa7</code>
</td>
<td>100727</td>
<td>Cisco IOS XE - Remote Code Execution - CVE:CVE-2023-20198</td>
<td>Log</td>
<td>Disabled</td>
<td>Fixed action value in changelog; no rule changes.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="83a677f082264693ad64a2827ee56b66">7ee56b66</code>
</td>
<td>100728</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2024-46938</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="166b7ce85ce443538f021228a6752a38">a6752a38</code>
</td>
<td>100729</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2023-33160</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35fe23e7bd324d00816c82d098d47b69">98d47b69</code>
</td>
<td>100730</td>
<td>
				Pentaho - Template Injection - CVE:CVE-2022-43769, CVE:CVE-2022-43939
</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2ce80fe815254f25b3c8f47569fe1e0d">69fe1e0d</code>
</td>
<td>100700</td>
<td>Apache SSRF vulnerability CVE-2021-40438</td>
<td>N/A</td>
<td>Block</td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/44/">Previous</a><span>Page 45 of 50</span><a class="pagination-next" rel="next" href="/changelog/46/">Next</a></nav>
</div>
