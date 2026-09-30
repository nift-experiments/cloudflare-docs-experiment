<p>Because Agents run on Cloudflare Workers and Durable Objects, they can be tested using the same tools and techniques as Workers and Durable Objects.</p>
<h2 id="writing-and-running-tests">Writing and running tests</h2>
<h3 id="setup">Setup</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1863.md")
</aside>
<p>Before you write your first test, install the necessary packages:</p>
<pre><code class="language-sh">npm install vitest@^4.1.0 @cloudflare/vitest-plugin --save-dev&#10;</code></pre>
<p>Ensure that your <code>vitest.config.js</code> has the <code>cloudflareTest</code> plugin configured:</p>
<pre><code class="language-js">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: { configPath: &quot;./wrangler.jsonc&quot; },&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h3 id="write-a-test">Write a test</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1862.md")
</aside>
<p>Tests use the <code>vitest</code> framework. A basic test suite for your Agent can validate how your Agent responds to requests, but can also unit test your Agent's methods and state.</p>
<pre><code class="language-ts">import { env, exports } from &quot;cloudflare:workers&quot;;&#10;import {&#10;	createExecutionContext,&#10;	waitOnExecutionContext,&#10;} from &quot;cloudflare:test&quot;;&#10;import { describe, it, expect } from &quot;vitest&quot;;&#10;import worker from &quot;../src&quot;;&#10;import { Env } from &quot;../src&quot;;&#10;&#10;interface ProvidedEnv extends Env {}&#10;&#10;describe(&quot;make a request to my Agent&quot;, () =&gt; {&#10;	// Unit testing approach&#10;	it(&quot;responds with state&quot;, async () =&gt; {&#10;		// Provide a valid URL that your Worker can use to route to your Agent&#10;		// If you are using routeAgentRequest, this will be /agents/:agent/:name&#10;		const request = new Request&lt;unknown, IncomingRequestCfProperties&gt;(&#10;			&quot;http://example.com/agents/my-agent/agent-123&quot;,&#10;		);&#10;		const ctx = createExecutionContext();&#10;		const response = await worker.fetch(request, env, ctx);&#10;		await waitOnExecutionContext(ctx);&#10;		expect(await response.json()).toEqual({ hello: &quot;from your agent&quot; });&#10;	});&#10;&#10;	it(&quot;also responds with state&quot;, async () =&gt; {&#10;		const request = new Request(&quot;http://example.com/agents/my-agent/agent-123&quot;);&#10;		const response = await exports.default.fetch(request);&#10;		expect(await response.json()).toEqual({ hello: &quot;from your agent&quot; });&#10;	});&#10;});&#10;</code></pre>
<h3 id="run-tests">Run tests</h3>
<p>Running tests is done using the <code>vitest</code> CLI:</p>
<pre><code class="language-sh">npm run test&#10;&#35; or run vitest directly&#10;npx vitest&#10;</code></pre>
<pre><code class="language-txt">  MyAgent&#10;    ✓ should return a greeting (1 ms)&#10;&#10;Test Files  1 passed (1)&#10;</code></pre>
<p>Review the <a href="/workers/testing/vitest-integration/write-your-first-test/">documentation on testing</a> for additional examples and test configuration.</p>
<h2 id="running-agents-locally">Running Agents locally</h2>
<p>You can also run an Agent locally using the <code>wrangler</code> CLI:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<pre><code class="language-txt">Your Worker and resources are simulated locally via Miniflare. For more information, see: https://developers.cloudflare.com/workers/testing/local-development.&#10;&#10;Your worker has access to the following bindings:&#10;&#45; Durable Objects:&#10;  &#45; MyAgent: MyAgent&#10;  Starting local server...&#10;[wrangler:inf] Ready on http://localhost:53645&#10;</code></pre>
<p>This spins up a local development server that runs the same runtime as Cloudflare Workers, and allows you to iterate on your Agent's code and test it locally without deploying it.</p>
<p>Visit the <a href="https://developers.cloudflare.com/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> docs to review the CLI flags and configuration options.</p>
