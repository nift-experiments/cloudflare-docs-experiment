<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-11-03">Nov 3, 2025</time><div>
<h2 id="post-2025-11-03-wrangler-output-file"><a href="/changelog/post/2025-11-03-wrangler-output-file/">Capture Wrangler command output in structured format</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now capture Wrangler command output in a structured <a href="https://github.com/ndjson/ndjson-spec">ND-JSON</a> format by setting the <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_PATH</code></a> or <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_DIRECTORY</code></a> environment variables. This feature is particularly useful for CI/CD pipelines and automation tools that need programmatic access to deployment information such as worker names, version IDs, deployment URLs, and error details. Commands that support this feature include <a href="/workers/wrangler/commands/#deploy"><code>wrangler deploy</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions upload</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions deploy</code></a>, and <a href="/workers/wrangler/commands/#deploy-1"><code>wrangler pages deploy</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-31">Oct 31, 2025</time><div>
<h2 id="post-2025-10-31-brand-protection-logo-dashboard-report-abuse"><a href="/changelog/post/2025-10-31-brand-protection-logo-dashboard-report-abuse/">Report logo misuse to Cloudflare directly from the Brand Protection dashboard</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>The Brand Protection logo query dashboard now allows you to use the <strong>Report to Cloudflare</strong> button to submit an Abuse report directly from the Brand Protection logo queries dashboard. While you could previously report new domains that were impersonating your brand before, now you can do the same for websites found to be using your logo without your permission. The abuse reports will be prefilled and you will only need to validate a few fields before you can click the submit button, after which our team process your request.</p>
<p>Ready to start? Check out the <a href="/security-center/brand-protection/">Brand Protection docs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-31">Oct 31, 2025</time><div>
<h2 id="post-2025-10-31-increased-websocket-message-size-limit"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span><span>browser-run</span></div><div class="changelog-body"><p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-31">Oct 31, 2025</time><div>
<h2 id="post-2025-10-28-raising-limits"><a href="/changelog/post/2025-10-28-raising-limits/">Increased Workflows instance and concurrency limits</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>We've raised the <a href="/workflows/">Cloudflare Workflows</a> account-level limits for all accounts on the <a href="/workers/platform/pricing/">Workers paid plan</a>:</p>
<ul>
<li><strong>Instance creation rate</strong> increased from 100 workflow instances per 10 seconds to 100 instances per second</li>
<li><strong>Concurrency limit</strong> increased from 4,500 to 10,000 workflow instances per account</li>
</ul>
<p>These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to <a href="/workflows/get-started/guide/">the getting started guide</a>.</p>
<p>If your application requires a higher limit, fill out the <a href="/workers/platform/limits/">Limit Increase Request Form</a> or contact your account team. Please refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-30">Oct 30, 2025</time><div>
<h2 id="post-2025-10-30-email-2FA"><a href="/changelog/post/2025-10-30-email-2FA/">Introducing email two-factor authentication</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Two-factor authentication (2FA) is one of the best ways to protect your account from the risk of account takeover. Cloudflare has offered phishing resistant 2FA options including hardware based keys (for example, a Yubikey) and app based TOTP (time-based one-time password) options which use apps like Google or Microsoft's Authenticator app. Unfortunately, while these solutions are very secure, they can be lost if you misplace the hardware based key, or lose the phone which includes that app. The result is that users sometimes get locked out of their accounts and need to contact support.</p>
<p>Today, we are announcing the addition of email as a 2FA factor for all Cloudflare accounts. Email 2FA is in wide use across the industry as a least common denominator for 2FA because it is low friction, loss resistant, and still improves security over username/password login only. We also know that most commercial email providers already require 2FA, so your email address is usually well protected already.</p>
<p>You can now enable email 2FA on the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Profile</strong> at the top right corner.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
</ol>
<h4 id="2025-10-30-email-2FA-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Review the following best practices and make sure you are doing your part to secure your account:</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked.</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company.</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account.</li>
</ul>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-30">Oct 30, 2025</time><div>
<h2 id="post-2025-10-30-member-management-improvements"><a href="/changelog/post/2025-10-30-member-management-improvements/">Revamped Member Management UI</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>As Cloudflare's platform has grown, so has the need for precise, role-based access control. We’ve redesigned the Member Management experience in the Dashboard to help administrators more easily discover, assign, and refine permissions for specific principals.</p>
<h4 id="2025-10-30-member-management-improvements-what-s-new">What's New</h4>
<p><strong>Refreshed member invite flow</strong></p>
<p>We overhauled the Invite Members UI to simplify inviting users and assigning permissions.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-invite-experience.gif" alt="Updated Invite Flow UX" /></p>
<p><strong>Refreshed Members Overview Page</strong></p>
<p>We've updated the Members Overview Page to clearly display:</p>
<ul>
<li>Member 2FA status</li>
<li>Which members hold Super Admin privileges</li>
<li>API access settings per member</li>
<li>Member onboarding state (accepted vs pending invite)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-member-management-screen.png" alt="Updated Member Management Overview" /></p>
<p><strong>New Member Permission Policies Details View</strong></p>
<p>We've created a new member details screen that shows all permission policies associated with a member; including policies inherited from group associations to make it easier for members to understand the effective permissions they have.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Permission Policies Details Screen" /></p>
<p><strong>Improved Member Permission Workflow</strong></p>
<p>We redesigned the permission management experience to make it faster and easier for administrators to review roles and grant access.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Member Permission Management UX" /></p>
<p><strong>Account-scoped Policies Restrictions Relaxed</strong></p>
<p>Previously, customers could only associate a single account-scoped policy with a member. We've relaxed this restriction, and now Administrators can now assign multiple account-scoped policies to the same member; bringing policy assignment behavior in-line with user-groups and providing greater flexibility in managing member permissions.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-30">Oct 30, 2025</time><div>
<h2 id="post-2025-10-30-tcp-rtt-and-tcp-fields"><a href="/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/">New TCP-based fields available in Rulesets</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><h4 id="2025-10-30-tcp-rtt-and-tcp-fields-build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-30">Oct 30, 2025</time><div>
<h2 id="post-2025-10-30-emergency-waf-release"><a href="/changelog/post/2025-10-30-emergency-waf-release/">WAF Release - 2025-10-30 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Oracle E-Business Suite, tracked as CVE-2025-61884.</p>
<p><strong>Key Findings</strong></p>
<p>The flaw is easily exploitable and allows an unauthenticated attacker with network access to compromise Oracle Configurator, which can grant access to sensitive resources and configuration data. The affected versions include 12.2.3 through 12.2.14.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-61884 may result in unauthorized access to critical business data or full exposure of information accessible through Oracle Configurator. Administrators are strongly advised to apply vendor's patches and recommended mitigations to reduce this exposure.</p>
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
        <code class="nb-rule-id" title="2749f13f8cb34a3dbd49c8c48827402f">8827402f</code>
