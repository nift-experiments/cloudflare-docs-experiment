<p>Learn how the location of data stored in D1 is determined, including where the database runs and how you optimize that location based on your needs.</p>
<h2 id="automatic-recommended">Automatic (recommended)</h2>
<p>By default, D1 will automatically create your primary database instance in a location close to where you issued the request to create a database. In most cases this allows D1 to choose the optimal location for your database on your behalf.</p>
<h2 id="restrict-database-to-a-jurisdiction">Restrict database to a jurisdiction</h2>
<p>Jurisdictions are used to create D1 databases that only run and store data within a region to help comply with data locality regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</p>
<p>Workers may still access the database constrained to a jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the database itself runs and persists data. Consider using <a href="/data-localization/regional-services/">Regional Services</a> to control the regions from which Cloudflare responds to requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7372.md")
</aside>
<h3 id="supported-jurisdictions">Supported jurisdictions</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>eu</td>
<td>The European Union</td>
</tr>
<tr>
<td>fedramp</td>
<td>FedRAMP-compliant data centers</td>
</tr>
</tbody>
</table>
<h3 id="use-the-dashboard">Use the dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>D1 SQL Database</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Database</strong>.</li>
<li>Under <strong>Data location</strong>, select <strong>Specify jurisdiction</strong> and choose a jurisdiction from the list.</li>
<li>Select <strong>Create</strong> to create your database.</li>
</ol>
<h3 id="use-wrangler">Use wrangler</h3>
<pre><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction=eu&#10;</code></pre>
<h3 id="use-rest-api">Use REST API</h3>
<pre><code class="language-curl">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKENn&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<h2 id="provide-a-location-hint">Provide a location hint</h2>
<p>Location hint is an optional parameter you can provide to indicate your desired geographical location for your primary database instance.</p>
<p>You may want to explicitly provide a location hint in cases where the majority of your writes to a specific database come from a different location than where you are creating the database from. Location hints can be useful when:</p>
<ul>
<li>Working in a distributed team.</li>
<li>Creating databases specific to users in specific locations.</li>
<li>Using continuous deployment (CD) or Infrastructure as Code (IaC) systems to programmatically create your databases.</li>
</ul>
<p>Provide a location hint when creating a D1 database when:</p>
<ul>
<li>Using <a href="/workers/wrangler/commands/d1/"><code>wrangler d1</code></a> to create a database.</li>
<li>Creating a database <a href="https://dash.cloudflare.com/?to=/:account/workers/d1">via the Cloudflare dashboard</a>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7371.md")
</aside>
<h3 id="use-wrangler-1">Use wrangler</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7370.md")
</aside>
<p>To provide a location hint when creating a new database, pass the <code>--location</code> flag with a valid location hint:</p>
<pre><code class="language-sh">wrangler d1 create new-database --location=weur&#10;</code></pre>
<h3 id="use-the-dashboard-1">Use the dashboard</h3>
<p>To provide a location hint when creating a database via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>D1 SQL Database</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create database</strong>.</li>
<li>Provide a database name and an optional <strong>Location</strong>.</li>
<li>Select <strong>Create</strong> to create your database.</li>
</ol>
<h3 id="available-location-hints">Available location hints</h3>
<p>D1 supports the following location hints:</p>
<table>
<thead>
<tr>
<th>Hint</th>
<th>Hint description</th>
</tr>
</thead>
<tbody>
<tr>
<td>wnam</td>
<td>Western North America</td>
</tr>
<tr>
<td>enam</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>weur</td>
<td>Western Europe</td>
</tr>
<tr>
<td>eeur</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>apac</td>
<td>Asia-Pacific</td>
</tr>
<tr>
<td>oc</td>
<td>Oceania</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7369.md")
</aside>
<h2 id="read-replica-locations">Read replica locations</h2>
<p>With read replication enabled, D1 creates and distributes read-only copies of the primary database instance around the world. This reduces the query latency for users located far away from the primary database instance.</p>
<p>When using D1 read replication, D1 automatically creates a read replica in <a href="/d1/configuration/data-location#available-location-hints">every available region</a>, including the region where the primary database instance is located.</p>
<p>If a jurisdiction is configured, read replicas are only created within the jurisdiction set on database creation.</p>
<p>Refer to <a href="/d1/best-practices/read-replication/">D1 read replication</a> for more information.</p>
