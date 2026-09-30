---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/
  description: New updates and improvements at Cloudflare.
  full_title: SSH through Wrangler is now enabled by default for Containers · Changelog
  head_html: <title>SSH through Wrangler is now enabled by default for Containers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="SSH through Wrangler is now enabled by default for Containers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/#page","headline":"SSH through Wrangler is now enabled by default for Containers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-12-ssh-enabled-by-default/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 12, 2026</time><h2 id="post-title">SSH through Wrangler is now enabled by default for Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>SSH through Wrangler is now enabled by default for <a href="/containers/">Containers</a>. Previously, you had to set <code>ssh.enabled</code> to <code>true</code> in your Container configuration before you could connect.</p>
<p>This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account. You also need to add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> before anyone can connect, so enabling SSH alone does not grant access.</p>
<p>To connect, add a public key to your Container configuration and run <code>wrangler containers ssh &lt;INSTANCE_ID&gt;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17711.md")</div>
<p>To disable SSH, set <code>ssh.enabled</code> to <code>false</code> in your Container configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17712.md")</div>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div></article></div>
