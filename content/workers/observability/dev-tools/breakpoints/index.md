<h2 id="debug-via-breakpoints">Debug via breakpoints</h2>
<p>When developing a Worker locally using Wrangler or Vite, you can debug via breakpoints in your Worker. Breakpoints provide the ability to review what is happening at a given point in the execution of your Worker. Breakpoint functionality exists in both DevTools and VS Code.</p>
<p>For more information on breakpoint debugging via Chrome's DevTools, refer to <a href="https://developer.chrome.com/docs/devtools/javascript/breakpoints/">Chrome's article on breakpoints</a>.</p>
<h3 id="vscode-debug-terminals">VSCode debug terminals</h3>
<p>Using VSCode's built-in <a href="https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal">JavaScript Debug Terminals</a>, all you have to do is open a JS debug terminal (<code>Cmd + Shift + P</code> and then type <code>javascript debug</code>) and run <code>wrangler dev</code> (or <code>vite dev</code>) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.</p>
<h3 id="setup-vs-code-to-use-breakpoints-with-launch-json-files">Setup VS Code to use breakpoints with <code>launch.json</code> files</h3>
<p>To setup VS Code for breakpoint debugging in your Worker project:</p>
<ol>
<li>Create a <code>.vscode</code> folder in your project's root folder if one does not exist.</li>
<li>Within that folder, create a <code>launch.json</code> file with the following content:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;configurations&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Listen Wrangler&quot;,&#10;			&quot;type&quot;: &quot;node&quot;,&#10;			&quot;request&quot;: &quot;attach&quot;,&#10;			&quot;port&quot;: 9229,&#10;			&quot;cwd&quot;: &quot;/&quot;,&#10;			&quot;resolveSourceMapLocations&quot;: null,&#10;			&quot;attachExistingChildren&quot;: false,&#10;			&quot;autoAttachChildProcesses&quot;: false,&#10;			&quot;sourceMaps&quot;: true // works with or without this line&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;Launch Wrangler&quot;,&#10;			&quot;command&quot;: &quot;npm run dev&quot;,&#10;			&quot;type&quot;: &quot;node-terminal&quot;,&#10;			&quot;request&quot;: &quot;launch&quot;,&#10;			&quot;console&quot;: &quot;integratedTerminal&quot;,&#10;			&quot;sourceMaps&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="3">
<li>
<p>Open your project in VS Code, open a new terminal window from VS Code, and run <code>npx wrangler dev</code> to start the local dev server.</p>
</li>
<li>
<p>At the top of the <strong>Run &amp; Debug</strong> panel, you should see an option to select a configuration. Choose <strong>Wrangler</strong>, and select the play icon. <strong>Wrangler: Remote Process [0]</strong> should show up in the Call Stack panel on the left.</p>
</li>
<li>
<p>Go back to a <code>.js</code> or <code>.ts</code> file in your project and add at least one breakpoint.</p>
</li>
<li>
<p>Open your browser and go to the Worker's local URL (default <code>http://127.0.0.1:8787</code>). The breakpoint should be hit, and you should be able to review details about your code at the specified line.</p>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17062.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17061.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/local-development/">Local Development</a> - Develop your Workers and connected resources locally via Wrangler and <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, for a fast, accurate feedback loop.</li>
</ul>
