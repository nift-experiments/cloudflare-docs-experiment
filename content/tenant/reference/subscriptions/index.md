---
cp9:
  canonical: https://developers.cloudflare.com/tenant/reference/subscriptions/
  description: Zone plan and account subscription values available to Cloudflare Tenant partners.
  full_title: Available subscriptions · Cloudflare Tenant docs
  head_html: <title>Available subscriptions · Cloudflare Tenant docs</title><meta name="generator" content="Nift"><meta name="description" content="Zone plan and account subscription values available to Cloudflare Tenant partners."><link rel="canonical" href="https://developers.cloudflare.com/tenant/reference/subscriptions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tenant/reference/subscriptions/index.md"><meta property="og:title" content="Available subscriptions · Cloudflare Tenant docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Zone plan and account subscription values available to Cloudflare Tenant partners."><meta property="og:url" content="https://developers.cloudflare.com/tenant/reference/subscriptions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Tenant"><meta name="algolia_product_filter" content="Tenant"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Tenant"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tenant/reference/subscriptions/#page","headline":"Available subscriptions \u00b7 Cloudflare Tenant docs","description":"Zone plan and account subscription values available to Cloudflare Tenant partners.","url":"https://developers.cloudflare.com/tenant/reference/subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tenant/reference/subscriptions/
  schema: 1
