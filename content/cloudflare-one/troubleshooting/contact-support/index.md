<p>If you cannot resolve an issue using our troubleshooting guides, you can <a href="/support/contacting-cloudflare-support/">open a support case</a>.</p>
<p>To help us investigate your issue quickly, please collect and provide the following information when you contact Cloudflare Support.</p>
<h2 id="1-gather-general-information"><ol>
<li>Gather general information</li>
</ol></h2>
<p>For all issues, please include:</p>
<ul>
<li><strong>Timestamp (UTC)</strong>: The exact time the issue occurred.</li>
<li><strong>Detailed description</strong>: A clear description of the problem and the steps to reproduce it.</li>
<li><strong>Actual vs. Expected</strong>: What happened versus what you expected to happen.</li>
<li><strong>Problem frequency</strong>: How often does the issue occur?</li>
<li><strong>Screenshots</strong>: Any relevant screenshots or videos of the error.</li>
<li><strong>Example URLs</strong>: Specific URLs where the issue is occurring.</li>
</ul>
<h2 id="2-collect-product-diagnostics"><ol start="2">
<li>Collect product diagnostics</li>
</ol></h2>
<p>Depending on the product, providing diagnostic files is critical for a technical investigation.</p>
<h3 id="cloudflare-one-client-warp">Cloudflare One Client (WARP)</h3>
If the issue involves the Cloudflare One Client, run the `warp-diag` command on the affected device and attach the resulting `.zip` file to your case. For more information, refer to [Diagnostic logs](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/).
<h3 id="cloudflare-tunnel">Cloudflare Tunnel</h3>
If the issue involves Cloudflare Tunnel, run the `cloudflared tunnel diag` command and provide the generated report. For more information, refer to [Tunnel diagnostic logs](/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).
<h3 id="access-and-gateway">Access and Gateway</h3>
For issues related to authentication loops, blocked websites, or policy enforcement:
<ul>
<li><strong>HAR file</strong>: Provide a <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR file</a> captured while reproducing the issue.</li>
<li><strong>Ray ID</strong>: If you see a Cloudflare error page, provide the <strong>Ray ID</strong> displayed at the bottom of the page.</li>
<li><strong>Identity Provider logs</strong>: Relevant logs from your identity provider (IdP) if the issue involves login failures.</li>
<li><strong>Request ID</strong>: For Gateway issues, you can find the <code>request_id</code> (HTTP logs) or <code>query_id</code> (DNS logs) in your <a href="/cloudflare-one/traffic-policies/troubleshooting/">Gateway logs</a>.</li>
</ul>
<h3 id="digital-experience-monitoring-dex">Digital Experience Monitoring (DEX)</h3>
For issues with DEX tests or device monitoring, provide a [remote capture](/cloudflare-one/insights/dex/diagnostics/client-packet-capture/) from the Zero Trust dashboard.
<hr />
<p>For more information, refer to <a href="/support/contacting-cloudflare-support/">Contacting Cloudflare Support</a>.</p>
