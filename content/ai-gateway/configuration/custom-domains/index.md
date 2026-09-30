---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/
  description: Send AI Gateway requests through a hostname that you own, such as ai.example.com.
  full_title: Custom domains · Cloudflare AI Gateway docs
  head_html: <title>Custom domains · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Send AI Gateway requests through a hostname that you own, such as ai.example.com."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/index.md"><meta property="og:title" content="Custom domains · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send AI Gateway requests through a hostname that you own, such as ai.example.com."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/#page","headline":"Custom domains \u00b7 Cloudflare AI Gateway docs","description":"Send AI Gateway requests through a hostname that you own, such as ai.example.com.","url":"https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/configuration/custom-domains/
  schema: 1
---
<p>Custom domains let you send AI Gateway requests through a hostname that you own, such as <code>ai.example.com</code>, instead of the default <code>gateway.ai.cloudflare.com</code> endpoint.</p>
<p>The hostname identifies your account and gateway, so you can omit the account ID and gateway ID from request URLs. Requests go directly to AI Gateway provider-native routes and OpenAI-compatible <code>compat</code> routes.</p>
<p>Custom domains are also the foundation for <a href="/ai-gateway/configuration/cloudflare-access/">identity-aware controls with Cloudflare Access</a>, which let users authenticate with your identity provider before they can call your gateway.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2883.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>For example, if your custom domain is <code>ai.example.com</code>, an OpenAI provider request uses:</p>
<pre tabindex="0"><code class="language-txt">https://ai.example.com/openai/v1/chat/completions&#10;</code></pre>
<p>Instead of:</p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/v1/chat/completions&#10;</code></pre>
<p>The same applies to the OpenAI-compatible endpoint. For example, <code>https://ai.example.com/compat/chat/completions</code> routes through the same gateway using the <code>compat</code> route.</p>
<h2 id="set-up-a-custom-domain-in-the-dashboard">Set up a custom domain in the dashboard</h2>
<p>To add a custom domain:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select the gateway you want to configure.</li>
<li>Go to the <strong>Domains</strong> tab.</li>
<li>Select <strong>Add Domain</strong> and enter the hostname you want to use. Optionally, choose a subdomain.</li>
<li>AI Gateway automatically creates the DNS record in the dashboard.</li>
</ol>
<p>After the domain is set up, you can send requests to it. To require users to authenticate before they can call the gateway, <a href="/ai-gateway/configuration/cloudflare-access/">set up Cloudflare Access on the domain</a>.</p>
<h2 id="set-up-a-custom-domain-via-api">Set up a custom domain via API</h2>
<p>You can also create and manage custom domains through the Cloudflare API.</p>
<p>Unlike the dashboard, the API does not create the DNS record for you. After you create the custom domain, use the returned <code>cname_target</code> to create a proxied CNAME record for your hostname.</p>
<h3 id="create-a-custom-domain">Create a custom domain</h3>
<pre tabindex="0"><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/custom-domains</code></pre>
<p>The response includes the custom domain status and the CNAME target:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;hostname&quot;: &quot;ai.example.com&quot;,&#10;		&quot;gateway_id&quot;: &quot;my-gateway&quot;,&#10;		&quot;status&quot;: &quot;pending_dcv&quot;,&#10;		&quot;cname_target&quot;: &quot;&lt;cname-target&gt;&quot;,&#10;		&quot;created_at&quot;: 1782925200000,&#10;		&quot;modified_at&quot;: 1782925200000&#10;	}&#10;}&#10;</code></pre>
<h3 id="create-the-dns-record">Create the DNS record</h3>
<p>Create a proxied CNAME record in the zone that owns your custom domain. Set <code>content</code> to the <code>cname_target</code> returned when you created the custom domain.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records</code></pre>
<p>The custom domain remains in <code>pending_dcv</code> until domain control validation completes.</p>
<h3 id="list-custom-domains">List custom domains</h3>
<pre tabindex="0"><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/custom-domains</code></pre>
<h3 id="get-a-custom-domain">Get a custom domain</h3>
<pre tabindex="0"><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/custom-domains/{hostname}</code></pre>
<h3 id="delete-a-custom-domain">Delete a custom domain</h3>
<pre tabindex="0"><code class="language-bash">curl --request DELETE --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/custom-domains/{hostname}</code></pre>
<h2 id="example-request">Example request</h2>
<p>Send requests to the custom domain without the account ID or gateway ID in the path:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://ai.example.com/openai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>If the domain is protected by Cloudflare Access, the request must also include a valid Access token. For details, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<h2 id="limitations">Limitations</h2>
<p>Custom domains are not yet supported on the newer AI Gateway endpoints served through the <a href="/api/">Cloudflare REST API</a> (<code>api.cloudflare.com</code>).</p>
