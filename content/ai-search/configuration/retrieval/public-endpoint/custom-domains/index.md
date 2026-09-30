---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/
  description: Serve an AI Search public endpoint from a hostname that you own, such as search.example.com.
  full_title: Custom domains · Cloudflare AI Search docs
  head_html: <title>Custom domains · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve an AI Search public endpoint from a hostname that you own, such as search.example.com."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/index.md"><meta property="og:title" content="Custom domains · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve an AI Search public endpoint from a hostname that you own, such as search.example.com."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/#page","headline":"Custom domains \u00b7 Cloudflare AI Search docs","description":"Serve an AI Search public endpoint from a hostname that you own, such as search.example.com.","url":"https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/retrieval/public-endpoint/custom-domains/
  schema: 1
---
<p>A custom domain serves your <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> from a hostname that you own, such as <code>search.example.com</code>, instead of the default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname.</p>
<p>The endpoints and request formats do not change. Only the hostname changes:</p>
<pre tabindex="0"><code class="language-txt">https://search.example.com/search&#10;https://search.example.com/chat/completions&#10;https://search.example.com/mcp&#10;</code></pre>
<p>Custom domains are also the foundation for <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">restricting access with Cloudflare Access</a>, which lets users authenticate with your identity provider before they can query your indexed content.</p>
<h2 id="requirements">Requirements</h2>
<ul>
<li>The public endpoint must already be enabled on the instance or namespace. Adding a custom domain to an instance without an active public endpoint returns error <code>7093</code>.</li>
<li>The hostname must belong to a zone that is <a href="/fundamentals/manage-domains/add-site/">added to the same Cloudflare account</a> and in an active state. A hostname on another account returns error <code>7090</code>.</li>
<li>Each instance or namespace supports one custom domain.</li>
<li>A hostname can only be attached to one public endpoint at a time. Reusing a hostname returns error <code>7091</code>.</li>
<li>The hostname must be a fully qualified domain name of up to 253 characters, such as <code>search.example.com</code>. Wildcards are not supported. Hostnames are stored in lowercase.</li>
</ul>
<h2 id="add-a-custom-domain">Add a custom domain</h2>
<p>Set <code>public_endpoint_params.custom_domains</code> when you create or update an instance.</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: {&#10;      &quot;enabled&quot;: true,&#10;      &quot;custom_domains&quot;: [&quot;search.example.com&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The same field is available on namespaces. Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">Namespace public endpoints</a>.</p>
<p>Cloudflare issues a certificate for the hostname and begins domain control validation.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3108.md")
</aside>
<h3 id="create-the-dns-record">Create the DNS record</h3>
<p>Create a <strong>proxied</strong> <code>CNAME</code> record in the zone that owns your custom domain. The target is the default hostname of the public endpoint, which is <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code>.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Target</th>
<th>Proxy status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>search</code></td>
<td><code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/zones/&lt;ZONE_ID&gt;/dns_records&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;type&quot;: &quot;CNAME&quot;,&#10;    &quot;name&quot;: &quot;search&quot;,&#10;    &quot;content&quot;: &quot;&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com&quot;,&#10;    &quot;proxied&quot;: true&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3109.md")
</aside>
<p>The custom domain starts serving traffic once domain control validation completes.</p>
<h2 id="turn-off-the-default-hostname">Turn off the default hostname</h2>
<p>By default, a public endpoint answers on both the custom domain and the default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname. Set <code>default_domain_enabled</code> to <code>false</code> to serve the custom domain only. The default hostname then returns a <code>404</code> with error <code>60018</code>.</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: {&#10;      &quot;enabled&quot;: true,&#10;      &quot;custom_domains&quot;: [&quot;search.example.com&quot;],&#10;      &quot;default_domain_enabled&quot;: false&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Turn this off whenever you put security controls in front of the custom domain. Those controls run in your own zone, so any traffic that reaches the default hostname skips them. Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a>.</p>
<p>Three rules apply:</p>
<ul>
<li>You cannot turn off the default hostname without at least one custom domain. The request returns error <code>7096</code>.</li>
<li>Because <code>public_endpoint_params</code> is replaced in full, omitting <code>default_domain_enabled</code> on a later update resets it to <code>true</code> and makes the default hostname reachable again.</li>
<li>Leave the <code>CNAME</code> record pointing at the default hostname. AI Search routes on the hostname the client requested, not the <code>CNAME</code> target, so the record keeps working after you turn the default hostname off.</li>
</ul>
<h2 id="remove-a-custom-domain">Remove a custom domain</h2>
<p>Send <code>custom_domains</code> as an empty array. Cloudflare removes the certificate and stops routing the hostname.</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: {&#10;      &quot;enabled&quot;: true,&#10;      &quot;custom_domains&quot;: []&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>If <code>default_domain_enabled</code> is <code>false</code>, removing the last custom domain in the same request returns error <code>7096</code>. Re-enable the default hostname first, then remove the domain.</p>
<p>Deleting the instance or namespace removes its custom domains and certificates.</p>
<h2 id="errors">Errors</h2>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7090</code></td>
<td><code>custom_domain_not_a_verified_zone_on_this_account</code></td>
<td>The hostname does not belong to an active zone on this account.</td>
</tr>
<tr>
<td><code>7091</code></td>
<td><code>custom_domain_already_in_use</code></td>
<td>The hostname is already attached to another public endpoint.</td>
</tr>
<tr>
<td><code>7092</code></td>
<td><code>custom_domain_provisioning_failed</code></td>
<td>Certificate provisioning failed. Retry the request.</td>
</tr>
<tr>
<td><code>7093</code></td>
<td><code>custom_domains_require_an_active_public_endpoint</code></td>
<td>The instance or namespace has no active public endpoint.</td>
</tr>
<tr>
<td><code>7096</code></td>
<td><code>disabling_the_default_domain_requires_at_least_one_custom_domain</code></td>
<td><code>default_domain_enabled</code> was set to <code>false</code> with no custom domain.</td>
</tr>
<tr>
<td><code>60018</code></td>
<td><code>default domain disabled</code></td>
<td>A request reached the default hostname while it is turned off.</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-cloudflare-access-ai-search-configuration-retrieval-public-endpoint-cloudflare-access"><a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a></h3><p>Require users to authenticate before they can query your public endpoint.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-endpoint-settings-ai-search-configuration-retrieval-public-endpoint"><a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint settings</a></h3><p>Rate limiting, allowed origins, and per-endpoint controls.</p></div>
