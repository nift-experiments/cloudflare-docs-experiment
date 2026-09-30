<p>We recommend you add the following HTTP policies to build an Internet and SaaS app security strategy for your organization.</p>
<p>For additional commonly used HTTP policy examples, refer to <a href="/cloudflare-one/traffic-policies/http-policies/common-policies/">Common HTTP policies</a>. For more information on building HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
<h2 id="all-http-application-inspectbypass">All-HTTP-Application-InspectBypass</h2>
<p>Bypass HTTP inspection for applications that use embedded certificates. This will help avoid any certificate pinning errors that may arise from an initial rollout.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10150.md")
</div></div>
<h2 id="android-http-application-inspectionbypass">Android-HTTP-Application-InspectionBypass</h2>
<p>Bypass HTTPS inspection for Android applications (such as Google Drive) that use certificate pinning, which is incompatible with Gateway inspection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10154.md")
</div></div>
<h2 id="all-http-domain-inspection-bypass">All-HTTP-Domain-Inspection-Bypass</h2>
<p>Bypass HTTP inspection for a custom list of domains identified as incompatible with TLS inspection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10158.md")
</div></div>
<h2 id="all-http-securityrisks-blocklist">All-HTTP-SecurityRisks-Blocklist</h2>
<p>Block <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security categories</a>, such as <strong>Command and Control &amp; Botnet</strong> and <strong>Malware</strong>, based on Cloudflare's threat intelligence.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10162.md")
</div></div>
<h2 id="all-http-contentcategories-blocklist">All-HTTP-ContentCategories-Blocklist</h2>
<p>Entries in the <a href="/cloudflare-one/traffic-policies/domain-categories/#security-risk-subcategories">security risk content subcategory</a>, such as <strong>New Domains</strong>, do not always pose a security threat. We recommend you first create an Allow policy to track policy matching and identify any false positives. You can add false positives to your <strong>Trusted Domains</strong> list used in <strong>All-HTTP-Domain-Allowlist</strong>.</p>
<p>After your test is complete, we recommend you change the action to Block to minimize risk to your organization.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10166.md")
</div></div>
<h2 id="all-http-domainhost-blocklist">All-HTTP-DomainHost-Blocklist</h2>
<p>Block specific domains or hosts that are malicious or pose a threat to your organization. Like <strong>All-HTTP-ResolvedIP-Blocklist</strong>, this blocklist can be updated manually or via API automation.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10170.md")
</div></div>
<h2 id="all-http-application-blocklist">All-HTTP-Application-Blocklist</h2>
<p>Block unauthorized applications to limit your users' access to certain web-based tools and minimize the risk of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10171.md")
</div>. For example, the following policy blocks known AI tools:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10175.md")
</div></div>
<h2 id="privilegedusers-http-any-isolate">PrivilegedUsers-HTTP-Any-Isolate</h2>
<p>Isolate traffic for privileged users who regularly access critical systems or execute actions such as threat analysis and malware testing.</p>
<p>Security teams often need to perform threat analysis or malware testing that could trigger malware detection. Likewise, privileged users could be the target of attackers trying to gain access to critical systems.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10179.md")
</div></div>
<h2 id="quarantined-users-http-restricted-access">Quarantined-Users-HTTP-Restricted-Access</h2>
<p>Restrict access for users included in an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10180.md")
</div> user group for risky users. This policy ensures your security team can restrict traffic for users of whom malicious or suspicious activity was detected.
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10184.md")
</div></div>
<h2 id="all-http-domain-isolate">All-HTTP-Domain-Isolate</h2>
<p>Isolate high risk domains or create a custom list of known risky domains to avoid data exfiltration or malware infection. Ideally, your incident response teams can update the blocklist with an <a href="/security-center/intel-apis/">API automation</a> to provide real-time threat protection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10188.md")
</div></div>