---
<p>When <a href="/tenant/how-to/manage-subscriptions/">provisioning services for an account</a>, you need to include certain values with each API call to specify a particular service.</p>
<p>The subscriptions available to you will vary depending on your current partner program (<a href="https://www.cloudflare.com/cloudflare-partners-self-serve-program-closed-beta/">Agency Partner Program</a> or <a href="https://portal.cloudflarepartners.com">Enterprise Resellers and MSP Program</a>).</p>
<p>The following values are samples and not exhaustive. For the complete list of subscription values available to you, make an API call to the <a href="/api/resources/zones/subresources/rate_plans/methods/get/">zone subscriptions</a> or <a href="/api/resources/accounts/subresources/subscriptions/methods/get/">account subscriptions</a> endpoints.</p>
<h2 id="zone-plans">Zone plans</h2>
<p>When creating or updating a <a href="/api/resources/zones/subresources/subscriptions/methods/get/">zone plan</a>, Partners can use one of the following values for the <code>id</code> of the <code>rate_plan</code> field (which controls the zone-level plan subscription).</p>
<table>
<thead>
<tr>
<th>Partner program</th>
<th>Available subscriptions</th>
</tr>
</thead>
<tbody>
<tr>
<td>Enterprise and self-serve resellers</td>
<td><code>PARTNERS_FREE</code>, <code>PARTNERS_PRO</code>, <code>PARTNERS_BIZ</code>, <code>PARTNERS_ENT</code></td>
</tr>
<tr>
<td>Agency partners</td>
<td><code>CF_FREE</code>, <code>CF_PRO_20_20</code>, <code>CF_BIZ</code></td>
</tr>
<tr>
<td>MSP partners</td>
<td><code>msp_biz</code></td>
</tr>
</tbody>
</table>
<h2 id="other-subscriptions">Other subscriptions</h2>
<p>When you <a href="/tenant/how-to/manage-subscriptions/#account-subscriptions">create an account subscription</a>, it provisions an add-on service for that account.</p>
<h3 id="zero-trust-subscriptions">Zero Trust subscriptions</h3>
<p>The following table lists sample values for various Zero Trust subscriptions.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Subscription IDs</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/integrations/identity-providers/">Access</a></td>
<td><code>PARTNERS_ACCESS_BASIC</code>, <code>PARTNERS_ACCESS_ENT</code>, <code>PARTNERS_ACCESS_PREMIUM</code>, <code>TEAMS_ACCESS_ENT</code>, <code>TEAMS_ACCESS</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/traffic-policies/">Gateway</a></td>
<td><code>TEAMS_GATEWAY_ENT</code>, <code>TEAMS_GATEWAY</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/">Cloudflare Zero Trust</a></td>
<td><code>TEAMS_ENT</code>, <code>TEAMS_FREE</code>, <code>TEAMS_STANDARD</code></td>
</tr>
</tbody>
</table>
<h3 id="developer-subscriptions">Developer subscriptions</h3>
<p>The following table lists sample values for various Developer platform subscriptions.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Subscription IDs</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/images/">Images</a></td>
<td><code>IMAGES_ENT</code>,<code>IMAGES_BASIC</code></td>
</tr>
<tr>
<td><a href="/images/optimization/transformations/overview/">Image transformations</a></td>
<td><code>IMAGE_RESIZING_ENT</code>, <code>IMAGE_RESIZING_BASIC</code></td>
</tr>
<tr>
<td><a href="/stream/">Stream</a></td>
<td><code>PARTNERS_STREAM_ENT</code>, <code>PARTNERS_STREAM_BASIC</code>, <code>STREAM_BASIC</code></td>
</tr>
<tr>
<td><a href="/workers">Workers</a></td>
<td><code>PARTNERS_WORKERS_ENT</code>, <code>WORKERS_PAID</code>, <code>PARTNERS_WORKERS_SS</code>, <code>PARTNERS_WORKERS_BASIC</code></td>
</tr>
</tbody>
</table>
<h3 id="application-performance-and-security">Application performance and security</h3>
<p>The following table lists sample values for various application performance and security subscriptions.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Subscription IDs</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api-shield/">API Shield</a></td>
<td><code>API_SHIELD_ZONE</code></td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificate manager</a></td>
<td><code>ADVANCED_CERT_MANAGER_FREE</code>, <code>ADVANCED_CERT_MANAGER</code></td>
</tr>
<tr>
<td><a href="/argo-smart-routing/">Argo smart routing</a></td>
<td><code>PARTNERS_ZONE_ARGO</code>, <code>ARGO_ZONE_BASIC</code></td>
</tr>
<tr>
<td><a href="/web3/ethereum-gateway/">Ethereum gateway</a></td>
<td><code>WEB3_ETHEREUM_ENT</code>, <code>WEB3_ETHEREUM_ENT_CONTRACT</code>, <code>WEB3_ETHEREUM_ENT_PAYGO</code></td>
</tr>
<tr>
<td><a href="/web3/ipfs-gateway/">IPFS gateway</a></td>
<td><code>WEB3_IPFS_ENT</code>, <code>WEB3_IPFS_ENT_CONTRACT</code>, <code>WEB3_IPFS_ENT_PAYGO</code></td>
</tr>
<tr>
<td><a href="/load-balancing/">Load balancing</a></td>
<td><code>PARTNERS_LOAD_BALANCING</code>, <code>PARTNERS_LOAD_BALANCING_ENT</code>, <code>LOAD_BALANCING_BASIC_PLUS</code></td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate limiting</a></td>
<td><code>PARTNERS_RATE_LIMITING</code></td>
</tr>
<tr>
<td><a href="/spectrum/">Spectrum</a></td>
<td><code>PARTNERS_SPECTRUM</code></td>
</tr>
<tr>
<td><a href="/waiting-room/">Waiting Room</a></td>
<td><code>WAITING_ROOMS_BASIC</code>, <code>WAITING_ROOMS_ADV</code></td>
</tr>
</tbody>
</table>
<h3 id="network-services">Network services</h3>
<p>The following table lists sample values for various network services subscriptions.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Subscription IDs</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a></td>
<td><code>MAGIC_FIREWALL_BASIC</code>, <code>MAGIC_FIREWALL_ADVANCED</code></td>
</tr>
<tr>
<td><a href="/cloudflare-wan/">Cloudflare WAN</a></td>
<td><code>MAGIC_WAN</code></td>
</tr>
</tbody>
</table>
<h2 id="getting-new-subscriptions">Getting new subscriptions</h2>
<p>If your reseller plan does not have access to a specific subscription, you will receive the following error when making an API call:</p>
<pre tabindex="0"><code class="language-json">&quot;errors&quot;: [&#10;        {&#10;            &quot;code&quot;: 1225,&#10;            &quot;message&quot;: &quot;Your account does not have access to this product. Contact billing@cloudflare.com for assistance.&quot;&#10;        }&#10;]&#10;</code></pre>
<p>To change your program or - in some cases - get a specific subscription added to your reseller plan, contact <code>partners@cloudflare.com</code>. Agency Partners should contact <a href="mailto:agency@cloudflare.com">agency@cloudflare.com</a></p>
