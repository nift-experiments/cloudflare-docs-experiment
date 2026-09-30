---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/
  description: Reference information for Network session analytics in Zero Trust analytics.
  full_title: Network session analytics · Cloudflare One docs
  head_html: <title>Network session analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Network session analytics in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/index.md"><meta property="og:title" content="Network session analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Network session analytics in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/#page","headline":"Network session analytics \u00b7 Cloudflare One docs","description":"Reference information for Network session analytics in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/analytics/network-sessions/
  schema: 1
---
<p>The Network session analytics dashboard provides visibility into your Cloudflare One traffic patterns. This dashboard helps you understand how traffic flows through your network, including on-ramps (how traffic enters Cloudflare, such as the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a>, <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>, or Cloudflare Tunnel) and off-ramps (how traffic exits Cloudflare, such as the public Internet or a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>).</p>
<p>The dashboard is based on the <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust network sessions Logpush dataset</a>. For definitions on any field, refer to the dataset schema documentation.</p>
<p>To review Network session analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong>Network session analytics</strong>.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="use-cases">Use cases</h2>
<p>The Network session analytics dashboard helps you:</p>
<ul>
<li><strong>Understand traffic patterns</strong>: Visualize how traffic flows through your network infrastructure.</li>
<li><strong>Monitor bandwidth usage</strong>: Track upload, download, and total bytes transferred across your network.</li>
<li><strong>Identify connection issues</strong>: Analyze connection close reasons to troubleshoot network problems.</li>
<li><strong>Track user and device activity</strong>: Monitor unique users and devices accessing your network.</li>
</ul>
<h2 id="provided-analytics">Provided analytics</h2>
<h3 id="summary-metrics">Summary metrics</h3>
<ul>
<li><strong>Session count</strong>: Total number of network sessions. Each session represents an individual TCP, UDP, ICMP, or ICMPv6 flow that passes through Gateway.</li>
<li><strong>Bytes total</strong>: Total bytes transferred (upload + download)</li>
<li><strong>Unique users</strong>: Number of distinct users</li>
</ul>
<h3 id="traffic-by-location">Traffic by location</h3>
<ul>
<li><strong>World map</strong>: Geographic visualization of network traffic by the Cloudflare data center where traffic entered the network (ingress) and where it exited (egress)</li>
<li><strong>Location list</strong>: Top Cloudflare data center locations by ingress and egress session count with accompanying graph</li>
<li><strong>Change</strong>: Shows the total change across ingress and egress for each location</li>
</ul>
<h3 id="top-analytics">Top analytics</h3>
<ul>
<li><strong>Top protocols</strong>: Most used network protocols (TCP, UDP, ICMP, ICMPv6)</li>
<li><strong>Top connection close reasons</strong>: Common reasons for session termination:
<ul>
<li>Client closed</li>
<li>Origin closed</li>
<li>Client idle timeout</li>
<li>Client error</li>
<li>Unknown</li>
<li>Client TLS error</li>
<li>Origin unreachable</li>
<li>Too many new sessions for user</li>
<li>Origin TLS error</li>
<li>Origin unroutable</li>
</ul>
</li>
</ul>
<p>For the full list of reasons for session termination, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#connectionclosereason">ConnectionCloseReason</a>.</p>
<h3 id="troubleshoot-session-limit-errors">Troubleshoot session limit errors</h3>
<p>Session limit close reasons identify the type and scope of a limit. Reasons containing <code>ACTIVE_SESSIONS</code> indicate too many concurrent sessions. Reasons containing <code>NEW_SESSIONS</code> indicate that sessions are being created too quickly. <code>FOR_ACCOUNT</code> reasons aggregate sessions for the account on the Cloudflare server enforcing the limit and can affect multiple users connected to that server. <code>FOR_USER</code> reasons apply to one user.</p>
<p>Use <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>, not Gateway activity logs, to investigate these errors. Filter by <code>ConnectionCloseReason</code>, then correlate <code>SessionStartTime</code> and <code>SessionID</code> with fields such as <code>Email</code>, <code>UserID</code>, <code>DeviceID</code>, <code>SourceIP</code>, <code>OriginIP</code>, <code>OriginPort</code>, <code>Protocol</code>, and <code>ConnectionReuse</code>.</p>
<p>Reduce automatic retries and connection churn in the affected application. Reuse connections when the application and protocol support it. If expected sustained traffic continues to produce these errors, contact your account team or <a href="/cloudflare-one/troubleshooting/contact-support/">Cloudflare Support</a> for review.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust network sessions Logpush dataset</a>: View detailed logs for individual network sessions.</li>
<li><a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>: Configure policies that apply to network traffic.</li>
</ul>
