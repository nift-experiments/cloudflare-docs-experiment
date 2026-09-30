<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17365.md")
</aside>
<p>You can use regular Node.js tools to debug your Workers. Setting breakpoints,
watching values and inspecting the call stack are all examples of things you can
do with a debugger.</p>
<h2 id="visual-studio-code">Visual Studio Code</h2>
<h3 id="create-configuration">Create configuration</h3>
<p>The easiest way to debug a Worker in VSCode is to create a new configuration.</p>
<p>Open the <strong>Run and Debug</strong> menu in the VSCode activity bar and create a
<code>.vscode/launch.json</code> file that contains the following:</p>
<pre><code class="language-json">&#45;--&#10;filename: .vscode/launch.json&#10;&#45;--&#10;{&#10;  &quot;configurations&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;Miniflare&quot;,&#10;      &quot;type&quot;: &quot;node&quot;,&#10;      &quot;request&quot;: &quot;attach&quot;,&#10;      &quot;port&quot;: 9229,&#10;      &quot;cwd&quot;: &quot;/&quot;,&#10;      &quot;resolveSourceMapLocations&quot;: null,&#10;      &quot;attachExistingChildren&quot;: false,&#10;      &quot;autoAttachChildProcesses&quot;: false,&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>From the <strong>Run and Debug</strong> menu in the activity bar, select the <code>Miniflare</code>
configuration, and click the green play button to start debugging.</p>
<h2 id="webstorm">WebStorm</h2>
<p>Create a new configuration, by clicking <strong>Add Configuration</strong> in the top right.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-node-add.png" alt="WebStorm add configuration button" /></p>
<p>Click the <strong>plus</strong> button in the top left of the popup and create a new
<strong>Node.js/Chrome</strong> configuration. Set the <strong>Host</strong> field to <code>localhost</code> and the
<strong>Port</strong> field to <code>9229</code>. Then click <strong>OK</strong>.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-settings.png" alt="WebStorm Node.js debug configuration" /></p>
<p>With the new configuration selected, click the green debug button to start
debugging.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-node-run.png" alt="WebStorm configuration debug button" /></p>
<h2 id="devtools">DevTools</h2>
<p>Breakpoints can also be added via the Workers DevTools. For more information,
<a href="/workers/observability/dev-tools">read the guide</a>
in the Cloudflare Workers docs.</p>
