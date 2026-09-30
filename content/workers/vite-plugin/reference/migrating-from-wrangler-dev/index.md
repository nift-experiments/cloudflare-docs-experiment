<p>In most cases, migrating from <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> is straightforward and you can follow the instructions in <a href="/workers/vite-plugin/get-started/">Get started</a>.
There are a few key differences to highlight:</p>
<h2 id="input-and-output-worker-config-files">Input and output Worker config files</h2>
<p>With the Cloudflare Vite plugin, your <a href="/workers/wrangler/configuration/">Worker config file</a> (for example, <code>wrangler.jsonc</code>) is the input configuration and a separate output configuration is created as part of the build.
This output file is a snapshot of your configuration at the time of the build and is modified to reference your build artifacts.
It is the configuration that is used for preview and deployment.
Once you have run <code>vite build</code>, running <code>wrangler deploy</code> or <code>vite preview</code> will automatically locate this output configuration file.</p>
<h2 id="cloudflare-environments">Cloudflare Environments</h2>
<p>With the Cloudflare Vite plugin, <a href="/workers/vite-plugin/reference/cloudflare-environments/">Cloudflare Environments</a> are applied at dev and build time.
Running <code>wrangler deploy --env some-env</code> is therefore not applicable and the environment to deploy should instead be set by running <code>CLOUDFLARE_ENV=some-env vite build</code>.</p>
<h2 id="redundant-fields-in-the-wrangler-config-file">Redundant fields in the Wrangler config file</h2>
<p>There are various options in the <a href="/workers/wrangler/configuration/">Worker config file</a> that are ignored when using Vite, as they are either no longer applicable or are replaced by Vite equivalents.
If these options are provided, then warnings will be printed to the console with suggestions for how to proceed.</p>
<h3 id="not-applicable">Not applicable</h3>
<p>The following build-related options are handled by Vite and are not applicable when using the Cloudflare Vite plugin:</p>
<ul>
<li><code>tsconfig</code></li>
<li><code>rules</code></li>
<li><code>build</code></li>
<li><code>no_bundle</code></li>
<li><code>find_additional_modules</code></li>
<li><code>base_dir</code></li>
<li><code>preserve_file_names</code></li>
</ul>
<h3 id="not-supported">Not supported</h3>
<ul>
<li><code>site</code> — Use <a href="/workers/static-assets/">Workers Assets</a> instead.</li>
</ul>
<h3 id="replaced-by-vite-equivalents">Replaced by Vite equivalents</h3>
<p>The following options have Vite equivalents that should be used instead:</p>
<table>
<thead>
<tr>
<th>Wrangler option</th>
<th>Vite equivalent</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>define</code></td>
<td><a href="https://vite.dev/config/shared-options.html#define"><code>define</code></a></td>
</tr>
<tr>
<td><code>alias</code></td>
<td><a href="https://vite.dev/config/shared-options.html#resolve-alias"><code>resolve.alias</code></a></td>
</tr>
<tr>
<td><code>minify</code></td>
<td><a href="https://vite.dev/config/build-options.html#build-minify"><code>build.minify</code></a></td>
</tr>
<tr>
<td>Local dev settings (<code>ip</code>, <code>port</code>, <code>local_protocol</code>, etc.)</td>
<td><a href="https://vite.dev/config/server-options.html">Server options</a></td>
</tr>
</tbody>
</table>
<p>See <a href="/workers/vite-plugin/reference/vite-environments/">Vite Environments</a> for more information about configuring your Worker environments in Vite.</p>
<h3 id="inferred">Inferred</h3>
<p>If <a href="https://vite.dev/config/build-options#build-sourcemap">build.sourcemap</a> is enabled for a given Worker environment in the Vite config, <code>&quot;upload_source_maps&quot;: true</code> is automatically added to the output Wrangler configuration file.
This means that generated sourcemaps are uploaded by default.
To override this setting, you can set the value of <code>upload_source_maps</code> explicitly in the input Worker config.</p>
