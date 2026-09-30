---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-security/8/
  description: '2025-04-09'
  full_title: Application security changelog - page 8 | Cloudflare Docs
  head_html: <title>Application security changelog - page 8 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-04-09"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-security/8/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application security changelog - page 8"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-04-09"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-security/8/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-security/8/#page","headline":"Application security changelog - page 8 | Cloudflare Docs","description":"2025-04-09","url":"https://developers.cloudflare.com/changelog/product-group/application-security/8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-security/8/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-secrets-store-now-available-in-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<p><em>2025-04-09</em></p>
<p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre tabindex="0"><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>


<h2 id="waf-release-2025-04-02"><a href="/changelog/post/2025-04-02-waf-release/">WAF Release - 2025-04-02</a></h2>
<p><em>2025-04-02</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8b8074e73b7d4aba92fc68f3622f0483">622f0483</code>
</td>
<td>100732</td>
<td>Sitecore - Code Injection - CVE:CVE-2025-27218</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8350947451a1401c934f5e660f101cca">0f101cca</code>
</td>
<td>100733</td>
<td>
				Angular-Base64-Upload - Remote Code Execution - CVE:CVE-2024-42640
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a9ec9cf625ff42769298671d1bbcd247">1bbcd247</code>
</td>
<td>100734</td>
<td>Apache Camel - Remote Code Execution - CVE:CVE-2025-29891</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3d6bf99039b54312a1a2165590aea1ca">90aea1ca</code>
</td>
<td>100735</td>
<td>
				Progress Software WhatsUp Gold - Remote Code Execution -
				CVE:CVE-2024-4885
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d104e3246dc14ac7851b4049d9d8c5f2">d9d8c5f2</code>
</td>
<td>100737</td>
<td>Apache Tomcat - Remote Code Execution - CVE:CVE-2025-24813</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="21c7a963e1b749e7b1753238a28a42c4">a28a42c4</code>
</td>
<td>100659</td>
<td>Common Payloads for Server-side Template Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="887843ffbe90436dadd1543adaa4b037">daa4b037</code>
</td>
<td>100659</td>
<td>Common Payloads for Server-side Template Injection - Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3565b80fc5b541b4832c0fc848f6a9cf">48f6a9cf</code>
</td>
<td>100642</td>
<td>LDAP Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="44d7bf9bf0fa4898b8579573e0713e9f">e0713e9f</code>
</td>
<td>100642</td>
<td>LDAP Injection Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e35c9a670b864a3ba0203ffb1bc977d1">1bc977d1</code>
</td>
<td>100005</td>
<td>
				DotNetNuke - File Inclusion - CVE:CVE-2018-9126, CVE:CVE-2011-1892,
				CVE:CVE-2022-31474
</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="cd8db44032694fdf8d6e22c1bb70a463">bb70a463</code>
</td>
<td>100527</td>
<td>Apache Struts - CVE:CVE-2021-31805</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0d838d9ab046443fa3f8b3e50c99546a">0c99546a</code>
</td>
<td>100702</td>
<td>Command Injection - CVE:CVE-2022-24108</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="533fbad558ce4c5ebcf013f09a5581d0">9a5581d0</code>
</td>
<td>100622C</td>
<td>
				Ivanti - Command Injection - CVE:CVE-2023-46805, CVE:CVE-2024-21887,
				CVE:CVE-2024-22024
