<p>Cloudflare's Advanced DNS Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, provides stateful protection against DNS-based DDoS attacks, specifically sophisticated and fully randomized DNS attacks such as <a href="/dns/dns-firewall/random-prefix-attacks/about/">random prefix attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7496.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Cloudflare's Advanced DNS Protection works by first learning your traffic patterns and forming a baseline of the type of DNS queries you normally receive. Later, the system will be able to distinguish between legitimate and malicious queries, protecting your DNS infrastructure without impacting legitimate traffic.</p>
<p>Currently, the protection system only analyzes DNS over UDP (it does not include DNS over TCP).</p>
<p>The <a href="/analytics/network-analytics/">Network Analytics dashboard</a> will display system-specific analytics for Advanced DNS Protection in the <strong>DNS protection</strong> tab, including the queried domains and record types.</p>
<hr />
<h2 id="setup">Setup</h2>
<p><a href="/ddos-protection/advanced-ddos-systems/how-to/create-rule/#create-an-advanced-dns-protection-rule">Create a rule</a> to enable Advanced DNS Protection.</p>
<hr />
<h2 id="data-collection">Data collection</h2>
<p>Cloudflare collects DNS-related data such as query type (for example, <code>A</code> record) and the queried domains. For details, refer to <a href="/analytics/network-analytics/reference/data-collection/">Data collection</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7495.md")
</aside>
<hr />
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="no-data-about-advanced-dns-protection-in-network-analytics">No data about Advanced DNS Protection in Network Analytics</h3>
<p>If you cannot find any data related to Advanced DNS Protection in the <strong>DNS Protection</strong> tab of Network Analytics, it could be because one of these reasons:</p>
<ul>
<li>You did not <a href="/ddos-protection/advanced-ddos-systems/how-to/add-prefix/">add your prefixes</a> to Advanced L3/4 DDoS Protection.</li>
<li>Accounts that existed before January 2025 were not automatically provisioned. If you onboarded before January 2025, Advanced DNS Protection may not have been enabled for your account.</li>
<li>You do not have any DNS over UDP traffic.</li>
</ul>
<hr />
<h2 id="related-products">Related products</h2>
<p>Advanced DNS Protection can protect you against volumetric DNS DDoS attacks. To perform DNS caching, proxying, and configuration, use the <a href="/dns/dns-firewall/">Cloudflare DNS Firewall</a>.</p>
<p>Currently, Advanced DNS Protection is not available for DNS Firewall.</p>
