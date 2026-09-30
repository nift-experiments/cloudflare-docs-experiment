---
cp9:
  canonical: https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/
  description: Add and manage zone and account-level subscriptions for tenant-managed Cloudflare accounts.
  full_title: Manage subscriptions · Cloudflare Tenant docs
  head_html: <title>Manage subscriptions · Cloudflare Tenant docs</title><meta name="generator" content="Nift"><meta name="description" content="Add and manage zone and account-level subscriptions for tenant-managed Cloudflare accounts."><link rel="canonical" href="https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/index.md"><meta property="og:title" content="Manage subscriptions · Cloudflare Tenant docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add and manage zone and account-level subscriptions for tenant-managed Cloudflare accounts."><meta property="og:url" content="https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Tenant"><meta name="algolia_product_filter" content="Tenant"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Tenant"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/#page","headline":"Manage subscriptions \u00b7 Cloudflare Tenant docs","description":"Add and manage zone and account-level subscriptions for tenant-managed Cloudflare accounts.","url":"https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tenant/how-to/manage-subscriptions/
  schema: 1
---
<p>Once your customer has a zone provisioned, you can add zone and account-level subscriptions.</p>
<h2 id="zone-subscriptions">Zone subscriptions</h2>
<h3 id="create-zone-subscription">Create zone subscription</h3>
<p>To create a zone subscription, typically used to upgrade a zone's plan from <code>PARTNERS_FREE</code> to a paid <a href="/tenant/reference/subscriptions/#zone-plans">Zone plan</a>, send a <a href="/api/resources/zones/subresources/subscriptions/methods/create/">POST</a> request to the <code>/zones/{zone_id}/subscription</code> endpoint and include the following values:</p>
<ul>
<li>
<p><code>rate_plan</code> object</p>
<ul>
<li>Contains the zone plan corresponding to what customers would order in the dashboard. For a list of available values, refer to <a href="/tenant/reference/subscriptions/#zone-plans">Zone subscriptions</a>.</li>
</ul>
</li>
<li>
<p><code>component_values</code> array</p>
<ul>
<li>Additional services depending on your reseller agreement, such as additional <code>page_rules</code>.</li>
</ul>
</li>
<li>
<p><code>frequency</code> string</p>
<ul>
<li>How often the subscription is renewed automatically (defaults to <code>&quot;monthly&quot;</code>).</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RATE_PLAN&gt;&quot;&#10;  },&#10;  &quot;frequency&quot;: &quot;annual&quot;&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;PARTNERS_BIZ&quot;&#10;  },&#10;  &quot;component_values&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;page_rules&quot;,&#10;      &quot;value&quot;: 50&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="get-zone-subscription-details">Get zone subscription details</h3>
<p>To get the details of a zone subscription, send a <a href="/api/resources/zones/subresources/subscriptions/methods/get/"><code>GET</code></a> request to the <code>/zones/&lt;ZONE_ID&gt;/subscription</code> endpoint.</p>
<h3 id="update-zone-subscription">Update zone subscription</h3>
<p>To update a subscription on a zone, typically used to update an existing subscription's 'component_values' or to downgrade a zone's subscription, send a <a href="/api/resources/zones/subresources/subscriptions/methods/update/"><code>PUT</code></a> request to the <code>/zones/&lt;ZONE_ID&gt;/subscription</code> endpoint.</p>
<hr />
<h2 id="account-subscriptions">Account subscriptions</h2>
<p>Depending on your agreement, you may be allowed to resell other add-on services. These are provisioned as account-level subscriptions.</p>
<h3 id="create-account-subscription">Create account subscription</h3>
<p>To create an account subscription, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/create/">POST</a> request to the <code>/accounts/{account_id}/subscriptions</code> endpoint and include the following values:</p>
<ul>
<li>
<p><code>rate_plan</code> object</p>
<ul>
<li>Contains the account subscription corresponding to a specific add-on service. For a list of available values, refer to <a href="/tenant/reference/subscriptions/">Available subscriptions</a>.</li>
</ul>
</li>
<li>
<p><code>component_values</code> array</p>
<ul>
<li>Additional services depending on your reseller agreement, such as additional endpoints for load balancing or additional seats for Cloudflare Zero Trust. If not included, the subscription includes the default values associated with each purchase.</li>
</ul>
</li>
<li>
<p><code>frequency</code> string</p>
<ul>
<li>How often the subscription is renewed automatically (defaults to <code>&quot;monthly&quot;</code>).</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/subscriptions&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RATE_PLAN_NAME&gt;&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="get-account-subscription-details">Get account subscription details</h3>
<p>To get all subscriptions for an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/get/"><code>GET</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions</code> endpoint.</p>
<h3 id="update-account-subscription">Update account subscription</h3>
<p>To update a subscription on an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/update/"><code>PUT</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions/&lt;SUBSCRIPTION_ID&gt;</code> endpoint.</p>
<h3 id="delete-account-subscription">Delete account subscription</h3>
<p>To delete a subscription on an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/delete/"><code>DELETE</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions/&lt;SUBSCRIPTION_ID&gt;</code> endpoint.</p>
