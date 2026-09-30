---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/
  description: New updates and improvements at Cloudflare.
  full_title: Workers native integrations were removed from the Cloudflare dashboard · Changelog
  head_html: <title>Workers native integrations were removed from the Cloudflare dashboard · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers native integrations were removed from the Cloudflare dashboard · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/#page","headline":"Workers native integrations were removed from the Cloudflare dashboard \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-06-09-workers-integrations-changes/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 9, 2025</time><h2 id="post-title">Workers native integrations were removed from the Cloudflare dashboard</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers native integrations were <a href="https://blog.cloudflare.com/announcing-database-integrations/">originally launched in May 2023</a> to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The <strong>Integrations</strong> tab in the dashboard has been removed in favor of a more direct, command-line-based approach using <a href="/workers/wrangler/commands/general/#secret">Wrangler secrets</a>.</p>
<h4 id="what-s-changed">What's changed</h4>
<ul>
<li><strong>Integrations tab removed</strong>: The integrations setup flow is no longer available in the Workers dashboard.</li>
<li><strong>Manual secret configuration</strong>: New connections should be configured by adding credentials as secrets to your Workers using <code>npx wrangler secret put</code> commands.</li>
</ul>
<h4 id="impact-on-existing-integrations">Impact on existing integrations</h4>
<p><strong>Existing integrations will continue to work without any changes required.</strong> If you have integrations that were previously created through the dashboard, they will remain functional.</p>
<h4 id="updating-existing-integrations">Updating existing integrations</h4>
<p>If you'd like to modify your existing integration, you can update the secrets, environment variables, or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> that were created from the original integration setup.</p>
<ul>
<li><strong>Update secrets</strong>: Use <code>npx wrangler secret put &lt;SECRET_NAME&gt;</code> to update credential values.</li>
<li><strong>Modify environment variables</strong>: Update variables through the dashboard or Wrangler configuration.</li>
<li><strong>Dashboard management</strong>: Access your Worker's settings in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> to modify connections created by our removed native integrations feature.</li>
</ul>
<p>If you have previously set up an observability integration with <a href="https://sentry.io">Sentry</a>, the following environment variables were set and are still modifiable:</p>
<ul>
<li><code>BLOCKED_HEADERS</code>: headers to exclude sending to Sentry</li>
<li><code>EXCEPTION_SAMPLING_RATE</code>: number from 0 - 100, where 0 = no events go through to Sentry, and 100 = all events go through to Sentry</li>
<li><code>STATUS_CODES_TO_SAMPLING_RATES</code>: a map of status codes -- like 400 or with wildcards like 4xx -- to sampling rates described above</li>
</ul>
<h4 id="setting-up-new-database-and-observability-connections">Setting up new database and observability connections</h4>
<p>For new connections, refer to our step-by-step guides on connecting to popular database and observability providers including: <a href="/workers/observability/third-party-integrations/sentry">Sentry</a>, <a href="/workers/databases/third-party-integrations/turso/">Turso</a>, <a href="/workers/databases/third-party-integrations/neon/">Neon</a>, <a href="/workers/databases/third-party-integrations/supabase/">Supabase</a>, <a href="/workers/databases/third-party-integrations/planetscale/">PlanetScale</a>, <a href="/workers/databases/third-party-integrations/upstash/">Upstash</a>, <a href="/workers/databases/third-party-integrations/xata/">Xata</a>.</p>
</div></article></div>
