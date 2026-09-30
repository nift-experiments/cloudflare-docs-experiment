<h2 id="local-development">Local development</h2>
<p><strong>Local simulations</strong>: During local development, your Worker code always executes locally and bindings connect to locally simulated resources <a href="/workers/local-development/#remote-bindings">by default</a>. This is supported in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p><strong>Remote binding connections:</strong>: Allows you to connect to remote resources on a <a href="/workers/local-development/#remote-bindings">per-binding basis</a>. This is supported in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<table>
<thead>
<tr>
<th>Binding</th>
<th align="center">Local simulations</th>
<th align="center">Remote binding connections</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Assets</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Analytics Engine</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Browser Run</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>D1</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Durable Objects</strong></td>
<td align="center">✅</td>
<td align="center">❌ <sup><a href="#footnote-workers-bindings-per-env-mdx-1">1</a></sup></td>
</tr>
<tr>
<td><strong>Containers</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Email Bindings</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Hyperdrive</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Images</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>KV</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Media Transformations</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>mTLS</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Queues</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>R2</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Rate Limiting</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Service Bindings (multiple Workers)</strong></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Vectorize</strong></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Workflows</strong></td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
</tbody>
</table>
<h2 id="remote-development">Remote development</h2>
<p>During remote development, all of your Worker code is uploaded and executed on Cloudflare's infrastructure, and bindings always connect to remote resources. <strong>We recommend using local development with remote binding connections instead</strong> for faster iteration and debugging.</p>
<p>Supported only in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev --remote</code></a> - there is <strong>no Vite plugin equivalent</strong>.</p>
<table>
<thead>
<tr>
<th>Binding</th>
<th align="center">Remote development</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Assets</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Analytics Engine</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Browser Run</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>D1</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Durable Objects</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Containers</strong></td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>Email Bindings</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Hyperdrive</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Images</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>KV</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Media Transformations</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>mTLS</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Queues</strong></td>
<td align="center">❌</td>
</tr>
<tr>
<td><strong>R2</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Rate Limiting</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Service Bindings (multiple Workers)</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Vectorize</strong></td>
<td align="center">✅</td>
</tr>
<tr>
<td><strong>Workflows</strong></td>
<td align="center">❌</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-workers-bindings-per-env-mdx-1">Refer to [Using remote resources with Durable Objects and Workflows](/workers/local-development/#using-remote-resources-with-durable-objects-and-workflows) for recommended workarounds.</li></ol></section>
