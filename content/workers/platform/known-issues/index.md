<p>Below are some known bugs and issues to be aware of when using Cloudflare Workers.</p>
<h2 id="route-specificity">Route specificity</h2>
<ul>
<li>When defining route specificity, a trailing <code>/*</code> in your pattern may not act as expected.</li>
</ul>
<p>Consider two different Workers, each deployed to the same zone. Worker A is assigned the <code>example.com/images/*</code> route and Worker B is given the <code>example.com/images*</code> route pattern. With these in place, here are how the following URLs will be resolved:</p>
<pre><code>// (A) example.com/images/*&#10;// (B) example.com/images*&#10;&#10;&quot;example.com/images&quot;&#10;// -&gt; B&#10;&quot;example.com/images123&quot;&#10;// -&gt; B&#10;&quot;example.com/images/hello&quot;&#10;// -&gt; B&#10;</code></pre>
<p>You will notice that all examples trigger Worker B. This includes the final example, which exemplifies the unexpected behavior.</p>
<p>When adding a wildcard on a subdomain, here are how the following URLs will be resolved:</p>
<pre><code>// (A) *.example.com/a&#10;// (B) a.example.com/*&#10;&#10;&quot;a.example.com/a&quot;&#10;// -&gt; B&#10;</code></pre>
<h2 id="wrangler-dev">wrangler dev</h2>
<ul>
<li>When running <code>wrangler dev --remote</code>, all outgoing requests are given the <code>cf-workers-preview-token</code> header, which Cloudflare recognizes as a preview request. This applies to the entire Cloudflare network, so making HTTP requests to other Cloudflare zones is currently discarded for security reasons. To enable a workaround, insert the following code into your Worker script:</li>
</ul>
<pre><code class="language-js">const request = new Request(url, incomingRequest);&#10;request.headers.delete(&#x27;cf-workers-preview-token&#x27;);&#10;return await fetch(request);&#10;</code></pre>
<h2 id="fetch-api-in-cname-setup">Fetch API in CNAME setup</h2>
<p>When you make a subrequest using <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> from a Worker, the Cloudflare DNS resolver is used. When a zone has a <a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup</a>, all hostnames that the Worker needs to be able to resolve require a dedicated DNS entry in Cloudflare's DNS setup. Otherwise the Fetch API call will fail with status code <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/">530 (1016)</a>.</p>
<p>Setup with missing DNS records in Cloudflare DNS</p>
<pre><code>// Zone in partial setup: example.com&#10;// DNS records at Authoritative DNS: sub1.example.com, sub2.example.com, ...&#10;// DNS records at Cloudflare DNS: sub1.example.com&#10;&#10;&quot;sub1.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;&quot;sub2.example.com/&quot;&#10;// -&gt; Cannot be resolved by Fetch API, will lead to 530 status code&#10;</code></pre>
<p>After adding <code>sub2.example.com</code> to Cloudflare DNS</p>
<pre><code>// Zone in partial setup: example.com&#10;// DNS records at Authoritative DNS: sub1.example.com, sub2.example.com, ...&#10;// DNS records at Cloudflare DNS: sub1.example.com, sub2.example.com&#10;&#10;&quot;sub1.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;&quot;sub2.example.com/&quot;&#10;// -&gt; Can be resolved by Fetch API&#10;</code></pre>
<h2 id="fetch-to-ip-addresses">Fetch to IP addresses</h2>
<p>For Workers subrequests, requests can only be made to URLs, not to IP addresses directly. To overcome this limitation <a href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/">add a A or AAAA name record to your zone</a> and then fetch that resource.</p>
<p>For example, in the zone <code>example.com</code> create a record of type <code>A</code> with the name <code>server</code> and value <code>192.0.2.1</code>, and then use:</p>
<pre><code class="language-js">await fetch(&#x27;http://server.example.com&#x27;)&#10;</code></pre>
<p>Do not use:</p>
<pre><code class="language-js">await fetch(&#x27;http://192.0.2.1&#x27;)&#10;</code></pre>
