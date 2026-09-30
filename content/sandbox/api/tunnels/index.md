---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/tunnels/
  description: Expose sandbox services on the public internet with quick tunnels (*.trycloudflare.com) or named tunnels bound to a hostname on your Cloudflare zone.
  full_title: Tunnels · Cloudflare Sandbox SDK docs
  head_html: <title>Tunnels · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose sandbox services on the public internet with quick tunnels (*.trycloudflare.com) or named tunnels bound to a hostname on your Cloudflare zone."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/tunnels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/tunnels/index.md"><meta property="og:title" content="Tunnels · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose sandbox services on the public internet with quick tunnels (*.trycloudflare.com) or named tunnels bound to a hostname on your Cloudflare zone."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/tunnels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/tunnels/#page","headline":"Tunnels \u00b7 Cloudflare Sandbox SDK docs","description":"Expose sandbox services on the public internet with quick tunnels (.trycloudflare.com) or named tunnels bound to a hostname on your Cloudflare zone.","url":"https://developers.cloudflare.com/sandbox/api/tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/tunnels/
  schema: 1
---
<p>The <code>sandbox.tunnels</code> namespace exposes a service running inside a sandbox on the public internet through a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. The SDK runs <code>cloudflared</code> inside the container and opens a persistent QUIC connection to Cloudflare's edge.</p>
<p>Two flavors are available:</p>
<ul>
<li><strong>Quick tunnels</strong> (<code>sandbox.tunnels.get(port)</code>) — zero-config. Cloudflare assigns a random <code>*.trycloudflare.com</code> hostname for each new <code>cloudflared</code> process. No Cloudflare account, API token, DNS record, or custom domain required. URLs change on every container restart.</li>
<li><strong>Named tunnels</strong> (<code>sandbox.tunnels.get(port, { name })</code>) — bind a stable hostname <code>&lt;name&gt;.&lt;your-zone&gt;</code> on a zone you control. The hostname survives container restarts and is shared across sandboxes that request the same <code>name</code>. Requires a Cloudflare API token, an account, and a zone.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="when-to-use-quick-vs-named-tunnels">When to use quick vs. named tunnels</h3>
@markup("md", "content/.markup/bodies/13590.md")
</aside>
<h2 id="requirements">Requirements</h2>
<p>Both tunnel flavors require:</p>
<ul>
<li><strong>RPC transport.</strong> Calling <code>sandbox.tunnels</code> on HTTP/Websocket transports throws <code>&quot;RPC transport required&quot;</code>. See <a href="/sandbox/configuration/transport/">Transport configuration</a>.</li>
</ul>
<p>Named tunnels additionally require a Cloudflare API token, account, and zone — refer to <a href="#prerequisites">Named tunnels: prerequisites</a>.</p>
<h2 id="methods">Methods</h2>
<h3 id="tunnels-get"><code>tunnels.get()</code></h3>
<p>Return a tunnel record for <code>port</code>. The SDK spawns a fresh <code>cloudflared</code> process inside the container if not already running. The method is idempotent: repeated calls with the same <code>(port, options)</code> return the same record.</p>
<pre tabindex="0"><code class="language-ts">const tunnel = await sandbox.tunnels.get(&#10;  port: number,&#10;  options?: { name?: string }&#10;): Promise&lt;TunnelInfo&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>port</code> — Port number inside the sandbox to expose (1024-65535, excluding reserved ports). The service to tunnel to must already be listening on <code>0.0.0.0:&lt;port&gt;</code> inside the container.</li>
<li><code>options.name</code> <em>(optional)</em> — Single DNS label (lowercase letters, digits, internal hyphens; 1–63 chars; no dots). When set, provisions a <a href="#named-tunnels">named tunnel</a> bound to <code>&lt;name&gt;.&lt;your-zone&gt;</code>. When omitted, provisions a quick tunnel.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;TunnelInfo&gt;</code> — the tunnel record. See <a href="#tunnelinfo"><code>TunnelInfo</code></a>.</p>
<p>Calling <code>get(port)</code> with different <code>options</code> on a port that already has a tunnel throws. Call <a href="#tunnelsdestroy"><code>destroy(port)</code></a> first.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13591.md")
</div>
<h3 id="tunnels-list"><code>tunnels.list()</code></h3>
<p>Return every tunnel currently tracked for this sandbox.</p>
<pre tabindex="0"><code class="language-ts">const tunnels = await sandbox.tunnels.list(): Promise&lt;TunnelInfo[]&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>Promise&lt;TunnelInfo[]&gt;</code> — an array of <a href="#tunnelinfo"><code>TunnelInfo</code></a> records. Empty when no tunnels are active.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13592.md")
</div>
<h3 id="tunnels-destroy"><code>tunnels.destroy()</code></h3>
<p>Tear down a tunnel. Accepts either the port number or the <code>TunnelInfo</code> record returned by <code>get()</code>. Idempotent — destroying an unknown port resolves successfully.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.tunnels.destroy(portOrInfo: number | TunnelInfo): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>portOrInfo</code> — Either the port number or the <code>TunnelInfo</code> record returned by <a href="#tunnelsget"><code>get()</code></a>.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13593.md")
</div>
<h2 id="types">Types</h2>
<h3 id="tunnelinfo"><code>TunnelInfo</code></h3>
<p>Quick tunnels omit <code>name</code>; named tunnels carry the label passed via <code>options.name</code>.</p>
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
<td><code>id</code></td>
<td><code>string</code></td>
<td>Tunnel identifier. <code>quick-&lt;random&gt;</code> for quick tunnels, the Cloudflare Tunnel UUID for named tunnels.</td>
</tr>
<tr>
<td><code>port</code></td>
<td><code>number</code></td>
<td>Port number inside the sandbox that the tunnel proxies to.</td>
</tr>
<tr>
<td><code>url</code></td>
<td><code>string</code></td>
<td>Public URL — <code>https://&lt;random&gt;.trycloudflare.com</code> (quick) or <code>https://&lt;name&gt;.&lt;your-zone&gt;</code> (named).</td>
</tr>
<tr>
<td><code>hostname</code></td>
<td><code>string</code></td>
<td>Hostname component of <code>url</code>.</td>
</tr>
<tr>
<td><code>createdAt</code></td>
<td><code>string</code></td>
<td>ISO-8601 timestamp of when the tunnel was created.</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td><strong>Named tunnels only.</strong> The label passed via <code>options.name</code>. Absent on quick tunnels.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-ts">type TunnelInfo = QuickTunnelInfo | NamedTunnelInfo;&#10;&#10;interface QuickTunnelInfo {&#10;  id: string;&#10;  port: number;&#10;  url: string;&#10;  hostname: string;&#10;  createdAt: string;&#10;  name?: never;&#10;}&#10;&#10;interface NamedTunnelInfo {&#10;  id: string;&#10;  port: number;&#10;  url: string;&#10;  hostname: string;&#10;  createdAt: string;&#10;  name: string;&#10;}&#10;</code></pre>
<h2 id="named-tunnels">Named tunnels</h2>
<p>Named tunnels bind a user-controlled hostname — <code>&lt;name&gt;.&lt;your-zone&gt;</code> — backed by a managed <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and a proxied <code>CNAME</code> record on your zone. Unlike quick tunnels, the URL is <strong>stable across container restarts</strong> and <strong>shared across sandboxes</strong> that call <code>get(port, { name })</code> with the same <code>name</code>.</p>
<h3 id="how-they-differ-from-quick-tunnels">How they differ from quick tunnels</h3>
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Quick tunnel</th>
<th>Named tunnel</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Random <code>*.trycloudflare.com</code>, assigned by Cloudflare</td>
<td><code>&lt;name&gt;.&lt;your-zone&gt;</code>, chosen by you</td>
</tr>
<tr>
<td>Stability</td>
<td>Changes on every container restart</td>
<td>Stable; persists across restarts and sandbox lifecycles</td>
</tr>
<tr>
<td>Cloudflare account</td>
<td>Not required</td>
<td>Required (API token + zone)</td>
</tr>
<tr>
<td>Cloudflare-side resources</td>
<td>None</td>
<td>Managed <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> + proxied DNS <code>CNAME</code></td>
</tr>
<tr>
<td>Uptime guarantee</td>
<td>None (debug aid)</td>
<td>Backed by your zone's standard Cloudflare SLA</td>
</tr>
<tr>
<td>TLS certificate</td>
<td>Cloudflare-owned wildcard</td>
<td>Universal SSL on <code>&lt;name&gt;.&lt;your-zone&gt;</code> (single DNS label only)</td>
</tr>
<tr>
<td>Server-Sent Events</td>
<td>Not supported (edge buffers <code>text/event-stream</code>)</td>
<td>Supported</td>
</tr>
</tbody>
</table>
<h3 id="prerequisites">Prerequisites</h3>
<p>To provision a named tunnel, you need:</p>
<ol>
<li>A <strong>Cloudflare account</strong> with a <strong>zone</strong> (a domain you control on Cloudflare DNS).</li>
<li>A <strong>Cloudflare API token</strong> with the correct scopes.</li>
<li>The <strong>account ID</strong> and <strong>zone ID</strong> — the SDK can infer both from the token when the token is scoped to exactly one of each.</li>
</ol>
<h4 id="create-the-api-token">Create the API token</h4>
<p>Create a token from <strong>My Profile</strong> &gt; <strong>API Tokens</strong> &gt; <strong>Create Token</strong> &gt; <strong>Custom token</strong> with the following permissions:</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Used for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Account</strong> · <strong>Cloudflare Tunnel</strong> · <strong>Edit</strong></td>
<td>Create, look up, and delete tunnels.</td>
</tr>
<tr>
<td><strong>Zone</strong> · <strong>DNS</strong> · <strong>Edit</strong></td>
<td>Upsert and delete the proxied <code>CNAME</code> for <code>&lt;name&gt;.&lt;your-zone&gt;</code>.</td>
</tr>
<tr>
<td><strong>Zone</strong> · <strong>Zone</strong> · <strong>Read</strong></td>
<td>Look up the zone's name to derive <code>&lt;name&gt;.&lt;your-zone&gt;</code>.</td>
</tr>
<tr>
<td><strong>Account</strong> · <strong>Account Settings</strong> · <strong>Read</strong> <em>(optional)</em></td>
<td>Lets the SDK infer the account ID from the token when not set explicitly.</td>
</tr>
</tbody>
</table>
<p>Under <strong>Account Resources</strong>, scope the token to the account that will own the tunnel. Under <strong>Zone Resources</strong>, scope it to the specific zone you want to bind to.</p>
<p>Both <a href="/fundamentals/api/get-started/create-token/">User API Tokens</a> and <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API Tokens</a> (secret prefixed <code>cfat_</code>) are supported — the SDK detects the token kind and uses the appropriate introspection endpoint.</p>
<h4 id="create-the-token-with-the-rest-api">Create the token with the REST API</h4>
<p>You can create the token without using the dashboard. The permission group IDs are stable; the snippet below uses placeholders — fetch the current IDs from <a href="/api/operations/permission-groups-list-permission-groups/"><code>GET /user/tokens/permission_groups</code></a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/user/tokens&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;sandbox-named-tunnels&quot;,&#10;    &quot;policies&quot;: [&#10;      {&#10;        &quot;effect&quot;: &quot;allow&quot;,&#10;        &quot;resources&quot;: { &quot;com.cloudflare.api.account.&lt;ACCOUNT_ID&gt;&quot;: &quot;*&quot; },&#10;        &quot;permission_groups&quot;: [{ &quot;id&quot;: &quot;&lt;TUNNEL_EDIT_GROUP_ID&gt;&quot; }]&#10;      },&#10;      {&#10;        &quot;effect&quot;: &quot;allow&quot;,&#10;        &quot;resources&quot;: { &quot;com.cloudflare.api.account.zone.&lt;ZONE_ID&gt;&quot;: &quot;*&quot; },&#10;        &quot;permission_groups&quot;: [&#10;          { &quot;id&quot;: &quot;&lt;DNS_EDIT_GROUP_ID&gt;&quot; },&#10;          { &quot;id&quot;: &quot;&lt;ZONE_READ_GROUP_ID&gt;&quot; }&#10;        ]&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="bind-the-token-and-ids-to-the-worker">Bind the token and IDs to the Worker</h4>
<p>The SDK reads <code>CLOUDFLARE_API_TOKEN</code> from the Worker environment and attempts to derive the account ID and zone ID from the token automatically. If the token is associated with multiple accounts or zones the SDK cannot pick one unambiguously, and you must set <code>CLOUDFLARE_ACCOUNT_ID</code> and/or <code>CLOUDFLARE_ZONE_ID</code> explicitly.</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Required?</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CLOUDFLARE_API_TOKEN</code></td>
<td>Yes</td>
<td>Store as a secret with <code>wrangler secret put</code>.</td>
</tr>
<tr>
<td><code>CLOUDFLARE_ACCOUNT_ID</code></td>
<td>Only if the token sees multiple accounts</td>
<td>Inferred from the token otherwise.</td>
</tr>
<tr>
<td><code>CLOUDFLARE_ZONE_ID</code></td>
<td>Only if the token sees multiple zones</td>
<td>Inferred from the token otherwise.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-bash">npx wrangler secret put CLOUDFLARE_API_TOKEN&#10;</code></pre>
<p>For local development, place the variables in <code>.dev.vars</code> (gitignored). For production, set the non-secret IDs (when needed) under <code>vars</code> in your Wrangler config:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;  &quot;vars&quot;: {&#10;    &quot;CLOUDFLARE_ACCOUNT_ID&quot;: &quot;&lt;account-id&gt;&quot;,&#10;    &quot;CLOUDFLARE_ZONE_ID&quot;: &quot;&lt;zone-id&gt;&quot;&#10;  }&#10;}&#10;</code></pre>
<p>When inference fails, the SDK throws a clear error naming the variable to set.</p>
<h3 id="example">Example</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13594.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="name-must-be-a-single-dns-label">`name` must be a single DNS label</h3>
@markup("md", "content/.markup/bodies/13589.md")
</aside>
<h3 id="lifecycle">Lifecycle</h3>
<p>Named tunnels are designed to outlive the container that provisioned them:</p>
<ol>
<li><strong>First call</strong> to <code>sandbox.tunnels.get(port, { name })</code>:
<ul>
<li>Resolves <code>&lt;name&gt;.&lt;your-zone&gt;</code> from the configured zone ID.</li>
<li>Creates a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> resource named <code>sandbox-&lt;sandbox-id&gt;-&lt;name&gt;</code> tagged with the sandbox ID.</li>
<li>Upserts a proxied <code>CNAME</code> from <code>&lt;name&gt;.&lt;your-zone&gt;</code> to <code>&lt;tunnel-id&gt;.cfargotunnel.com</code>.</li>
<li>Spawns <code>cloudflared</code> inside the container with the tunnel's token.</li>
</ul>
</li>
<li><strong>Subsequent calls</strong> with the same <code>(port, name)</code> return the cached record without contacting Cloudflare.</li>
<li><strong>Container restart</strong> (Durable Object eviction, deploy, crash):
<ul>
<li><code>cloudflared</code> dies with the container, but the Cloudflare Tunnel and DNS record are preserved.</li>
<li>On the next <code>get(port, { name })</code>, the SDK rediscovers the tagged tunnel via the Cloudflare API and respawns <code>cloudflared</code>. The hostname is unchanged.</li>
</ul>
</li>
<li><strong>Explicit teardown</strong> with <code>sandbox.tunnels.destroy(port)</code>:
<ul>
<li>Stops <code>cloudflared</code> inside the container.</li>
<li>Deletes the Cloudflare Tunnel resource.</li>
<li>Deletes the proxied <code>CNAME</code> record.</li>
</ul>
</li>
<li><strong>Sandbox destroy</strong> with <code>sandbox.destroy()</code> tears down every tunnel the sandbox provisioned, including the Cloudflare-side resources, before stopping the container.</li>
</ol>
<p>If <code>destroy()</code> fails to reach the Cloudflare API (for example, the token was revoked between <code>get()</code> and <code>destroy()</code>), the SDK logs a warning naming the orphaned <code>tunnelId</code> and <code>dnsRecordId</code> so you can clean up manually from the dashboard.</p>
<h3 id="cloudflare-resources-and-tagging">Cloudflare resources and tagging</h3>
<p>Named tunnels create resources <strong>on your Cloudflare account, outside the sandbox container</strong>. They are not stored in Durable Object storage and do not count against sandbox quotas, but they do show up in the Cloudflare dashboard and consume your account's tunnel and DNS quotas.</p>
<p>For each <code>(sandbox, name)</code> pair, the SDK creates:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Name / location</th>
<th>Identifier</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Tunnel</td>
<td><strong>Networking</strong> &gt; <strong>Tunnels</strong></td>
<td><code>sandbox-&lt;sandbox-id&gt;-&lt;name&gt;</code></td>
</tr>
<tr>
<td>Proxied DNS record</td>
<td>Your zone, <strong>DNS</strong> &gt; <strong>Records</strong></td>
<td><code>CNAME &lt;name&gt;.&lt;zone&gt; → &lt;tunnel-id&gt;.cfargotunnel.com</code></td>
</tr>
</tbody>
</table>
<p>Both resources are tagged so you can audit, query, and bulk-clean them from the dashboard or API:</p>
<ul>
<li><strong>Tunnel metadata</strong>: <code>{ sandboxId, createdBy: 'sandbox-sdk', name, port }</code></li>
<li><strong>DNS record comment</strong>: <code>sandbox-&lt;sandbox-id&gt;</code></li>
<li><strong>Resource tag</strong> <em>(Enterprise plans only)</em>: <code>sandboxId:&lt;sandbox-id&gt;</code></li>
</ul>
<p>On non-Enterprise plans, Cloudflare rejects resource tags; the SDK detects this and retries the request without tags. The DNS comment and tunnel metadata still apply, so you can always trace a resource back to its sandbox.</p>
<p>To list every tunnel created by the SDK for a given account:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/cfd_tunnel?name=sandbox-&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p><strong>Both tunnel flavors:</strong></p>
<ul>
<li><strong>WARP / Zero Trust egress.</strong> If your local machine runs Cloudflare WARP or another Zero Trust egress policy, outbound traffic to <code>api.trycloudflare.com</code> and the cloudflared edge can be blocked. When that happens, <code>tunnels.get()</code> hangs on the edge handshake and eventually times out. Disable WARP or add an egress exception for these destinations.</li>
<li><strong>Brief DNS warm-up.</strong> The first request through a brand-new URL can take a couple of seconds while DNS propagates, even after <code>get()</code> resolves.</li>
</ul>
<p><strong>Quick tunnels only:</strong></p>
<ul>
<li><strong>URLs do not survive container restart.</strong> Cloudflare assigns the hostname during <code>cloudflared</code>'s startup handshake, so every restart yields a new URL. The SDK clears its tunnel cache when the container starts, so the next <code>tunnels.get(port)</code> returns a fresh record. Use a <a href="#named-tunnels">named tunnel</a> for a stable hostname.</li>
<li><strong>No uptime guarantee.</strong> Cloudflare positions <code>trycloudflare.com</code> as a debug aid, not a production target.</li>
<li><strong>No Server-Sent Events.</strong> The <code>trycloudflare.com</code> edge buffers <code>text/event-stream</code> responses, so SSE events never reach the client. WebSockets work normally. Use a <a href="#named-tunnels">named tunnel</a> if your service streams SSE.</li>
</ul>
<p><strong>Named tunnels only:</strong></p>
<ul>
<li><strong>Single DNS label.</strong> <code>name</code> must not contain dots. Universal SSL only covers <code>&lt;name&gt;.&lt;your-zone&gt;</code>.</li>
<li><strong>Counts against your zone's quotas.</strong> Each named tunnel creates a Cloudflare Tunnel and a DNS record on your account. See <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/">Cloudflare Tunnel limits</a>.</li>
<li><strong>Cleanup requires the API token.</strong> If <code>destroy()</code> runs after the token has been revoked, the Cloudflare-side resources are orphaned. The SDK logs the orphan IDs so you can remove them manually.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/preview-urls/">Preview URLs concept</a> — Worker-fronted preview URLs and how they differ from quick tunnels.</li>
<li><a href="/sandbox/api/ports/">Ports API</a> — <code>exposePort()</code> and the Worker-fronted preview URL flow.</li>
<li><a href="/sandbox/guides/expose-services/">Expose services guide</a> — End-to-end walkthrough for exposing services in production.</li>
<li><a href="/sandbox/configuration/transport/">Transport configuration</a> — RPC vs. route-based transport.</li>
</ul>