</td>
<td>N/A</td>
<td>Oracle E-Business Suite - SSRF - CVE:CVE-2025-61884</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-30">Oct 30, 2025</time><div>
<h2 id="post-2025-10-30-builds-preview"><a href="/changelog/post/2025-10-30-builds-preview/">Access Workers preview URLs from the Build details page</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> directly from the build details page, making it easier to test your changes when reviewing builds in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/builds-preview-button.png" alt="preview button" /></p>
<p><strong>What's new</strong></p>
<ul>
<li>A <strong>Preview</strong> button now appears in the top-right corner of the build details page for successful builds</li>
<li>Click it to instantly open the latest preview URL</li>
<li>Matches the same experience you're familiar with from Pages</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-28">Oct 28, 2025</time><div>
<h2 id="post-2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols"><a href="/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/">Access private hostname applications support all ports/protocols</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Cloudflare Access for private hostname applications</a> can now secure traffic on all ports and protocols.</p>
<p>Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port <code>443</code> and support Server Name Indicator (SNI).</p>
<p>This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.</p>
<p><img src="/assets/upstream/images/changelog/access/internal_private_app_any_port.png" alt="Example private application on non-443 port" /></p>
<p>For example, you can now create a self-hosted application in Access for <code>ssh.testapp.local</code> running on port <code>22</code>. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.</p>
<p>This feature is generally available across all plans.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-28">Oct 28, 2025</time><div>
<h2 id="post-2025-10-27-ai-search-reranking-system-prompt"><a href="/changelog/post/2025-10-27-ai-search-reranking-system-prompt/">Reranking and API-based system prompt configuration in AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.</p>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-rerank-for-more-relevant-results">Rerank for more relevant results</h4>
<p>You can now enable <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<p>You can enable and configure reranking in the dashboard or directly in your API requests:</p>
<pre><code class="language-javascript">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-set-system-prompts-in-api">Set system prompts in API</h4>
<p>Previously, <a href="/ai-search/configuration/retrieval/system-prompt/">system prompts</a> could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:</p>
<pre><code class="language-javascript">// Dynamically set query and system prompt in AI Search&#10;async function getAnswer(query, tone) {&#10;	const systemPrompt = `You are a ${tone} assistant.`;&#10;&#10;	const response = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;		query: query,&#10;		system_prompt: systemPrompt,&#10;	});&#10;&#10;	return response;&#10;}&#10;&#10;// Example usage&#10;const query = &quot;What is Cloudflare?&quot;;&#10;const tone = &quot;friendly&quot;;&#10;&#10;const answer = await getAnswer(query, tone);&#10;console.log(answer);&#10;</code></pre>
<p>Learn more about <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> and <a href="/ai-search/configuration/retrieval/system-prompt/">System Prompt</a> in AI Search.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-28">Oct 28, 2025</time><div>
<h2 id="post-2025-10-28-casb-roles"><a href="/changelog/post/2025-10-28-casb-roles/">CASB introduces new granular roles</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:</p>
<ul>
<li><strong>Cloudflare CASB Read:</strong> Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.</li>
<li><strong>Cloudflare CASB:</strong> Provides full administrative access to configure and manage all aspects of the CASB product.</li>
</ul>
<p>These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the <strong>Super Administrator</strong> or <strong>Administrator</strong> roles.</p>
<p>To enable <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Data Loss Prevention (DLP)</a>, scans in CASB, account members will need the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Members</strong>.</p>
<p>To learn more about managing roles and permissions, refer to the <a href="/fundamentals/manage-members/roles/">Manage account members and roles documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-28">Oct 28, 2025</time><div>
<h2 id="post-Gateway-application-categories-added"><a href="/changelog/post/Gateway-application-categories-added/">New Application Categories added for HTTP Traffic Management</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>To give you precision and flexibility while creating policies to block unwanted traffic, we are introducing new, more granular application categories in the Gateway product.</p>
<p>We have added the following categories to provide more precise organization and allow for finer-grained policy creation, designed around how users interact with different types of applications:</p>
<ul>
<li>Business</li>
<li>Education</li>
<li>Entertainment &amp; Events</li>
<li>Food &amp; Drink</li>
<li>Health &amp; Fitness</li>
<li>Lifestyle</li>
<li>Navigation</li>
<li>Photography &amp; Graphic Design</li>
<li>Travel</li>
</ul>
<p>The new categories are live now, but we are providing a transition period for existing applications to be fully remapped to these new categories.</p>
<p>The full remapping will be completed by January 30, 2026.</p>
<p>We encourage you to use this time to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify and adjust any existing HTTP policies that reference older categories to ensure a smooth transition.</li>
</ul>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-27">Oct 27, 2025</time><div>
<h2 id="post-2025-10-27-Sentinel-connector"><a href="/changelog/post/2025-10-27-Sentinel-connector/">Azure Sentinel Connector</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Logpush now supports integration with <a href="https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel">Microsoft Sentinel</a>.The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.</p>
<p>This upgrade significantly streamlines log ingestion, improves security, and provides greater control:</p>
<ul>
<li>Simplified Implementation: Easier for engineering teams to set up and maintain.</li>
<li>Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.</li>
<li>Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.</li>
<li>Data Lake Integration: Includes native integration with Data Lake.</li>
</ul>
<p>Find the new solution <a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">here</a> and refer to the <a href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules">Cloudflare's developer documentation</a>for more information on the connector, including setup steps, supported logs and Microsoft's resources.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-27">Oct 27, 2025</time><div>
<h2 id="post-2025-10-27-radar-tld-insights"><a href="/changelog/post/2025-10-27-radar-tld-insights/">TLD Insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.</p>
<p>The following dimensions were added to the Radar DNS API, specifically, to the <a href="/api/resources/radar/subresources/dns/methods/summary_v2/"><code>/dns/summary/{dimension}</code></a> and <a href="/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/"><code>/dns/timeseries_groups/{dimension}</code></a> endpoints:</p>
<ul>
<li><code>tld</code>: Top-level domain extracted from DNS queries; can also be used as a filter.</li>
<li><code>tld_dns_magnitude</code>: Top-level domain ranking by <a href="/radar/glossary#dns-magnitude">DNS magnitude</a>.</li>
</ul>
<p>And the following endpoints were added:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> - Lists all TLDs.</li>
<li><a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a> - Retrieves information about a specific TLD.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-ranking-by-dns-magnitude.png" alt="Screenshot of the TLD ranking by DNS magnitude" /></p>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/tlds">new Radar page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-27">Oct 27, 2025</time><div>
<h2 id="post-2025-10-27-RFI-Tokens-in-Dash"><a href="/changelog/post/2025-10-27-RFI-Tokens-in-Dash/">Cloudforce One RFI tokens are now visible in the dashboard</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>The Requests for Information (RFI) dashboard now shows users the number of tokens used by each submitted RFI to better understand usage of tokens and how they relate to each request submitted.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-24RFITokens.png" alt="Cloudforce One RFI tokens" /></p>
<p>What’s new:</p>
<ul>
<li>Users can now see the number of tokens used for a submitted request for information.</li>
<li>Users can see the remaining tokens allocated to their account for the quarter.</li>
<li>Users can only select the Routine priority for the <code>Strategic Threat Research</code> request type.</li>
</ul>
<p>Cloudforce One subscribers can try it now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/requests">Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-24">Oct 24, 2025</time><div>
<h2 id="post-2025-10-24-emergency-waf-release"><a href="/changelog/post/2025-10-24-emergency-waf-release/">WAF Release - 2025-10-24 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.</p>
<p><strong>Key Findings</strong></p>
<p>The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.</p>
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
        <code class="nb-rule-id" title="5eaeb5ea6e5a4bce867eb3ffbd72ba08">bd72ba08</code>
