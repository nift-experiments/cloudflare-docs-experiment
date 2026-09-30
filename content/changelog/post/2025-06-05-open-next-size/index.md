<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 6, 2025</time><h2 id="post-title">Performance and size optimization for the Cloudflare adapter for Open Next</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans <a href="https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead">to improve performance and size</a>.</p>
<p><code>@opennextjs/cloudflare</code> v1.2 released on June 5, 2025 delivers on these enhancements. By removing <code>babel</code> from the app code and dropping a dependency on <code>@ampproject/toolbox-optimizer</code>, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.</p>
<p>This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.</p>
<p>Users only need to update to the latest version of <code>@opennextjs/cloudflare</code> to automatically benefit from these improvements.</p>
<p>Note that we published <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">CVE-2005-6087</a> for a SSRF vulnerability in the <code>@opennextjs/cloudflare</code> package.
The vulnerability has been fixed from <code>@opennextjs/cloudflare</code> v1.3.0 onwards. Please update to any version after this one.</p>
</div></article></div>
