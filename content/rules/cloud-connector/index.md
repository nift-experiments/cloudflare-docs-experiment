<p>Cloud Connector <div class="nb-data-component" data-cf-component="ProductAvailabilityText"></div> allows you to route matching incoming traffic from your website to a public cloud provider that you define: <a href="/r2/">Cloudflare R2</a> object storage or an external provider such as AWS, Google Cloud, Microsoft Azure, and Oracle Cloud. With Cloud Connector, you can manage traffic to cloud-hosted content through the same Cloudflare dashboard you use for the rest of your website, without having to configure additional rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13034.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>First, you configure a Cloud Connector rule that specifies:</p>
<ul>
<li>The cloud provider and a supported cloud service that will accept traffic.</li>
<li>The traffic that will be routed to that cloud service.</li>
</ul>
<p>Then, Cloudflare will create the <a href="#applied-configurations">necessary configurations</a> so that the content is accessible for requests matching your Cloud Connector rule. Your object storage bucket must be publicly accessible for Cloud Connector to work.</p>
<p>Cloud Connector rules are evaluated last in the <a href="/ruleset-engine/reference/phases-list/">request evaluation workflow</a>. When a Cloud Connector rule matches and other rules have modified the same settings (such as the <code>Host</code> header), the Cloud Connector rule takes precedence.</p>
<h2 id="applied-configurations">Applied configurations</h2>
<p>Cloud Connector will perform the following configurations automatically, depending on the cloud provider:</p>
<ul>
<li>Modify the <code>Host</code> header.</li>
<li>Adjust SSL/TLS for bucket-related traffic (<a href="/rules/cloud-connector/providers/#ssl-connections-to-aws-s3-endpoints">AWS S3 website endpoints</a> only).</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="additional-configurations-you-may-need">Additional configurations you may need</h3>
@markup("md", "content/.markup/bodies/13033.md")
</aside>
<h2 id="availability">Availability</h2>
<p>Cloud Connector is available in beta to all customers. The maximum number of rules depends on your Cloudflare plan:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
</tbody>
</table>
