<p>The following Cloudflare Gateway DNS policies are commonly used to secure DNS traffic. Each example includes both dashboard and API instructions that you can adapt for your organization.</p>
<p>For a baseline set of recommended policies, refer to <a href="/learning-paths/secure-internet-traffic/build-dns-policies/recommended-dns-policies/">Secure your Internet traffic and SaaS apps</a>.</p>
<p>Refer to the <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies page</a> for a comprehensive list of other selectors, operators, and actions.</p>
<h2 id="allow-corporate-domains">Allow corporate domains</h2>
<p>This policy allows users to access official corporate domains. By deploying the policy with high <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">order of precedence</a>, you ensure that employees can access trusted domains even if they fall under a blocked category like <em>Newly seen domains</em> or <em>Login pages</em>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6666.md")
</div></div>
<h2 id="block-security-threats">Block security threats</h2>
<p>Block <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security categories</a> such as Command &amp; Control, Botnet and Malware based on Cloudflare's threat intelligence.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6670.md")
</div></div>
<h2 id="block-content-categories">Block content categories</h2>
<p>The categories included in this policy are not always a security threat, but blocking them can help minimize the risk that your organization is exposed to. For more information, refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">domain categories</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6674.md")
</div></div>
<h2 id="block-a-dynamic-list-of-categories">Block a dynamic list of categories</h2>
<p>You can add a list of category IDs to the <a href="https://datatracker.ietf.org/doc/html/rfc6891">EDNS (Extension Mechanisms for DNS)</a> header of a request sent to Gateway as a JSON object using OPT code <code>65050</code>. EDNS allows extra metadata to be attached to a DNS query beyond the standard fields. For example:</p>
<pre><code class="language-json">{&#10;	&quot;categories&quot;: [2, 67, 125, 133]&#10;}&#10;</code></pre>
<p>With the <a href="/cloudflare-one/traffic-policies/dns-policies/#request-context-categories">Request Context Categories</a> selector, you can block the category IDs sent with EDNS. This is useful to filter by categories not known at the time of creating a policy, or to enforce device-specific DNS content filtering without reaching your account limit. When Gateway uses this selector to block a DNS query, the request will return an Extended DNS Error (EDE) Code 15 (<code>Blocked</code>), along with a field containing an array of the matched categories.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6678.md")
</div></div>
<h2 id="block-unauthorized-applications">Block unauthorized applications</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6663.md")
</aside>
<p>To minimize the risk of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6679.md")
</div>, some organizations choose to limit their users' access to certain web-based tools and applications. For example, the following policy blocks known AI tools:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6683.md")
</div></div>
<h2 id="block-banned-countries">Block banned countries</h2>
<p>You can implement policies to block websites hosted in countries categorized as high risk. The designation of such countries may result from your organization's requirements or through regulations including <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">EAR (Export Administration Regulations)</a>, <a href="https://orpa.princeton.edu/export-controls/sanctioned-countries">OFAC (Office of Foreign Assets Control)</a>, and <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">ITAR (International Traffic in Arms Regulations)</a>. This policy blocks DNS queries that resolve to IP addresses geolocated in the countries you specify.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6686.md")
</div></div>
<h2 id="block-top-level-domains">Block top-level domains</h2>
<p>Blocking <a href="https://www.spamhaus.org/statistics/tlds/">frequently misused</a> top-level domains (TLDs) — the last segment of a domain name, such as <code>.com</code> or <code>.ru</code> — can reduce security risks, especially when there is no discernible advantage to be gained from allowing access. Similarly, restricting access to specific country-level TLDs may be necessary to comply with regulations like <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">ITAR</a> or <a href="https://orpa.princeton.edu/export-controls/sanctioned-countries">OFAC</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6689.md")
</div></div>
<h2 id="block-phishing-attacks">Block phishing attacks</h2>
<p>To protect against <a href="https://blog.cloudflare.com/2022-07-sms-phishing-attacks/">sophisticated phishing attacks</a>, you could prevent users from accessing phishing domains that are specifically targeting your organization. The following policy blocks specific keywords associated with an organization or its authentication services (such as <em>okta</em>, <em>2fa</em>, <em>cloudflare</em> or <em>sso</em>), while still allowing access to official corporate domains.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6692.md")
</div></div>
<h2 id="block-online-tracking">Block online tracking</h2>
<p>To safeguard user privacy, some organizations will block tracking domains such as <code>dig.whatsapp.com</code> as well as other tracking domains embedded at the OS level. This policy is implemented by creating a custom blocklist. Refer to <a href="https://github.com/nextdns/native-tracking-domains/tree/28991a0d5b2ab6d35588a74af82162ea7caff420/domains">this repository</a> for a list of widespread tracking domains that you can add to your blocklist.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6695.md")
</div></div>
<h2 id="block-malicious-ips">Block malicious IPs</h2>
<p>Block specific IP addresses that are known to be malicious or pose a threat to your organization. This policy is usually implemented by creating custom blocklists or by using blocklists provided by threat intelligence partners or regional Computer Emergency and Response Teams (CERTs).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6698.md")
</div></div>
<h2 id="turn-on-cipa-filter">Turn on CIPA filter</h2>
<p>The CIPA (Children's Internet Protection Act) Filter is a collection of subcategories that encompass a wide range of topics that could be harmful or inappropriate for minors. It is used as a part of <a href="/fundamentals/reference/policies-compliances/cybersafe/">Project Cybersafe Schools</a> to block access to unwanted or harmful online content. Upon creating this policy, your organization will have minimum <a href="https://www.fcc.gov/consumers/guides/childrens-internet-protection-act">CIPA compliance</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6701.md")
</div></div>
<h2 id="hide-explicit-search-results">Hide explicit search results</h2>
<p>SafeSearch is a feature of search engines that helps you filter explicit or offensive content. You can force SafeSearch on search engines like Google, Bing, Yandex, YouTube, and DuckDuckGo:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6704.md")
</div></div>
<h2 id="check-user-identity">Check user identity</h2>
<p>Configure access on a per user or group basis by adding <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based conditions</a> to your policies.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6707.md")
</div></div>
<h2 id="restrict-access-to-specific-groups">Restrict access to specific groups</h2>
<p>Filter DNS queries to allow only specific users access.</p>
<p>The following example includes two policies. The first policy allows the specified group, while the second policy blocks all other users. To ensure the policies are evaluated properly, place the Allow policy above the Block policy. For more information, refer to the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">order of precedence</a>.</p>
<h3 id="1-allow-a-group"><ol>
<li>Allow a group</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6710.md")
</div></div>
<h3 id="2-block-all-other-users"><ol start="2">
<li>Block all other users</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6713.md")
</div></div>
<h2 id="control-ip-version">Control IP version</h2>
<p>Enterprise users can pair these policies with an <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policy</a> to control which IP version is used when Gateway connects to the destination server.</p>
<p>Optionally, you can use the Domain selector to control the IP version for specific sites.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6662.md")
</aside>
<h3 id="force-ipv4">Force IPv4</h3>
<p>Force users to connect with IPv4 by blocking <code>AAAA</code> (IPv6) record resolution.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6716.md")
</div></div>
<h3 id="force-ipv6">Force IPv6</h3>
<p>Force users to connect with IPv6 by blocking <code>A</code> (IPv4) record resolution.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6719.md")
</div></div>
