<h2 id="vcpu-memory-and-disk">vCPU, Memory and Disk</h2>
<p>Containers are billed for every 10ms that they are actively running at the following rates, with included monthly usage as part of the $5 USD per month <a href="/workers/platform/pricing/">Workers Paid plan</a>:</p>
<table>
<thead>
<tr>
<th></th>
<th>Memory</th>
<th>CPU</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Free</strong></td>
<td>N/A</td>
<td>N/A</td>
<td></td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>25 GiB-hours/month included <br/> +$0.0000025 per additional GiB-second</td>
<td>375 vCPU-minutes/month <br/>+ $0.000020 per additional vCPU-second</td>
<td>200 GB-hours/month <br/> +$0.00000007 per additional GB-second</td>
</tr>
</tbody>
</table>
<p>You only pay for what you use — charges start when a request is sent to the container or when it is manually started. Charges stop after the container instance goes to sleep, which can happen automatically after a timeout. This makes it easy to scale to zero, and allows you to get high utilization even with bursty traffic.</p>
<p>Memory and disk usage are based on the <em>provisioned resources</em> for the instance type you select, while CPU usage is based on <em>active usage</em> only.</p>
<h4 id="instance-types">Instance Types</h4>
<p>When you deploy a container, you specify an <a href="/containers/platform/limits/#instance-types">instance type</a>.</p>
<p>The instance type you select will impact your bill — larger instances include more memory and disk, incurring additional costs, and higher CPU capacity, which allows you to incur higher CPU costs based on active usage.</p>
<p>The following instance types are currently available:</p>
<table>
<thead>
<tr>
<th>Instance Type</th>
<th>vCPU</th>
<th>Memory</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td>lite</td>
<td>1/16</td>
<td>256 MiB</td>
<td>2 GB</td>
</tr>
<tr>
<td>basic</td>
<td>1/4</td>
<td>1 GiB</td>
<td>4 GB</td>
</tr>
<tr>
<td>standard-1</td>
<td>1/2</td>
<td>4 GiB</td>
<td>8 GB</td>
</tr>
<tr>
<td>standard-2</td>
<td>1</td>
<td>6 GiB</td>
<td>12 GB</td>
</tr>
<tr>
<td>standard-3</td>
<td>2</td>
<td>8 GiB</td>
<td>16 GB</td>
</tr>
<tr>
<td>standard-4</td>
<td>4</td>
<td>12 GiB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<h2 id="network-egress">Network Egress</h2>
<p>Egress from Containers is priced at the following rates:</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Price per GB</th>
<th>Included Allotment per month</th>
</tr>
</thead>
<tbody>
<tr>
<td>North America &amp; Europe</td>
<td>$0.025</td>
<td>1 TB</td>
</tr>
<tr>
<td>Oceania, Korea, Taiwan</td>
<td>$0.05</td>
<td>500 GB</td>
</tr>
<tr>
<td>Everywhere Else</td>
<td>$0.04</td>
<td>500 GB</td>
</tr>
</tbody>
</table>
<h2 id="workers-and-durable-objects-pricing">Workers and Durable Objects Pricing</h2>
<p>When you use Containers, incoming requests to your containers are handled by your <a href="/workers/platform/pricing/">Worker</a>, and each container has its own
<a href="/durable-objects/platform/pricing/">Durable Object</a>. You are billed for your usage of both Workers and Durable Objects.</p>
<h2 id="logs-and-observability">Logs and Observability</h2>
<p>Containers are integrated with the <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> platform, and billed at the same rate. Refer to <a href="/workers/observability/logs/workers-logs/#pricing">Workers Logs pricing</a> for details.</p>
<p>When you <a href="/workers/observability/logs/workers-logs/#enable-workers-logs">enable observability for your Worker</a> with a binding to a container, logs from your container will show in both the Containers and Observability sections of the Cloudflare dashboard.</p>
