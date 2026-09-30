<p>This page provides information about some of the different types of DNS records that you can manage on Cloudflare. For guidance on how to add, edit, or delete DNS records, refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7799.md")
</aside>
<hr />
<h2 id="ip-address-resolution">IP address resolution</h2>
<p>At least one <strong>IP address resolution</strong> record is required for each domain on Cloudflare. These records are the only ones you can <a href="/dns/proxy-status/">proxy</a> through Cloudflare.</p>
<h3 id="a-and-aaaa">A and AAAA</h3>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/">A and AAAA records</a> map a domain name to one or multiple IPv4 or IPv6 address(es).</p>
<p>These records include the following fields:</p>
<ul>
<li>
<p><strong>Name</strong>: A subdomain or the zone apex (<code>@</code>).</p>
<ul>
<li>The name must be composed of labels of 63 characters or less (<code>label1.label2.label3</code>), where the fully qualified domain name (<code>label1.label2.label3.example.com</code>) does not exceed 253 characters.</li>
<li>DNS labels can contain any octet (byte value). However, for compatibility with hostnames and TLS certificates, it is recommended to use only letters, digits, and hyphens (LDH rule). This is not a DNS protocol requirement, meaning DNS will work even if you do not follow these conventions.</li>
<li>There is no requirement to start with a letter or end with a letter or digit.</li>
<li>Underscores are valid in DNS and commonly used for service records.</li>
</ul>
</li>
<li>
<p><strong>IPv4/IPv6 address</strong>: Your origin server address (cannot be a <a href="https://www.cloudflare.com/ips">Cloudflare IP</a>)</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7798.md")
</aside>
<ul>
<li><strong>TTL</strong>: Time to live, which controls how long DNS resolvers should cache a response before revalidating it.
<ul>
<li>If the <strong>Proxy Status</strong> is <strong>Proxied</strong>, this value defaults to <strong>Auto</strong>, which is 300 seconds.</li>
<li>If the <strong>Proxy Status</strong> is <strong>DNS Only</strong>, you can customize the value.</li>
</ul>
</li>
<li><strong>Proxy status</strong>: For more details, refer to <a href="/dns/proxy-status/">Proxied DNS records</a>.</li>
<li><strong>Private network routing</strong>: Some Enterprise customers also have access to <a href="/dns/private-origins/private-network-routing/">private network routing</a>. For <code>A</code> and <code>AAAA</code> records, this feature allows you to proxy HTTP/HTTPS traffic from public hostnames to origins in your private network.</li>
</ul>
<h4 id="example-api-call">Example API call</h4>
<p>When creating A or AAAA records <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">using the API</a>:</p>
<ul>
<li>The <code>content</code> of the records is an IP address (IPv4 for A or IPv6 for AAAA).</li>
<li>The <code>proxied</code> field affects the record's <a href="/dns/proxy-status/">proxy status</a>.</li>
</ul>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;A&quot;,&#10;  &quot;name&quot;: &quot;www.example.com&quot;,&#10;  &quot;content&quot;: &quot;192.0.2.1&quot;,&#10;  &quot;ttl&quot;: 3600,&#10;  &quot;proxied&quot;: false&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;A&quot;,&#10;		&quot;content&quot;: &quot;192.0.2.1&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="cname">CNAME</h3>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/">CNAME records</a> map a domain name to another (canonical) domain name. They can be used to resolve other record types present on the target domain name.</p>
<p>These records include the following fields:</p>
<ul>
<li><strong>Name</strong>: A subdomain or the zone apex (<code>@</code>).
<ul>
<li>The name must be composed of labels of 63 characters or less (<code>label1.label2.label3</code>), where the fully qualified domain name (<code>label1.label2.label3.example.com</code>) does not exceed 253 characters.</li>
<li>DNS labels can contain any octet (byte value). However, for compatibility with hostnames and TLS certificates, it is recommended to use only letters, digits, and hyphens (LDH rule). This is not a DNS protocol requirement, meaning DNS will work even if you do not follow these conventions.</li>
<li>There is no requirement to start with a letter or end with a letter or digit.</li>
<li>Underscores are valid in DNS and commonly used for service records.</li>
</ul>
</li>
<li><strong>Target</strong>: The hostname
where traffic should be directed (<code>example.com</code>). - <strong>TTL</strong>: Time to live, which
controls how long DNS resolvers should cache a response before revalidating it.</li>
<li>If the <strong>Proxy Status</strong> is <strong>Proxied</strong>, this value defaults to <strong>Auto</strong>, which
is 300 seconds. - If the <strong>Proxy Status</strong> is <strong>DNS Only</strong>, you can customize the
value. - <strong>Proxy status</strong>: For more details, refer to <a href="/dns/proxy-status/">Proxied DNS
records</a>.</li>
</ul>
<h4 id="proxied-cname-records">Proxied CNAME records</h4>
<p>Observe the following aspects, especially before changing a CNAME record from <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7800.md")
</div> to DNS-only or vice versa:
<ul>
<li>If a hostname is meant to proxy traffic, you can use CNAME records to point to other CNAME records (<code>www.example2.com</code> --&gt; <code>www.example1.com</code> --&gt; <code>www.example.com</code>), but the final record must point to a hostname with a valid IP address (and therefore a valid A or AAAA record). Also, queries for other record types on the same name are not supported.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7803.md")
</div></details>
<ul>
<li>
<p>Cloudflare uses a process called CNAME flattening to deliver better performance. This process supports a few features and can interact with <a href="/dns/cname-flattening/#aspects-to-keep-in-mind">different setups that depend on CNAME records</a>. Refer to the <a href="/dns/cname-flattening/">CNAME flattening section</a> to learn more about this.</p>
</li>
<li>
<p>If you encounter a CNAME record that you cannot proxy — usually associated with another CDN provider — a proxied version of that record will cause connectivity errors. Cloudflare is purposely preventing that record from being proxied to protect you from a misconfiguration. Refer to <a href="/dns/proxy-status/limitations/#proxy-eligibility">proxying limitations</a> for details.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7797.md")
</aside>
<h4 id="example-api-call-1">Example API call</h4>
<p>When creating CNAME records <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">using the API</a>:</p>
<ul>
<li>The <code>content</code> of the records is a <a href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">fully qualified domain name</a>.</li>
<li>The <code>proxied</code> field affects the record's <a href="/dns/proxy-status/">proxy status</a>.</li>
</ul>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;CNAME&quot;,&#10;  &quot;name&quot;: &quot;www.example.com&quot;,&#10;  &quot;content&quot;: &quot;www.another-example.com&quot;,&#10;  &quot;ttl&quot;: 3600,&#10;  &quot;proxied&quot;: false&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;CNAME&quot;,&#10;		&quot;content&quot;: &quot;www.another-example.com&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<hr />
<h2 id="email-authentication">Email authentication</h2>
<p>These records are recommended regardless of whether your domain sends email messages. Creating <a href="https://blog.cloudflare.com/tackling-email-spoofing/">secure email records</a> can help protect your domain against email spoofing.</p>
<p>If your domain is not used to send email messages, learn more about creating recommended <a href="https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/">restrictive records</a>.</p>
<h3 id="mx">MX</h3>
<p>A mail exchange (MX) record is required to deliver email to a mail server.</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/">MX record syntax</a></li>
<li><a href="/dns/manage-dns-records/how-to/email-records/#send-and-receive-email">Create an MX record</a></li>
</ul>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="dkim">DKIM</h3>
<p>A DomainKeys Identified Mail (DKIM) record ensures email authenticity by cryptographically signing emails:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM record syntax</a></li>
<li><a href="/dmarc-management/security-records/#create-security-records">Create a DKIM record</a></li>
</ul>
<h3 id="spf">SPF</h3>
<p>A Sender Policy Framework (SPF) record lists authorized IP addresses and domains that can send email on behalf of your domain.</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">SPF record syntax</a></li>
<li><a href="/dmarc-management/security-records/#create-security-records">Create an SPF record</a></li>
</ul>
<h3 id="dmarc">DMARC</h3>
<p>A Domain-based Message Authentication Reporting and Conformance (DMARC) record helps generate aggregate reports about your email traffic and provide clear instructions for how email receivers should treat non-conforming emails.</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC record syntax</a></li>
<li><a href="/dmarc-management/security-records/#create-security-records">Create a DMARC record</a></li>
</ul>
<hr />
<h2 id="specialized-records">Specialized records</h2>
<h3 id="txt">TXT</h3>
<p>A <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/">text (TXT) record</a> lets you enter text into the DNS system.</p>
<p>As the content of TXT records consist of one or more text strings delimited by double quotes (<code>&quot;</code>), you might find a validation error if you add inconsistent quotation marks (for example, <code>&quot;this</code> or <code>&quot;these&quot; ones&quot;</code>). For new records, if you save your TXT content without any quotes, Cloudflare will automatically add double quotes. For details, refer to <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/">What is a DNS TXT record</a>.</p>
<p>At Cloudflare, TXT records are most commonly used to demonstrate domain ownership prior to issuing SSL/TLS certificates for <a href="/ssl/edge-certificates/changing-dcv-method/">your domain</a> or a <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">Cloudflare for SaaS domain</a>.</p>
<p>You could also use TXT to create email authentication records, but we recommend that you use our <a href="/dns/manage-dns-records/how-to/email-records/#prevent-domain-spoofing">Email security Wizard</a> instead.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="caa">CAA</h3>
<p>A <a href="/ssl/edge-certificates/caa-records/">Certificate Authority Authorization (CAA) record</a> specifies which Certificate Authorities (CAs) are allowed to issue certificates for a domain.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="srv">SRV</h3>
<p>A <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/">service record (SRV)</a> specifies a host and port for specific services like voice over IP (VOIP), instant messaging, and more.</p>
<h4 id="example-api-call-2">Example API call</h4>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;SRV&quot;,&#10;  &quot;name&quot;: &quot;_xmpp._tcp.example.com&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;priority&quot;: 10,&#10;    &quot;weight&quot;: 5,&#10;    &quot;port&quot;: 5223,&#10;    &quot;target&quot;: &quot;server.example.com&quot;&#10;  }&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;_xmpp._tcp.example.com&quot;,&#10;		&quot;type&quot;: &quot;SRV&quot;,&#10;		&quot;content&quot;: &quot;5 5223 server.example.com&quot;,&#10;		&quot;priority&quot;: 10,&#10;		&quot;proxiable&quot;: false,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;data&quot;: {&#10;			&quot;port&quot;: 5223,&#10;			&quot;priority&quot;: 10,&#10;			&quot;target&quot;: &quot;server.example.com&quot;,&#10;			&quot;weight&quot;: 5&#10;		},&#10;		&quot;meta&quot;: {&#10;			&quot;auto_added&quot;: false,&#10;			&quot;managed_by_apps&quot;: false,&#10;			&quot;managed_by_argo_tunnel&quot;: false,&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2022-11-08T15:57:39.585977Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2022-11-08T15:57:39.585977Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="svcb-and-https">SVCB and HTTPS</h3>
<p>Service Binding (SVCB) and HTTPS Service (HTTPS) records allow you to provide a client with information about how it should connect to a server upfront, without the need of an initial plaintext HTTP connection.</p>
<p>If your domain has <a href="/speed/optimization/protocol/">HTTP/2 or HTTP/3 enabled</a>, <a href="/dns/proxy-status/">proxied DNS records</a>, and is also using <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a>, Cloudflare automatically generates HTTPS records on the fly, to advertise to clients how they should connect to your server.</p>
<h4 id="proxied-vs-dns-only-names">Proxied vs DNS-only names</h4>
For [proxied (orange cloud)](/dns/proxy-status/) names, Cloudflare synthesizes HTTPS records automatically when Universal SSL is enabled. Manually-added HTTPS records on proxied names are not served — Cloudflare uses the auto-generated records instead.
<p>If you have disabled Universal SSL (for example, because you use <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificates</a> exclusively), Cloudflare will not generate HTTPS records for proxied names.</p>
<p>For <a href="/dns/proxy-status/">DNS-only (grey cloud)</a> names, you can manually add HTTPS records and Cloudflare will serve them. However, <strong>all records with the same name must be DNS-only</strong> for the manual HTTPS record to be served.</p>
<details class="nb-details"><summary>Example: Manual HTTPS records and proxy status</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7806.md")
</div></details>
<p>For more details and context, refer to the <a href="https://blog.cloudflare.com/speeding-up-https-and-http-3-negotiation-with-dns/">announcement blog post</a> and <a href="https://www.rfc-editor.org/rfc/rfc9460.html">RFC 9460</a>.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="ptr">PTR</h3>
<p>A <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/">pointer (PTR) record</a> specifies the allowed hosts for a given IP address.</p>
<p>Within Cloudflare, PTR records are used for reverse DNS lookups and should preferably be added to <a href="/dns/additional-options/reverse-zones/">reverse zones</a>.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="soa">SOA</h3>
<p>A start of authority (SOA) record stores information about your domain such as admin email address, when the domain was last updated, and more. Refer to <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/">What is a DNS SOA record</a> for an example.</p>
<p>If you are using Cloudflare for your <a href="/dns/zone-setups/full-setup/">authoritative DNS</a>, you do not need to create an SOA record. Cloudflare creates this record automatically when you start using Cloudflare's authoritative nameservers.</p>
<p>With Enterprise accounts, you also have the option to change the SOA record values that Cloudflare will use:</p>
<ul>
<li>As a DNS zone default: Define the SOA record values that Cloudflare will use for all new zones added to your account. Refer to <a href="/dns/additional-options/dns-zone-defaults/">Configure DNS zone defaults</a> for step-by-step guidance.</li>
<li>For existing zones: Override the defaults or Cloudflare-generated values under <strong>DNS record options</strong> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</li>
</ul>
<p>Refer to the following list for information about each SOA record field:</p>
<details class="nb-details"><summary>SOA record fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7807.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7796.md")
</aside>
<h3 id="ns">NS</h3>
<p>A <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/">nameserver (NS) record</a> indicates which server should be used for authoritative DNS.</p>
<p>You only need to add NS records to your DNS records table in Cloudflare when you are using <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a> or <a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">delegating subdomains outside of Cloudflare</a>.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7795.md")
</aside>
<h4 id="limits">Limits</h4>
<p>When creating NS records, there are limits on the number of nameservers that can be associated with a single delegation name.</p>
<p>According to DNS standards defined in <a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>, a delegation should not include more than seven nameserver names for the same delegation name.</p>
<p>To align with these standards and maintain platform stability:</p>
<ul>
<li>Cloudflare supports up to 10 NS records per delegation name, but the best practice is to keep the set at seven or fewer.</li>
<li>Creating more than 10 NS records for the same name is not supported. Requests that exceed this limit may be rejected or fail validation.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7809.md")
</div></details>
<h3 id="ds-and-dnskey">DS and DNSKEY</h3>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/">DS and DNSKEY</a> records help implement DNSSEC, which cryptographically signs DNS records to prevent domain spoofing.</p>
<p>Most Cloudflare domains do not need to add these records and should instead follow our <a href="/dns/dnssec/">DNSSEC setup guide</a>.</p>
<p>For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">API documentation</a> (visible once you select the record type under the request body specification).</p>
<h3 id="other">Other</h3>
<p>Cloudflare also supports other record types that are less common, such as URI, NAPTR, and certificate-related record types (SSHFP, TLSA, SMIMEA, and CERT). Refer to our <a href="https://blog.cloudflare.com/additional-record-types-available-with-cloudflare-dns/">blog post</a> for more information.</p>
