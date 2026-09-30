---
cp9:
  canonical: https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/
  description: Persist cached content in R2 storage to eliminate cache evictions.
  full_title: Cache Reserve · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Reserve · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Persist cached content in R2 storage to eliminate cache evictions."><link rel="canonical" href="https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/index.md"><meta property="og:title" content="Cache Reserve · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Persist cached content in R2 storage to eliminate cache evictions."><meta property="og:url" content="https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#page","headline":"Cache Reserve \u00b7 Cloudflare Cache (CDN) docs","description":"Persist cached content in R2 storage to eliminate cache evictions.","url":"https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/advanced-configuration/cache-reserve/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/3856.md")
</aside>
<p>Cache Reserve is a large, persistent data store <a href="/r2/">implemented on top of R2</a>. By pushing a single button in the dashboard, your website's cacheable content will be written to Cache Reserve.</p>
<p>In the same way that Tiered Cache builds a hierarchy of caches between your visitors and your origin, Cache Reserve serves as the ultimate upper-tier cache, that will reserve storage space for your assets for as long as you want. This ensures that your content is served from cache longer, shielding your origin from unneeded egress fees.</p>
<p><img src="/assets/upstream/images/cache/content-being-served.png" alt="Content served from origin and getting cached in Cache Reserve, and Edge Cache Data Centers (T1=upper-tier, T2=lower-tier) on its way back to the client" /></p>
<p>Content in Cache Reserve is considered fresh based on the <a href="/cache/how-to/edge-browser-cache-ttl/#edge-cache-ttl">Edge Cache TTL</a> setting, or your origin's <code>Cache-Control</code> headers if Edge Cache TTL is not set. After the freshness period expires, Cloudflare revalidates the asset with your origin the next time it is requested. This is the same behavior as in Cloudflare's regular CDN.</p>
<p>The retention period controls how long an asset stays in Cache Reserve before it is removed. Cache Reserve starts with a retention period of 30 days. If an asset is not requested within the retention period, it is removed from Cache Reserve. Requesting the asset resets the retention period.</p>
<p>Assets must <a href="#cache-reserve-asset-eligibility">meet certain criteria</a> to use Cache Reserve.</p>
<p>Cache Reserve is a usage-based product and <a href="#pricing">pricing</a> is detailed below. While Cache Reserve does require a paid plan, users can continue to use Cloudflare’s CDN (without Cache Reserve) for free.</p>
<h2 id="enable-cache-reserve">Enable Cache Reserve</h2>
<p>A paid Cache Reserve plan is required.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3859.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3855.md")
</aside>
<p>If you are an Enterprise customer and are interested in Cache Reserve, contact your account team to get help with your configuration.</p>
<h2 id="cache-reserve-asset-eligibility">Cache Reserve asset eligibility</h2>
<p>Not all assets are eligible for Cache Reserve. To be admitted into Cache Reserve, assets must:</p>
<ul>
<li>Be cacheable, according to Cloudflare's standard <a href="/cache/">cacheability factors</a>.</li>
<li>Have a freshness time-to-live (TTL) of at least 10 hours (set by any means such as Cache-Control / <a href="/cache/concepts/cache-control/">CDN-Cache-Control</a> origin response headers, <a href="/cache/how-to/edge-browser-cache-ttl/#edge-cache-ttl">Edge Cache TTL</a>, <a href="/cache/how-to/configure-cache-status-code/">Cache TTL By Status</a>, or <a href="/cache/how-to/cache-rules/">Cache Rules</a>),</li>
<li>Have a Content-Length response header.</li>
<li>When using <a href="/images/optimization/hosted-images/create-variants/">Image transformations</a>, original files are eligible for Cache Reserve, but resized file variants are not eligible because transformations happen after Cache Reserve in the response flow.</li>
</ul>
<h2 id="purge-behavior">Purge behavior</h2>
<p>To remove all data from Cache Reserve, refer to <a href="#cache-reserve-clear-button">Cache Reserve clear button</a>.</p>
<p>Note that <a href="/cache/how-to/purge-cache/">Purge Everything</a> performs a soft purge on Cache Reserve and does not update metadata set by <a href="/cache/how-to/cache-response-rules/">Cache Response Rules</a> (such as cache tags). To refresh that metadata, purge the individual asset or wait for it to fully expire.</p>
<h2 id="limits">Limits</h2>
<ul>
<li>Cache Reserve file limits are the same as <a href="/r2/platform/limits/">R2 limits</a>. Note that <a href="/cache/concepts/default-cache-behavior/#customization-options-and-limits">CDN cache limits</a> still apply. Assets larger than standard limits will not be stored in the standard CDN cache, so these assets will incur Cache Reserve operations costs far more frequently.</li>
<li>Origin Range requests are not supported at this time from Cache Reserve.</li>
<li><a href="/cache/advanced-configuration/vary-for-images/">Vary for images</a> is currently not compatible with Cache Reserve.</li>
<li>Requests to <a href="/r2/buckets/public-buckets/">R2 public buckets linked to a zone's domain</a> will not use Cache Reserve. Enabling Cache Reserve for the connected zone will use Cache Reserve only for requests not destined for the R2 bucket.</li>
<li>Cache Reserve makes requests for uncompressed content directly from the origin. Unlike the standard Cloudflare CDN, Cache Reserve does not include the <code>Accept-Encoding: gzip</code> header when sending requests to the origin.</li>
<li>Cache Reserve is bypassed when using the Cloudflare <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a> setup.</li>
</ul>
<h2 id="usage">Usage</h2>
<p>Like the standard CDN, Cache Reserve also uses the <code>cf-cache-status</code> header to indicate <a href="/cache/concepts/cache-responses/">cache response statuses</a> like <code>MISS</code>, <code>HIT</code>, and <code>REVALIDATED</code>. Cache Reserve cache misses and hits are factored into the dashboard's cache hit ratio.</p>
<p>Individual sampled requests that filled or were served by Cache Reserve are viewable via the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">CacheReserveUsed</a> Logpush field.</p>
<p>Cache Reserve monthly operations and storage usage are viewable in the dashboard.</p>
<h2 id="pricing">Pricing</h2>
<p>Cache Reserve charges based on the total volume of data stored, along with two classes of operations on that data:</p>
<ul>
<li><a href="/r2/pricing/#class-a-operations">Class A operations</a> which are more expensive and tend to mutate state.</li>
<li><a href="/r2/pricing/#class-b-operations">Class B operations</a> which tend to read existing state.</li>
</ul>
<p>In most cases, a Cache Reserve miss will result in both one class A and one class B operation, and a Cache Reserve hit will result in one class B operation. Assets larger than 1 GB will incur more operations proportional to their size.</p>
<h3 id="cache-reserve-pricing">Cache Reserve pricing</h3>
<table>
<tbody>
<th></th>
<th>Rates</th>
<tr>
<td>Storage</td>
<td>$0.015 / GB-month</td>
</tr>
<tr>
<td>Class A Operations (writes)</td>
<td>$4.50 / million requests</td>
</tr>
<tr>
<td>Class B Operations (reads)</td>
<td>$0.36 / million requests</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3854.md")
</aside>
<h3 id="storage-usage">Storage usage</h3>
<p>Storage is billed using gigabyte-month (GB-month) as the billing metric. A GB-month is calculated by recording total bytes stored for the duration of the month.</p>
<p>For example:</p>
<ul>
<li>Storing 1 GB for 30 days will be charged as 1 GB-month.</li>
<li>Storing 2 GB for 15 days will be charged as 1 GB-month.</li>
</ul>
<h3 id="operations">Operations</h3>
<p>Operations are performed by Cache Reserve on behalf of the user to write data from the origin to Cache Reserve and to pass that data downstream to other parts of Cloudflare’s network. These operations are managed internally by Cloudflare.</p>
<h4 id="class-a-operations-writes">Class A operations (writes)</h4>
<p>Class A operations are performed based on cache misses from Cloudflare’s CDN. When a request cannot be served from cache, it will be fetched from the origin and written to cache reserve as well as our edge caches on the way back to the visitor.</p>
<h4 id="class-b-operations-reads">Class B operations (reads)</h4>
<p>Class B operations are performed when data needs to be fetched from Cache Reserve to respond to a miss in the edge cache.</p>
<h4 id="purge">Purge</h4>
<p>Asset purges are free operations.</p>
<p>Cache Reserve will be instantly purged along with edge cache when you send a purge by URL request. Refer to <a href="/cache/how-to/purge-cache/">cache configurations</a> for details.</p>
<p>Other purge methods, such as purge by tag, host, prefix, or purge everything will force an attempt to <a href="/cache/concepts/cache-responses/#revalidated">revalidate</a> on the subsequent request for the Cache Reserve asset. Note that assets purged this way will still incur storage costs until their retention TTL expires.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3853.md")
</aside>
<h2 id="cache-reserve-billing-examples">Cache Reserve billing examples</h2>
<h4 id="example-1">Example 1</h4>
<p>Assuming 1,000 assets (each 1 GB) are written to Cache Reserve at the start of the month and each asset is read 1,000 times, the estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Billable Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Class B Operations</td>
<td>(1,000 assets) * (1,000 reads per asset)</td>
<td>1,000,000</td>
<td>$0.36</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>(1,000 assets) * (1 write per asset)</td>
<td>1,000</td>
<td>$4.50</td>
</tr>
<tr>
<td>Storage</td>
<td>(1,000 assets) * (1GB per asset)</td>
<td>1,000 GB-months</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td><strong>$19.86</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3852.md")
</aside>
<h4 id="example-2">Example 2</h4>
<p>Assuming 1,000,000 assets (each 1 MB) are in Cache Reserve, and:</p>
<ul>
<li>each asset expires and is rewritten into Cache Reserve 1 time per day</li>
<li>each asset is read 2 times per day</li>
</ul>
<p>the estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Billable Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Class B Operations</td>
<td>(1,000,000 assets) * (2 reads per day) * (30 days)</td>
<td>60,000,000</td>
<td>$21.60</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>(1,000,000 assets) * (1 write per day) * (30 days)</td>
<td>30,000,000</td>
<td>$135.00</td>
</tr>
<tr>
<td>Storage</td>
<td>(1,000,000 assets) * (1MB per asset)</td>
<td>1,000 GB-months</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td><strong>$171.60</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3851.md")
</aside>
<h2 id="tips-and-best-practices">Tips and best practices</h2>
<p>Cache Reserve is designed for use with <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> enabled for maximum origin shielding. Using Cache Reserve without Tiered Cache may result in higher storage operation costs. The Cloudflare dashboard will warn you if you try to enable Cache Reserve without Tiered Cache.</p>
<h2 id="cache-reserve-analytics">Cache Reserve Analytics</h2>
<p>Cache Reserve Analytics provides insights regarding your Cache Reserve usage. It allows you to check what content is stored in Cache Reserve, how often it is being accessed, how long it has been there and how much egress from your origin it is saving you.</p>
<p>In the <strong>Overview</strong> section, under <strong>Cache Reserve</strong>, you have access to the following metrics:</p>
<ul>
<li><strong>Egress savings (bandwidth)</strong> - is an estimation based on response bytes served from Cache Reserve that did not need to be served from your origin server. These are represented as cache hits.</li>
<li><strong>Requests served by Cache Reserve</strong> - is the number of requests served by Cache Reserve (total).</li>
<li><strong>Data storage summary</strong> - is based on a representative sample of requests. Refer to <a href="/analytics/graphql-api/sampling/">Sampling</a> for more details about how Cloudflare samples data.
<ul>
<li><strong>Current data stored</strong> - is the data stored (currently) over time.</li>
<li><strong>Aggregate storage usage</strong> - is the total of storage used for the selected timestamp.</li>
</ul>
</li>
<li><strong>Operations</strong> - Class A (writes) and Class B (reads) operations over time.</li>
</ul>
<h2 id="cache-reserve-clear-button">Cache Reserve clear button</h2>
<p>You can remove all data stored in Cache Reserve through the dashboard or via API. To clear your cache reserve:</p>
<ul>
<li>Cache Reserve must have already been enabled for the zone.</li>
<li>Cache Reserve needs to be off.</li>
</ul>
<p>Be aware that the deletion may take up to 24 hours to complete.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3862.md")
</div></div>
