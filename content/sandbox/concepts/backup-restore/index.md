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
