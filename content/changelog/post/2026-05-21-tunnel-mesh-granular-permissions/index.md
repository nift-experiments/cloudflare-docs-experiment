---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/
  description: New updates and improvements at Cloudflare.
  full_title: Granular permissions for Cloudflare Tunnel and Cloudflare Mesh · Changelog
  head_html: <title>Granular permissions for Cloudflare Tunnel and Cloudflare Mesh · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Granular permissions for Cloudflare Tunnel and Cloudflare Mesh · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/#page","headline":"Granular permissions for Cloudflare Tunnel and Cloudflare Mesh \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-21-tunnel-mesh-granular-permissions/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 21, 2026</time><h2 id="post-title">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</h2>
<div class="changelog-badges"><span>fundamentals</span><span>cloudflare-one</span><span>cloudflare-tunnel-sase</span><span>tunnel</span><span>mesh</span></div><div class="changelog-body"><p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>
</div></article></div>
