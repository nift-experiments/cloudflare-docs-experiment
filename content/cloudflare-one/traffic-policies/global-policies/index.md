---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/
  description: Reference information for Global policies in Gateway.
  full_title: Global policies · Cloudflare One docs
  head_html: <title>Global policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Global policies in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/index.md"><meta property="og:title" content="Global policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Global policies in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/#page","headline":"Global policies \u00b7 Cloudflare One docs","description":"Reference information for Global policies in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/global-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/global-policies/
  schema: 1
---
<p>Cloudflare Zero Trust applies a set of global policies to all accounts. These policies prevent you from accidentally blocking Cloudflare services that Zero Trust depends on, such as the dashboard, API, and client registration.</p>
<p>Zero Trust logs prepend an identifier to global policy names. For example, matches for the global policy <strong>Allow Zero Trust Services</strong> will appear in your logs with the name <strong>Global Policy - Allow Zero Trust Services</strong>.</p>
<p>The following policies are sorted by <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">order of precedence</a> within each policy type.</p>
<h2 id="dns-resolution-policies">DNS resolution policies</h2>
<p>Gateway enforces global DNS and resolver policies before any other policies. This ensures the traffic is not blocked by user policies and gets resolved with Cloudflare's public DNS resolver, <a href="/1.1.1.1/">1.1.1.1</a>. Each global DNS policy evaluates traffic based on the domain in the query.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>ID</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow DNS queries for cloudflareclient.com domain</td>
<td><code>00000001-e139-4a1b-90d5-698d8fa371e0</code></td>
<td><code>cloudflareclient.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve cloudflareclient.com through 1.1.1.1</td>
<td><code>00000001-e738-4554-823b-0b2c75af2c66</code></td>
<td><code>cloudflareclient.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for content.browser.run domain</td>
<td><code>00000001-9bff-4d83-a9e4-e5ed321fe0b9</code></td>
<td><code>content.browser.run</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve content.browser.run through 1.1.1.1</td>
<td><code>00000001-0df5-472b-80c0-02888e7167ee</code></td>
<td><code>content.browser.run</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for edge.browser.run and cloudflarebrowser.com domains</td>
<td><code>00000001-e2f1-4e99-bab3-91df88879587</code></td>
<td><code>edge.browser.run</code> and <code>cloudflarebrowser.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve edge.browser.run and cloudflarebrowser.com through 1.1.1.1</td>
<td><code>00000001-b103-44c6-a114-7a784cdf3fb7</code></td>
<td><code>edge.browser.run</code> and <code>cloudflarebrowser.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for help.teams.cloudflare.com and help.one.cloudflare.com domains</td>
<td><code>00000001-b2fc-46db-b0f1-69ef3553bd7a</code></td>
<td><code>help.teams.cloudflare.com</code> and <code>help.one.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve help.teams.cloudflare.com and help.one.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-ce13-486a-b006-ba0435ccb013</code></td>
<td><code>help.teams.cloudflare.com</code> and <code>help.one.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for cloudflare-gateway.com domain</td>
<td><code>00000001-e83d-492b-995e-351970cd5e8e</code></td>
<td><code>cloudflare-gateway.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve cloudflare-gateway.com through 1.1.1.1</td>
<td><code>00000001-d9bc-4913-a2f5-905dbb3ecf9a</code></td>
<td><code>cloudflare-gateway.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for cloudflarestatus.com domain</td>
<td><code>00000001-78da-4f8a-b9ee-76563f1ec46b</code></td>
<td><code>cloudflarestatus.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve cloudflarestatus.com through 1.1.1.1</td>
<td><code>00000001-4d1d-43a3-9015-c49fc3a6da31</code></td>
<td><code>cloudflarestatus.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for nel.cloudflare.com domain</td>
<td><code>00000001-af28-4afa-8987-eadc21187e14</code></td>
<td><code>nel.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve nel.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-0034-45a0-8333-f339451fba46</code></td>
<td><code>nel.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for api.cloudflare.com domain</td>
<td><code>00000001-5eea-4932-8dd5-8e1ec9770396</code></td>
<td><code>api.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve api.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-4f0c-4f86-9b96-5d26123a194b</code></td>
<td><code>api.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for one.dash.cloudflare.com domain</td>
<td><code>00000001-0f75-48a9-b3e1-925a974d2b65</code></td>
<td><code>one.dash.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve one.dash.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-3d84-41a6-bc84-3014685c0d81</code></td>
<td><code>one.dash.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for one.dash.cloudflare.com domain</td>
<td><code>00000001-a9fd-40de-a662-51d3a3ae0ad8</code></td>
<td><code>one.dash.cloudflare.com</code> and <code>one.dash.fed.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve one.dash.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-70f2-4eea-b711-201bca434ed4</code></td>
<td><code>one.dash.cloudflare.com</code> and <code>one.dash.fed.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for dash.cloudflare.com domain</td>
<td><code>00000001-0c2a-4b31-8606-3e5a1d87c1bf</code></td>
<td><code>dash.cloudflare.com</code> and <code>dash.fed.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve dash.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-c47f-41f3-b234-d66c82b8d422</code></td>
<td><code>dash.cloudflare.com</code> and <code>dash.fed.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for cloudflareportal.com, cloudflareok.com and cloudflarecp.com domains</td>
<td><code>00000001-1c6c-4793-b48f-799eee6e0e31</code></td>
<td><code>cloudflareportal.com</code>, <code>cloudflareok.com</code>, and <code>cloudflarecp.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve cloudflareportal.com, cloudflareok.com and cloudflarecp.com through 1.1.1.1</td>
<td><code>00000001-8c35-4d7d-9dbb-cb7350375b7b</code></td>
<td><code>cloudflareportal.com</code>, <code>cloudflareok.com</code>, and <code>cloudflarecp.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for cloudflareaccess.com domain</td>
<td><code>00000001-d738-4dad-bac4-1a50201d9503</code></td>
<td><code>cloudflareaccess.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve cloudflareaccess.com through 1.1.1.1</td>
<td><code>00000001-4404-4572-80f6-f7b098909460</code></td>
<td><code>cloudflareaccess.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for blocked.teams.cloudflare.com domain</td>
<td><code>00000001-76f4-4438-b8ab-a9da53f4a2f1</code></td>
<td><code>blocked.teams.cloudflare.com</code> and <code>blocked.teams.fed.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve blocked.teams.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-af3c-458f-aeb2-b3bb5d3fe1d5</code></td>
<td><code>blocked.teams.cloudflare.com</code> and <code>blocked.teams.fed.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for developers.cloudflare.com domain</td>
<td><code>00000001-4263-4808-8457-4d4329c91f66</code></td>
<td><code>developers.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve developers.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-9f91-4462-9270-78beca5b4dbc</code></td>
<td><code>developers.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS queries for speed.cloudflare.com domain</td>
<td><code>00000001-4fc0-4286-b783-6c442adda171</code></td>
<td><code>speed.cloudflare.com</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve speed.cloudflare.com through 1.1.1.1</td>
<td><code>00000001-ec51-4471-9e78-bd47d46a3002</code></td>
<td><code>speed.cloudflare.com</code></td>
<td>resolve</td>
</tr>
<tr>
<td>Allow DNS requests to browser-rendered Access Apps</td>
<td><code>00000001-1232-4a9f-a165-1e8ed59483c4</code></td>
<td><code>*.zero-trust-apps.cfdata.org</code>, <code>*.zero-trust-apps-staging.cfdata.org</code>, <code>*.zero-trust-apps.fed.cfdata.org</code>, or <code>*.zero-trust-apps-staging.fed.cfdata.org</code></td>
<td>allow</td>
</tr>
<tr>
<td>Resolve browser-rendered Access Apps domains through 1.1.1.1</td>
<td><code>00000001-9461-43c7-ba63-d0fdf9376bd4</code></td>
<td><code>*.zero-trust-apps.cfdata.org</code>, <code>*.zero-trust-apps-staging.cfdata.org</code>, <code>*.zero-trust-apps.fed.cfdata.org</code>, or <code>*.zero-trust-apps-staging.fed.cfdata.org</code></td>
<td>resolve</td>
</tr>
</tbody>
</table>
<h2 id="network-proxy-policies">Network proxy policies</h2>
<table>
<thead>
<tr>
<th>Name</th>
<th>ID</th>
<th>Criteria</th>
<th>Value</th>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow CF Network Error Logging L4</td>
<td><code>00000001-e4af-4b82-8f8c-c79c1d5d212e</code></td>
<td>Hostname</td>
<td><code>*.nel.cloudflare.com</code></td>
<td>allow</td>
<td>Allows SNI domains for Cloudflare One Client registration.</td>
</tr>
<tr>
<td>Allow CF Client</td>
<td><code>00000001-8c3d-4e27-a01b-af8418000077</code></td>
<td>Hostname</td>
<td><code>*.cloudflareclient.com</code> and <code>*.fed.cloudflareclient.com</code></td>
<td>allow</td>
<td>Allows Zero Trust client.</td>
</tr>
<tr>
<td>Allow Gateway Proxy PAC</td>
<td><code>00000001-776e-438d-9856-987d7053762b</code></td>
<td>Hostname</td>
<td><code>*.cloudflare-gateway.com</code> and <code>*.fed.cloudflare-gateway.com</code></td>
<td>allow</td>
<td>Allows Gateway proxy with <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a>.</td>
</tr>
<tr>
<td>Allow Zero Trust Services</td>
<td><code>00000001-e1e8-421b-a0fe-895397489f28</code></td>
<td>Hostname</td>
<td><code>one.dash.cloudflare.com</code>, <code>help.teams.cloudflare.com</code>, <code>blocked.teams.cloudflare.com</code>, <code>blocked.teams.fed.cloudflare.com</code>, <code>api.cloudflare.com</code>, <code>api.fed.cloudflare.com</code>, <code>cloudflarestatus.com</code>, <code>www.cloudflarestatus.com</code>, <code>one.dash.cloudflare.com</code>, <code>one.dash.fed.cloudflare.com</code>, <code>help.one.cloudflare.com</code>, <code>dash.cloudflare.com</code>, <code>dash.fed.cloudflare.com</code>, and <code>developers.cloudflare.com</code></td>
<td>allow</td>
<td>Allows Cloudflare Zero Trust services.</td>
</tr>
<tr>
<td>Allow Access Apps L4</td>
<td><code>00000001-daa2-41e2-8a88-698af4066951</code></td>
<td>Hostname</td>
<td><code>*.cloudflareaccess.com</code> and <code>*.fed.cloudflareaccess.com</code></td>
<td>allow</td>
<td>Allows <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> applications.</td>
</tr>
<tr>
<td>Allow HTTP requests to browser-rendered Access Apps</td>
<td><code>00000001-1f93-4476-8f92-9aa4407d1c5f</code></td>
<td>Hostname</td>
<td><code>*.zero-trust-apps.cfdata.org</code>, <code>*.zero-trust-apps-staging.cfdata.org</code>, <code>*.zero-trust-apps.fed.cfdata.org</code>, or <code>*.zero-trust-apps-staging.fed.cfdata.org</code></td>
<td>allow</td>
<td>Allows Cloudflare Access terminal applications <a href="/cloudflare-one/access-controls/applications/non-http/browser-rendering/#ssh-and-vnc">rendered in a browser</a>.</td>
</tr>
</tbody>
</table>
<h2 id="http-inspection-policies">HTTP inspection policies</h2>
<table>
<thead>
<tr>
<th>Name</th>
<th>ID</th>
<th>Criteria</th>
<th>Value</th>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prevent Account Change Block</td>
<td><code>00000001-d1f2-461a-8253-501c8d882a15</code></td>
<td>Hostname</td>
<td><code>*.cloudflareclient.com</code> and <code>*.fed.cloudflareclient.com</code>; not <code>notifications.cloudflareclient.com</code> or <code>notifications.fed.cloudflareclient.com</code></td>
<td>bypass</td>
<td>Ensures users cannot accidentally block themselves from making account changes.</td>
</tr>
<tr>
<td>Bypass RBI Assets</td>
<td><code>00000001-df61-4068-aa6c-0f684c3cd4e6</code></td>
<td>Hostname</td>
<td><code>*.content.browser.run</code></td>
<td>bypass</td>
<td>Required for <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>.</td>
</tr>
<tr>
<td>Inspect RBI Urls</td>
<td><code>00000001-3faa-4f59-98d4-0f6d6af4b6d0</code></td>
<td>Hostname</td>
<td><code>*.edge.browser.run</code> and <code>*.cloudflarebrowser.com</code></td>
<td>bypass</td>
<td>Required for Browser Isolation.</td>
</tr>
<tr>
<td>Allow Gateway Help Page</td>
<td><code>00000001-8e9a-4429-b3c2-d267d0ce6114</code></td>
<td>Hostname</td>
<td><code>help.teams.cloudflare.com</code> and <code>help.one.cloudflare.com</code></td>
<td>allow</td>
<td>Used by the Cloudflare One Client to check if Gateway is on by inspecting the certificate and checking if it is properly installed on the client device.</td>
</tr>
<tr>
<td>Allow Gateway Services</td>
<td><code>00000001-346f-4710-b444-eb62e369b5f7</code></td>
<td>Capability</td>
<td>Gateway Block Page</td>
<td>allow</td>
<td>Ensures HTTP requests to render the Gateway block page are always allowed.</td>
</tr>
<tr>
<td>Bypass Gateway DNS</td>
<td><code>00000001-d9c0-46b0-8704-2ea5b9d7bdfc</code></td>
<td>Hostname</td>
<td><code>*.cloudflare-gateway.com</code> and <code>*.fed.cloudflare-gateway.com</code></td>
<td>bypass</td>
<td>Ensures requests to the <code>cloudflare-gateway.com</code> DNS endpoint will not be inspected.</td>
</tr>
<tr>
<td>Bypass CF Status</td>
<td><code>00000001-5399-4b71-a9fc-d4d90ccf0758</code></td>
<td>Hostname</td>
<td><code>*.cloudflarestatus.com</code></td>
<td>bypass</td>
<td>Bypasses <code>cloudflarestatus.com</code> so users can reach the status page in case of a Gateway outage.</td>
</tr>
<tr>
<td>Bypass CF Network Error Logging</td>
<td><code>00000001-dfe0-4737-8d1e-8191e8f637df</code></td>
<td>Hostname</td>
<td><code>*.nel.cloudflare.com</code></td>
<td>bypass</td>
<td>Bypasses <code>*.nel.cloudflarestatus.com</code> for Cloudflare's network error logging feature.</td>
</tr>
<tr>
<td>Bypass CF API</td>
<td><code>00000001-a424-43fb-b1f1-d3eb35ed7ddd</code></td>
<td>Hostname</td>
<td><code>api.cloudflare.com</code> and <code>api.fed.cloudflare.com</code></td>
<td>bypass</td>
<td>Bypasses Cloudflare's API endpoint.</td>
</tr>
<tr>
<td>Prevent ZT Dashboard Lockout</td>
<td><code>00000001-d38e-42db-96fe-60613b6b308f</code></td>
<td>Hostname</td>
<td><code>dash.teams.cloudflare.com</code>, <code>one.dash.cloudflare.com</code>, and <code>one.dash.fed.cloudflare.com</code></td>
<td>bypass</td>
<td>Prevents users from being locked out of the Zero Trust dashboard.</td>
</tr>
<tr>
<td>Bypass CF Dashboard</td>
<td><code>00000001-d343-4ded-908e-b3fe43c5e61e</code></td>
<td>Hostname</td>
<td><code>*.dash.cloudflare.com</code> and <code>*.dash.fed.cloudflare.com</code></td>
<td>bypass</td>
<td>Bypasses the Cloudflare dashboard and subdomains.</td>
</tr>
<tr>
<td>Bypass Zero Trust Captive Portal Sites</td>
<td><code>00000001-8b62-4367-919e-5c160a06ddf7</code></td>
<td>Hostname</td>
<td><code>cloudflareportal.com</code>, <code>cloudflareok.com</code>, and <code>cloudflarecp.com</code></td>
<td>bypass</td>
<td>Bypasses the Zero Trust captive portal detection sites.</td>
</tr>
<tr>
<td>Bypass OCSP</td>
<td><code>00000001-34ce-47c7-ad0f-199f46eba194</code></td>
<td>Application</td>
<td>Online Certificate Status Protocol</td>
<td>bypass</td>
<td>Enables OCSP stapling.</td>
</tr>
<tr>
<td>Allow Access Apps L7</td>
<td><code>00000001-8d6b-4951-8a18-3bbc9010976c</code></td>
<td>Hostname</td>
<td><code>*.cloudflareaccess.com</code> and <code>*.fed.cloudflareaccess.com</code></td>
<td>allow</td>
<td>Allows Cloudflare Access applications.</td>
</tr>
<tr>
<td>Prevent Block Page Loop</td>
<td><code>00000001-48b1-4ade-93c1-f0f3759dc19c</code></td>
<td>Hostname</td>
<td><code>blocked.teams.cloudflare.com</code> and <code>blocked.teams.fed.cloudflare.com</code></td>
<td>bypass</td>
<td>Prevents an infinite loop on the Gateway block page.</td>
</tr>
<tr>
<td>Always Blocked Categories</td>
<td><code>00000001-bed5-462e-b0f1-2e2c3555e9f7</code></td>
<td>Content Category</td>
<td><a href="/cloudflare-one/traffic-policies/domain-categories/#category-and-subcategory-ids">Child Abuse category</a></td>
<td>block</td>
<td>Blocks child abuse materials (CSAM).</td>
</tr>
<tr>
<td>Don't Isolate RBI Help Pages</td>
<td><code>00000001-1a18-431f-9c9d-bce431f1002a</code></td>
<td>Hostname</td>
<td><code>developers.cloudflare.com</code> and <code>help.cloudflarebrowser.com</code></td>
<td>noisolate</td>
<td>Prevents browser isolation of Cloudflare developer docs and help pages to help users troubleshoot configuration issues.</td>
</tr>
<tr>
<td>Don't AV Scan CF Speed</td>
<td><code>00000001-c194-408f-87dd-9a366ce76e12</code></td>
<td>Hostname</td>
<td><code>speed.cloudflare.com</code></td>
<td>noscan</td>
<td>Allows files transferred by the Cloudflare speed test.</td>
</tr>
</tbody>
</table>
