<p><a href="https://upstash.com/">Upstash</a> is a serverless database with Redis* and Kafka API. Upstash also offers QStash, a task queue/scheduler designed for the serverless.</p>
<h2 id="upstash-for-redis">Upstash for Redis</h2>
<p>To set up an integration with Upstash:</p>
<ol>
<li>
<p>You need an existing Upstash database to connect to. <a href="https://docs.upstash.com/redis#create-a-database">Create an Upstash database</a> or <a href="https://docs.upstash.com/redis/howto/connectclient">load data from an existing database to Upstash</a>.</p>
</li>
<li>
<p>Insert some data to your Upstash database. You can add data to your Upstash database in two ways:</p>
<ul>
<li>Use the CLI directly from your Upstash console.</li>
<li>Alternatively, install <a href="https://redis.io/docs/getting-started/installation/">redis-cli</a> locally and run the following commands.</li>
</ul>
</li>
</ol>
<pre><code class="language-sh">set GB &quot;Ey up?&quot;&#10;</code></pre>
<pre><code class="language-sh">OK&#10;</code></pre>
<pre><code class="language-sh">set US &quot;Yo, what’s up?&quot;&#10;</code></pre>
<pre><code class="language-sh">OK&#10;</code></pre>
<pre><code class="language-sh">set NL &quot;Hoi, hoe gaat het?&quot;&#10;</code></pre>
<pre><code class="language-sh">OK&#10;</code></pre>
<ol start="3">
<li>
<p>Configure the Upstash Redis credentials in your Worker:</p>
<p>You need to add your Upstash Redis database URL and token as secrets to your Worker. Get these from your <a href="https://console.upstash.com">Upstash Console</a> under your database details, then add them as secrets using Wrangler:</p>
</li>
</ol>
<pre><code class="language-sh">&#35; Add the Upstash Redis URL as a secret&#10;npx wrangler secret put UPSTASH_REDIS_REST_URL&#10;&#35; When prompted, paste your Upstash Redis REST URL&#10;&#10;&#35; Add the Upstash Redis token as a secret&#10;npx wrangler secret put UPSTASH_REDIS_REST_TOKEN&#10;&#35; When prompted, paste your Upstash Redis REST token&#10;</code></pre>
<ol start="4">
<li>In your Worker, install the <code>@upstash/redis</code>, a HTTP client to connect to your database and start manipulating data:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="5">
<li>The following example shows how to make a query to your Upstash database in a Worker. The credentials needed to connect to Upstash have been added as secrets to your Worker.</li>
</ol>
<pre><code class="language-js">import { Redis } from &quot;@upstash/redis/cloudflare&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		const redis = Redis.fromEnv(env);&#10;&#10;		const country = request.headers.get(&quot;cf-ipcountry&quot;);&#10;		if (country) {&#10;			const greeting = await redis.get(country);&#10;			if (greeting) {&#10;				return new Response(greeting);&#10;			}&#10;		}&#10;&#10;		return new Response(&quot;Hello What&#x27;s up!&quot;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16853.md")
</aside>
<p>To learn more about Upstash, refer to the <a href="https://docs.upstash.com/redis">Upstash documentation</a>.</p>
<h2 id="upstash-qstash">Upstash QStash</h2>
<p>To set up an integration with Upstash QStash:</p>
<ol>
<li>
<p>Configure the <a href="https://docs.upstash.com/qstash#1-public-api">publicly available HTTP endpoint</a> that you want to send your messages to.</p>
</li>
<li>
<p>Configure the Upstash QStash credentials in your Worker:</p>
<p>You need to add your Upstash QStash token as a secret to your Worker. Get your token from your <a href="https://console.upstash.com">Upstash Console</a> under QStash settings, then add it as a secret using Wrangler:</p>
</li>
</ol>
<pre><code class="language-sh">&#35; Add the QStash token as a secret&#10;npx wrangler secret put QSTASH_TOKEN&#10;&#35; When prompted, paste your QStash token&#10;</code></pre>
<ol start="3">
<li>In your Worker, install the <code>@upstash/qstash</code>, a HTTP client to connect to your database QStash endpoint:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="4">
<li>Refer to the <a href="https://docs.upstash.com/qstash/quickstarts/cloudflare-workers#3-use-qstash-in-your-handler">Upstash documentation on how to receive webhooks from QStash in your Cloudflare Worker</a>.</li>
</ol>
<p>* Redis is a trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Upstash is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Upstash.</p>
