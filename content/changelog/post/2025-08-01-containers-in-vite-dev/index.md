---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/
  description: New updates and improvements at Cloudflare.
  full_title: Develop locally with Containers and the Cloudflare Vite plugin · Changelog
  head_html: <title>Develop locally with Containers and the Cloudflare Vite plugin · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Develop locally with Containers and the Cloudflare Vite plugin · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/#page","headline":"Develop locally with Containers and the Cloudflare Vite plugin \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-01-containers-in-vite-dev/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 1, 2025</time><h2 id="post-title">Develop locally with Containers and the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now configure and run <a href="/containers">Containers</a> alongside your <a href="/workers">Worker</a> during local development when using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. Previously, you could only develop locally when using <a href="/workers/wrangler/">Wrangler</a> as your local development server.</p>
<h4 id="configuration">Configuration</h4>
<p>You can simply configure your Worker and your Container(s) in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17782.md")</div>
<h4 id="worker-code">Worker Code</h4>
<p>Once your Worker and Containers are configured, you can access the Container instances from your Worker code:</p>
<pre tabindex="0"><code class="language-ts">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;  defaultPort = 4000; // Port the container is listening on&#10;  sleepAfter = &quot;10m&quot;; // Stop the instance if requests not sent for 10 minutes&#10;}&#10;&#10;async fetch(request, env) {&#10;  const { &quot;session-id&quot;: sessionId } = await request.json();&#10;  // Get the container instance for the given session ID&#10;  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)&#10;  // Pass the request to the container instance on its default port&#10;  return containerInstance.fetch(request);&#10;}&#10;</code></pre>
<h4 id="local-development">Local development</h4>
<p>To develop your Worker locally, start a local dev server by running</p>
<pre tabindex="0"><code class="language-sh">vite dev&#10;</code></pre>
<p>in your terminal.</p>
<h4 id="resources">Resources</h4>
<p>Learn more about <a href="https://developers.cloudflare.com/containers/">Cloudflare Containers</a> or the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a> in our developer docs.</p>
</div></article></div>
