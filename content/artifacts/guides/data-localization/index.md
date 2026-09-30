<p>Artifacts jurisdictions ensure repo data is stored and processed only within a selected location. Set a jurisdiction when you create a namespace to apply the restriction to every repo in that namespace.</p>
<h2 id="supported-jurisdictions">Supported jurisdictions</h2>
<p>Artifacts supports the following jurisdictions:</p>
<table>
<thead>
<tr>
<th>Jurisdiction</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eu</code></td>
<td>European Union</td>
</tr>
<tr>
<td><code>us</code></td>
<td>United States</td>
</tr>
</tbody>
</table>
<h2 id="create-a-namespace-with-a-jurisdiction">Create a namespace with a jurisdiction</h2>
<p>To restrict a namespace to the European Union, set <code>jurisdiction</code> to <code>eu</code> when you create the namespace:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>The selected jurisdiction applies to every repo in the namespace. You cannot change the jurisdiction after creating the namespace. The <code>jurisdiction</code> parameter is optional. If you omit it, the namespace remains unrestricted.</p>
<p>For endpoint details, refer to the <a href="/artifacts/api/rest-api/#create-a-namespace">Artifacts REST API reference</a>.</p>
