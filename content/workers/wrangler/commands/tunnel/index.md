<p>Manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from Wrangler. Create, run, and manage tunnels that securely connect your local services to Cloudflare's network — no public IPs required.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17429.md")
</aside>
<p>Wrangler manages the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, Wrangler will prompt you to download <code>cloudflared</code> to a local cache directory. You can skip this by installing <code>cloudflared</code> yourself and adding it to your <code>PATH</code>, or by setting the <code>CLOUDFLARED_PATH</code> environment variable to point to an existing binary.</p>
<h3 id="tunnel-create">tunnel create</h3>
<p>Create a new remotely managed <a href="/tunnel/">Cloudflare Tunnel</a>.</p>
<pre><code class="language-txt">wrangler tunnel create &lt;NAME&gt;&#10;</code></pre>
<ul>
<li><code>NAME</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>A name for your tunnel. Must be unique within your account.</li>
</ul>
</li>
</ul>
<p>Tunnels created via Wrangler are always <strong>remotely managed</strong> — configure them in the <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Cloudflare dashboard</a> or via the API.</p>
<p>After creation, use <code>wrangler tunnel run</code> with the tunnel ID to start the tunnel.</p>
<pre><code class="language-sh">npx wrangler tunnel create my-app&#10;</code></pre>
<pre><code class="language-sh">Creating tunnel &quot;my-app&quot;&#10;Created tunnel.&#10;ID: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;Name: my-app&#10;&#10;To run this tunnel, configure its ingress rules in the Cloudflare dashboard, then run:&#10;   wrangler tunnel run f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="tunnel-delete">tunnel delete</h3>
<p>Delete a Cloudflare Tunnel from your account.</p>
<pre><code class="language-txt">wrangler tunnel delete &lt;TUNNEL&gt; [OPTIONS]&#10;</code></pre>
<ul>
<li><code>TUNNEL</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name or UUID of the tunnel to delete.</li>
</ul>
</li>
<li><code>--force</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Skip the confirmation prompt.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17428.md")
</aside>
<pre><code class="language-sh">npx wrangler tunnel delete f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;</code></pre>
<pre><code class="language-sh">Are you sure you want to delete tunnel &quot;f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&quot;? This action cannot be undone. (y/n)&#10;Deleting tunnel f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;Tunnel deleted.&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="tunnel-info">tunnel info</h3>
<p>Display details about a Cloudflare Tunnel, including its ID, name, status, and creation time.</p>
<pre><code class="language-txt">wrangler tunnel info &lt;TUNNEL&gt;&#10;</code></pre>
<ul>
<li><code>TUNNEL</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name or UUID of the tunnel to inspect.</li>
</ul>
</li>
</ul>
<pre><code class="language-sh">npx wrangler tunnel info f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;</code></pre>
<pre><code class="language-sh">Getting tunnel details&#10;ID: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415&#10;Name: my-app&#10;Status: healthy&#10;Created: 2025-01-15T10:30:00Z&#10;Type: cfd_tunnel&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="tunnel-list">tunnel list</h3>
<p>List all Cloudflare Tunnels in your account.</p>
<pre><code class="language-txt">wrangler tunnel list&#10;</code></pre>
<p>The output includes the tunnel ID, name, status, and creation date for each tunnel. Only non-deleted tunnels are shown.</p>
<pre><code class="language-sh">npx wrangler tunnel list&#10;</code></pre>
<pre><code class="language-sh">Listing Cloudflare Tunnels&#10;&#10;ID                                   Name       Status    Created&#10;f70ff985-a4ef-4643-bbbc-4a0ed4fc8415 my-app     healthy   2025-01-15T10:30:00Z&#10;550e8400-e29b-41d4-a716-446655440000 api-tunnel inactive  2025-01-10T15:45:00Z&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="tunnel-run">tunnel run</h3>
<p>Run a Cloudflare Tunnel using the <a href="/tunnel/downloads/">cloudflared</a> daemon. This starts a persistent connection between your local machine and Cloudflare's network.</p>
<pre><code class="language-txt">wrangler tunnel run [TUNNEL] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>TUNNEL</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name or UUID of the tunnel to run. Required unless <code>--token</code> is provided.</li>
</ul>
</li>
<li><code>--token</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A tunnel token to use directly. Skips API authentication.</li>
</ul>
</li>
<li><code>--log-level</code> <span class="nb-type">string</span> <span class="nb-metainfo">(default: info) optional</span>
<ul>
<li>Log level for <code>cloudflared</code>. Does not affect Wrangler logs (controlled by <code>WRANGLER_LOG</code>). One of: <code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code>.</li>
</ul>
</li>
</ul>
<p>Named tunnels are <strong>remotely managed</strong> — configure ingress rules (which local services to expose) in the <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Cloudflare dashboard</a> or via the API before running the tunnel.</p>
<p>There are two ways to run a tunnel:</p>
<p><strong>By tunnel name or ID</strong> (fetches the token via the API):</p>
<pre><code class="language-sh">npx wrangler tunnel run my-app&#10;</code></pre>
<p><strong>By token</strong> (no API authentication needed — useful for CI/CD or remote servers):</p>
<pre><code class="language-sh">npx wrangler tunnel run --token eyJhIjoiNGE2MjY...&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17427.md")
</aside>
<p>Press <code>Ctrl+C</code> to stop the tunnel. Wrangler will send a graceful shutdown signal to <code>cloudflared</code> before exiting.</p>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="tunnel-quick-start">tunnel quick-start</h3>
<p>Start a free, temporary tunnel without a Cloudflare account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>. This is useful for quick demos, testing webhooks, or sharing local development servers.</p>
<pre><code class="language-txt">wrangler tunnel quick-start &lt;URL&gt;&#10;</code></pre>
<ul>
<li><code>URL</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The local URL to expose (for example, <code>http://localhost:8080</code>).</li>
</ul>
</li>
</ul>
<p>The tunnel is assigned a random <code>*.trycloudflare.com</code> subdomain and lasts for the duration of the process.</p>
<pre><code class="language-sh">npx wrangler tunnel quick-start http://localhost:8080&#10;</code></pre>
<pre><code class="language-sh">Starting quick tunnel to http://localhost:8080...&#10;Your tunnel URL: https://random-words-here.trycloudflare.com&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17426.md")
</aside>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
