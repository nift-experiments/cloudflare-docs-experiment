---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/
  description: New updates and improvements at Cloudflare.
  full_title: High availability replica management for Cloudflare Mesh · Changelog
  head_html: <title>High availability replica management for Cloudflare Mesh · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="High availability replica management for Cloudflare Mesh · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/#page","headline":"High availability replica management for Cloudflare Mesh \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-28-mesh-ha-replica-ui/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">High availability replica management for Cloudflare Mesh</h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p>The <a href="/mesh/">Cloudflare Mesh</a> dashboard now shows per-replica details for <a href="/mesh/features/high-availability/">high availability</a> nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/mesh-ha-replicas.gif" alt="Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option" /></p>
<h4 id="what-s-new">What's new</h4>
<ul>
<li><strong>Replica tabs</strong> on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.</li>
<li><strong>Active/passive badges</strong> identify which replica is currently routing traffic.</li>
<li><strong>Manual failover</strong> — promote a passive replica to active with a single click. The previous active replica switches to standby.</li>
<li><strong>HA badge</strong> in the overview table identifies nodes running multiple replicas.</li>
<li><strong>Active replica IP</strong> shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.</li>
</ul>
<h4 id="manual-failover">Manual failover</h4>
<p>To manually promote a passive replica:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
<li>Select an HA-enabled node.</li>
<li>Select the passive replica tab.</li>
<li>Select <strong>Promote to active</strong> and confirm.</li>
</ol>
<p>Traffic reroutes to the promoted replica immediately. Refer to <a href="/mesh/features/high-availability/">High availability</a> for details on failover behavior.</p>
</div></article></div>
