<p>To purge zone versions via the Cloudflare API, follow these steps:</p>
<h2 id="step-1-retrieve-the-environment-id">Step 1: Retrieve the environment ID</h2>
<p>First, retrieve your zone's environment ID by sending a request to the following API endpoint:</p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/&lt;zone_id&gt;/environments&#10;</code></pre>
<p>This API call will return a JSON response similar to the example below:</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;environments&quot;: [&#10;      {&#10;        &quot;name&quot;: &quot;Production&quot;,&#10;        &quot;ref&quot;: &quot;12abcd3e45f678940a573f51834a54&quot;,&#10;        &quot;version&quot;: 0,&#10;        &quot;expression&quot;: &quot;(cf.zone.name eq \&quot;example.com\&quot;)&quot;,&#10;        &quot;locked_on_deployment&quot;: false,&#10;        &quot;position&quot;: {&#10;          &quot;before&quot;: &quot;5d41402abc4b2a76b9719d911017c&quot;&#10;        }&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;Staging&quot;,&#10;        &quot;ref&quot;: &quot;5d41402abc4b2a76b9719d911017c&quot;,&#10;        &quot;version&quot;: 0,&#10;        &quot;expression&quot;: &quot;((cf.edge.server_ip in {1.2.3.4 5.6.7.8})) and (cf.zone.name eq \&quot;example.com\&quot;)&quot;,&#10;        &quot;locked_on_deployment&quot;: false,&#10;        &quot;position&quot;: {&#10;          &quot;before&quot;: &quot;49f0bad299687c62334182178bfd&quot;,&#10;          &quot;after&quot;: &quot;12abcd3e45f678940a573f51834a54&quot;&#10;        }&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;Development&quot;,&#10;        &quot;ref&quot;: &quot;49f0bad299687c62334182178bfd&quot;,&#10;        &quot;version&quot;: 0,&#10;        &quot;expression&quot;: &quot;((any(http.request.cookies[\&quot;development\&quot;][*] eq \&quot;true\&quot;))) and (cf.zone.name eq \&quot;example.com\&quot;)&quot;,&#10;        &quot;locked_on_deployment&quot;: false,&#10;        &quot;position&quot;: {&#10;          &quot;after&quot;: &quot;5d41402abc4b2a76b9719d911017c&quot;&#10;        }&#10;      }&#10;    ]&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>In this particular example, we have three environments: Production, Staging, and Development. You can find the environment ID in the <code>ref</code> field.</p>
<h2 id="step-2-purge-cache-per-environment">Step 2: Purge cache per environment</h2>
<p>To purge the Production environment, use the general cache purge endpoint:</p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/&lt;zone_id&gt;/purge_cache/&#10;</code></pre>
<p>To purge non-production environments, you must use a new <code>purge_cache</code> endpoint and specify the environment you would like to purge.</p>
<p>To purge the Staging environment from the example above, send a request to the following endpoint:</p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/&lt;zone_id&gt;/environments/5d41402abc4b2a76b9719d911017c/purge_cache/&#10;</code></pre>
<p>To purge the Development environment from the example above, send a request to the following endpoint:</p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/&lt;zone_id&gt;/environments/49f0bad299687c62334182178bfd/purge_cache/&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3865.md")
</aside>
