<p>As a SaaS provider, you may want to configure and manage Cloudflare for SaaS <a href="/api/">via the API</a> rather than the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. Below are relevant API calls for creating, editing, and deleting custom hostnames, as well as monitoring, updating, and deleting fallback origins. Further details can be found in the <a href="/api/">Cloudflare API documentation</a>.</p>
<hr />
<h2 id="custom-hostnames">Custom hostnames</h2>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/custom_hostnames/methods/list/">List custom hostnames</a></td>
<td>Use the <code>page</code> parameter to pull additional pages. Add a <code>hostname</code> parameter to search for specific hostnames.</td>
</tr>
<tr>
<td><a href="/api/resources/custom_hostnames/methods/create/">Create custom hostname</a></td>
<td>In the <code>validation_records</code> object of the response, use the <code>txt_name</code> and <code>txt_record</code> listed to validate the custom hostname.</td>
</tr>
<tr>
<td><a href="/api/resources/custom_hostnames/methods/get/">Custom hostname details</a></td>
<td>Use this endpoint to check hostname activation and certificate status.</td>
</tr>
<tr>
<td><a href="/api/resources/custom_hostnames/methods/edit/">Edit custom hostname</a></td>
<td>When sent with an <code>ssl</code> object that matches the existing value, indicates that hostname should restart domain control validation (DCV).</td>
</tr>
<tr>
<td><a href="/api/resources/custom_hostnames/methods/delete/">Delete custom hostname</a></td>
<td>Also deletes any associated SSL/TLS certificates.</td>
</tr>
</tbody>
</table>
<h3 id="confirm-custom-hostname-readiness">Confirm custom hostname readiness</h3>
<p>To confirm that a custom hostname is fully configured, check both status fields in the <a href="/api/resources/custom_hostnames/methods/get/">Custom hostname details endpoint</a> response:</p>
<table>
<thead>
<tr>
<th>API field</th>
<th>What it means</th>
<th>Ready value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>result.status</code></td>
<td>Hostname activation status. This field shows whether Cloudflare has validated and activated the custom hostname.</td>
<td><code>active</code></td>
</tr>
<tr>
<td><code>result.ssl.status</code></td>
<td>Certificate status. This field shows whether the hostname's SSL/TLS certificate has completed issuance and deployment.</td>
<td><code>active</code></td>
</tr>
</tbody>
</table>
<p>Treat the custom hostname as ready for production HTTPS when <code>result.status</code> is <code>active</code>, <code>result.ssl.status</code> is <code>active</code>, and the customer's DNS points to your CNAME target or apex proxying target.</p>
<p>If <code>result.status</code> is <code>active</code> but <code>result.ssl.status</code> is not <code>active</code>, the hostname is active but its certificate has not completed issuance and deployment. A successful TLS handshake alone does not mean the custom hostname certificate has finished provisioning because Cloudflare may present another matching certificate for that hostname. For more information, refer to <a href="/ssl/reference/certificate-and-hostname-priority/">Certificate and hostname priority</a>.</p>
<p>When you use the <a href="/api/resources/custom_hostnames/methods/create/">Create custom hostname endpoint</a>, choose one <code>ssl.method</code> value: <code>http</code>, <code>txt</code>, or <code>email</code>. For non-wildcard custom hostnames, Cloudflare always attempts <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#non-wildcard-custom-hostnames">HTTP certificate validation</a> after the hostname points to your SaaS target, even if you selected <strong>TXT</strong> validation.</p>
<h2 id="fallback-origins">Fallback origins</h2>
<p>Our API includes the following endpoints related to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">fallback origin</a> of a custom hostname:</p>
<ul>
<li><a href="/api/resources/custom_hostnames/subresources/fallback_origin/methods/get/">Get fallback origin</a></li>
<li><a href="/api/resources/custom_hostnames/subresources/fallback_origin/methods/update/">Update fallback origin</a></li>
<li><a href="/api/resources/custom_hostnames/subresources/fallback_origin/methods/delete/">Remove fallback origin</a></li>
</ul>
