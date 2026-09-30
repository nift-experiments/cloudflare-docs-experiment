<p>Secure Web Gateway allows you to inspect HTTP traffic and control which websites users can visit. DNS filtering can only block or allow entire domains (for example, all of <code>dropbox.com</code>). HTTP filtering goes deeper — it inspects full URLs and request content, so you can block a specific page like <code>dropbox.com/shared-folder</code>, scan file uploads for sensitive data, or enforce acceptable use policies based on what users are actually doing on a site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6603.md")
</aside>
<h2 id="1-connect-to-gateway"><ol>
<li>Connect to Gateway</li>
</ol></h2>
<p>HTTP filtering requires three components working together: the Cloudflare One Client routes device traffic through Cloudflare, a root certificate lets Gateway decrypt HTTPS traffic so it can inspect URLs and content, and the Gateway proxy enables Gateway to intercept and evaluate HTTP requests. Without the certificate, Gateway can only see the domain name — not the full URL or request body.</p>
<p>To filter HTTP requests from a device:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install the Cloudflare root certificate</a> on your device.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Install the Cloudflare One Client</a> on your device.</li>
<li>In the Cloudflare One Client Settings, log in to your organization's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/6604.md")
</div>.
4. [Enable the Gateway proxy](/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy) for TCP. Optionally, enable the UDP proxy to also inspect QUIC traffic on port 443 — this covers HTTP/3, a newer protocol some browsers use by default.
5. To inspect HTTPS traffic, [enable TLS decryption](/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption). TLS decryption allows Gateway to read encrypted requests. Without it, Gateway can see that a user visited `example.com` but not which specific page or what they uploaded.
6. (Optional) To scan file uploads and downloads for malware, [enable anti-virus scanning](/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/).
<h2 id="2-verify-device-connectivity"><ol start="2">
<li>Verify device connectivity</li>
</ol></h2>
<p>To verify your device is connected to Cloudflare One and traffic is flowing through Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Under <strong>Log traffic activity</strong>, enable activity logging for all HTTP logs.</li>
<li>On your device, open a browser and go to any website.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP</strong>.</li>
<li>Make sure HTTP requests from your device appear.</li>
</ol>
<p>After creating your first HTTP policy in the next step, you can test it by visiting a URL that your policy should block and confirming the request is denied.</p>
<h2 id="3-create-your-first-http-policy"><ol start="3">
<li>Create your first HTTP policy</li>
</ol></h2>
<p>An HTTP policy defines which requests to match (for example, uploads to file-sharing sites) and the action to take (for example, block).</p>
<p>To create a new HTTP policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6607.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
<h2 id="4-add-optional-policies"><ol start="4">
<li>Add optional policies</li>
</ol></h2>
<p>Refer to our list of <a href="/cloudflare-one/traffic-policies/http-policies/common-policies">common HTTP policies</a> for other policies you may want to create. Common additions include blocking file downloads by type, isolating risky websites in a <a href="/cloudflare-one/remote-browser-isolation/">remote browser</a>, and adding Do Not Inspect rules for applications that break under TLS decryption (for example, apps that use certificate pinning to enforce their own certificates). Do Not Inspect rules tell Gateway to skip decryption for specific destinations so those applications continue to work.</p>
