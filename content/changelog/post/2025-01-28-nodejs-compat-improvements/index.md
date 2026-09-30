<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 28, 2025</time><h2 id="post-title">Support for Node.js DNS, Net, and Timer APIs in Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled, you can now use the following Node.js APIs:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/net/"><code>node:net</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/dns/"><code>node:dns</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/timers/"><code>node:timers</code></a></li>
</ul>
<h4 id="node-net">node:net</h4>
<p>You can use <a href="https://nodejs.org/api/net.html"><code>node:net</code></a> to create a direct connection to servers via a TCP sockets
with <a href="https://nodejs.org/api/net.html#class-netsocket"><code>net.Socket</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17762.md")</div>
<p>Additionally, you can now use other APIs including <a href="https://nodejs.org/api/net.html#class-netblocklist"><code>net.BlockList</code></a> and
<a href="https://nodejs.org/api/net.html#class-netsocketaddress"><code>net.SocketAddress</code></a>.</p>
<p>Note that <a href="https://nodejs.org/api/net.html#class-netserver"><code>net.Server</code></a> is not supported.</p>
<h4 id="node-dns">node:dns</h4>
<p>You can use <a href="https://nodejs.org/api/dns.html"><code>node:dns</code></a> for name resolution via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> using
<a href="https://www.cloudflare.com/application-services/products/dns/">Cloudflare DNS</a> at 1.1.1.1.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17763.md")</div>
<p>All <code>node:dns</code> functions are available, except <code>lookup</code>, <code>lookupService</code>, and <code>resolve</code> which throw &quot;Not implemented&quot; errors when called.</p>
<h4 id="node-timers">node:timers</h4>
<p>You can use <a href="https://nodejs.org/api/timers.html"><code>node:timers</code></a> to schedule functions to be called at some future period of time.</p>
<p>This includes <a href="https://nodejs.org/api/timers.html#settimeoutcallback-delay-args"><code>setTimeout</code></a> for calling a function after a delay,
<a href="https://nodejs.org/api/timers.html#setintervalcallback-delay-args"><code>setInterval</code></a> for calling a function repeatedly,
and <a href="https://nodejs.org/api/timers.html#setimmediatecallback-args"><code>setImmediate</code></a> for calling a function in the next iteration of the event loop.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17764.md")</div>
</div></article></div>
