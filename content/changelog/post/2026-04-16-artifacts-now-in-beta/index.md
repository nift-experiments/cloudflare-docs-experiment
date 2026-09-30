---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/
  description: New updates and improvements at Cloudflare.
  full_title: 'Artifacts now in beta: versioned filesystem with Git access · Changelog'
  head_html: '<title>Artifacts now in beta: versioned filesystem with Git access · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Artifacts now in beta: versioned filesystem with Git access · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/#page","headline":"Artifacts now in beta: versioned filesystem with Git access \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-16-artifacts-now-in-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 16, 2026</time><h2 id="post-title">Artifacts now in beta: versioned filesystem with Git access</h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p><a href="/artifacts/">Artifacts</a> is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.</p>
<p>You can <a href="https://blog.cloudflare.com/artifacts-git-for-agents-beta/">read the announcement blog</a> to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.</p>
<p>Artifacts has three API surfaces:</p>
<ul>
<li>Workers bindings (for creating and managing repositories)</li>
<li>REST API (for creating and managing repos from any other compute platform)</li>
<li>Git protocol (for interacting with repos)</li>
</ul>
<p>As an example: you can use the Workers binding to create a repo and read back its remote URL:</p>
<pre tabindex="0"><code class="language-ts">&#35; Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.&#10;const created = await env.PROD_ARTIFACTS.create(&quot;agent-007&quot;);&#10;const remote = (await created.repo.info())?.remote;&#10;</code></pre>
<p>Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos&quot; --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; --header &quot;Content-Type: application/json&quot; --data &#x27;{&quot;name&quot;:&quot;agent-007&quot;}&#x27;&#10;</code></pre>
<p>Any Git client that speaks smart HTTP can use the returned remote URL:</p>
<pre tabindex="0"><code class="language-bash">&#35; Agents know git.&#10;&#35; Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.&#10;git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git&#10;</code></pre>
<p>To learn more, refer to <a href="/artifacts/get-started/">Get started</a>, <a href="/artifacts/api/workers-binding/">Workers binding</a>, and <a href="/artifacts/api/git-protocol/">Git protocol</a>.</p>
</div></article></div>
