<p>The Cloudflare Vite plugin has debugging enabled by default and listens on port <code>9229</code>.
You may choose a custom port or disable debugging by setting the <code>inspectorPort</code> option in the <a href="/workers/vite-plugin/reference/api#interface-pluginconfig">plugin config</a>.
There are two recommended methods for debugging your Workers during local development:</p>
<h2 id="devtools">DevTools</h2>
<p>When running <code>vite dev</code> or <code>vite preview</code>, a <code>/__debug</code> route is added that provides access to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches">Cloudflare's implementation</a> of <a href="https://developer.chrome.com/docs/devtools/overview">Chrome's DevTools</a>.
Navigating to this route will open a DevTools tab for each of the Workers in your application.</p>
<p>Once the tab(s) are open, you can make a request to your application and start debugging your Worker code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17392.md")
</aside>
<h2 id="vs-code">VS Code</h2>
<p>To set up <a href="https://code.visualstudio.com/">VS Code</a> to support breakpoint debugging in your application, you should create a <code>.vscode/launch.json</code> file that contains the following configuration:</p>
<pre><code class="language-json">{&#10;	&quot;configurations&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;&lt;NAME_OF_WORKER&gt;&quot;,&#10;			&quot;type&quot;: &quot;node&quot;,&#10;			&quot;request&quot;: &quot;attach&quot;,&#10;			&quot;websocketAddress&quot;: &quot;ws://localhost:9229/&lt;NAME_OF_WORKER&gt;&quot;,&#10;			&quot;resolveSourceMapLocations&quot;: null,&#10;			&quot;attachExistingChildren&quot;: false,&#10;			&quot;autoAttachChildProcesses&quot;: false,&#10;			&quot;sourceMaps&quot;: true&#10;		}&#10;	],&#10;	&quot;compounds&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Debug Workers&quot;,&#10;			&quot;configurations&quot;: [&quot;&lt;NAME_OF_WORKER&gt;&quot;],&#10;			&quot;stopAll&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Here, <code>&lt;NAME_OF_WORKER&gt;</code> indicates the name of the Worker as specified in your Worker config file.
If you have used the <code>inspectorPort</code> option to set a custom port then this should be the value provided in the <code>websocketaddress</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17391.md")
</aside>
<p>With this set up, you can run <code>vite dev</code> or <code>vite preview</code> and then select <strong>Debug Workers</strong> at the top of the <strong>Run &amp; Debug</strong> panel to start debugging.</p>
