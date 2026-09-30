<p>Workflows allow you to build durable, multi-step applications using the Workers platform. A Workflow can automatically retry, persist state, run for hours or days, and coordinate between third-party APIs.</p>
<p>You can build Workflows to post-process file uploads to <a href="/r2/">R2 object storage</a>, automate generation of <a href="/workers-ai/">Workers AI</a> embeddings into a <a href="/vectorize/">Vectorize</a> vector database, or to trigger user lifecycle emails using <a href="/email-service/">Email Service</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17502.md")
</aside>
<p>In this guide, you will create and deploy a Workflow that fetches data, pauses, and processes results.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and pull down the complete Workflow we are building in this guide, run:</p>
<pre><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>Use this option if you are familiar with Cloudflare Workers or want to explore the code first and learn the details later.</p>
<p>Follow the steps below to learn how to build a Workflow from scratch.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17503.md")
</div></details>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17505.md")
</div>
<h2 id="2-write-your-workflow"><ol start="2">
<li>Write your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17506.md")
</div>
<h2 id="3-configure-your-workflow"><ol start="3">
<li>Configure your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17509.md")
</div>
<h2 id="4-write-your-api"><ol start="4">
<li>Write your API</li>
</ol></h2>
<p>Now, you'll need a place to call your Workflow.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17510.md")
</div>
<h2 id="5-develop-locally"><ol start="5">
<li>Develop locally</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17511.md")
</div>
<h2 id="6-deploy-your-workflow"><ol start="6">
<li>Deploy your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17512.md")
</div>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/workflows/build/events-and-parameters/"><h3 id="card-events-and-parameters-workflows-build-events-and-parameters">Events and parameters</h3><p>Pass data to Workflows and pause for external events with waitForEvent.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workflows/build/sleeping-and-retrying/"><h3 id="card-sleeping-and-retrying-workflows-build-sleeping-and-retrying">Sleeping and retrying</h3><p>Configure retry behavior and sleep patterns.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workflows/build/workers-api/"><h3 id="card-workers-api-workflows-build-workers-api">Workers API</h3><p>Explore the full Workflows API for programmatic control.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workflows/build/rules-of-workflows/"><h3 id="card-rules-of-workflows-workflows-build-rules-of-workflows">Rules of Workflows</h3><p>Understand the programming model and best practices.</p></a></p>
