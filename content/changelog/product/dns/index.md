---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/dns/
  description: '2026-09-14'
  full_title: dns changelog | Cloudflare Docs
  head_html: <title>dns changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-14"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/dns/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="dns changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-14"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/dns/#page","headline":"dns changelog | Cloudflare Docs","description":"2026-09-14","url":"https://developers.cloudflare.com/changelog/product/dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/dns/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="shadowed-record-warnings-are-now-available-for-all-zones"><a href="/changelog/post/2026-09-14-shadowed-record-warnings/">Shadowed record warnings are now available for all zones</a></h2>
<p><em>2026-09-14</em></p>
<p>Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.</p>
<p>Shadow metadata is also available in DNS records API responses when you set <code>include_shadow_metadata=true</code>. The metadata identifies the delegating <code>NS</code> records and, when applicable, whether an <code>A</code> or <code>AAAA</code> record is glue. For more information, refer to <a href="/dns/manage-dns-records/reference/shadowed-records/">Shadowed records</a>.</p>


<h2 id="internal-dns-is-now-generally-available"><a href="/changelog/post/2026-07-15-internal-dns-ga/">Internal DNS is now generally available</a></h2>
<p><em>2026-07-15</em></p>
<p><a href="/dns/internal-dns/">Internal DNS</a> is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.</p>
<h4 id="2026-07-15-internal-dns-ga-why-it-matters">Why it matters</h4>
<ul>
<li><strong>Consolidate DNS operations.</strong> Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.</li>
<li><strong>Simplify split-horizon DNS.</strong> Internal and external resolution are defined as separate <a href="/dns/internal-dns/dns-views/">views</a> over shared zones, managed from a single control plane — so there is no drift to chase down.</li>
<li><strong>Extend Zero Trust to DNS.</strong> Resolver policies decide which users and devices resolve against which view, enforced by the same <a href="/cloudflare-one/traffic-policies/">Gateway</a> that already governs the rest of your traffic.</li>
</ul>
<p>Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.</p>
<pre tabindex="0"><code class="language-json">POST /zones&#10;{&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  },&#10;  &quot;name&quot;: &quot;corp.internal&quot;,&#10;  &quot;type&quot;: &quot;internal&quot;&#10;}&#10;</code></pre>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. To get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="new-dns-firewall-ux-with-more-dashboard-settings"><a href="/changelog/post/2026-07-09-new-dns-firewall-ux/">New DNS Firewall UX with more dashboard settings</a></h2>
<p><em>2026-07-09</em></p>
<p>The DNS Firewall page in the Cloudflare dashboard has been refreshed, bringing several settings that were previously API-only into the UI and modernizing how you view and manage your DNS Firewall clusters.</p>
<p><img src="/assets/upstream/images/changelog/dns/dnsfw-new-ux.png" alt="New DNS Firewall UX" /></p>
<h4 id="2026-07-09-new-dns-firewall-ux-what-is-new">What is new</h4>
<ul>
<li><strong>More settings in the dashboard</strong>: cluster options that were previously only configurable through the API — such as attack mitigation, rate limiting, negative TTL, and resolver subnet — are now available directly in the dashboard.</li>
<li><strong>Better table experience</strong>: the DNS Firewall cluster table has been revised to surface cluster details at a glance, with resizable columns and the option to show or hide columns to tailor the view to your workflow.</li>
<li><strong>New create and edit UX</strong>: adding and editing clusters now uses a modernized form that groups related settings together, making configuration faster and clearer.</li>
</ul>
<h4 id="2026-07-09-new-dns-firewall-ux-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2026-07-09-new-dns-firewall-ux-where-to-find-it">Where to find it</h4>
<p>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/dns-firewall/">DNS Firewall</a>.</p>


<h2 id="account-level-dns-records-quota"><a href="/changelog/post/2026-06-10-account-level-record-quota/">Account-level DNS records quota</a></h2>
<p><em>2026-06-10</em></p>
<p>Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.</p>
<p>Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.</p>
<p>For more details, refer to <a href="/dns/manage-dns-records/#dns-records-quota">DNS records quota</a>.</p>


