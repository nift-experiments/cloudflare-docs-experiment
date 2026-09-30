<p>Create point-in-time snapshots of sandbox directories and restore them from R2.</p>
<p>For setup, restore workflows, and generated-cache exclusions, refer to <a href="/sandbox/guides/backup-restore/">Backup and restore</a>. For overlay semantics, refer to <a href="/sandbox/concepts/backup-restore/">Directory backups</a>.</p>
<h2 id="methods">Methods</h2>
<h3 id="createbackup"><code>createBackup()</code></h3>
<p>Create a snapshot of a directory and upload it to R2.</p>
<pre><code class="language-ts">await sandbox.createBackup(options: BackupOptions): Promise&lt;DirectoryBackup&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>options</code> - Backup configuration (see <a href="#backupoptions"><code>BackupOptions</code></a>):
<ul>
<li><code>dir</code> (required) - Absolute path to back up. Must be under <code>/workspace</code>, <code>/home</code>, <code>/tmp</code>, <code>/var/tmp</code>, or <code>/app</code>.</li>
<li><code>name</code> (optional) - Human-readable name. Maximum 256 characters. Control characters are rejected.</li>
<li><code>ttl</code> (optional) - Time-to-live in seconds. Default: <code>259200</code> (3 days). Must be a positive number.</li>
<li><code>gitignore</code> (optional) - When <code>true</code>, exclude paths matching <code>.gitignore</code> rules if <code>dir</code> is inside a git repository. Default: <code>false</code>. If the directory is not in a git repository, no git exclusions apply. If <code>git</code> is not installed, the SDK logs a warning and continues without git-based exclusions.</li>
<li><code>excludes</code> (optional) - Glob patterns to omit from the archive. Passed to <code>mksquashfs</code> as wildcard excludes. <code>**</code> globstars are normalized automatically. Default: <code>[]</code>.</li>
<li><code>localBucket</code> (optional) - When <code>true</code>, use the <code>BACKUP_BUCKET</code> R2 binding instead of presigned URLs. Intended for <code>wrangler dev</code>. Default: <code>false</code>.</li>
<li><code>compression</code> (optional) - Archive compression. Default format: <code>lz4</code>. Default threads: <code>8</code>. Format must be <code>gzip</code>, <code>lz4</code>, or <code>zstd</code>. <code>threads</code> must be a positive integer.</li>
<li><code>multipart</code> (optional) - Use parallel multipart upload for large archives. Default: <code>true</code>.</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;DirectoryBackup&gt;</code> containing:</p>
<ul>
<li><code>id</code> - Unique backup identifier (UUID)</li>
<li><code>dir</code> - Directory that was backed up</li>
<li><code>localBucket</code> (optional) - Whether the backup used local R2 binding mode</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13701.md")
</div>
<p><strong>How it works</strong>:</p>
<p>In production:</p>
<ol>
<li>The container creates a compressed squashfs archive.</li>
<li>The container uploads the archive to R2 with a presigned URL.</li>
<li>Metadata is stored alongside the archive in R2.</li>
<li>The local archive is deleted.</li>
</ol>
<p>With <code>localBucket: true</code>:</p>
<ol>
<li>The container creates a compressed squashfs archive.</li>
<li>The archive is uploaded through the <code>BACKUP_BUCKET</code> R2 binding.</li>
<li>Metadata is stored alongside the archive in R2.</li>
<li>The local archive is deleted.</li>
</ol>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>InvalidBackupConfigError</code> - If <code>dir</code> is not an allowed absolute path, the <code>BACKUP_BUCKET</code> binding is missing, or (in production) R2 presigned URL credentials are not configured</li>
<li><code>BackupCreateError</code> - If archive creation or the upload to R2 fails</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="r2-binding-required">R2 binding required</h3>
@markup("md", "content/.markup/bodies/13700.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="path-permissions">Path permissions</h3>
@markup("md", "content/.markup/bodies/13699.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="partial-writes">Partial writes</h3>
@markup("md", "content/.markup/bodies/13698.md")
</aside>
<hr />
<h3 id="restorebackup"><code>restoreBackup()</code></h3>
<p>Restore a previously created backup.</p>
<pre><code class="language-ts">await sandbox.restoreBackup(backup: DirectoryBackup): Promise&lt;RestoreBackupResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>backup</code> - Handle returned by <code>createBackup()</code>. Contains <code>id</code> and <code>dir</code>. Restore writes into <code>backup.dir</code>, which may differ from the original backup path. (see <a href="#directorybackup"><code>DirectoryBackup</code></a>)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;RestoreBackupResult&gt;</code> containing:</p>
<ul>
<li><code>success</code> - Whether the restore succeeded</li>
<li><code>dir</code> - Directory that was restored</li>
<li><code>id</code> - Backup ID that was restored</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13702.md")
</div>
<p><strong>How it works</strong>:</p>
<p>In production:</p>
<ol>
<li>Metadata is downloaded from R2 and the TTL is checked, with a 60-second buffer. An expired backup throws.</li>
<li>The container downloads the archive from R2 with a presigned URL.</li>
<li>The container mounts the archive with FUSE overlayfs.</li>
</ol>
<p>With <code>localBucket: true</code>:</p>
<ol>
<li>Metadata is downloaded from the <code>BACKUP_BUCKET</code> binding and the TTL is checked.</li>
<li>The archive is downloaded from the R2 binding.</li>
<li>The archive is extracted with <code>unsquashfs</code>.</li>
</ol>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>InvalidBackupConfigError</code> - If <code>backup.id</code> is missing or not a UUID, or <code>backup.dir</code> is invalid</li>
<li><code>BackupNotFoundError</code> - If the metadata or archive is not in R2</li>
<li><code>BackupExpiredError</code> - If the TTL has elapsed</li>
<li><code>BackupRestoreError</code> - If the container fails to restore</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="copy-on-write">Copy-on-write</h3>
@markup("md", "content/.markup/bodies/13697.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="ephemeral-mount">Ephemeral mount</h3>
@markup("md", "content/.markup/bodies/13696.md")
</aside>
<h2 id="behavior">Behavior</h2>
<ul>
<li>Concurrent backup and restore operations on the same sandbox are serialized.</li>
<li><code>DirectoryBackup</code> is serializable. Store it in KV, D1, or Durable Object storage.</li>
<li>Overlapping backups are independent. Restoring a parent directory overwrites subdirectory mounts. Restore the parent first when restoring both.</li>
<li><code>ttl</code> is enforced at restore time only. Expired objects remain in R2 until you delete them or an <a href="/r2/buckets/object-lifecycles/">R2 lifecycle rule</a> removes them.</li>
<li>Backup objects use <code>backups/{id}/data.sqsh</code> and <code>backups/{id}/meta.json</code>.</li>
</ul>
<h2 id="types">Types</h2>
<h3 id="backupoptions"><code>BackupOptions</code></h3>
<pre><code class="language-ts">interface BackupCompressionOptions {&#10;	format?: &quot;gzip&quot; | &quot;lz4&quot; | &quot;zstd&quot;;&#10;	threads?: number;&#10;}&#10;&#10;interface BackupOptions {&#10;	dir: string;&#10;	name?: string;&#10;	ttl?: number;&#10;	gitignore?: boolean;&#10;	excludes?: string[];&#10;	localBucket?: boolean;&#10;	compression?: BackupCompressionOptions;&#10;	multipart?: boolean;&#10;}&#10;</code></pre>
<p><strong>Fields</strong>:</p>
<ul>
<li><code>dir</code> (required) - Absolute path under <code>/workspace</code>, <code>/home</code>, <code>/tmp</code>, <code>/var/tmp</code>, or <code>/app</code></li>
<li><code>name</code> (optional) - Human-readable name. Maximum 256 characters. No control characters.</li>
<li><code>ttl</code> (optional) - Time-to-live in seconds. Default: <code>259200</code> (3 days). Must be a positive number.</li>
<li><code>gitignore</code> (optional) - When <code>true</code>, exclude <code>.gitignore</code> matches if <code>dir</code> is inside a git repository. Default: <code>false</code>.</li>
<li><code>excludes</code> (optional) - Glob patterns to omit. Example: <code>['node_modules/.cache', '*.log']</code>. Refer to <a href="/sandbox/guides/backup-restore/#exclude-generated-caches">Exclude generated caches</a>.</li>
<li><code>localBucket</code> (optional) - Use the <code>BACKUP_BUCKET</code> binding instead of presigned URLs. Default: <code>false</code>.</li>
<li><code>compression</code> (optional) - <code>format</code> defaults to <code>lz4</code>. <code>threads</code> defaults to <code>8</code>.</li>
<li><code>multipart</code> (optional) - Parallel multipart upload. Default: <code>true</code>.</li>
</ul>
<h3 id="directorybackup"><code>DirectoryBackup</code></h3>
<pre><code class="language-ts">interface DirectoryBackup {&#10;	readonly id: string;&#10;	readonly dir: string;&#10;	readonly localBucket?: boolean;&#10;}&#10;</code></pre>
<p><strong>Fields</strong>:</p>
<ul>
<li><code>id</code> - Unique backup identifier (UUID)</li>
<li><code>dir</code> - Directory to restore into</li>
<li><code>localBucket</code> (optional) - Whether the backup used local R2 binding mode</li>
</ul>
<h3 id="restorebackupresult"><code>RestoreBackupResult</code></h3>
<pre><code class="language-ts">interface RestoreBackupResult {&#10;	success: boolean;&#10;	dir: string;&#10;	id: string;&#10;}&#10;</code></pre>
<p><strong>Fields</strong>:</p>
<ul>
<li><code>success</code> - Whether the restore succeeded</li>
<li><code>dir</code> - Directory that was restored</li>
<li><code>id</code> - Backup ID that was restored</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/backup-restore/">Backup and restore</a> - Setup and restore workflows</li>
<li><a href="/sandbox/concepts/backup-restore/">Directory backups</a> - Overlay restore and <code>EXDEV</code></li>
<li><a href="/sandbox/api/storage/">Storage API</a> - Mount S3-compatible buckets</li>
<li><a href="/sandbox/api/files/">Files API</a> - Read and write files</li>
<li><a href="/sandbox/configuration/wrangler/">Wrangler configuration</a> - Configure bindings</li>
</ul>
