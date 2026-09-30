<p>We recommend you add the following DNS policies to build an Internet and SaaS app security strategy for your organization.</p>
<p>For additional commonly used DNS policy examples, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/common-policies/">Common DNS policies</a>. For more information on building DNS policies, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>.</p>
<h2 id="all-dns-domain-allowlist">All-DNS-Domain-Allowlist</h2>
<p>Allowlist any known domains and hostnames. With this policy, you ensure that your users can access your organization's domains even if the domains fall under a blocked category, such as <strong>Newly Seen Domains</strong> or <strong>Login Screens</strong>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10219.md")
</div></div>
<h2 id="quarantined-users-dns-restricted-access">Quarantined-Users-DNS-Restricted-Access</h2>
<p>Restrict access for users included in an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10220.md")
</div> user group for risky users. This policy ensures your security team can restrict traffic for users of whom malicious or suspicious activity was detected.
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10224.md")
</div></div>
<h2 id="all-dns-securitycategories-blocklist">All-DNS-SecurityCategories-Blocklist</h2>
<p>Block <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security categories</a>, such as <strong>Command and Control &amp; Botnet</strong> and <strong>Malware</strong>, based on Cloudflare's threat intelligence.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10228.md")
</div></div>
<h2 id="all-dns-contentcategories-blocklist">All-DNS-ContentCategories-Blocklist</h2>
<p>Entries in the <a href="/cloudflare-one/traffic-policies/domain-categories/#security-risk-subcategories">security risk content subcategory</a>, such as <strong>New Domains</strong>, do not always pose a security threat. We recommend you first create an Allow policy to track policy matching and identify any false positives. You can add false positives to your <strong>Trusted Domains</strong> list used in <strong>All-DNS-Domain-Allowlist</strong>.</p>
<p>After your test is complete, we recommend you change the action to Block to minimize risk to your organization.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10232.md")
</div></div>
<h2 id="all-dns-application-blocklist">All-DNS-Application-Blocklist</h2>
<p>Block unauthorized applications to limit your users' access to certain web-based tools and minimize the risk of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10233.md")
</div>. For example, the following policy blocks known AI tools:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10237.md")
</div></div>
<h2 id="all-dns-geocountryip-blocklist">All-DNS-GeoCountryIP-Blocklist</h2>
<p>Block websites hosted in countries categorized as high risk. The designation of such countries may result from your organization's users or through the implementation of regulations including <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">EAR</a>, <a href="https://orpa.princeton.edu/export-controls/sanctioned-countries">OFAC</a>, and <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">ITAR</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10241.md")
</div></div>
<h2 id="all-dns-domaintoplevel-blocklist">All-DNS-DomainTopLevel-Blocklist</h2>
<p>Block frequently misused top-level domains (TLDs) to reduce security risks, especially when there is no discernible advantage to be gained from allowing access. Similarly, restricting access to specific country-level TLDs may be necessary to comply with regulations such as <a href="https://orpa.princeton.edu/export-controls/sanctioned-countries">OFAC</a> and <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">ITAR</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10245.md")
</div></div>
<h2 id="all-dns-domainphishing-blocklist">All-DNS-DomainPhishing-Blocklist</h2>
<p>Block misused domains to protect your users against sophisticated phishing attacks, such as domains that specifically target your organization. For example, the following policy blocks specific keywords associated with an organization or its authentication services (such as <code>okta</code>, <code>2fa</code>, <code>cloudflare</code> and <code>sso</code>) while still allowing access to known domains.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10249.md")
</div></div>
<h2 id="all-dns-resolvedip-blocklist">All-DNS-ResolvedIP-Blocklist</h2>
<p>Block specific IP addresses that are malicious or pose a threat to your organization.</p>
<p>You can implement this policy by either creating custom blocklists or by using blocklists provided by threat intelligence partners or regional Computer Emergency and Response Teams (CERTs). Ideally, your CERTs can update the blocklist with an <a href="/security-center/intel-apis/">API automation</a> to provide real-time threat protection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10253.md")
</div></div>
<h2 id="all-dns-domainhost-blocklist">All-DNS-DomainHost-Blocklist</h2>
<p>Block specific domains or hosts that are malicious or pose a threat to your organization. Like <strong>All-DNS-ResolvedIP-Blocklist</strong>, this blocklist can be updated manually or via API automation.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10257.md")
</div></div>
