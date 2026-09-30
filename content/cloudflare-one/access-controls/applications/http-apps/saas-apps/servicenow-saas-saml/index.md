---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/
  description: Integrate ServiceNow (SAML) with Access.
  full_title: ServiceNow (SAML) · Cloudflare One docs
  head_html: <title>ServiceNow (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate ServiceNow (SAML) with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/index.md"><meta property="og:title" content="ServiceNow (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate ServiceNow (SAML) with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML,ServiceNow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/#page","headline":"ServiceNow (SAML) \u00b7 Cloudflare One docs","description":"Integrate ServiceNow (SAML) with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML","ServiceNow"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/servicenow-saas-saml/
  schema: 1
---
<p>This guide covers how to configure <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/task/t_CreateASAML2Upd1SSOConfigMultiSSO.html">ServiceNow</a> as a SAML application in Cloudflare One.</p>
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
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://&lt;INSTANCE-NAME&gt;.service-now.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://&lt;INSTANCE-NAME&gt;.service-now.com/navpage.do</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
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
<h2 id="3-add-and-test-a-saml-sso-provider-in-servicenow"><ol start="3">
<li>Add and Test a SAML SSO provider in ServiceNow</li>
</ol></h2>
<ol>
<li>Select <strong>All</strong>.</li>
<li>In the search bar enter <code>Multi-Provider SSO</code>, and select <strong>Identity Providers</strong>.</li>
<li>Select <strong>New</strong> &gt; <strong>SAML</strong>.</li>
<li>In the pop-up, ensure that <strong>URL</strong> is selected.</li>
<li>Paste the <strong>SAML Metadata endpoint</strong> from application configuration in Cloudflare One in the empty field.</li>
<li>Select <strong>Import</strong>.</li>
<li>(Optional) Change the <strong>Name</strong> field to a more recognizable name.</li>
<li>Turn off <strong>Sign AuthnRequest</strong>.</li>
<li>Select <strong>Update</strong>.</li>
<li>In the pop-up, select <strong>Cancel</strong> and then <strong>&gt;</strong>.</li>
<li>Select the <strong>Name</strong> of the configuration you just completed.</li>
<li>Select <strong>Test Connection</strong>.</li>
<li>If the test succeeds, select <strong>Activate</strong>.</li>
</ol>
