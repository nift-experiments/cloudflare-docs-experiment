<p>If you encounter issues <a href="/fundamentals/manage-domains/add-site/">adding a domain</a> to Cloudflare, follow these troubleshooting steps.</p>
<h2 id="disable-dnssec">Disable DNSSEC</h2>
<p>Cloudflare cannot provide authoritative DNS resolution for a domain — a <a href="/dns/zone-setups/full-setup/">domain on a primary setup (full)</a> — when <strong>DNSSEC</strong> is enabled at your domain registrar.</p>
<p>If you do not disable <strong>DNSSEC</strong> before changing your nameservers, you might experience the following issues:</p>
<ul>
<li>DNS does not resolve after switching to Cloudflare's nameservers.</li>
<li>DNS query response status is <code>SERVFAIL</code>.</li>
<li>The domain remains in a <a href="/dns/zone-setups/reference/domain-status/">Pending status</a>.</li>
</ul>
<p>If you experience these issues, refer to <a href="/dns/dnssec">Configuring DNSSEC</a> and <a href="/dns/dnssec/troubleshooting/">Troubleshooting DNSSEC</a>.</p>
<hr />
<h2 id="register-the-domain">Register the domain</h2>
<p>If the issue is with your registrar, you may receive the following error messages:</p>
<ul>
<li><code>exampledomain.com is not a registered domain (Code: 1049)</code></li>
<li><code>We were unable to identify bad.psl-example as a registered domain. Please ensure you are providing the root domain and not any subdomains (e.g., example.com, not subdomain.example.com) (Code: 1099)</code></li>
<li><code>Failed to lookup registrar and hosting information of exampledomain.com at this time. Please contact Cloudflare Support or try again later. (Code: 1110)</code></li>
</ul>
<p>If you receive these error messages, make sure that:</p>
<ul>
<li>You are providing the apex domain (also known as &quot;root domain&quot;, e.g. <code>example.com</code>) and not a subdomain (<code>www.example.com</code>).</li>
<li>Your domain is fully registered and its registration data lists its nameservers.</li>
<li>Your domain uses a verified <a href="https://publicsuffix.org/list/">top-level domain (TLD)</a>.</li>
</ul>
<hr />
<h2 id="resolve-dns-for-apex-domain">Resolve DNS for apex domain</h2>
<p>Before a domain can be added to Cloudflare, the domain must return <code>NS</code> records for valid, working nameservers. <code>NS</code> records can be checked via third-party online tools such as <a href="https://www.whatsmydns.net/">https://www.whatsmydns.net</a> or via a command-line terminal using a dig command:</p>
<pre><code class="language-sh">dig +short ns cloudflare.com&#10;</code></pre>
<pre><code class="language-sh">&#10;ns3.cloudflare.com.&#10;ns4.cloudflare.com.&#10;ns5.cloudflare.com.&#10;ns6.cloudflare.com.&#10;ns7.cloudflare.com.&#10;</code></pre>
<p>Additionally, the domain must return a valid <code>SOA</code> record when queried. <code>SOA</code> records can be checked via third-party online tools such as <a href="https://www.whatsmydns.net/">https://www.whatsmydns.net</a> or via a command-line terminal:</p>
<pre><code class="language-sh">dig +short soa cloudflare.com&#10;</code></pre>
<pre><code class="language-sh">&#10;ns3.cloudflare.com. dns.cloudflare.com. 2029202248 10000 2400 604800 300&#10;</code></pre>
<hr />
<h2 id="check-if-the-domain-is-restricted-at-cloudflare">Check if the domain is restricted at Cloudflare</h2>
<p>If Cloudflare has temporary or permanent restrictions on a domain, you will receive the following errors:</p>
<ul>
<li><strong>Error 1105</strong>
<ul>
<li><strong>Message</strong>: <code>Error with Cloudflare request: [1105] This zone is temporarily restricted and cannot be added to Cloudflare at this time, please contact Cloudflare Support.</code></li>
<li><strong>Cause</strong>: We have seen too many attempts to add a domain to Cloudflare</li>
<li><strong>Resolution</strong>: Wait 3 hours before attempting to re-add the domain to Cloudflare. Support cannot speed up this process.</li>
</ul>
</li>
<li><strong>Error 1093 or 1116</strong>
<ul>
<li><strong>Message</strong>: <code>This zone cannot be added to Cloudflare at this time, please contact Cloudflare Support. (Code: 1093)</code></li>
<li><strong>Cause</strong>: You may have entered a subdomain (<code>www.example.com</code>) instead of the apex domain (also known as &quot;root domain&quot;, e.g. <code>example.com</code>).</li>
<li><strong>Resolution</strong>: Verify that you are entering the apex domain. If you are and still experience issues, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</li>
</ul>
</li>
<li><strong>Error 1097</strong>
<ul>
<li><strong>Message</strong>: <code>This web property cannot be added to Cloudflare at this time. If you are an Enterprise customer, contact your account team. Otherwise, email abusereply@cloudflare.com with a detailed explanation of your association with this zone. (Code: 1097)</code></li>
<li><strong>Resolution</strong>: Contact <a href="mailto:abusereply@cloudflare.com">abusereply@cloudflare.com</a> with a detailed explanation of your association with this zone.</li>
</ul>
</li>
<li><strong>Error: Cannot be found</strong> OR <strong><code>&lt;your domain&gt;</code> is not a registered domain (code: 1049)</strong>
<ul>
<li>This can happen if the domain has not been registered yet. Some domains, like <code>.gov</code> domains, have special requirements that require the domain be added first.</li>
<li><strong>Resolution:</strong> Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> if you require assistance adding a <code>.gov</code> and/or other domains that require manual registration.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="contact-the-zone-owner-in-case-of-zone-hold-error">Contact the zone owner in case of zone hold error</h2>
<p>Enterprise customers can use the <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> feature to prevent domains to be added in any other account.
If you get the following error when adding your domain, it means that a zone hold is active:</p>
<pre><code>The zone name provided is subject to a hold which disallows the creation of this zone.&#10;Please contact the owner of the Cloudflare account that manages this domain to have this hold removed.&#10;</code></pre>
<p>In this case, you need to remove the zone hold if you own the Cloudflare account in which the zone is active, or contact the owner of the Cloudflare account that has the zone active.</p>
<p>If you are not the owner of the Cloudflare account that has the hold on the zone, using an online WHOIS tool might help you finding the owner of a website.</p>
<p>See this <a href="https://www.godaddy.com/whois">external WHOIS tool</a> or this <a href="https://www.whois.com/whois/">other external tool</a>.</p>
<p>The owner might be your hosting provider, or a SaaS service provider.</p>
<p>You can also use the <a href="https://dash.cloudflare.com/forgot-email">Cloudflare Forgot Email?</a> page, and check the documentation related to the <a href="/fundamentals/user-profiles/change-password-or-email/#forgot-your-email-address">Forgot Email? feature</a>.</p>
