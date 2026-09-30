---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/
  description: Zone status values and what they mean.
  full_title: Zone status · Cloudflare DNS docs
  head_html: <title>Zone status · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Zone status values and what they mean."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/index.md"><meta property="og:title" content="Zone status · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Zone status values and what they mean."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/#page","headline":"Zone status \u00b7 Cloudflare DNS docs","description":"Zone status values and what they mean.","url":"https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/reference/domain-status/
  schema: 1
---
<p>Review information on the different statuses that your <a href="/dns/concepts/#zone">zone</a> can have after you <a href="/fundamentals/manage-domains/add-site/">add your website or application</a> to Cloudflare.</p>
<p>Zone status is also referred to as domain status. An <strong>active</strong> domain status is a requirement for your <a href="/fundamentals/manage-domains/add-site/">application services configurations</a> to be applied. Refer to <a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a> for details.</p>
<p>If your zone status changes, you will receive an email at the address associated with your account.</p>
<p>The following diagram gives you an overview of the different statuses applicable and how your zone may transition from one status to the other. For zones with an active paid subscription, the time to automatic deletion or purge may not correspond to this diagram. Refer to the sections below for details.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Zone status flow&#10;accDescr: Diagram of the different statuses applicable to Cloudflare zones and the transitions from one status to the other.&#10;&#10;A[Initializing]&#10;B[Pending]&#10;C[Active]&#10;D[Moved]&#10;E[Deleted]&#10;F[Purged]&#10;&#10; A-- Plan &lt;br /&gt;selection --&gt; B&#10; B-- Zone &lt;br /&gt;authentication --&gt; C&#10; C-- DNS &lt;br /&gt;checks fail --&gt; D&#10; D-- Moved &lt;br /&gt;for 7 days --&gt; E&#10; E-- Deleted &lt;br /&gt;for 7 days --&gt; F&#10;&#10; B-- Pending for &lt;br /&gt;28 days --&gt; E&#10; A-- Initializing for 28 days --&gt; E&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7911.md")
</aside>
<h2 id="initializing-finish-setup">Initializing (Finish setup)</h2>
<p>You have initiated the setup via dashboard, but did not select a plan for your zone. Your zone status is presented as <strong>Finish setup</strong> on the Cloudflare dashboard.</p>
<p>In this state, Cloudflare does not respond to any DNS queries for your domain.</p>
<p>If your zone is in <strong>Finish setup</strong> for over 28 days, it will be automatically <a href="#deleted">deleted</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7910.md")
</aside>
<h2 id="pending">Pending</h2>
<p>Your zone status is presented as <strong>Pending Nameserver Update</strong> on the Cloudflare dashboard.</p>
<p>Cloudflare responds to DNS queries for pending zones on the assigned Cloudflare nameserver IPs, but your zone is still not active and cannot be used to <a href="/dns/proxy-status/limitations/#pending-domains">proxy traffic to Cloudflare</a>.</p>
<h3 id="causes">Causes</h3>
<ul>
<li><a href="/dns/zone-setups/full-setup/">Primary setup (Full)</a>: You have either not <a href="/dns/nameservers/update-nameservers/">changed your authoritative nameservers</a> or your change has not yet been authenticated by Cloudflare.</li>
<li><a href="/dns/zone-setups/partial-setup/">CNAME setup (Partial)</a>: You have either not added the verification TXT record to your authoritative DNS provider or the record has not yet been authenticated by Cloudflare.</li>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as Secondary DNS provider</a>: When you have either not <a href="/dns/nameservers/update-nameservers/">changed your authoritative nameservers</a> to include the Cloudflare Secondary nameservers or your change has not yet been authenticated by Cloudflare.</li>
</ul>
<p>After you add your domain, Cloudflare performs checks on a schedule to confirm you have updated your nameservers. The first check occurs after 60 seconds and the following attempts happen at gradually increased intervals. You can re-trigger the check <a href="/api/resources/zones/subresources/activation_check/methods/trigger/">via API</a> or on the Dashboard, in the respective domain <a href="https://dash.cloudflare.com/?to=/:account/:zone/">Overview page</a>.</p>
<p>The activation check behavior depends on your zone setup:</p>
<table>
<thead>
<tr>
<th>Zone setup</th>
<th>Activation requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Primary setup (full)</a> without <a href="/dns/nameservers/nameserver-options/#multi-provider-dns">multi-provider DNS</a></td>
<td>At the registrar (or parent zone), only the assigned Cloudflare nameservers must be listed. Any nameservers from other DNS providers cause failure.</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Primary setup (full)</a> with <a href="/dns/nameservers/nameserver-options/#multi-provider-dns">multi-provider DNS</a> enabled, or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary setup</a></td>
<td>At the registrar (or parent zone), the assigned Cloudflare nameservers must be present. Nameservers from other DNS providers are allowed.</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">CNAME setup (partial)</a></td>
<td>The verification TXT record must be present on your authoritative DNS provider. Nameservers at the registrar are not changed.</td>
</tr>
</tbody>
</table>
<h3 id="expected-behavior-for-different-plans">Expected behavior for different plans</h3>
<p>If your domain is on the Free plan, it will be automatically deleted if it is not activated within 28 days.</p>
<p>Any pending zone with a paid plan (Pro, Business, Enterprise) will remain pending until the plan is removed, or the domain is activated or <a href="/fundamentals/manage-domains/remove-domain/">removed from Cloudflare</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-use-pending-zones-in-production">Do not use pending zones in production</h3>
@markup("md", "content/.markup/bodies/7909.md")
</aside>
<p>For Enterprise zones, if you want to adjust settings before zone activation, Logpush for <a href="/logs/logpush/logpush-job/datasets/zone/dns_logs/">DNS logs</a> and <a href="/dns/zone-setups/zone-transfers/">DNS Zone Transfer</a> configuration work as expected in pending state.</p>
<h2 id="active">Active</h2>
<p>Cloudflare has authenticated your <a href="/dns/nameservers/update-nameservers/">nameserver changes</a> or <a href="/dns/zone-setups/partial-setup/setup/#2-verify-ownership-for-your-domain">verification TXT record</a> and you can proxy domain traffic through Cloudflare. For more details refer to <a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a> and <a href="/fundamentals/manage-domains/add-site/">Domain configurations</a>.</p>
<h2 id="moved">Moved</h2>
<p>Your domain has failed multiple DNS checks, where either the Cloudflare nameservers are no longer present on your domain's <code>NS</code> records (<a href="/dns/zone-setups/full-setup/">Primary setup (Full)</a>) or no <code>SOA</code> record is returned for the zone (<a href="/dns/zone-setups/partial-setup/">CNAME setup (Partial)</a>).</p>
<h3 id="expected-behavior-for-different-plans-1">Expected behavior for different plans</h3>
<p>If your domain is on the Free plan, it will be automatically deleted 7 days after it entered the moved status.</p>
<p>For moved zones with a paid plan (Pro, Business, Enterprise), deletion will occur after 7 days if any of the following is observed:</p>
<ul>
<li>The paid plan is removed.</li>
<li>The domain is activated in another Cloudflare account.</li>
</ul>
<p>You can also <a href="/fundamentals/manage-domains/remove-domain/">manually remove</a> your domain from Cloudflare.</p>
<h2 id="deleted">Deleted</h2>
<p>Your zone has been archived. Cloudflare still responds to DNS queries for deleted zones on the assigned Cloudflare nameserver IPs (for non-deleted DNS records) and you can re-add the domain to Cloudflare by following the <a href="/fundamentals/manage-domains/add-site/">regular onboarding flow</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="new-nameserver-assignment">New nameserver assignment</h3>
@markup("md", "content/.markup/bodies/7908.md")
</aside>
<p>After being deleted for seven days, zones are automatically <a href="#purged">purged</a>.</p>
<h2 id="purged">Purged</h2>
<p>After a zone is deleted for seven days, it will be purged. Cloudflare does not respond to DNS queries for purged zones and, unlike <a href="#deleted">deleted zones</a>, this status cannot be reverted. In this case, even if you re-add the domain to the same Cloudflare account, none of the zone settings are expected to be restored.</p>
