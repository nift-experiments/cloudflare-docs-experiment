<p>This tutorial takes you through the steps needed to adapt a Vite project to use the Cloudflare Vite plugin.
Much of the content can also be applied to adapting existing Vite projects and to front-end frameworks other than React.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16024.md")
</aside>
<h2 id="introduction">Introduction</h2>
<p>In this tutorial, you will create a React SPA that can be deployed as a Worker with static assets.
You will then add an API Worker that can be accessed from the front-end code.
You will develop, build, and preview the application using Vite before finally deploying to Cloudflare.</p>
<h2 id="set-up-and-configure-the-react-spa">Set up and configure the React SPA</h2>
<h3 id="scaffold-a-vite-project">Scaffold a Vite project</h3>
<p>Start by creating a React TypeScript project with Vite.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create vite@latest -- cloudflare-vite-tutorial --template react-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create vite@latest -- cloudflare-vite-tutorial --template react-ts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create vite cloudflare-vite-tutorial --template react-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create vite cloudflare-vite-tutorial --template react-ts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create vite@latest cloudflare-vite-tutorial --template react-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create vite@latest cloudflare-vite-tutorial --template react-ts" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Next, open the <code>cloudflare-vite-tutorial</code> directory in your editor of choice.</p>
<h3 id="add-the-cloudflare-dependencies">Add the Cloudflare dependencies</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="add-the-cloudflare-vite-plugin-to-your-project">Add the Cloudflare Vite plugin to your project</h3>
<p>In your <code>vite.config.ts</code>, add the Cloudflare Vite plugin after your framework plugin:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import react from &quot;@vitejs/plugin-react&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [react(), cloudflare()],&#10;});&#10;</code></pre>
<p>The Cloudflare Vite plugin does not require any configuration by default and will look for a <code>wrangler.jsonc</code>, <code>wrangler.json</code>, or <code>wrangler.toml</code> in the root of your application.</p>
<h3 id="create-your-worker-config-file">Create your Worker config file</h3>
<p>Create a <code>wrangler.jsonc</code> file in the root of your project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16025.md")
</div>
<p>The <a href="/workers/static-assets/routing/single-page-application/"><code>not_found_handling</code></a> value has been set to <code>single-page-application</code>.
This means that all not-found requests will serve the <code>index.html</code> file, which is required for React Router and other client-side routing solutions.</p>
<p>With the Cloudflare plugin, the <code>assets</code> routing configuration is used in place of Vite's default behavior.
This ensures that your application's <a href="/workers/static-assets/routing/">routing configuration</a> works the same way while developing as it does when deployed to production.</p>
<p>The <a href="/workers/static-assets/binding/#directory"><code>directory</code></a> field is not used when configuring assets with Vite.
The <code>directory</code> in the output configuration will automatically point to the client build output.
Refer to <a href="/workers/vite-plugin/reference/static-assets/">Static Assets</a> for more information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16023.md")
</aside>
<h3 id="update-the-gitignore-file">Update the <code>.gitignore</code> file</h3>
<p>When developing Workers, additional files are used and/or generated that should not be stored in Git.
Add the following lines to your <code>.gitignore</code> file:</p>
<pre><code class="language-txt">.wrangler&#10;.dev.vars*&#10;</code></pre>
<h3 id="run-the-development-server">Run the development server</h3>
<p>Run your framework's development command to start the Vite development server and verify that your application is working as expected.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For a purely front-end application, you could now build, preview, and deploy your application.
The following sections will show you how to go further and add an API Worker.</p>
<h2 id="add-an-api-worker">Add an API Worker</h2>
<h3 id="add-workers-typescript-types">Add Workers TypeScript types</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Create a <code>tsconfig.worker.json</code> that extends your Node TypeScript configuration and adds the Workers types:</p>
<pre><code class="language-jsonc">{&#10;	&quot;extends&quot;: &quot;./tsconfig.node.json&quot;,&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;tsBuildInfoFile&quot;: &quot;./node_modules/.tmp/tsconfig.worker.tsbuildinfo&quot;,&#10;		&quot;types&quot;: [&quot;@cloudflare/workers-types/2023-07-01&quot;, &quot;vite/client&quot;],&#10;	},&#10;	&quot;include&quot;: [&quot;worker&quot;],&#10;}&#10;</code></pre>
<p>Then add a reference to this new configuration in your root <code>tsconfig.json</code>:</p>
<pre><code class="language-jsonc">{&#10;	&quot;files&quot;: [],&#10;	&quot;references&quot;: [&#10;		{ &quot;path&quot;: &quot;./tsconfig.app.json&quot; },&#10;		{ &quot;path&quot;: &quot;./tsconfig.node.json&quot; },&#10;		{ &quot;path&quot;: &quot;./tsconfig.worker.json&quot; },&#10;	],&#10;}&#10;</code></pre>
<h3 id="add-the-worker-entrypoint-to-your-configuration">Add the Worker entrypoint to your configuration</h3>
<p>Update your Wrangler configuration file to add a <code>main</code> field that points to your Worker entrypoint:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16026.md")
</div>
<p>The <code>main</code> field specifies the entry file for your Worker code.</p>
<h3 id="add-your-api-worker">Add your API Worker</h3>
<p>Create a <code>worker/index.ts</code> file with the following contents:</p>
<pre><code class="language-ts">export default {&#10;	fetch(request) {&#10;		const url = new URL(request.url);&#10;&#10;		if (url.pathname.startsWith(&quot;/api/&quot;)) {&#10;			return Response.json({&#10;				name: &quot;Cloudflare&quot;,&#10;			});&#10;		}&#10;&#10;		return new Response(null, { status: 404 });&#10;	},&#10;} satisfies ExportedHandler;&#10;</code></pre>
<p>The Worker defined in the preceding code block will be invoked for any non-navigation request that does not match a static asset.
It returns a JSON response if the <code>pathname</code> starts with <code>/api/</code> and otherwise returns a <code>404</code> response.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16022.md")
</aside>
<h3 id="call-the-api-from-the-client">Call the API from the client</h3>
<p>Edit <code>src/App.tsx</code> so that it includes an additional button that calls the API and sets some state:</p>
<pre><code class="language-tsx">import { useState } from &quot;react&quot;;&#10;import reactLogo from &quot;./assets/react.svg&quot;;&#10;import viteLogo from &quot;/vite.svg&quot;;&#10;import &quot;./App.css&quot;;&#10;&#10;function App() {&#10;	const [count, setCount] = useState(0);&#10;	const [name, setName] = useState(&quot;unknown&quot;);&#10;&#10;	return (&#10;		&lt;&gt;&#10;			&lt;div&gt;&#10;				&lt;a href=&quot;https://vite.dev&quot; target=&quot;_blank&quot;&gt;&#10;					&lt;img src={viteLogo} className=&quot;logo&quot; alt=&quot;Vite logo&quot; /&gt;&#10;				&lt;/a&gt;&#10;				&lt;a href=&quot;https://react.dev&quot; target=&quot;_blank&quot;&gt;&#10;					&lt;img src={reactLogo} className=&quot;logo react&quot; alt=&quot;React logo&quot; /&gt;&#10;				&lt;/a&gt;&#10;			&lt;/div&gt;&#10;			&lt;h1&gt;Vite + React&lt;/h1&gt;&#10;			&lt;div className=&quot;card&quot;&gt;&#10;				&lt;button&#10;					onClick={() =&gt; setCount((count) =&gt; count + 1)}&#10;					aria-label=&quot;increment&quot;&#10;				&gt;&#10;					count is {count}&#10;				&lt;/button&gt;&#10;				&lt;p&gt;&#10;					Edit &lt;code&gt;src/App.tsx&lt;/code&gt; and save to test HMR&#10;				&lt;/p&gt;&#10;			&lt;/div&gt;&#10;			&lt;div className=&quot;card&quot;&gt;&#10;				&lt;button&#10;					onClick={() =&gt; {&#10;						fetch(&quot;/api/&quot;)&#10;							.then((res) =&gt; res.json() as Promise&lt;{ name: string }&gt;)&#10;							.then((data) =&gt; setName(data.name));&#10;					}}&#10;					aria-label=&quot;get name&quot;&#10;				&gt;&#10;					Name from API is: {name}&#10;				&lt;/button&gt;&#10;				&lt;p&gt;&#10;					Edit &lt;code&gt;api/index.ts&lt;/code&gt; to change the name&#10;				&lt;/p&gt;&#10;			&lt;/div&gt;&#10;			&lt;p className=&quot;read-the-docs&quot;&gt;&#10;				Click on the Vite and React logos to learn more&#10;			&lt;/p&gt;&#10;		&lt;/&gt;&#10;	);&#10;}&#10;&#10;export default App;&#10;</code></pre>
<p>Now, if you click the button, it will display 'Name from API is: Cloudflare'.</p>
<p>Increment the counter to update the application state in the browser.
Next, edit <code>api/index.ts</code> by changing the <code>name</code> it returns to <code>'Cloudflare Workers'</code>.
If you click the button again, it will display the new <code>name</code> while preserving the previously set counter value.</p>
<p>With Vite and the Cloudflare plugin, you can iterate on the client and server parts of your app together, without losing UI state between edits.</p>
<h3 id="build-your-application">Build your application</h3>
<p>Run the build command to build your application.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm run build</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn run build</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm run build</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run build" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The <code>dist</code> directory will contain your client build output in the <code>client</code> subdirectory and your Worker code alongside the output <code>wrangler.json</code> configuration file.</p>
<h3 id="preview-your-application">Preview your application</h3>
<p>Run the preview command to validate that your application runs as expected.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm run preview</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run preview" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn run preview</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run preview" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm run preview</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run preview" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This command will run your build output locally in the Workers runtime, closely matching its behavior in production.</p>
<h3 id="deploy-to-cloudflare">Deploy to Cloudflare</h3>
<p>Run the deploy command to deploy your application to Cloudflare.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This command will automatically use the output <code>wrangler.json</code> that was included in the build output.</p>
<h2 id="next-steps">Next steps</h2>
<p>In this tutorial, we created an SPA that could be deployed as a Worker with static assets.
We then added an API Worker that could be accessed from the front-end code.
Finally, we deployed both the client and server-side parts of the application to Cloudflare.</p>
<p>Possible next steps include:</p>
<ul>
<li>Adding a binding to another Cloudflare service such as a <a href="/kv/">KV namespace</a> or <a href="/d1/">D1 database</a></li>
<li>Expanding the API to include additional routes</li>
<li>Using a library, such as <a href="https://hono.dev/">Hono</a> or <a href="https://trpc.io/">tRPC</a>, in your API Worker</li>
</ul>