<h2 id="new-dns-records-ux-is-rolling-out"><a href="/changelog/post/2026-05-20-new-dns-records-ux/">New DNS records UX is rolling out</a></h2>
<p><em>2026-05-20</em></p>
<p>Starting today, everyone can opt in to a refreshed DNS records page in the Cloudflare dashboard. Over the coming weeks, the new experience will become the default for Free plan users first, followed by paid plans.</p>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.png" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-what-is-new">What is new</h4>
<ul>
<li><strong>Better table experience</strong>: resizable and hideable columns, row pinning, advanced filters with logical operators (AND/OR), configurable pagination, and expanded input fields so long values are no longer cut off.</li>
<li><strong>First-class mobile experience</strong>: responsive layout with a touch-friendly, card-based UI and compact controls for small screens.</li>
<li><strong>DNS quick reference</strong>: bite-sized explainers for DNS, proxy status, and TTL, available directly in the product to help users configure records without leaving the page.</li>
<li><strong>Modern frontend</strong>: a refactor onto Cloudflare's new UI framework that improves performance and lays the foundation for future improvements.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.gif" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-rollout-plan">Rollout plan</h4>
<p>Dates are subject to change based on feedback received during the rollout.</p>
<ul>
<li><strong>20 May - 05 June</strong>: ramped rollout to Free, then Pro and Business plans.</li>
<li><strong>08 June - 03 July</strong>: ramped rollout to Enterprise plans.</li>
</ul>
<h4 id="2026-05-20-new-dns-records-ux-share-your-feedback">Share your feedback</h4>
<p>Once the new experience is turned on for your account, look for the feedback link at the top of the DNS records page in the Cloudflare dashboard and let us know what you think. Your input helps us prioritize the next round of improvements.</p>


<h2 id="account-level-enforce-dns-only"><a href="/changelog/post/2026-04-28-enforce-dns-only/">Account-level enforce DNS-only</a></h2>
<p><em>2026-04-28</em></p>
<p>You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new <code>enforce_dns_only</code> setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs.
This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17717.md")</aside>
<h4 id="2026-04-28-enforce-dns-only-key-characteristics">Key characteristics</h4>
<ul>
<li><strong>Account-level</strong> — Affects all zones in the account simultaneously with a single API call.</li>
<li><strong>Non-destructive</strong> — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.</li>
<li><strong>API-only</strong> — Available through the API only, not in the Cloudflare dashboard.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-what-s-affected">What's affected</h4>
<p><strong>Included:</strong> Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.</p>
<p><strong>Excluded:</strong> Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.</p>
<h4 id="2026-04-28-enforce-dns-only-before-you-enable">Before you enable</h4>
<ul>
<li>Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.</li>
<li>Review which origin IPs will become publicly visible through DNS queries.</li>
<li>Test the API in a staging account before relying on it for incident response.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-availability">Availability</h4>
<p>Available via API to all Cloudflare customers.</p>
<p>For information on how to use it, refer to <a href="/dns/proxy-status/enforce-dns-only/">Enforce DNS-only developer documentation</a> .</p>


