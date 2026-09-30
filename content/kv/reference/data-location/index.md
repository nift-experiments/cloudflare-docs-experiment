<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9496.md")
</aside>
<p>Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction.</p>
<h2 id="automatic-default">Automatic (default)</h2>
<p>By default, data written to a Workers KV namespace is replicated globally across Cloudflare's network with no jurisdictional restriction, allowing your data to be read with low latency from anywhere in the world.</p>
<h2 id="restrict-a-namespace-to-a-jurisdiction">Restrict a namespace to a jurisdiction</h2>
<p>Jurisdictions are used to create Workers KV namespaces that only durably store data within a region, to help comply with data locality regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</p>
<p>Workers may still access a namespace constrained to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction location on Cloudflare's network. The jurisdiction constraint only controls where the namespace's data is durably stored. Consider using <a href="/data-localization/regional-services/">Regional Services</a> to control the regions from which Cloudflare responds to requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9495.md")
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
<tr>
<td>us</td>
<td>The United States of America</td>
</tr>
</tbody>
</table>
<h3 id="get-access">Get access</h3>
<p>Workers KV jurisdictions are in private beta. If you are interested in restricting your namespaces to a supported jurisdiction, contact your Cloudflare account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to request access.</p>
