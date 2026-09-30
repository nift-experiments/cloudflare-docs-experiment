<p>By default, R2 buckets are private. To serve R2 objects through Cloudflare's cache, you need to attach a domain name you control — called a <a href="/r2/buckets/public-buckets/#custom-domains">Custom Domain</a> — to the bucket. This creates a public URL backed by Cloudflare's network, so requests for your stored files go through Cloudflare's cache instead of hitting R2 directly every time.</p>
<p>Follow these steps to set up a Custom Domain for your bucket:</p>
<ol>
<li>Go to <strong>R2</strong> and select your bucket.</li>
<li>On the bucket page, select <strong>Settings</strong>.</li>
<li>Under <strong>Public access</strong> &gt; <strong>Custom Domains</strong>, select <strong>Connect Domain</strong>.</li>
<li>Enter the domain name you want to connect to and select <strong>Continue</strong>.</li>
<li>Review the new DNS record that will be added and select <strong>Connect Domain</strong>.</li>
</ol>
<p>Cloudflare automatically adds a CNAME record that maps your domain to the bucket, generating a publicly available URL in the format <code>[name].domain.com</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3803.md")
</aside>
<h2 id="tiered-cache">Tiered Cache</h2>
<p>By default, Cloudflare caches R2 content at edge data centers (the data centers closest to visitors) based on <a href="/cache/how-to/cache-rules/">cache rules</a>. Each edge data center that gets a cache miss fetches content directly from R2.</p>
<p><a href="/cache/how-to/tiered-cache/">Tiered Cache</a> changes this by organizing data centers into a hierarchy. When a nearby data center has a cache miss, it first checks a designated upper-tier data center before going to R2. This reduces the number of requests that reach R2.</p>
<p>To enable Tiered Cache for R2, configure <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a>, which automatically selects the upper-tier data center with the lowest latency to your R2 bucket.</p>
<h2 id="additional-considerations">Additional considerations</h2>
<ul>
<li><strong>Access controls</strong>: When you connect a Custom Domain, your R2 bucket becomes publicly accessible. Apply access controls to restrict who can request your files. Refer to <a href="/cache/interaction-cloudflare-products/waf-snippets/">Control cache access with WAF and Snippets</a> for more information.</li>
<li><strong>Cacheable size limits</strong>: Files that exceed the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">cacheable size limits</a> are not cached. Free, Pro, and Business plans have a limit of 512 MB per file. Enterprise plans default to 5 GB per file.</li>
<li><strong>Default cached file types</strong>: Cloudflare does not cache all file types by default. For example, HTML and JSON are not cached unless you create a <a href="/cache/how-to/cache-rules/">Cache Rule</a> with the appropriate settings.</li>
</ul>
