---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/
  description: New updates and improvements at Cloudflare.
  full_title: Expanded File Type Controls for Executables and Disk Images · Changelog
  head_html: <title>Expanded File Type Controls for Executables and Disk Images · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Expanded File Type Controls for Executables and Disk Images · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/#page","headline":"Expanded File Type Controls for Executables and Disk Images \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-01-new-file-type-support/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 1, 2025</time><h2 id="post-title">Expanded File Type Controls for Executables and Disk Images</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.</p>
<p>We have expanded Gateway's file type controls to include:</p>
<ul>
<li>Apple Disk Image (dmg)</li>
<li>Microsoft Software Installer (msix, appx)</li>
<li>Apple Software Package (pkg)</li>
</ul>
<p>You can find these new options within the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types"><em>Upload File Types</em> and <em>Download File Types</em> selectors</a> when creating or editing an HTTP policy. The file types are categorized as follows:</p>
<ul>
<li><strong>System</strong>: <em>Apple Disk Image (dmg)</em></li>
<li><strong>Executable</strong>: <em>Microsoft Software Installer (msix)</em>, <em>Microsoft Software Installer (appx)</em>, <em>Apple Software Package (pkg)</em></li>
</ul>
<p>To ensure these file types are blocked effectively, please note the following behaviors:</p>
<ul>
<li>DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.</li>
<li>MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type <em>Unscannable</em>. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.</li>
</ul>
<p>To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#supported-file-types">supported file types</a>.</p>
</div></article></div>
