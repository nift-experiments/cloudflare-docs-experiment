<p>You can configure how Email security handles links in emails.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4933.md")
</aside>
<p>To configure link actions:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, then go to <strong>Detection settings</strong> &gt; <strong>Link actions</strong> &gt; <strong>View</strong>.</li>
</ol>
<p>You can configure <strong>Link actions settings</strong>, or <strong>URL rewrite ignore patterns</strong>.</p>
<h2 id="link-actions-settings">Link actions settings</h2>
<p>To configure link actions, select <strong>Configure</strong>.</p>
<p>The dashboard will display <strong>Open links evaluated as suspicious in a remote browser (Recommended)</strong>. This option is turned on by default. Email security will also allow you to select message dispositions to open all the links for dispositioned emails in a remote browser.</p>
<p>Select one or more disposition, then select <strong>Save</strong>.</p>
<p>If <strong>Open links evaluated as suspicious in a remote browser (Recommended)</strong> is turned off, you can select <strong>URL defang</strong> or <strong>No action</strong> on each disposition. Select <strong>Save</strong> once you have completed the configuration.</p>
<p>When opening links, Email security will not allow you to:</p>
<ul>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Copy (from remote to client)</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Paste (from client to remote)</a></li>
<li>Use <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">keyboard</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Print</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Download files</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Uploads files</a></li>
</ul>
<h2 id="add-patterns-for-urls">Add patterns for URLs</h2>
<p>You can add patterns for URLs that should be rewritten.</p>
<ol>
<li>Under <strong>URL rewrite ignore patterns</strong>, select <strong>Add a pattern</strong>.</li>
<li>Enter a valid IP, URL, or regular expression. You can enter up to 512 characters.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To edit a pattern, go to the pattern you want to edit, select the three dots, then <strong>Edit</strong>. Once you have finished modifying the URL patter, select <strong>Save</strong>.</p>
<p>To delete a pattern, go to the pattern you want to delete, select the three dots, then <strong>Delete</strong>.</p>