<h2 id="internal-dns-now-in-open-beta"><a href="/changelog/post/2026-03-31-internal-dns-open-beta/">Internal DNS - now in open beta</a></h2>
<p><em>2026-03-31</em></p>
<p>Internal DNS is now in open beta.</p>
<h4 id="2026-03-31-internal-dns-open-beta-who-can-use-it">Who can use it?</h4>
Internal DNS is bundled as a part of Cloudflare Gateway and is now available to every Enterprise customer with one of the following subscriptions:
<ul>
<li>Cloudflare Zero Trust Enterprise</li>
<li>Cloudflare Gateway Enterprise</li>
</ul>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="dns-analytics-for-customer-metadata-boundary-set-to-eu-region"><a href="/changelog/post/2026-03-20-dns-analytics-cmb-eu/">DNS Analytics for Customer Metadata Boundary set to EU region</a></h2>
<p><em>2026-03-20</em></p>
<p>DNS Analytics is now available for customers with <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) set to EU. Query your DNS analytics data while keeping metadata stored in the EU region.</p>
<p>This update includes:</p>
<ul>
<li><strong>DNS Analytics</strong> — Access the same DNS analytics experience for zones in CMB=EU accounts.</li>
<li><strong>EU data residency</strong> — Analytics data is stored and queried from the EU region, meeting data localization requirements.</li>
<li><strong>DNS Firewall Analytics</strong> — DNS Firewall analytics is now supported for CMB=EU customers.</li>
</ul>
<h4 id="2026-03-20-dns-analytics-cmb-eu-availability">Availability</h4>
<p>Available to customers with the <a href="/data-localization/">Data Localization Suite</a> who have Customer Metadata Boundary configured for the EU region.</p>
<h4 id="2026-03-20-dns-analytics-cmb-eu-where-to-find-it">Where to find it</h4>
<ul>
<li><strong>Authoritative DNS:</strong> In the Cloudflare dashboard, select your zone and go to the <strong>Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li><strong>DNS Firewall:</strong> In the Cloudflare dashboard, go to the <strong>DNS Firewall Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/additional-options/analytics/">DNS Analytics</a> and <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a>.</p>


<h2 id="dns-firewall-analytics-now-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-09-16-DNSFW-Analytics-UI/">DNS Firewall Analytics — now in the Cloudflare dashboard</a></h2>
<p><em>2025-09-16</em></p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-what-s-new">What's New</h4>
<p>Access <a href="/dns/dns-firewall/analytics/">GraphQL-powered DNS Firewall analytics</a> directly in the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/dns/DNSFW_Analytics_UI.png" alt="DNS Firewall Analytics UI" /></p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-explore-four-interactive-panels">Explore Four Interactive Panels</h4>
<ul>
<li><strong>Query summary</strong>: Describes trends over time, segmented by dimensions.</li>
<li><strong>Query statistics</strong>: Describes totals, cached/uncached queries, and processing/response times.</li>
<li><strong>DNS queries by data center</strong>: Describes global view and the top 10 data centers.</li>
<li><strong>Top query statistics</strong>: Shows a breakdown by key dimensions, with search and expand options (up to top 100 items).</li>
</ul>
<p>Additional features:</p>
<ul>
<li>Apply filters and time ranges once. Changes reflect across all panels.</li>
<li>Filter by dimensions like query name, query type, cluster, data center, protocol (UDP/TCP), IP version, response code/reason, and more.</li>
<li>Access up to 62 days of historical data with flexible intervals.</li>
</ul>
<h4 id="2025-09-16-DNSFW-Analytics-UI-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-where-to-find-it">Where to Find It</h4>
<ul>
<li>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Refer to the <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a> to learn more.</li>
</ul>


