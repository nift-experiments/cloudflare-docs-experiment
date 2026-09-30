<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16818.md")
</aside>
<p>Workers Sites require the latest version of <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a>.</p>
<h2 id="wrangler-configuration-file">Wrangler configuration file</h2>
<p>There are a few specific configuration settings for Workers Sites in your Wrangler file:</p>
<ul>
<li>
<p><code>bucket</code> required</p>
<ul>
<li>The directory containing your static assets, path relative to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. Example: <code>bucket = &quot;./public&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>include</code> optional</p>
<ul>
<li>A list of gitignore-style patterns for files or directories in <code>bucket</code> you exclusively want to upload. Example: <code>include = [&quot;upload_dir&quot;]</code>.</li>
</ul>
</li>
<li>
<p><code>exclude</code> optional</p>
<ul>
<li>A list of gitignore-style patterns for files or directories in <code>bucket</code> you want to exclude from uploads. Example: <code>exclude = [&quot;ignore_dir&quot;]</code>.</li>
</ul>
</li>
</ul>
<p>To learn more about the optional <code>include</code> and <code>exclude</code> fields, refer to <a href="#ignoring-subsets-of-static-assets">Ignoring subsets of static assets</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16817.md")
</aside>
<p>Example of a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16819.md")
</div>
<h2 id="storage-limits">Storage limits</h2>
<p>For very exceptionally large pages, Workers Sites might not work for you. There is a 25 MiB limit per page or file.</p>
<h2 id="ignoring-subsets-of-static-assets">Ignoring subsets of static assets</h2>
<p>Workers Sites require <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a> - make sure to use the <a href="/workers/wrangler/install-and-update/#update-wrangler">latest version</a>.</p>
<p>There are cases where users may not want to upload certain static assets to their Workers Sites.
In this case, Workers Sites can also be configured to ignore certain files or directories using logic
similar to <a href="https://doc.rust-lang.org/cargo/reference/manifest.html#the-exclude-and-include-fields-optional">Cargo's optional include and exclude fields</a>.</p>
<p>This means that you should use gitignore semantics when declaring which directory entries to include or ignore in uploads.</p>
<h3 id="exclusively-including-files-directories">Exclusively including files/directories</h3>
<p>If you want to include only a certain set of files or directories in your <code>bucket</code>, you can add an <code>include</code> field to your <code>[site]</code> section of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16820.md")
</div>
<p>Wrangler will only upload files or directories matching the patterns in the <code>include</code> array.</p>
<h3 id="excluding-files-directories">Excluding files/directories</h3>
<p>If you want to exclude files or directories in your <code>bucket</code>, you can add an <code>exclude</code> field to your <code>[site]</code> section of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16821.md")
</div>
<p>Wrangler will ignore files or directories matching the patterns in the <code>exclude</code> array when uploading assets to Workers KV.</p>
<h3 id="include-exclude">Include &gt; exclude</h3>
<p>If you provide both <code>include</code> and <code>exclude</code> fields, the <code>include</code> field will be used and the <code>exclude</code> field will be ignored.</p>
<h3 id="default-ignored-entries">Default ignored entries</h3>
<p>Wrangler will always ignore:</p>
<ul>
<li><code>node_modules</code></li>
<li>Hidden files and directories</li>
<li>Symlinks</li>
</ul>
<h4 id="more-about-include-exclude-patterns">More about include/exclude patterns</h4>
<p>Learn more about the standard patterns used for include and exclude in the <a href="https://git-scm.com/docs/gitignore">gitignore documentation</a>.</p>
