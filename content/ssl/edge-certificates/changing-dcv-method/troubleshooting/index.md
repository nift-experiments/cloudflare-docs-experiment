<p>If your certificate is stuck in <strong>Pending Validation</strong> or failing to issue, the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14101.md")
</div> may be unable to complete [domain control validation (DCV)](/ssl/edge-certificates/changing-dcv-method/dcv-flow/). This page helps you identify and resolve common DCV issues.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14100.md")
</aside>
<h2 id="quick-checklist">Quick checklist</h2>
<p>Use this checklist to identify common DCV issues:</p>
<ul>
<li>[ ] <a href="#blocked-validation-url">No rules blocking the validation URL</a> - WAF rules, IP access rules, or Under Attack mode can block the CA</li>
<li>[ ] <a href="#redirection">No redirects on the validation path</a> - The <code>/.well-known/*</code> path must not redirect (especially HTTP to HTTPS in partial setups)</li>
<li>[ ] <a href="#dns-settings-and-records">DNS records are resolvable</a> - DNSSEC must be valid, and records must resolve from all locations</li>
<li>[ ] <a href="#caa-records">CAA records allow the CA</a> - CAA records must permit Cloudflare's partner CAs to issue certificates</li>
<li>[ ] <a href="#ca-errors">No CA-side errors</a> - Rate limits, policy blocks, or temporary CA issues</li>
</ul>
<hr />
<h2 id="blocked-validation-url">Blocked validation URL</h2>
<p>If you have issues while HTTP DCV is in place, review the following settings:</p>
<ul>
<li>
<p><strong>Anything affecting <code>/.well-known/*</code></strong>: Review <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/waf/tools/ip-access-rules/">IP Access Rules</a>, and other <a href="/rules/configuration-rules/">configuration rules</a> to make sure that your rules <em>do not</em> enable interactive challenge on the validation URL.</p>
</li>
<li>
<p><strong>Workers routes</strong>: If you have <a href="/workers/configuration/routing/routes/">Workers routes</a> matching <code>*/*</code> or paths that include <code>/.well-known/pki-validation/*</code> or <code>/.well-known/acme-challenge/*</code>, your Worker may intercept DCV requests from the certificate authority. Make sure your Worker either passes through requests to these paths or does not match them. This is especially relevant for <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> zones that use a <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/">Worker as the fallback origin</a>.</p>
</li>
<li>
<p><strong>Cloudflare Account Settings</strong> and <strong>Page Rules</strong>: Review your <a href="/fundamentals/reference/under-attack-mode/">account settings</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, and <a href="/rules/page-rules/">Page Rules</a> to ensure you have not enabled Under Attack mode on the validation URL.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14099.md")
</aside>
<h2 id="redirection">Redirection</h2>
<p>Enabling <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> does not impact the validation process.</p>
<p>In a <a href="/ssl/edge-certificates/changing-dcv-method/#partial-dns-setup---action-sometimes-required">Partial (CNAME) setup</a> where you are managing the token on the origin side, please ensure that no redirection from HTTP to HTTPS occurs on the <code>/.well-known/*</code> path.</p>
<p>When using <a href="/rules/url-forwarding/single-redirects/">Redirect Rules</a>, exclude the <code>/.well-known/*</code> path from redirections by adding a condition to your rule:</p>
<pre><code class="language-txt">not starts_with(http.request.uri.path, &quot;/.well-known/&quot;)&#10;</code></pre>
<p>For example, if you have a rule that redirects all HTTP traffic to HTTPS, modify the rule expression to:</p>
<pre><code class="language-txt">(http.request.scheme eq &quot;http&quot;) and not starts_with(http.request.uri.path, &quot;/.well-known/&quot;)&#10;</code></pre>
<h2 id="dns-settings-and-records">DNS settings and records</h2>
<p>The errors below refer to situations that have to be addressed at the authoritative DNS provider:</p>
<ul>
<li><code>the Certificate Authority had trouble performing a DNS lookup: dns problem: looking up caa for &lt;hostname&gt;: dnssec: bogus</code></li>
<li><code>Certificate authority encountered a SERVFAIL during DNS lookup, please check your DNS reachability.</code></li>
</ul>
<p>Consider the following when troubleshooting:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-security/">DNSSEC</a> must be configured correctly. You can use <a href="https://dnsviz.net/">DNSViz</a> to understand and troubleshoot the deployment of DNSSEC.</li>
<li>The HTTP verification process is done preferably over <strong>IPv6</strong>, so if any AAAA record exists and does not point to the same dual-stack location as the A record, the validation will fail.</li>
<li>If an <a href="/dns/manage-dns-records/reference/dns-record-types/#ns">NS record</a> is present for the hostname or its parent, DNS resolution will be managed externally by the DNS provider defined in the NS target. In this case, you must either add the DCV TXT record at the external DNS provider, or remove the NS record at Cloudflare.</li>
</ul>
<h3 id="caa-records">CAA records</h3>
<ul>
<li>Your <a href="/ssl/edge-certificates/caa-records/">CAA records</a> must be resolvable from all locations.</li>
<li>Your <a href="/ssl/edge-certificates/caa-records/">CAA records</a> should allow Cloudflare's partner <a href="/ssl/reference/certificate-authorities/">certificate authorities (CAs)</a> to issue certificates on your behalf.</li>
<li>If you are using a <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a> (<code>subdomain.example.com</code>) and Cloudflare is not the authoritative DNS provider for the parent domain (<code>example.com</code>), you should make sure that the parent domain (<code>example.com</code>) either has CAA records that allow <a href="/ssl/reference/certificate-authorities/">Cloudflare's partner CAs</a>, or has no CAA records at all.</li>
</ul>
<p>You can check the CAA records by running the following command:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14104.md")
</div></div>
<h2 id="certificate-authority-ca-errors">Certificate authority (CA) errors</h2>
<p>A <a href="/ssl/reference/certificate-authorities/">certificate authority (CA)</a> is the organization that issues your SSL/TLS certificate. Cloudflare partners with multiple CAs to provide certificates for your domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14098.md")
</aside>
<h3 id="rate-limiting">Rate limiting</h3>
<p>As mentioned in <a href="/ssl/reference/certificate-authorities/">Certificate authorities</a>, specific CAs may have their own limitations. If you use Let’s Encrypt and receive the error below, it means you hit the <a href="https://letsencrypt.org/docs/duplicate-certificate-limit/">duplicate certificate limit</a> imposed by Let's Encrypt.</p>
<p><code>The authority has rate limited these domains. Please wait for the rate limit to expire or try another authority.</code></p>
<p>A certificate is considered a duplicate of an earlier certificate if it contains the exact same set of hostnames.</p>
<p>In this case, you can either wait for the rate limit window to end or choose a different certificate authority.</p>
<p>When you see <code>The authority has rate limited these domains. Please wait for the rate limit to expire or try another authority</code>, the certificate authority has temporarily blocked certificate issuance for your domain due to too many recent requests.</p>
<p>Rate limit windows vary by CA:</p>
<ul>
<li><strong>Let's Encrypt</strong>: 7 days for most rate limits (refer to <a href="https://letsencrypt.org/docs/rate-limits/">Let's Encrypt rate limits</a>)</li>
<li><strong>Google Trust Services</strong>: Varies by limit type (refer to <a href="https://pki.goog/faq/">Google Trust Services documentation</a>)</li>
</ul>
<p><strong>Resolution</strong>: Wait for the rate limit window to expire, or select a different CA.</p>
<h3 id="caa-records-block-issuance">CAA records block issuance</h3>
<p>The error <code>CAA records block issuance. Please remove all CAA records or add records for this authority</code> indicates that your domain's <a href="/ssl/edge-certificates/caa-records/">CAA records</a> do not allow the selected certificate authority to issue certificates.</p>
<p><strong>Resolution</strong>: Either remove all CAA records from your domain, or add CAA records that explicitly allow <a href="/ssl/reference/certificate-authorities/">Cloudflare's partner certificate authorities</a>.</p>
<h3 id="multiple-perspective-validation-errors">Multiple perspective validation errors</h3>
<p>Certificate authorities perform domain validation from multiple geographic locations to prevent certain attacks. You may encounter one of these errors:</p>
<ul>
<li><code>Certificate authority encountered a multiple perspective CAA check error, please ensure your DNS is configured to allow CAA queries from all geographic perspectives</code></li>
<li><code>Certificate authority was unable to verify domain ownership from multiple geographic locations (MPIC failure). Please ensure your DNS records are reachable from all geographic perspectives and try again.</code></li>
</ul>
<p><strong>Resolution</strong>: Ensure your DNS records (including CAA records) are consistently resolvable from all geographic locations. You can investigate resolution errors using the <a href="https://dig.ping.pe/">ping.pe tool</a>. For example, for a <a href="/ssl/reference/certificate-authorities/#google-trust-services">Google Trust Services</a> certificate, check: <code>&lt;hostname&gt;:CAA:8.8.8.8</code>.</p>
<p>Read more from certificate authority documentation: <a href="https://www.ssl.com/blogs/multi-perspective-issuance-corroboration-mpic-arrives/">SSL.com</a>, <a href="https://letsencrypt.org/2020/02/19/multi-perspective-validation">Let's Encrypt</a>, and <a href="https://pki.goog/faq/#faq-mpic">Google Trust Services</a>.</p>
<h3 id="dns-lookup-errors">DNS lookup errors</h3>
<p>The error <code>the Certificate Authority had trouble performing a DNS lookup</code> indicates that the CA could not resolve your domain's DNS records. Common causes include SERVFAIL responses, NXDOMAIN, or DNSSEC validation failures.</p>
<p><strong>Resolution</strong>: Verify that your DNS records are correctly configured and resolvable. Use tools like <a href="https://dnsviz.net/">DNSViz</a> to check for DNSSEC issues, and ensure your authoritative nameservers are responding correctly.</p>
<h3 id="rejected-identifier">Rejected identifier</h3>
<p>The error <code>The certificate authority will not issue for this domain. Please check your input or try another authority</code> means the CA has policies that prevent issuing certificates for your specific domain.</p>
<p><strong>Resolution</strong>: Verify that your domain name is correctly spelled and does not violate the CA's issuance policies. If the domain is valid, try selecting a different CA.</p>
<h3 id="internal-errors">Internal errors</h3>
<p>When you see <code>Internal error with Certificate Authority. Please check later</code>, the certificate authority encountered a temporary issue during validation.</p>
<p><strong>Resolution</strong>: Wait a few minutes and retry. If the issue persists, try selecting a different CA. Cloudflare will automatically retry validation according to the <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">validation backoff schedule</a>.</p>
