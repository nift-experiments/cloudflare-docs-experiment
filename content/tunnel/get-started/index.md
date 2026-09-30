<p>Create a Cloudflare Tunnel and publish your first application in under 5 minutes.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/fundamentals/manage-domains/add-site/">domain on Cloudflare</a> (required to publish applications)</li>
<li>A server or VM with internet access where you will install <code>cloudflared</code></li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/14940.md")
</aside>
<h2 id="create-a-tunnel">Create a tunnel</h2>
<p>To create a new Cloudflare Tunnel:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14943.md")
</div></div>
<h2 id="publish-an-application">Publish an application</h2>
<p>To make an application accessible from the Internet, add a published application route to your tunnel. The tunnel route maps a public hostname to a local service.</p>
<p>If your origin already serves HTTPS or redirects HTTP to HTTPS, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins</a> to choose the <strong>Service URL</strong> and origin settings.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14951.md")
</div></div>
<p>Your application is now live at the hostname you configured. Cloudflare automatically proxies traffic through its network, applying CDN caching, WAF, and DDoS protection.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14939.md")
</aside>
<h2 id="quick-tunnels-development">Quick tunnels (development)</h2>
<p>For local development, you can instantly expose localhost without a Cloudflare account:</p>
<pre><code class="language-sh">cloudflared tunnel --url http://localhost:8080&#10;</code></pre>
<p>This generates a random <code>trycloudflare.com</code> subdomain that proxies traffic to your local server. Quick tunnels are for testing only — they have a 200 concurrent request limit and do not support Server-Sent Events (SSE).</p>
<p>For production use, <a href="#create-a-tunnel">create a tunnel</a> instead.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/tunnel/concepts/routing/">Routing</a> — Configure DNS records, load balancers, and protocol support.</li>
<li><a href="/tunnel/configuration/">Configuration</a> — Deploy replicas, manage tokens, and tune performance.</li>
<li><a href="/tunnel/guides/">Guides</a> — Deploy on Kubernetes, AWS, GCP, Terraform, and more.</li>
<li><a href="/tunnel/troubleshooting/">Troubleshooting</a> — Resolve common errors and connectivity issues.</li>
</ul>
