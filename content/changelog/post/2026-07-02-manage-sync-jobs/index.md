---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/
  description: New updates and improvements at Cloudflare.
  full_title: Manage AI Search sync jobs with Wrangler CLI · Changelog
  head_html: <title>Manage AI Search sync jobs with Wrangler CLI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Manage AI Search sync jobs with Wrangler CLI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/#page","headline":"Manage AI Search sync jobs with Wrangler CLI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-02-manage-sync-jobs/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 2, 2026</time><h2 id="post-title">Manage AI Search sync jobs with Wrangler CLI</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>When you connect a <a href="/ai-search/configuration/data-source/">data source</a> to your <a href="/ai-search/">AI Search</a> instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from <a href="/ai-search/wrangler-commands/">Wrangler</a>.</p>
<p>For example, you can trigger a sync job from your CI/CD or automated pipelines with the <code>jobs create</code> command so your index refreshes when you push a change:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search jobs create my-instance&#10;</code></pre>
<p>This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed.
The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search jobs create</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs list</code></td>
<td>List sync jobs for an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs get</code></td>
<td>Get details for a job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs cancel</code></td>
<td>Cancel a running job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs logs</code></td>
<td>View log entries for a job</td>
</tr>
</tbody>
</table>
<p>All commands accept <code>--namespace</code>/<code>-n</code> (defaults to <code>default</code>) and <code>--json</code> for structured output that automation and AI agents can parse directly. The <code>list</code> and <code>logs</code> commands also support <code>--page</code> and <code>--per-page</code> for pagination, and <code>cancel</code> prompts for confirmation unless you pass <code>-y</code>/<code>--force</code>.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>
</div></article></div>
