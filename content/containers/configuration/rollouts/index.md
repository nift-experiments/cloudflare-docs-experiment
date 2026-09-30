<h2 id="how-rollouts-work">How rollouts work</h2>
<p>A <strong>rollout</strong> applies a target container application configuration after you <a href="/containers/guides/deploy/">deploy</a> a Worker that uses Containers. The target can change the image, instance type, limits, placement, or other container settings.</p>
<p>A <strong>container instance</strong> is one running copy of your container image on Cloudflare's network. It runs the process your image starts (<code>ENTRYPOINT</code>/<code>CMD</code> in the Dockerfile, or the base image default). When the target changes the image, the rollout replaces container instances with copies that run the target image. Rollouts do not change Durable Object storage.</p>
<p>When an existing container application's effective configuration changes, <code>wrangler deploy</code>:</p>
<ol>
<li>Uploads and activates the new Worker version, including Durable Object class code.</li>
<li>Builds and pushes a Dockerfile image when needed, or uses the configured registry image reference.</li>
<li>Starts a rollout to apply the target container configuration.</li>
</ol>
<p>The Worker is active before the image and rollout steps begin. These steps are not transactional, so the Worker can remain active if a later image or rollout step fails. Deploy success means the rollout started, not that every container instance has finished replacing. The first deploy creates the container application directly, and a deploy with no effective container changes starts no rollout.</p>
<p>When the image changes, new Worker code can still reach container instances on the previous image until the rollout finishes. Prefer Worker and image changes that work together during that window, or choose <a href="#immediate">immediate</a> when you need the shortest mixed window the platform allows.</p>
<p>Field names and allowed values are listed under <a href="/workers/wrangler/configuration/#containers">Containers configuration</a>.</p>
<h2 id="defaults">Defaults</h2>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rollout_step_percentage</code></td>
<td><code>100</code> if <code>max_instances</code> is omitted or less than <code>2</code>; otherwise <code>[10, 100]</code></td>
</tr>
<tr>
<td><code>rollout_active_grace_period</code></td>
<td><code>0</code> seconds</td>
</tr>
<tr>
<td>Stop sequence when replacing a container instance</td>
<td><code>SIGTERM</code> to the main process, then <code>SIGKILL</code> after 15 minutes if it has not exited</td>
</tr>
</tbody>
</table>
<h2 id="gradual-rollouts">Gradual rollouts</h2>
<p>By default, Wrangler starts a rolling rollout using <code>rollout_step_percentage</code>. If <code>max_instances</code> is omitted or less than <code>2</code>, Wrangler uses one <code>100</code> step. Otherwise, Wrangler requests <code>[10, 100]</code>:</p>
<ol>
<li>Request a target of about 10% of container instances with the new configuration. The platform raises this percentage when necessary so the step represents at least one instance at the configured <code>max_instances</code>.</li>
<li>Target 100% of container instances with the new configuration.</li>
</ol>
<p>Configure the steps with <code>rollout_step_percentage</code> in Wrangler. Override the default plan for one deploy with <a href="#rollout-modes"><code>--containers-rollout</code></a>.</p>
<h2 id="how-a-container-instance-is-replaced">How a container instance is replaced</h2>
<p>When the rollout selects a container instance to update:</p>
<ol>
<li><strong>Grace period (if configured).</strong> If <code>rollout_active_grace_period</code> is greater than <code>0</code>, container instances that only recently became connected to their <a href="/durable-objects/">Durable Object</a> are skipped until they pass that window. Default <code>0</code> means no extra wait. Refer to <a href="#rollout-active-grace-period">Rollout active grace period</a>.</li>
<li><strong>Signal stop.</strong> The platform sends <code>SIGTERM</code> to the main process in the container so it can stop accepting new work and finish in-flight work. Handle <code>SIGTERM</code> in your image if that process needs cleanup before exit.</li>
<li><strong>Drain.</strong> The process has up to 15 minutes to exit after <code>SIGTERM</code>.</li>
<li><strong>Force stop if needed.</strong> If the process is still running after 15 minutes, the platform sends <code>SIGKILL</code>.</li>
<li><strong>After exit.</strong> The Container class <a href="/containers/reference/container-class/#onstop"><code>onStop</code></a> hook can run in the Worker once the container process has exited.</li>
<li><strong>Start a new container instance</strong> with the target image. Disk is <a href="/containers/faq/#is-disk-persistent-what-happens-to-my-disk-when-my-container-sleeps">ephemeral</a> unless you store data outside the container filesystem.</li>
</ol>
<p>Each selected container instance follows this sequence on its own schedule. The fleet does not restart in a single moment.</p>
<h3 id="requests-while-a-container-instance-starts">Requests while a container instance starts</h3>
<p>The new container instance must start its process. Startup often takes on the order of seconds, depending on image size and what runs at start. Refer to <a href="/containers/concepts/architecture/#starting-a-container">cold starts</a>.</p>
<p>A request that needs that container instance may wait until the container is ready, or fail if a client or Worker timeout is shorter than startup. Keep startup work fast, use port readiness checks if you configure them, and set timeouts with startup in mind.</p>
<h2 id="rollout-active-grace-period">Rollout active grace period</h2>
<p><code>rollout_active_grace_period</code> applies only during a rollout, when the platform chooses which container instances to replace.</p>
<p>Containers are <a href="/containers/concepts/architecture/#worker-to-durable-object">backed by Durable Objects</a>. Each running container instance is associated with a Durable Object instance that starts it and sends it traffic. The grace period is how long that connection must already have been up before a rollout may shut the container down. It is not measured from deploy completion.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0</code> (default)</td>
<td>No extra protection. Selected container instances may be replaced as soon as the rollout reaches them.</td>
</tr>
<tr>
<td>Greater than <code>0</code> (for example <code>300</code>)</td>
<td>Container instances connected to their Durable Object for less than this many seconds are left alone until they pass the window.</td>
</tr>
</tbody>
</table>
<p>Use a non-zero value when short sessions should finish before a rollout replaces the container. Container instances that have been connected longer can still be replaced once they pass the window.</p>
<p><code>rollout_active_grace_period</code> applies in every rollout mode, including <a href="#immediate">immediate</a>.</p>
<h2 id="rollout-modes">Rollout modes</h2>
<p><code>--containers-rollout</code> applies to <a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a> only. It does not apply to <a href="/workers/wrangler/commands/workers/#versions"><code>wrangler versions upload</code></a>.</p>
<p>On a full deploy, Wrangler activates the Worker before it processes the container image and rollout. Rollout mode controls how the target container configuration is applied.</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Flag</th>
<th>Container instances</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gradual (default)</td>
<td>omit flag</td>
<td>Use <code>rollout_step_percentage</code>, which can contain one or multiple steps</td>
</tr>
<tr>
<td>Immediate</td>
<td><code>--containers-rollout=immediate</code></td>
<td>Target 100% of container instances in one step</td>
</tr>
<tr>
<td>None</td>
<td><code>--containers-rollout=none</code></td>
<td>Leave images and running container instances unchanged; deploy Worker code only</td>
</tr>
</tbody>
</table>
<p><span id="immediate-rollouts"></span></p>
<h3 id="immediate">Immediate</h3>
<p>Immediate sets the rollout plan to a single step that targets 100% of container instances. There is no intermediate percentage hold.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy --containers-rollout=immediate</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy --containers-rollout=immediate" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Use immediate when Worker code and the container image need to stay compatible and you want the mixed window as short as the platform allows (for example a breaking change in how the Worker talks to the process in the image).</p>
<p>Behavior:</p>
<ul>
<li>The new Worker version is activated before the container image and rollout are processed.</li>
<li>The rollout then replaces container instances toward 100% using the same <a href="#how-a-container-instance-is-replaced">replace sequence</a> as gradual mode, including grace period when configured.</li>
<li>Replacements complete over wall-clock time. How long depends on how many container instances are running, how long each takes to stop and start, and any grace period.</li>
<li>When the image changes, immediate minimizes but does not eliminate the period when the new Worker can reach instances on the previous image.</li>
<li>Deploy success means the rollout started, not that replacements finished.</li>
</ul>
<h3 id="none">None</h3>
<p>None leaves images and running container instances unchanged and deploys Worker code only.</p>
<p>Use none when the deploy should not publish a new image or start a container instance rollout. If <code>image</code> is a Dockerfile path and Docker is unavailable, Wrangler may require this flag or a working Docker setup so the deploy can skip container steps.</p>
<h2 id="example-configuration">Example configuration</h2>
<p><code>rollout_active_grace_period</code> of 300 seconds (five minutes) and steps <code>[10, 100]</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7151.md")
</div>
<h2 id="related">Related</h2>
<ul>
<li><a href="/containers/guides/deploy/">Deploy Containers</a></li>
<li><a href="/containers/concepts/architecture/">Lifecycle of a Container</a></li>
<li><a href="/containers/guides/image-management/">Image management</a></li>
<li><a href="/workers/wrangler/configuration/#containers">Containers configuration</a></li>
</ul>
