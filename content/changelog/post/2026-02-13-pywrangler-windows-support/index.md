---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/
  description: New updates and improvements at Cloudflare.
  full_title: Better Windows support for Python Workers · Changelog
  head_html: <title>Better Windows support for Python Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Better Windows support for Python Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/#page","headline":"Better Windows support for Python Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-13-pywrangler-windows-support/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">Better Windows support for Python Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a>, the CLI tool for managing Python Workers and packages,
now supports Windows, allowing you to develop and deploy Python Workers from Windows environments.
Previously, Pywrangler was only available on macOS and Linux.</p>
<p>You can install and use Pywrangler on Windows the same way you would on other platforms.
<a href="/workers/languages/python/packages/">Specify your Worker's Python dependencies</a> in your <code>pyproject.toml</code> file,
then use the following commands to develop and deploy:</p>
<pre tabindex="0"><code class="language-bash">uvx --from workers-py pywrangler dev&#10;uvx --from workers-py pywrangler deploy&#10;</code></pre>
<p>All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.</p>
<h4 id="requirements">Requirements</h4>
<p>This feature requires the following minimum versions:</p>
<ul>
<li><code>wrangler</code> &gt;= 4.64.0</li>
<li><code>workers-py</code> &gt;= 1.72.0</li>
<li><code>uv</code> &gt;= 0.29.8</li>
</ul>
<p>To upgrade <code>workers-py</code> (which includes Pywrangler) in your project, run:</p>
<pre tabindex="0"><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade <code>wrangler</code>, run:</p>
<pre tabindex="0"><code class="language-bash">npm install -g wrangler@latest&#10;</code></pre>
<p>To upgrade <code>uv</code>, run:</p>
<pre tabindex="0"><code class="language-bash">uv self update&#10;</code></pre>
<p>To get started with Python Workers on Windows, refer to the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler.</p>
</div></article></div>
