<p>Custom builds are a way for you to customize how your code is compiled, before being processed by Wrangler.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15928.md")
</aside>
<h2 id="configure-custom-builds">Configure custom builds</h2>
<p>Custom builds are configured by adding a <code>[build]</code> section in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, and using the following options for configuring your custom build.</p>
<ul>
<li>
<p><code>command</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The command used to build your Worker. On Linux and macOS, the command is executed in the <code>sh</code> shell and the <code>cmd</code> shell for Windows. The <code>&amp;&amp;</code> and <code>||</code> shell operators may be used. This command will be run as part of <code>wrangler dev</code> and <code>npx wrangler deploy</code>.</li>
</ul>
</li>
<li>
<p><code>cwd</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The directory in which the command is executed.</li>
</ul>
</li>
<li>
<p><code>watch_dir</code> <span class="nb-type">string | string[]</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The directory to watch for changes while using <code>wrangler dev</code>. Defaults to the current working directory.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15929.md")
</div>
<h2 id="wrangler-command-environment-variable"><code>WRANGLER_COMMAND</code> environment variable</h2>
<p>When Wrangler runs your custom build command, it sets the <code>WRANGLER_COMMAND</code> environment variable so your build script can detect which Wrangler command triggered the build. This allows you to customize the build process based on the deployment context.</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Wrangler command triggered</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dev</code></td>
<td><code>wrangler dev</code></td>
</tr>
<tr>
<td><code>deploy</code></td>
<td><code>wrangler deploy</code></td>
</tr>
<tr>
<td><code>versions upload</code></td>
<td><code>wrangler versions upload</code></td>
</tr>
<tr>
<td><code>types</code></td>
<td><code>wrangler types</code></td>
</tr>
</tbody>
</table>
<p>For example, you can use this to apply different build settings for development and production:</p>
<pre><code class="language-bash">&#35;!/bin/bash&#10;if [ &quot;$WRANGLER_COMMAND&quot; = &quot;dev&quot; ]; then&#10;  echo &quot;Building for development...&quot;&#10;  &#35; run a development build&#10;else&#10;  echo &quot;Building for production...&quot;&#10;  &#35; run a production build&#10;fi&#10;</code></pre>
