---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/
  description: Enable and configure TLS decryption.
  full_title: Use TLS inspection · Cloudflare Learning Paths
  head_html: <title>Use TLS inspection · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Enable and configure TLS decryption."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/index.md"><meta property="og:title" content="Use TLS inspection · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable and configure TLS decryption."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/#page","headline":"Use TLS inspection \u00b7 Cloudflare Learning Paths","description":"Enable and configure TLS decryption.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-http-policies/tls-inspection/
  schema: 1
---
<p>TLS inspection (also known as TLS decryption or HTTPS inspection) allows Cloudflare Gateway to perform deeper traffic analysis and take actions like scanning request bodies for sensitive data, upgrading to a remote browser isolation session, and redirecting based on the complete URL and path of requests.</p>
<p>TLS inspection is desirable for security policy involving users accessing sensitive systems, but it can also present challenges. Without TLS inspection turned on, policies can still use user identity, device posture, IP address, resolved domain, SNI, and a number of other attributes that support a Zero Trust security implementation.</p>
<p>Organizations are often hesitant to adopt TLS inspection practices due to concerns about interoperability with existing systems due to past experiences with legacy systems that conceptually worked in the same way. However, Cloudflare's approach to TLS inspection is capable, performant, modern, and above all, flexible. We understand that it is never possible to inspect absolutely all traffic — something will always break. Our recommendations keep this practical reality in mind.</p>
<h2 id="get-started">Get started</h2>
<p>To decide why and how you should turn on TLS inspection, we recommend you start with the following steps:</p>
<h3 id="1-identify-your-goals"><ol>
<li>Identify your goals</li>
</ol></h3>
<p>Cloudflare Zero Trust requires TLS inspection for most advanced security and <span class="nb-glossary-tooltip" title="Cloudflare Data Loss Prevention (DLP)">data loss prevention (DLP)</span> features.</p>
<p>Some security organizations choose to avoid TLS inspection due to concerns about user privacy and acceptable use. This is an important and sometimes complicated organization decision, but you can simplify it by establishing goals related to your security practices. Questions to consider:</p>
<ul>
<li>Is your organizational use of TLS inspection designed to protect from the &quot;known&quot; (such as sensitive data in corporate-sanctioned SaaS applications) or the &quot;unknown&quot; (such as users downloading or uploading files to brand-new blob storage buckets)?</li>
<li>Do you intend to primarily block by domain or hostname or by building policies for complete URLs?</li>
<li>Do you plan to scan the body of requests or files against DLP profiles or scan downloaded files with an antivirus or anti-malware engine?</li>
<li>Do you intend to use inline <span class="nb-glossary-tooltip" title="Cloudflare Browser Isolation">Remote Browser Isolation</span> to take advantage of data security capabilities like copy/paste blocking, keyboard blocking, and print blocking?</li>
</ul>
<p>If the answer to a majority of these questions is no and your organization relies mostly on hostname or DNS-based security controls, then you may not need to inspect most, if not all TLS traffic. Because Cloudflare operates both as a secure web gateway and as a secure DNS resolver for your connected users, you can apply policy control that may increase your security posture without the need to broadly inspect TLS traffic.</p>
<h3 id="2-turn-on-tls-inspection"><ol start="2">
<li>Turn on TLS inspection</li>
</ol></h3>
<p>To turn on TLS inspection for your Zero Trust organization:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10140.md")
</div></div>
<h4 id="inspect-on-all-ports">Inspect on all ports <span class="nb-badge">Beta</span></h4>
<p>By default, Gateway will only inspect HTTP traffic through port <code>80</code>. Additionally, if you <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">turn on TLS decryption</a>, Gateway will inspect HTTPS traffic through port <code>443</code>.</p>
<p>To detect and inspect HTTP and HTTPS traffic on ports in addition to <code>80</code> and <code>443</code>, <p>you can turn on <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a> and configure Gateway to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect traffic on all ports</a></p>
.</p>
<h3 id="3-determine-the-certificate-used-for-inspection"><ol start="3">
<li>Determine the certificate used for inspection</li>
</ol></h3>
<p>TLS inspection requires a trusted private root certificate to be able to inspect and filter encrypted traffic. A <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">Cloudflare root certificate</a> is a simple and common solution that is usually appropriate for testing or proof-of-concept conditions when deployed to your devices. You can <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">generate a Cloudflare certificate</a> in Zero Trust.</p>
<p>Alternatively, if you already have a root CA that you use for other inspection or trust applications, we recommend <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">using your own certificate</a>. A few reasons for this include:</p>
<ul>
<li>Assuming the root certificate is already deployed on the relevant fleet of devices, using a single certificate streamlines your IT management.</li>
<li>If external services like Git workflows or CLI tools rely on an existing certificate store, presenting the same certificate in inspection is far less likely to interrupt their traffic flow, although these are things that you may wish to exempt from inspection.</li>
<li>If you are using <a href="/mesh/">Cloudflare Mesh</a> or a <a href="/cloudflare-wan/">Cloudflare WAN</a> IPsec/GRE tunnel to on-ramp traffic to Cloudflare, devices behind those tunnels will not be able to use HTTP policies that require TLS inspection unless they have a certificate that matches your organization's certificate of choice. Your network infrastructure most likely already has your own device certificates deployed, so using your own existing public key infrastructure for inspection will simplify protection.</li>
</ul>
<p>Once you generate a Cloudflare certificate or upload a custom certificate, you will need to set it as <strong>Available</strong> to deploy it across the Cloudflare network and as <strong>In-Use</strong> to use it for inspection. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#activate-a-root-certificate">Activate a root certificate</a>.</p>
<h3 id="4-build-a-baseline-do-not-inspect-policy"><ol start="4">
<li>Build a baseline Do Not Inspect policy</li>
</ol></h3>
<p>Do you want to inspect all traffic by default, or do you only want to inspect explicit destinations? We recommend that you build a Gateway list of applications and endpoints to exclude from inspection and add the list as an OR operator in addition to our existing Do Not Inspect application group. For example:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Do Not Inspect</em></td>
<td>Or</td>
<td>Do Not Inspect</td>
</tr>
<tr>
<td>Host</td>
<td>in list</td>
<td><em>Trusted Hostnames</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>If your organization is newly adopting the security framework that requires TLS inspection, we recommend starting minimally. In fact, it may even be appropriate to choose to only explicitly inspect a predetermined list of hostnames, IPs, or specific user groups or device types and forego inspection for everything else during the initial deployment stage. Cloudflare has a unique and flexible approach to where and when you can deploy inspection, meaning it can be as limited and granular as your organization needs without impacting device routing tables or other memory-sensitive local constructs.</p>
<h3 id="5-build-the-necessary-pass-through-rules"><ol start="5">
<li>Build the necessary pass-through rules</li>
</ol></h3>
<p>You can build pass-through rules to accommodate any type of device or user group that should not be subject to inspection.</p>
<p>For example, if users are issued a corporate-managed iPhone with limited permissions, set an additional Do Not Inspect policy for all traffic matching the device posture value. That could include the OS type, OS version, or a list of serial numbers (updated via the API with hooks from your MDM tool) for those iPhones:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10143.md")
</div></div>
<p>If you filter your network-connected devices with IPsec/GRE tunnels, Cloudflare Mesh, or other devices that do not have a Cloudflare certificate installed, you will need to accommodate by creating pass-through policies. For these devices, you should explicitly exempt TLS inspection for the source network IP range from which that traffic will be originating. For example:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10146.md")
</div></div>
