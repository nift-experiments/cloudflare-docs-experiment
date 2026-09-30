---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-security/4/
  description: '2026-03-06'
  full_title: Application security changelog - page 4 | Cloudflare Docs
  head_html: <title>Application security changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-03-06"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-security/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application security changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-03-06"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-security/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-security/4/#page","headline":"Application security changelog - page 4 | Cloudflare Docs","description":"2026-03-06","url":"https://developers.cloudflare.com/changelog/product-group/application-security/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-security/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="dismiss-and-filter-matches-in-brand-protection"><a href="/changelog/post/2026-03-06-brand-protection-dismiss-match/">Dismiss and filter matches in Brand Protection</a></h2>
<p><em>2026-03-06</em></p>
<p>We have introduced new triage controls to help you manage your Brand Protection results more efficiently. You can now clear out the noise by dismissing matches while maintaining full visibility into your historical decisions.</p>
<h4 id="2026-03-06-brand-protection-dismiss-match-what-s-new">What's new</h4>
<ul>
<li><strong>Dismiss matches</strong>: Users can now mark specific results as dismissed if they are determined to be benign or false positives, removing them from the primary triage view.</li>
<li><strong>Show/Hide toggle</strong>: A new visibility control allows you to instantly switch between viewing only active matches and including previously dismissed ones.</li>
<li><strong>Persistent review states</strong>: Dismissed status is saved across sessions, ensuring that your workspace remains organized and focused on new or high-priority threats.</li>
</ul>
<h4 id="2026-03-06-brand-protection-dismiss-match-key-benefits-of-the-dismiss-match-functionality">Key benefits of the dismiss match functionality:</h4>
<ul>
<li>Reduce alert fatigue by hiding known-safe results, allowing your team to focus exclusively on unreviewed or high-risk infringements.</li>
<li>Auditability and recovery through the visibility toggle, ensuring that no match is ever truly &quot;lost&quot; and can be re-evaluated if a site's content changes.</li>
<li>Improved collaboration as your team members can see which matches have already been vetted and dismissed by others.</li>
</ul>
<p>Ready to clean up your match queue? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="waf-release-2026-03-02"><a href="/changelog/post/2026-03-02-waf-release/">WAF Release - 2026-03-02</a></h2>
<p><em>2026-03-02</em></p>
<p>This week's release introduces new detections for vulnerabilities in SmarterTools SmarterMail (CVE-2025-52691 and CVE-2026-23760), alongside improvements to an existing Command Injection (nslookup) detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-52691: SmarterTools SmarterMail mail server is vulnerable to Arbitrary File Upload, allowing an unauthenticated attacker to upload files to any location on the mail server, potentially enabling remote code execution.</li>
<li>CVE-2026-23760: SmarterTools SmarterMail versions prior to build 9511 contain an authentication bypass vulnerability in the password reset API permitting unaunthenticated to reset system administrator accounts failing to verify existing password or reset token.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these SmarterMail vulnerabilities could lead to full system compromise or unauthorized administrative access to mail servers. Administrators are strongly encouraged to apply vendor patches without delay.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0f282f3c89614779966faf52966ec6b1">966ec6b1</code>
</td>
<td>N/A</td>
<td>SmarterMail - Arbitrary File Upload - CVE-2025-52691</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35978af68e374a059e397bf5ee964a8c">ee964a8c</code>
</td>
<td>N/A</td>
<td>SmarterMail - Authentication Bypass - CVE-2026-23760</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4bb099bcd71141d4a35c1aa675b64d99">75b64d99</code>
</td>
<td>N/A</td>
<td>Command Injection - Nslookup - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Command Injection - Nslookup" (ID: <code class="nb-rule-id" title="f4a310393c564d50bd585601b090ba9a">b090ba9a</code>)</td>
</tr>
</tbody>
</table>


