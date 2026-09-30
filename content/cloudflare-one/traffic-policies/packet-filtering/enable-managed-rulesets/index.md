---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/
  description: Enable Managed Rulesets in Gateway.
  full_title: Enable Managed Rulesets · Cloudflare One docs
  head_html: <title>Enable Managed Rulesets · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Managed Rulesets in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/index.md"><meta property="og:title" content="Enable Managed Rulesets · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Managed Rulesets in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/#page","headline":"Enable Managed Rulesets \u00b7 Cloudflare One docs","description":"Enable Managed Rulesets in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/
  schema: 1
---
<p>With <a href="/ruleset-engine/managed-rulesets/">managed rulesets</a>, you can quickly deploy pre-built firewall rules maintained by Cloudflare. You use Cloudflare Network Firewall to control which managed rules are enabled.</p>
<p>In addition to enabling managed rulesets, you can also add and enable custom policies. Refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/add-policies/">add policies</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6418.md")
</aside>
<p>To enable or disable a rule, you specify which properties should be overridden. Overrides are configured in the root ruleset of the Managed phase (the top-level ruleset that controls which managed rules are active). This root ruleset can contain only one rule, but that single rule can include multiple overrides for different managed rules.</p>
<p>Cloudflare recommends starting with the <code>action</code> set to <code>log</code> to evaluate impact before switching to block.</p>
<p>You have multiple options for enabling rules:</p>
<ul>
<li>Select an individual rule and enable it.</li>
<li>Enable multiple rules by enabling by category in the <code>magic-transit-phase</code>.</li>
<li>Enable an entire ruleset.</li>
</ul>
<h2 id="api">API</h2>
<h3 id="1-create-a-managed-phase-managed-kind-ruleset"><ol>
<li>Create a Managed phase Managed kind ruleset</li>
</ol></h3>
<p>To create a managed ruleset, you must first build a request with the following:</p>
<ul>
<li><code>managed_ruleset_id</code>: The ID of the Managed phase Managed kind ruleset that contains the rule you want to enable. To find this ID, list available managed rulesets using <code>GET /accounts/{account_id}/rulesets?kind=managed&amp;phase=magic_transit_managed</code>.</li>
<li><code>managed_rule_id</code>: The ID of the rule you want to enable.</li>
</ul>
<p>Additionally, you need the properties you want to override. The properties you can override include:</p>
<ul>
<li><code>enabled</code>: This value can be set to <code>true</code> or <code>false</code>. When set to <code>true</code>, the rule matches packets and applies the rule's default action if the action is not overridden. When set to <code>false</code>, the rule is disabled and does not match any packets.</li>
<li><code>action</code>: The value can be set to <code>log</code> so the rule only produces logs instead of applying the rule's default action.</li>
</ul>
<p>The <code>enabled</code> and <code>action</code> properties for a rule are set in the Managed phase Managed kind ruleset. All rules in the Managed phase are currently disabled by default.</p>
<p>The example below contains a request for a Managed phase Managed Kind ruleset.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;execute ruleset&quot;,&#10;  &quot;description&quot;: &quot;Ruleset containing execute rules&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit_managed&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;description&quot;: &quot;Enable one rule &quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;version&quot;: &quot;latest&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;MANAGED_RULE_ID&gt;&quot;,&#10;              &quot;enabled&quot;: true,&#10;              &quot;action&quot;: &quot;log&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="2-patch-a-managed-phase-managed-kind-ruleset"><ol start="2">
<li>Patch a Managed phase Managed kind ruleset</li>
</ol></h3>
<p>Because the root ruleset can only contain one rule, you must PATCH that existing rule (rather than adding new rules) when you want to enable additional managed rules.</p>
<p>Building off the example from the previous step, the example below enables a category to select multiple rules instead of a single rule. The category will be set to <code>log</code> mode, which means the rule can produce logs but will not accept or drop packets.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{root_kind_ruleset}/rules/{root_kind_rule} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;    &quot;version&quot;: &quot;latest&quot;,&#10;    &quot;overrides&quot;: {&#10;      &quot;rules&quot;: [&#10;        {&#10;          &quot;id&quot;: &quot;&lt;MANAGED_RULE_ID&gt;&quot;,&#10;          &quot;enabled&quot;: true&#10;        }&#10;      ],&#10;      &quot;categories&quot;: [&#10;        {&#10;          &quot;category&quot;: &quot;simple&quot;,&#10;          &quot;enabled&quot;: true,&#10;          &quot;action&quot;: &quot;log&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="3-enable-all-rules"><ol start="3">
<li>Enable all rules</li>
</ol></h3>
<p>To enable the complete ruleset or enable all rules, send the request below.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{root_kind_ruleset}/rules/{root_kind_rule} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;    &quot;version&quot;: &quot;latest&quot;,&#10;    &quot;overrides&quot;: {&#10;      &quot;enabled&quot;: true&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="4-delete-a-ruleset"><ol start="4">
<li>Delete a ruleset</li>
</ol></h3>
<p>To delete a ruleset, refer to <a href="/ruleset-engine/rulesets-api/delete-rule/">Delete a rule in a ruleset</a>.</p>
<h2 id="cloudflare-dashboard">Cloudflare dashboard</h2>
<h3 id="enable-rules">Enable rules</h3>
<p>You can also use the dashboard to enable managed rulesets:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select <strong>Managed rulesets</strong>. This is where the dashboard lists all your managed rules.</li>
<li>To enable a rule, turn <strong>Status</strong> on.</li>
</ol>
<h3 id="edit-rules">Edit rules</h3>
<p>To edit a rule:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select <strong>Managed rulesets</strong>. This is where the dashboard lists all your managed rules.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Make the necessary changes, then select <strong>Save</strong>.</li>
</ol>
<h3 id="view-rules">View rules</h3>
<p>To view basic information about your rules:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select <strong>Managed rulesets</strong>. This is where the dashboard lists all your managed rules.</li>
<li>Locate your managed rule, select the three dots &gt; <strong>View</strong>.</li>
</ol>