<h2 id="account-level-dns-analytics-now-available-via-graphql-analytics-api"><a href="/changelog/post/2025-06-23-account-level-dns-analytics-api/">Account-level DNS analytics now available via GraphQL Analytics API</a></h2>
<p><em>2025-06-19</em></p>
<p>Authoritative DNS analytics are now available on the <strong>account level</strong> via the <a href="/analytics/graphql-api/">Cloudflare GraphQL Analytics API</a>.</p>
<p>This allows users to query DNS analytics across multiple zones in their account, by using the <code>accounts</code> filter.</p>
<p>Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an <code>NXDOMAIN</code> response over a given time frame. Please replace <code>a30f822fcd7c401984bf85d8f2a5111c</code> with your actual account ID.</p>
<pre tabindex="0"><code class="language-graphql">query GetLatestNXDOMAINResponses {&#10;	viewer {&#10;		accounts(filter: { accountTag: &quot;a30f822fcd7c401984bf85d8f2a5111c&quot; }) {&#10;			dnsAnalyticsAdaptive(&#10;				filter: {&#10;					date_geq: &quot;2025-06-16&quot;&#10;					date_leq: &quot;2025-06-18&quot;&#10;					responseCode: &quot;NXDOMAIN&quot;&#10;				}&#10;				limit: 10000&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				zoneTag&#10;				queryName&#10;				responseCode&#10;				queryType&#10;				datetime&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To learn more and get started, refer to the <a href="/dns/additional-options/analytics/#analytics">DNS Analytics documentation</a>.</p>


<h2 id="internal-dns-beta-now-manageable-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-16-internal-dns-beta-ui/">Internal DNS (beta) now manageable in the Cloudflare dashboard</a></h2>
<p><em>2025-06-16</em></p>
<p>Participating beta testers can now fully configure <a href="/dns/internal-dns/">Internal DNS</a> directly in the <a href="https://dash.cloudflare.com/?to=/:account/internal-dns">Cloudflare dashboard</a>.</p>
<h4 id="2025-06-16-internal-dns-beta-ui-internal-dns-enables-customers-to">Internal DNS enables customers to:</h4>
<ul>
<li>
<p>Map internal hostnames to private IPs for services, devices, and applications not exposed to the public Internet</p>
</li>
<li>
<p>Resolve internal DNS queries securely through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></p>
</li>
<li>
<p>Use split-horizon DNS to return different responses based on network context</p>
</li>
<li>
<p>Consolidate internal and public DNS zones within a single management platform</p>
</li>
</ul>
<h4 id="2025-06-16-internal-dns-beta-ui-what-s-new-in-this-release">What’s new in this release:</h4>
<ul>
<li>Beta participants can now create and manage internal zones and views in the Cloudflare dashboard</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/internal-dns-beta-ui.png" alt="Internal DNS UI" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17716.md")</aside>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="nsec3-support-for-dnssec"><a href="/changelog/post/2025-06-11-nsec3-support/">NSEC3 support for DNSSEC</a></h2>
<p><em>2025-06-11</em></p>
<p>Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>NSEC3 support for live-signed zones</strong> – For both primary and secondary zones that are configured to be live-signed (also known as &quot;on-the-fly signing&quot;), NSEC3 can now be selected as proof of non-existence.</p>
</li>
<li>
<p><strong>NSEC3 support for pre-signed zones</strong> – Secondary zones that are transferred to Cloudflare in a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">pre-signed setup</a> now also support NSEC3 as proof of non-existence.</p>
</li>
</ul>
<p>For more information and how to enable NSEC3, refer to the <a href="/dns/dnssec/enable-nsec3/">NSEC3 documentation</a>.</p>


<h2 id="improved-onboarding-for-shopify-merchants"><a href="/changelog/post/2025-06-03-shopify-o2o-improvements/">Improved onboarding for Shopify merchants</a></h2>
<p><em>2025-06-03</em></p>
<p>Shopify merchants can now onboard to <strong>O2O</strong> automatically, without needing to contact support or community members.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>Automatic enablement</strong> – O2O is available for all mutual Cloudflare and Shopify customers.</p>
</li>
<li>
<p><strong>Branded record display</strong> – Merchants see a Shopify logo in DNS records, complete with helpful tooltips.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/shop-dns-icon-o2o.png" alt="Shopify O2O logo" /></p>
<ul>
<li><strong>Checkout protection</strong> – Workers and Snippets are blocked from running on the checkout path to reduce risk and improve security.</li>
</ul>
<p>For more information, refer to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/">provider guide</a>.</p>


<h2 id="removed-unused-meta-fields-from-dns-records"><a href="/changelog/post/2025-02-02-removed-meta-fields/">Removed unused meta fields from DNS records</a></h2>
<p><em>2025-02-02</em></p>
<p>Cloudflare is removing five fields from the <code>meta</code> object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.</p>
<p>The affected fields are:</p>
<ul>
<li>the <code>auto_added</code> boolean</li>
<li>the <code>managed_by_apps</code> boolean and corresponding <code>apps_install_id</code></li>
<li>the <code>managed_by_argo_tunnel</code> boolean and corresponding <code>argo_tunnel_id</code></li>
</ul>
<p>An example record returned from the API would now look like the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;A&quot;,&#10;		&quot;content&quot;: &quot;192.0.2.1&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;auto_added&quot;: false,&#10;			&quot;managed_by_apps&quot;: false,&#10;			&quot;managed_by_argo_tunnel&quot;: false,&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more guidance, refer to <a href="/dns/manage-dns-records/">Manage DNS records</a>.</p>



