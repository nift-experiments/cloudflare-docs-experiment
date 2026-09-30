<h2 id="resolve-a-timed-out-state">Resolve a timed out state</h2>
<p>If a certificate issuance times out, Cloudflare tells you where in the chain of issuance the timeout occurred: Initializing, Validation, Issuance, Deployment, or Deletion.</p>
<p>To resolve timeout issues, try one or more of the following options:</p>
<ul>
<li>Change the <strong>Proxy status</strong> of related DNS records to <strong>DNS only</strong> (gray-clouded) and wait at least a minute. Then, change the <strong>Proxy status</strong> back to <strong>Proxied</strong> (orange-clouded).</li>
<li><a href="/ssl/edge-certificates/universal-ssl/disable-universal-ssl/">Disable Universal SSL</a> and wait at least a minute. Then, re-enable Universal SSL.</li>
<li>Send a PATCH request to the <a href="/api/resources/ssl/subresources/verification/methods/edit/">validation endpoint</a> using the same <a href="/ssl/edge-certificates/changing-dcv-method/">DCV method</a> (API only). Make sure that the <code>--data</code> field is not empty in your request.</li>
<li>Review your domain control validation (DCV). Changing the DCV method will restart certificate issuance.</li>
</ul>
<h2 id="delete-certificates">Delete certificates</h2>
<p>You can <a href="/api/resources/ssl/subresources/certificate_packs/methods/delete/">use the API</a> to delete certificates that you no longer want listed on the Cloudflare dashboard.</p>
<h2 id="other-issues">Other issues</h2>
<p>For additional troubleshooting help, refer to <a href="/ssl/troubleshooting/">Troubleshooting SSL errors</a>.</p>
