<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/13860.md")
</aside>
<p>Cache Reserve is a large, persistent data store <a href="/r2/">implemented on top of R2</a>. By pushing a single button in the dashboard, your website's cacheable content will be written to Cache Reserve.</p>
<p>In the same way that Tiered Cache builds a hierarchy of caches between your visitors and your origin, Cache Reserve serves as the ultimate upper-tier cache, that will reserve storage space for your assets for as long as you want. This ensures that your content is served from cache longer, shielding your origin from unneeded egress fees.</p>
<p>Smart Shield Advanced includes 2 TB of storage for Cache Reserve.</p>
<h2 id="asset-eligibility">Asset eligibility</h2>
<p>Not all assets are eligible for Cache Reserve. To be admitted into Cache Reserve, assets must:</p>
<ul>
<li>Be cacheable, according to Cloudflare's standard <a href="/cache/">cacheability factors</a>.</li>
<li>Have a freshness time-to-live (TTL) of at least 10 hours (set by any means such as Cache-Control / <a href="/cache/concepts/cache-control/">CDN-Cache-Control</a> origin response headers, <a href="/cache/how-to/edge-browser-cache-ttl/#edge-cache-ttl">Edge Cache TTL</a>, <a href="/cache/how-to/configure-cache-status-code/">Cache TTL By Status</a>, or <a href="/cache/how-to/cache-rules/">Cache Rules</a>),</li>
<li>Have a Content-Length response header.</li>
<li>When using <a href="/images/optimization/hosted-images/create-variants/">Image transformations</a>, original files are eligible for Cache Reserve, but resized file variants are not eligible because transformations happen after Cache Reserve in the response flow.</li>
</ul>
<h2 id="limits">Limits</h2>
<ul>
<li>Cache Reserve file limits are the same as <a href="/r2/platform/limits/">R2 limits</a>. Note that <a href="/cache/concepts/default-cache-behavior/#customization-options-and-limits">CDN cache limits</a> still apply. Assets larger than standard limits will not be stored in the standard CDN cache, so these assets will incur Cache Reserve operations costs far more frequently.</li>
<li>Origin Range requests are not supported at this time from Cache Reserve.</li>
<li><a href="/cache/advanced-configuration/vary-for-images/">Vary for images</a> is currently not compatible with Cache Reserve.</li>
<li>Requests to <a href="/r2/buckets/public-buckets/">R2 public buckets linked to a zone's domain</a> will not use Cache Reserve. Enabling Cache Reserve for the connected zone will use Cache Reserve only for requests not destined for the R2 bucket.</li>
<li>Cache Reserve makes requests for uncompressed content directly from the origin. Unlike the standard Cloudflare CDN, Cache Reserve does not include the <code>Accept-Encoding: gzip</code> header when sending requests to the origin.</li>
<li>Cache Reserve is bypassed when using the Cloudflare <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a> setup.</li>
</ul>
<h2 id="delete-data">Delete data</h2>
<p>You can remove all data stored in Cache Reserve. In most cases, deletion takes around 24 hours to be completed.</p>
<ol>
<li>Select the three dots next to Cache Reserve in your Smart Shield configurations.</li>
<li>Choose <strong>View details</strong> to open the Cache Reserve sidebar.</li>
<li>Make sure to pause Cache Reserve.</li>
<li>Select <strong>Delete data</strong> and then <strong>Save</strong>.</li>
<li>Select <strong>Delete</strong> again in the dialog to confirm.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13859.md")
</aside>
