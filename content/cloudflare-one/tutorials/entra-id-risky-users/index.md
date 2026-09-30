---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/
  description: Microsoft Entra ID (formerly Azure Active Directory) calculates a user's risk level based on the probability that their account has been compromised. With Cloudflare Zero Trust, you can synchronize the Entra ID risky users list with Cloudflare Access and apply more stringent Zero Trust policies to users at higher risk.
  full_title: Isolate risky Entra ID users · Cloudflare One docs
  head_html: <title>Isolate risky Entra ID users · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Microsoft Entra ID (formerly Azure Active Directory) calculates a user&#x27;s risk level based on the probability that their account has been compromised. With Cloudflare Zero Trust, you can synchronize the Entra ID risky users list with Cloudflare Access and apply more stringent Zero Trust policies to users at higher risk."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/index.md"><meta property="og:title" content="Isolate risky Entra ID users · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Microsoft Entra ID (formerly Azure Active Directory) calculates a user&#x27;s risk level based on the probability that their account has been compromised. With Cloudflare Zero Trust, you can synchronize the Entra ID risky users list with Cloudflare Access and apply more stringent Zero Trust policies to users at higher risk."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft Entra ID,SCIM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/#page","headline":"Isolate risky Entra ID users \u00b7 Cloudflare One docs","description":"Microsoft Entra ID (formerly Azure Active Directory) calculates a user's risk level based on the probability that their account has been compromised. With Cloudflare Zero Trust, you can synchronize the Entra ID risky users list with Cloudflare Access and apply more stringent Zero Trust policies to users at higher risk.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-risky-users/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft Entra ID","SCIM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/entra-id-risky-users/
  schema: 1
