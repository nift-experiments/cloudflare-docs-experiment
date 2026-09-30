<div class="nb-description">
@markup("md", "content/.markup/bodies/16949.md")
</div>
<p>Cloudflare recommends <a href="https://vinext.dev/">vinext</a> as the default way to run Next.js applications on Cloudflare Workers. vinext gives you two starting points: scaffold a new Workers-ready app with <code>create-vinext-app</code>, or add vinext to an existing Next.js 16 app with a single non-destructive <code>vinext init</code> (your existing <code>next dev</code> keeps working). You do not need a Cloudflare-specific template either way.</p>
<p>Already on OpenNext? See <a href="#use-another-nextjs-deployment-path">other Next.js deployment paths</a>.</p>
<h2 id="what-is-next-js">What is Next.js?</h2>
<p><a href="https://nextjs.org/">Next.js</a> is a <a href="https://react.dev/">React</a> framework for building full-stack applications.</p>
<p>Next.js supports server-side rendering, client-side rendering, static generation, React Server Components, Server Actions, route handlers, and middleware.</p>
<h2 id="what-is-vinext">What is vinext?</h2>
<p><a href="https://github.com/cloudflare/vinext">vinext</a> is a Vite plugin that reimplements the Next.js API surface. You can keep your existing <code>app/</code>, <code>pages/</code>, <code>next.config.js</code>, and <code>public/</code> directories while using the Vite toolchain.</p>
<p>vinext is in beta. Before adopting it for an existing production application, run the compatibility check from your project directory and review the <a href="https://vinext.dev/compatibility">vinext compatibility dashboard</a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx vinext check</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx vinext check" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn dlx vinext check</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn dlx vinext check" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpx vinext check</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpx vinext check" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="supported-features">Supported features</h2>
<p>vinext supports most commonly used Next.js features on Cloudflare Workers:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>vinext support</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>App Router</td>
<td>Supported</td>
<td>Includes layouts, route handlers, metadata, loading, error, and not-found routes.</td>
</tr>
<tr>
<td>Pages Router</td>
<td>Supported</td>
<td>Includes <code>getStaticProps</code>, <code>getStaticPaths</code>, and <code>getServerSideProps</code>.</td>
</tr>
<tr>
<td>React Server Components</td>
<td>Supported</td>
<td>Uses Vite's React Server Components support.</td>
</tr>
<tr>
<td>Server Actions</td>
<td>Supported</td>
<td>Works with forms and server mutations.</td>
</tr>
<tr>
<td>Server-side rendering</td>
<td>Supported</td>
<td>Includes streaming rendering.</td>
</tr>
<tr>
<td>Static generation and static export</td>
<td>Supported</td>
<td>Use <code>output: &quot;export&quot;</code> for static exports.</td>
</tr>
<tr>
<td>Incremental Static Regeneration (ISR)</td>
<td>Supported</td>
<td>Uses a stale-while-revalidate caching model so Workers can serve cached content while refreshing it in the background. Refer to <a href="/cache/concepts/revalidation/#asynchronous-revalidation">asynchronous revalidation</a>.</td>
</tr>
<tr>
<td>Middleware and proxy routes</td>
<td>Supported</td>
<td>Includes <code>middleware.ts</code> and <code>proxy.ts</code>.</td>
</tr>
<tr>
<td><code>next/*</code> imports</td>
<td>Mostly supported</td>
<td>Review the compatibility dashboard for module-level details.</td>
</tr>
<tr>
<td>Cloudflare bindings</td>
<td>Supported</td>
<td>Use <code>cloudflare:workers</code> in server components, route handlers, and server actions.</td>
</tr>
<tr>
<td>Image optimization</td>
<td>Partially supported</td>
<td>Cloudflare image optimization is available at request time.</td>
</tr>
</tbody>
</table>
<p>For detailed compatibility results, refer to <a href="https://vinext.dev/compatibility">vinext compatibility</a>.</p>
<h2 id="choose-a-setup-path">Choose a setup path</h2>
<p>Most Next.js projects can start from the same workflow: open a Next.js app, check compatibility, add vinext, then deploy to Workers.</p>
<ul>
<li>Use <a href="#add-vinext-with-an-agent">Add vinext with an agent</a> if you want an agent to inspect the project and apply the migration.</li>
<li>Use <a href="#add-vinext-with-the-cli">Add vinext with the CLI</a> if you want a direct, repeatable command-line setup.</li>
<li>Use <a href="#create-a-cloudflare-ready-project">Create a Cloudflare-ready project</a> if you want to scaffold a new project already configured for Workers.</li>
</ul>
<h2 id="add-vinext-with-an-agent">Add vinext with an agent</h2>
<p>Use the vinext Agent Skill when you want a coding agent to inspect your Next.js project, run compatibility checks, update configuration, and start the vinext development server.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16950.md")
</div>
<h2 id="add-vinext-with-the-cli">Add vinext with the CLI</h2>
<p>Use <code>vinext init</code> when you want a direct command-line setup. The migration is non-destructive: your existing Next.js setup continues to work alongside vinext while you test the Cloudflare Workers deployment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16951.md")
</div>
<h2 id="create-a-cloudflare-ready-project">Create a Cloudflare-ready project</h2>
<p>Use the create-cloudflare CLI (C3) when you want to scaffold a new Next.js project already configured for Cloudflare Workers.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16953.md")
</div>
<h2 id="access-cloudflare-bindings">Access Cloudflare bindings</h2>
<p>In vinext applications deployed to Workers, use <code>cloudflare:workers</code> to access bindings from server components, route handlers, and server actions. Define bindings in your Wrangler configuration, then generate types with <a href="/workers/wrangler/commands/workers/#types"><code>wrangler types</code></a>.</p>
<p>For example, you can import <code>env</code> from <code>cloudflare:workers</code> in server-side application code to access D1, R2, KV, Durable Objects, Workers AI, Queues, Vectorize, and other bindings.</p>
<h2 id="use-another-next-js-deployment-path">Use another Next.js deployment path</h2>
<p>vinext is the recommended path for Next.js applications on Cloudflare Workers, but other deployment paths remain documented:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/framework-guides/web-apps/opennext/">OpenNext adapter</a></td>
<td>You maintain an existing OpenNext application that cannot yet migrate to vinext because of a compatibility gap.</td>
</tr>
<tr>
<td><a href="/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/">Static Next.js on Pages</a></td>
<td>Your application is a static export and you specifically want to deploy it to Cloudflare Pages.</td>
</tr>
</tbody>
</table>