<h2 id="saved-views-for-threat-events"><a href="/changelog/post/2026-02-23-Saved-views-in-threat-events/">Saved views for Threat Events</a></h2>
<p><em>2026-02-23</em></p>
<p><strong>TL;DR:</strong> You can now create and save custom configurations of the Threat Events dashboard, allowing you to instantly return to specific filtered views — such as industry-specific attacks or regional Sankey flows — without manual reconfiguration.</p>
<h4 id="2026-02-23-Saved-views-in-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is personalized. Previously, analysts had to manually re-apply complex filters (like combining specific industry datasets with geographic origins) every time they logged in. This update provides material value by:</p>
<ul>
<li>Analysts can now jump straight into &quot;Known Ransomware Infrastructure&quot; or &quot;Retail Sector Targets&quot; views with a single click, eliminating repetitive setup tasks</li>
<li>Teams can ensure everyone is looking at the same data subsets by using standardized saved views, reducing the risk of missing critical patterns due to inconsistent filtering.</li>
</ul>
<p>Cloudforce One subscribers can start saving their custom views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="manage-cloudflare-tunnel-directly-from-the-main-cloudflare-dashboard"><a href="/changelog/post/2026-02-20-tunnel-core-dashboard/">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</a></h2>
<p><em>2026-02-20</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="2026-02-20-tunnel-core-dashboard-choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="2026-02-20-tunnel-core-dashboard-get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>


<h2 id="cloudforce-one-threat-events-graphs-are-now-visible-in-the-dashboard"><a href="/changelog/post/2026-02-19-threat-events-graphs/">Cloudforce One Threat events graphs are now visible in the dashboard</a></h2>
<p><em>2026-02-19</em></p>
<p>We have introduced dynamic visualizations to the Threat Events dashboard to help you better understand the threat landscape and identify emerging patterns at a glance.</p>
<p>What's new:</p>
<ul>
<li><strong>Sankey Diagrams</strong>: Trace the flow of attacks from country of origin to target country to identify which regions are being hit hardest and where the threat infrastructure resides.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-sankey-diagram.png" alt="Sankey Diagram" /></p>
<ul>
<li><strong>Dataset Distribution over time</strong>: Instantly pivot your view to understand if a specific campaign is targeting your sector or if it is a broad-spectrum commodity attack.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-events-over-time.png" alt="Events over time" /></p>
<ul>
<li><strong>Enhanced Filtering</strong>: Use these visual tools to filter and drill down into specific attack vectors directly from the charts.</li>
</ul>
<p>Cloudforce One subscribers can explore these new views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="waf-release-2026-02-16"><a href="/changelog/post/2026-02-16-waf-release/">WAF Release - 2026-02-16</a></h2>
<p><em>2026-02-16</em></p>
<p>This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the <code>/h/rest</code> endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.</li>
<li>CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via <code>?inline&amp;import</code> when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="695d76ff756844d384cab548833761f7">833761f7</code>
</td>
<td>N/A</td>
<td>Zimbra - Local File Inclusion - CVE:CVE-2025-68645</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38fff9f3deba46a2abc10a8f950ed8c8">950ed8c8</code>
</td>
<td>N/A</td>
<td>Vite - WASM Import Path Traversal - CVE:CVE-2025-31125</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="enhanced-logo-matching-for-brand-protection"><a href="/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/">Enhanced Logo Matching for Brand Protection</a></h2>
<p><em>2026-02-12</em></p>
<p>We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.</p>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-what-s-new">What's new</h4>
<ul>
<li><strong>Configurable match thresholds</strong>: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.</li>
<li><strong>Visual match scores</strong>: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.</li>
<li><strong>Direct logo previews</strong>: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.</li>
</ul>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-key-benefits">Key benefits</h4>
<ul>
<li><strong>Expose sophisticated impersonators</strong> who use slightly altered logos to bypass basic detection filters.</li>
<li><strong>Faster triage</strong> of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.</li>
</ul>
<p>Ready to protect your visual identity? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="waf-release-2026-02-10"><a href="/changelog/post/2026-02-10-waf-release/">WAF Release - 2026-02-10</a></h2>
<p><em>2026-02-10</em></p>
<p>This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ce11be543594412bb4bb92516aa0bef8">6aa0bef8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Google Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>We are changing the action for this rule from BLOCK to Disabled</td>
</tr>
</tbody>
</table>


