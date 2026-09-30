<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-09-09">Sep 9, 2026</time><div>
<h2 id="post-2026-09-09-casb-zoom-integration"><a href="/changelog/post/2026-09-09-casb-zoom-integration/">New CASB integration for Zoom</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> now integrates with <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">Zoom</a>. The integration connects through Cloudflare's pre-built OAuth application — no manual app setup in Zoom is required. After an initial scan, CASB continuously scans your Zoom account to surface new findings as your environment changes.</p>
<p>Zoom is widely used for meetings, webinars, and collaboration. Misconfigurations in account settings, meeting security controls, and recording access can expose organizations to data leakage, unauthorized access, and compliance risk. Cloudflare CASB ingests Zoom account data via API to surface security findings across these areas.</p>
<h4 id="2026-09-09-casb-zoom-integration-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Account settings</strong> — Detect weak password policies, unlocked security controls, and two-factor authentication gaps across your Zoom account</li>
<li><strong>User accounts</strong> — Identify users not enforcing SSO, accounts with insecure host keys, unverified or inactive users, and unsafe overrides of account-level security settings</li>
<li><strong>Meetings</strong> — Surface meetings without passwords or waiting rooms, meetings using Personal Meeting IDs (PMIs), and meetings with external domain hosts</li>
<li><strong>Recordings</strong> — Detect publicly accessible cloud recordings, recordings without passcodes, and weak recording password configurations</li>
<li><strong>Content</strong> — Identify sensitive information in meeting and recording content via DLP Profile matching</li>
</ul>
<h4 id="2026-09-09-casb-zoom-integration-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">integration</a> is available to all Cloudflare Zero Trust customers today. New customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the Cloudflare One dashboard under <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-08">Sep 8, 2026</time><div>
<h2 id="post-2026-09-08-radar-search-events"><a href="/changelog/post/2026-09-08-radar-search-events/">Radar search now includes Internet events</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Cloudflare Radar</strong></a> search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.</p>
<p><img src="/assets/upstream/images/radar/radar-search-events.png" alt="Radar search results showing Internet outage events associated with locations and autonomous systems" /></p>
<p>Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through <a href="/browser-run/features/webmcp/">WebMCP</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-08">Sep 8, 2026</time><div>
<h2 id="post-2026-09-08-waf-release"><a href="/changelog/post/2026-09-08-waf-release/">WAF Release - 2026-09-08</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.</p>
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
				<code class="nb-rule-id" title="d5d9f863e50b416faf43934dc76ba662">c76ba662</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID:{" "}<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="771ac3761dcd485cb0e91ea0208457cf">208457cf</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID:{" "}<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>).</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-08">Sep 8, 2026</time><div>
