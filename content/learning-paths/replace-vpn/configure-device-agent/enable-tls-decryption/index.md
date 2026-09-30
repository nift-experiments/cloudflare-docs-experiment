<p><a href="https://www.cloudflare.com/learning/security/what-is-https-inspection/">TLS decryption</a> allows Cloudflare Gateway to inspect HTTPS requests to your private network applications.</p>
<h2 id="should-i-enable-tls-decryption">Should I enable TLS decryption?</h2>
<p>With TLS decryption turned on, you can apply advanced Gateway policies, such as:</p>
<ul>
<li>Filtering based on the complete URL and path of requests</li>
<li>Scanning for sensitive data with <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a></li>
<li>Starting a remote browser isolation session with <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a></li>
</ul>
<p>These features can increase the security posture of sensitive systems, but TLS decryption can also break your users' access to certain resources. For instance, if your internal applications use self-signed certificates, you will need to either configure a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policy or an <a href="/cloudflare-one/traffic-policies/http-policies/#untrusted-certificates">Untrusted certificate <em>Pass through</em></a> policy to allow users to connect. To learn more, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#inspection-limitations">TLS decryption limitations</a>.</p>
<p>With TLS decryption turned off, Gateway can only inspect and apply HTTP policies to unencrypted HTTP requests. However, you can still apply network policies to HTTPS traffic based on user identity, device posture, IP, resolved domain, SNI, and other attributes that support a Zero Trust security implementation. For more information, refer to <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>.</p>
<h2 id="enable-tls-decryption">Enable TLS decryption</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9943.md")
</div></div>
<p>Next, choose a <a href="#configure-user-side-certificates">user-side certificate</a> to use for inspection.</p>
<h2 id="configure-user-side-certificates">Configure user-side certificates</h2>
<p>When you enable TLS decryption, Gateway will decrypt all traffic sent over HTTPS, apply your HTTP policies, and then re-encrypt the request with a certificate on the user device. You can either <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">install the certificate provided by Cloudflare</a> (default option) or <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">upload a custom root certificate</a> to Cloudflare (Enterprise-only option).</p>
<h3 id="best-practices">Best practices</h3>
<p>Deploying the Cloudflare root certificate is the simplest way to get started with TLS decryption and is usually appropriate for testing or proof of concept conditions.</p>
<p>If you already have a certificate that you use for other inspection or trust purposes, we recommend uploading your own root certificate for the following reasons:</p>
<ul>
<li>Using a single certificate streamlines IT management.</li>
<li>If other services (such as <code>git</code> workflows, other CLI tools, or thick client applications) rely on an existing certificate store, presenting the same certificate in inspection is far less likely to interrupt their traffic flow.</li>
<li>If you are using Cloudflare Mesh to connect devices to Cloudflare, those devices will not be able to leverage HTTP policies that require decrypting TLS unless they have a certificate that matches either your uploaded certificate or the Cloudflare root certificate. It is more likely that your network infrastructure already has your own device certificates deployed, so using the existing PKI infrastructure for inspection will reduce the number of steps needed to deploy Zero Trust.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mdm-deployments">MDM deployments</h3>
@markup("md", "content/.markup/bodies/9940.md")
</aside>
