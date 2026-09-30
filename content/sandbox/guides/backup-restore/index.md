---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/backup-restore/
  description: Snapshot a sandbox directory to R2 and restore it later.
  full_title: Backup and restore · Cloudflare Sandbox SDK docs
  head_html: <title>Backup and restore · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Snapshot a sandbox directory to R2 and restore it later."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/backup-restore/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/backup-restore/index.md"><meta property="og:title" content="Backup and restore · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Snapshot a sandbox directory to R2 and restore it later."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/backup-restore/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/backup-restore/#page","headline":"Backup and restore \u00b7 Cloudflare Sandbox SDK docs","description":"Snapshot a sandbox directory to R2 and restore it later.","url":"https://developers.cloudflare.com/sandbox/guides/backup-restore/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/backup-restore/
  schema: 1
---
<p>This guide shows you how to snapshot a sandbox directory to R2 and restore it later.</p>
<p>Use backup and restore when a project directory such as <code>/workspace</code> should come back after the sandbox sleeps. For a separate persisted storage path, mount a bucket instead. If you mount a bucket over <code>/workspace</code>, the mount overlays files seeded by your image in production.</p>
<p>For why production restore uses an overlay, refer to <a href="/sandbox/concepts/backup-restore/">Directory backups</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Create an R2 bucket:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket create my-backup-bucket&#10;</code></pre>
<ol start="2">
<li>Add the <code>BACKUP_BUCKET</code> R2 binding and presigned URL settings to your Wrangler configuration:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13489.md")
</div>
<p>If the bucket uses a jurisdiction-specific endpoint, add <code>BACKUP_BUCKET_ENDPOINT</code> to <code>vars</code>. For an EU bucket, use <code>https://&lt;ACCOUNT_ID&gt;.eu.r2.cloudflarestorage.com</code>.</p>
<ol start="3">
<li>Store R2 API credentials as secrets:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put R2_ACCESS_KEY_ID&#10;npx wrangler secret put R2_SECRET_ACCESS_KEY&#10;</code></pre>
<p>Create the token in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>R2</strong> &gt; <strong>Overview</strong> &gt; <strong>Manage R2 API Tokens</strong>. Grant <strong>Object Read &amp; Write</strong> on the backup bucket.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13488.md")
</aside>
<h2 id="create-a-backup">Create a backup</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13490.md")
</div>
<p>The directory must be an absolute path under <code>/workspace</code>, <code>/home</code>, <code>/tmp</code>, <code>/var/tmp</code>, or <code>/app</code>.</p>
<h2 id="restore-a-backup">Restore a backup</h2>
<p>Stop processes that write to the target directory, then restore:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13491.md")
</div>
<p>In production, restore mounts a copy-on-write overlay. The mount is lost when the sandbox sleeps or the container restarts. Restore again from the stored handle.</p>
<p>The restore target is <code>backup.dir</code>. You can point that field at a different allowed directory than the one you originally backed up.</p>
<h2 id="exclude-generated-caches">Exclude generated caches</h2>
<p>After a production restore, renaming a directory inside the restored tree can fail with <code>EXDEV</code> (<code>cross-device link not permitted</code>). Omit disposable generated directories from the backup, or delete them after restore. Vite's cache is one such directory:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13492.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13493.md")
</div>
<p>This failure does not occur in <code>wrangler dev</code>, which extracts the archive. For overlay restore, refer to <a href="/sandbox/concepts/backup-restore/">Directory backups</a>.</p>
<h2 id="exclude-gitignored-files">Exclude gitignored files</h2>
<p>To skip <code>.gitignore</code> matches such as <code>node_modules/</code> or <code>dist/</code> in a git repository:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13494.md")
</div>
<p>If the directory is not inside a git repository, <code>gitignore</code> has no effect. If <code>git</code> is not installed in the container, the SDK logs a warning and continues without git-based exclusions. Nested <code>.gitignore</code> files apply.</p>
<h2 id="checkpoint-and-roll-back">Checkpoint and roll back</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13495.md")
</div>
<h2 id="store-backup-handles">Store backup handles</h2>
<p><code>DirectoryBackup</code> is serializable. Persist it to KV, D1, or Durable Object storage:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13496.md")
</div>
<h2 id="set-a-name-and-ttl">Set a name and TTL</h2>
<p>Names can be up to 256 characters. The default TTL is 3 days (<code>259200</code> seconds). The SDK rejects an expired backup at restore time. It does not delete the R2 objects.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13497.md")
</div>
<p>To delete expired objects automatically, add an <a href="/r2/buckets/object-lifecycles/">R2 object lifecycle rule</a> on the <code>backups/</code> prefix. If your longest TTL is 7 days, expire objects older than 7 days.</p>
<h2 id="clean-up-backup-objects">Clean up backup objects</h2>
<p>Archives live at <code>backups/{backupId}/data.sqsh</code> and <code>backups/{backupId}/meta.json</code>.</p>
<h3 id="replace-the-latest-backup">Replace the latest backup</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13498.md")
</div>
<h3 id="delete-a-backup-by-id">Delete a backup by ID</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13499.md")
</div>
<h3 id="delete-backups-by-age">Delete backups by age</h3>
<p>List objects under <code>backups/</code> and delete by upload time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13500.md")
</div>
<h2 id="use-backup-and-restore-in-local-development">Use backup and restore in local development</h2>
<p>Pass <code>localBucket: true</code> so <code>wrangler dev</code> uses the <code>BACKUP_BUCKET</code> binding. Presigned URL credentials are not required.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13501.md")
</div>
<p>Local restore extracts the archive with <code>unsquashfs</code> and replaces the directory. The stored handle's <code>localBucket</code> field selects the restore path.</p>
<h2 id="fix-path-permissions">Fix path permissions</h2>
<p><code>createBackup()</code> must read every file under the target directory. Files with mode <code>0600</code> or directories owned by another user cause <code>BackupCreateError</code>.</p>
<p>Set permissions in the image when you can. <code>a+rX</code> adds read permission on files and execute permission on directories:</p>
<pre tabindex="0"><code class="language-dockerfile">RUN mkdir -p /home/sandbox &amp;&amp; chmod -R a+rX /home/sandbox&#10;</code></pre>
<p>If a process creates restrictive files at runtime, fix them before the backup:</p>
<pre tabindex="0"><code class="language-ts">await sandbox.exec(&quot;chmod -R a+rX /home/sandbox/.claude&quot;);&#10;const backup = await sandbox.createBackup({ dir: &quot;/home/sandbox&quot; });&#10;</code></pre>
<h2 id="handle-errors">Handle errors</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13502.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/backup-restore/">Directory backups</a> - Overlay restore, local extract, and <code>EXDEV</code></li>
<li><a href="/sandbox/api/backups/">Backups API</a> - Methods, options, and types</li>
<li><a href="/sandbox/api/storage/">Storage API</a> - Mount S3-compatible buckets</li>
<li><a href="/r2/">R2 documentation</a> - R2 buckets and credentials</li>
<li><a href="/r2/buckets/object-lifecycles/">R2 lifecycle rules</a> - Automatic object cleanup</li>
</ul>
