<p>Forcing or dropping trailing slashes on request paths (for example, <code>example.com/page/</code> vs. <code>example.com/page</code>) is often something that developers wish to control for cosmetic reasons. Additionally, it can impact SEO because search engines often treat URLs with and without trailing slashes as different, separate pages. This distinction can lead to duplicate content issues, indexing problems, and overall confusion about the correct canonical version of a page.</p>
<p>The <a href="/workers/wrangler/configuration/#assets"><code>assets.html_handling</code> configuration</a> determines the redirects and rewrites of requests for HTML content. It is used to specify the pattern for canonical URLs, thus where Cloudflare serves HTML content from, and additionally, where Cloudflare redirects non-canonical URLs to.</p>
<p>Take the following directory structure:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/17311.md")&#10;&#10;&#10;</pre>
<h2 id="automatic-trailing-slashes-default">Automatic trailing slashes (default)</h2>
<p>This will usually give you the desired behavior automatically: individual files (e.g. <code>foo.html</code>) will be served <em>without</em> a trailing slash and folder index files (e.g. <code>foo/index.html</code>) will be served <em>with</em> a trailing slash.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17312.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="force-trailing-slashes">Force trailing slashes</h2>
<p>Alternatively, you can force trailing slashes (<code>force-trailing-slash</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17313.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file/</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder/</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="drop-trailing-slashes">Drop trailing slashes</h2>
<p>Or you can drop trailing slashes (<code>drop-trailing-slash</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17314.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/file/index.html</td>
<td>307 to /file</td>
<td>-</td>
</tr>
<tr>
<td>/folder</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
<tr>
<td>/folder.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>307 to /folder</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="disable-html-handling">Disable HTML handling</h2>
<p>Alternatively, if you have bespoke needs, you can disable the built-in HTML handling entirely (<code>none</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17315.md")
</div>
<p>Based on the incoming requests, the following assets would be served:</p>
<table>
<thead>
<tr>
<th>Incoming Request</th>
<th>Response</th>
<th>Asset Served</th>
</tr>
</thead>
<tbody>
<tr>
<td>/file</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file.html</td>
<td>200</td>
<td>/dist/file.html</td>
</tr>
<tr>
<td>/file/</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file/index</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/file/index.html</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder.html</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/index</td>
<td>Depends on <code>not_found_handling</code></td>
<td>Depends on <code>not_found_handling</code></td>
</tr>
<tr>
<td>/folder/index.html</td>
<td>200</td>
<td>/dist/folder/index.html</td>
</tr>
</tbody>
</table>
