<p>Test changes to your <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dynamic dispatch Worker</a> by running the dynamic dispatch Worker locally but connecting it to user Workers that have been deployed to Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4208.md")
</aside>
<p>This is helpful when:</p>
<ul>
<li><strong>Testing routing changes</strong> and validating that updates continue to work with deployed User Workers</li>
<li><strong>Adding new middleware</strong> like authentication, rate limiting, or logging to the dynamic dispatch Worker</li>
<li><strong>Debugging issues</strong> in the dynamic dispatcher that may be impacting deployed User Workers</li>
</ul>
<h3 id="how-to-use-remote-dispatch-namespaces">How to use remote dispatch namespaces</h3>
<p>In the dynamic dispatch Worker's Wrangler file, configure the <a href="/workers/wrangler/configuration/#dispatch-namespace-bindings-workers-for-platforms">dispatch namespace binding</a> to connect to the remote namespace by setting <a href="/workers/local-development/#remote-bindings"><code>remote = true</code></a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4209.md")
</div>
<p>This tells your dispatch Worker that's running locally to connect to the remote <code>production</code> namespace. When you run <code>wrangler dev</code>, your Dispatch Worker will route requests to the User Workers deployed in that namespace.</p>
<p>For more information about remote bindings during local development, refer to <a href="/workers/local-development/#remote-bindings">remote bindings documentation</a>.</p>