</td>
<td>N/A</td>
<td>Block</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04176552f62f4b75bf65981206d0b009">06d0b009</code>
</td>
<td>100536C</td>
<td>GraphQL Command Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="25883bf28575433c952b830c1651d0c8">1651d0c8</code>
</td>
<td>100536</td>
<td>GraphQL Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7b70da1bb8d243bd80cd7a73af00f61d">af00f61d</code>
</td>
<td>100536A</td>
<td>GraphQL Introspection</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58c4853c250946359472b7eaa41e5b67">a41e5b67</code>
</td>
<td>100536B</td>
<td>GraphQL SSRF</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c241ed5f5bd44b19e17476b433e5b3d">433e5b3d</code>
</td>
<td>100559A</td>
<td>Prototype Pollution - Common Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="af748489e1c2411d80d855954816b26f">4816b26f</code>
</td>
<td>100559A</td>
<td>Prototype Pollution - Common Payloads - Base64</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ccc47ab7e34248c09546c284fcea5ed2">fcea5ed2</code>
</td>
<td>100734</td>
<td>Apache Camel - Remote Code Execution - CVE:CVE-2025-29891</td>
<td>N/A</td>
<td>Disabled</td>
<td>N/A</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-03-22-emergency"><a href="/changelog/post/2025-03-22-emergency-waf-release/">WAF Release - 2025-03-22 - Emergency</a></h2>
<p><em>2025-03-22</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="34583778093748cc83ff7b38f472013e">f472013e</code>
</td>
<td>100739</td>
<td>Next.js - Auth Bypass - CVE:CVE-2025-29927</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="new-managed-waf-rule-for-next-js-cve-2025-29927"><a href="/changelog/post/2025-03-22-next-js-vulnerability-waf/">New Managed WAF rule for Next.js CVE-2025-29927.</a></h2>
<p><em>2025-03-22</em></p>
<p><strong>Update: Mon Mar 24th, 11PM UTC</strong>: Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions <code>15.2.4</code>, <code>14.2.26</code>, <code>13.5.10</code> or <code>12.3.6</code>. <strong>If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation</strong>.</p>
<p><strong>Update: Mon Mar 24th, 8PM UTC</strong>: Next.js has now <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">backported the patch for this vulnerability</a> to cover Next.js v12 and v13. Users on those versions will need to patch to <code>13.5.9</code> and <code>12.3.5</code> (respectively) to mitigate the vulnerability.</p>
<p><strong>Update: Sat Mar 22nd, 4PM UTC</strong>: We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.</p>
<p><strong>We strongly recommend updating your version of Next.js (if eligible)</strong> to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-enable-the-managed-rule-strongly-recommended">Enable the Managed Rule (strongly recommended)</h4>
<p>This rule is opt-in only for sites on the Pro plan or above in the <a href="/waf/managed-rules/">WAF managed ruleset</a>.</p>
<p>To enable the rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Click the three dots next to <strong>Cloudflare Managed Ruleset</strong> and choose <strong>Edit</strong></li>
<li>Scroll down and choose <strong>Browse Rules</strong></li>
<li>Search for <strong>CVE-2025-29927</strong> (ruleId: <code>34583778093748cc83ff7b38f472013e</code>)</li>
<li>Change the <strong>Status</strong> to <strong>Enabled</strong> and the <strong>Action</strong> to <strong>Block</strong>. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.</li>
<li>Click <strong>Next</strong></li>
<li>Scroll down and choose <strong>Save</strong></li>
</ol>
<p>This will enable the WAF rule and block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-create-a-waf-rule-manual">Create a WAF rule (manual)</h4>
<p>For users on the Free plan, or who want to define a more specific rule, you can create a <a href="/waf/custom-rules/create-dashboard/">Custom WAF rule</a> to block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<p>To create a custom rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Give the rule a name - e.g. <code>next-js-CVE-2025-29927</code></li>
<li>Set the matching parameters for the rule match any request where the <code>x-middleware-subrequest</code> header <code>exists</code> per the rule expression below.</li>
</ol>
<pre tabindex="0"><code class="language-sh">(len(http.request.headers[&quot;x-middleware-subrequest&quot;]) &gt; 0)&#10;</code></pre>
<ol start="4">
<li>Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).</li>
<li><strong>Deploy</strong> the rule.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/workers/waf-rule-cve-2025-29927.png" alt="Next.js CVE-2025-29927 WAF rule" /></p>
<h4 id="2025-03-22-next-js-vulnerability-waf-next-js-cve-2025-29927">Next.js CVE-2025-29927</h4>
<p>We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">Next.js authentication bypass vulnerability</a> (<code>CVE-2025-29927</code>) published on March 21st, 2025.</p>
<p><strong>Note</strong>: This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.</p>
<ul>
<li>This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.</li>
<li>This rule has been made available (but not enabled by default) to all sites as part of our <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">WAF Managed Ruleset</a> and blocks requests that attempt to bypass authentication in Next.js applications.</li>
<li>The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js <code>14.2.26</code> and <code>15.2.4</code>. Earlier, interim releases did not fully patch this vulnerability.</li>
<li><strong>Users on older versions of Next.js (<code>11.1.4</code> to <code>13.5.6</code>) did not originally have a patch available</strong>, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions <code>12.3.6</code> and <code>13.5.10</code> as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.</li>
</ul>
<p>The managed WAF rule mitigates this by blocking <em>external</em> user requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.</p>


