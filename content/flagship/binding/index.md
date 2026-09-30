<p>Workers access Flagship through a binding that you add to your Wrangler configuration file. The <code>binding</code> field sets the variable name you use in your Worker code.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8732.md")
</div>
<p>Replace <code>&lt;APP_ID&gt;</code> with the app ID from your Flagship app. If you have not created an app yet, refer to the <a href="/flagship/get-started/#create-an-app-and-a-flag">Get started guide</a>. With this configuration, the binding is available as <code>env.FLAGS</code>. Refer to <a href="/flagship/configuration/">Configuration</a> for additional options such as binding to multiple apps.</p>
<p>The binding provides type-safe methods for evaluating feature flags. If an evaluation fails or a flag is not found, the method returns the default value you provide.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8733.md")
</div>
<p>The binding has the type <code>Flagship</code> from the <code>@cloudflare/workers-types</code> package.</p>
<ul class="directory-listing"><li><a href="/flagship/binding/types/">Types</a></li><li><a href="/flagship/binding/methods/">Methods</a></li></ul>
