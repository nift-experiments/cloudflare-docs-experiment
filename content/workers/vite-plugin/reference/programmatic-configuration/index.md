<p>The Wrangler configuration file is optional when using the Cloudflare Vite plugin. Without one, the plugin uses default values. You can customize Worker configuration programmatically with the <code>config</code> option. This is useful when the Cloudflare plugin runs inside another plugin or framework.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17389.md")
</aside>
<h2 id="default-configuration">Default configuration</h2>
<p>Without a configuration file, the plugin generates sensible defaults for an assets-only Worker. The <code>name</code> comes from <code>package.json</code> or the project directory name. The <code>compatibility_date</code> uses the latest date supported by your installed Miniflare version.</p>
<h2 id="the-config-option">The <code>config</code> option</h2>
<p>The <code>config</code> option offers three ways to programmatically configure your Worker. You can set any property from the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, though some options are <a href="/workers/vite-plugin/reference/migrating-from-wrangler-dev/#redundant-fields-in-the-wrangler-config-file">ignored or replaced by Vite equivalents</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17388.md")
</aside>
<h3 id="configuration-object">Configuration object</h3>
<p>Set <code>config</code> to an object to provide values that merge with defaults and Wrangler config file settings:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				compatibility_date: &quot;2025-01-01&quot;,&#10;				vars: {&#10;					API_URL: &quot;https://api.example.com&quot;,&#10;				},&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>These values merge with Wrangler config file values, with the <code>config</code> values taking precedence.</p>
<h3 id="dynamic-configuration-function">Dynamic configuration function</h3>
<p>Use a function when configuration depends on existing config values or external data, or if you need to compute or conditionally set values:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; ({&#10;				vars: {&#10;					WORKER_NAME: userConfig.name,&#10;					BUILD_TIME: new Date().toISOString(),&#10;				},&#10;			}),&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>The function receives the current configuration (defaults or loaded config file). Return an object with values to merge.</p>
<h3 id="in-place-editing">In-place editing</h3>
<p>A <code>config</code> function can mutate the config object directly instead of returning overrides. This is useful for deleting properties or removing array items:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; {&#10;				// Replace all existing compatibility flags&#10;				userConfig.compatibility_flags = [&quot;nodejs_compat&quot;];&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17387.md")
</aside>
<h2 id="auxiliary-workers">Auxiliary Workers</h2>
<p>Auxiliary Workers also support the <code>config</code> option, enabling multi-Worker architectures without config files.</p>
<p>Define auxiliary Workers without config files using <code>config</code> inside the <code>auxiliaryWorkers</code> array:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				name: &quot;entry-worker&quot;,&#10;				main: &quot;./src/entry.ts&quot;,&#10;				compatibility_date: &quot;2025-01-01&quot;,&#10;				services: [{ binding: &quot;API&quot;, service: &quot;api-worker&quot; }],&#10;			},&#10;			auxiliaryWorkers: [&#10;				{&#10;					config: {&#10;						name: &quot;api-worker&quot;,&#10;						main: &quot;./src/api.ts&quot;,&#10;						compatibility_date: &quot;2025-01-01&quot;,&#10;					},&#10;				},&#10;			],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h3 id="configuration-overrides">Configuration overrides</h3>
<p>Combine a config file with <code>config</code> to override specific values:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			configPath: &quot;./wrangler.jsonc&quot;,&#10;			auxiliaryWorkers: [&#10;				{&#10;					configPath: &quot;./workers/api/wrangler.jsonc&quot;,&#10;					config: {&#10;						vars: {&#10;							ENDPOINT: &quot;https://api.example.com/v2&quot;,&#10;						},&#10;					},&#10;				},&#10;			],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h3 id="configuration-inheritance">Configuration inheritance</h3>
<p>Auxiliary Workers receive the resolved entry Worker config in the second parameter to the <code>config</code> function. This makes it straightforward to inherit configuration from the entry Worker in auxiliary Workers.</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			auxiliaryWorkers: [&#10;				{&#10;					config: (_, { entryWorkerConfig }) =&gt; ({&#10;						name: &quot;auxiliary-worker&quot;,&#10;						main: &quot;./src/auxiliary-worker.ts&quot;,&#10;						// Inherit compatibility settings from entry Worker&#10;						compatibility_date: entryWorkerConfig.compatibility_date,&#10;						compatibility_flags: entryWorkerConfig.compatibility_flags,&#10;					}),&#10;				},&#10;			],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h2 id="configuration-merging-behavior">Configuration merging behavior</h2>
<p>The <code>config</code> option uses <a href="https://github.com/unjs/defu">defu</a> for merging configuration objects.</p>
<ul>
<li>Object properties are recursively merged</li>
<li>Arrays are concatenated (<code>config</code> values first, then existing values)</li>
<li>Primitive values from <code>config</code> override existing values</li>
<li><code>undefined</code> values in <code>config</code> do not override existing values</li>
</ul>
