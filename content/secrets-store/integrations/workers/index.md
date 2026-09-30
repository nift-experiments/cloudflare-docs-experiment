<p><a href="/secrets-store/">Cloudflare Secrets Store</a> is a secure, centralized location in which account-level secrets are stored and managed. The secrets are securely encrypted and stored across all Cloudflare data centers.</p>
<p>Consider the steps below to learn how to use values from your account secrets store with <a href="/workers/">Cloudflare Workers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13801.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>
<p>If <a href="#via-dashboard">using the Dashboard</a>, make sure you already have a Workers application. Refer to the <a href="/workers/get-started/dashboard/">Workers get started</a> for guidance.</p>
</li>
<li>
<p>You should also have a store created under the <strong>Secrets Store</strong> tab on the Dashboard. The first store in your account is created automatically when a user with <a href="/secrets-store/access-control/">Super Administrator or Secrets Store Admin role</a> interacts with it.</p>
<pre><code>  - If no store exists in your account yet and you have the necessary permissions, you can use the [Wrangler command](/workers/wrangler/commands/secrets-store/#secrets-store-store) `secrets-store store create &lt;name&gt; --remote` to create your first store.&#10;</code></pre>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-mode">Local development mode</h3>
@markup("md", "content/.markup/bodies/13800.md")
</aside>
<h2 id="1-set-up-account-secrets-in-secrets-store"><ol>
<li>Set up account secrets in Secrets Store</li>
</ol></h2>
<p>Follow the steps below to create secrets. You must have a <a href="/secrets-store/access-control/">Super Administrator or a Secrets Store Admin role</a> within your Cloudflare account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13799.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13805.md")
</div></div>
<p>Refer to <a href="/secrets-store/manage-secrets/">manage account secrets</a> for further options.</p>
<h2 id="2-bind-an-account-secret-to-your-worker"><ol start="2">
<li>Bind an account secret to your Worker</li>
</ol></h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Worker to interact with resources on your Cloudflare account.</p>
<p>To bind an account secret to your Worker, you must have one of the following <a href="/secrets-store/access-control/">roles within your Cloudflare account</a>:</p>
<ul>
<li>Super Administrator</li>
<li>Secrets Store Deployer</li>
</ul>
<h3 id="via-wrangler">Via Wrangler</h3>
<ol>
<li>Add a Secrets Store binding to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:
<ul>
<li><code>binding</code>: a descriptive name for your binding. This will be used in the Workers application when <a href="/secrets-store/integrations/workers/#3-access-the-secret-on-the-env-object">accessing your secret on the <code>env</code> object</a>.</li>
<li><code>store_id</code>: the corresponding Secrets Store ID where your account secret was created.</li>
<li><code>secret_name</code>: the unique secret name, defined when your account secret was created.</li>
</ul>
</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13806.md")
</div>
<h3 id="via-dashboard">Via Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a Workers application.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Bindings</strong> and select <strong>Add</strong>.</li>
<li>On the <strong>Add a resource binding</strong> side panel, choose <strong>Secrets Store</strong>.</li>
<li>Fill in the required fields:
<ul>
<li><strong>Variable name</strong>: a name for the binding. This will be used for your Worker to access the secret (<a href="#3-access-the-secret-on-the-env-object">step 3</a> below).</li>
<li><strong>Secret name</strong>: select from the list of available account secrets created in <a href="#1-set-up-account-secrets-in-secrets-store">step 1</a>.</li>
<li>(Optional - Admins only) If the secret you need does not exist yet, select <strong>Create secret</strong>. This will add an account level secret in the same way as if you had <a href="/secrets-store/manage-secrets/">created it on the Secrets Store</a>.</li>
</ul>
</li>
<li>Select <strong>Deploy</strong> to deploy your binding. When deploying, there are two options:
<ul>
<li><strong>Deploy:</strong> Immediately deploy the binding to 100% of your audience.</li>
<li><strong>Save version:</strong> Save a version of the binding which you can deploy in the future.</li>
</ul>
</li>
</ol>
<h2 id="3-access-the-secret-on-the-env-object"><ol start="3">
<li>Access the secret on the <code>env</code> object</li>
</ol></h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> are located on the <code>env</code> object. To access the secret you first need an asynchronous call.</p>
<h3 id="call-get-on-the-binding-variable">Call <code>get()</code> on the binding variable</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-mode-1">Local development mode</h3>
@markup("md", "content/.markup/bodies/13798.md")
</aside>
<pre><code class="language-js">export default {&#10;  async fetch(request, env) {&#10;    // Example of using the secret safely in an API request&#10;		const APIkey = await env.&lt;BINDING_VARIABLE&gt;.get()&#10;&#10;    const response = await fetch(&quot;https://api.example.com/data&quot;, {&#10;      headers: { &quot;Authorization&quot;: `Bearer ${APIKey}` },&#10;    });&#10;&#10;    if (!response.ok) {&#10;      return new Response(&quot;Failed to fetch data&quot;, { status: response.status });&#10;    }&#10;&#10;    const data = await response.json();&#10;    return new Response(JSON.stringify(data), {&#10;      headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
