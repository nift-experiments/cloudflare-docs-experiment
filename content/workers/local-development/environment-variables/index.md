<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16291.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16290.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/16289.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/16288.md")
</aside>
<p>To set different secrets for each Cloudflare environment, create files named <code>.dev.vars.&lt;environment-name&gt;</code> or <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you select a Cloudflare environment in your local development, the corresponding environment-specific file will be loaded ahead of the generic <code>.dev.vars</code> (or <code>.env</code>) file.</p>
<ul>
<li>When using <code>.dev.vars.&lt;environment-name&gt;</code> files, all secrets must be defined per environment. If <code>.dev.vars.&lt;environment-name&gt;</code> exists then only this will be loaded; the <code>.dev.vars</code> file will not be loaded.</li>
<li>In contrast, all matching <code>.env</code> files are loaded and the values are merged. For each variable, the value from the most specific file is used, with the following precedence:
<ul>
<li><code>.env.&lt;environment-name&gt;.local</code> (most specific)</li>
<li><code>.env.local</code></li>
<li><code>.env.&lt;environment-name&gt;</code></li>
<li><code>.env</code> (least specific)</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="controlling-env-handling">Controlling `.env` handling</h3>
@markup("md", "content/.markup/bodies/16287.md")
</aside>
<h3 id="basic-setup">Basic setup</h3>
<p>Here are steps to set up environment variables for local development using either <code>.dev.vars</code> or <code>.env</code> files.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16292.md")
</div>
<h2 id="multiple-local-environments">Multiple local environments</h2>
<p>To simulate different local environments, you can provide environment-specific files.
For example, you might have a <code>staging</code> environment that requires different settings than your development environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16293.md")
</div>
<h2 id="learn-more">Learn more</h2>
<ul>
<li>To learn how to configure multiple environments in Wrangler configuration, <a href="/workers/wrangler/environments/#_top">read the documentation</a>.</li>
<li>To learn how to use Wrangler environments and Vite environments together, <a href="/workers/vite-plugin/reference/cloudflare-environments/">read the Vite plugin documentation</a></li>
</ul>