<h2 id="waf-release-2025-03-19-emergency"><a href="/changelog/post/2025-03-19-emergency-waf-release/">WAF Release - 2025-03-19 - Emergency</a></h2>
<p><em>2025-03-19</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="470b477e27244fddb479c4c7a2cafae7">a2cafae7</code>
</td>
<td>100736</td>
<td>Generic HTTP Request Smuggling</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="new-api-posture-management-for-api-shield"><a href="/changelog/post/2025-03-18-api-posture-management/">New API Posture Management for API Shield</a></h2>
<p><em>2025-03-18</em></p>
<p>Now, API Shield <strong>automatically</strong> labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.</p>
<p>View these risks in <a href="/api-shield/management-and-monitoring/">Endpoint Management</a> by label:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/endpoint-management-label.png" alt="A list of endpoint management labels" /></p>
<p>...or in <a href="/security/security-insights/">Security Center Insights</a>:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/posture-management-insight.png" alt="An example security center insight" /></p>
<p>API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:</p>
<ul>
<li><strong>cf-risk-sensitive</strong>: applied if the customer is subscribed to the <a href="/waf/managed-rules/reference/sensitive-data-detection/">sensitive data detection ruleset</a> and the WAF detects sensitive data returned on an endpoint in the last seven days.</li>
<li><strong>cf-risk-missing-auth</strong>: applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.</li>
<li><strong>cf-risk-mixed-auth</strong>: applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.</li>
<li><strong>cf-risk-missing-schema</strong>: added when a learned schema is available for an endpoint that has no active schema.</li>
<li><strong>cf-risk-error-anomaly</strong>: added when an endpoint experiences a recent increase in response errors over the last 24 hours.</li>
<li><strong>cf-risk-latency-anomaly</strong>: added when an endpoint experiences a recent increase in response latency over the last 24 hours.</li>
<li><strong>cf-risk-size-anomaly</strong>: added when an endpoint experiences a spike in response body size over the last 24 hours.</li>
</ul>
<p>In addition, API Shield has two new 'beta' scans for <strong>Broken Object Level Authorization (BOLA) attacks</strong>. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:</p>
<ul>
<li><strong>cf-risk-bola-enumeration</strong>: added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.</li>
<li><strong>cf-risk-bola-pollution</strong>: added when an endpoint experiences successful responses where parameters are found in multiple places in the request.</li>
</ul>
<p>We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/cloudflare-security-posture-management/">blog post</a> for more information about Cloudflare's expanded posture management capabilities.</p>


<h2 id="waf-release-2025-03-17"><a href="/changelog/post/2025-03-17-waf-release/">WAF Release - 2025-03-17</a></h2>
<p><em>2025-03-17</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28b2a12993a04e62a98abcd9e59ec18a">e59ec18a</code>
</td>
<td>100725</td>
<td>
				Fortinet FortiManager - Remote Code Execution - CVE:CVE-2023-42791,
				CVE:CVE-2024-23666
</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f253d755910e4998bd90365d1dbf58df">1dbf58df</code>
</td>
<td>100726</td>
<td>Ivanti - Remote Code Execution - CVE:CVE-2024-8190</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="19ae0094a8d845a1bb1997af0ad61fa7">0ad61fa7</code>
</td>
<td>100727</td>
<td>Cisco IOS XE - Remote Code Execution - CVE:CVE-2023-20198</td>
<td>Log</td>
<td>Disabled</td>
<td>Fixed action value in changelog; no rule changes.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="83a677f082264693ad64a2827ee56b66">7ee56b66</code>
</td>
<td>100728</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2024-46938</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="166b7ce85ce443538f021228a6752a38">a6752a38</code>
</td>
<td>100729</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2023-33160</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35fe23e7bd324d00816c82d098d47b69">98d47b69</code>
</td>
<td>100730</td>
<td>
				Pentaho - Template Injection - CVE:CVE-2022-43769, CVE:CVE-2022-43939
