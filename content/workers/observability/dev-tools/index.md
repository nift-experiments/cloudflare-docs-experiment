<h2 id="using-devtools">Using DevTools</h2>
<p>When running your Worker locally using the <a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler CLI</a> (<code>wrangler dev</code>) or using <a href="https://vite.dev/">Vite</a> with the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>, you automatically have access to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches">Cloudflare's implementation</a> of <a href="https://developer.chrome.com/docs/devtools/overview">Chrome DevTools</a>.</p>
<p>You can use Chrome DevTools to:</p>
<ul>
<li>View logs directly in the Chrome console</li>
<li><a href="/workers/observability/dev-tools/breakpoints/">Debug code by setting breakpoints</a></li>
<li><a href="/workers/observability/dev-tools/cpu-usage/">Profile CPU usage</a></li>
<li><a href="/workers/observability/dev-tools/memory-usage/">Observe memory usage and debug memory leaks in your code that can cause out-of-memory (OOM) errors</a></li>
</ul>
<h2 id="opening-devtools">Opening DevTools</h2>
<h3 id="wrangler">Wrangler</h3>
<ul>
<li>Run your Worker locally, by running <code>wrangler dev</code></li>
<li>Press the <code>D</code> key from your terminal to open DevTools in a browser tab</li>
</ul>
<h3 id="vite">Vite</h3>
<ul>
<li>Run your Worker locally by running <code>vite</code></li>
<li>In a new Chrome tab, open the debug URL that shows in your console (for example, <code>http://localhost:5173/__debug</code>)</li>
</ul>
<h3 id="dashboard-editor-playground">Dashboard editor &amp; playground</h3>
<p>Both the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and the <a href="https://workers.cloudflare.com/playground">Worker's Playground</a> include DevTools in the UI.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/local-development/">Local development</a> - Develop your Workers and connected resources locally via Wrangler and workerd, for a fast, accurate feedback loop.</li>
</ul>
