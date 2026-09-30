<p>To use Flagship in a Cloudflare Worker, add a Flagship binding to your Wrangler configuration file. The binding gives your Worker access to <code>env.FLAGS</code>, which provides methods to evaluate feature flags.</p>
<h2 id="add-the-binding">Add the binding</h2>
<p>Add the <code>flagship</code> block to your Wrangler configuration file with a binding name and your app ID.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1017.md")
</div>
<p>Replace <code>&lt;APP_ID&gt;</code> with the app ID from your Flagship app. If you have not created an app yet, refer to the <a href="/flagship/get-started/#create-an-app-and-a-flag">Get started guide</a>. The <code>binding</code> field sets the name you use to access Flagship in your Worker code (for example, <code>env.FLAGS</code>).</p>
<h2 id="bind-to-multiple-apps">Bind to multiple apps</h2>
<p>A single Worker can bind to multiple Flagship apps. Use the array form to define more than one binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1018.md")
</div>
<p>Each binding is available as a separate property on the <code>env</code> object (for example, <code>env.FLAGS</code> and <code>env.EXPERIMENT_FLAGS</code>).</p>
<h2 id="generate-types">Generate types</h2>
<p>After adding the binding, run <code>npx wrangler types</code> to generate TypeScript types. This creates the <code>Env</code> interface with each binding typed as <code>Flagship</code>.</p>
<pre><code class="language-ts">interface Env {&#10;	FLAGS: Flagship;&#10;	EXPERIMENT_FLAGS: Flagship;&#10;}&#10;</code></pre>
<h2 id="use-the-binding">Use the binding</h2>
<p>Call evaluation methods on <code>env.FLAGS</code> to resolve flag values at runtime. Each method accepts a flag key, a default value, and an optional evaluation context.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1019.md")
</div>
<p>Refer to the <a href="/flagship/binding/">binding API reference</a> for the full list of methods.</p>
<h2 id="local-development">Local development</h2>
<p>Flagship bindings work with <code>wrangler dev</code>. Local Workers use the live Flagship app configured by <code>app_id</code>. There is no local flag store. Make sure your local Wrangler configuration points to a valid Flagship app before testing evaluations.</p>
