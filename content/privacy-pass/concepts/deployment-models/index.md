<p>This page covers how a deployment of Privacy Pass is structured: who operates each of the four roles, detailed example deployment models, which deployment models work for different customer needs, and Privacy Pass as a part of other products.</p>
<hr />
<h2 id="who-operates-each-role">Who operates each role</h2>
<p>While Privacy Pass tokens offer cryptographic protection through blind signatures and large anonymity sets, roles must also be assigned with enough separation to ensure privacy guarantees. A typical Cloudflare deployment is structured like this:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Operated by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>The end user's software (browser, app, or device)</td>
</tr>
<tr>
<td>Origin</td>
<td>The website or application a user is attempting to reach; if run on Cloudflare Edge, Cloudflare acts as the Origin</td>
</tr>
<tr>
<td>Attester</td>
<td>The customer, although this is the role that varies the most depending on deployment</td>
</tr>
<tr>
<td>Issuer</td>
<td>Cloudflare, which operates a public, RFC 9578-compliant issuer</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11116.md")
</aside>
<p>Most importantly, this splits information about the Client so that no single role knows everything, also known as unlinkability. While different deployment models can change who exactly knows what, unlinkability guarantees that no one knows both who a Client is and where they are going. Generally, information is separated like this:</p>
<ul>
<li><strong>Attester</strong> — knows who the Client is and any identifiable information shared during the attestation phase, but not the Origin identity.</li>
<li><strong>Issuer</strong> — knows only that the Client was attested for and is owed a signed token. (This depends on the deployment: if the Attester and Issuer are the same entity, the Issuer may learn identity information, but the Origin identity stays hidden.)</li>
<li><strong>Origin</strong> — knows only that the Client is verified.</li>
</ul>
<p>It is important to note that the unlinkability between token issuance and redemption provided by Privacy Pass only partially relies on the separation of roles. To provide meaningful privacy, the anonymity set–e.g., the group of clients that are part of the same deployment setup–must also be kept large. Anything that causes clients to see different setups splits them into smaller groups, shrinking anonymity.</p>
<p>For more information, see the Privacy Pass RFC's <a href="https://datatracker.ietf.org/doc/html/rfc9576#name-privacy-considerations">guidelines</a>.</p>
<hr />
<h2 id="example-deployment-models">Example deployment models</h2>
<p>The main structural choice is determining whether the Attester, Issuer, and Origin have overlap in their operating entities or are kept entirely separate. While a fully split model is the most secure, there are benefits to combining certain entities based on the use case. Other possible models include joint Attester-Issuer and joint Issuer-Origin, which don't break the privacy guarantees as long as <a href="https://datatracker.ietf.org/doc/html/rfc9576#name-deployment-models">additional guidelines</a> are followed.</p>
<h3 id="apple-s-private-access-token-pat-deployment">Apple's Private Access Token (PAT) deployment</h3>
<p><a href="https://developer.apple.com/videos/play/wwdc2022/10077/">Apple created PATs</a> to almost entirely bypass CAPTCHA challenges for their iOS 16+ users on Safari and participating apps and third-party browsers. In this deployment, Apple leverages their role as a hardware provider to allow them to attest to device legitimacy using signals such as valid Apple ID and device integrity checks instead of through a CAPTCHA. The role separation is structure like this:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Operated by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>The end user's iOS software</td>
</tr>
<tr>
<td>Origin</td>
<td>The website or application the user is attempting to reach</td>
</tr>
<tr>
<td>Attester</td>
<td>Apple; attesting that the user holds a device in good standing</td>
</tr>
<tr>
<td>Issuer</td>
<td>Cloudflare and Fastly</td>
</tr>
</tbody>
</table>
<p>This deployment uses a <strong>fully split</strong> model, meaning that all roles are operated by non-colluding entities. A split model is ideal for Apple because their job as a hardware/infrastructure provider naturally fits into an Attester role. However, this model can be less useful for customers who operate as the Origin since either a third party must be brought in to be the Attester, or roles must be consolidated between Cloudflare and the customer to ensure that all three are being operated.</p>
<h3 id="attribute-attestation-deployment">Attribute attestation deployment</h3>
<p>Application developers may want to ensure that users of their service are subscribers or exceed a certain age, without persistently storing that information alongside their account. In such use case, the role separation structure might look like this:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Operated by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>The end user's software</td>
</tr>
<tr>
<td>Origin</td>
<td>Example.com (or Example Application)</td>
</tr>
<tr>
<td>Attester</td>
<td>Cloudflare; operating an Attester built to customer specifications</td>
</tr>
<tr>
<td>Issuer</td>
<td>Cloudflare</td>
</tr>
</tbody>
</table>
<p>This deployment uses a <strong>joint Attester-Issuer model</strong>, where Cloudflare operates both the Issuer and Attester. If the customer is acting as the Origin, they should generally not operate the Attester as well, since that would create an Origin-Attester entity that knows both user identity and destination, making privacy significantly harder to guarantee. Having Cloudflare operate it jointly with the Issuer prevents having to introduce an entirely new third party, although is not necessary. The joint Attester-Issuer model is also useful if the roles are reversed, such that the customer is an identity authority (e.g., an enterprise IdP/SSO provider) who wants to offer private verification for their Origins.</p>
<hr />
<h2 id="privacy-pass-as-part-of-another-product">Privacy Pass as part of another product</h2>
<p>Privacy Pass also powers existing Cloudflare products. The most established example is <a href="/privacy-proxy/">Privacy Proxy</a>, used in single-hop (<a href="https://blog.cloudflare.com/cloudflare-now-powering-microsoft-edge-secure-network/">Microsoft Edge Secure Network</a>) and double-hop (<a href="https://blog.cloudflare.com/icloud-private-relay/">Apple Private Relay</a>) deployments, where Privacy Pass handles the initial authentication between the client and the proxy (or the first proxy, in double-hop). If your use case fits an existing product, that may be the simplest path. For the proxy-level architecture, see <a href="/privacy-proxy/concepts/deployment-models/">Privacy Proxy deployment models</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/privacy-pass/concepts/privacy-pass-protocol/">Privacy Pass Protocol</a></li>
<li><a href="/privacy-pass/production-deployment-testing/">Production Deployment Testing</a> — what deploying one of these models with Cloudflare looks like.</li>
<li><a href="https://developer.apple.com/videos/play/wwdc2022/10077/">Replace CAPTCHAs with Private Access Tokens (Apple WWDC22)</a> — Apple's overview of its Private Access Token deployment.</li>
</ul>