</td>
<td>Log</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2ce80fe815254f25b3c8f47569fe1e0d">69fe1e0d</code>
</td>
<td>100700</td>
<td>Apache SSRF vulnerability CVE-2021-40438</td>
<td>N/A</td>
<td>Block</td>
<td></td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-03-11-emergency"><a href="/changelog/post/2025-03-11-emergency-waf-release/">WAF Release - 2025-03-11 - Emergency</a></h2>
<p><em>2025-03-11</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0823d16dd8b94cc6b27a9ab173febb31">73febb31</code>
</td>
<td>100731</td>
<td>Apache Camel - Code Injection - CVE:CVE-2025-27636</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-03-10"><a href="/changelog/post/2025-03-10-waf-release/">WAF Release - 2025-03-10</a></h2>
<p><em>2025-03-10</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d4f68c1c65c448e58fe4830eb2a51e3d">b2a51e3d</code>
</td>
<td>100722</td>
<td>Ivanti - Information Disclosure - CVE:CVE-2025-0282</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fda130e396224ffc9f0a9e72259073d5">259073d5</code>
</td>
<td>100723</td>
<td>Cisco IOS XE - Information Disclosure - CVE:CVE-2023-20198</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="updated-leaked-credentials-database"><a href="/changelog/post/2025-03-07-updated-leaked-credentials-database/">Updated leaked credentials database</a></h2>
<p><em>2025-03-07</em></p>
<p>Added new records to the leaked credentials database. The record sources are: Have I Been Pwned (HIBP) database, RockYou 2024 dataset, and another third-party database.</p>


<h2 id="waf-release-2025-03-03"><a href="/changelog/post/2025-03-03-waf-release/">WAF Release - 2025-03-03</a></h2>
<p><em>2025-03-03</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="90356ececae3444b9accb3d393e63099">93e63099</code>
</td>
<td>100721</td>
<td>
				Ivanti - Remote Code Execution - CVE:CVE-2024-13159, CVE:CVE-2024-13160,
				CVE:CVE-2024-13161
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6cf09ce2fa73482abb7f677ecac42ce2">cac42ce2</code>
</td>
<td>100596</td>
<td>
				Citrix Content Collaboration ShareFile - Remote Code Execution -
				CVE:CVE-2023-24489
</td>
<td>N/A</td>
<td>Block</td>
<td></td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-02-24"><a href="/changelog/post/2025-02-24-waf-release/">WAF Release - 2025-02-24</a></h2>
<p><em>2025-02-24</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f7b9d265b86f448989fb0f054916911e">4916911e</code>
</td>
<td>100718A</td>
<td>SonicWall SSLVPN 2 - Auth Bypass - CVE:CVE-2024-53704</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="77c13c611d2a4fa3a89c0fafc382fdec">c382fdec</code>
</td>
<td>100720</td>
<td>Palo Alto Networks - Auth Bypass - CVE:CVE-2025-0108</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-02-18"><a href="/changelog/post/2025-02-18-waf-release/">WAF Release - 2025-02-18</a></h2>
<p><em>2025-02-18</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d1d45e4f59014f0fb22e0e6aa2ffa4b8">a2ffa4b8</code>
</td>
<td>100715</td>
<td>FortiOS - Auth Bypass - CVE:CVE-2024-55591</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="14b5cdeb4cde490ba37d83555a883e12">5a883e12</code>
</td>
<td>100716</td>
<td>Ivanti - Auth Bypass - CVE:CVE-2021-44529</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="498fcd81a62a4b5ca943e2de958094d3">958094d3</code>
</td>
<td>100717</td>
<td>SimpleHelp - Auth Bypass - CVE:CVE-2024-57727</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6e0d8afc36ba4ce9836f81e63b66df22">3b66df22</code>
</td>
<td>100718</td>
<td>SonicWall SSLVPN - Auth Bypass - CVE:CVE-2024-53704</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8eb4536dba1a4da58fbf81c79184699f">9184699f</code>
</td>
<td>100719</td>
<td>Yeti Platform - Auth Bypass - CVE:CVE-2024-46507</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="upload-a-certificate-bundle-with-an-rsa-and-ecdsa-certificate-per-custom-hostname"><a href="/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/">Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname</a></h2>
<p><em>2025-02-14</em></p>
<p>Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.</p>
<p>Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.</p>
<pre tabindex="0"><code>curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;d &#x27;{&#10;    &quot;hostname&quot;: &quot;hostname&quot;,&#10;    &quot;ssl&quot;: {&#10;        &quot;custom_cert_bundle&quot;: [&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;RSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;RSA Key&quot;&#10;            },&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;ECDSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;ECDSA Key&quot;&#10;            }&#10;        ],&#10;        &quot;bundle_method&quot;: &quot;force&quot;,&#10;        &quot;wildcard&quot;: false,&#10;        &quot;settings&quot;: {&#10;            &quot;min_tls_version&quot;: &quot;1.0&quot;&#10;        }&#10;    }&#10;}’&#10;</code></pre>
<p>You can also:</p>
<ul>
<li>
<p><a href="/api/resources/custom_hostnames/methods/create/">Upload</a> an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/">Replace</a> the RSA or ECDSA certificate with a certificate of its same type.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/">Delete</a> the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).</p>
</li>
</ul>
<p>This feature is available for Business and Enterprise customers who have purchased custom certificates.</p>


