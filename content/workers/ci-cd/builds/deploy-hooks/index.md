<p>By default, Workers Builds triggers a build when you push a commit to your <a href="/workers/ci-cd/builds/git-integration/">connected Git repository</a>. Deploy Hooks provide another way to trigger a build. Each hook is a unique URL that triggers a manual build for one branch when it receives an HTTP POST request. Use Deploy Hooks to connect Workers Builds with workflows such as:</p>
<ul>
<li>Rebuild automatically when content changes in a headless CMS</li>
<li>Build on a schedule using an external cron service</li>
<li>Trigger deployments from custom CI/CD pipelines based on specific conditions</li>
</ul>
<h2 id="create-a-deploy-hook">Create a Deploy Hook</h2>
<p>Before creating a Deploy Hook, ensure your Worker is <a href="/workers/ci-cd/builds/git-integration/">connected to a Git repository</a>.</p>
<ol>
<li>Go to <strong>Workers &amp; Pages</strong> and select your Worker.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</li>
<li>Enter a <strong>name</strong> and select the <strong>branch</strong> to build.</li>
<li>Select <strong>Create</strong> and copy the generated URL.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16768.md")
</aside>
<h2 id="trigger-a-deploy-hook">Trigger a Deploy Hook</h2>
<p>Send an HTTP POST request to your Deploy Hook URL to start a build:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>No <code>Authorization</code> header is needed. The unique identifier embedded in the URL acts as the authentication credential.</p>
<p>Example response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;build_uuid&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;    &quot;branch&quot;: &quot;main&quot;,&#10;    &quot;worker&quot;: &quot;my-worker&quot;&#10;  }&#10;}&#10;</code></pre>
<p>The <code>build_uuid</code> in the response can be used to <a href="/workers/ci-cd/builds/api-reference/#get-build-logs">monitor build status and retrieve logs</a>.</p>
<h3 id="verify-the-build">Verify the build</h3>
<p>After you trigger a Deploy Hook, you can verify it from the dashboard:</p>
<ul>
<li>In the <strong>Deploy Hooks</strong> list, the hook shows when it was last triggered.</li>
<li>In your Worker's build history, the <strong>Triggered by</strong> column identifies builds started by a Deploy Hook using the hook name and a <code>deploy hook</code> label.</li>
</ul>
<p>If you need to inspect these builds programmatically, use <a href="/workers/ci-cd/builds/api-reference/#list-builds-for-a-worker">List builds for a Worker</a> in the Builds API reference. Hook-triggered builds are recorded with <code>build_trigger_source: &quot;deploy_hook&quot;</code>.</p>
<h2 id="cms-integration">CMS integration</h2>
<p>Most headless CMS platforms support webhooks that call your Deploy Hook URL when content changes. The general setup is the same across platforms:</p>
<ol>
<li>Find the webhooks or integrations settings in your CMS.</li>
<li>Create a new webhook and paste your Deploy Hook URL as the target URL.</li>
<li>Select which events should trigger the webhook (for example, publish, unpublish, or update).</li>
</ol>
<p>Refer to your CMS documentation for platform-specific instructions. Popular platforms with webhook support include Contentful, Sanity, Strapi, Storyblok, DatoCMS, and Prismic.</p>
<h2 id="idempotency">Idempotency</h2>
<p>If the same Deploy Hook is triggered again before the previous build has fully started, Workers Builds does not create a duplicate build. Instead, it returns the build that is already in progress.</p>
<p>If an external system sends the same Deploy Hook twice in quick succession:</p>
<ol>
<li>The first request creates a build.</li>
<li>If a second request arrives while that build is still <code>queued</code> or <code>initializing</code>, no second build is created.</li>
<li>Instead, the response returns the existing <code>build_uuid</code> and sets <code>already_exists</code> to <code>true</code>.</li>
</ol>
<p>Example response when an existing pending build is returned:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;build_uuid&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;    &quot;status&quot;: &quot;queued&quot;,&#10;    &quot;created_on&quot;: &quot;2026-01-21T18:50:00Z&quot;,&#10;    &quot;already_exists&quot;: true&#10;  }&#10;}&#10;</code></pre>
<p>Once the earlier build moves past <code>initializing</code>, a later POST creates a new build as normal. This makes Deploy Hooks safe to use with systems that retry webhooks or emit bursts of content-update events.</p>
<h2 id="examples">Examples</h2>
<h3 id="deploy-from-a-slack-slash-command">Deploy from a Slack slash command</h3>
<p>A Worker that receives a <code>/deploy</code> command from Slack and triggers a build:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16769.md")
</div>
<h3 id="rebuild-on-a-schedule">Rebuild on a schedule</h3>
<p>A Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> that rebuilds every hour:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16770.md")
</div>
<h2 id="security-considerations">Security considerations</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16771.md")
</aside>
<ul>
<li>Store Deploy Hook URLs in environment variables or a secrets manager, never in source code or public configuration files.</li>
<li>Restrict access to the URL to only the systems that need it.</li>
<li>If a URL is compromised or you suspect unauthorized use, delete the Deploy Hook immediately and create a new one. The old URL stops working as soon as it is deleted.</li>
</ul>
<h3 id="using-the-builds-api-for-authenticated-triggers">Using the Builds API for authenticated triggers</h3>
<p>If your external system supports custom headers, you can call the <a href="/api/resources/workers_builds/subresources/triggers/methods/create_build">manual build endpoint</a> with an API token in the <code>Authorization</code> header instead. This gives you token-based authentication and the ability to choose the branch per request. For a step-by-step walkthrough, see <a href="/workers/ci-cd/builds/api-reference/#trigger-a-manual-build">Trigger a manual build</a>.</p>
<h2 id="limits">Limits</h2>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all Workers Builds limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
