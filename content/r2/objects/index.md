<p>Objects are individual files or data that you store in an R2 bucket. Each object is identified by its key, a string like <code>images/photo.png</code>.</p>
<h2 id="prefixes-and-folders">Prefixes and folders</h2>
<p>R2 uses a flat storage structure. There are no real directories or folders. The <code>/</code> character in an object key is used as a delimiter to group objects by prefix.</p>
<p>The R2 dashboard groups objects that share a common prefix into folders when the <strong>View prefixes as directories</strong> checkbox is selected. For example, objects with keys <code>logs/jan.csv</code> and <code>logs/feb.csv</code> appear under a <code>logs/</code> folder. These folders are a visual grouping and do not exist as separate resources in your bucket.</p>
<h2 id="manage-objects">Manage objects</h2>
<ul class="directory-listing"><li><a href="/r2/objects/upload-objects/">Upload objects</a></li><li><a href="/r2/objects/download-objects/">Download objects</a></li><li><a href="/r2/objects/delete-objects/">Delete objects</a></li></ul>
<h2 id="other-resources">Other resources</h2>
<p>For information on R2 Workers Binding API, refer to <a href="/r2/api/workers/workers-api-reference/">R2 Workers API reference</a>.</p>