<h2 id="increased-cloudflare-rules-limits"><a href="/changelog/post/2025-02-12-rules-upgraded-limits/">Increased Cloudflare Rules limits</a></h2>
<p><em>2025-02-12</em></p>
<p>We have upgraded and streamlined <a href="/rules/">Cloudflare Rules</a> limits across all plans, simplifying rule management and improving scalability for everyone.</p>
<p><strong>New limits by product:</strong></p>
<ul>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>
<ul>
<li>Free: <strong>20</strong> → <strong>10,000</strong> URL redirects across lists</li>
<li>Pro: <strong>500</strong> → <strong>25,000</strong> URL redirects across lists</li>
<li>Business: <strong>500</strong> → <strong>50,000</strong> URL redirects across lists</li>
<li>Enterprise: <strong>10,000</strong> → <strong>1,000,000</strong> URL redirects across lists</li>
</ul>
</li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a>
<ul>
<li>Free: <strong>5</strong> → <strong>10</strong> connectors</li>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> connectors</li>
</ul>
</li>
<li><a href="/rules/custom-errors/">Custom Errors</a>
<ul>
<li>Pro: <strong>5</strong> → <strong>25</strong> error assets and rules</li>
<li>Business: <strong>20</strong> → <strong>50</strong> error assets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> error assets and rules</li>
</ul>
</li>
<li><a href="/rules/snippets/">Snippets</a>
<ul>
<li>Pro: <strong>10</strong> → <strong>25</strong> code snippets and rules</li>
<li>Business: <strong>25</strong> → <strong>50</strong> code snippets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> code snippets and rules</li>
</ul>
</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, and <a href="/rules/transform/">Transform Rules</a>
<ul>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> rules</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-rules-upgraded-limits-gradual-rollout">Gradual rollout</h4>
@markup("md", "content/.markup/bodies/17745.md")</aside>


<h2 id="custom-errors-beta-stored-assets-account-level-rules"><a href="/changelog/post/2025-02-11-custom-errors-beta/">Custom Errors (beta): Stored Assets & Account-level Rules</a></h2>
<p><em>2025-02-11</em></p>
<p>We're introducing <a href="/rules/custom-errors/">Custom Errors</a> (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.</p>
<p>This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.</p>
<p>This brings the following new capabilities:</p>
<ul>
<li><strong>Custom error assets</strong> – Fetch and store external error pages at the edge for use in error responses.</li>
<li><strong>Account-Level custom errors</strong> – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.</li>
</ul>
<p>You can use Cloudflare API to upload your existing assets for use with Custom Errors:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;maintenance&quot;,&#10;  &quot;description&quot;: &quot;Maintenance template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<p>You can then reference the stored asset in a Custom Error rule:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;serve_error&quot;,&#10;			&quot;action_parameters&quot;: {&#10;				&quot;asset_name&quot;: &quot;maintenance&quot;,&#10;				&quot;content_type&quot;: &quot;text/html&quot;,&#10;				&quot;status_code&quot;: 503&#10;			},&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;http.request.uri.path contains \&quot;error\&quot;&quot;&#10;		}&#10;	]&#10;}&#x27;&#10;</code></pre>


