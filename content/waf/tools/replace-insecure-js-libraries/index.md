<p>This feature, when turned on, automatically rewrites URLs to external JavaScript libraries to point to Cloudflare-hosted libraries instead. This change improves security and performance, and reduces the risk of malicious code being injected.</p>
<p>This rewrite operation currently supports the <code>polyfill</code> JavaScript library hosted in <code>polyfill.io</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15339.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When turned on, Cloudflare will check HTTP(S) proxied traffic for <code>script</code> tags with an <code>src</code> attribute pointing to a potentially insecure service and replace the <code>src</code> value with the equivalent link hosted under <a href="https://cdnjs.cloudflare.com/">cdnjs</a>.</p>
<p>The rewritten URL will keep the original URL scheme (<code>http://</code> or <code>https://</code>).</p>
<p>For <code>polyfill.io</code> URL rewrites, all <code>3.*</code> versions of the <code>polyfill</code> library are supported under the <code>/v3</code> path. Additionally, the <code>/v2</code> path is also supported. If an unknown version is requested under the <code>/v3</code> path, Cloudflare will rewrite the URL to use the latest <code>3.*</code> version of the library (currently <code>3.111.0</code>).</p>
<h2 id="availability">Availability</h2>
<p>The feature is available in all Cloudflare plans, and is turned on by default on Free plans.</p>
<hr />
<h2 id="configure">Configure</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15343.md")
</div></div>
<hr />
<h2 id="final-remarks">Final remarks</h2>
<p>Since <a href="/pages/configuration/preview-deployments/"><code>pages.dev</code> zones</a> are on a Free plan, the <strong>Replace insecure JavaScript libraries</strong> feature is turned on by default on these zones and it is not possible to turn it off.</p>
