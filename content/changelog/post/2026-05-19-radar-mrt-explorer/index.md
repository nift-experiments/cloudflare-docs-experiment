---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/
  description: New updates and improvements at Cloudflare.
  full_title: MRT Explorer on Cloudflare Radar · Changelog
  head_html: <title>MRT Explorer on Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="MRT Explorer on Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/#page","headline":"MRT Explorer on Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-19-radar-mrt-explorer/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 19, 2026</time><h2 id="post-title">MRT Explorer on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes an <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer</a> tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.</p>
<h4 id="loading-a-file">Loading a file</h4>
<p>Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-form.png" alt="Screenshot of the MRT Explorer file input form" /></p>
<h4 id="inspecting-events">Inspecting events</h4>
<p>Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-list.png" alt="Screenshot of the MRT Explorer event list" /></p>
<h4 id="event-details">Event details</h4>
<p>Clicking on the &quot;View details&quot; action opens a modal with additional properties and the full event JSON.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-details.png" alt="Screenshot of the MRT Explorer event details modal" /></p>
<h4 id="shareable-urls">Shareable URLs</h4>
<p>When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.</p>
<p>Try the <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer on Cloudflare Radar</a>.</p>
</div></article></div>
