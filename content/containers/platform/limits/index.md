<h2 id="instance-types">Instance Types</h2>
<p>The memory, vCPU, and disk space for Containers are set through instance types. You can use one of six predefined instance types or configure a <a href="#custom-instance-types">custom instance type</a>.</p>
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
<p>These are specified using the <a href="/workers/wrangler/configuration/#containers"><code>instance_type</code> property</a> in your Worker's Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7090.md")
</aside>
<h3 id="custom-instance-types">Custom Instance Types</h3>
<p>In addition to the predefined instance types, you can configure custom instance types by specifying <code>vcpu</code>, <code>memory_mib</code>, and <code>disk_mb</code> values. See the <a href="/workers/wrangler/configuration/#custom-instance-types">Wrangler configuration documentation</a> for configuration details.</p>
<p>Custom instance types have the following constraints:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minimum vCPU</td>
<td>1</td>
</tr>
<tr>
<td>Maximum vCPU</td>
<td>4</td>
</tr>
<tr>
<td>Maximum Memory</td>
<td>12 GiB</td>
</tr>
<tr>
<td>Maximum Disk</td>
<td>20 GB</td>
</tr>
<tr>
<td>Memory to vCPU ratio</td>
<td>Minimum 3 GiB memory per vCPU</td>
</tr>
<tr>
<td>Disk to Memory ratio</td>
<td>Maximum 2 GB disk per 1 GiB memory</td>
</tr>
</tbody>
</table>
<p>For workloads requiring less than 1 vCPU, use the predefined instance types such as <code>lite</code> or <code>basic</code>.</p>
<p>If you need larger instance sizes or higher account-level limits, contact your account team, file a
support ticket, or fill out <a href="https://forms.gle/CscdaEGuw5Hb6H2s7">this form</a>.</p>
<h2 id="account-limits">Account limits</h2>
<p>The following limits apply per account:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent memory</td>
<td>6 TiB</td>
</tr>
<tr>
<td>Concurrent vCPU</td>
<td>1,500</td>
</tr>
<tr>
<td>Concurrent disk</td>
<td>30 TB</td>
</tr>
<tr>
<td>Image size</td>
<td>Same as <a href="#instance-types">instance disk space</a></td>
</tr>
<tr>
<td>Total image storage per account</td>
<td>50 GB <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Delete container images with `wrangler containers delete` to free up space. If you delete a container image and then [roll back](/workers/versions-and-deployments/rollbacks/) your Worker to a previous version, this version may no longer work.</li></ol></section>
