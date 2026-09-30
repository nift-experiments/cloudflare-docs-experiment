<p>This page details which R2 location or jurisdiction is recommended based on your Snowflake region.</p>
<p>You have the following inputs to control the physical location where objects in your R2 buckets are stored (for more information refer to <a href="/r2/reference/data-location/">data location</a>):</p>
<ul>
<li><a href="/r2/reference/data-location/#location-hints"><strong>Location hints</strong></a>: Specify a geophrical area (for example, Asia-Pacific or Western Europe). R2 makes a best effort to place your bucket in or near that location to optimize performance. You can confirm bucket placement after creation by navigating to the <strong>Settings</strong> tab of your bucket and referring to the <strong>Bucket details</strong> section.</li>
<li><a href="/r2/reference/data-location/#jurisdictional-restrictions"><strong>Jurisdictions</strong></a>: Enforce that data is both stored and processed within a specific jurisdiction (for example, US, EU, or FedRAMP environments). Use jurisdictions when you need to ensure data is stored and processed within a jurisdiction to meet data residency requirements, including local regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</li>
</ul>
<h2 id="north-and-south-america-commercial">North and South America (Commercial)</h2>
<table>
<thead>
<tr>
<th>Snowflake region name</th>
<th>Cloud</th>
<th>Region ID</th>
<th>Recommended R2 location</th>
</tr>
</thead>
<tbody>
<tr>
<td>Canada (Central)</td>
<td>AWS</td>
<td><code>ca-central-1</code></td>
<td>Location hint: <code>enam</code></td>
</tr>
<tr>
<td>South America (Sao Paulo)</td>
<td>AWS</td>
<td><code>sa-east-1</code></td>
<td>Location hint: <code>enam</code></td>
</tr>
<tr>
<td>US West (Oregon)</td>
<td>AWS</td>
<td><code>us-west-2</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>wnam</code></td>
</tr>
<tr>
<td>US East (Ohio)</td>
<td>AWS</td>
<td><code>us-east-2</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>US East (N. Virginia)</td>
<td>AWS</td>
<td><code>us-east-1</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>US Central1 (Iowa)</td>
<td>GCP</td>
<td><code>us-central1</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>US East4 (N. Virginia)</td>
<td>GCP</td>
<td><code>us-east4</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>Canada Central (Toronto)</td>
<td>Azure</td>
<td><code>canadacentral</code></td>
<td>Location hint: <code>enam</code></td>
</tr>
<tr>
<td>Central US (Iowa)</td>
<td>Azure</td>
<td><code>centralus</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>East US 2 (Virginia)</td>
<td>Azure</td>
<td><code>eastus2</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>Mexico Central (Mexico City)</td>
<td>Azure</td>
<td><code>mexicocentral</code></td>
<td>Location hint: <code>wnam</code></td>
</tr>
<tr>
<td>South Central US (Texas)</td>
<td>Azure</td>
<td><code>southcentralus</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>enam</code></td>
</tr>
<tr>
<td>West US 2 (Washington)</td>
<td>Azure</td>
<td><code>westus2</code></td>
<td>Jurisdiction: <code>us</code> or hint: <code>wnam</code></td>
</tr>
</tbody>
</table>
<h2 id="u-s-government">U.S. Government</h2>
<table>
<thead>
<tr>
<th>Snowflake region name</th>
<th>Cloud</th>
<th>Region ID</th>
<th>Recommended R2 location</th>
</tr>
</thead>
<tbody>
<tr>
<td>US Gov East 1</td>
<td>AWS</td>
<td><code>us-gov-east-1</code></td>
<td>Jurisdiction: <code>fedramp</code></td>
</tr>
<tr>
<td>US Gov West 1</td>
<td>AWS</td>
<td><code>us-gov-west-1</code></td>
<td>Jurisdiction: <code>fedramp</code></td>
</tr>
<tr>
<td>US Gov Virginia</td>
<td>Azure</td>
<td><code>usgovvirginia</code></td>
<td>Jurisdiction: <code>fedramp</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11547.md")
</aside>
<h2 id="europe-and-middle-east">Europe and Middle East</h2>
<table>
<thead>
<tr>
<th>Snowflake region name</th>
<th>Cloud</th>
<th>Region ID</th>
<th>Recommended R2 location</th>
</tr>
</thead>
<tbody>
<tr>
<td>EU (Frankfurt)</td>
<td>AWS</td>
<td><code>eu-central-1</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>EU (Zurich)</td>
<td>AWS</td>
<td><code>eu-central-2</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>EU (Stockholm)</td>
<td>AWS</td>
<td><code>eu-north-1</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>EU (Ireland)</td>
<td>AWS</td>
<td><code>eu-west-1</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Europe (London)</td>
<td>AWS</td>
<td><code>eu-west-2</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>EU (Paris)</td>
<td>AWS</td>
<td><code>eu-west-3</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Middle East Central2 (Dammam)</td>
<td>GCP</td>
<td><code>me-central2</code></td>
<td>Location hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Europe West2 (London)</td>
<td>GCP</td>
<td><code>europe-west-2</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Europe West3 (Frankfurt)</td>
<td>GCP</td>
<td><code>europe-west-3</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Europe West4 (Netherlands)</td>
<td>GCP</td>
<td><code>europe-west-4</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>North Europe (Ireland)</td>
<td>Azure</td>
<td><code>northeurope</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>Switzerland North (Zurich)</td>
<td>Azure</td>
<td><code>switzerlandnorth</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>West Europe (Netherlands)</td>
<td>Azure</td>
<td><code>westeurope</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>UAE North (Dubai)</td>
<td>Azure</td>
<td><code>uaenorth</code></td>
<td>Location hint: <code>weur</code>/<code>eeur</code></td>
</tr>
<tr>
<td>UK South (London)</td>
<td>Azure</td>
<td><code>uksouth</code></td>
<td>Jurisdiction: <code>eu</code> or hint: <code>weur</code>/<code>eeur</code></td>
</tr>
</tbody>
</table>
<h2 id="asia-pacific-and-china">Asia Pacific and China</h2>
<table>
<thead>
<tr>
<th>Snowflake region name</th>
<th>Cloud</th>
<th>Region ID</th>
<th>Recommended R2 location</th>
</tr>
</thead>
<tbody>
<tr>
<td>Asia Pacific (Tokyo)</td>
<td>AWS</td>
<td><code>ap-northeast-1</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Asia Pacific (Seoul)</td>
<td>AWS</td>
<td><code>ap-northeast-2</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Asia Pacific (Osaka)</td>
<td>AWS</td>
<td><code>ap-northeast-3</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Asia Pacific (Mumbai)</td>
<td>AWS</td>
<td><code>ap-south-1</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Asia Pacific (Singapore)</td>
<td>AWS</td>
<td><code>ap-southeast-1</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Asia Pacific (Sydney)</td>
<td>AWS</td>
<td><code>ap-southeast-2</code></td>
<td>Location hint: <code>oc</code></td>
</tr>
<tr>
<td>Asia Pacific (Jakarta)</td>
<td>AWS</td>
<td><code>ap-southeast-3</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>China (Ningxia)</td>
<td>AWS</td>
<td><code>cn-northwest-1</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Australia East (New South Wales)</td>
<td>Azure</td>
<td><code>australiaeast</code></td>
<td>Location hint: <code>oc</code></td>
</tr>
<tr>
<td>Central India (Pune)</td>
<td>Azure</td>
<td><code>centralindia</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Japan East (Tokyo)</td>
<td>Azure</td>
<td><code>japaneast</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
<tr>
<td>Southeast Asia (Singapore)</td>
<td>Azure</td>
<td><code>southeastasia</code></td>
<td>Location hint: <code>apac</code></td>
</tr>
</tbody>
</table>
