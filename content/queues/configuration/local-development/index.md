<p>Queues support local development workflows using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers. Wrangler runs the same version of Queues as Cloudflare runs globally.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To develop locally with Queues, you will need:</p>
<ul>
<li>
<p><a href="https://blog.cloudflare.com/wrangler3/">Wrangler v3.1.0</a> or later.</p>
</li>
<li>
<p>Node.js version of <code>18.0.0</code> or later. Consider using a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node versions.</p>
</li>
<li>
<p>If you are new to Queues and/or Cloudflare Workers, refer to the <a href="/queues/get-started/">Queues tutorial</a> to install <code>wrangler</code> and deploy their first Queue.</p>
</li>
</ul>
<h2 id="start-a-local-development-session">Start a local development session</h2>
<p>Open your terminal and run the following commands to start a local development session:</p>
<pre><code class="language-sh">npx wrangler@latest dev&#10;</code></pre>
<pre><code class="language-sh">&#45;-----------------&#10;Your Worker and resources are simulated locally via Miniflare. For more information, see: https://developers.cloudflare.com/workers/testing/local-development.&#10;&#10;Your worker has access to the following bindings:&#10;&#45; Queues: &lt;QUEUE-NAME&gt;&#10;</code></pre>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment Queues runs in so you can test your Workers <em>before</em> you deploy to production.</p>
<p>Refer to the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code> documentation</a> to learn more about how to configure a local development session.</p>
<h2 id="separating-producer-consumer-workers">Separating producer &amp; consumer Workers</h2>
Wrangler supports running multiple Workers simultaneously with a single command. If your architecture separates the producer and consumer into distinct Workers, you can use this functionality to test the entire message flow locally.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11264.md")
</aside>
<p>For example, if your project has the following directory structure:</p>
<pre><code>producer-worker/&#10;├── wrangler.jsonc&#10;├── index.ts&#10;└── consumer-worker/&#10;    ├── wrangler.jsonc&#10;    └── index.ts&#10;</code></pre>
<p>You can start development servers for both workers with the following command:</p>
<pre><code class="language-sh">npx wrangler@latest dev -c wrangler.jsonc -c consumer-worker/wrangler.jsonc --persist-to .wrangler/state&#10;</code></pre>
<p>When the producer Worker sends messages to the queue, the consumer Worker will automatically be invoked to handle them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11263.md")
</aside>
<h2 id="known-issues">Known Issues</h2>
- Queues does not support Wrangler remote mode (`wrangler dev --remote`).
