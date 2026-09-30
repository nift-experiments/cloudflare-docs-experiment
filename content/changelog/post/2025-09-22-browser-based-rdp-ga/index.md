---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/
  description: New updates and improvements at Cloudflare.
  full_title: Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available! · Changelog
  head_html: <title>Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available! · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available! · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/#page","headline":"Access Remote Desktop Protocol (RDP) destinations securely from your browser \u2014 now generally available! \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-22-browser-based-rdp-ga/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 22, 2025</time><h2 id="post-title">Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>Since we announced our <a href="/changelog/access/#2025-06-30">open beta</a>, we've made a few improvements:</p>
<ul>
<li>Support for targets with IPv6.</li>
<li>Support for <a href="/cloudflare-wan/">Magic WAN</a> and <a href="/mesh/">WARP Connector</a> as on-ramps.</li>
<li>More robust error messaging on the login page to help you if you encounter an issue.</li>
<li>Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.</li>
<li>Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.</li>
</ul>
<p>As a refresher, here are some benefits browser-based RDP provides:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browser-based RDP Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>
</div></article></div>
