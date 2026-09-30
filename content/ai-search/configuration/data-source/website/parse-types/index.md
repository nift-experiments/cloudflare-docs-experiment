---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/
  description: Choose how AI Search finds pages on a website data source.
  full_title: Parse types · Cloudflare AI Search docs
  head_html: <title>Parse types · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose how AI Search finds pages on a website data source."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/index.md"><meta property="og:title" content="Parse types · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose how AI Search finds pages on a website data source."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#page","headline":"Parse types \u00b7 Cloudflare AI Search docs","description":"Choose how AI Search finds pages on a website data source.","url":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/data-source/website/parse-types/
  schema: 1
---
<p>The parse type controls how AI Search finds the pages to index on a <a href="/ai-search/configuration/data-source/website/">website data source</a>. AI Search supports two parse types.</p>
<table>
<thead>
<tr>
<th>Parse type</th>
<th>Page discovery</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sitemap</code> (default)</td>
<td>Reads the XML sitemaps declared in <code>robots.txt</code>, or the sitemap URLs you configure. Does not follow links.</td>
<td>Your site publishes a complete and current sitemap.</td>
</tr>
<tr>
<td><code>discover</code></td>
<td>Starts at the source URL and, by default, uses both your sitemaps and the links it finds on the pages it crawls.</td>
<td>Your site has no sitemap, or its sitemap does not cover every page you need.</td>
</tr>
</tbody>
</table>
<p>Set the parse type in <code>source_params.web_crawler.parse_type</code>. If you do not set it, AI Search uses <code>sitemap</code>.</p>
<p>Both parse types require a source URL on a domain that you have onboarded onto the same Cloudflare account. Refer to <a href="/fundamentals/manage-domains/add-site/">Onboard a domain</a> if your domain is not on Cloudflare yet.</p>
<h2 id="which-parse-type-to-use">Which parse type to use</h2>
<p>Both parse types can read your sitemaps, so the choice is not simply &quot;sitemap or links&quot;. <code>discover</code> defaults to a <a href="#discovery-source">discovery source</a> of <code>all</code>, which means it reads your sitemaps <strong>and</strong> follows links. What differs is how thoroughly each one uses the sitemap.</p>
<p>If your site publishes a sitemap that covers the pages you want indexed, prefer <code>sitemap</code>. It is the more reliable of the two, because:</p>
<ul>
<li><strong>Updates are driven by your sitemap.</strong> <code>sitemap</code> re-crawls a page when its <code>&lt;lastmod&gt;</code> date changes, so edits are picked up on the next sync. <code>discover</code> ignores <code>&lt;lastmod&gt;</code> and <code>&lt;changefreq&gt;</code> entirely and re-fetches on a fixed <a href="#cache-age">cache age</a> instead.</li>
<li><strong>Nothing is cut off.</strong> <code>discover</code> stops at the configured <a href="#page-limit-and-depth">page limit and depth</a>, so pages that sit deep in your link graph, or past the limit, can be skipped. <code>sitemap</code> indexes everything the sitemap lists.</li>
<li><strong>You control the order.</strong> <code>sitemap</code> indexes pages by their <code>&lt;priority&gt;</code> value, so your most important pages are indexed first if you hit an instance limit.</li>
<li><strong>You can narrow the crawl.</strong> <a href="#specific-sitemap">Specific sitemap</a> is not supported with <code>discover</code>.</li>
</ul>
<p>Choose <code>discover</code> when a sitemap is missing, incomplete, or stale.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3088.md")
</aside>
<h2 id="sitemap">Sitemap</h2>
<p>The <code>sitemap</code> parse type is the default. AI Search reads the XML sitemaps your site publishes to decide which pages to index, and re-crawls a page when its <code>&lt;lastmod&gt;</code> date changes.</p>
<h3 id="how-pages-are-found">How pages are found</h3>
<p>When you connect a domain, the crawler looks for your website's sitemap to determine which pages to visit:</p>
<ol>
<li>If you configure one or more custom sitemap URLs in the dashboard under <strong>Parser options</strong> &gt; <strong>Specific sitemap</strong>, AI Search crawls only those sitemap URLs.</li>
<li>Otherwise, the crawler checks <code>robots.txt</code> for listed sitemaps.</li>
<li>If no <code>robots.txt</code> is found, the crawler checks for a sitemap at <code>/sitemap.xml</code>.</li>
<li>If no sitemap is available, the domain cannot be crawled with the <code>sitemap</code> parse type. Use <a href="#discover"><code>discover</code></a> instead.</li>
</ol>
<h3 id="indexing-order">Indexing order</h3>
<p>If your sitemaps include <code>&lt;priority&gt;</code> attributes, AI Search reads all sitemaps and indexes pages based on each page's priority value, regardless of which sitemap the page is in.</p>
<p>If no <code>&lt;priority&gt;</code> is specified, pages are indexed in the order the sitemaps are provided, either from the configured custom sitemap URLs or from <code>robots.txt</code> from top to bottom.</p>
<p>AI Search supports <code>.gz</code> compressed sitemaps. Both <code>robots.txt</code> and sitemaps can use partial URLs.</p>
<h3 id="sync-and-updates">Sync and updates</h3>
<p>During scheduled or manual <a href="/ai-search/configuration/indexing/syncing/">sync jobs</a>, the crawler will check for changes to the <code>&lt;lastmod&gt;</code> attribute in your sitemap. If it has been changed to a date occurring after the last sync date, then the page is crawled, the updated version is stored, and the page is automatically reindexed so that your search results always reflect the latest content.</p>
<p>If the <code>&lt;lastmod&gt;</code> attribute is not defined, AI Search uses the <code>&lt;changefreq&gt;</code> attribute to determine how often to re-crawl the URL. If neither <code>&lt;lastmod&gt;</code> nor <code>&lt;changefreq&gt;</code> is defined, AI Search automatically crawls each link once a day.</p>
<h3 id="specific-sitemap">Specific sitemap</h3>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code> in the order they appear (top to bottom). If you do not want the crawler to index everything, or if your sitemap is hosted at a non-standard path, you can configure custom sitemap URLs in the dashboard under <strong>Parser options</strong> &gt; <strong>Specific sitemap</strong>.</p>
<p>When custom sitemap URLs are configured, AI Search uses those sitemap URLs instead of auto-discovering sitemaps from <code>robots.txt</code> or <code>/sitemap.xml</code>. You can add up to five sitemap URLs.</p>
<h3 id="robots-txt">robots.txt</h3>
<p>The AI Search crawler uses the user agent <code>Cloudflare-AI-Search</code>. Your <code>robots.txt</code> file should reference your sitemap and allow the crawler:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;</code></pre>
<p>You can list multiple sitemaps or use a sitemap index file:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;Sitemap: https://example.com/blog-sitemap.xml&#10;Sitemap: https://example.com/sitemap.xml.gz&#10;</code></pre>
<p>To block all other crawlers but allow only AI Search:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Disallow: /&#10;&#10;User-agent: Cloudflare-AI-Search&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;</code></pre>
<h3 id="sitemap-structure">Sitemap structure</h3>
<p>Structure your sitemap to give AI Search the information it needs to crawl efficiently:</p>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;urlset xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;&#10;  &lt;url&gt;&#10;    &lt;loc&gt;https://example.com/important-page&lt;/loc&gt;&#10;    &lt;lastmod&gt;2026-01-15&lt;/lastmod&gt;&#10;    &lt;changefreq&gt;weekly&lt;/changefreq&gt;&#10;    &lt;priority&gt;1.0&lt;/priority&gt;&#10;  &lt;/url&gt;&#10;  &lt;url&gt;&#10;    &lt;loc&gt;https://example.com/other-page&lt;/loc&gt;&#10;    &lt;lastmod&gt;2026-01-10&lt;/lastmod&gt;&#10;    &lt;changefreq&gt;monthly&lt;/changefreq&gt;&#10;    &lt;priority&gt;0.5&lt;/priority&gt;&#10;  &lt;/url&gt;&#10;&lt;/urlset&gt;&#10;</code></pre>
<p>Use these attributes to control crawling behavior:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Purpose</th>
<th>Recommendation</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;loc&gt;</code></td>
<td>URL of the page</td>
<td>Required. Use full or partial URLs.</td>
</tr>
<tr>
<td><code>&lt;lastmod&gt;</code></td>
<td>Last modification date</td>
<td>Include to enable change detection. AI Search re-crawls pages when this date changes.</td>
</tr>
<tr>
<td><code>&lt;changefreq&gt;</code></td>
<td>Expected change frequency</td>
<td>Use when <code>&lt;lastmod&gt;</code> is not available. Values: <code>always</code>, <code>hourly</code>, <code>daily</code>, <code>weekly</code>, <code>monthly</code>, <code>yearly</code>, <code>never</code>.</td>
</tr>
<tr>
<td><code>&lt;priority&gt;</code></td>
<td>Relative importance (0.0-1.0)</td>
<td>Set higher values for important pages. AI Search indexes pages in priority order.</td>
</tr>
</tbody>
</table>
<p>You can also use a Sitemap Index to bundle other domain-specific sitemaps:</p>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;sitemapindex xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;&#10;  &lt;sitemap&gt;&#10;    &lt;loc&gt;https://www.example.com/sitemap-blog.xml&lt;/loc&gt;&#10;    &lt;lastmod&gt;2024-08-15T10:00:00+00:00&lt;/lastmod&gt;&#10;  &lt;/sitemap&gt;&#10;  &lt;sitemap&gt;&#10;    &lt;loc&gt;https://www.example.com/sitemap-docs.xml&lt;/loc&gt;&#10;    &lt;lastmod&gt;2024-08-10T12:00:00+00:00&lt;/lastmod&gt;&#10;  &lt;/sitemap&gt;&#10;&lt;/sitemapindex&gt;&#10;</code></pre>
<p>When parsing a Sitemap Index, AI Search collects all child sitemaps and then crawls them recursively, collecting all relevant URLs present in your sitemaps.</p>
<h3 id="sitemap-recommendations">Sitemap recommendations</h3>
<ul>
<li>Include <code>&lt;lastmod&gt;</code> on all URLs to enable efficient change detection during syncs.</li>
<li>Set <code>&lt;priority&gt;</code> to control indexing order. Pages with higher priority are indexed first.</li>
<li>Use <code>&lt;changefreq&gt;</code> as a fallback when <code>&lt;lastmod&gt;</code> is not available.</li>
<li>Use sitemap index files for large sites with multiple sitemaps.</li>
<li>Compress large sitemaps using <code>.gz</code> format to reduce bandwidth.</li>
<li>Keep sitemaps under 50MB and 50,000 URLs per file (standard sitemap limits).</li>
</ul>
<h2 id="discover">Discover</h2>
<p>The <code>discover</code> parse type delegates page discovery to the Browser Run <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>. AI Search starts a crawl job at your source URL and stores every page it fetches in <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>.</p>
<p>By default, <code>discover</code> collects candidate URLs from both your sitemaps and the links on the pages it crawls. Use the <a href="#discovery-source">discovery source</a> option to restrict it to one or the other.</p>
<p>Because <code>discover</code> does not depend on a sitemap, it reaches pages that a sitemap omits.</p>
<h3 id="how-discovery-works">How discovery works</h3>
<ol>
<li>AI Search starts a crawl job at the source URL.</li>
<li>The crawler collects candidate URLs from sitemaps, from links on crawled pages, or from both, depending on the discovery source.</li>
<li>The crawler follows links up to the configured depth and stops once it reaches the page limit.</li>
<li>Each fetched page is stored in built-in storage, converted to Markdown, chunked, and indexed.</li>
</ol>
<p>The crawler identifies itself as <code>Cloudflare-AI-Search</code> on domains in your Cloudflare account. If you enable <a href="#external-links-and-subdomains">external links or subdomains</a> and the crawl reaches a domain outside your account, it identifies itself as <code>Cloudflare-AI-Search-External</code>. Pages that <code>robots.txt</code> disallows are recorded with the <code>blocked_by_robots_txt</code> <a href="/ai-search/troubleshooting/indexing-error-codes/">indexing error code</a> instead of being indexed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3087.md")
</aside>
<h3 id="configure-in-the-dashboard">Configure in the dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3089.md")
</div>
<p>To change these options later, select your instance, open the <strong>Settings</strong> tab, and edit <strong>Crawl options</strong> under <strong>Parser options</strong>. Saving the change starts a new indexing job that reindexes every item.</p>
<h3 id="configure-with-the-api">Configure with the API</h3>
<p>Set <code>parse_type</code> to <code>discover</code>, then pass any non-default settings in <code>discover_options</code>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_type&quot;: &quot;discover&quot;,&#10;        &quot;discover_options&quot;: {&#10;          &quot;source&quot;: &quot;links&quot;,&#10;          &quot;limit&quot;: 5000,&#10;          &quot;depth&quot;: 3,&#10;          &quot;max_age&quot;: 86400,&#10;          &quot;include_subdomains&quot;: true&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="discover-options">Discover options</h3>
<p>The following options apply only when <code>parse_type</code> is <code>discover</code>. All of them are optional.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Range or values</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>source</code></td>
<td>string</td>
<td><code>all</code></td>
<td><code>all</code>, <code>sitemaps</code>, <code>links</code></td>
<td>Where the crawler looks for candidate URLs.</td>
</tr>
<tr>
<td><code>limit</code></td>
<td>number</td>
<td><code>100000</code></td>
<td>1 to 100,000</td>
<td>Maximum number of pages to crawl.</td>
</tr>
<tr>
<td><code>depth</code></td>
<td>number</td>
<td><code>5</code></td>
<td>1 to 100,000</td>
<td>Maximum number of link hops to follow from the source URL.</td>
</tr>
<tr>
<td><code>max_age</code></td>
<td>number</td>
<td><code>86400</code></td>
<td>0 to 604,800 seconds</td>
<td>How long the crawler reuses cached page content before it re-fetches.</td>
</tr>
<tr>
<td><code>include_external_links</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td><code>true</code>, <code>false</code></td>
<td>Whether to follow links that point to other domains.</td>
</tr>
<tr>
<td><code>include_subdomains</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td><code>true</code>, <code>false</code></td>
<td>Whether to follow links that point to subdomains of the source URL.</td>
</tr>
</tbody>
</table>
<h4 id="discovery-source">Discovery source</h4>
<p>The <code>source</code> option selects where candidate URLs come from:</p>
<ul>
<li><code>all</code>: Uses both sitemaps and links found on crawled pages.</li>
<li><code>sitemaps</code>: Uses only URLs listed in sitemaps.</li>
<li><code>links</code>: Uses only links found on crawled pages.</li>
</ul>
<p>Use <code>links</code> when your sitemap is missing or unreliable. Use <code>sitemaps</code> when you want sitemap coverage without following in-page links.</p>
<h4 id="page-limit-and-depth">Page limit and depth</h4>
<p>The <code>limit</code> option caps the number of pages the crawler indexes, up to a maximum of <code>100000</code>. Values above that maximum are rejected when you create or update the instance. Your <a href="/ai-search/platform/limits-pricing/">instance object limit</a> still applies, so the effective cap is whichever value is lower.</p>
<p>The <code>depth</code> option caps how far the crawler travels from the source URL. A depth of <code>1</code> crawls only the pages linked directly from the source URL.</p>
<h4 id="cache-age">Cache age</h4>
<p>The <code>max_age</code> option sets the maximum age, in seconds, of cached page content that the crawler accepts before it re-fetches the page from your origin. Set it to <code>0</code> to always fetch from the origin.</p>
<p>In the dashboard, <strong>Max cache age</strong> offers <strong>No cache</strong>, <strong>1 hour</strong>, <strong>1 day</strong>, <strong>3 days</strong>, and <strong>7 days</strong>.</p>
<h4 id="external-links-and-subdomains">External links and subdomains</h4>
<p>By default, the crawler stays on the host of the source URL. Enable <code>include_subdomains</code> to follow links into subdomains, and <code>include_external_links</code> to follow links to other domains.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3086.md")
</aside>
<h3 id="sync-behavior">Sync behavior</h3>
<p>Each <a href="/ai-search/configuration/indexing/syncing/">sync job</a> starts a new crawl job. AI Search reindexes the pages the crawl returns, and removes pages it can no longer reach.</p>
<p>If a crawl does not finish, or if it stops at the page limit, AI Search keeps the pages it indexed previously rather than deleting the pages that crawl did not reach.</p>
<p><code>discover</code> does not read the <code>&lt;lastmod&gt;</code> or <code>&lt;changefreq&gt;</code> sitemap attributes. Use <code>max_age</code> to control how often the crawler returns to your origin.</p>
<h3 id="unsupported-options">Unsupported options</h3>
<p><code>parse_options.specific_sitemaps</code> is only valid when <code>parse_type</code> is <code>sitemap</code>. Sending it with <code>discover</code> returns a validation error.</p>
<h2 id="options-that-apply-to-both-parse-types">Options that apply to both parse types</h2>
<p>The following website settings apply whichever parse type you choose:</p>
<ul>
<li><a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a>: Include and exclude URL patterns. Excluded pages are never fetched.</li>
<li><a href="/ai-search/configuration/data-source/website/content-selectors/">Content selectors</a>: Restrict indexing to the elements a CSS selector matches.</li>
<li><a href="/ai-search/configuration/data-source/website/authentication-headers/">Authentication headers</a>: Custom HTTP headers sent with each request.</li>
<li><a href="/ai-search/configuration/data-source/website/custom-metadata/">Custom metadata</a>: Metadata extracted from <code>&lt;meta&gt;</code> tags.</li>
<li><a href="/ai-search/configuration/data-source/website/#rendering-mode">Rendering mode</a>: Whether pages load in a headless browser.</li>
</ul>
<h2 id="limits">Limits</h2>
<p>A <code>discover</code> crawl indexes at most 100,000 pages and follows at most 100,000 link hops from the source URL, set with <a href="#page-limit-and-depth"><code>limit</code> and <code>depth</code></a>.</p>
<p>The <a href="/ai-search/platform/limits-pricing/#limits">files per instance</a> limit also applies, so the effective cap is whichever value is lower. For every limit that applies to website data sources, refer to <a href="/ai-search/configuration/data-source/website/#limits">Website</a>.</p>
