---
cp9:
  canonical: https://developers.cloudflare.com/byoip/get-started/
  description: Onboard your IP prefixes to Cloudflare with BYOIP.
  full_title: Get started · Cloudflare BYOIP docs
  head_html: <title>Get started · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Onboard your IP prefixes to Cloudflare with BYOIP."><link rel="canonical" href="https://developers.cloudflare.com/byoip/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Onboard your IP prefixes to Cloudflare with BYOIP."><meta property="og:url" content="https://developers.cloudflare.com/byoip/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="BYOIP"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/get-started/#page","headline":"Get started \u00b7 Cloudflare BYOIP docs","description":"Onboard your IP prefixes to Cloudflare with BYOIP.","url":"https://developers.cloudflare.com/byoip/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /byoip/get-started/
  schema: 1
---
<p>To use your own IP addresses with Cloudflare, please check with your account team to confirm your contract covers this functionality. You will need to configure settings specific to the services you want to use, as well as meet some standard requirements for all BYOIP customers.</p>
<p>Once your account configurations are in place, consider the sections below to learn how to set up your BYOIP prefixes. Also make sure to review the <a href="https://www.cloudflare.com/service-specific-terms-network-services/#bring-your-own-ip-terms">BYOIP Service-Specific Terms</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="magic-transit">Magic Transit</h3>
@markup("md", "content/.markup/bodies/1393.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>
<p>Your prefix must be registered under one of the Regional Internet Registries (RIRs):</p>
<ul>
<li><a href="https://afrinic.net/">AFRINIC</a></li>
<li><a href="https://www.apnic.net/">APNIC</a></li>
<li><a href="https://www.arin.net/">ARIN</a></li>
<li><a href="https://lacnic.net/">LACNIC</a></li>
<li><a href="https://www.ripe.net/">RIPE</a></li>
</ul>
</li>
<li>
<p>Also verify that your <a href="/byoip/concepts/irr-entries/">Internet Routing Registry (IRR)</a> records are up to date and contain:</p>
<ul>
<li><code>route</code> or <code>route6</code> objects matching the exact prefixes you want to onboard</li>
<li><code>origin</code> matching the correct ASN you want to onboard</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-cloudflare-s-asn">Use Cloudflare's ASN</h3>
@markup("md", "content/.markup/bodies/1392.md")
</aside>
<ul>
<li>
<p>You must use <a href="/byoip/concepts/route-filtering-rpki/">Resource Public Key Infrastructure (RPKI) validation</a> and make sure your ROAs are accurate. You can use <a href="https://rpki.cloudflare.com/?view=validator">Cloudflare's RPKI Portal</a> and a second source such as <a href="https://rpki-validator.ripe.net/ui/">Routinator</a> to double-check your prefixes.</p>
</li>
<li>
<p>If you are not familiar with how Cloudflare API works, refer to <a href="/fundamentals/api/">Fundamentals</a>. Make sure you have the necessary permissions and that you have your account ID.</p>
</li>
</ul>
<hr />
<h2 id="1-set-up-your-prefixes"><ol>
<li>Set up your prefixes</li>
</ol></h2>
<h3 id="add-your-prefix">Add your prefix</h3>
<ol>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/methods/create/">Add Prefix endpoint</a> to create a prefix in the Cloudflare account that should own the BYOIP prefix.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-cloudflare-s-asn-1">Use Cloudflare's ASN</h3>
@markup("md", "content/.markup/bodies/1391.md")
</aside>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;cidr&quot;: &quot;203.0.113.0/24&quot;,&#10;  &quot;asn&quot;: 13335,&#10;  &quot;delegate_loa_creation&quot;: true&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">&#10; &quot;result&quot;: {&#10;	 &quot;id&quot;: &quot;72823e95d6c64d48a8111fec81179816&quot;,&#10;    &quot;created_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;modified_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;cidr&quot;: &quot;203.0.113.0/24&quot;,&#10;    &quot;account_id&quot;: &quot;654c5f71c324478cc9f68d60065d4620&quot;,&#10;    &quot;description&quot;: &quot;&quot;,&#10;    &quot;approved&quot;: &quot;P&quot;,&#10;    &quot;on_demand_enabled&quot;: false,&#10;    &quot;on_demand_locked&quot;: false,&#10;    &quot;advertised&quot;: null,&#10;    &quot;advertised_modified_at&quot;: null,&#10;    &quot;loa_document_id&quot;: &quot;b9ff4afe312246a8b2e7324d98f40b23&quot;,&#10;    &quot;asn&quot;: 13335,&#10;    &quot;ownership_validation_token&quot;: &quot;&lt;OWNERSHIP_VALIDATION_TOKEN&gt;&quot;,&#10;    &quot;delegate_loa_creation&quot; : true,&#10;    &quot;irr_validation_state&quot;: &quot;pending&quot;,&#10;    &quot;rpki_validation_state&quot;: &quot;pending&quot;,&#10;    &quot;ownership_validation_state&quot;: &quot;pending&quot;,&#10;  }&#10;</code></pre>
<ol start="2">
<li>Take note of the <code>id</code> assigned to the prefix you added. It will be used in future steps.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="letter-of-agency-loa">Letter of Agency (LOA)</h3>
@markup("md", "content/.markup/bodies/1390.md")
</aside>
<h3 id="validate-prefix-ownership">Validate prefix ownership</h3>
<ol>
<li>Validate prefix ownership using one of the following methods:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1397.md")
</div></div>
<ol start="2">
<li></li>
</ol>
<p>After applying the necessary changes, use the Validate Prefix endpoint to trigger the validation checks.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/validate \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>Once the ownership validation is successful, you can remove the token.</p>
<p>When all validations pass - RPKI, IRR, and ownership - the <code>approved</code> field in your prefix will return <code>&quot;V&quot;</code>. This means you can proceed to create IP address service bindings<sup><a href="#footnote-1">1</a></sup>.</p>
<p>If needed, you can use the <a href="/api/resources/addressing/subresources/prefixes/methods/get/">Prefix Details endpoint</a> to check if any issues were found during validation. If so, proceed with the necessary changes and make a request to restart validation. Refer to <a href="/byoip/troubleshooting/prefix-validation/">Prefix validation checks</a> for details.</p>
<h3 id="optional-delegate-your-byoip-prefixes">(Optional) Delegate your BYOIP prefixes</h3>
<p>You can allow other accounts to use part or all of your BYOIP prefix. Refer to <a href="/byoip/concepts/prefix-delegations/">Prefix delegations</a> for details.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;cidr&quot;: &quot;&lt;IP_PREFIX_TO_DELEGATE&gt;&quot;,&#10;  &quot;delegated_account_id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1387.md")
</aside>
<hr />
<h2 id="2-create-service-bindings"><ol start="2">
<li>Create service bindings</li>
</ol></h2>
<p>In IP address management, service bindings map the traffic destined for a given IP address to the Cloudflare service that it should be routed through.</p>
<h3 id="default-service-binding">Default service binding</h3>
<p>When you onboard your IP prefixes to Cloudflare, there must be one service binding that spans across your entire prefix. Traffic destined for a given IP address will be routed to this service by default. You can also configure <a href="#optional-additional-bindings">additional service bindings</a> as described in the next step.</p>
<ol>
<li>Make a <code>GET</code> request to the <a href="/api/resources/addressing/subresources/services/methods/list/">List Services</a> endpoint and take note of the <code>id</code> associated with the service you want to use.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cdn-egress">CDN egress</h3>
@markup("md", "content/.markup/bodies/1386.md")
</aside>
<ol start="2">
<li>(Optional) If needed, use the <a href="/api/resources/addressing/subresources/prefixes/methods/list/">List Prefixes</a> endpoint to get or confirm the <code>id</code> associated with your prefix.</li>
<li>Make a <code>POST</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/">Create service binding</a> endpoint, indicating the entire BYOIP prefix that you are onboarding and the service that should be used for your default binding.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;cidr&quot;: &quot;203.0.113.0/24&quot;,&#10;  &quot;service_id&quot;: &quot;&lt;DEFAULT_SERVICE&gt;&quot;&#10;}&#x27;</code></pre>
<p>A corresponding BGP prefix will be created automatically. Allow five hours before you advertise the prefix.</p>
<h3 id="optional-additional-bindings">(Optional) Additional bindings</h3>
<p>If you want to selectively route traffic on a per-IP address basis to CDN or Spectrum, you can create additional service bindings.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1385.md")
</aside>
<ol>
<li>Plan for what IP(s) will get the additional binding. Cloudflare <strong>strongly</strong> recommends implementing service bindings through an <strong>aggregated</strong> CIDR block, as it is more efficient than adding discrete bindings for non-contiguous CIDR blocks.</li>
</ol>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1398.md")
</div></details>
<ol start="2">
<li>Make a <code>POST</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/">Create service binding</a> endpoint, indicating the IP address you want to bind to the CDN or Spectrum. Specify the <strong>corresponding network mask</strong> as needed.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;cidr&quot;: &quot;203.0.113.16/29&quot;,&#10;  &quot;service_id&quot;: &quot;&lt;SERVICE_ID&gt;&quot;&#10;}&#x27;</code></pre>
<p>In the response body, the initial provisioning state should be <code>provisioning</code>.</p>
<pre tabindex="0"><code class="language-json">&#10;   {&#10;     &quot;errors&quot;: [],&#10;     &quot;messages&quot;: [],&#10;     &quot;success&quot;: true,&#10;     &quot;result&quot;: {&#10;       &quot;cidr&quot;: &quot;203.0.113.16/29&quot;,&#10;       &quot;id&quot;: &quot;&lt;SERVICE_BINDING_ID&gt;&quot;,&#10;       &quot;provisioning&quot;: {&#10;         &quot;state&quot;: &quot;provisioning&quot;&#10;         },&#10;       &quot;service_id&quot;: &quot;&lt;SERVICE_ID&gt;&quot;,&#10;       &quot;service_name&quot;: &quot;&lt;SERVICE_NAME&gt;&quot;&#10;     }&#10;   }&#10;</code></pre>
<p>Once a service binding is created (or deleted), it will take <strong>four to six hours</strong> to propagate across Cloudflare's global network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1384.md")
</aside>
<hr />
<h2 id="3-advertise-the-bgp-prefix"><ol start="3">
<li>Advertise the BGP prefix</li>
</ol></h2>
<p>Once automatically created (following <a href="#2-create-service-bindings">step 2</a>), BGP prefixes are initially withdrawn. After all your configurations are in place - including <a href="/byoip/address-maps/">address maps</a><sup><a href="#footnote-2">2</a></sup> if you will use CDN service -, proceed to advertise the BGP route for your prefix.</p>
<ol>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit/">Update BGP prefix</a> endpoint to start the advertisement.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;on_demand&quot;: {&#10;    &quot;advertised&quot;: true&#10;  }&#10;}&#x27;</code></pre>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Mappings that control through which pipeline traffic destined for a given IP address will be routed.</li>
<li id="footnote-2">Mappings that specify which IP addresses should be used when Cloudflare responds to DNS queries for proxied hostnames.</li></ol></section>
