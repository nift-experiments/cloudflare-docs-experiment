<p>Cloudflare Pages' build environment has broad support for a variety of languages, such as Ruby, Node.js, Python, PHP, and Go.</p>
<p>If you need to use a <a href="#override-default-versions">specific version</a> of a language, (for example, Node.js or Ruby) you can specify it by providing an associated environment variable in your build configuration, or setting the relevant file in your source code.</p>
<h2 id="supported-languages-and-tools">Supported languages and tools</h2>
<p>In the following tables, review the preinstalled versions for languages and tools included in the Cloudflare Pages' build image, and the environment variables and/or files available for <a href="#override-default-versions">overriding the preinstalled version</a>:</p>
<h3 id="languages-and-runtime">Languages and runtime</h3>
<div class="nb-tabs" data-nb-tabs><section class="nb-tab-panel" data-nb-tab-label="v3"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Go</td><td>1.24.3</td><td>Any version</td><td>GO_VERSION</td><td></td></tr><tr><td>Node.js</td><td>22.16.0</td><td>Any version</td><td>NODE_VERSION</td><td>.nvmrc, .node-version</td></tr><tr><td>Bun</td><td>1.2.15</td><td>Any version</td><td>BUN_VERSION</td><td></td></tr><tr><td>Python</td><td>3.13.3</td><td>Any version</td><td>PYTHON_VERSION</td><td>.python-version, runtime.txt</td></tr><tr><td>Ruby</td><td>3.4.4</td><td>Any version</td><td>RUBY_VERSION</td><td>.ruby-version</td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v2"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Go</td><td>1.21.0</td><td>Any version</td><td>GO_VERSION</td><td></td></tr><tr><td>Node.js</td><td>18.17.1</td><td>Any version</td><td>NODE_VERSION</td><td>.nvmrc, .node-version</td></tr><tr><td>Bun</td><td>1.1.33</td><td>Any version</td><td>BUN_VERSION</td><td></td></tr><tr><td>Python</td><td>3.11.5</td><td>Any version</td><td>PYTHON_VERSION</td><td>.python-version, runtime.txt</td></tr><tr><td>Ruby</td><td>3.2.2</td><td>Any version</td><td>RUBY_VERSION</td><td>.ruby-version</td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v1"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Clojure</td><td></td><td></td><td></td><td></td></tr><tr><td>Elixir</td><td>1.7</td><td>1.7 only</td><td></td><td></td></tr><tr><td>Erlang</td><td>21</td><td>21 only</td><td></td><td></td></tr><tr><td>Go</td><td>1.14.4</td><td>Any version</td><td>GO_VERSION</td><td></td></tr><tr><td>Java</td><td>8</td><td>8 only</td><td></td><td></td></tr><tr><td>Node.js</td><td>12.18.0</td><td>Any version</td><td>NODE_VERSION</td><td>.nvmrc, .node-version</td></tr><tr><td>PHP</td><td>5.6</td><td>5.6, 7.2, 7.4 only</td><td>PHP_VERSION</td><td></td></tr><tr><td>Python</td><td>2.7</td><td>2.7, 3.5, 3.7 only</td><td>PYTHON_VERSION</td><td>runtime.txt, Pipfile</td></tr><tr><td>Ruby</td><td>2.7.1</td><td>Any version between 2.6.2 and 2.7.5</td><td>RUBY_VERSION</td><td>.ruby-version</td></tr><tr><td>Swift</td><td>5.2.5</td><td>Any 5.x version</td><td>SWIFT_VERSION</td><td>.swift-version</td></tr><tr><td>.NET</td><td>3.1.302</td><td></td><td></td><td></td></tr></tbody></table></section></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="any-version">Any version</h3>
@markup("md", "content/.markup/bodies/11075.md")
</aside>
<h3 id="tools">Tools</h3>
<div class="nb-tabs" data-nb-tabs><section class="nb-tab-panel" data-nb-tab-label="v3"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Bundler</td><td>2.6.9</td><td>Corresponds with Ruby version</td><td></td><td></td></tr><tr><td>Embedded Dart Sass</td><td>1.62.1</td><td>Up to 1.62.1</td><td>EMBEDDED_DART_SASS_VERSION</td><td></td></tr><tr><td>gem</td><td>3.6.9</td><td>Corresponds with Ruby version</td><td></td><td></td></tr><tr><td>Hugo</td><td>0.147.7</td><td>Any version</td><td>HUGO_VERSION</td><td></td></tr><tr><td>npm</td><td>10.9.2</td><td>Corresponds with Node.js version</td><td></td><td></td></tr><tr><td>pip</td><td>25.1.1</td><td>Corresponds with Python version</td><td></td><td></td></tr><tr><td>pipx</td><td>1.7.1</td><td></td><td></td><td></td></tr><tr><td>pnpm</td><td>10.11.1</td><td>Any version</td><td>PNPM_VERSION</td><td></td></tr><tr><td>Poetry</td><td>2.1.3</td><td></td><td></td><td></td></tr><tr><td>Yarn</td><td>4.9.1</td><td>Any version</td><td>YARN_VERSION</td><td></td></tr><tr><td>Zola</td><td>0.22.1</td><td>Any version</td><td>ZOLA_VERSION</td><td></td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v2"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Bundler</td><td>2.4.10</td><td>Corresponds with Ruby version</td><td></td><td></td></tr><tr><td>Embedded Dart Sass</td><td>1.62.1</td><td>Up to 1.62.1</td><td>EMBEDDED_DART_SASS_VERSION</td><td></td></tr><tr><td>gem</td><td>3.4.10</td><td>Corresponds with Ruby version</td><td></td><td></td></tr><tr><td>Hugo</td><td>0.118.2</td><td>Any version</td><td>HUGO_VERSION</td><td></td></tr><tr><td>npm</td><td>9.6.7</td><td>Corresponds with Node.js version</td><td></td><td></td></tr><tr><td>pip</td><td>23.2.1</td><td>Corresponds with Python version</td><td></td><td></td></tr><tr><td>pipx</td><td>1.2.0</td><td></td><td></td><td></td></tr><tr><td>pnpm</td><td>8.7.1</td><td>Any version</td><td>PNPM_VERSION</td><td></td></tr><tr><td>Poetry</td><td>1.6.1</td><td></td><td></td><td></td></tr><tr><td>Yarn</td><td>3.6.3</td><td>Any version</td><td>YARN_VERSION</td><td></td></tr><tr><td>Zola</td><td>0.22.1</td><td>Any version</td><td>ZOLA_VERSION</td><td></td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v1"><table><thead><tr><th>Tool</th><th>Default version</th><th>Supported versions</th><th>Environment variable</th><th>File</th></tr></thead><tbody><tr><td>Boot</td><td>2.5.2</td><td>2.5.2</td><td></td><td></td></tr><tr><td>Bower</td><td></td><td></td><td></td><td></td></tr><tr><td>Cask</td><td></td><td></td><td></td><td></td></tr><tr><td>Composer</td><td></td><td></td><td></td><td></td></tr><tr><td>Doxygen</td><td>1.8.6</td><td></td><td></td><td></td></tr><tr><td>Emacs</td><td>25</td><td></td><td></td><td></td></tr><tr><td>Gutenberg</td><td>(requires environment variable)</td><td>Any version</td><td>GUTENBERG_VERSION</td><td></td></tr><tr><td>Hugo</td><td>0.54.0</td><td>Any version</td><td>HUGO_VERSION</td><td></td></tr><tr><td>GNU Make</td><td>3.8.1</td><td></td><td></td><td></td></tr><tr><td>ImageMagick</td><td>6.7.7</td><td></td><td></td><td></td></tr><tr><td>jq</td><td>1.5</td><td></td><td></td><td></td></tr><tr><td>Leiningen</td><td></td><td></td><td></td><td></td></tr><tr><td>OptiPNG</td><td>0.6.4</td><td></td><td></td><td></td></tr><tr><td>npm</td><td>Corresponds with Node.js version</td><td>Any version</td><td>NPM_VERSION</td><td></td></tr><tr><td>pip</td><td>Corresponds with Python version</td><td></td><td></td><td></td></tr><tr><td>Pipenv</td><td>Latest version</td><td></td><td></td><td></td></tr><tr><td>sqlite3</td><td>3.11.0</td><td></td><td></td><td></td></tr><tr><td>Yarn</td><td>1.22.4</td><td>Any version from 0.2.0 to 1.22.19</td><td>YARN_VERSION</td><td></td></tr><tr><td>Zola</td><td>(requires environment variable)</td><td>Any version from 0.5.0 and up</td><td>ZOLA_VERSION</td><td></td></tr></tbody></table></section></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="any-version-1">Any version</h3>
@markup("md", "content/.markup/bodies/11074.md")
</aside>
<h3 id="frameworks">Frameworks</h3>
<p>To use a specific version of a framework, specify it in the project's package manager configuration file.
For example, if you use Gatsby, your <code>package.json</code> should include the following:</p>
<pre><code>&quot;dependencies&quot;: {&#10;	&quot;gatsby&quot;: &quot;^5.13.7&quot;,&#10;}&#10;</code></pre>
<p>When your build starts, if not already <a href="/pages/configuration/build-caching/">cached</a>, version 5.13.7 of Gatsby will be installed using <code>npm install</code>.</p>
<h2 id="advanced-settings">Advanced Settings</h2>
<h3 id="override-default-versions">Override default versions</h3>
<p>To override default versions of languages and tools in the build system, you can either set the desired version through environment variables or by adding files to your project.</p>
<p>To set the version using environment variables, you can:</p>
<ol>
<li>Find the environment variable name for the language or tool in <a href="/pages/configuration/build-image/#supported-languages-and-tools">this table</a>.</li>
<li>Add the environment variable on the dashboard by going to <strong>Settings</strong> &gt; <strong>Environment variables</strong> in your Pages project, or <a href="/workers/configuration/environment-variables/#add-environment-variables-via-wrangler">add the environment variable via Wrangler</a>.</li>
</ol>
<p>Or, to set the version by adding a file to your project, you can:</p>
<ol>
<li>Find the file name for the language or tool in <a href="/pages/configuration/build-image/#supported-languages-and-tools">this table</a>.</li>
<li>Add the specified file name to the root directory of your project, and add the desired version number as the contents of the file.</li>
</ol>
<p>For example, if you were previously relying on the default version of Node.js in the v1 build system, to migrate to v2, you must specify that you need Node.js <code>12.18.0</code> by setting a <code>NODE_VERSION = 12.18.0</code> environment variable or by adding a <code>.node-version</code> or <code>.nvmrc</code> file to your project with <code>12.18.0</code> added as the contents to the file.</p>
<h3 id="skip-dependency-install">Skip dependency install</h3>
<p>You can add the following environment variable to disable automatic dependency installation, and run a custom install command instead.</p>
<table>
<thead>
<tr>
<th>Build variable</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SKIP_DEPENDENCY_INSTALL</code></td>
<td><code>1</code> or <code>true</code></td>
</tr>
</tbody>
</table>
<h2 id="v3-build-system">v3 build system</h2>
<p>The v3 build system updates the default tools, libraries and languages to their LTS versions, as of May 2025.</p>
<h3 id="v2-to-v3-migration">v2 to v3 Migration</h3>
<p>To migrate to this new version, configure your Pages project settings in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Deployments** > **All deployments** > and select the latest version.
<p>If you were previously relying on the default versions of any languages or tools in the build system, your build may fail when migrating to v3. To fix this, you must specify the version you wish to use by <a href="/pages/configuration/build-image/#overriding-default-versions">overriding</a> the default versions.</p>
<h3 id="limitations">Limitations</h3>
<p>The following features are not currently supported when using the v3 build system:</p>
<ul>
<li>Specifying Node.js versions as codenames (for example, <code>hydrogen</code> or <code>lts/hydrogen</code>).</li>
<li>Detecting Yarn version from <code>yarn.lock</code> file version.</li>
<li>Detecting pnpm version detection based <code>pnpm-lock.yaml</code> file version.</li>
<li>Detecting Node.js and package managers from <code>package.json</code> -&gt; <code>&quot;engines&quot;</code>.</li>
<li><code>pipenv</code> and <code>Pipfile</code> support.</li>
</ul>
<h2 id="build-environment">Build environment</h2>
<p>Cloudflare Pages builds are run in a <a href="https://gvisor.dev/docs/">gVisor</a> container.</p>
<div class="nb-tabs" data-nb-tabs><section class="nb-tab-panel" data-nb-tab-label="v3"><table><thead><tr><th>Property</th><th>Value</th></tr></thead><tbody><tr><td>Build environment</td><td>Ubuntu `22.04.2`</td></tr><tr><td>Architecture</td><td>x86_64</td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v2"><table><thead><tr><th>Property</th><th>Value</th></tr></thead><tbody><tr><td>Build environment</td><td>Ubuntu `22.04.2`</td></tr><tr><td>Architecture</td><td>x86_64</td></tr></tbody></table></section><section class="nb-tab-panel" data-nb-tab-label="v1"><table><thead><tr><th>Property</th><th>Value</th></tr></thead><tbody><tr><td>Build environment</td><td>Ubuntu `20.04.5`</td></tr><tr><td>Architecture</td><td>x86_64</td></tr></tbody></table></section></div>
<h2 id="build-image-policy">Build Image Policy</h2>
<h3 id="build-image-version-deprecation">Build Image Version Deprecation</h3>
<p>If you are currently using the v1 or v2 build image, your project will be automatically moved to v3:</p>
<ul>
<li><strong>v1 build image</strong>: If you are using the Pages v1 build image, your project will be automatically moved to v3 on September 15, 2026.</li>
<li><strong>v2 build image</strong>: If you are using the Pages v2 build image, your project will be automatically moved to v3 on February 23, 2027.</li>
</ul>
<p>You will receive 6 months’ notice before the deprecation date via the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email.</p>
<p>Going forward, the v3 build image will receive rolling updates to preinstalled software per the policy below. There will be no further build image version changes.</p>
<h3 id="preinstalled-software-updates">Preinstalled Software Updates</h3>
<p>Preinstalled software (languages and tools) will be updated before reaching end-of-life (EOL). These updates apply only if you have not <a href="/pages/configuration/build-image/#override-default-versions">overridden the default version</a>.</p>
<ul>
<li><strong>Minor version updates</strong>: May be updated to the latest available minor version without notice. For tools that do not follow semantic versioning (e.g., Bun or Hugo), updates that may contain breaking changes will receive 3 months’ notice.</li>
<li><strong>Major version updates</strong>: Updated to the next stable long-term support (LTS) version with 3 months’ notice.</li>
</ul>
<p><strong>How you'll be notified (for changes requiring notice):</strong></p>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a></li>
<li>Dashboard notifications for projects that will receive the update</li>
<li>Email notifications to project owners</li>
</ul>
<p>To maintain a specific version and avoid automatic updates, <a href="/pages/configuration/build-image/#override-default-versions">override the default version</a>.</p>
<h3 id="best-practices">Best Practices</h3>
<p>To avoid unexpected build failures:</p>
<ul>
<li><strong>Monitor announcements</strong> via the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email</li>
<li><strong>Plan for migration</strong> when you receive update notices</li>
<li><strong>Pin specific versions</strong> of critical preinstalled software by <a href="/pages/configuration/build-image/#override-default-versions">overriding default versions</a></li>
</ul>
