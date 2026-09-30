<p>In this guide, you will create a feature flag in Flagship and evaluate it inside a Cloudflare Worker.</p>
<h2 id="create-an-app-and-a-flag">Create an app and a flag</h2>
<p>In this example, you will create a boolean flag called <code>new-checkout</code> that controls whether users see a new checkout experience.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Flagship</strong>.</li>
<li>Select <strong>Create app</strong>. Give the app a name that matches your project or service (for example, <code>checkout-service</code>).</li>
<li>Inside the app, select <strong>Create flag</strong>.</li>
<li>Create a boolean flag with the key <code>new-checkout</code>. Optionally, add <a href="/flagship/targeting/">targeting rules</a> to control who sees the flag.</li>
<li>Turn on the flag and select <strong>Save</strong>.</li>
</ol>
<h2 id="add-the-flagship-binding-to-your-worker">Add the Flagship binding to your Worker</h2>
<p>Add the Flagship binding in your Wrangler configuration file so your Worker can evaluate flags through a binding.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1010.md")
</div>
<p>Replace <code>&lt;APP_ID&gt;</code> with the app ID shown in the <a href="https://dash.cloudflare.com/?to=/:account/flagship">Cloudflare dashboard</a>. The <code>binding</code> field sets the name you use to access Flagship in your Worker code. In this example, the binding is available as <code>env.FLAGS</code>.</p>
<p>After updating the Wrangler configuration, run <code>npx wrangler types</code> to generate TypeScript types for the binding.</p>
<h2 id="evaluate-the-flag-in-your-worker">Evaluate the flag in your Worker</h2>
<p>Use the <code>env.FLAGS</code> binding to evaluate the flag. The binding provides type-safe methods that return the flag value and fall back to the default you provide if evaluation fails.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1011.md")
</div>
<p>The third argument to <code>getBooleanValue</code> is the <a href="/flagship/concepts/#evaluation-context">evaluation context</a>. Flagship uses the context attributes to match targeting rules. In this example, the <code>userId</code> attribute is passed so that percentage rollouts and user-specific targeting work correctly.</p>
<h2 id="deploy-and-test">Deploy and test</h2>
<p>Deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Test flag evaluation by sending a request:</p>
<pre><code class="language-sh">curl &quot;https://&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/?userId=user-42&quot;&#10;</code></pre>
<p>Change the flag value or targeting rules in the dashboard and observe the updated response. Flag changes propagate globally within seconds.</p>
<h2 id="optional-use-the-openfeature-sdk">(Optional) Use the OpenFeature SDK</h2>
<p>If you prefer the <a href="https://openfeature.dev/">OpenFeature</a> standard interface, or if you are running outside of a Cloudflare Worker, you can use the <a href="https://www.npmjs.com/package/@cloudflare/flagship"><code>@cloudflare/flagship</code></a> SDK instead of the binding.</p>
<p>Install the SDK:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Evaluate flags using the OpenFeature client:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1016.md")
</div></div>
<p>Refer to the <a href="/flagship/sdk/">SDK documentation</a> for detailed setup instructions.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Manage flags from the command line with the <a href="/flagship/reference/wrangler-commands/"><code>wrangler flagship</code> commands</a>.</li>
<li>Learn about <a href="/flagship/targeting/">targeting rules</a> to serve different values based on user attributes.</li>
<li>Explore the full <a href="/flagship/binding/">binding API reference</a> for all evaluation methods.</li>
<li>Read about <a href="/flagship/targeting/percentage-rollouts/">percentage rollouts</a> for gradual feature releases.</li>
<li>Create an <a href="/flagship/api-tokens/">API token</a> to evaluate flags from a server-side environment.</li>
<li>Refer to the <a href="/flagship/reference/api-reference/">Flagship API reference</a> to manage Flagship programmatically.</li>
</ul>
