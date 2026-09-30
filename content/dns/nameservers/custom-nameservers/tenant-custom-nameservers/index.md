---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/
  description: With tenant-level custom nameservers, you can use the same custom nameservers for different zones and across different accounts, as long as the accounts are part of the [tenant](/tenant/). The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.
  full_title: Tenant custom nameservers · Cloudflare DNS docs
  head_html: <title>Tenant custom nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="With tenant-level custom nameservers, you can use the same custom nameservers for different zones and across different accounts, as long as the accounts are part of the [tenant](/tenant/). The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/index.md"><meta property="og:title" content="Tenant custom nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With tenant-level custom nameservers, you can use the same custom nameservers for different zones and across different accounts, as long as the accounts are part of the [tenant](/tenant/). The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/#page","headline":"Tenant custom nameservers \u00b7 Cloudflare DNS docs","description":"With tenant-level custom nameservers, you can use the same custom nameservers for different zones and across different accounts, as long as the accounts are part of the tenant. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.","url":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/custom-nameservers/tenant-custom-nameservers/
  schema: 1
---
<p>Tenant custom nameservers (TCNS) allow you to define tenant-level custom nameservers and use them for different accounts within a Cloudflare tenant.</p>
<p>TCNS are organized in different sets (<code>ns_set</code>) and TCNS names can be provided by any domain, even if the domain does not exist as a zone in Cloudflare.</p>
<p>For instance, if the TCNS are <code>ns1.example.com</code> and <code>ns2.vanity.test</code>, the domains <code>example.com</code> and <code>vanity.test</code> are not required to be zones in Cloudflare.</p>
<h2 id="availability">Availability</h2>
<p>Tenant custom nameservers, if created by the tenant owner, will be available to all zones belonging to any account that is part of the tenant. Via API only.</p>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>For this configuration to be possible, a few conditions apply:</p>
<ul>
<li>Tenant owners can create up to five different tenant custom nameserver sets. Each nameserver set must have between two and five different nameserver names (<code>ns_name</code>), and each name cannot belong to more than one set. For example, if <code>ns1.example.com</code> is part of <code>ns_set 1</code> it cannot be part of <code>ns_set 2</code> or vice versa.</li>
<li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a> or <a href="/dns/additional-options/reverse-zones/">reverse zones</a> can use tenant custom nameservers as long as they use a different nameserver set (<code>ns_set</code>) than their parent, child, or any other zone in their direct hierarchy tree.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7870.md")
</aside>
<h2 id="for-account-owners">For account owners</h2>
<h3 id="enable-tenant-custom-nameservers-on-a-zone">Enable tenant custom nameservers on a zone</h3>
<p>If you are an account owner and your account is part of a tenant that has custom nameservers, do the following:</p>
<ol>
<li>Use the endpoint <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings for a Zone</a> and configure the <code>nameservers</code> object accordingly.</li>
</ol>
<pre tabindex="0"><code class="language-txt">  &quot;nameservers&quot;: {&#10;    &quot;type&quot;: &quot;custom.tenant&quot;&#10;  }&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7869.md")
</aside>
<ol start="2">
<li>If you are <strong>not</strong> using <a href="/registrar/">Cloudflare Registrar</a>, update the nameservers at your registrar to use the TCNS names. If you are using <a href="/registrar/">Cloudflare Registrar</a>, no further action is needed.</li>
</ol>
<p>To make these TCNS the default namerservers for all new zones added to your account from now on, use the endpoint <a href="/api/resources/dns/subresources/settings/subresources/account/methods/edit/">Update DNS Settings for an Account</a>. Within the <code>zone_defaults</code> object, set the following:</p>
<pre tabindex="0"><code class="language-txt">&quot;zone_defaults&quot;: {&#10;  &quot;nameservers&quot;: {&#10;    &quot;type&quot;: &quot;custom.tenant&quot;&#10;  }&#10;}&#10;</code></pre>
<h3 id="disable-tenant-custom-nameservers-on-a-zone">Disable tenant custom nameservers on a zone</h3>
<ul>
<li>
<p>If you are using <a href="/registrar/">Cloudflare Registrar</a>, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS settings endpoint</a> to set the <code>type</code> parameter in the <code>nameservers</code> object to a different value. Then, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to set your nameservers back to the nameservers you chose to use.</p>
</li>
<li>
<p>If you are not using Cloudflare Registrar, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS settings endpoint</a> to choose a different nameserver type, and also remove the TCNS at your domain's registrar.</p>
</li>
</ul>
<h2 id="for-tenant-owners">For tenant owners</h2>
<h3 id="create-tenant-custom-nameservers">Create tenant custom nameservers</h3>
<p>If you are a tenant owner and you want to make TCNS available for accounts within your tenant, do the following:</p>
<ol>
<li>Observe the <a href="#configuration-conditions">conditions</a> for <code>ns_name</code> and <code>ns_set</code>, and create TCNS in your tenant by using the following POST command:</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/tenants/{tenant_id}/custom_ns \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;ns_name&quot;: &quot;&lt;NS_NAME&gt;&quot;,&#10;  &quot;ns_set&quot;: &lt;SET&gt;&#10;}&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7868.md")
</aside>
<ol start="2">
<li>
<p>Add the account custom nameservers and IP addresses to your domain's registrar as glue (A and AAAA) records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>).</p>
</li>
<li>
<p>If the domain or domains that are used for the tenant custom nameservers do not exist within the same account, you must create the <code>A/AAAA</code> records on the configured nameserver names (for example, <code>ns1.example.com</code>) at the authoritative DNS provider.</p>
</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7871.md")
</div>
<h3 id="get-a-list-of-all-tcns-names">Get a list of all TCNS names</h3>
<p>To get a list of all TCNS names in your tenant account, use the following API request:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/tenants/{tenant_id}/custom_ns \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
