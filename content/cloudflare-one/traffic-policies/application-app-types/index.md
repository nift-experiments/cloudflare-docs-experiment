---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/
  description: Reference information for Applications and app types in Gateway.
  full_title: Applications and app types · Cloudflare One docs
  head_html: <title>Applications and app types · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Applications and app types in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/index.md"><meta property="og:title" content="Applications and app types · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Applications and app types in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/#page","headline":"Applications and app types \u00b7 Cloudflare One docs","description":"Reference information for Applications and app types in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/application-app-types/
  schema: 1
---
<p>Gateway allows you to create DNS, Network, and HTTP policies based on applications and application types. Because a single application often spans multiple hostnames, selecting an application by name is easier than writing separate rules for each hostname. You can select individual applications or application types to filter specific traffic on your network.</p>
<h2 id="applications">Applications</h2>
<p>When you choose the <em>Application</em> selector in a Gateway policy builder, the <strong>Value</strong> field will include all supported applications and their respective app types. Alternatively, you can use the <a href="/api/resources/zero_trust/subresources/gateway/subresources/app_types/methods/list/">Gateway API</a> to fetch a list of applications, app types, and ID numbers.</p>
<p>To manage a consolidated list of applications across Cloudflare One, you can use the <a href="/cloudflare-one/team-and-resources/app-library/">Application Library</a>.</p>
<h2 id="app-types">App types</h2>
<p>Gateway sorts applications into the following app type groups:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Artificial Intelligence</td>
<td>AI assistance applications</td>
</tr>
<tr>
<td>Business</td>
<td>Applications used for general business purposes</td>
</tr>
<tr>
<td>Collaboration &amp; Online Meetings</td>
<td>Business communication and collaboration applications</td>
</tr>
<tr>
<td>Dating</td>
<td>Online dating applications</td>
</tr>
<tr>
<td>Development</td>
<td>Software development and development operations applications</td>
</tr>
<tr>
<td>Education</td>
<td>Applications used for educational purposes and e-learning</td>
</tr>
<tr>
<td>Email</td>
<td>Email applications</td>
</tr>
<tr>
<td>Entertainment &amp; Events</td>
<td>Applications used for entertainment content and event information</td>
</tr>
<tr>
<td>Encrypted DNS</td>
<td>DNS encryption applications</td>
</tr>
<tr>
<td>File Sharing</td>
<td>File sharing applications</td>
</tr>
<tr>
<td>Finance &amp; Accounting</td>
<td>Financial and accounting applications</td>
</tr>
<tr>
<td>Food &amp; Drink</td>
<td>Applications related to food delivery and recipe services</td>
</tr>
<tr>
<td>Gaming</td>
<td>Games and gaming applications</td>
</tr>
<tr>
<td>Health &amp; Fitness</td>
<td>Applications used for health monitoring and fitness tracking</td>
</tr>
<tr>
<td>Human Resources</td>
<td>Employee management applications and workforce tools</td>
</tr>
<tr>
<td>Instant Messaging</td>
<td>Instant messaging applications</td>
</tr>
<tr>
<td>IT Management</td>
<td>IT deployment management applications</td>
</tr>
<tr>
<td>Legal</td>
<td>Legal tools and applications</td>
</tr>
<tr>
<td>Lifestyle</td>
<td>Applications related to lifestyle and personal interests</td>
</tr>
<tr>
<td>Music &amp; Audio Streaming</td>
<td>Applications used for streaming music and audio</td>
</tr>
<tr>
<td>Navigation</td>
<td>Applications used for maps and navigation services</td>
</tr>
<tr>
<td>News, Books, &amp; Magazines</td>
<td>Applications delivering news, books, and magazine content</td>
</tr>
<tr>
<td>Photography &amp; Graphic Design</td>
<td>Applications used for photography and graphic design</td>
</tr>
<tr>
<td>Productivity</td>
<td>Business and productivity applications</td>
</tr>
<tr>
<td>Public Cloud</td>
<td>Public cloud infrastructure management applications</td>
</tr>
<tr>
<td>Sales &amp; Marketing</td>
<td>Sales and marketing applications</td>
</tr>
<tr>
<td>Search Engines</td>
<td>Web search engines and applications</td>
</tr>
<tr>
<td>Security</td>
<td>Information security applications, including <span class="nb-glossary-tooltip" title="shadow IT">shadow IT</span></td>
</tr>
<tr>
<td>Shopping</td>
<td>Online shopping applications</td>
</tr>
<tr>
<td>Social Networking</td>
<td>Social networking applications</td>
</tr>
<tr>
<td>Sports</td>
<td>Sports streaming and news applications</td>
</tr>
<tr>
<td>Travel</td>
<td>Travel related applications</td>
</tr>
<tr>
<td>Video Streaming &amp; Editing</td>
<td>Applications used for streaming and editing video</td>
</tr>
<tr>
<td><a href="#do-not-inspect-applications">Do Not Inspect</a></td>
<td>Applications incompatible with the TLS certificate required by the <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a></td>
</tr>
</tbody>
</table>
<h2 id="application-hostnames">Application hostnames</h2>
<p>An application like Google Drive uses its own hostnames (for example, <code>drive.google.com</code>) and shared resources used by other applications (for example, <code>accounts.google.com</code> for login). Gateway separates these into <a href="#hostnames">hostnames</a> and <a href="#support-hostnames">support hostnames</a> so you can control the behavior of each application independently.</p>
<h3 id="hostnames">Hostnames</h3>
<p>Hostnames are domains that are core to the application and not <a href="#overlapping-hostnames">used by other applications</a>. These are the domains that Gateway blocks when you block an application. The App Library surfaces these hostnames in the <a href="/cloudflare-one/team-and-resources/app-library/#overview">Hostnames table</a> for an application.</p>
<h3 id="support-hostnames">Support hostnames</h3>
<p>Support hostnames are shared resources that applications depend on for content delivery, authentication, or third-party integrations. Because multiple applications share these hostnames, blocking them can cause unexpected side effects.</p>
<p>For example, assume that <code>file-sharing-service.com</code> relies on <code>content-delivery.com</code>. If you allow access to <code>file-sharing-service.com</code> and its associated subdomains but not <code>content-delivery.com</code>, some of the functionality of <code>file-sharing-service.com</code> may break when Gateway matches the traffic.</p>
<p>To prevent this, Gateway only uses support hostnames in Allow policies — it will allow support hostname connections but will not block them. For example, many Google applications use <code>accounts.google.com</code> for authentication. If you create an Allow policy for an application that lists <code>accounts.google.com</code> as a support hostname, Gateway will allow both <code>accounts.google.com</code> and the application's own domains.</p>
<h2 id="application-controls">Application controls</h2>
<p>When you use the <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls"><em>Application</em> selector</a> in an HTTP policy with the <em>is</em> operator, you can choose specific actions and operations to match application traffic. Supported applications and operations include:</p>
<div class="nb-data-component" data-cf-component="GranularControlApplicationsList"></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/">Application Granular Controls</a>.</p>
<h2 id="usage">Usage</h2>
<h3 id="overlapping-hostnames">Overlapping hostnames</h3>
<p>Overlapping hostnames are most common for vendors with many applications, such as Google or Meta. When you use the Application selector in Gateway policies, actions taken by Gateway will be limited to the specific application defined. Gateway will also log other applications that use the same hostnames, but it will not take action unless the application was matched by the policy. For example, both the Facebook and Facebook Messenger apps use the <code>chat-e2ee.facebook.com</code> hostname. When evaluating traffic to the Facebook Messenger app, Gateway will only take action on Facebook Messenger traffic but may log both the Facebook and Facebook Messenger apps.</p>
<p>To ensure Gateway evaluates traffic with your desired precedence, order your most specific policies with the highest priority according to <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#priority-within-a-policy-builder">order of precedence</a>.</p>
<h3 id="do-not-inspect-applications">Do Not Inspect applications</h3>
<p>Gateway automatically groups applications incompatible with TLS decryption into the <em>Do Not Inspect</em> app type. As Cloudflare identifies incompatible applications, Gateway will periodically update this app type to add new applications. To ensure Gateway does not intercept any current or future incompatible traffic, you can <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">create a Do Not Inspect HTTP policy</a> with the entire <em>Do Not Inspect</em> app type selected.</p>
<p>When managing applications with the <a href="/cloudflare-one/team-and-resources/app-library/">Application Library</a>, Do Not Inspect applications will appear under the corresponding application. For example, the App Library will group <em>Google Drive (Do Not Inspect)</em> under <strong>Google Drive</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="install-cloudflare-certificate-manually-to-allow-tls-decryption">Install Cloudflare certificate manually to allow TLS decryption</h3>
@markup("md", "content/.markup/bodies/4423.md")
</aside>
<h4 id="tls-decryption-limitations">TLS decryption limitations</h4>
<p>Applications can be incompatible with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> for various reasons:</p>
<ul>
<li>
<div class="nb-glossary-definition"><p><strong>Certificate pinning</strong>: Certificate pinning is a security mechanism used to prevent on-path attacks on the Internet by hardcoding information about the certificate that the application expects to receive. If the wrong certificate is received, even if it is trusted by the system, the application will refuse to connect.</p></div>
</li>
<li>
<p><strong>Non-web traffic</strong>: Some applications send non-web traffic over TLS, such as Session Initiation Protocol (SIP) for voice and video calls and Extensible Messaging and Presence Protocol (XMPP) for chat. Gateway cannot inspect these protocols.</p>
</li>
</ul>
<h4 id="microsoft-365-integration">Microsoft 365 integration</h4>
<p>To optimize performance for Microsoft 365 applications and services, you can bypass TLS decryption by turning on the Microsoft 365 traffic integration. This will create a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect policy</a> for all <a href="https://docs.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-ip-web-service">Microsoft 365 domains and IP addresses</a> specified by Microsoft. This policy also uses Cloudflare intelligence to identify other Microsoft 365 traffic not explicitly defined.</p>
<p>To turn on the Microsoft 365 integration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong> &gt; <strong>Policy settings</strong>.</li>
<li>In <strong>Bypass decryption of Microsoft 365 traffic</strong>, select <strong>Create policy</strong>.</li>
<li>To verify the policy was created, select <strong>View policy</strong>. Alternatively, go to <strong>Traffic policies</strong> &gt; <strong>HTTP policies</strong>. A policy named Microsoft 365 Auto Generated will be enabled in your list.</li>
</ol>
<p>All future Microsoft 365 traffic will bypass Gateway logging and filtering. To disable this behavior, turn off or delete the policy.</p>
<h3 id="terraform">Terraform</h3>
<p>Terraform users can retrieve the app types list with the <code>cloudflare_zero_trust_gateway_app_types_list</code> data source. This allows you to create Gateway policies with the application's name rather than its numeric ID. For example:</p>
<pre tabindex="0"><code class="language-tf">data &quot;cloudflare_zero_trust_gateway_app_types_list&quot; &quot;gateway_apptypes&quot; {&#10;  account_id = var.cloudflare_account_id&#10;}&#10;&#10;locals {&#10;  apptypes_map = merge([&#10;    for c in data.cloudflare_zero_trust_gateway_app_types_list.gateway_apptypes.result :&#10;    { (c.name) = c.id }&#10;  ]...)&#10;}&#10;&#10;resource &quot;cloudflare_zero_trust_gateway_policy&quot; &quot;zt_block_dns_apps&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;DNS Blocked apps&quot;&#10;  action     = &quot;block&quot;&#10;  traffic    = &quot;any(app.ids[*] in {${join(&quot; &quot;, [&#10;    local.apptypes_map[&quot;Discord&quot;],&#10;    local.apptypes_map[&quot;GoToMeeting&quot;],&#10;    local.apptypes_map[&quot;Greenhouse&quot;],&#10;    local.apptypes_map[&quot;Zelle&quot;],&#10;    local.apptypes_map[&quot;Microsoft Visual Studio&quot;]&#10;  ])}})&quot;&#10;}&#10;</code></pre>
