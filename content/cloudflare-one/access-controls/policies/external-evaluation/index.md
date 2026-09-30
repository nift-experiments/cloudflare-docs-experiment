<p>With Cloudflare Access, you can create Allow or Block policies which evaluate the user based on custom criteria. This is done by adding an <strong>External Evaluation</strong> rule to your policy. The <strong>External Evaluation</strong> selector requires two values:</p>
<ul>
<li><strong>Evaluate URL</strong> — the API endpoint containing your business logic.</li>
<li><strong>Keys URL</strong> — the key that Access uses to verify that the response came from your API</li>
</ul>
<p>After the user authenticates with your identity provider, Access sends the user's identity to the external API at <strong>Evaluate URL</strong>. The external API returns a True or False response to Access, which will then allow or deny access to the user. To protect against man-in-the-middle attacks, Access signs all requests with your Access account key and checks that responses are signed by the key at <strong>Keys URL</strong>.</p>
<p>You can set up External Evaluation rules using any API service, but to get started quickly we recommend using <a href="/workers/">Cloudflare Workers</a>.</p>
<h2 id="set-up-external-api-and-key-with-cloudflare-workers">Set up external API and key with Cloudflare Workers</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/workers/get-started/guide/">Workers account</a></li>
<li>Install <a href="https://docs.npmjs.com/getting-started">npm</a></li>
<li>Install <a href="https://nodejs.org/en/">Node.js</a></li>
<li>Application protected by Access</li>
</ul>
<h3 id="1-create-a-new-worker"><ol>
<li>Create a new Worker</li>
</ol></h3>
<ol>
<li>Open a terminal and clone our example project.</li>
</ol>
<pre><code class="language-sh">npm create cloudflare@latest my-worker -- --template https://github.com/cloudflare/workers-access-external-auth-example&#10;</code></pre>
<ol start="2">
<li>Go to the project directory.</li>
</ol>
<pre><code class="language-sh">cd my-worker&#10;</code></pre>
<ol start="3">
<li>Create a <a href="/kv/concepts/kv-namespaces/">Workers KV namespace</a> to store the key. The binding name should be <code>KV</code> if you want to run the example as written.</li>
</ol>
<pre><code class="language-sh">npx wrangler kv namespace create &quot;KV&quot;&#10;</code></pre>
<p>The command will output the binding name and KV namespace ID, for example</p>
<pre><code class="language-txt">  [[kv_namespaces]]&#10;   binding = &quot;KV&quot;&#10;   id = &quot;YOUR_KV_NAMESPACE_ID&quot;&#10;</code></pre>
<ol start="4">
<li>
<p>Open the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in an editor and insert the following:</p>
<ul>
<li><code>[[kv_namespaces]]</code>: Add the output generated in the previous step.</li>
<li><code>&lt;TEAM_NAME&gt;</code>: your Cloudflare One <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/4594.md")
</div>.
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4595.md")
</div>
<h3 id="2-program-your-business-logic"><ol start="2">
<li>Program your business logic</li>
</ol></h3>
<ol>
<li>Open <code>index.js</code> and modify the <code>externalEvaluation</code> function to perform logic on any identity-based data sent by Access.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4593.md")
</aside>
<ol start="2">
<li>Deploy the Worker to Cloudflare's global network.</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>The Worker will be deployed to your <code>*.workers.dev</code> subdomain at <code>my-worker.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<h3 id="3-generate-a-key"><ol start="3">
<li>Generate a key</li>
</ol></h3>
<p>To generate an RSA private/public key pair:</p>
<ol>
<li>
<p>Open a browser and go to <code>https://my-worker.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/keys</code>.</p>
</li>
<li>
<p>(Optional) Verify that the key has been stored in the <code>KV</code> namespace:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers KV</strong> page.</li>
</ol>
</li>
</ol>
<div class="nb-dash-button"></div>
   2. Select **View** next to `my-worker-KV`.
<p>Other key formats (such as DSA) are not supported at this time.</p>
<h3 id="4-create-an-external-evaluation-rule"><ol start="4">
<li>Create an External Evaluation rule</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</p>
</li>
<li>
<p>Edit an existing policy or select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Add the following rule to your policy:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Rule Type</th>
<th>Selector</th>
<th>Evaluate URL</th>
<th>Keys URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>External Evaluation</td>
<td><code>https://my-worker.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/</code></td>
<td><code>https://my-worker.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/keys/</code></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>
<p>Save the policy.</p>
</li>
<li>
<p>Go to <strong>Access controls</strong> &gt; <strong>Applications</strong> and edit the application for which you want to apply the External Evaluation rule.</p>
</li>
<li>
<p>In the <strong>Policies</strong> tab, add the policy that contains the External Evaluation rule.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>When a user logs in to your application, Access will now check their email, device, location, and other identity-based data against your business logic.</p>
<h3 id="troubleshooting-the-worker">Troubleshooting the Worker</h3>
<p>To debug your External Evaluation rule:</p>
<ol>
<li>Go to your Worker directory.</li>
</ol>
<pre><code class="language-sh">cd my-worker&#10;</code></pre>
<ol start="2">
<li>
<p>Open the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in an editor and set the <code>debug</code> variable to <code>TRUE</code>.</p>
</li>
<li>
<p>Deploy your changes.</p>
</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="4">
<li>Next, start a session to output realtime logs from your Worker.</li>
</ol>
<pre><code class="language-sh">wrangler tail -f pretty&#10;</code></pre>
<ol start="5">
<li>
<p>Log in to your Access application.</p>
<p>The session logs should show an incoming and outgoing JWT. The incoming JWT was sent by Access to the Worker API, while the outgoing JWT was sent by the Worker back to Access.</p>
</li>
<li>
<p>To decode the contents of a JWT, you can copy the token into <a href="https://jwt.io/">jwt.io</a>.</p>
<p>The incoming JWT should contain the user's identity data. The outgoing JWT should look similar to:</p>
</li>
</ol>
<pre><code class="language-js">{&#10;&quot;success&quot;: true,&#10;&quot;iat&quot;: 1655409315,&#10;&quot;exp&quot;: 1655409375,&#10;&quot;nonce&quot;: &quot;9J2E9Xg6wYj8tlnA5MV4Zgp6t8rzmS0Q&quot;&#10;}&#10;</code></pre>
<p>Access checks the outgoing JWT for all of the following criteria:</p>
<ul>
<li>Token was signed by <strong>Keys URL</strong>.</li>
<li>Expiration date has not elapsed.</li>
<li>API returns <code>&quot;success&quot;: true</code>.</li>
<li><code>nonce</code> is unchanged from the incoming JWT. The <code>nonce</code> value is unique per request.</li>
</ul>
<p>If any condition fails, the External Evaluation rule evaluates to false.</p>
