<p>By default, <a href="/workers/">Workers</a> and <a href="/pages/functions/">Pages Functions</a> are invoked in a data center closest to where the request was received. If you are running back-end logic in a Pages Function, it may be more performant to run that Pages Function closer to your back-end infrastructure rather than the end user. Smart Placement (beta) automatically places your workloads in an optimal location that minimizes latency and speeds up your applications.</p>
<h2 id="background">Background</h2>
<p>Smart Placement applies to Pages Functions and middleware. Normally, assets are always served globally and closest to your users.</p>
<p>Smart Placement on Pages currently has some caveats. While assets are always meant to be served from a location closest to the user, there are two exceptions to this behavior:</p>
<ol>
<li>
<p>If using middleware for every request (<code>functions/_middleware.js</code>) when Smart Placement is enabled, all assets will be served from a location closest to your back-end infrastructure. This may result in an unexpected increase in latency as a result.</p>
</li>
<li>
<p>When using <a href="https://developers.cloudflare.com/pages/functions/advanced-mode/"><code>env.ASSETS.fetch</code></a>, assets served via the <code>ASSETS</code> fetcher from your Pages Function are served from the same location as your Function. This could be the location closest to your back-end infrastructure and not the user.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10941.md")
</aside>
<h2 id="enable-smart-placement-beta">Enable Smart Placement (beta)</h2>
<p>Smart Placement is available on all plans.</p>
<h3 id="enable-smart-placement-via-the-dashboard">Enable Smart Placement via the dashboard</h3>
<p>To enable Smart Placement via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Pages project.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Runtime</strong>.</li>
<li>Under <strong>Placement</strong>, choose <strong>Smart</strong>.</li>
<li>Send some initial traffic (approximately 20-30 requests) to your Pages Functions. It takes a few minutes after you have sent traffic to your Pages Function for Smart Placement to take effect.</li>
<li>View your Pages Function's <a href="/workers/observability/metrics-and-analytics/">request duration metrics</a> under Functions Metrics.</li>
</ol>
<h2 id="give-feedback-on-smart-placement">Give feedback on Smart Placement</h2>
<p>Smart Placement is in beta. To share your thoughts and experience with Smart Placement, join the <a href="https://discord.cloudflare.com">Cloudflare Developer Discord</a>.</p>
