<h1 id="changelog">Changelog</h1>

<h2 id="create-app-scoped-api-tokens-for-flagship"><a href="/changelog/post/2026-08-26-app-scoped-tokens/">Create app-scoped API tokens for Flagship</a></h2>
<p><em>2026-08-26</em></p>
<p>You can now create <strong>app-scoped API tokens</strong> for <a href="/flagship/">Flagship</a>. These tokens grant access only to the Flagship apps you select, instead of every app in the account.</p>
<p>When you create a custom token, open the resource dropdown (it defaults to <strong>Entire Account</strong>) and select <strong>Specified Flagship apps</strong>. Then choose the app and a <strong>Flagship App</strong> permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.</p>
<p>Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.</p>
<p>To create a token, refer to <a href="/flagship/api-tokens/">API tokens</a> or <a href="https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&amp;scope=specified_flagship_app">open the app-scoped token form</a> in the dashboard.</p>


<h2 id="manage-flagship-from-the-command-line-with-wrangler"><a href="/changelog/post/2026-07-16-wrangler-commands/">Manage Flagship from the command line with Wrangler</a></h2>
<p><em>2026-07-16</em></p>
<p><strong><a href="/workers/wrangler/">Wrangler</a></strong> now includes <code>wrangler flagship</code>, a command suite for managing <a href="/flagship/">Flagship</a> apps and feature flags from your terminal.</p>
<p>Create an app and, if you use it from a Worker, add it to your <code>wrangler.json</code> or <code>wrangler.jsonc</code> file as a binding:</p>
<pre><code class="language-bash">wrangler flagship apps create &quot;My Worker App&quot; \&#10;  &#45;-binding FLAGS \&#10;  &#45;-update-config&#10;</code></pre>
<p>Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:</p>
<pre><code class="language-bash">wrangler flagship flags create &lt;APP_ID&gt; new-checkout&#10;&#10;wrangler flagship flags create &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-variation control=old-checkout \&#10;  &#45;-variation treatment=new-checkout \&#10;  &#45;-default control \&#10;  &#45;-type string&#10;</code></pre>
<p>After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:</p>
<pre><code class="language-bash">wrangler flagship flags update &lt;APP_ID&gt; checkout-flow --default treatment&#10;wrangler flagship flags disable &lt;APP_ID&gt; checkout-flow&#10;wrangler flagship flags enable &lt;APP_ID&gt; checkout-flow&#10;</code></pre>
<p>For release workflows, use <code>rollout</code>, <code>split</code>, and <code>rules</code> to change exposure without redeploying your Worker:</p>
<pre><code class="language-bash">wrangler flagship flags rollout &lt;APP_ID&gt; new-checkout \&#10;  &#45;-to on \&#10;  &#45;-percentage 25 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags split &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-weight control=80 \&#10;  &#45;-weight treatment=20 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags rules update &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-priority 1 \&#10;  &#45;-when &quot;country equals US&quot;&#10;</code></pre>
<p>These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.</p>
<p>Refer to the <a href="/flagship/reference/wrangler-commands/"><code>wrangler flagship</code> command reference</a> for the full command guide.</p>


<h2 id="flagship-api-reference-now-available"><a href="/changelog/post/2026-06-10-api-reference/">Flagship API reference now available</a></h2>
<p><em>2026-06-10</em></p>
<p>The <strong><a href="/api/resources/flagship/">Flagship API reference</a></strong> is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.</p>
<p>For example, create a new boolean flag with the API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;key&quot;: &quot;new-checkout&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;default_variation&quot;: &quot;off&quot;,&#10;    &quot;variations&quot;: {&#10;      &quot;off&quot;: false,&#10;      &quot;on&quot;: true&#10;    },&#10;    &quot;rules&quot;: []&#10;  }&#x27;&#10;</code></pre>
<p>To create an API token, go to <a href="https://dash.cloudflare.com/?to=/:account/api-tokens">Account API Tokens</a> in the Cloudflare dashboard and search for Flagship.</p>
<p>The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the <a href="https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship">Flagship reference in the Cloudflare skill</a> to create and manage Flagship resources.</p>
<p>Refer to the <a href="/flagship/">Flagship documentation</a> to learn more about evaluating feature flags from your applications.</p>


<h2 id="flagship-now-in-public-beta"><a href="/changelog/post/2026-05-26-public-beta/">Flagship now in public beta</a></h2>
<p><em>2026-05-26</em></p>
<p><strong><a href="/flagship/">Flagship</a></strong> is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.</p>
<p>Evaluate a flag from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17724.md")</div>
<p>Start creating flags from the Cloudflare dashboard today. Refer to the <a href="/flagship/get-started/">Flagship documentation</a> to get started.</p>



