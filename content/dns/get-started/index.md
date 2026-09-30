<p>You can use Cloudflare DNS with a variety of <a href="/dns/zone-setups/">setups</a>. For an overview of what these setups are and an introduction to specific DNS terminology, refer to <a href="/dns/concepts/">Concepts</a>.</p>
<p>In the most common setup (full), you <a href="/fundamentals/manage-domains/add-site/">add your domain</a>, import your <a href="/dns/manage-dns-records/">DNS records</a>, and <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> to make Cloudflare your primary authoritative DNS provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1123.md")
</aside>
<p>Once the setup is completed:</p>
<ul>
<li>
<p>You <a href="/dns/manage-dns-records/how-to/create-dns-records/">manage DNS records</a> through the Cloudflare dashboard or API. This is how you control which resources are available on the apex domain (<code>example.com</code>) or specific subdomains (<code>blog.example.com</code>) of your website, as well as control other configurations.</p>
</li>
<li>
<p>Cloudflare <a href="/fundamentals/concepts/how-cloudflare-works/">responds to all DNS queries</a> for your hostnames and your DNS records are propagated across the <a href="https://www.cloudflare.com/network/">Cloudflare global network</a>, speeding up your domain.</p>
</li>
</ul>
<h2 id="resources">Resources</h2>
<p>The following links introduce important concepts and will guide you through actions you may need to take while having your website or application on Cloudflare.</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/">DNS records</a>: DNS records contain information about your domain and are used to make your website or application available to visitors and other web services.</p>
</li>
<li>
<p><a href="/dns/nameservers/">Nameservers</a>: In the context of Cloudflare DNS, nameservers refer to authoritative nameservers. When a nameserver is authoritative for <code>example.com</code>, it means that DNS resolvers will consider responses from this nameserver when a user tries to access <code>example.com</code>.</p>
</li>
<li>
<p><a href="/dns/proxy-status/">Proxy status</a>: Proxy status affects how Cloudflare treats incoming HTTP/S requests to A, AAAA, and CNAME records. When a record is proxied, Cloudflare responds with <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IPs</a>, which speeds up and protects HTTP/S traffic with our <a href="/cache/">cache</a>/<a href="https://www.cloudflare.com/learning/cdn/what-is-a-cdn/">CDN</a>, <a href="/ddos-protection/">DDoS protection</a>, <a href="/waf/">WAF</a>, and <a href="/directory/?product-group=Application+performance%2CApplication+security">more</a>.</p>
</li>
</ul>
<h2 id="further-reading">Further reading</h2>
<ul>
<li>
<p><a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a>: An overview of how Cloudflare works as a DNS provider and as a reverse proxy.</p>
</li>
<li>
<p><a href="/dns/additional-options/analytics/">DNS analytics</a>: An overview of the different data sources and insights you can get when using Cloudflare DNS.</p>
</li>
<li>
<p><a href="/dns/troubleshooting/">Troubleshooting</a>: A full resources list for when something is not working.</p>
</li>
</ul>
