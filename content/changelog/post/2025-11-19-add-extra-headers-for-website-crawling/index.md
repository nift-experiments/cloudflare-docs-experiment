<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 19, 2025</time><h2 id="post-title">AI Search support for crawling login protected website content</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/authentication-headers/">custom HTTP headers</a> for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.</p>
<p>Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.</p>
<p>This is particularly useful for indexing content like:</p>
<ul>
<li><strong>Internal documentation</strong> behind corporate login systems</li>
<li><strong>Premium content</strong> that requires users to provide access to unlock</li>
<li><strong>Sites protected by Cloudflare Access</strong> using service tokens</li>
</ul>
<p>To add custom headers when creating an AI Search instance, select <strong>Parse options</strong>. In the <strong>Extra headers</strong> section, you can add up to five custom headers per Website data source.</p>
<p><img src="/assets/upstream/images/ai-search/ai-search-extra-headers.png" alt="Custom headers configuration in AI Search" /></p>
<p>For example, to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you can add service token credentials as custom headers:</p>
<pre><code>CF-Access-Client-Id: your-token-id.access&#10;CF-Access-Client-Secret: your-token-secret&#10;</code></pre>
<p>The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.</p>
<p>Learn more about <a href="/ai-search/configuration/data-source/website/authentication-headers/">configuring custom headers for website crawling</a> in AI Search.</p>
</div></article></div>
