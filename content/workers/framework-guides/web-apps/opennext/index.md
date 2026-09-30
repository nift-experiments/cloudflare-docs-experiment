<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-path">Recommended path</h3>
@markup("md", "content/.markup/bodies/16945.md")
</aside>
<p>Use this guide to maintain an existing OpenNext application. Migrate to vinext when compatibility allows.</p>
<p><a href="https://opennext.js.org/">OpenNext</a> adapts the output of <code>next build</code> so it can run on different platforms, including Cloudflare Workers.</p>
<h2 id="supported-features">Supported features</h2>
<p>Most Next.js features are supported by the Cloudflare OpenNext adapter:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Cloudflare OpenNext adapter</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>App Router</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Pages Router</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Route Handlers</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>React Server Components</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Static Site Generation (SSG)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Server-Side Rendering (SSR)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Incremental Static Regeneration (ISR)</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Server Actions</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Response streaming</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Asynchronous work with <code>next/after</code></td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Middleware</td>
<td>Supported</td>
<td></td>
</tr>
<tr>
<td>Image optimization</td>
<td>Supported</td>
<td>Supported through <a href="/images/">Cloudflare Images</a>.</td>
</tr>
<tr>
<td>Partial Prerendering (PPR)</td>
<td>Supported</td>
<td>PPR is experimental in Next.js.</td>
</tr>
<tr>
<td>Composable Caching (<code>&quot;use cache&quot;</code>)</td>
<td>Supported</td>
<td>Composable Caching is experimental in Next.js.</td>
</tr>
<tr>
<td>Node.js in Middleware</td>
<td>Not yet supported</td>
<td>Node.js middleware introduced in Next.js 15.2 is not yet supported.</td>
</tr>
</tbody>
</table>
<p>For detailed OpenNext documentation, refer to <a href="https://opennext.js.org/cloudflare">OpenNext for Cloudflare</a>.</p>
<h2 id="configure-opennext-manually">Configure OpenNext manually</h2>
<p>Wrangler automatic configuration uses vinext for Next.js projects. To use OpenNext, configure the adapter manually.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16948.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-builds">Workers Builds</h3>
@markup("md", "content/.markup/bodies/16943.md")
</aside>
