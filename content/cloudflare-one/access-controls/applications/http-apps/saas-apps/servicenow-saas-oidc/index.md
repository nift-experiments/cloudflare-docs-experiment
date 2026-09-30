---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/
  description: Integrate ServiceNow (OIDC) with Access.
  full_title: ServiceNow (OIDC) · Cloudflare One docs
  head_html: <title>ServiceNow (OIDC) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate ServiceNow (OIDC) with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/index.md"><meta property="og:title" content="ServiceNow (OIDC) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate ServiceNow (OIDC) with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="ServiceNow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/#page","headline":"ServiceNow (OIDC) \u00b7 Cloudflare One docs","description":"Integrate ServiceNow (OIDC) with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["ServiceNow"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-oidc/
  schema: 1
---
<p>This guide covers how to configure <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/task/create-OIDC-configuration-SSO.html">ServiceNow</a> as an OIDC application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a ServiceNow account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>ServiceNow</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>OIDC</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>In <strong>Scopes</strong>, select the attributes that you want Access to send in the ID token.</li>
<li>In <strong>Redirect URLs</strong>, enter <code>https://&lt;INSTANCE-NAME&gt;.service-now.com/navpage.do</code>.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</li>
<li>Copy the <strong>Client secret</strong> and <strong>Client ID</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>(Optional) In <strong>Experience settings</strong>, configure <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher settings</a> by turning on <strong>Enable App in App Launcher</strong> and, in <strong>App Launcher URL</strong>, entering <code>https://&lt;INSTANCE-NAME&gt;.service-now.com</code>.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-the-multiple-provider-single-sign-on-installer-plugin-to-servicenow"><ol start="2">
<li>Add the Multiple Provider Single Sign-On Installer Plugin to ServiceNow</li>
</ol></h2>
<ol>
<li>In ServiceNow, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>System Applications</code>, and under <strong>All Available Applications</strong>, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>Integration - Multiple Provider Single Sign-On Installer</code>.</li>
<li>Select <strong>Install</strong>.</li>
<li>Ensure that <strong>Install now</strong> is selected, and select <strong>Install</strong>.</li>
</ol>
<h2 id="3-add-and-test-an-oidc-sso-provider-in-servicenow"><ol start="3">
<li>Add and Test an OIDC SSO provider in ServiceNow</li>
</ol></h2>
<ol>
<li>Select <strong>All</strong>.</li>
<li>In the search bar enter <code>Multi-Provider SSO</code>, and select <strong>Identity Providers</strong>.</li>
<li>Select <strong>New</strong> &gt; <strong>OpenID Connect</strong>.</li>
<li>In the pop-up, fill in the following fields:
<ul>
<li><strong>Name</strong>: Name of the SSO (for example, <code>Cloudflare Access</code>). Unless otherwise configured, users will select this name when signing in to ServiceNow.</li>
<li><strong>Client ID</strong>: <strong>Client ID</strong> from application configuration in Cloudflare One.</li>
<li><strong>Client Secret</strong>: <strong>Client Secret</strong> from application configuration in Cloudflare One.</li>
<li><strong>Well Known Configuration URL</strong>: <code>https://&lt;TEAM-DOMAIN&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;CLIENT-ID&gt;/.well-known/openid-configuration</code>.</li>
</ul>
</li>
<li>Select <strong>Import</strong>.</li>
<li>Ensure <strong>Active</strong> is turned on</li>
<li>Turn on <strong>Show as Login option</strong>, and for <strong>SSO label</strong> enter a label for the user login screen, if desired.</li>
<li>Select <strong>Update</strong>.</li>
</ol>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>For SSO to appear on the login screen, you must have <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/concept/sso-acct-recovery.html">account recovery</a> enabled and configured for at least one admin account. After account recovery is configured, log out of ServiceNow and open an incognito browser window. Go to your ServiceNow URL. Select the SSO name you just configured, which will prompt you to sign in with your identity provider. When the integration is successful, you can go back to the OIDC configuration screen to turn on <strong>Default</strong> and/or <strong>Auto Redirect IDP</strong>.</p>
