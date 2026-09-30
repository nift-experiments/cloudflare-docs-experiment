<p>A KV namespace is a key-value database replicated to Cloudflare’s global network.</p>
<p>Bind your KV namespaces through Wrangler or via the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9523.md")
</aside>
<h2 id="jurisdictions">Jurisdictions</h2>
<p>Namespaces can optionally be restricted to a jurisdiction to durably store data only within a specific region. This feature is currently in private beta. Refer to <a href="/kv/reference/data-location/">Data location</a> for more information.</p>
<h2 id="bind-your-kv-namespace-through-wrangler">Bind your KV namespace through Wrangler</h2>
<p>To bind KV namespaces to your Worker, assign an array of the below object to the <code>kv_namespaces</code> key.</p>
<ul>
<li>
<p><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The binding name used to refer to the KV namespace.</li>
</ul>
</li>
<li>
<p><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The ID of the KV namespace.</li>
</ul>
</li>
<li>
<p><code>preview_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The ID of the KV namespace used during <code>wrangler dev</code>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9524.md")
</div>
<h2 id="bind-your-kv-namespace-via-the-dashboard">Bind your KV namespace via the dashboard</h2>
<p>To bind the namespace to your Worker in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your **Worker**.
3. Select **Settings** > **Bindings**.
4. Select **Add**.
5. Select **KV Namespace**.
6. Enter your desired variable name (the name of the binding).
7. Select the KV namespace you wish to bind the Worker to.
8. Select **Deploy**.
