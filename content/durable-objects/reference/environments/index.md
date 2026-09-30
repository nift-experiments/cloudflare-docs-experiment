<p>Environments provide isolated spaces where your code runs with specific dependencies and configurations. This can be useful for a number of reasons, such as compatibility testing or version management. Using different environments can help with code consistency, testing, and production segregation, which reduces the risk of errors when deploying code.</p>
<h2 id="wrangler-environments">Wrangler environments</h2>
<p><a href="/workers/wrangler/install-and-update/">Wrangler</a> allows you to deploy the same Worker application with different configuration for each <a href="/workers/wrangler/environments/">environment</a>.</p>
<p>If you are using Wrangler environments, you must specify any <a href="/workers/runtime-apis/bindings/">Durable Object bindings</a> you wish to use on a per-environment basis.</p>
<p>Durable Object bindings are not inherited. For example, you can define an environment named <code>staging</code> as below:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8099.md")
</div>
<p>Because Wrangler appends the <a href="/workers/wrangler/environments/">environment name</a> to the top-level name when publishing, for a Worker named <code>worker-name</code> the above example is equivalent to:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8100.md")
</div>
<p><code>&quot;EXAMPLE_CLASS&quot;</code> in the staging environment is bound to a different Worker code name compared to the top-level <code>&quot;EXAMPLE_CLASS&quot;</code> binding, and will therefore access different Durable Objects with different persistent storage.</p>
<p>If you want an environment-specific binding that accesses the same Objects as the top-level binding, specify the top-level Worker code name explicitly using <code>script_name</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8101.md")
</div>
<h3 id="migration-environments">Migration environments</h3>
<p>You can define a Durable Object migration for each environment, as well as at the top level. Migrations at the environment-level override migrations at the top level.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/#migration-wrangler-configuration">Migration Wrangler Configuration</a>.</p>
<h2 id="local-development">Local development</h2>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment, so that you can test your Worker and Durable Objects before you deploy to production.</p>
<p>An existing Durable Object binding of <code>DB</code> would be available to your Worker when running locally.</p>
<p>Refer to Workers <a href="/workers/local-development/bindings-per-env/">Local development</a>.</p>
<h2 id="remote-development">Remote development</h2>
<p>KV-backed Durable Objects support remote development using the dashboard playground. The dashboard playground uses a browser version of Visual Studio Code, allowing you to rapidly iterate on your Worker entirely in your browser.</p>
<p>To start remote development:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing Worker.
3. Select the **Edit code** icon located on the upper-right of the screen.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8098.md")
</aside>
