---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/
  description: New updates and improvements at Cloudflare.
  full_title: File transfer controls for browser-based RDP (beta) · Changelog
  head_html: <title>File transfer controls for browser-based RDP (beta) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="File transfer controls for browser-based RDP (beta) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/#page","headline":"File transfer controls for browser-based RDP (beta) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-07-rdp-file-transfer-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 7, 2026</time><h2 id="post-title">File transfer controls for browser-based RDP (beta)</h2>
<div class="changelog-badges"><span>access</span><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/file-transfer-policy-control.png" alt="File transfer connection settings in the Access policy configuration." /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.</p>
<h4 id="configuration-options">Configuration options</h4>
<p>File transfer controls are configured per policy within your Access application, alongside existing <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">text clipboard controls</a>. For each policy, you can select one of the following options:</p>
<ul>
<li><strong>Client to remote RDP session allowed</strong> — Users can upload files from their local machine into the browser-based RDP session.</li>
<li><strong>Remote RDP session to client allowed</strong> — Users can download files from the browser-based RDP session to their local machine.</li>
<li><strong>Both directions allowed</strong> — Users can upload and download files between their local machine and the browser-based RDP session.</li>
<li><strong>Disable copying/pasting</strong> — Users are not allowed to transfer files between their local machine and the browser-based RDP session.</li>
</ul>
<p>By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.</p>
<h4 id="how-it-works">How it works</h4>
<p>To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/clipboard-side-panel.png" alt="The clipboard side panel showing files available for transfer." /></p>
<p><img src="/assets/upstream/images/changelog/access/remote-doc-ready-for-download-or-print-local.png" alt="A remote document ready for download or local printing." /></p>
<p>This feature is in beta and available on all Zero Trust plans. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files">File transfer for browser-based RDP</a>.</p>
</div></article></div>
