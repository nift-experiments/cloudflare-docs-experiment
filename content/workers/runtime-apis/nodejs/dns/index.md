<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17154.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/dns.html"><code>node:dns</code></a> for name resolution via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> using
<a href="https://www.cloudflare.com/application-services/products/dns/">Cloudflare DNS</a> at 1.1.1.1.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17155.md")
</div>
<p>All <code>node:dns</code> functions are available, except <code>lookup</code>, <code>lookupService</code>, and <code>resolve</code> which throw &quot;Not implemented&quot; errors when called.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17153.md")
</aside>
<p>The full <code>node:dns</code> API is documented in the <a href="https://nodejs.org/api/dns.html">Node.js documentation for <code>node:dns</code></a>.</p>
<pre><code>&#10;</code></pre>
