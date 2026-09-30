<p class="article-summary">Determine how to cache a resource by setting TTLs, custom cache keys, and cache headers in a fetch request.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/cache-using-fetch"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16508.md")
</div></div>
<h2 id="caching-html-resources">Caching HTML resources</h2>
<pre><code class="language-js">// Force Cloudflare to cache an asset&#10;fetch(event.request, { cf: { cacheEverything: true } });&#10;</code></pre>
<p>Setting the cache level to <strong>Cache Everything</strong> will override the default cacheability of the asset. For time-to-live (TTL), Cloudflare will still rely on headers set by the origin.</p>
<h2 id="custom-cache-keys">Custom cache keys</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16502.md")
</aside>
<p>A request's cache key is what determines if two requests are the same for caching purposes. If a request has the same cache key as some previous request, then Cloudflare can serve the same cached response for both. For more about cache keys, refer to the <a href="/cache/how-to/cache-keys/#create-custom-cache-keys">Create custom cache keys</a> documentation.</p>
<pre><code class="language-js">// Set cache key for this request to &quot;some-string&quot;.&#10;fetch(event.request, { cf: { cacheKey: &quot;some-string&quot; } });&#10;</code></pre>
<p>Normally, Cloudflare computes the cache key for a request based on the request's URL. Sometimes, though, you may like different URLs to be treated as if they were the same for caching purposes. For example, if your website content is hosted from both Amazon S3 and Google Cloud Storage - you have the same content in both places, and you can use a Worker to randomly balance between the two. However, you do not want to end up caching two copies of your content. You could utilize custom cache keys to cache based on the original request URL rather than the subrequest URL:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16512.md")
</div></div>
<p>Workers operating on behalf of different zones cannot affect each other's cache. You can only override cache keys when making requests within your own zone (in the above example <code>event.request.url</code> was the key stored), or requests to hosts that are not on Cloudflare. When making a request to another Cloudflare zone (for example, belonging to a different Cloudflare customer), that zone fully controls how its own content is cached within Cloudflare; you cannot override it.</p>
<h2 id="cache-expected-vary-responses">Cache expected Vary responses</h2>
<p>Use <code>cf.vary</code> when an origin returns a <code>Vary</code> header and you want a Worker subrequest to cache expected variants. This setting applies only to the <code>fetch()</code> request where you set it.</p>
<p>For Vary behavior details, refer to <a href="/cache/concepts/vary/">Vary</a>. For the full request init object, refer to <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16513.md")
</div>
<h2 id="override-based-on-origin-response-code">Override based on origin response code</h2>
<pre><code class="language-js">// Force response to be cached for 86400 seconds for 200 status&#10;// codes, 1 second for 404, and do not cache 500 errors.&#10;fetch(request, {&#10;	cf: { cacheTtlByStatus: { &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 } },&#10;});&#10;</code></pre>
<p>This option is a version of the <code>cacheTtl</code> feature which chooses a TTL based on the response's status code and does not automatically set <code>cacheEverything: true</code>. If the response to this request has a status code that matches, Cloudflare will cache for the instructed time, and override cache directives sent by the origin. You can review <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties">details on the <code>cacheTtl</code> feature on the Request page</a>.</p>
<h2 id="customize-cache-behavior-based-on-request-file-type">Customize cache behavior based on request file type</h2>
<p>Using custom cache keys and overrides based on response code, you can write a Worker that sets the TTL based on the response status code from origin, and request file type.</p>
<p>The following example demonstrates how you might use this to cache requests for streaming media assets:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16516.md")
</div></div>
<h2 id="using-the-http-cache-api">Using the HTTP Cache API</h2>
<p>The <code>cache</code> mode can be set in <code>fetch</code> options.
Currently Workers only support the <code>no-store</code> and <code>no-cache</code> mode for controlling the cache.
When <code>no-store</code> is supplied the cache is bypassed on the way to the origin and the request is not cacheable.
When <code>no-cache</code> is supplied the cache is forced to revalidate the currently cached response with the
origin.</p>
<pre><code class="language-js">fetch(request, { cache: &#x27;no-store&#x27;});&#10;fetch(request, { cache: &#x27;no-cache&#x27;});&#10;</code></pre>