</td>
<td>N/A</td>
<td>Windows Server - Deserialization - CVE:CVE-2025-59287</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-24">Oct 24, 2025</time><div>
<h2 id="post-2025-10-24-automatic-resource-provisioning"><a href="/changelog/post/2025-10-24-automatic-resource-provisioning/">Automatic resource provisioning for KV, R2, and D1</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Previously, if you wanted to develop or deploy a worker with attached resources, you'd have to first manually create the desired resources. Now, if your Wrangler configuration file includes a KV namespace, D1 database, or R2 bucket that does not yet exist on your account, you can develop locally and deploy your application seamlessly, without having to run additional commands.</p>
<p>Automatic provisioning is launching as an open beta, and we'd love to hear your feedback to help us make improvements! It currently works for KV, R2, and D1 bindings. You can disable the feature using the <code>--no-x-provision</code> flag.</p>
<p>To use this feature, update to wrangler@4.45.0 and add bindings to your config file <em>without</em> resource IDs e.g.:</p>
<pre><code class="language-jsonc">{&#10;	&quot;kv_namespaces&quot;: [{ &quot;binding&quot;: &quot;MY_KV&quot; }],&#10;	&quot;d1_databases&quot;: [{ &quot;binding&quot;: &quot;MY_DB&quot; }],&#10;	&quot;r2_buckets&quot;: [{ &quot;binding&quot;: &quot;MY_R2&quot; }],&#10;}&#10;</code></pre>
<p><code>wrangler dev</code> will then automatically create these resources for you locally, and on your next run of <code>wrangler deploy</code>, Wrangler will call the Cloudflare API to create the requested resources and link them to your Worker.</p>
<p>Though resource IDs will be automatically written back to your Wrangler config file after resource creation, resources will stay linked across future deploys even without adding the resource IDs to the config file. This is especially useful for shared templates, which now no longer need to include account-specific resource IDs when adding a binding.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-24">Oct 24, 2025</time><div>
<h2 id="post-2025-10-24-tanstack-start"><a href="/changelog/post/2025-10-24-tanstack-start/">Build TanStack Start apps with the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports <a href="https://tanstack.com/start/">TanStack Start</a> apps.
Get started with new or existing projects.</p>
<h4 id="2025-10-24-tanstack-start-new-projects">New projects</h4>
<p>Create a new TanStack Start project that uses the Cloudflare Vite plugin via the <code>create-cloudflare</code> CLI:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2025-10-24-tanstack-start-existing-projects">Existing projects</h4>
<p>Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:</p>
<ol>
<li>Install <code>@cloudflare/vite-plugin</code> and <code>wrangler</code></li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Add the Cloudflare plugin to your Vite config</li>
</ol>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import viteReact from &quot;@vitejs/plugin-react&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;		tanstackStart(),&#10;		viteReact(),&#10;	],&#10;});&#10;</code></pre>
<ol start="3">
<li>Add your Worker config file</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17789.md")</div>
<ol start="4">
<li>Modify the scripts in your <code>package.json</code></li>
</ol>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite dev&quot;,&#10;		&quot;build&quot;: &quot;vite build &amp;&amp; tsc --noEmit&quot;,&#10;		&quot;start&quot;: &quot;node .output/server/index.mjs&quot;,&#10;		&quot;preview&quot;: &quot;vite preview&quot;,&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;,&#10;		&quot;cf-typegen&quot;: &quot;wrangler types&quot;&#10;	}&#10;}&#10;</code></pre>
<p>See the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start framework guide</a> for more info.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-23">Oct 23, 2025</time><div>
<h2 id="post-2025-10-23-emergency-waf-release"><a href="/changelog/post/2025-10-23-emergency-waf-release/">WAF Release - 2025-10-23 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update enhances detection logic to provide more resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<p>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</p>
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
        <code class="nb-rule-id" title="6e04fa2b9eb34fb088034d3fc6ef59a1">c6ef59a1</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-23">Oct 23, 2025</time><div>
<h2 id="post-2025-10-23-preview-url-default-behavior"><a href="/changelog/post/2025-10-23-preview-url-default-behavior/">Workers Preview URL default behavior now matches your workers.dev setting</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We have updated the default behavior for Cloudflare Workers <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>. <strong>Going forward, if a preview URL setting is not <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">explicitly configured</a> during deployment, its default behavior will automatically match the setting of your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>.</strong></p>
<p>This change is intended to provide a more intuitive and secure experience by aligning your preview URL's default state with your <code>workers.dev</code> configuration to prevent cases where a preview URL might remain public even after you disabled your <code>workers.dev</code> route.</p>
<p><strong>What this means for you:</strong></p>
<ul>
<li><strong>If neither setting is configured:</strong> both the workers.dev route and the preview URL will default to enabled</li>
<li><strong>If your workers.dev route is enabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to enabled</li>
<li><strong>If your workers.dev route is disabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to disabled</li>
</ul>
<p>You can override the default setting by explicitly enabling or disabling the preview URL in your Worker's configuration through the <a href="/api/resources/workers/subresources/scripts/subresources/subdomain/">API</a>, <a href="/workers/versions-and-deployments/preview-urls/#from-the-dashboard">Dashboard</a>, or <a href="/workers/versions-and-deployments/preview-urls/#from-the-wrangler-configuration-file">Wrangler</a>.</p>
<p><strong>Wrangler Version Behavior</strong></p>
<p>The default behavior depends on the version of Wrangler you are using. This new logic applies to the latest version. Here is a summary of the behavior across different versions:</p>
<ul>
<li><strong>Before v4.34.0:</strong> Preview URLs defaulted to enabled, regardless of the workers.dev setting.</li>
<li><strong>v4.34.0 up to (but not including) v4.44.0:</strong> Preview URLs defaulted to disabled, regardless of the workers.dev setting.</li>
<li><strong>v4.44.0 or later:</strong> Preview URLs now default to matching your workers.dev setting.</li>
</ul>
<p><strong>Why we’re making this change</strong></p>
<p>In July, <a href="/changelog/2025-07-23-workers-preview-urls/">we introduced preview URLs to Workers</a>, which let you preview code changes before deploying to production. This made disabling your Worker’s workers.dev URL an ambiguous action — the preview URL, served as a subdomain of <code>workers.dev</code> (ex: <code>preview-id-worker-name.account-name.workers.dev</code>) would still be live even if you had disabled your Worker’s <code>workers.dev</code> route. If you misinterpreted what it meant to disable your <code>workers.dev</code> route, you might unintentionally leave preview URLs enabled when you didn’t mean to, and expose them to the public Internet.</p>
<p>To address this, we made a <a href="/changelog/2025-09-17-update-preview-url-setting/">one-time update</a> to disable preview URLs on existing Workers that had their workers.dev route disabled and changed the default behavior to be disabled for all new deployments where a preview URL setting was not explicitly configured.</p>
<p>While this change helped secure many customers, it was disruptive for customers who keep their <code>workers.dev</code> route enabled and actively use the preview functionality, as it now required them to explicitly enable preview URLs on every redeployment.This new, more intuitive behavior ensures that your preview URL settings align with your <code>workers.dev</code> configuration by default, providing a more secure and predictable experience.</p>
<p><strong>Securing access to <code>workers.dev</code> and preview URL endpoints</strong></p>
<p>To further secure your <code>workers.dev</code> subdomain and preview URL, you can <a href="/changelog/2025-10-03-one-click-access-for-workers/">enable Cloudflare Access with a single click</a> in your Worker's settings to limit access to specific users or groups.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-23">Oct 23, 2025</time><div>
<h2 id="post-2025-10-23-new-markdown-conversion-endpoint"><a href="/changelog/post/2025-10-23-new-markdown-conversion-endpoint/">Workers AI Markdown Conversion: New endpoint to list supported formats</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Developers can now programmatically retrieve a list of all file formats supported by the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a> in Workers AI.</p>
<p>You can use the <a href="/workers-ai/configuration/bindings/"><code>env.AI</code></a> binding:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown().supported()&#10;</code></pre>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<p>Both return a list of file formats that users can convert into Markdown:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;extension&quot;: &quot;.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;	},&#10;	{&#10;		&quot;extension&quot;: &quot;.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;	},&#10;	...&#10;]&#10;</code></pre>
<p>Learn more about our <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-21">Oct 21, 2025</time><div>
<h2 id="post-2025-10-21-track-robots-txt"><a href="/changelog/post/2025-10-21-track-robots-txt/">New Robots.txt tab for tracking crawler compliance</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now includes a <strong>Robots.txt</strong> tab that provides insights into how AI crawlers interact with your <code>robots.txt</code> files.</p>
<h4 id="2025-10-21-track-robots-txt-what-s-new">What's new</h4>
<p>The Robots.txt tab allows you to:</p>
<ul>
<li>Monitor the health status of <code>robots.txt</code> files across all your hostnames, including HTTP status codes, and identify hostnames that need a <code>robots.txt</code> file.</li>
<li>Track the total number of requests to each <code>robots.txt</code> file, with breakdowns of successful versus unsuccessful requests.</li>
<li>Check whether your <code>robots.txt</code> files contain <a href="https://contentsignals.org/">Content Signals</a> directives for AI training, search, and AI input.</li>
<li>Identify crawlers that request paths explicitly disallowed by your <code>robots.txt</code> directives, including the crawler name, operator, violated path, specific directive, and violation count.</li>
<li>Filter <code>robots.txt</code> request data by crawler, operator, category, and custom time ranges.</li>
</ul>
<h4 id="2025-10-21-track-robots-txt-take-action">Take action</h4>
<p>When you identify non-compliant crawlers, you can:</p>
<ul>
<li>Block the crawler in the <a href="/ai-crawl-control/features/manage-ai-crawlers/">Crawlers tab</a></li>
<li>Create custom <a href="/waf/">WAF rules</a> for path-specific security</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide crawlers to appropriate areas of your site</li>
</ul>
<p>To get started, go to <strong>AI Crawl Control</strong> &gt; <strong>Robots.txt</strong> in the Cloudflare dashboard. Learn more in the <a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-20">Oct 20, 2025</time><div>
<h2 id="post-2025-10-20-schedule-dns-policies-from-the-ui"><a href="/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/">Schedule DNS policies from the UI</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Admins can now create <a href="/cloudflare-one/traffic-policies/dns-policies/timed-policies/">scheduled DNS policies</a> directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.</p>
<ul>
<li><strong>Preset Schedules</strong>: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.</li>
<li><strong>Custom Schedules</strong>: Define your own schedule with specific days and up to three non-overlapping time ranges per day.</li>
<li><strong>Timezone Control</strong>: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.</li>
<li><strong>Combined with Duration</strong>: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.</li>
</ul>
<p>You can see the flow in the demo GIF:</p>
<p><img src="/assets/upstream/images/gateway/gateway-dns-scheduled-policies-ui.gif" alt="Schedule DNS policies demo" /></p>
<p>This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-20">Oct 20, 2025</time><div>
<h2 id="post-2025-10-20-waf-release"><a href="/changelog/post/2025-10-20-waf-release/">WAF Release - 2025-10-20</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block  unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.</li>
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
				<code class="nb-rule-id" title="933fc13202cd4e8ba498c0f32b4101ab">2b4101ab</code>
</td>
<td>100598A</td>
<td>Remote Code Execution - Common Bash Bypass - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: <code class="nb-rule-id" title="f8238867ed3e4d3a9a7b731a50cec478">50cec478</code>)</td>
</tr>         
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="185b5df42d1e44e0aeb8f8b8a1118614">a1118614</code>
</td>
<td>100916A</td>
<td>Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="646bccf7e9dc46918a4150d6c22b51d3">c22b51d3</code>
</td>
<td>N/A</td>
<td>HTTP Truncated</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/31/">Previous</a><span>Page 32 of 50</span><a class="pagination-next" rel="next" href="/changelog/33/">Next</a></nav>
</div>
