---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/
  description: New updates and improvements at Cloudflare.
  full_title: Cron triggers are now supported in Python Workers · Changelog
  head_html: <title>Cron triggers are now supported in Python Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cron triggers are now supported in Python Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/#page","headline":"Cron triggers are now supported in Python Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-04-22-python-worker-cron-triggers/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 24, 2025</time><h2 id="post-title">Cron triggers are now supported in Python Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create Python Workers which are executed via a cron trigger.</p>
<p>This is similar to how it's done in JavaScript Workers, simply define a scheduled event
listener in your Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import handler&#10;&#10;@handler&#10;async def on_scheduled(event, env, ctx):&#10;  print(&quot;cron processed&quot;)&#10;</code></pre>
<p>Define a cron trigger configuration in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17772.md")</div>
<p>Then test your new handler by using Wrangler with the <code>--test-scheduled</code> flag and
making a request to <code>/cdn-cgi/local/scheduled?cron=*+*+*+*+*</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Consult the <a href="/workers/configuration/cron-triggers/">Workers Cron Triggers page</a> for full details on cron triggers in Workers.</p>
</div></article></div>
