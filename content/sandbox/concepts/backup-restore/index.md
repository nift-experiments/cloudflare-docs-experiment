---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/concepts/backup-restore/
  description: Production restore mounts a copy-on-write overlay. Local restore extracts the archive instead.
  full_title: Directory backups · Cloudflare Sandbox SDK docs
  head_html: <title>Directory backups · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Production restore mounts a copy-on-write overlay. Local restore extracts the archive instead."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/concepts/backup-restore/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/concepts/backup-restore/index.md"><meta property="og:title" content="Directory backups · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Production restore mounts a copy-on-write overlay. Local restore extracts the archive instead."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/concepts/backup-restore/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/concepts/backup-restore/#page","headline":"Directory backups \u00b7 Cloudflare Sandbox SDK docs","description":"Production restore mounts a copy-on-write overlay. Local restore extracts the archive instead.","url":"https://developers.cloudflare.com/sandbox/concepts/backup-restore/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/concepts/backup-restore/
  schema: 1
---
<p>Backup and restore snapshot a sandbox directory into an R2 archive, then bring that tree back later. The public API is the same in production and in <code>wrangler dev</code>. The restore mechanism is not.</p>
<p>Use backups when you want a project directory such as <code>/workspace</code> to return later. Use <a href="/sandbox/guides/mount-buckets/">bucket mounts</a> when a separate storage path such as <code>/data</code> should persist independently of the sandbox filesystem.</p>
<h2 id="production-restore">Production restore</h2>
<p>In production, <code>restoreBackup()</code> mounts the squashfs archive with FUSE overlayfs:</p>
<ul>
<li>The backup is a read-only lower layer.</li>
<li>New writes go to a writable upper layer.</li>
<li>The original archive in R2 does not change.</li>
<li>Restoring the same handle again discards the upper layer.</li>
</ul>
<p>The overlay exists only while the container is running. When the sandbox sleeps or the container restarts, the mount is gone and the directory is empty. Store the <code>DirectoryBackup</code> handle and restore again.</p>
<h2 id="local-restore">Local restore</h2>
<p>With <code>localBucket: true</code>, <code>wrangler dev</code> extracts the archive with <code>unsquashfs</code>. The target directory is replaced. There is no overlay, so local restore does not reproduce production FUSE behavior.</p>
<h2 id="cross-device-renames">Cross-device renames</h2>
<p>Overlayfs treats the lower and upper layers as different devices. A rename that moves a directory from the restored lower layer into the writable upper layer can fail with <code>EXDEV</code> (<code>cross-device link not permitted</code>).</p>
<p>Vite does this with <code>node_modules/.vite/deps</code>. Omit that directory from the backup, or delete it after restore.</p>
<p>For the procedure, refer to <a href="/sandbox/guides/backup-restore/#exclude-generated-caches">Exclude generated caches</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/backup-restore/">Backup and restore</a> - Create, restore, and exclude caches</li>
<li><a href="/sandbox/api/backups/">Backups API</a> - Method signatures and options</li>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a> - What happens when a sandbox sleeps</li>
</ul>
