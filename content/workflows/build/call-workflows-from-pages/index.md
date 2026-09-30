<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="use-static-assets">Use Static Assets</h3>
@markup("md", "content/.markup/bodies/17590.md")
</aside>
<hr />
<p>You can bind and trigger Workflows from <a href="/pages/functions/">Pages Functions</a> by deploying a Workers project with your Workflow definition and then invoking that Worker using <a href="/pages/functions/bindings/#service-bindings">service bindings</a> or a standard <code>fetch()</code> call.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17589.md")
</aside>
<h3 id="use-service-bindings">Use Service Bindings</h3>
<p><a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> allow you to call a Worker from another Worker or a Pages Function without needing to expose it directly.</p>
<p>To do this, you will need to:</p>
<ol>
<li>Deploy your Workflow in a Worker</li>
<li>Create a Service Binding to that Worker in your Pages project</li>
<li>Call the Worker remotely using the binding</li>
</ol>
<p>For example, if you have a Worker called <code>workflows-starter</code>, you would create a new Service Binding in your Pages project as follows, ensuring that the <code>service</code> name matches the name of the Worker your Workflow is defined in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17591.md")
</div>
<p>Your Worker can expose a specific method (or methods) that only other Workers or Pages Functions can call over the Service Binding.</p>
<p>In the following example, we expose a specific <code>createInstance</code> method that accepts our <code>Payload</code> and returns the <a href="/workflows/build/workers-api/#instancestatus"><code>InstanceStatus</code></a> from the Workflows API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17592.md")
</div>
<p>Your Pages Function would resemble the following:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17593.md")
</div>
<p>To learn more about binding to resources from Pages Functions, including how to bind via the Cloudflare dashboard, refer to the <a href="/pages/functions/bindings/#service-bindings">bindings documentation for Pages Functions</a>.</p>
<h3 id="using-fetch">Using fetch</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="service-bindings-vs-fetch">Service Bindings vs. fetch</h3>
@markup("md", "content/.markup/bodies/17588.md")
</aside>
<p>An alternative to setting up a Service Binding is to call the Worker over HTTP by using the Workflows <a href="/workflows/build/workers-api/#workflow">Workers API</a> to <code>create</code> a new Workflow instance for each incoming HTTP call to the Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17594.md")
</div>
<p>Your <a href="/pages/functions/get-started/">Pages Function</a> can then make a regular <code>fetch</code> call to the Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17595.md")
</div>
<p>You can also choose to authenticate these requests by passing a shared secret in a header and validating that in your Worker.</p>
<h3 id="next-steps">Next steps</h3>
<ul>
<li>Learn more about how to programmatically call and trigger Workflows from the <a href="/workflows/build/workers-api/">Workers API</a></li>
<li>Understand how to send <a href="/workflows/build/events-and-parameters/">events and parameters</a> when triggering a Workflow</li>
<li>Review the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and best practices for writing Workflows</li>
</ul>
