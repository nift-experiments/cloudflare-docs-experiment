<p>Sandbox runs on <a href="/containers/">Containers</a>. For deploy commands, Workers Builds, and rollout flags, refer to <a href="/containers/guides/deploy/">Deploy Containers</a> and <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<p>To put <code>exposePort()</code> on a custom domain, refer to <a href="/sandbox/guides/preview-urls-custom-domain/">Configure preview URLs on a custom domain</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13473.md")
</aside>
<h2 id="keep-the-package-and-image-aligned">Keep the package and image aligned</h2>
<p>The Worker depends on <code>@cloudflare/sandbox</code> (or <code>@cloudflare/sandbox@next</code>). The container image must come from the same release line (Dockerfile and base image tags from the template or docs for that version).</p>
<p>When you bump the npm package:</p>
<ol>
<li>Update the Dockerfile or image reference for the same line.</li>
<li>Run <code>wrangler deploy</code> so the new image is published.</li>
<li>If the Worker and image must cut over together, deploy with an immediate rollout:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Use this for stable to <code>@next</code> cutovers and other breaking package/image pairs. Refer to <a href="/sandbox/1-0-preview/migrate/#deploy-the-cutover">Migrate</a> and <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<p>Do not mix a stable package with a <code>@next</code> image, or the reverse.</p>
<h2 id="deploy-from-your-machine">Deploy from your machine</h2>
<ol>
<li>Start Docker if <code>image</code> is a Dockerfile path. Registry image references do not need Docker at deploy time.</li>
<li>From the project root:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="3">
<li>Confirm the Worker URL responds, then exercise a sandbox route.</li>
</ol>
<p>The first deploy can take several minutes while the image provisions.</p>
<h2 id="workers-builds">Workers Builds</h2>
<p>For production, use <code>wrangler deploy</code> so the package and image can update together.</p>
<p>Non-production Workers Builds defaults to <code>wrangler versions upload</code>, which does not publish a new image. <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> are not generated for these Workers (they implement Durable Objects). Test with <code>wrangler dev</code>, or with a staging Worker or <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">environment</a> that runs <code>wrangler deploy</code>.</p>
<p>More detail: <a href="/containers/guides/deploy/#before-production">Before production</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/containers/guides/deploy/">Deploy Containers</a></li>
<li><a href="/containers/configuration/rollouts/">Rollouts</a></li>
<li><a href="/sandbox/guides/preview-urls-custom-domain/">Configure preview URLs on a custom domain</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate to Sandbox SDK 1.0 preview</a></li>
</ul>
