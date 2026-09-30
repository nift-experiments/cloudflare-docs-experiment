<div class="nb-description">
@markup("md", "content/.markup/bodies/1502.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1501.md")
</aside>
<p>Artifacts stores versioned file trees behind a Git-compatible interface. Create repositories programmatically, import existing repositories, and hand off a URL to any standard Git client.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> before you start, then choose the namespace name you will use for these repos.</p>
<p>Use Artifacts when you need to:</p>
<ul>
<li>Store versioned file trees instead of raw blobs</li>
<li>Hand off work to Git-aware tools, agents, and automation</li>
<li>Isolate work in separate repos or branches for safer parallel execution</li>
<li>Fork from a shared baseline and diff or merge the results later</li>
</ul>
<p>The same repository can be addressed from <a href="/artifacts/get-started/workers/">Workers</a>, the REST API, and Git clients. You can create one repo per agent, user, branch, or task, keep each unit of work separate, and compare or merge the results later.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/1510.md")
</div>
