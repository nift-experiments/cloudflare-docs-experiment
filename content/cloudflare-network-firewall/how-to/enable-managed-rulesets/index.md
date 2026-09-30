---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/
  description: Enable managed rulesets for the Network Firewall.
  full_title: Enable Managed Rulesets · Cloudflare Network Firewall docs
  head_html: <title>Enable Managed Rulesets · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable managed rulesets for the Network Firewall."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/index.md"><meta property="og:title" content="Enable Managed Rulesets · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable managed rulesets for the Network Firewall."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/#page","headline":"Enable Managed Rulesets \u00b7 Cloudflare Network Firewall docs","description":"Enable managed rulesets for the Network Firewall.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/how-to/enable-managed-rulesets/
  schema: 1
---
<p>With <a href="/ruleset-engine/managed-rulesets/">managed rulesets</a>, you can quickly deploy rules maintained by Cloudflare, and you can use Cloudflare Network Firewall (formerly Magic Firewall) to control which rules are enabled.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/4267.md")
</aside>
<p>To enable or disable a rule, you can specify which properties should be overridden. The overrides occur in the Managed phase, root kind ruleset. Currently, you can only have one rule in the root ruleset, but a single rule can contain multiple overrides.</p>
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
<li><code>managed_ruleset_id</code>: The ID of the Managed phase Managed kind ruleset that contains the rule you want to enable.</li>
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
<p>To ensure a root kind ruleset only contains one rule, patch the rule to enable new managed rules.</p>
<p>Building off the example from the previous step, the example below enables a category to select multiple rules instead of a single rule. The category will be set to <code>log</code> mode, which means the rule can produce logs but will not accept or drop packets.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{root_kind_ruleset}/rules/{root_kind_rule} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;    &quot;version&quot;: &quot;latest&quot;,&#10;    &quot;overrides&quot;: {&#10;      &quot;rules&quot;: [&#10;        {&#10;          &quot;id&quot;: &quot;&lt;MANAGED_RULE_ID&gt;&quot;,&#10;          &quot;enabled&quot;: true&#10;        }&#10;      ],&#10;      &quot;categories&quot;: [&#10;        {&#10;          &quot;category&quot;: &quot;simple&quot;,&#10;          &quot;enabled&quot;: true,&#10;          &quot;action&quot;: &quot;log&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="3-enable-all-rules"><ol start="3">
<li>Enable all rules</li>
</ol></h3>
<p>To enable the complete ruleset or enable all rules, send the request below.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}{account_id}/rulesets/{root_kind_ruleset}/rules/{root_kind_rule} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;    &quot;version&quot;: &quot;latest&quot;,&#10;    &quot;overrides&quot;: {&#10;      &quot;enabled&quot;: true&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="4-delete-a-ruleset"><ol start="4">
<li>Delete a ruleset</li>
</ol></h3>
<p>To delete a ruleset, refer to <a href="/ruleset-engine/rulesets-api/delete-rule/">Delete a rule in a ruleset</a>.</p>
<h2 id="cloudflare-dashboard">Cloudflare dashboard</h2>
<p>You can also use the dashboard to enable managed rulesets.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall/managed">Firewall Policies</a> page.</li>
<li>In the <strong>Managed rulesets</strong> tab, select <strong>Deploy managed ruleset</strong>.</li>
<li>The page will refresh and show you rulesets configured by Cloudflare that are available to your account. Choose the ruleset you want with <strong>Manage</strong>. If the ruleset you want is not displayed, contact your account manager to get a list of all Network Firewall Managed rulesets.</li>
<li>Under <strong>Ruleset configuration</strong>, configure the <strong>Ruleset action</strong> from the drop-down menu. Cloudflare recommends you change this setting to <strong>Log</strong> to evaluate how the ruleset impacts your traffic before deciding on an action. For more information, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a>.</li>
<li>Still under <strong>Ruleset configuration</strong>, choose <em>Enabled</em> from the dropdown-menu for the <strong>Ruleset status</strong>. This will apply an override to the default status of all the rules in the ruleset.</li>
<li>Select <strong>Save</strong> to deploy the Network Firewall Managed ruleset with no rule-level overrides.</li>
</ol>
<h3 id="add-rule-level-overrides">Add rule-level overrides</h3>
<p>Applying a rule-level override allows you to customize the behavior of the managed ruleset. If you implemented Cloudflare's above recommendation for the ruleset configuration, the rules will be set to a <strong>Log</strong> action and an <strong>Enabled</strong> status.</p>
<p>On the other hand, if you did not apply Cloudflare's recommendation in the previous step, the ruleset is implemented with all its defaults applied.</p>
<p>To add rule-level overrides in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall/managed">Firewall Policies</a> page.</li>
<li>In the <strong>Managed rulesets</strong> tab, locate the Network Firewall managed ruleset you want to add rule-overrides to and select <strong>Manage</strong>.</li>
<li>Select <strong>Browse rules</strong>.</li>
<li>In the rule you need to change, select an <strong>Action</strong> from the drop-down to change its action, or use the toggle to disable or enable the rule.</li>
<li>Select <strong>Next</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The Cloudflare dashboard should now show you the rule-level override you have set.</p>
<h3 id="delete-network-firewall-managed-ruleset">Delete Network Firewall managed ruleset</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall/managed">Firewall Policies</a> page.</li>
<li>In the <strong>Managed rulesets</strong> tab, locate the Network Firewall managed ruleset you want to delete and select <strong>Manage</strong>.</li>
<li>Select <strong>Delete deployment</strong>.</li>
</ol>
<p>Your Cloudflare Network Firewall managed ruleset is now deleted.</p>
