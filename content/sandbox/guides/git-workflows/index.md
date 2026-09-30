<p>This guide shows you how to clone repositories, manage branches, and automate Git operations in the sandbox.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13416.md")
</aside>
<h2 id="clone-repositories">Clone repositories</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13417.md")
</div>
<h2 id="clone-private-repositories">Clone private repositories</h2>
<p>Use a personal access token in the URL:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13418.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="more-secure-alternative">More secure alternative</h3>
@markup("md", "content/.markup/bodies/13415.md")
</aside>
<h2 id="clone-and-build">Clone and build</h2>
<p>Clone a repository and run build steps:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13419.md")
</div>
<h2 id="work-with-branches">Work with branches</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13420.md")
</div>
<h2 id="make-changes-and-commit">Make changes and commit</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13421.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Use shallow clones</strong> - Faster for large repos with <code>depth: 1</code></li>
<li><strong>Store credentials securely</strong> - Use environment variables for tokens</li>
<li><strong>Clean up</strong> - Delete unused repositories to save space</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="authentication-fails">Authentication fails</h3>
<p>Verify your token is set:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13422.md")
</div>
<h3 id="large-repository-timeout">Large repository timeout</h3>
<p>Use shallow clone:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13423.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/files/">Files API reference</a> - File operations after cloning</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - Run git commands</li>
<li><a href="/sandbox/guides/manage-files/">Manage files guide</a> - Work with cloned files</li>
</ul>
