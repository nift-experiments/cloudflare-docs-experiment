---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare Tunnel now runs connectivity pre-checks at startup · Changelog
  head_html: <title>Cloudflare Tunnel now runs connectivity pre-checks at startup · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare Tunnel now runs connectivity pre-checks at startup · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/#page","headline":"Cloudflare Tunnel now runs connectivity pre-checks at startup \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-27-cloudflared-connectivity-prechecks/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 27, 2026</time><h2 id="post-title">Cloudflare Tunnel now runs connectivity pre-checks at startup</h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/cloudflared-connectivity-prechecks.gif" alt="cloudflared connectivity pre-checks output" /></p>
<p>On every <code>cloudflared tunnel run</code> (and <code>cloudflared tunnel diag</code>), the binary now natively checks:</p>
<ul>
<li><strong>DNS resolution</strong> — <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> resolve to valid Cloudflare IPs.</li>
<li><strong>Transport connectivity</strong> — outbound <code>UDP (QUIC)</code> and <code>TCP (HTTP/2)</code> on port <code>7844</code>.</li>
<li><strong>Management API</strong> — outbound <code>TCP/443</code> to <code>api.cloudflare.com</code> for software updates.</li>
</ul>
<p>Results are printed in a scannable CLI table with three states:</p>
<ul>
<li>✅ <strong>Pass</strong> — the check succeeded.</li>
<li>⚠️ <strong>Warn</strong> — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.</li>
<li>❌ <strong>Fail</strong> — a blocking issue, with a specific remediation hint (for example, <code>Allow outbound UDP on port 7844</code>).</li>
</ul>
<p>If DNS is unresolvable, or <strong>both</strong> UDP and TCP fail on port 7844, <code>cloudflared</code> exits early with the failure rather than looping on opaque <code>failed to dial</code> errors.</p>
<p>Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.</p>
<p>To get the new behavior, upgrade <code>cloudflared</code> to version <code>2026.5.2</code> or later. For more details, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">Connectivity pre-checks documentation</a>.</p>
</div></article></div>
