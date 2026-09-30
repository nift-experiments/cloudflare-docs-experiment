---
cp9:
  canonical: https://developers.cloudflare.com/kv/concepts/how-kv-works/
  description: Workers KV stores data centrally and caches it globally, optimizing for high-read, low-latency workloads.
  full_title: How KV works · Cloudflare Workers KV docs
  head_html: <title>How KV works · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers KV stores data centrally and caches it globally, optimizing for high-read, low-latency workloads."><link rel="canonical" href="https://developers.cloudflare.com/kv/concepts/how-kv-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/concepts/how-kv-works/index.md"><meta property="og:title" content="How KV works · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers KV stores data centrally and caches it globally, optimizing for high-read, low-latency workloads."><meta property="og:url" content="https://developers.cloudflare.com/kv/concepts/how-kv-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/concepts/how-kv-works/#page","headline":"How KV works \u00b7 Cloudflare Workers KV docs","description":"Workers KV stores data centrally and caches it globally, optimizing for high-read, low-latency workloads.","url":"https://developers.cloudflare.com/kv/concepts/how-kv-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/concepts/how-kv-works/
  schema: 1
---
<p>KV is a global, low-latency, key-value data store. It stores data in a small number of centralized data centers, then caches that data in Cloudflare's data centers after access.</p>
<p>KV supports exceptionally high read volumes with low latency, making it possible to build dynamic APIs that scale thanks to KV's built-in caching and global distribution.
Requests which are not in cache and need to access the central stores can experience higher latencies.</p>
<h2 id="write-data-to-kv-and-read-data-from-kv">Write data to KV and read data from KV</h2>
<p>When you write to KV, your data is written to central data stores. Your data is not sent automatically to every location's cache.</p>
<p><img src="/assets/upstream/images/kv/kv-write.svg" alt="Your data is written to central data stores when you write to KV." /></p>
<p>Initial reads from a location do not have a cached value. Data must be read from the nearest regional tier, followed by a central tier, degrading finally to the central stores for a truly cold global read. While the first access is slow globally, subsequent requests are faster, especially if requests are concentrated in a single region.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="hot-and-cold-read">Hot and cold read</h3>
@markup("md", "content/.markup/bodies/9528.md")
</aside>
<p><img src="/assets/upstream/images/kv/kv-slow-read.svg" alt="Initial reads will miss the cache and go to the nearest central data store first." /></p>
<p>Frequent reads from the same location return the cached value without reading from anywhere else, resulting in the fastest response times. KV operates diligently to update the cached values by refreshing from upper tier caches and central data stores before cache expires in the background.</p>
<p>Refreshing from upper tiers and the central data stores in the background is done carefully so that assets that are being accessed continue to be kept served from the cache without any stalls.</p>
<p><img src="/assets/upstream/images/kv/kv-fast-read.svg" alt="As mentioned above, frequent reads will return a cached value." /></p>
<p>KV is optimized for high-read applications. It stores data centrally and uses a hybrid push/pull-based replication to store data in cache. KV is suitable for use cases where you need to write relatively infrequently, but read quickly and frequently. Infrequently read values are pulled from other data centers or the central stores, while more popular values are cached in the data centers they are requested from.</p>
<h2 id="performance">Performance</h2>
<p>To improve KV performance, increase the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter"><code>cacheTtl</code> parameter</a> up from its default 60 seconds.</p>
<p>KV achieves high performance by <a href="https://www.cloudflare.com/en-gb/learning/cdn/what-is-caching/">caching</a> which makes reads eventually-consistent with writes.</p>
<p>Changes are usually immediately visible in the Cloudflare global network location at which they are made. Changes may take up to 60 seconds or more to be visible in other global network locations as their cached versions of the data time out.</p>
<p>Negative lookups indicating that the key does not exist are also cached, so the same delay exists noticing a value is created as when a value is changed.</p>
<h2 id="consistency">Consistency</h2>
<p>KV achieves high performance by being eventually-consistent. At the Cloudflare global network location at which changes are made, these changes are usually immediately visible. However, this is not guaranteed and therefore it is not advised to rely on this behaviour. In other global network locations changes may take up to 60 seconds or more to be visible as their cached versions of the data time-out.</p>
<p>Visibility of changes takes longer in locations which have recently read a previous version of a given key (including reads that indicated the key did not exist, which are also cached locally).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9527.md")
</aside>
<p>An approach to achieve write-after-write consistency is to send all of your writes for a given KV key through a corresponding instance of a Durable Object, and then read that value from KV in other Workers. This is useful if you need more control over writes, but are satisfied with KV's read characteristics described above.</p>
<h2 id="guidance">Guidance</h2>
<p>Workers KV is an eventually-consistent edge key-value store. That makes it ideal for <strong>read-heavy</strong>, highly cacheable workloads such as:</p>
<ul>
<li>Serving static assets</li>
<li>Storing application configuration</li>
<li>Storing user preferences</li>
<li>Implementing allow-lists/deny-lists</li>
<li>Caching</li>
</ul>
<p>In these scenarios, Workers are invoked in a data center closest to the user and Workers KV data will be cached in that region for subsequent requests to minimize latency.</p>
<p>If you have a <strong>write-heavy</strong> <a href="https://redis.io">Redis</a>-type workload where you are updating the same key tens or hundreds of times per second, KV will not be an ideal fit.
If you can revisit how your application writes to single key-value pairs and spread your writes across several discrete keys, Workers KV can suit your needs.
Alternatively, <a href="/durable-objects/">Durable Objects</a> provides a key-value API with higher writes per key rate limits.</p>
<h2 id="security">Security</h2>
<p>Refer to <a href="/kv/reference/data-security/">Data security documentation</a> to understand how Workers KV secures data.</p>
