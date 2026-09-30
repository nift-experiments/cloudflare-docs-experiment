<p>When connected to your git repository, Pages allows you to control which environments and branches you would like to automatically deploy to. By default, Pages will trigger a deployment any time you commit to either your production or preview environment. However, with branch deployment controls, you can configure automatic deployments to suit your preference on a per project basis.</p>
<h2 id="production-branch-control">Production branch control</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="direct-upload">Direct Upload</h3>
@markup("md", "content/.markup/bodies/11081.md")
</aside>
<p>To configure deployment options, go to your Pages project &gt; <strong>Settings</strong> &gt; <strong>Builds &amp; deployments</strong> &gt; <strong>Configure Production deployments</strong>. Pages will default to setting your production environment to the branch you first push, but you can set your production to another branch if you choose.</p>
<p>You can also enable or disable automatic deployment behavior on the production branch by checking the <strong>Enable automatic production branch deployments</strong> box. You must save your settings in order for the new production branch controls to take effect.</p>
<h2 id="preview-branch-control">Preview branch control</h2>
<p>When configuring automatic preview deployments, there are three options to choose from.</p>
<ul>
<li><strong>All non-Production branches</strong>: By default, Pages will automatically deploy any and every commit to a preview branch.</li>
<li><strong>None</strong>: Turns off automatic builds for all preview branches.</li>
<li><strong>Custom branches</strong>: Customize the automatic deployments of certain preview branches.</li>
</ul>
<h3 id="custom-preview-branch-control">Custom preview branch control</h3>
<p>By selecting <strong>Custom branches</strong>, you can specify branches you wish to include and exclude from automatic deployments in the provided configuration fields. The configuration fields can be filled in two ways:</p>
<ul>
<li><strong>Static branch names</strong>: Enter the precise name of the branch you are looking to include or exclude (for example, staging or dev).</li>
<li><strong>Wildcard syntax</strong>: Use wildcards to match multiple branches. You can specify wildcards at the start or end of your rule. The order of execution for the configuration is (1) Excludes, (2) Includes, (3) Skip. Pages will process the exclude configuration first, then go to the include configuration. If a branch does not match either then it will be skipped.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wildcard-syntax">Wildcard syntax</h3>
@markup("md", "content/.markup/bodies/11080.md")
</aside>
<p><strong>Example 1:</strong></p>
<p>If you want to enforce branch prefixes such as <code>fix/</code>, <code>feat/</code>, or <code>chore/</code> with wildcard syntax, you can include and exclude certain branches with the following rules:</p>
<ul>
<li>
<p>Include Preview branches:
<code>fix/*</code>, <code>feat/*</code>, <code>chore/*</code></p>
</li>
<li>
<p>Exclude Preview branches:
``</p>
</li>
</ul>
<p>Here Pages will include any branches with the indicated prefixes and exclude everything else. In this example, the excluding option is left empty.</p>
<p><strong>Example 2:</strong></p>
<p>If you wanted to prevent <a href="https://github.com/dependabot">dependabot</a> from creating a deployment for each PR it creates, you can exclude those branches with the following:</p>
<ul>
<li>
<p>Include Preview branches:
<code>*</code></p>
</li>
<li>
<p>Exclude Preview branches:
<code>dependabot/*</code></p>
</li>
</ul>
<p>Here Pages will include all branches except any branch starting with <code>dependabot</code>. In this example, the excluding option means any <code>dependabot/</code> branches will not be built.</p>
<p><strong>Example 3:</strong></p>
<p>If you only want to deploy release-prefixed branches, then you could use the following rules:</p>
<ul>
<li>
<p>Include Preview branches:
<code>release/*</code></p>
</li>
<li>
<p>Exclude Preview branches:
<code>*</code></p>
</li>
</ul>
<p>This will deploy only branches starting with <code>release/</code>.</p>
