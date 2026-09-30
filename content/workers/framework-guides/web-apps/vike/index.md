<p>You can deploy your <a href="https://vike.dev">Vike</a> app to Cloudflare using the Vike extension <a href="https://vike.dev/vike-photon"><code>vike-photon</code></a>.</p>
<p>All app types (SSR/SPA/SSG) are supported.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="already-have-a-vike-project">Already have a Vike project?</h3>
@markup("md", "content/.markup/bodies/16897.md")
</aside>
<div class="nb-interactive-component" data-cf-component="AutoconfigDiagram"></div>
<h2 id="what-is-vike">What is Vike?</h2>
<p><a href="https://vike.dev">Vike</a> is a Next.js/Nuxt alternative for advanced applications, powered by a modular architecture for unprecedented flexibility and stability.</p>
<h2 id="new-app">New app</h2>
<p>Use <a href="https://vike.dev/new">vike.dev/new</a> to scaffold a new Vike app that uses <code>vike-photon</code> with <code>@photonjs/cloudflare</code>.</p>
<h2 id="add-to-existing-app">Add to existing app</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16898.md")
</div>
<h2 id="cloudflare-apis-bindings">Cloudflare APIs (bindings)</h2>
<p>To access Cloudflare APIs (such as <a href="/d1/">D1</a> and <a href="/kv/">KV</a>), use <a href="/workers/runtime-apis/bindings/">bindings</a> which are available via the <code>env</code> object <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">imported from <code>cloudflare:workers</code></a>.</p>
<pre><code class="language-ts">import { env } from &#x27;cloudflare:workers&#x27;&#10;// Key-value store&#10;env.KV.get(&#x27;my-key&#x27;)&#10;// Environment variable&#10;env.LOG_LEVEL&#10;// ...&#10;</code></pre>
<blockquote>
<p>Example of using Cloudflare D1:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create vike@latest -- --react --hono --drizzle --cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create vike@latest -- --react --hono --drizzle --cloudflare" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create vike --react --hono --drizzle --cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create vike --react --hono --drizzle --cloudflare" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create vike@latest --react --hono --drizzle --cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create vike@latest --react --hono --drizzle --cloudflare" aria-label="Copy to clipboard">Copy</button></div></div>
Or go to [vike.dev/new](https://vike.dev/new) and select `Cloudflare` with an ORM.
</blockquote>
<h2 id="typescript">TypeScript</h2>
<p>If you use TypeScript, run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> whenever you change your Cloudflare configuration to update the <code>worker-configuration.d.ts</code> file.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then commit:</p>
<pre><code class="language-bash">git commit -am &quot;update cloudflare types&quot;&#10;</code></pre>
<p>Make sure TypeScript loads it:</p>
<pre><code class="language-diff">  {&#10;    &quot;compilerOptions&quot;: {&#10;&#43;     &quot;types&quot;: [&quot;./worker-configuration.d.ts&quot;]&#10;   }&#10;  }&#10;</code></pre>
<p>See also: <a href="/workers/languages/typescript/">Cloudflare Workers &gt; TypeScript</a>.</p>
<h2 id="see-also">See also</h2>
<ul>
<li><a href="https://vike.dev/cloudflare">Vike Docs &gt; Cloudflare</a></li>
</ul>