<h2 id="post-2026-09-08-miniflare-v5"><a href="/changelog/post/2026-09-08-miniflare-v5/">Miniflare v5 prepares local development for the cf CLI</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Miniflare v5 prepares Cloudflare local development tooling for the upcoming <code>cf</code> CLI.</p>
<p>Miniflare powers local Workers development behind <code>wrangler dev</code>, the Cloudflare Vite plugin, and <code>@cloudflare/vitest-plugin</code>.
Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.</p>
<p>The most significant change is a new configuration shape which aligns Miniflare with <code>cloudflare.config.ts</code>, the programmatic Cloudflare configuration format now available for testing.</p>
<p>Other breaking changes include:</p>
<ul>
<li>Removed deprecated APIs and options, such as legacy alpha D1 bindings.</li>
<li>Removed now-unused, internal APIs like <code>wrappedBindings</code></li>
<li>Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.</li>
<li>Moved local-only /cdn-cgi routes under /cdn-cgi/local.</li>
<li>Replaced per-resource persistence options with shared persistence root options.</li>
</ul>
<p>For a more comprehensive list, refer to <a href="https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha">Miniflare's changelog</a></p>
<p>This work sets up a cleaner foundation for the next generation of local development tooling, including the new <code>cf</code> CLI.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-08">Sep 8, 2026</time><div>
<h2 id="post-2026-09-08-python-workers-314"><a href="/changelog/post/2026-09-08-python-workers-314/">Python 3.14 for Python Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python workers now use Python 3.14 by default.</p>
<p>This change applies to all new Python workers using compatibility date <code>2026-09-08</code> or later.</p>
<p>Internally, this change updates the Pyodide runtime to 314.0.6.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-04">Sep 4, 2026</time><div>
<h2 id="post-2026-09-04-enterprise-self-serve-upload-limits"><a href="/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/">Enterprise customers can self-serve CDN upload limits up to 5 GB</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>workers</span></div><div class="changelog-body"><p>Enterprise customers can now configure a zone's CDN <strong>Maximum Upload Size</strong> up to 5 GB directly from the <strong>Network</strong> page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.</p>
<p>The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.</p>
<p>Refer to <a href="/cache/concepts/default-cache-behavior/#upload-limits">Cache upload limits</a> and <a href="/workers/platform/limits/#request-and-response-limits">Workers request body size limits</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-04">Sep 4, 2026</time><div>
<h2 id="post-2026-09-04-r2-data-access-logs"><a href="/changelog/post/2026-09-04-r2-data-access-logs/">R2 Data Access Logs</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below <code>400</code>.</p>
<p>Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through <code>r2.dev</code> or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.</p>
<p>Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.</p>
<p>Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to <a href="/r2/buckets/data-access-logs/">R2 Data Access Logs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-04">Sep 4, 2026</time><div>
<h2 id="post-2026-09-04-increased-worker-size-limit"><a href="/changelog/post/2026-09-04-increased-worker-size-limit/">Deploy larger Workers — up to 64 MiB for both free and paid plans</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.</p>
<p>When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.</p>
<p>To check your Worker's bundle size before deploying:</p>
<pre><code class="language-sh">wrangler deploy --outdir bundled/ --dry-run&#10;</code></pre>
<pre><code class="language-sh">Total Upload: 259.61 KiB / gzip: 47.23 KiB&#10;</code></pre>
<p>The <code>Total Upload</code> value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The <code>gzip</code> value is shown for reference but is no longer a limit.</p>
<p>For more information, refer to the <a href="/workers/platform/limits/#worker-size">Worker size limits documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-origin-range-requests-rulesets-api"><a href="/changelog/post/2026-09-02-origin-range-requests-rulesets-api/">Configure Origin Range Requests with the Rulesets API</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.</p>
<p>Set <code>origin_range_requests.mode</code> to <code>on</code>, <code>off</code>, or <code>default</code> for any traffic matched by a Cache Rule.</p>
<p>To override Cloudflare's default Origin Range Requests behavior, set the mode to <code>off</code>. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:</p>
<pre><code class="language-json">{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;set_cache_settings&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;origin_range_requests&quot;: {&#10;      &quot;mode&quot;: &quot;off&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores <code>Range</code> and returns a complete <code>200 OK</code>, Cloudflare can use the response but must download the complete file. Origins should honor <code>Accept-Encoding: identity</code> and return consistent, unencoded partial responses.</p>
<p>For configuration details and mode behavior, refer to <a href="/cache/how-to/cache-rules/settings/#origin-range-requests">Origin Range Requests in Cache Rules</a>. For client responses and the complete origin contract, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-appliance-custom-application-traffic-steering"><a href="/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/">Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-appliance-dhcp-options-ui"><a href="/changelog/post/2026-09-02-appliance-dhcp-options-ui/">Configure DHCP options from the dashboard on Cloudflare One Appliance</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-images-binding-updates"><a href="/changelog/post/2026-09-02-images-binding-updates/">New in Images: text rasterization and updates to the binding</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>We've added more ways to manage and manipulate images with the <a href="/images/optimization/binding/">Images binding</a>. Here's what's new:</p>
<p><strong>Render text into an image.</strong> Output a string of text into its own image or draw it over another image.</p>
<ul>
<li>Use the <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> method to rasterize text with the Images binding.</li>
<li>Style content using the <code>font</code>, <code>size</code>, and <code>color</code> options.</li>
<li>The <a href="/images/optimization/draw-overlays/#draw-with-cfimage"><code>draw</code></a> array in <code>cf.image</code> now accepts a <code>text</code> key.</li>
</ul>
<p><strong>Manage hosted images without an API token.</strong></p>
<ul>
<li><strong>Metadata filtering:</strong> Pass <code>filter.metadata</code> to <a href="/images/storage/binding/#listoptions"><code>.list()</code></a> to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, <code>priority: { gte: 2, lte: 5 }</code>.</li>
<li><strong>Server-side signing:</strong> Get a signed URL for a private image with <a href="/images/storage/binding/#imageimageidsignedurloptions"><code>.signedUrl()</code></a>.</li>
<li><strong>User uploads:</strong> Create a Direct Creator Upload link with <a href="/images/storage/binding/#createdirectuploadoptions"><code>.createDirectUpload()</code></a> so that a client can upload an image to your storage.</li>
</ul>
<p><strong>Set headers in a single call.</strong></p>
<ul>
<li>Pass a <code>headers</code> option to <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> to set headers without rebuilding the <code>Response</code>.</li>
<li><code>Content-Type</code> is always taken from the optimized image and can't be overridden by a specified header.</li>
<li>Set <code>Cache-Control</code> with <a href="/workers/cache/">Workers Cache</a> to cache your optimized image at the edge.</li>
</ul>
<p>For more information, refer to <a href="/images/optimization/binding/">Optimize with Workers</a>, <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>, and <a href="/images/storage/binding/">Manage hosted images with Workers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-tunnel-mesh-bulk-route-creation"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-one</span><span>cloudflare-wan</span><span>mesh</span></div><div class="changelog-body"><p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-cursor-cloud-agents"><a href="/changelog/post/2026-09-02-cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a></h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><p><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines</a> let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by <a href="/containers/">Cloudflare Containers</a>.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/cursor-cloud-agents-self-hosted-pool.png" alt="Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool" /></p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source <a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a> deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-02">Sep 2, 2026</time><div>
<h2 id="post-2026-09-02-python-workers-web-framework-support"><a href="/changelog/post/2026-09-02-python-workers-web-framework-support/">Python Workers now support WSGI web frameworks like Django and Flask</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python web frameworks following the <a href="https://peps.python.org/pep-3333/">Web Server Gateway Interface (WSGI)</a> or <a href="https://asgi.readthedocs.io/">Asynchronous Server Gateway Interface (ASGI)</a> specification can now be used in Python Workers.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-using-web-frameworks-with-python-workers">Using web frameworks with Python Workers</h4>
<p>Based on the web framework you are using, you can use either <code>wsgi</code> or <code>asgi</code> from the <code>workers</code> module.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-wsgi-frameworks">WSGI frameworks</h4>
<p>For WSGI frameworks like Django or Flask:</p>
<pre><code class="language-python">from workers import wsgi&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;&#10;app = get_wsgi_application()&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p>The <code>wsgi.entrypoint</code> is equivalent to creating a <code>WorkerEntrypoint</code> class and using the <code>wsgi.fetch</code> method. If you want more control over the <code>WorkerEntrypoint</code> class, you can do so:</p>
<pre><code class="language-python">from workers import wsgi, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(app, request, self.env)&#10;</code></pre>
<h4 id="2026-09-02-python-workers-web-framework-support-asgi-frameworks">ASGI frameworks</h4>
<p>For ASGI frameworks like FastAPI or Starlette:</p>
<pre><code class="language-python">from workers import asgi&#10;&#10;from fastapi import FastAPI&#10;&#10;app = FastAPI()&#10;Default = asgi.entrypoint(app)&#10;</code></pre>
<p>For more information about using individual web frameworks, refer to the <a href="/workers/languages/python/packages/">packages documentation in Python Workers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-01">Sep 1, 2026</time><div>
<h2 id="post-2026-09-01-billing-and-model-names"><a href="/changelog/post/2026-09-01-billing-and-model-names/">AI Gateway consolidates monthly usage invoice line items and standardizes model names</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.</p>
<p>For example, an invoice that previously included these separate line items:</p>
<ul>
<li><code>anthropic claude-haiku-4-5-20251001 Input Tokens</code>: 40,000 tokens at $0.000001 ($0.04)</li>
<li><code>anthropic claude-haiku-4-5-20251001 Output Tokens</code>: 24,000 tokens at $0.000005 ($0.12)</li>
</ul>
<p>The updated invoice includes one line item: <code>anthropic/claude-haiku-4.5</code>: $0.16.</p>
<p>AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent <code>provider/model</code> identifier.</p>
<p>For more information, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and <a href="/ai-gateway/observability/logging/">AI Gateway logging documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-01">Sep 1, 2026</time><div>
<h2 id="post-2026-09-01-d1-free-tier-limit-enforcement"><a href="/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/">D1 enforces free tier daily query limits</a></h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>Beginning September 1, 2026, D1 queries on the <a href="/workers/platform/pricing/#workers">Workers Free plan</a> will fail when an account exceeds the daily <a href="/d1/platform/pricing/">row read or row write limits</a>. Queries via the <a href="/d1/worker-api/">Workers Binding API</a> and the <a href="/d1/rest-api/">REST API</a> will return errors until the limit resets at midnight UTC. Stored data is not affected.</p>
<p>You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row read limit.</td>
</tr>
<tr>
<td>Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row write limit.</td>
</tr>
</tbody>
</table>
<p>Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add <a href="/d1/best-practices/use-indexes/">indexes</a> to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>.</p>
<p>For more information on D1 errors and how to handle them, refer to the <a href="/d1/observability/debug-d1/#error-list">D1 error list</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-01">Sep 1, 2026</time><div>
<h2 id="post-2026-09-01-waf-release"><a href="/changelog/post/2026-09-01-waf-release/">WAF Release - 2026-09-01</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.</li>
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
				<code class="nb-rule-id" title="d2d75b2f0614405f9fab0354bcfa0966">bcfa0966</code>
</td>
<td>N/A</td>
<td>SQLi - WHERE Comparison With WITH Clause</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-31">Aug 31, 2026</time><div>
<h2 id="post-2026-08-31-crawl-content-use"><a href="/changelog/post/2026-08-31-crawl-content-use/">Crawl endpoint now respects the Content Signals `use` directive</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code></a> endpoint now respects the <code>use</code> directive of the <a href="https://contentsignals.org/">Content Signals</a> standard, letting site owners express the maximum level at which their content may be used.</p>
<p>You can declare your intended level with the new <code>contentUse</code> parameter. Allowed values, from least to most permissive, are <code>reference</code> and <code>full</code>, and the default is <code>full</code>. If a target site's <code>robots.txt</code> sets a <code>use</code> level that is more restrictive than your declared <code>contentUse</code>, the crawl request is rejected with a <code>400</code> error.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/browser-run/quick-actions/crawl-endpoint/#content-signals">Content Signals</a> in the <code>/crawl</code> endpoint documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-31">Aug 31, 2026</time><div>
<h2 id="post-2026-08-31-pool-sets"><a href="/changelog/post/2026-08-31-pool-sets/">Load Balancing now supports pool sets</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.</p>
<p>Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.</p>
<p>For example, this pool set uses Dynamic Latency steering for traffic from Germany:</p>
<pre><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;germany-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.</p>
<p>For configuration details and more examples, refer to <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-30">Aug 30, 2026</time><div>
<h2 id="post-2026-08-30-glm-5.3-flash"><a href="/changelog/post/2026-08-30-glm-5.3-flash/">AI Search now supports GLM-5.3 Flash</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports <a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> for text generation. The model has a 1,048,576-token context window and runs on Workers AI.</p>
<p>To configure the model for an AI Search instance, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-29">Aug 29, 2026</time><div>
<h2 id="post-2026-08-28-warp-linux-ga"><a href="/changelog/post/2026-08-28-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.7.1377.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-29">Aug 29, 2026</time><div>
<h2 id="post-2026-08-28-warp-macos-ga"><a href="/changelog/post/2026-08-28-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.7.1376.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-29">Aug 29, 2026</time><div>
<h2 id="post-2026-08-28-warp-windows-ga"><a href="/changelog/post/2026-08-28-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.7.1376.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-28">Aug 28, 2026</time><div>
<h2 id="post-2026-08-28-dataset-configuration"><a href="/changelog/post/2026-08-28-dataset-configuration/">Improved dataset configuration in Log Explorer</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.</p>
<ul>
<li><strong>Grouped field selection</strong> organizes fields by category and shows the number selected in each group.</li>
<li><strong>Field details</strong> identify each field's data type and mark required or deprecated fields.</li>
<li><strong>Bulk controls</strong> let you select all fields or reset the selection to the dataset defaults.</li>
<li><strong>Ingestion filters</strong> let you ingest all events or only events that match your conditions.</li>
</ul>
<p>These controls are available when you add a dataset or select <strong>Actions</strong> &gt; <strong>Edit</strong> for an enabled dataset.</p>
<p>For more information, refer to <a href="/log-explorer/manage-datasets/#configure-fields-and-filters">Configure fields and filters</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/">Previous</a><span>Page 2 of 50</span><a class="pagination-next" rel="next" href="/changelog/3/">Next</a></nav>
</div>