---
<p>Microsoft Entra ID (formerly Azure Active Directory) calculates a user's <a href="https://learn.microsoft.com/entra/id-protection/howto-identity-protection-investigate-risk">risk level</a> based on the probability that their account has been compromised. With Cloudflare Zero Trust, you can synchronize the Entra ID risky users list with Cloudflare Access and apply more stringent Zero Trust policies to users at higher risk.</p>
<p>This tutorial demonstrates how to automatically redirect users to a remote browser when they are deemed risky by Entra ID.</p>
<p><strong>Time to complete:</strong></p>
<p>1 hour</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Microsoft Entra ID Premium P2 license</li>
<li><a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a> add-on</li>
<li><a href="/cloudflare-one/traffic-policies/get-started/http/">Gateway HTTP filtering</a> enabled on your devices</li>
<li><a href="https://docs.npmjs.com/getting-started">npm</a> installation</li>
<li><a href="https://nodejs.org/en/">Node.js</a> installation</li>
</ul>
<h2 id="1-set-up-entra-id-as-an-identity-provider"><ol>
<li>Set up Entra ID as an identity provider</li>
</ol></h2>
<p>Refer to <a href="/cloudflare-one/integrations/identity-providers/entra-id/#set-up-entra-id-as-an-identity-provider">our IdP setup instructions</a> for Entra ID.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4303.md")
</aside>
<h2 id="2-add-entra-id-api-permissions"><ol start="2">
<li>Add Entra ID API permissions</li>
</ol></h2>
<p>Once the base IdP integration is tested and working, enable additional permissions that will allow a script to create and update risky user groups in Entra ID:</p>
<ol>
<li>
<p>In Microsoft Entra ID, go to <strong>App registrations</strong>.</p>
</li>
<li>
<p>Select the application you created for the IdP integration.</p>
</li>
<li>
<p>Go to <strong>API permissions</strong> and select <strong>Add a permission</strong>.</p>
</li>
<li>
<p>Select <strong>Microsoft Graph</strong>.</p>
</li>
<li>
<p>Select <strong>Application permissions</strong> and add the following <a href="https://learn.microsoft.com/en-us/graph/permissions-reference">permissions</a>:</p>
<ul>
<li><code>IdentityRiskyUser.ReadAll</code></li>
<li><code>Directory.ReadWriteAll</code></li>
<li><code>Group.Create</code></li>
<li><code>Group.ReadAll</code></li>
<li><code>GroupMember.ReadAll</code></li>
<li><code>GroupMember.ReadWriteAll</code></li>
</ul>
</li>
<li>
<p>Select <strong>Grant admin consent</strong>.</p>
</li>
</ol>
<p>You will see the list of enabled permissions.</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/risky-users-permissions.png" alt="API permissions in Entra ID" /></p>
<h2 id="3-add-risky-users-to-entra-id-group"><ol start="3">
<li>Add risky users to Entra ID group</li>
</ol></h2>
<p>Next, configure an automated script that will populate an Entra ID security group with risky users.</p>
<p>To get started quickly, deploy our example Cloudflare Workers script by following the step-by-step instructions below. Alternatively, you can implement the script using <a href="https://learn.microsoft.com/azure/azure-functions/functions-overview">Azure Functions</a> or any other tool.</p>
<ol>
<li>Open a terminal and clone our example project.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest risky-users -- --template https://github.com/cloudflare/msft-risky-user-ad-sync&#10;</code></pre>
<ol start="2">
<li>Go to the project directory.</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd risky-users&#10;</code></pre>
<ol start="3">
<li>Modify the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to include the following values:
<ul>
<li><code>&lt;ACCOUNT_ID&gt;</code>: your Cloudflare <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
<li><code>&lt;TENANT_ID&gt;</code>: your Entra ID <strong>Directory (tenant) ID</strong>, obtained when <a href="#1-set-up-entra-id-as-an-identity-provider">setting up Entra ID as an identity provider</a>.</li>
<li><code>&lt;CLIENT_ID&gt;</code>: your Entra ID <strong>Application (client) ID</strong>, obtained when <a href="#1-set-up-entra-id-as-an-identity-provider">setting up Entra ID as an identity provider</a>.</li>
</ul>
</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4304.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4302.md")
</aside>
<ol start="4">
<li>Deploy the Worker to Cloudflare's global network.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="5">
<li>Create a secret variable named <code>AZURE_AD_CLIENT_SECRET</code>.</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler secret put AZURE_AD_CLIENT_SECRET&#10;</code></pre>
<p>You will be prompted to input the secret's value. Enter the <strong>Client secret</strong> obtained when <a href="#1-set-up-azure-ad-as-an-identity-provider">setting up Microsoft Entra ID as an identity provider</a>.</p>
<p>The Worker script will begin executing once per minute. To view realtime logs, run the following command and wait for the script to execute:</p>
<pre tabindex="0"><code class="language-sh">wrangler tail --format pretty&#10;</code></pre>
<p>After the initial run, the auto-generated groups will appear in the Entra ID dashboard.</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/risky-users-groups.png" alt="Risky user groups in the Entra ID dashboard" /></p>
<h2 id="4-synchronize-risky-user-groups"><ol start="4">
<li>Synchronize risky user groups</li>
</ol></h2>
<p>Next, synchronize Entra ID risky user groups with Cloudflare Access:</p>
<ol>
<li>
<p><a href="/cloudflare-one/integrations/identity-providers/entra-id/#synchronize-users-and-groups">Enable SCIM synchronization</a>.</p>
</li>
<li>
<p>In Entra ID, assign the following groups to your SCIM enterprise application:</p>
<ul>
<li><code>IdentityProtection-RiskyUser-RiskLevel-high</code></li>
<li><code>IdentityProtection-RiskyUser-RiskLevel-medium</code></li>
<li><code>IdentityProtection-RiskyUser-RiskLevel-low</code></li>
</ul>
</li>
</ol>
<p>Cloudflare Access will now synchronize changes in group membership with Entra ID. You can verify the synchronization status on the SCIM application's <strong>Provisioning</strong> page.</p>
<h2 id="5-create-a-browser-isolation-policy"><ol start="5">
<li>Create a browser isolation policy</li>
</ol></h2>
<p>Finally, create a <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policy</a> to isolate traffic for risky user groups.</p>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Build an <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Isolate policy</a> that contains a <em>User Group Names</em> rule. For example, the following policy serves <code>app1.example.com</code> and <code>app2.example.com</code> in a remote browser for all members flagged as high risk:</p>
</li>
</ol>
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
<td>Domain</td>
<td>in</td>
<td><code>app1.example.com</code>, <code>app2.example.com</code></td>
<td>And</td>
<td>Isolate</td>
</tr>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><code>IdentityProtection-RiskyUser-RiskLevel-high</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>To test the policy, refer to the Microsoft documentation for <a href="https://learn.microsoft.com/entra/id-protection/howto-identity-protection-simulate-risk">simulating risky detections</a>.</p>
