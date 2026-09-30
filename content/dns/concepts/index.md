<p>The Domain Name System (DNS) translates human-readable domain names (like <code>example.com</code>) into IP addresses that computers use to locate each other on the Internet. This page covers key DNS concepts used throughout the Cloudflare DNS documentation. For more concepts and broader descriptions, refer to the <a href="https://www.cloudflare.com/learning/dns/what-is-dns/">Cloudflare Learning Center</a>.</p>
<h2 id="domain">Domain</h2>
<p>Also known as domain name, a domain is the string of text that identifies a specific website, such as <code>google.com</code> or <code>facebook.com</code>. Every time you access a website from your web browser, a DNS query (a lookup request to translate the domain into an address) takes place and the DNS service maps the domain to the actual IP address where the website is <a href="/fundamentals/manage-domains/">hosted</a>.</p>
<h2 id="registrar">Registrar</h2>
<p>Before you can start using the Cloudflare DNS service, you must first have a domain. You obtain a domain through a registrar, a service that handles the reservation of domain names as explained in the <a href="https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/">Learning Center</a>.</p>
<p>Very often the same company that offers domain registration also offers web hosting and DNS management.</p>
<p>You can register a domain name at cost (without markup fees) through <a href="/registrar/">Cloudflare Registrar</a>. Every domain acquired through Cloudflare Registrar must also use Cloudflare as their <a href="#authoritative-dns">primary authoritative DNS</a>.</p>
<h2 id="nameserver">Nameserver</h2>
<p>DNS resolution — the process of translating a domain name into an IP address — involves several types of servers. In this documentation, nameserver usually refers to the Cloudflare authoritative nameservers, the servers that hold the definitive DNS records for your domain and provide the final answer in DNS resolution. For more context on the different server types involved, refer to the <a href="https://www.cloudflare.com/learning/dns/dns-server-types/">article about DNS server types</a>.</p>
<p>Refer to <a href="/dns/nameservers/">Nameservers</a> for details on the different nameserver offerings.</p>
<h2 id="authoritative-dns">Authoritative DNS</h2>
<p>Authoritative DNS refers to the service whose nameservers provide the final answer mapping a hostname (such as <code>example.com</code> or <code>blog.example.com</code>) to the IP address that hosts the corresponding content or resources.</p>
<p>The speed and reliability of your authoritative DNS service directly affects how available, resilient, and responsive your website or application is. If the authoritative DNS is slow or unreachable, visitors may not be able to reach your site. Cloudflare DNS is an authoritative DNS service that runs on Cloudflare's global network, distributing DNS answers from data centers worldwide. Refer to <a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a> for details.</p>
<h2 id="dns-setups">DNS setups</h2>
<p>It is also possible that one same company will use more than one DNS provider. Usually, this relates to making a domain more resilient - if one provider faces an outage, the nameservers operated by the other DNS provider will most likely still be available.</p>
<p>In this context, you can have a primary DNS setup, when you use Cloudflare to manage your <a href="#dns-records">DNS records</a>, or a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary DNS setup</a>, when your DNS records are managed on a different provider and Cloudflare simply receives zone transfers containing your DNS records.</p>
<p>When you have a primary DNS setup, you can either use only Cloudflare (also known as <a href="/dns/zone-setups/full-setup/">Full setup</a>), or you can use Cloudflare and another provider, where the other provider is the one to receive <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">outgoing zone transfers</a> from Cloudflare.</p>
<p>Finally, as Cloudflare also works as a <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">reverse proxy</a>, you can use a <a href="/dns/zone-setups/partial-setup/">CNAME setup</a> (also known as partial) when you do not want Cloudflare to be <a href="#authoritative-dns">authoritative</a> for your domain but you still want to proxy individual subdomains through Cloudflare.</p>
<h2 id="dns-records">DNS records</h2>
<p>DNS records are instructions that live in the authoritative DNS servers and provide information about a <a href="#zone">zone</a>. This includes what IP address is associated with a particular domain, but can also cover many other use cases, such as directing emails to a mail server or validating ownership of a domain.</p>
<p>For more details about using DNS records within Cloudflare, refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a> and <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a>.</p>
<h2 id="zone">Zone</h2>
<p>A DNS zone is an administrative boundary that defines who controls the DNS records for a given domain and its subdomains. For example, the zone for <code>example.com</code> contains the records for <code>example.com</code> and its subdomains like <code>blog.example.com</code>. Read more in the <a href="https://www.cloudflare.com/learning/dns/glossary/dns-zone/">&quot;What is a DNS zone?&quot; Learning Center article</a>.</p>
<p>Each domain added to a Cloudflare account is listed on the account home page as a zone. The exact properties and behaviors of your zone depend on its <a href="/dns/zone-setups/">DNS setup</a>.</p>
<p>Different Cloudflare products and features are configurable at the zone level. Refer to <a href="/fundamentals/manage-domains/add-site/">Fundamentals</a> for details.</p>
<h3 id="zone-apex">Zone apex</h3>
<p>The <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1127.md")
</div> is the highest-level domain within a zone — the starting point from which all DNS records in that zone are managed.
<p>In most cases, the zone apex is the same as the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1128.md")
</div> (for example, `example.com`). However, with [subdomain delegation](/dns/zone-setups/subdomain-setup/) (available on Enterprise plans), a subdomain like `sub.example.com` can be its own zone, making that subdomain the zone apex.
<details class="nb-details"><summary>Example 1</summary><div class="nb-details-body">
@input("content/.markup/bodies/1130.md")
</div></details>
<details class="nb-details"><summary>Example 2</summary><div class="nb-details-body">
@input("content/.markup/bodies/1132.md")
</div></details>
<p>To create a DNS record at the zone apex, use <code>@</code> for the record <strong>Name</strong>. The <code>@</code> symbol is a DNS convention that represents the zone apex itself. For details, refer to <a href="/dns/manage-dns-records/how-to/create-zone-apex/">Create zone apex record</a>.</p>
<details class="nb-details"><summary>Record at the zone apex</summary><div class="nb-details-body">
@input("content/.markup/bodies/1135.md")
</div></details>
<h2 id="dnssec">DNSSEC</h2>
<p>Without additional protection, DNS responses can be spoofed — an attacker could return a forged response and redirect visitors to a malicious site. DNSSEC (DNS Security Extensions) addresses this by adding cryptographic signatures to DNS records. These signatures can then be checked to verify that a record came from the correct DNS server, preventing anyone else from issuing false DNS records on your behalf and redirecting traffic intended for your domain. You can read more about it in the <a href="https://www.cloudflare.com/learning/dns/dns-security/">article about DNS security</a>.</p>
<p>For help setting up DNSSEC in Cloudflare, refer to <a href="/dns/dnssec/">Enable DNSSEC</a>.</p>