<h2 id="threat-actor-identification-with-also-known-as-aliases"><a href="/changelog/post/2026-02-03-threat-actor-name-mapping/">Threat actor identification with "also known as" aliases</a></h2>
<p><em>2026-02-03</em></p>
<p>Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, <strong>Cloudflare Threat Events</strong> now include an <strong>Also known as</strong> field, providing a list of common aliases and industry-standard names for the groups we track.</p>
<p>This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the <strong>Attacker</strong> field) or by adding it as a column in your configurable table view.</p>
<h4 id="2026-02-03-threat-actor-name-mapping-key-benefits">Key benefits</h4>
<ul>
<li>Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.</li>
<li>Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.</li>
</ul>
<p>For more information on how to access this data, refer to the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/">Threat Events API documentation</a>.</p>


<h2 id="waf-release-2026-02-02"><a href="/changelog/post/2026-02-02-waf-release/">WAF Release - 2026-02-02</a></h2>
<p><em>2026-02-02</em></p>
<p>This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the <code>Q()</code> class.</li>
<li>CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7a47683eacce4abd870ab2c630698ff3">30698ff3</code>
</td>
<td>N/A</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ad5c52f6ca334ef4a844e5e5da8ba7e6">da8ba7e6</code>
</td>
<td>N/A</td>
<td>Django SQLI - CVE:CVE-2025-64459</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8f0d5c98bd24460a9305a1558d667511">8d667511</code>
</td>
<td>N/A</td>
<td>NoSQL, MongoDB - SQLi - Comparison - 2</td>
<td>Block</td>
<td>Block</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="control-request-and-response-body-buffering-in-configuration-rules"><a href="/changelog/post/2026-01-27-body-buffering-settings/">Control request and response body buffering in Configuration Rules</a></h2>
<p><em>2026-01-27</em></p>
<p>You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>
<h4 id="2026-01-27-body-buffering-settings-request-body-buffering">Request body buffering</h4>
<p>Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management.</td>
</tr>
<tr>
<td><strong>Full</strong></td>
<td>Buffers the entire request body before sending to origin.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the request body streams directly to origin without inspection.</td>
</tr>
</tbody>
</table>
<h4 id="2026-01-27-body-buffering-settings-response-body-buffering">Response body buffering</h4>
<p>Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the response body for enabled functionality.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the response body streams directly to the client without inspection.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17748.md")</aside>
<h4 id="2026-01-27-body-buffering-settings-api-example">API example</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;action&quot;: &quot;set_config&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;request_body_buffering&quot;: &quot;standard&quot;,&#10;    &quot;response_body_buffering&quot;: &quot;none&quot;&#10;  }&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>


