<h2 id="error-1016-origin-dns-error">Error 1016: Origin DNS error</h2>
<p>This error indicates that Cloudflare cannot resolve the origin web server's IP address.</p>
<h3 id="common-cause">Common cause</h3>
<p>Common causes for error <code>1016</code> are:</p>
<ul>
<li>A missing DNS A record that mentions origin IP address.</li>
<li>A CNAME record in the Cloudflare DNS points to an unresolvable external domain.</li>
<li>The origin hostnames (CNAMEs) in your Cloudflare <a href="/load-balancing/">Load Balancer</a> default, region, and fallback pools are unresolvable. Use a fallback pool configured with an origin IP as a backup in case all other pools are unavailable.</li>
<li>When creating a Spectrum app with a CNAME origin, you need first to create a CNAME on the Cloudflare DNS side that points to the origin. Please see <a href="/spectrum/get-started/#create-a-spectrum-application-using-a-cname-record">Spectrum CNAME origins</a> for more details.</li>
<li>There is no DNS record for the hostname in the target <a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup zone</a> of a Workers subrequest (<a href="/workers/runtime-apis/fetch/">Fetch API</a>).</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>To resolve error <code>1016</code>:</p>
<ol>
<li>Verify your Cloudflare DNS settings include an A record that points to a valid IP address that resolves via a <a href="https://dnschecker.org/">DNS lookup tool</a>.</li>
<li>For a CNAME record pointing to a different domain, ensure that the target domain resolves via a <a href="https://dnschecker.org/">DNS lookup tool</a>.</li>
<li>For a Workers subrequest to a Partial (CNAME) setup zone, ensure that the hostname exists on the Cloudflare zone (and not only at the authoritative DNS).</li>
</ol>
<h2 id="error-1016-in-the-context-of-ssl-for-saas">Error 1016 in the context of SSL for SaaS</h2>
<p>Cloudflare returns a <code>1016</code> error when the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/">custom hostname</a> cannot be routed or proxied.</p>
<h3 id="common-cause-1">Common cause</h3>
<ul>
<li>Custom hostname ownership validation is not complete.</li>
<li>Fallback origin is not <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">correctly set</a>.</li>
<li>A wildcard custom hostname has been created, but the requested hostname is associated with a domain that exists in Cloudflare as a standalone zone.</li>
<li>There is no DNS record for the hostname in the Cloudflare for SaaS target zone.</li>
</ul>
<h3 id="resolution-1">Resolution</h3>
<ol>
<li>To check validation status, run an API call to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/">search for a certificate by hostname</a> and check the verification error field: <code>&quot;verification_errors&quot;: [&quot;custom hostname does not CNAME to this zone.&quot;]</code>. The error will be resolved once the status is <code>active</code>.</li>
<li>Confirm that you have created a DNS record for the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">fallback origin</a> and also set the fallback origin.</li>
<li>The <a href="/ssl/reference/certificate-and-hostname-priority/#hostname-priority">hostname priority</a> for the standalone zone will take precedence over the wildcard custom hostname. This behavior applies even if there is no DNS record for this standalone zone hostname. Use a specific hostname instead of a wildcard or <a href="/fundamentals/manage-domains/remove-domain/">remove the standalone zone from Cloudflare</a>.</li>
<li>Make sure that each hostname that needs to be served by the Cloudflare for SaaS parent zone has been added as an individual custom hostname and has the status <code>active</code>.</li>
</ol>
<h2 id="workers">Workers</h2>
<p>If you encounter this error with a Worker, you might be using the <a href="/workers/platform/known-issues/#fetch-api-in-cname-setup">Fetch API in a partial zone setup</a>.</p>
