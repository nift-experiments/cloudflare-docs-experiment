<p>This guide describes the steps to migrate a webpack project from Wrangler v1 to Wrangler v2. After completing this guide, <a href="/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/">update your Wrangler version</a>.</p>
<p>Previous versions of Wrangler offered rudimentary support for <a href="https://webpack.js.org/">webpack</a> with the <code>type</code> and <code>webpack_config</code> keys in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. Starting with Wrangler v2, Wrangler no longer supports the <code>type</code> and <code>webpack_config</code> keys, but you can still use webpack with your Workers.</p>
<p>As a developer using webpack with Workers, you may be in one of four categories:</p>
<ol>
<li>
<p><a href="#i-use-build-to-run-webpack-or-another-bundler-external-to-wrangler">I use <code>[build]</code> to run webpack (or another bundler) external to <code>wrangler</code>.</a>.</p>
</li>
<li>
<p><a href="#i-use-type--webpack-but-do-not-provide-my-own-configuration-and-let-wrangler-take-care-of-it">I use <code>type = webpack</code>, but do not provide my own configuration and let Wrangler take care of it.</a>.</p>
</li>
<li>
<p><a href="#i-use-type--webpack-and-webpack_config--pathtowebpackconfigjs-to-handle-jsx-typescript-webassembly-html-files-and-other-non-standard-filetypes">I use <code>type = webpack</code> and <code>webpack_config = &lt;path/to/webpack.config.js&gt;</code> to handle JSX, TypeScript, WebAssembly, HTML files, and other non-standard filetypes.</a>.</p>
</li>
<li>
<p><a href="#i-use-type--webpack-and-webpack_config--pathtowebpackconfigjs-to-perform-code-transforms-andor-other-code-modifying-functionality">I use <code>type = webpack</code> and <code>webpack_config = &lt;path/to/webpack.config.js&gt;</code> to perform code-transforms and/or other code-modifying functionality.</a>.</p>
</li>
</ol>
<p>If you do not see yourself represented, <a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">file an issue</a> and we can assist you with your specific situation and improve this guide for future readers.</p>
<h3 id="i-use-build-to-run-webpack-or-another-bundler-external-to-wrangler">I use <code>[build]</code> to run webpack (or another bundler) external to Wrangler.</h3>
<p>Wrangler v2 supports the <code>[build]</code> key, so your Workers will continue to build using your own setup.</p>
<h3 id="i-use-type-webpack-but-do-not-provide-my-own-configuration-and-let-wrangler-take-care-of-it">I use <code>type = webpack</code>, but do not provide my own configuration and let Wrangler take care of it.</h3>
<p>Wrangler will continue to take care of it. Remove <code>type = webpack</code> from your Wrangler file.</p>
<h3 id="i-use-type-webpack-and-webpack-config-to-handle-jsx-typescript-webassembly-html-files-and-other-non-standard-filetypes">I use <code>type = webpack</code> and <code>webpack_config = &lt;path/to/webpack.config.js&gt;</code> to handle JSX, TypeScript, WebAssembly, HTML files, and other non-standard filetypes.</h3>
<p>As of Wrangler v2, Wrangler has built-in support for this use case. Refer to <a href="/workers/wrangler/bundling/">Bundling</a> for more details.</p>
<p>The Workers runtime handles JSX and TypeScript. You can <code>import</code> any modules you need into your code and the Workers runtime includes them in the built Worker automatically.</p>
<p>You should remove the <code>type</code> and <code>webpack_config</code> keys from your Wrangler file.</p>
<h3 id="i-use-type-webpack-and-webpack-config-to-perform-code-transforms-and-or-other-code-modifying-functionality">I use <code>type = webpack</code> and <code>webpack_config = &lt;path/to/webpack.config.js&gt;</code> to perform code-transforms and/or other code-modifying functionality.</h3>
<p>Wrangler v2 drops support for project types, including <code>type = webpack</code> and configuration via the <code>webpack_config</code> key. If your webpack configuration performs operations beyond adding loaders (for example, for TypeScript) you will need to maintain your custom webpack configuration. In the long term, you should <a href="/workers/wrangler/custom-builds/">migrate to an external <code>[build]</code> process</a>. In the short term, it is still possible to reproduce Wrangler v1's build steps in newer versions of Wrangler by following the instructions below.</p>
<ol>
<li>Add <a href="https://www.npmjs.com/package/wranglerjs-compat-webpack-plugin">wranglerjs-compat-webpack-plugin</a> as a <code>devDependency</code>.</li>
</ol>
<p><a href="https://www.npmjs.com/package/wrangler-js">wrangler-js</a>, shipped as a separate library from <a href="https://www.npmjs.com/package/@cloudflare/wrangler/v/1.19.11">Wrangler v1</a>, is a Node script that configures and executes <a href="https://unpkg.com/browse/wrangler-js@0.1.11/package.json">webpack 4</a> for you. When you set <code>type = webpack</code>, Wrangler v1 would execute this script for you. We have ported the functionality over to a new package, <a href="https://www.npmjs.com/package/wranglerjs-compat-webpack-plugin">wranglerjs-compat-webpack-plugin</a>, which you can use as a <a href="https://v4.webpack.js.org/configuration/plugins/">webpack plugin</a>.</p>
<p>To do that, you will need to add it as a dependency:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You should see this reflected in your <code>package.json</code> file:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;version&quot;: &quot;x.y.z&quot;,&#10;	// ...&#10;	&quot;devDependencies&quot;: {&#10;		// ...&#10;		&quot;wranglerjs-compat-webpack-plugin&quot;: &quot;^x.y.z&quot;,&#10;		&quot;webpack&quot;: &quot;^4.46.0&quot;,&#10;		&quot;webpack-cli&quot;: &quot;^x.y.z&quot;&#10;	}&#10;}&#10;</code></pre>
<ol start="2">
<li>Add <code>wranglerjs-compat-webpack-plugin</code> to <code>webpack.config.js</code>.</li>
</ol>
<p>Modify your <code>webpack.config.js</code> file to include the plugin you just installed.</p>
<pre><code class="language-js">const {&#10;	WranglerJsCompatWebpackPlugin,&#10;} = require(&quot;wranglerjs-compat-webpack-plugin&quot;);&#10;&#10;module.exports = {&#10;	// ...&#10;	plugins: [new WranglerJsCompatWebpackPlugin()],&#10;};&#10;</code></pre>
<ol start="3">
<li>Add a build script your <code>package.json</code>.</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;version&quot;: &quot;2.0.0&quot;,&#10;	// ...&#10;	&quot;scripts&quot;: {&#10;		&quot;build&quot;: &quot;webpack&quot; // &lt;-- Add this line!&#10;		// ...&#10;	}&#10;}&#10;</code></pre>
<ol start="4">
<li>Remove unsupported entries from your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ol>
<p>Remove the <code>type</code> and <code>webpack_config</code> keys from your Wrangler file, as they are not supported anymore.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17449.md")
</div>
<ol start="5">
<li>Tell Wrangler how to bundle your Worker.</li>
</ol>
<p>Wrangler no longer has any knowledge of how to build your Worker. You will need to tell it how to call webpack and where to look for webpack's output. This translates into two fields:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17450.md")
</div>
<ol start="6">
<li>Test your project.</li>
</ol>
<p>Try running <code>npx wrangler deploy</code> to test that your configuration works as expected.</p>