<h2 id="waf-release-2025-02-11"><a href="/changelog/post/2025-02-11-waf-release/">WAF Release - 2025-02-11</a></h2>
<p><em>2025-02-11</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="742306889c2e4f6087de6646483b4c26">483b4c26</code>
</td>
<td>100708</td>
<td>Aviatrix Network - Remote Code Execution - CVE:CVE-2024-50603</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="042228dffe0a4f1587da0e737e924ca3">7e924ca3</code>
</td>
<td>100709</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2024-46982</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2a12278325464d6682afb53483a7d8ff">83a7d8ff</code>
</td>
<td>100710</td>
<td>
				Progress Software WhatsUp Gold - Directory Traversal -
				CVE:CVE-2024-12105
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="82ce3424fbe84e9e99d77332baa8eb34">baa8eb34</code>
</td>
<td>100711</td>
<td>WordPress - Remote Code Execution - CVE:CVE-2024-56064</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5afacd39dcfd42f89a6c43f787f5d34e">87f5d34e</code>
</td>
<td>100712</td>
<td>WordPress - Remote Code Execution - CVE:CVE-2024-9047</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="05842b06f0a4415880b58f7fbf72cf8a">bf72cf8a</code>
</td>
<td>100713</td>
<td>FortiOS - Auth Bypass - CVE:CVE-2022-40684</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="updated-leaked-credentials-database-1"><a href="/changelog/post/2025-02-04-updated-leaked-credentials-database/">Updated leaked credentials database</a></h2>
<p><em>2025-02-04</em></p>
<p>Added new records to the leaked credentials database from a third-party database.</p>


<h2 id="new-snippets-code-editor"><a href="/changelog/post/2025-01-29-snippets-code-editor/">New Snippets Code Editor</a></h2>
<p><em>2025-01-29</em></p>
<p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>


<h2 id="waf-release-2025-01-21"><a href="/changelog/post/2025-01-21-waf-release/">WAF Release - 2025-01-21</a></h2>
<p><em>2025-01-21</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f4a310393c564d50bd585601b090ba9a">b090ba9a</code>
</td>
<td>100303</td>
<td>Command Injection - Nslookup</td>
<td>Log</td>
<td>Block</td>
<td>
				This was released as <code class="nb-rule-id" title="aad6f9f85e034022b6a8dee4b8d152f4">b8d152f4</code>
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fd5d5678ce594ea898aa9bf149e6b538">49e6b538</code>
</td>
<td>100534</td>
<td>Web Shell Activity</td>
<td>Log</td>
<td>Block</td>
<td>
				This was released as <code class="nb-rule-id" title="39c8f6066c19466ea084e51e82fe4e7f">82fe4e7f</code>
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-01-13"><a href="/changelog/post/2025-01-13-waf-release/">WAF Release - 2025-01-13</a></h2>
<p><em>2025-01-13</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6e0bfbe4b9c6454c8bd7bd24f49e5840">f49e5840</code>
</td>
<td>100704</td>
<td>
				Cleo Harmony - Auth Bypass - CVE:CVE-2024-55956, CVE:CVE-2024-55953
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c993997b7d904a9e89448fe6a6d43bc2">a6d43bc2</code>
</td>
<td>100705</td>
<td>Sentry - SSRF</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f40ce742be534ba19d610961ce6311bb">ce6311bb</code>
</td>
<td>100706</td>
<td>Apache Struts - Remote Code Execution - CVE:CVE-2024-53677</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="67ac639a845c482d948b465b2233da1f">2233da1f</code>
</td>
<td>100707</td>
<td>
				FortiWLM - Remote Code Execution - CVE:CVE-2023-48782,
				CVE:CVE-2023-34993, CVE:CVE-2023-34990
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="870cca2b874d41738019d4c3e31d972a">e31d972a</code>
</td>
<td>100007C_BETA</td>
<td>Command Injection - Common Attack Commands</td>
<td></td>
<td>Disabled</td>
<td></td>
</tr>
</tbody>
</table>


<h2 id="new-rules-overview-interface"><a href="/changelog/post/2025-01-09-rules-overview/">New Rules Overview Interface</a></h2>
<p><em>2025-01-09</em></p>
<p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>


