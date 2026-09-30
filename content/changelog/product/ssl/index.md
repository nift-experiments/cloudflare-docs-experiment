<h1 id="changelog">Changelog</h1>

<h2 id="certificate-transparency-monitoring-is-now-generally-available"><a href="/changelog/post/2026-08-13-ct-monitoring-ga/">Certificate Transparency Monitoring is now Generally Available</a></h2>
<p><em>2026-08-13</em></p>
<p>Certificate Transparency Monitoring is now <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">generally available</a> across all Cloudflare plans.</p>
<p>Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.</p>
<p>Learn more in the <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">launch blog post</a> or the <a href="/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">CT Monitoring docs</a>.</p>


<h2 id="faster-and-more-secure-tls-handshakes-to-your-origins-automatically"><a href="/changelog/post/2026-07-21-automatic-origin-key-exchange/">Faster and more secure TLS handshakes to your origins, automatically</a></h2>
<p><em>2026-07-21</em></p>
<p>Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first <code>ClientHello</code>, helping avoid a <code>HelloRetryRequest</code> and one extra network round trip.</p>
<p>Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum <code>X25519MLKEM768</code> hybrid key agreement.</p>
<p>To change this behavior, go to <strong>SSL/TLS</strong> &gt; <strong>Overview</strong> &gt; <strong>Origin connection &amp; post-quantum encryption</strong>. Turn off <strong>Automatic key exchange</strong> to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.</p>
<p><strong>Compliance requirements</strong> apply only to TLS 1.3 connections. The <strong>Post-quantum hybrid</strong> option requires hybrid post-quantum key agreements support on your origin server. The <strong>Federal Information Processing Standards (FIPS)</strong> option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.</p>
<p>For requirements, configuration options, and rollout details, refer to <a href="/ssl/origin-configuration/automatic-key-exchange/">Automatic key exchange to origins</a>.</p>


<h2 id="post-quantum-ml-dsa-certificates-for-authenticated-origin-pulls-and-custom-origin-trust-store"><a href="/changelog/post/2026-06-17-pqc-mldsa-aop-cots/">Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store</a></h2>
<p><em>2026-06-17</em></p>
<p>Cloudflare now accepts <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a> (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.</p>
<p>ML-DSA is supported in two origin-facing features:</p>
<ul>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.</li>
<li><a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</li>
</ul>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and setup guidance, and to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the current post-quantum deployment status across Cloudflare.</p>


<h2 id="manage-mtls-and-byo-ca-certificates-from-the-cloudflare-dashboard"><a href="/changelog/post/2026-04-07-mtls-byoca-dashboard/">Manage mTLS and BYO CA certificates from the Cloudflare dashboard</a></h2>
<p><em>2026-04-07</em></p>
<p>You can now manage mutual TLS (mTLS) and Bring Your Own Certificate Authority
(BYO CA) configurations directly from the Cloudflare dashboard — no API required.</p>
<p>Previously, these advanced workflows required the Cloudflare API. The following
are now available in the dashboard:</p>
<ul>
<li><strong>AOP certificate management</strong> — Upload and manage your own
certificate authorities for <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls (AOP)</a>
directly from the dashboard.</li>
<li><strong>BYO Client mTLS certificate management</strong> — Upload and manage your own CA
certificates for <a href="/ssl/client-certificates/byo-ca/">client mTLS enforcement</a>
without needing API access.</li>
<li><strong>CDN hostname to client mTLS certificate mapping</strong> — Associate client mTLS
certificates with specific hostnames directly from the dashboard.</li>
</ul>


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="increased-limits-for-cloudflare-for-saas-and-secrets-store-free-and-pay-as-you-go-plans"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<p><em>2025-05-27T11:00:00+00:00</em></p>
<p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>


<h2 id="cloudflare-secrets-store-now-available-in-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<p><em>2025-04-09</em></p>
<p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>


<h2 id="upload-a-certificate-bundle-with-an-rsa-and-ecdsa-certificate-per-custom-hostname"><a href="/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/">Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname</a></h2>
<p><em>2025-02-14</em></p>
<p>Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.</p>
<p>Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.</p>
<pre><code>curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;d &#x27;{&#10;    &quot;hostname&quot;: &quot;hostname&quot;,&#10;    &quot;ssl&quot;: {&#10;        &quot;custom_cert_bundle&quot;: [&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;RSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;RSA Key&quot;&#10;            },&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;ECDSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;ECDSA Key&quot;&#10;            }&#10;        ],&#10;        &quot;bundle_method&quot;: &quot;force&quot;,&#10;        &quot;wildcard&quot;: false,&#10;        &quot;settings&quot;: {&#10;            &quot;min_tls_version&quot;: &quot;1.0&quot;&#10;        }&#10;    }&#10;}’&#10;</code></pre>
<p>You can also:</p>
<ul>
<li>
<p><a href="/api/resources/custom_hostnames/methods/create/">Upload</a> an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/">Replace</a> the RSA or ECDSA certificate with a certificate of its same type.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/">Delete</a> the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).</p>
</li>
</ul>
<p>This feature is available for Business and Enterprise customers who have purchased custom certificates.</p>



