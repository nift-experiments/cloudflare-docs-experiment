---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare One Client for Windows (version 2026.8.1290.1) · Changelog
  head_html: <title>Cloudflare One Client for Windows (version 2026.8.1290.1) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One Client for Windows (version 2026.8.1290.1) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/#page","headline":"Cloudflare One Client for Windows (version 2026.8.1290.1) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-09-warp-windows-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 10, 2026</time><h2 id="post-title">Cloudflare One Client for Windows (version 2026.8.1290.1)</h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.</li>
<li>Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.</li>
<li>Improved API reliability by retrying requests dropped when reusing pooled connections.</li>
<li>The client no longer requires the Windows WLAN AutoConfig service to be running.</li>
<li>Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.</li>
<li>Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.</li>
<li>Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.</li>
<li>Fixed the client continuing to report 'No network' after a successful manual disconnect.</li>
<li>Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.</li>
<li>Fixed the client UI crashing at startup when it could not write to the Windows registry.</li>
<li>Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.</li>
<li>Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.</li>
<li>Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.</li>
<li>Fixed a startup crash when date formatting data for the system locale had not yet loaded.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation, see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation, see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div></article></div>
