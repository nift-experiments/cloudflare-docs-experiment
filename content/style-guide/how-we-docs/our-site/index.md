<p>We use a variety of tools to make our docs site work. You could use these tools to build up your own docs site and - in most cases - do so for free or starting on a free tier.</p>
<h2 id="content-management-system">Content management system</h2>
<p>Our content lives in a public GitHub repository, <a href="https://github.com/cloudflare/cloudflare-docs"><code>cloudflare-docs</code></a>.</p>
<p>GitHub offers a generous <a href="https://github.com/pricing">free tier</a>.</p>
<h2 id="search">Search</h2>
<p>We use Cloudflare's <a href="/ai-search/">AI Search</a> as our search provider.</p>
<p>We used to use Algolia, which is also great for open-source docs because you can be part of the free <a href="https://docsearch.algolia.com/">DocSearch program</a>.</p>
<h2 id="site-framework">Site framework</h2>
<p>We use <a href="https://nimbus-docs.com/">Nimbus</a> for our docs, a documentation framework built on <a href="https://astro.build/">Astro</a>.</p>
<p>Nimbus's component <a href="https://nimbus-docs.com/registry/">registry</a> and <a href="https://nimbus-docs.com/writing/linting/">linting</a> system have exponentially increased our <a href="/style-guide/build-the-page/components/">site's capabilities</a> (without much extra work).</p>
<h2 id="builds">Builds</h2>
<p>We use <a href="https://github.com/features/actions">GitHub Actions</a> to build our site, which is then <a href="#hosting">hosted</a> on Cloudflare.</p>
<p>We are moving to <a href="/workers/ci-cd/">Workers CI/CD</a>, which currently runs in the background.</p>
<p>Both of these options include a free tier.</p>
<h2 id="hosting">Hosting</h2>
<p>We host our content using <a href="/workers/static-assets/">Cloudflare Workers</a>, specifically using their built in values for <a href="/workers/framework-guides/web-apps/astro/">Astro sites</a></p>
<p>Workers offers a generous <a href="/workers/platform/pricing/">free tier</a>.</p>
<h2 id="analytics">Analytics</h2>
<p>We send analytics to multiple destinations using <a href="/zaraz/">Cloudflare Zaraz</a>, which has a generous <a href="/zaraz/pricing-info/">free tier</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14607.md")
</aside>
