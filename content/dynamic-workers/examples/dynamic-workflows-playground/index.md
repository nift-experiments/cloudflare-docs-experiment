<p>Try the <a href="https://github.com/cloudflare/dynamic-workflows/tree/main/examples/basic">dynamic workflows playground</a>, write workflow logic in JavaScript, execute it from a Dynamic Worker, and log every step in real time.</p>
<p>This example shows you how to run <a href="/workflows/">Cloudflare Workflows</a> from a <a href="/dynamic-workers/">Dynamic Worker</a> to get full durable execution, including step retries, sleep, hibernation, and <code>waitForEvent</code>, for any workflow you need to run on demand.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/dynamic-workflows/tree/main/examples/basic"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="how-it-works">How it works</h2>
<p>There are two parts:</p>
<ul>
<li><strong>Worker Loader</strong> — The Worker that runs your platform logic. It receives a request, loads the user's workflow code as a Dynamic Worker, and gives it a Workflow binding so it can create and run workflows.</li>
<li><strong>Dynamic Worker</strong> — This is where the workflow is defined. You write the workflow logic here, including which steps need to run, how long it sleeps, and what events it waits for.</li>
</ul>
<p>The <a href="https://www.npmjs.com/package/@cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a> library connects the two. When the Dynamic Worker creates a workflow, the library tags it with information about which Dynamic Worker created it. That tag is persisted by the Workflows engine, so when a workflow needs to resume after a sleep, a failure, or a server restart, the engine knows which Dynamic Worker to reload to continue execution.</p>
<p>For a full walkthrough of the library and how to set it up, refer to the <a href="/dynamic-workers/usage/dynamic-workflows/">Dynamic Workflows guide</a>.</p>
<h2 id="what-this-playground-includes">What this playground includes</h2>
<ul>
<li><strong>Worker Loader and Dynamic Worker setup</strong> — A full working example of a Worker Loader that loads workflow code at runtime and a Dynamic Worker that runs it with durable execution, using <a href="https://www.npmjs.com/package/@cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a>.</li>
<li><strong>Live log streaming</strong> — Every <code>console.log()</code> and <code>console.warn()</code> from the Dynamic Worker is captured and streamed to the browser in real time, so you can see what is happening inside each step as it runs.</li>
<li><strong>Source persistence</strong> — The workflow code is saved so that if the workflow pauses (for example, during a <code>step.sleep()</code>) and the server recycles the process, it can reload the same code and resume where it left off.</li>
</ul>
