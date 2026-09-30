---
cp9:
  canonical: https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/
  description: Resolve prefix validation errors during BYOIP onboarding.
  full_title: Troubleshoot prefix validation · Cloudflare BYOIP docs
  head_html: <title>Troubleshoot prefix validation · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve prefix validation errors during BYOIP onboarding."><link rel="canonical" href="https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/index.md"><meta property="og:title" content="Troubleshoot prefix validation · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve prefix validation errors during BYOIP onboarding."><meta property="og:url" content="https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="BYOIP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/#page","headline":"Troubleshoot prefix validation \u00b7 Cloudflare BYOIP docs","description":"Resolve prefix validation errors during BYOIP onboarding.","url":"https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /byoip/troubleshooting/prefix-validation/
  schema: 1
---
<ol>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/methods/get/">Prefix Details endpoint</a> to check if any issues were found during validation.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">&#10; &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;72823e95d6c64d48a8111fec81179816&quot;,&#10;    &quot;created_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;modified_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;cidr&quot;: &quot;203.0.113.0/24&quot;,&#10;    &quot;account_id&quot;: &quot;654c5f71c324478cc9f68d60065d4620&quot;,&#10;    &quot;description&quot;: &quot;&quot;,&#10;    &quot;approved&quot;: &quot;P&quot;,&#10;    &quot;on_demand_enabled&quot;: false,&#10;    &quot;on_demand_locked&quot;: false,&#10;    &quot;advertised&quot;: null,&#10;    &quot;advertised_modified_at&quot;: null,&#10;    &quot;loa_document_id&quot;: &quot;b9ff4afe312246a8b2e7324d98f40b23&quot;,&#10;    &quot;asn&quot;: 13335,&#10;    &quot;ownership_validation_token&quot;: &quot;&lt;OWNERSHIP_VALIDATION_TOKEN&gt;&quot;,&#10;    &quot;delegate_loa_creation&quot; : true,&#10;    &quot;irr_validation_state&quot;: &quot;valid&quot;,&#10;    &quot;rpki_validation_state&quot;: &quot;valid&quot;,&#10;    &quot;ownership_validation_state&quot;: &quot;missing&quot;,&#10;  }&#10;</code></pre>
<ol start="2">
<li>
<p>Consider the states returned in the API response (for example, <code>missing</code>, <code>invalid</code>, <code>mismatch_asn</code>) and review your IRR record, <span class="nb-glossary-tooltip" title="Route Origin Authorization (ROA)">ROA</span>, and ownership validation method accordingly.</p>
<ul>
<li>
<p>Information in the IRR and ROA records should meet the <a href="/byoip/get-started/#before-you-begin">onboarding prerequisites</a>.</p>
</li>
<li>
<p><a href="/byoip/get-started/#validate-prefix-ownership">Ownership validation</a> requires a matching ROA and the correct validation token found in all DNS TXT records or in the IRR record.</p>
</li>
</ul>
</li>
<li></li>
</ol>
<p>After applying the necessary changes, use the Validate Prefix endpoint to trigger the validation checks.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/validate \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
