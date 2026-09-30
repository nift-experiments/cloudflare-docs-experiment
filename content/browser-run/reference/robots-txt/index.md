---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/reference/robots-txt/
  description: Configure robots.txt rules and sitemaps to control how Browser Run accesses your website.
  full_title: robots.txt and sitemaps · Cloudflare Browser Run docs
  head_html: <title>robots.txt and sitemaps · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure robots.txt rules and sitemaps to control how Browser Run accesses your website."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/reference/robots-txt/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/reference/robots-txt/index.md"><meta property="og:title" content="robots.txt and sitemaps · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure robots.txt rules and sitemaps to control how Browser Run accesses your website."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/reference/robots-txt/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/reference/robots-txt/#page","headline":"robots.txt and sitemaps \u00b7 Cloudflare Browser Run docs","description":"Configure robots.txt rules and sitemaps to control how Browser Run accesses your website.","url":"https://developers.cloudflare.com/browser-run/reference/robots-txt/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/reference/robots-txt/
  schema: 1
---
<p>This page provides general guidance on configuring <code>robots.txt</code> and sitemaps for websites you plan to access with Browser Run.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="robots-txt-is-advisory-not-enforceable">robots.txt is advisory, not enforceable</h3>
@markup("md", "content/.markup/bodies/3583.md")
</aside>
<h2 id="identifying-browser-run-requests">Identifying Browser Run requests</h2>
<p>Requests can be identified by the <a href="/browser-run/reference/automatic-request-headers/">automatic headers</a> that Cloudflare attaches:</p>
<ul>
<li><a href="/browser-run/reference/automatic-request-headers/#user-agent">User-Agent</a>: Each Browser Run method has a different default User-Agent, which you can use to write targeted <code>robots.txt</code> rules</li>
<li><code>cf-brapi-request-id</code>: Unique identifier for Quick Actions requests</li>
<li><code>Signature-agent</code>: Pointer to Cloudflare's bot verification keys</li>
</ul>
<p>To allow or block Browser Run traffic using WAF rules instead of <code>robots.txt</code>, use the <a href="/browser-run/reference/automatic-request-headers/#bot-detection">bot detection IDs</a> on the automatic request headers page.</p>
<h2 id="best-practices-for-robots-txt">Best practices for robots.txt</h2>
<p>A well-configured <code>robots.txt</code> helps crawlers understand which parts of your site they can access.</p>
<h3 id="reference-your-sitemap">Reference your sitemap</h3>
<p>Include a reference to your sitemap in <code>robots.txt</code> so crawlers can discover your URLs:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;</code></pre>
<p>You can list multiple sitemaps:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;Sitemap: https://example.com/blog-sitemap.xml&#10;</code></pre>
<h3 id="set-a-crawl-delay">Set a crawl delay</h3>
<p>Use <code>crawl-delay</code> to control how frequently crawlers request pages from your server:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Crawl-delay: 2&#10;Allow: /&#10;&#10;Sitemap: https://example.com/sitemap.xml&#10;</code></pre>
<p>The value is in seconds. A <code>crawl-delay</code> of 2 means the crawler waits two seconds between requests.</p>
<h2 id="blocking-crawlers-with-robots-txt">Blocking crawlers with robots.txt</h2>
<p>If you want to prevent Browser Run (or other crawlers) from accessing your site, you can configure your <code>robots.txt</code> to restrict access.</p>
<h3 id="block-all-bots-from-your-entire-site">Block all bots from your entire site</h3>
<p>To prevent all crawlers from accessing any page on your site:</p>
<pre tabindex="0"><code class="language-txt">User-agent: *&#10;Disallow: /&#10;</code></pre>
<p>This is the most restrictive configuration and blocks all compliant bots, not just Browser Run.</p>
<h3 id="block-only-the-crawl-endpoint">Block only the /crawl endpoint</h3>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a> identifies itself with the User-Agent <code>CloudflareBrowserRenderingCrawler/1.0</code>. To block the <code>/crawl</code> endpoint while allowing all other traffic (including other Browser Run <a href="/browser-run/quick-actions/">Quick Actions</a> endpoints, which use a <a href="/browser-run/reference/automatic-request-headers/#user-agent">different User-Agent</a>):</p>
<pre tabindex="0"><code class="language-txt">User-agent: CloudflareBrowserRenderingCrawler&#10;Disallow: /&#10;&#10;User-agent: *&#10;Allow: /&#10;</code></pre>
<h3 id="block-the-crawl-endpoint-on-specific-paths">Block the /crawl endpoint on specific paths</h3>
<p>To allow the <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a> to access your site but block specific sections:</p>
<pre tabindex="0"><code class="language-txt">User-agent: CloudflareBrowserRenderingCrawler&#10;Disallow: /admin/&#10;Disallow: /private/&#10;Allow: /&#10;&#10;User-agent: *&#10;Allow: /&#10;</code></pre>
<h2 id="best-practices-for-sitemaps">Best practices for sitemaps</h2>
<p>Structure your sitemap to help crawlers process your site efficiently:</p>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;urlset xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;&#10;  &lt;url&gt;&#10;    &lt;loc&gt;https://example.com/important-page&lt;/loc&gt;&#10;    &lt;lastmod&gt;2025-01-15T00:00:00+00:00&lt;/lastmod&gt;&#10;    &lt;priority&gt;1.0&lt;/priority&gt;&#10;  &lt;/url&gt;&#10;  &lt;url&gt;&#10;    &lt;loc&gt;https://example.com/other-page&lt;/loc&gt;&#10;    &lt;lastmod&gt;2025-01-10T00:00:00+00:00&lt;/lastmod&gt;&#10;    &lt;priority&gt;0.5&lt;/priority&gt;&#10;  &lt;/url&gt;&#10;&lt;/urlset&gt;&#10;</code></pre>
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
<td>Required. Use full URLs.</td>
</tr>
<tr>
<td><code>&lt;lastmod&gt;</code></td>
<td>Last modification date</td>
<td>Include to help the crawler identify updated content. Use ISO 8601 format.</td>
</tr>
<tr>
<td><code>&lt;priority&gt;</code></td>
<td>Relative importance (0.0-1.0)</td>
<td>Set higher values for important pages. The crawler will process pages in priority order.</td>
</tr>
</tbody>
</table>
<h3 id="sitemap-index-files">Sitemap index files</h3>
<p>For large sites with multiple sitemaps, use a sitemap index file. Browser Run uses the <code>depth</code> parameter to control how many levels of nested sitemaps are crawled:</p>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;urlset xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;&#10;  ...&#10;&lt;/urlset&gt;&#10;&lt;sitemapindex xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;&#10;   &lt;sitemap&gt;&#10;      &lt;loc&gt;https://www.example.com/sitemap-products.xml&lt;/loc&gt;&#10;   &lt;/sitemap&gt;&#10;   &lt;sitemap&gt;&#10;      &lt;loc&gt;https://www.example.com/sitemap-blog.xml&lt;/loc&gt;&#10;   &lt;/sitemap&gt;&#10;&lt;/sitemapindex&gt;&#10;</code></pre>
<h3 id="caching-headers">Caching headers</h3>
<p>Browser Run periodically refetches sitemaps to keep content fresh. Serve your sitemap with <code>Last-Modified</code> or <code>ETag</code> response headers so the crawler can detect whether the sitemap has changed since the last fetch.</p>
<h3 id="recommendations">Recommendations</h3>
<ul>
<li>Include <code>&lt;lastmod&gt;</code> on all URLs to help identify which pages have changed. Use ISO 8601 format (for example, <code>2025-01-15T00:00:00+00:00</code>).</li>
<li>Use sitemap index files for large sites with multiple sitemaps.</li>
<li>Compress large sitemaps using <code>.gz</code> format to reduce bandwidth.</li>
<li>Keep sitemaps under 50 MB and 50,000 URLs per file (standard sitemap limits).</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/browser-run/faq/#will-browser-run-be-detected-by-bot-management">FAQ: Will Browser Run be detected by Bot Management?</a> — How Browser Run interacts with bot protection and how to create a WAF skip rule</li>
<li><a href="/browser-run/reference/automatic-request-headers/">Automatic request headers</a> — User-Agent strings and non-configurable headers used by Browser Run</li>
</ul>
