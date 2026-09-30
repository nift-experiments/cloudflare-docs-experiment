---
cp9:
  canonical: https://developers.cloudflare.com/network/websockets/
  description: Proxy WebSocket connections through Cloudflare's network.
  full_title: WebSockets · Cloudflare Network settings docs
  head_html: <title>WebSockets · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Proxy WebSocket connections through Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/network/websockets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/websockets/index.md"><meta property="og:title" content="WebSockets · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Proxy WebSocket connections through Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/network/websockets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/websockets/#page","headline":"WebSockets \u00b7 Cloudflare Network settings docs","description":"Proxy WebSocket connections through Cloudflare's network.","url":"https://developers.cloudflare.com/network/websockets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network/websockets/
  schema: 1
---
<p>Cloudflare supports proxied WebSocket connections without additional configuration.</p>
<h2 id="background">Background</h2>
<p>WebSockets are open connections sustained between the client and the origin server. Inside a WebSockets connection, the client and the origin can pass data back and forth without having to reestablish sessions. This makes exchanging data within a WebSockets connection fast. WebSockets are often used for real-time applications such as live chat and gaming.</p>
<h2 id="enable-websockets">Enable WebSockets</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/664.md")
</div></div>
<h2 id="compatibility-notes">Compatibility notes</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Compatible</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/argo-smart-routing/">Argo</a></td>
<td>No</td>
<td>Argo is not compatible with WebSockets.</td>
</tr>
<tr>
<td><a href="/ssl/">SSL</a></td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/waf/">WAF</a></td>
<td>Yes*</td>
<td>The initial HTTP 101 request is subject to WAF managed rules, custom rules, rate limiting rules, and other WAF features like any other WebSockets connection. However, once a connection has been established, the WAF does not perform any further inspections.</td>
</tr>
<tr>
<td><a href="/workers/examples/websockets/">Workers</a></td>
<td>Yes</td>
<td>You can also use <a href="/durable-objects/">Durable Objects</a> as an endpoint for WebSocket sessions, giving you full control over messages sent to and from clients.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/661.md")
</aside>
<h2 id="availability">Availability</h2>
<p>WebSockets are supported on all Cloudflare plans.</p>
<h2 id="requests-and-bandwidth-measurement">Requests and Bandwidth measurement</h2>
<p>Given the nature of WebSocket connections, you may notice they differ from typical HTTP traffic in terms of requests and bandwidth usage. If you are an Enterprise customer, it is important to consider how Cloudflare measures requests and bandwidth to accurately estimate your usage.</p>
<p>Cloudflare measures a single WebSocket connection in the following way:</p>
<ul>
<li>
<p><strong>Requests</strong>: Cloudflare recognizes only the initial upgrade request per WebSocket connection as an HTTP request. Even though you can send a bidirectional message stream through the established WebSocket connection, it will be counted as a single long-lived HTTP request.</p>
</li>
<li>
<p><strong>Bandwidth</strong>: Cloudflare measures data transfer sent from Cloudflare to the client. This typically means that messages from the WebSocket server behind Cloudflare to the WebSocket client are counted towards bandwidth usage.</p>
</li>
</ul>
<p>Once a WebSocket connection is closed, you can view your aggregated WebSocket usage through <a href="/analytics/account-and-zone-analytics/zone-analytics/#traffic">Traffic Analytics</a>, the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, and <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests logs</a>.</p>
<h2 id="technical-note">Technical note</h2>
<p>When Cloudflare releases new code to its global network, we may restart servers, which terminates WebSockets connections.</p>
<h3 id="best-practices">Best practices</h3>
<ul>
<li>Implement a <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_servers#pings_and_pongs_the_heartbeat_of_websockets">keepalive</a>.</li>
<li>Review and then remove or extend timeout settings on the origin and/or on the client.</li>
</ul>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>Investigating issues with Websocket can be facilitated with client tools like <a href="https://github.com/websockets/wscat">wscat</a>.
Being able to reproduce an issue on a single URL with a minimalistic tool helps narrowing down the issue.</p>
<p>The <code>EdgeStartTimestamp</code> and <code>EdgeStopTimestamp</code> fields in <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests logs</a> represent the duration of the WebSocket connection (they do not represent the initial HTTP connection).</p>
<h2 id="connection-limits">Connection limits</h2>
<h3 id="idle-timeout">Idle timeout</h3>
<p>Cloudflare will close a WebSocket connection when no data is transmitted in either direction for a period of time. Enterprise customers can contact their account team to configure a custom idle timeout. To keep long-lived connections alive during periods of inactivity, implement a client-side heartbeat (ping/pong) mechanism.</p>
<h3 id="session-affinity-for-load-balanced-websocket-origins">Session affinity for load-balanced WebSocket origins</h3>
<p>If your WebSocket origin is behind a Cloudflare Load Balancer, turn on <strong>Session affinity</strong> to ensure all requests from the same client are routed to the same origin server. Without session affinity, a WebSocket reconnect may land on a different origin that does not have the session state.</p>