<h2 id="waf-release-2025-01-06"><a href="/changelog/post/2025-01-06-waf-release/">WAF Release - 2025-01-06</a></h2>
<p><em>2025-01-06</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="3a321b10270b42549ac201009da08beb">9da08beb</code>
</td>
<td>100678</td>
<td>Pandora FMS - Remote Code Execution - CVE:CVE-2024-11320</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="1fe510368b4a47dda90363c2ecdf3d02">ecdf3d02</code>
</td>
<td>100679</td>
<td>
				Palo Alto Networks - Remote Code Execution - CVE:CVE-2024-0012,
				CVE:CVE-2024-9474
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="b7ba636927b44ee288b9a697a40f2a35">a40f2a35</code>
</td>
<td>100680</td>
<td>Ivanti - Command Injection - CVE:CVE-2024-37397</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="6bd9b07c8acc4beeb17c8bee58ae3c89">58ae3c89</code>
</td>
<td>100681</td>
<td>Really Simple Security - Auth Bypass - CVE:CVE-2024-10924</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c86e79e15a4a4307870f6f77e37f2da6">e37f2da6</code>
</td>
<td>100682</td>
<td>Magento - XXE - CVE:CVE-2024-34102</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="945f41b48be9485f953116015054c752">5054c752</code>
</td>
<td>100683</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51567</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="aec9a2e554a34a8fa547d069dfe93d7b">dfe93d7b</code>
</td>
<td>100684</td>
<td>
				Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38094,
				CVE:CVE-2024-38024, CVE:CVE-2024-38023
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="e614dd46c1ce404da1909e841454c856">1454c856</code>
</td>
<td>100685</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51568</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="685a4edf68f740b4a2c80d45e92362e5">e92362e5</code>
</td>
<td>100686</td>
<td>Seeyon - Remote Code Execution</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="204f9d948a124829acb86555b9f1c9f8">b9f1c9f8</code>
</td>
<td>100687</td>
<td>
				WordPress - Remote Code Execution - CVE:CVE-2024-10781,
				CVE:CVE-2024-10542
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="19587024724e49329d5b482d0d7ca374">0d7ca374</code>
</td>
<td>100688</td>
<td>ProjectSend - Remote Code Execution - CVE:CVE-2024-11680</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="fa49213e55484f6c824e0682a5260b70">a5260b70</code>
</td>
<td>100689</td>
<td>
				Palo Alto GlobalProtect - Remote Code Execution - CVE:CVE-2024-5921
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="11b5fc23e85b41ca90316bddd007118b">d007118b</code>
</td>
<td>100690</td>
<td>Ivanti - Remote Code Execution - CVE:CVE-2024-37404</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="aaeada52bcc840598515de6cc3e49f64">c3e49f64</code>
</td>
<td>100691</td>
<td>Array Networks - Remote Code Execution - CVE:CVE-2023-28461</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="e2c7ce1ecd6847219f8d9aedfcc6f5bb">fcc6f5bb</code>
</td>
<td>100692</td>
<td>CyberPanel - Remote Code Execution - CVE:CVE-2024-51378</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="84d481b1f49c4735afa2fb2bb615335e">b615335e</code>
</td>
<td>100693</td>
<td>Symfony Profiler - Auth Bypass - CVE:CVE-2024-50340</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="9f258f463f9f4b26ad07e3c209d08c8a">09d08c8a</code>
</td>
<td>100694</td>
<td>Citrix Virtual Apps - Remote Code Execution - CVE:CVE-2024-8069</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="b490d6edcfec4028aef45cf08aafb2f5">8aafb2f5</code>
</td>
<td>100695</td>
<td>MSMQ Service - Remote Code Execution - CVE:CVE-2023-21554</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c8f65bc9eeef4665820ecfe411b7a8c7">11b7a8c7</code>
</td>
<td>100696</td>
<td>Nginxui - Remote Code Execution - CVE:CVE-2024-49368</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="d5f2e133e34640198d06d7b345954c7e">45954c7e</code>
</td>
<td>100697</td>
<td>
				Apache ShardingSphere - Remote Code Execution - CVE:CVE-2022-22733
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="c34432e257074cffa9fa15f3f5311209">f5311209</code>
</td>
<td>100698</td>
<td>Mitel MiCollab - Auth Bypass - CVE:CVE-2024-41713</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Specials</td>
<td>
				<code class="nb-rule-id" title="3bda15acd73a4b55a5f60cd2b3e5e46e">b3e5e46e</code>
</td>
<td>100699</td>
<td>Apache Solr - Auth Bypass - CVE:CVE-2024-45216</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
</tbody>
</table>


<h2 id="troubleshoot-tunnels-with-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<p><em>2024-12-19</em></p>
<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="terraform-support-for-snippets"><a href="/changelog/post/2024-12-11-terraform-snippets/">Terraform Support for Snippets</a></h2>
<p><em>2024-12-11</em></p>
<p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/7/">Previous</a><span>Page 8 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/9/">Next</a></nav>
