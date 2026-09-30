<p>By default, containers run in the location nearest to the incoming request with a pre-fetched image. Use placement constraints to restrict where your containers run for data residency, compliance, or latency requirements.</p>
<h2 id="regional-constraints">Regional constraints</h2>
<p>Use the <code>regions</code> constraint to limit container placement to specific geographic areas:</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Description</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ENAM</code></td>
<td>Eastern North America</td>
<td></td>
</tr>
<tr>
<td><code>WNAM</code></td>
<td>Western North America</td>
<td></td>
</tr>
<tr>
<td><code>EEUR</code></td>
<td>Eastern Europe</td>
<td></td>
</tr>
<tr>
<td><code>WEUR</code></td>
<td>Western Europe</td>
<td></td>
</tr>
<tr>
<td><code>APAC</code></td>
<td>Asia Pacific</td>
<td></td>
</tr>
<tr>
<td><code>SAM</code></td>
<td>South America</td>
<td></td>
</tr>
<tr>
<td><code>ME</code></td>
<td>Middle East</td>
<td>Limited capacity</td>
</tr>
<tr>
<td><code>OC</code></td>
<td>Oceania</td>
<td>Limited capacity</td>
</tr>
<tr>
<td><code>AFR</code></td>
<td>Africa</td>
<td>Limited capacity</td>
</tr>
</tbody>
</table>
<p>Limited capacity regions (ME, OC, AFR) cannot be used exclusively. Include at least one other region, or contact support for dedicated access.</p>
<h2 id="jurisdictional-constraints">Jurisdictional constraints</h2>
<p>Use the <code>jurisdiction</code> constraint to restrict containers to compliance boundaries:</p>
<table>
<thead>
<tr>
<th>Jurisdiction</th>
<th>Regions</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eu</code></td>
<td>EEUR, WEUR</td>
<td>EU data residency</td>
</tr>
<tr>
<td><code>fedramp</code></td>
<td>ENAM, WNAM</td>
<td>FedRAMP regions</td>
</tr>
</tbody>
</table>
<p>When you specify both <code>jurisdiction</code> and <code>regions</code>, the regions must be valid for that jurisdiction. For example, specifying <code>jurisdiction: &quot;eu&quot;</code> with <code>regions: [&quot;ENAM&quot;]</code> is invalid.</p>
<h2 id="configure-placement">Configure placement</h2>
<p>Set placement constraints in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7152.md")
</div>
<p>Refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a> for more details on how placement affects container startup and routing.</p>
