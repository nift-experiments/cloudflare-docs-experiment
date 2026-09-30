<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5317.md")
</aside>
<p>Developers can use the TryCloudflare tool to experiment with Cloudflare Tunnel without adding a site to Cloudflare's DNS. TryCloudflare will launch a process that generates a random subdomain on <code>trycloudflare.com</code>. Requests to that subdomain will be proxied through the Cloudflare network to your web server running on localhost.</p>
<h2 id="use-trycloudflare">Use TryCloudflare</h2>
<ol>
<li>Follow <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">these instructions</a> to install <code>cloudflared</code>. If you have an older copy, update to 2020.5.1 or later.</li>
<li>Launch a web server that is available over localhost to <code>cloudflared</code>.</li>
<li>Run the following terminal command to start a free tunnel.</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel --url http://localhost:8080&#10;</code></pre>
<p><code>cloudflared</code> will generate a random subdomain when connecting to the Cloudflare network and print it in the terminal for you to use and share. The output will serve traffic from the server on your local machine to the public Internet at a public URL.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5316.md")
</aside>
<h2 id="faq">FAQ</h2>
<h3 id="what-are-some-example-use-cases-for-trycloudflare">What are some example use cases for TryCloudflare?</h3>
<ul>
<li>Create a web server for a project on your laptop that you want to share with others on different networks</li>
<li>Test browser compatibility for a new site by creating a free Tunnel and testing the link in different browsers</li>
<li>Run speed tests from different regions by using a tool like Pingdom or WebPageTest to connect to the randomly-generated subdomain created by TryCloudflare</li>
</ul>
<h3 id="why-does-cloudflare-provide-this-service-for-free">Why does Cloudflare provide this service for free?</h3>
<ul>
<li>We want more users to experience the speed and security improvements of Cloudflare Tunnel. We hope you test it with TryCloudflare and decide to add it to your production sites.</li>
<li>Cloudflare's features historically require you to own a domain, set that domain's DNS to Cloudflare's nameservers, and configure its DNS records before you can begin to use any services. We hope to make more and more of our products available to trial without that burden.</li>
<li>We don't guarantee any SLA or uptime of TryCloudflare - we plan to test new Cloudflare Tunnel features and improvements on these free tunnels. This provides us with a group of connections to test before we deploy to production customers. Free tunnels are meant to be used for testing and development, not for deploying a production website.</li>
</ul>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Quick Tunnels are subject to a hard limit on the number of concurrent requests that can be proxied at any point in time. Currently, this limit is 200 in-flight requests. If a Quick Tunnel hits this limit, the HTTP response will return a <code>429</code> status code.</li>
<li>Quick Tunnels do not support Server-Sent Events (SSE).</li>
</ul>
<p>These limitations only apply to Quick Tunnels. To avoid these limitations, <a href="https://dash.cloudflare.com/sign-up">sign up</a> for a Cloudflare account and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">create a Cloudflare Tunnel</a>.</p>
<h3 id="legal">Legal</h3>
<p>Your installation of cloudflared software constitutes a symbol of your signature indicating that you accept the terms of the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/license/">Cloudflare License</a>, <a href="https://www.cloudflare.com/terms/">Terms</a> and <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>.</p>
