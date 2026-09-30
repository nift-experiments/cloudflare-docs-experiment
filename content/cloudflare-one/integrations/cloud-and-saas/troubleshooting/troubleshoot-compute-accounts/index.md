---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/
  description: Troubleshoot Troubleshoot compute accounts issues in Zero Trust integrations.
  full_title: Troubleshoot compute accounts · Cloudflare One docs
  head_html: <title>Troubleshoot compute accounts · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Troubleshoot compute accounts issues in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/index.md"><meta property="og:title" content="Troubleshoot compute accounts · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Troubleshoot compute accounts issues in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AWS,GCP,Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/#page","headline":"Troubleshoot compute accounts \u00b7 Cloudflare One docs","description":"Troubleshoot Troubleshoot compute accounts issues in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS","GCP","Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/
  schema: 1
---
<p>Cloudflare CASB detects when compute accounts are unhealthy or outdated. Common compute account issues include security or functionality updates and API token misconfigurations.</p>
<h2 id="identify-unhealthy-compute-accounts">Identify unhealthy compute accounts</h2>
<p>To identify unhealthy compute accounts:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose the integration you created for cloud scanning.</li>
<li>Select <strong>Manage compute accounts</strong>.</li>
</ol>
<p>CASB will display the status of each compute account next to its name. If a compute account is broken or outdated, CASB will set its status to <strong>Unhealthy</strong>. If the status is <strong>Healthy</strong>, no action is required.</p>
<h2 id="repair-an-unhealthy-compute-account">Repair an unhealthy compute account</h2>
<p>When CASB marks a compute account as <strong>Unhealthy</strong>, CASB will not use new scan configuration changes and new scan results will not appear in the dashboard.</p>
<p>To repair a compute account marked as <strong>Unhealthy</strong>, first <a href="#upgrade-a-compute-account">upgrade the compute account</a>. If the compute account is still unhealthy, <a href="#roll-api-tokens">roll your API token</a>.</p>
<h2 id="upgrade-a-compute-account">Upgrade a compute account</h2>
<p>Upgrading a compute account applies the latest software features, bug fixes, and infrastructure changes to a cloud compute account. You should run upgrades periodically to keep the compute account software up to date or when recommended by Cloudflare to address an issue. CASB deploys compute account upgrades through Terraform updates.</p>
<p>To upgrade a compute account:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS integrations</strong>.</li>
<li>Choose the integration you created for cloud scanning.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to validate your local Terraform and CLI configuration.</li>
<li>Under <strong>Step 2: Deploy Terraform Configuration</strong>, copy the template to your local configuration. This template will be the most up to date version of the integration's Terraform configuration.</li>
<li>In a local terminal, update the cached version of the CDS Terraform modules:</li>
</ol>
<pre tabindex="0"><code class="language-bash">terraform init --upgrade&#10;</code></pre>
<ol start="7">
<li>Apply the upgraded Terraform configuration to your compute account:</li>
</ol>
<pre tabindex="0"><code class="language-bash">terraform apply&#10;</code></pre>
<h2 id="roll-api-tokens">Roll API tokens</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5100.md")
</aside>
<p>You may need to roll the Cloudflare API token used for your compute account if a security or operational issue appears, your API token is compromised, or your API token is removed from your compute account.</p>
<p>If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>To roll your API token:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Next to the API token you want to roll, select the <strong>three dot icon</strong> &gt; <strong>Roll</strong>.</p>
</li>
<li>
<p>Select <strong>Confirm</strong> to generate a new API token.</p>
</li>
<li>
<p>Copy your API token.</p>
</li>
</ol>
<p>Once you roll your API token in Cloudflare, you can update the API token value in your secrets manager for <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret-value.html">Amazon Web Services (AWS)</a> or <a href="https://cloud.google.com/secret-manager/docs/edit-secrets">Google Cloud Platform (GCP)</a>.</p>
<h3 id="common-token-issues">Common token issues</h3>
<h4 id="cloudflare-cds-secrets-does-not-exist-in-the-compute-account-s-secrets-manager"><code>cloudflare-cds-secrets</code> does not exist in the compute account's secrets manager</h4>
<p>To recreate the secret in your compute account:</p>
<ol>
<li>Validate that you selected the correct region.</li>
<li><a href="#upgrade-a-compute-account">Upgrade the compute account</a> to recreate the secret.</li>
<li><a href="#roll-api-tokens">Update the secret value</a> in your compute account.</li>
</ol>
<h4 id="i-no-longer-have-access-to-the-cloudflare-api-token-i-created">I no longer have access to the Cloudflare API token I created</h4>
<p><a href="#roll-api-tokens">Roll your Cloudflare API token</a> and add it to your compute account. If the <a href="#identify-unhealthy-compute-accounts">status of the compute account</a> is set to <strong>Healthy</strong>, the issue has been solved.</p>
