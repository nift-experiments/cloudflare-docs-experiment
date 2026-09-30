<p>Gradual deployments let you incrementally deploy new <a href="/workers/versions-and-deployments/#versions">versions</a> of your Worker by splitting traffic across versions. Instead of shifting all traffic to a new version at once, you can route a percentage of requests to the new version while the rest continue to be handled by the previous version.</p>
<p><img src="/assets/upstream/images/workers/platform/versions-and-deployments/gradual-deployments.png" alt="Gradual Deployments" /></p>
<p>Using gradual deployments, you can:</p>
<ul>
<li>Gradually shift traffic to a newer version of your Worker</li>
<li>Monitor error rates and exceptions across versions using <a href="/workers/versions-and-deployments/gradual-deployments/#observability">observability</a> tooling</li>
<li><a href="/workers/versions-and-deployments/rollbacks/">Roll back</a> to a previously stable version if you notice issues</li>
</ul>
<h2 id="use-gradual-deployments">Use gradual deployments</h2>
<p>The following section guides you through an example usage of gradual deployments.</p>
<h3 id="via-wrangler">Via Wrangler</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17380.md")
</aside>
<h4 id="1-create-and-deploy-a-new-worker"><ol>
<li>Create and deploy a new Worker</li>
</ol></h4>
<p>Create a new <code>&quot;Hello World&quot;</code> Worker using the <a href="/pages/get-started/c3/"><code>create-cloudflare</code> CLI (C3)</a> and deploy it.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- &lt;NAME&gt; -- --type=hello-world</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- &lt;NAME&gt; -- --type=hello-world" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare &lt;NAME&gt; -- --type=hello-world</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare &lt;NAME&gt; -- --type=hello-world" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest &lt;NAME&gt; -- --type=hello-world</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest &lt;NAME&gt; -- --type=hello-world" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Answer <code>yes</code> or <code>no</code> to using TypeScript. Answer <code>yes</code> to deploying your application. This is the first version of your Worker.</p>
<h4 id="2-create-a-new-version-of-the-worker"><ol start="2">
<li>Create a new version of the Worker</li>
</ol></h4>
<p>Edit the Worker code by changing the <code>Response</code> content and upload the Worker using the <a href="/workers/wrangler/commands/general/#versions-upload"><code>wrangler versions upload</code></a> command.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions upload</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions upload" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will create a new version of the Worker that is not automatically deployed.</p>
<h4 id="3-create-a-new-deployment"><ol start="3">
<li>Create a new deployment</li>
</ol></h4>
<p>Use the <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a> command to create a new deployment that splits traffic between two versions. Follow the interactive prompts to select your desired percentages for each version.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="4-test-the-split-deployment"><ol start="4">
<li>Test the split deployment</li>
</ol></h4>
<p>Run a cURL command on your Worker to test the split deployment.</p>
<pre><code class="language-bash">for j in {1..10}&#10;do&#10;    curl -s https://$WORKER_NAME.$SUBDOMAIN.workers.dev&#10;done&#10;</code></pre>
<p>You should see 10 responses. Responses will vary depending on the percentages configured in <a href="/workers/versions-and-deployments/gradual-deployments/#3-create-a-new-deployment">step #3</a>.</p>
<p>You can also target a specific version using <a href="/workers/versions-and-deployments/version-overrides/">version overrides</a>.</p>
<h4 id="5-set-your-new-version-to-100-deployment"><ol start="5">
<li>Set your new version to 100% deployment</li>
</ol></h4>
<p>Run <code>wrangler versions deploy</code> again and follow the interactive prompts. Select the new version and set it to 100%.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Hello World</strong> template &gt; deploy your Worker.</li>
<li>Once the Worker is deployed, go to the online code editor through <strong>Edit code</strong>. Edit the Worker code (change the <code>Response</code> content).</li>
<li>To save changes without deploying, select the <strong>down arrow</strong> next to <strong>Deploy</strong> &gt; <strong>Save</strong>. This will create a new version of your Worker.</li>
<li>Go to <strong>Deployments</strong> and select <strong>Promote deployment</strong> to create a split between the two versions.</li>
</ol>
<h2 id="version-skew">Version skew</h2>
<p>Because gradual deployments mean multiple versions of your Worker serve traffic simultaneously, clients and services can end up interacting with more than one version in ways that produce errors or inconsistent behavior. This is called <strong>version skew</strong>.</p>
<h3 id="version-skew-within-a-worker">Version skew within a Worker</h3>
<p>By default, each request is independently routed to a version based on the configured percentages. This means consecutive requests from the same user - including page reloads and asset fetches - can be handled by different versions.</p>
<p>If you want to pin a user to a consistent version for the duration of the gradual deployment, you can use <a href="/workers/versions-and-deployments/gradual-deployments/version-affinity/">version affinity</a>.</p>
<h3 id="version-skew-between-workers">Version skew between Workers</h3>
<p>When one Worker calls another via a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a>, the two Workers may be at different points in their own gradual deployment. Worker A (on its new version) might call Worker B, but the request lands on Worker B's old version where the API contract is different.</p>
<p>You can use <a href="/workers/versions-and-deployments/version-overrides/">version overrides</a> to pin a downstream Worker to a specific version during a subrequest.</p>
<h2 id="durable-objects">Durable Objects</h2>
<p>Gradual deployments work differently for <a href="/durable-objects/">Durable Objects</a> because only one version of each Durable Object can run at a time. Refer to <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/">Gradual Deployments with Durable Objects</a> for details on version assignment, guarantees, and migrations.</p>
<h2 id="observability">Observability</h2>
<p>When using gradual deployments, you may want to attribute Workers invocations to a specific version in order to get visibility into the impact of deploying new versions.</p>
<h3 id="logpush">Logpush</h3>
<p>A new <code>ScriptVersion</code> object is available in <a href="/workers/observability/logs/logpush/">Workers Logpush</a>. <code>ScriptVersion</code> can only be added through the Logpush API right now. Sample API call:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/logpush/jobs&#x27; \&#10;&#45;H &#x27;Authorization: Bearer &lt;TOKEN&gt;&#x27; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;d &#x27;{&#10;&quot;name&quot;: &quot;workers-logpush&quot;,&#10;&quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&quot;Event&quot;, &quot;EventTimestampMs&quot;, &quot;Outcome&quot;, &quot;Logs&quot;, &quot;ScriptName&quot;, &quot;ScriptVersion&quot;]&#10;},&#10;&quot;destination_conf&quot;: &quot;&lt;DESTINATION_URL&gt;&quot;,&#10;&quot;dataset&quot;: &quot;workers_trace_events&quot;,&#10;&quot;enabled&quot;: true&#10;}&#x27;| jq .&#10;</code></pre>
<p><code>ScriptVersion</code> is an object with the following structure:</p>
<pre><code class="language-json">{&#10;	&quot;ScriptVersion&quot;: {&#10;		&quot;id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;		&quot;message&quot;: &quot;&lt;MESSAGE&gt;&quot;,&#10;		&quot;tag&quot;: &quot;&lt;TAG&gt;&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="runtime-binding">Runtime binding</h3>
<p>Use the <a href="/workers/runtime-apis/bindings/version-metadata/">Version metadata binding</a> to access version ID or version tag in your Worker.</p>
<h2 id="limits">Limits</h2>
<h3 id="deployments-limit">Deployments limit</h3>
<p>You can only create a gradual deployment with the last 100 uploaded versions of your Worker.</p>
