<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 9, 2026</time><h2 id="post-title">AI Search now with more granular controls over indexing</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>Get your content updates into <a href="/ai-search/">AI Search</a> faster and avoid a full rescan when you do not need it.</p>
<h4 id="reindex-individual-files-without-a-full-sync">Reindex individual files without a full sync</h4>
<p>Updated a file or need to retry one that errored? When you know exactly which file changed, you can now <a href="/ai-search/configuration/indexing/syncing/#controls">reindex it directly</a> instead of rescanning your entire data source.</p>
<p>Go to <strong>Overview</strong> &gt; <strong>Indexed Items</strong> and select the sync icon next to any file to reindex it immediately.</p>
<p><img src="/assets/upstream/images/ai-search/individual-file-indexing.png" alt="Sync individual files from Indexed Items" /></p>
<h4 id="crawl-only-the-sitemap-you-need">Crawl only the sitemap you need</h4>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code>, up to the <a href="/ai-search/platform/limits-pricing/#limits">maximum files per index limit</a>. If your site has multiple sitemaps but you only want to index a specific set, you can now <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specify a single sitemap URL</a> to limit what the crawler visits.</p>
<p>For example, if your <code>robots.txt</code> lists both <code>blog-sitemap.xml</code> and <code>docs-sitemap.xml</code>, you can specify just <code>https://example.com/docs-sitemap.xml</code> to index only your documentation.</p>
<p>Configure your selection anytime in <strong>Settings</strong> &gt; <strong>Parsing options</strong> &gt; <strong>Specific sitemaps</strong>, then trigger a sync to apply the changes.</p>
<p><img src="/assets/upstream/images/ai-search/specify-sitemap.png" alt="Specify a sitemap in Parsinh options" /></p>
<p>Learn more about <a href="/ai-search/configuration/indexing/syncing/#controls">indexing controls</a> and <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">website crawling configuration</a>.</p>
</div></article></div>
