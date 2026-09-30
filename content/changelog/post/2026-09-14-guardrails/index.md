---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/
  description: New updates and improvements at Cloudflare.
  full_title: Control which hostnames Browser Run sessions can access · Changelog
  head_html: <title>Control which hostnames Browser Run sessions can access · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Control which hostnames Browser Run sessions can access · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/#page","headline":"Control which hostnames Browser Run sessions can access \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-14-guardrails/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 14, 2026</time><h2 id="post-title">Control which hostnames Browser Run sessions can access</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now supports <a href="/browser-run/features/guardrails/">guardrails</a>, which limit a browser session's HTTP and HTTPS requests to permitted hostnames.</p>
<p>Use guardrails when you need to:</p>
<ul>
<li>Keep a browser workflow limited to a specific website and its subdomains.</li>
<li>Load only known third-party APIs, scripts, images, and fonts.</li>
<li>Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.</li>
</ul>
<p>Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named <code>MYBROWSER</code>, pass <code>guardrails</code> when launching Puppeteer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17700.md")</div>
<p>In addition to session guardrails, Browser Run now supports a read-only mode for <a href="/browser-run/features/live-view/">Live View</a>. Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.</p>
<p>To create a read-only link, set <code>{ mode: &quot;readonly&quot; }</code> when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.</p>
<p>Refer to the <a href="/browser-run/features/guardrails/">guardrails documentation</a> for more information.</p>
</div></article></div>
