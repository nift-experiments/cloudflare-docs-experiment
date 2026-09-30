<p>Cloudflare Gateway can perform <a href="https://www.cloudflare.com/learning/security/what-is-https-inspection/">SSL/TLS decryption</a> to inspect HTTPS traffic for malware and other security risks. TLS decryption is required for HTTP policies to inspect HTTPS traffic. Without it, information contained within HTTPS encryption, such as the full URL, headers, and request body, <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">will not be visible to Gateway</a>.</p>
<p>When you turn on TLS decryption, Gateway will decrypt all traffic sent over HTTPS, apply your HTTP policies, and then re-encrypt the request with a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">user-side certificate</a>.</p>
<p>Cloudflare prevents traffic interference by decrypting, inspecting, and re-encrypting HTTPS requests in its data centers in memory only. Gateway only stores eligible cache content at rest. All cache disks are encrypted at rest. You can configure where TLS decryption takes place with <a href="/data-localization/regional-services/">Regional Services</a> in the <a href="/data-localization/">Cloudflare Data Localization Suite (DLS)</a>. To further control what data centers traffic egresses from, you can use <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>.</p>
<p>Cloudflare supports connections from users to Gateway over TLS 1.1, 1.2, and 1.3.</p>
<h2 id="turn-on-tls-decryption">Turn on TLS decryption</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisite">Prerequisite</h3>
@markup("md", "content/.markup/bodies/6474.md")
</aside>
<p>To turn on TLS decryption:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6477.md")
</div></div>
<h2 id="inspection-limitations">Inspection limitations</h2>
<p>Gateway does not support TLS decryption for applications which use:</p>
<ul>
<li><a href="#incompatible-certificates">Certificate pinning</a></li>
<li><a href="#incompatible-certificates">Self-signed certificates</a></li>
<li><a href="#incompatible-certificates">Mutual TLS (mTLS) authentication</a></li>
<li><a href="#esni-and-ech">ESNI and ECH handshake encryption</a></li>
<li><a href="#google-chrome-automatic-https-upgrades">Automatic HTTPS upgrades</a></li>
</ul>
<h3 id="inspect-on-all-ports">Inspect on all ports</h3>
<p>By default, Gateway will only inspect HTTP traffic through port <code>80</code>. Additionally, if you <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">turn on TLS decryption</a>, Gateway will inspect HTTPS traffic through port <code>443</code>.</p>
<p>To detect and inspect HTTP and HTTPS traffic on ports in addition to <code>80</code> and <code>443</code>, <p>you can turn on <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a> and configure Gateway to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect traffic on all ports</a></p>
.</p>
<h3 id="incompatible-certificates">Incompatible certificates</h3>
<p>Applications that use certificate pinning and mTLS authentication do not trust Cloudflare certificates. For example, most mobile applications use <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6478.md")
</div>. Cloudflare does not trust applications that use self-signed certificates instead of certificates signed by a public CA.
<p>If you try to perform TLS decryption on an application with an incompatible certificate configuration, the application may return an SSL or trust error and/or fail to load. To resolve this issue, you can:</p>
<ul>
<li>Add a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#add-the-certificate-to-applications">Cloudflare certificate</a> to supported applications.</li>
<li>Create a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect policy</a> to exempt applications from inspection. The <a href="/cloudflare-one/traffic-policies/http-policies/#application">Application selector</a> provides a list of trusted applications that are known to use embedded certificates. Note that if you create a Do Not Inspect policy for an application or website, you will lose the ability to log or block HTTP requests, apply DLP policies, and perform AV scanning.</li>
<li>Configure a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> in Include mode to ensure Gateway will only inspect traffic destined for your IPs or domains. This is useful for organizations that deploy Zero Trust on users' personal devices or otherwise expect personal applications to be used.</li>
</ul>
<p>Alternatively, to allow HTTP filtering while accessing a site with an insecure certificate, set your <a href="/cloudflare-one/traffic-policies/http-policies/#untrusted-certificates">Untrusted certificate action</a> to <em>Pass through</em>.</p>
<h3 id="google-chrome-automatic-https-upgrades">Google Chrome automatic HTTPS upgrades</h3>
<p>Google Chrome can automatically upgrade HTTP requests to HTTPS requests, even when you select a link that explicitly declares <code>http://</code>. When you use Gateway to proxy and filter your traffic, this upgrade can interrupt the connection between your Zero Trust users and Gateway.</p>
<p>You can turn off automatic HTTPS upgrades via a Gateway pass through policy, a Chrome browser flag, or a Chrome Enterprise policy.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6482.md")
</div></div>
<h3 id="mutual-tls-mtls">Mutual TLS (mTLS)</h3>
<p>In mutual TLS (mTLS), both the client and server present certificates to verify each other's identity. When Gateway decrypts TLS traffic, it terminates the connection from the client and creates a new connection to the origin server. Because Gateway cannot forward the client's certificate to the origin, the mTLS handshake fails. To prevent connection failures, create a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect policy</a> for this traffic.</p>
<h3 id="esni-and-ech">ESNI and ECH</h3>
<p>Websites that adhere to <a href="https://blog.cloudflare.com/encrypted-client-hello/">ESNI or Encrypted Client Hello (ECH) standards</a> encrypt the Server Name Indication (SNI) during the TLS handshake and are therefore incompatible with HTTP inspection. Gateway relies on the SNI to match an HTTP request to a policy — if the SNI is encrypted, Gateway cannot determine which policy to apply. If the ECH fails, browsers will retry the TLS handshake using the unencrypted SNI from the initial request. To avoid this behavior, you can disable ECH in your users' browsers.</p>
<p>You can still apply all <a href="/cloudflare-one/traffic-policies/network-policies/#selectors">network policy filters</a> except for SNI and SNI Domain. To restrict ESNI and ECH traffic, an option is to filter out all port <code>80</code> and <code>443</code> traffic that does not include an SNI header.</p>
<h2 id="post-quantum-support">Post-quantum support</h2>
<p>Gateway supports post-quantum cryptography using a hybrid key exchange with X25519 and MLKEM768 over TLS 1.3. Once the key exchange is complete, Gateway uses AES-128-GCM to encrypt traffic.</p>
<p>Refer to <a href="/ssl/post-quantum-cryptography/">Post-quantum cryptography</a> to learn more.</p>
<h2 id="fips-compliance">FIPS compliance</h2>
<p>By default, TLS decryption can use both TLS version 1.2 and 1.3. However, some environments such as FedRAMP may require cipher suites and TLS versions compliant with FIPS 140-3. FIPS compliance currently requires TLS version 1.2.</p>
<h3 id="enable-fips-compliance">Enable FIPS compliance</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6485.md")
</div></div>
<ol start="3">
<li>Select <strong>Enable only cipher suites and TLS versions compliant with FIPS 140-3</strong>.</li>
</ol>
<h3 id="limitations">Limitations</h3>
<p>When FIPS compliance is enabled, Gateway will only choose <a href="#cipher-suites">FIPS-compliant cipher suites</a> when connecting to the origin. If the origin does not support FIPS-compliant ciphers, the request will fail.</p>
<p>FIPS-compliant traffic defaults to <a href="/cloudflare-one/traffic-policies/http-policies/http3/">HTTP/3</a>. To enforce HTTP policies for UDP traffic, you must turn on the <a href="/cloudflare-one/traffic-policies/http-policies/http3/#enable-http3-inspection">Gateway proxy for UDP</a>.</p>
<h2 id="fedramp-compliance">FedRAMP compliance</h2>
<p>When you use <a href="/data-localization/regional-services/">Cloudflare Regional Services</a> in the United States and the Cloudflare One Client to on-ramp TLS traffic to Gateway, traffic will egress from a Cloudflare data center within Cloudflare's FedRAMP boundary. If a user's closest data center is non-FedRAMP compliant, their traffic will still egress from a FedRAMP compliant data center, maintaining FedRAMP compliance for the traffic.</p>
<pre><code class="language-mermaid">flowchart LR&#10; %% Accessibility&#10; accTitle: How Gateway routes FedRAMP compliant traffic with Regional Services&#10; accDescr: Flowchart describing how the Cloudflare One Client with Gateway routes traffic to egress from a FedRAMP compliant data center when used with Regional Services in the United States.&#10;&#10; %% Flowchart&#10; subgraph s1[&quot;Non-FedRAMP data center&quot;]&#10;        n2[&quot;WARP TLS encryption terminated&quot;]&#10;  end&#10; subgraph s2[&quot;FedRAMP data center&quot;]&#10;        n3[&quot;Gateway TLS encryption (FIPS) terminated&quot;]&#10;  end&#10; subgraph s3[&quot;Private internal network&quot;]&#10;        n5[&quot;FedRAMP compliant cloudflared&quot;]&#10;        n6([&quot;Private server&quot;])&#10;  end&#10;    n1([&quot;User near non-FedRAMP compliant data center&quot;]) -- Gateway TLS connection wrapped with WARP TLS (MASQUE) --&gt; n2&#10;    n2 -- Gateway TLS connection --&gt; n3&#10;    n3 &lt;-- FIPS tunnel --&gt; n5&#10;    n5 --&gt; n6&#10;&#10;    n5@{ shape: rect}&#10;</code></pre>
<h2 id="cipher-suites">Cipher suites</h2>
<div class="nb-glossary-definition"><p>A cipher suite is a set of encryption algorithms for establishing a secure communications connection. There are several cipher suites in wide use, and a client and server agree on the cipher suite to use when establishing the TLS connection. Support of multiple cipher suites allows compatibility across various clients.</p></div>
<p>The following table lists the default cipher suites Gateway uses for TLS decryption.</p>
<table>
<thead>
<tr>
<th>Name (OpenSSL)</th>
<th>Name (IANA)</th>
<th>FIPS-compliant</th>
</tr>
</thead>
<tbody>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-GCM-SHA384</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-GCM-SHA384</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA384</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384</td>
<td>✅</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>TLS_RSA_WITH_AES_128_GCM_SHA256</td>
<td>✅</td>
</tr>
<tr>
<td>AES256-GCM-SHA384</td>
<td>TLS_RSA_WITH_AES_256_GCM_SHA384</td>
<td>✅</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>TLS_RSA_WITH_AES_128_CBC_SHA</td>
<td>❌</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>TLS_RSA_WITH_AES_256_CBC_SHA</td>
<td>❌</td>
</tr>
</tbody>
</table>
<p>For more information on cipher suites, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">Cipher suites</a>.</p>
