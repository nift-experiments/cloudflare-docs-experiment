<p>You can connect a website you own as a data source for your AI Search instance. AI Search crawls and indexes the pages automatically.</p>
<p>You can only crawl domains that you have onboarded onto the same Cloudflare account. Refer to <a href="/fundamentals/manage-domains/add-site/">Onboard a domain</a> for more information on adding a domain to your Cloudflare account.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="bot-protection-may-block-crawling">Bot protection may block crawling</h3>
@markup("md", "content/.markup/bodies/3091.md")
</aside>
<h2 id="get-started">Get started</h2>
<p>You can connect a website when creating a new instance through the <a href="/ai-search/get-started/dashboard/">dashboard</a>, the <a href="/ai-search/get-started/api/">REST API</a>, or <a href="/ai-search/get-started/wrangler/">Wrangler</a>. Website is an optional data source that you can add alongside <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>.</p>
<h2 id="how-website-crawling-works">How website crawling works</h2>
<p>AI Search finds the pages on your site, fetches each one, converts it to Markdown, splits it into chunks, and adds it to the index. The <a href="/ai-search/configuration/data-source/website/parse-types/">parse type</a> controls how pages are found:</p>
<ul>
<li><strong>Sitemap</strong> (default): reads the XML sitemaps your site publishes.</li>
<li><strong>Discover</strong>: starts at the source URL and, by default, uses both your sitemaps and the links it finds on the pages it crawls.</li>
</ul>
<p>Refer to <a href="/ai-search/configuration/data-source/website/parse-types/">Parse types</a> for how each type finds pages, how each one handles sitemaps and syncing, and which settings apply to only one of them.</p>
<h2 id="storage">Storage</h2>
<p>Crawled pages are stored in built-in storage automatically.</p>
<p>To see the items parsed from your website, <a href="/ai-search/api/items/workers-binding/#itemslist">list the instance's items</a> with the Items API, or open the <strong>Items</strong> tab in the dashboard (<strong>AI</strong> &gt; <strong>AI Search</strong> &gt; your instance &gt; <strong>Items</strong>).</p>
<h2 id="configuration">Configuration</h2>
<p>Configure these options during onboarding, or later in your instance settings under <strong>Parser options</strong>.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#path-filtering">Path filtering</a></td>
<td>Include and exclude URL patterns that decide which pages are crawled.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/parse-types/">Parse type</a></td>
<td>How the crawler finds pages. <strong>Sitemap</strong> reads your XML sitemaps. <strong>Discover</strong> starts at the source URL and, by default, uses both your sitemaps and the links it finds.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">Specific sitemap</a></td>
<td>Crawl a set of sitemap URLs that you choose instead of the ones AI Search discovers. Up to five URLs. Applies to the sitemap parse type only.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/parse-types/#discover-options">Discover options</a></td>
<td>Discovery source, page limit, crawl depth, cache age, and whether to follow external links and subdomains. Applies to the discover parse type only.</td>
</tr>
<tr>
<td><a href="#rendering-mode">Rendering mode</a></td>
<td>Whether pages are downloaded as raw HTML or loaded in a headless browser first.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/authentication-headers/">Authentication headers</a></td>
<td>Custom HTTP headers sent with each request, so the crawler can reach pages behind authentication. Up to five headers.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/content-selectors/">Content selectors</a></td>
<td>Restrict indexing to the elements that a CSS selector matches, so you skip navigation, sidebars, and footers.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/custom-metadata/">Custom metadata</a></td>
<td>Values extracted from the <code>&lt;meta&gt;</code> tags in each page's <code>&lt;head&gt;</code>, stored alongside the indexed content.</td>
</tr>
</tbody>
</table>
<h3 id="path-filtering">Path filtering</h3>
<p>You can control which pages get indexed by defining include and exclude rules for URL paths. Use this to limit indexing to specific sections of your site or to exclude content you do not want searchable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3090.md")
</aside>
<p>For example, to index only blog posts while excluding drafts:</p>
<ul>
<li><strong>Include:</strong> <code>**/blog/**</code></li>
<li><strong>Exclude:</strong> <code>**/blog/drafts/**</code></li>
</ul>
<p>Refer to <a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a> for pattern syntax, filtering behavior, and more examples.</p>
<p>For supported file types and size limits, refer to <a href="/ai-search/configuration/data-source/#supported-file-types">Data source</a>.</p>
<h3 id="rendering-mode">Rendering mode</h3>
<p>You can choose how pages are parsed during crawling:</p>
<ul>
<li><strong>Static sites</strong>: Downloads the raw HTML for each page.</li>
<li><strong>Rendered sites</strong>: Loads pages with a headless browser and downloads the fully rendered version, including dynamic JavaScript content.</li>
</ul>
<h2 id="allow-ai-search-through-waf">Allow AI Search through WAF</h2>
<p>If you have Security rules configured to block bot activity on your own site, you can add a rule to allowlist the AI Search bot. Refer to <a href="https://radar.cloudflare.com/bots/directory/cloudflare-ai-search">AI Search in the Cloudflare Radar bot directory</a> for its verified identity and user agent.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3092.md")
</div>
<h2 id="limits">Limits</h2>
<p>The regular AI Search <a href="/ai-search/platform/limits-pricing/">limits</a> apply when using the Website data source. The following limits apply to website data sources on both Workers plans:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pages per crawl, <a href="/ai-search/configuration/data-source/website/parse-types/#discover"><code>discover</code> parse type</a></td>
<td>100,000</td>
</tr>
<tr>
<td>Crawl depth, <a href="/ai-search/configuration/data-source/website/parse-types/#page-limit-and-depth"><code>discover</code> parse type</a></td>
<td>100,000 link hops (defaults to 5)</td>
</tr>
<tr>
<td>Cached page age, <a href="/ai-search/configuration/data-source/website/parse-types/#cache-age"><code>discover</code> parse type</a></td>
<td>604,800 seconds (7 days)</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">Specific sitemap</a> URLs</td>
<td>5 per instance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/authentication-headers/">Authentication headers</a></td>
<td>5 per instance</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/content-selectors/">Content selector</a> entries</td>
<td>10 per instance</td>
</tr>
<tr>
<td>Content selector path pattern and selector length</td>
<td>200 characters each</td>
</tr>
</tbody>
</table>
<p>The <a href="/ai-search/platform/limits-pricing/#limits">files per instance</a> limit also applies, so the effective cap is whichever value is lower. The crawler indexes the first pages it visits until it reaches that cap, and any file it downloads that exceeds the maximum file size is not indexed.</p>