<h2 id="waf-release-2026-01-26"><a href="/changelog/post/2026-01-26-waf-release/">WAF Release - 2026-01-26</a></h2>
<p><em>2026-01-26</em></p>
<p>This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>) affects <code>react-server-dom-parcel</code>, <code>react-server-dom-turbopack</code>, and <code>react-server-dom-webpack</code> packages.</li>
<li>Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3e93c9faaafa447c83a525f2dcdffcf8">dcdffcf8</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="930020d567684f19b05fb35b349edbc6">349edbc6</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 3</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="new-cryptographic-functions-encode-base64-and-sha256"><a href="/changelog/post/2026-01-22-sha256-base64-encode-functions/">New cryptographic functions — encode_base64() and sha256()</a></h2>
<p><em>2026-01-22</em></p>
<p>Cloudflare Rulesets now includes <code>encode_base64()</code> and <code>sha256()</code> functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.</p>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>encode_base64(input, flags)</code></td>
<td>Encodes a string to Base64 format. Optional <code>flags</code> parameter: <code>u</code> for URL-safe encoding, <code>p</code> for padding (adds <code>=</code> characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding.</td>
<td>All plans (in header transform rules)</td>
</tr>
<tr>
<td><code>sha256(input)</code></td>
<td>Computes a SHA256 hash of the input string.</td>
<td>Requires enablement</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17747.md")</aside>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-examples">Examples</h4>
<p><strong>Encode a string to Base64 format:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Encode a string to Base64 format with padding:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;p&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ=</code></p>
<p><strong>Perform a URL-safe Base64 encoding of a string:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;u&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Compute the SHA256 hash of a secret token:</strong></p>
<pre tabindex="0"><code class="language-txt">sha256(&quot;my-token&quot;)&#10;</code></pre>
<p>Returns a hash that your origin can validate to authenticate requests.</p>
<p><strong>Compute the SHA256 hash of a string and encode the result to Base64 format:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(sha256(&quot;my-token&quot;))&#10;</code></pre>
<p>Combines hashing and encoding for systems that expect Base64-encoded signatures.</p>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="new-functions-for-array-and-map-operations"><a href="/changelog/post/2026-01-20-array-map-functions/">New functions for array and map operations</a></h2>
<p><em>2026-01-20</em></p>
<h4 id="2026-01-20-array-map-functions-new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
<p>Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.</p>
<hr />
<h4 id="2026-01-20-array-map-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>split(source, delimiter)</code></td>
<td>Splits a string into an array of strings using the specified delimiter.</td>
</tr>
<tr>
<td><code>join(array, delimiter)</code></td>
<td>Joins an array of strings into a single string using the specified delimiter.</td>
</tr>
<tr>
<td><code>has_key(map, key)</code></td>
<td>Returns <code>true</code> if the specified key exists in the map.</td>
</tr>
<tr>
<td><code>has_value(map, value)</code></td>
<td>Returns <code>true</code> if the specified value exists in the map.</td>
</tr>
</tbody>
</table>
<hr />
<h4 id="2026-01-20-array-map-functions-example-use-cases">Example use cases</h4>
<p><strong>Check if a country code exists in a header list:</strong></p>
<pre tabindex="0"><code class="language-txt">has_value(split(http.response.headers[&quot;x-allow-country&quot;][0], &quot;,&quot;), ip.src.country)&#10;</code></pre>
<p><strong>Check if a specific header key exists:</strong></p>
<pre tabindex="0"><code class="language-txt">has_key(http.request.headers, &quot;x-custom-header&quot;)&#10;</code></pre>
<p><strong>Join array values for logging or comparison:</strong></p>
<pre tabindex="0"><code class="language-txt">join(http.request.headers.names, &quot;, &quot;)&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="waf-release-2026-01-20"><a href="/changelog/post/2026-01-20-waf-release/">WAF Release - 2026-01-20</a></h2>
<p><em>2026-01-20</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL injection.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a291bd530fa346d18cc1ce5a68d90c8f">68d90c8f</code>
</td>
<td>N/A</td>
<td>SQLi - Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Comment" (ID: <code class="nb-rule-id" title="42c424998d2a42c9808ab49c6d8d8fe4">6d8d8fe4</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="da289f9e692e4f5397d915fbfaa045cf">faa045cf</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Comparison" (ID: <code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="verify-warp-connector-connectivity-with-a-simple-ping"><a href="/changelog/post/2026-01-15-warp-connector-ping-support/">Verify WARP Connector connectivity with a simple ping</a></h2>
<p><em>2026-01-15</em></p>
<p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>


<h2 id="waf-release-2026-01-15"><a href="/changelog/post/2026-01-15-waf-release/">WAF Release - 2026-01-15</a></h2>
<p><em>2026-01-15</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="eb3f44c07266448b9fa54ee7ad7dad3e">ad7dad3e</code>
</td>
<td>N/A</td>
<td>SQLi - String Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - String Function" (ID: <code class="nb-rule-id" title="63e03eecddfc4b3fb0cad587d32b798c">d32b798c</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Sub Query - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Sub Query" (ID: <code class="nb-rule-id" title="6ec5ecf52c094330aff99a38743e66b1">743e66b1</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="url-scanner-now-supports-pdf-report-downloads"><a href="/changelog/post/2026-01-14-Download-URL-Scanner-Report-PDF/">URL Scanner now supports PDF report downloads</a></h2>
<p><em>2026-01-14</em></p>
<p>We have expanded the reporting capabilities of the Cloudflare URL Scanner. In addition to existing JSON and HAR exports, users can now generate and download a <strong>PDF report</strong> directly from the Cloudflare dashboard.
This update streamlines how security analysts can share findings with stakeholders who may not have access to the Cloudflare dashboard or specialized tools to parse JSON and HAR files.</p>
<p><strong>Key Benefits:</strong></p>
<ul>
<li>Consolidate scan results, including screenshots, security signatures, and metadata, into a single, portable document</li>
<li>Easily share professional-grade summaries with non-technical stakeholders or legal teams for faster incident response</li>
</ul>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>PDF Export Button:</strong> A new download option is available in the URL Scanner results page within the Cloudflare dashboard</li>
<li><strong>Unified Documentation:</strong> Access all scan details—from high-level summaries to specific security flags—in one offline-friendly file</li>
</ul>
<p>To get started with the URL Scanner and explore our reporting capabilities, visit the <a href="https://developers.cloudflare.com/api/resources/url_scanner/">URL Scanner API documentation</a>.</p>
<hr />


<h2 id="metro-code-field-now-available-in-rules"><a href="/changelog/post/2026-01-12-dma-metro-code-field/">Metro code field now available in Rules</a></h2>
<p><em>2026-01-12</em></p>
<p>The <code>ip.src.metro_code</code> field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.</p>
<p>You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.</p>
<h4 id="2026-01-12-dma-metro-code-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ip.src.metro_code</code></td>
<td>String | null</td>
<td>The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>ip.src.metro_code eq &quot;501&quot;&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/">Fields reference</a>.</p>


<h2 id="cloudflare-threat-events-now-support-stix2-format"><a href="/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/">Cloudflare Threat Events now support STIX2 format</a></h2>
<p><em>2026-01-12</em></p>
<p>We are excited to announce that <strong>Cloudflare Threat Events</strong> now supports the <strong>STIX2 (Structured Threat Information Expression)</strong> format. This was a highly requested feature designed to streamline how security teams consume and act upon our threat intelligence.</p>
<p>By adopting this industry-standard format, you can now integrate Cloudflare's threat events data more effectively into your existing security ecosystem.</p>
<h4 id="2026-01-12-STIX2-available-for-threat-events-api-key-benefits">Key benefits</h4>
<ul>
<li>
<p>Eliminate the need for custom parsers, as STIX2 allows for &quot;out of the box&quot; ingestion into major <strong>Threat Intel Platforms (TIPs)</strong>, <strong>SIEMs</strong>, and <strong>SOAR</strong> tools.</p>
</li>
<li>
<p>STIX2 provides a standardized way to represent relationships between indicators, sightings, and threat actors, giving your analysts a clearer picture of the threat landscape.</p>
</li>
</ul>
<p>For technical details on how to query events using this format, please refer to our <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/">Threat Events API Documentation</a>.</p>
<hr />


<h2 id="waf-release-2026-01-12"><a href="/changelog/post/2026-01-12-waf-release/">WAF Release - 2026-01-12</a></h2>
<p><em>2026-01-12</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="72963b917ef74697b5bde02f48a1841a">48a1841a</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR MAKE_SET/ELT" (ID: <code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Benchmark Function" (ID: <code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2025-12-18"><a href="/changelog/post/2025-12-18-waf-release/">WAF Release - 2025-12-18</a></h2>
<p><em>2025-12-18</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6429f7386b1546cf9dfce631be5ec20c">be5ec20c</code>
</td>
<td>N/A</td>
<td>Atlassian Confluence - Code Injection - CVE:CVE-2021-26084 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Atlassian Confluence - Code Injection - CVE:CVE-2021-26084" (ID: <code class="nb-rule-id" title="e8c550810618437c953cf3a969e0b97a">69e0b97a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9108ddb347b3497e9f9351640d9206e3">0d9206e3</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - Copy - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "PostgreSQL - SQLi - COPY" (ID: <code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cb687d73cc954092b58b90b00cd00ba7">0cd00ba7</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bf30657ffa2a424cbf6570dbcd679ad4">cd679ad4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6df040f716194070a242967cfd181fb3">fd181fb3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="39a4fdc37be948709fa7492e7a95bc3a">7a95bc3a</code>
</td>
<td>N/A</td>
<td>SQLi - Tautology - URI - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Tautology - URI" (ID: <code class="nb-rule-id" title="4c580ea1b5174183b7f5e940b3de2e0a">b3de2e0a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="810e0ffe1dd84e67b159129b432ac90d">432ac90d</code>
</td>
<td>N/A</td>
<td>SQLi - WaitFor Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - WaitFor Function" (ID: <code class="nb-rule-id" title="b16fe708799441dea3049a99d5faba59">d5faba59</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="80690005fef342e0ad6bc9af596c741e">596c741e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit" (ID: <code class="nb-rule-id" title="98e7e08ae64247e2801ca4b388d80772">88d80772</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="eaf11ab80b0d491cbb7186f303b2f3fe">03b2f3fe</code>
</td>
<td>N/A</td>
<td>SQLi - Equation 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Equation" (ID: <code class="nb-rule-id" title="133c6f83cdf14509a4ca6b82a72a6b3a">a72a6b3a</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2025-12-11-emergency"><a href="/changelog/post/2025-12-11-emergency-waf-release/">WAF Release - 2025-12-11 - Emergency</a></h2>
<p><em>2025-12-11</em></p>
<p>This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.</p>
<p><strong>Key Findings</strong></p>
<p>Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>React - DoS - CVE:CVE-2025-55184</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was labeled as Generic – Server Function Resource Exhaustion.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-12-10-emergency"><a href="/changelog/post/2025-12-10-emergency-waf-release/">WAF Release - 2025-12-10 - Emergency</a></h2>
<p><em>2025-12-10</em></p>
<p>This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.</p>
<p><strong>Key Findings</strong></p>
<p>Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bc1aee59731c488ca8b5314615fce168">15fce168</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="cbdd3f48396e4b7389d6efd174746aff">74746aff</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Resource Exhaustion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="increased-waf-payload-limit-for-all-plans"><a href="/changelog/post/2025-12-05-rcs-vuln/">Increased WAF payload limit for all plans</a></h2>
<p><em>2025-12-05</em></p>
<p>Cloudflare WAF now inspects request-payload size of up to 1 MB across all plans to enhance our detection capabilities for React RCE (CVE-2025-55182).</p>
<p><strong>Key Findings</strong></p>
<p>React payloads commonly have a default maximum size of 1 MB. Cloudflare WAF previously inspected up to 128 KB on Enterprise plans, with even lower limits on other plans.</p>
<p><strong>Update:</strong> We later reinstated the maximum request-payload size the Cloudflare WAF inspects. Refer to <a href="/changelog/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a> for details.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/3/">Previous</a><span>Page 4 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/5/">Next</a></nav>
