<p>Cloudflare offers language software development kits (SDKs) as well as <code>curl</code> examples to demonstrate how to use the Cloudflare API. The SDK libraries allow you to interact with the Cloudflare API in language-specific syntax and more easily integrate with your existing applications.</p>
<p>Cloudflare currently offers the following SDKs:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go">Go</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">TypeScript</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python">Python</a></li>
</ul>
<h2 id="when-to-use-curl-vs-sdk">When to use cURL vs SDK</h2>
<p>There is no definite answer on which you should use. Instead, consider your use case and determine whether cURL or an SDK is the best fit.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>cURL</th>
<th>SDK</th>
</tr>
</thead>
<tbody>
<tr>
<td>Quick testing within the CLI</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Use within bash scripts or CI</td>
<td>✅</td>
<td>❌*</td>
</tr>
<tr>
<td>Usage from within an existing application or framework</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>More complex usage where you need to chain together outputs</td>
<td>❌</td>
<td>✅</td>
</tr>
</tbody>
</table>
<p>* It is possible, although not straight forward, to use the SDKs within bash scripts or CI environments with additional runtime dependencies and setup.</p>
<h2 id="example">Example</h2>
<p>The following are examples of how you would query all of the Cloudflare zones you have access to.</p>
<h3 id="with-curl">With cURL:</h3>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h3 id="with-the-typescript-sdk">With the TypeScript SDK:</h3>
<pre><code class="language-js">const client = new Cloudflare({&#10;	apiToken: process.env[&quot;CLOUDFLARE_API_TOKEN&quot;],&#10;});&#10;&#10;const zones = await client.zones.list();&#10;&#10;console.log(zones);&#10;</code></pre>
