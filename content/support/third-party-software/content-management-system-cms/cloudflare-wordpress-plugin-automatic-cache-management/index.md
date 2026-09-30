<h2 id="overview">Overview</h2>
<p>The Cloudflare WordPress plugin contains a feature called Automatic Cache Management. When a user adds, edits, or deletes a post, page, attachment, or comment - any associated URLs are purged from the Cloudflare cache.</p>
<p>When you switch a theme or customise a theme within the WordPress admin panel, the cache will automatically be cleared too.</p>
<p>Automatic Cache Management uses native hooks built into WordPress. The Cloudflare WordPress plugin purges the following cache URLs:</p>
<ul>
<li>deleted_post</li>
<li>edit_post</li>
<li>delete_attachment</li>
<li>autoptimize_action_cachepurged (for compatibility with the Autoptimize WordPress plugin)</li>
<li>switch_theme</li>
<li>customize_save_after</li>
</ul>
<hr />
<h2 id="enable-automatic-cache-management">Enable Automatic Cache Management</h2>
<p>To enable Automatic Cache Management after <a href="/automatic-platform-optimization/">installing the WordPress plugin</a>:</p>
<ol>
<li>Log in to your WordPress account.</li>
<li>Click <strong>Settings</strong> and choose the Cloudflare plugin. The Cloudflare plugin home page appears.</li>
<li>Click <strong>Enable</strong> to the right of the <strong>Automatic Cache</strong> feature. A confirmation dialog appears.</li>
<li>Click <strong>I'm sure</strong> in the confirmation dialog to confirm.</li>
</ol>
