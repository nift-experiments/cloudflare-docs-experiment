<p>To allow a Worker to receive inbound HTTP requests, you must connect it to an external endpoint such that it can be accessed by the Internet.</p>
<p>There are three types of routes:</p>
<ul>
<li>
<p><a href="/workers/configuration/routing/custom-domains">Custom Domains</a>: Routes to a domain or subdomain (such as <code>example.com</code> or <code>shop.example.com</code>) within a Cloudflare zone where the Worker is the origin.</p>
</li>
<li>
<p><a href="/workers/configuration/routing/routes/">Routes</a>: Routes that are set within a Cloudflare zone where your origin server, if you have one, is behind a Worker that the Worker can communicate with.</p>
</li>
<li>
<p><a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a>: A <code>workers.dev</code> subdomain route is automatically created for each Worker to help you getting started quickly. You may choose to <a href="/workers/configuration/routing/workers-dev/">disable</a> your <code>workers.dev</code> subdomain.</p>
</li>
</ul>
<h2 id="what-is-best-for-me">What is best for me?</h2>
<p>It's recommended to run production Workers on a <a href="/workers/configuration/routing/">Workers route or custom domain</a>, rather than on your <code>workers.dev</code> subdomain. Your <code>workers.dev</code> subdomain is treated as a <a href="https://www.cloudflare.com/plans/">Free website</a> and is intended for personal or hobby projects that aren't business-critical.</p>
<p>Custom Domains are recommended for use cases where your Worker is your application's origin server. Custom Domains can also be invoked within the same zone via <code>fetch()</code>, unlike Routes.</p>
<p>Routes are recommended for use cases where your application's origin server is external to Cloudflare. Note that Routes cannot be the target of a same-zone <code>fetch()</code> call.</p>
