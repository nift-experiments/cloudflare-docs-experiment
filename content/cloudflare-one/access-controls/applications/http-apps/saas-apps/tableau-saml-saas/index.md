---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/
  description: Integrate Tableau Cloud with Access.
  full_title: Tableau Cloud · Cloudflare One docs
  head_html: <title>Tableau Cloud · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Tableau Cloud with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/index.md"><meta property="og:title" content="Tableau Cloud · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Tableau Cloud with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/#page","headline":"Tableau Cloud \u00b7 Cloudflare One docs","description":"Integrate Tableau Cloud with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/tableau-saml-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://help.tableau.com/current/online/en-us/saml_config_site.htm">Tableau Cloud</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Tableau Cloud site</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Tableau</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Keep this window open. You will finish this configuration in step <a href="#4-finish-adding-a-saas-application-to-cloudflare-one">4. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-download-the-metadata-file"><ol start="2">
<li>Download the metadata file</li>
</ol></h2>
<ol>
<li>Paste the SAML Metadata endpoint from application configuration in Cloudflare One in a web browser.</li>
<li>Follow your browser-specific steps to download the URL's contents as an <code>.xml</code> file.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-tableau-cloud"><ol start="3">
<li>Add a SAML SSO provider to Tableau Cloud</li>
</ol></h2>
<ol>
<li>In Tableau Cloud, go to <strong>Settings</strong> &gt; <strong>Authentication</strong>.</li>
<li>Turn on <strong>Enable an additional authentication method</strong>. For <strong>select authentication type</strong>, select <em>SAML</em>.</li>
<li>Under <strong>1. Get Tableau Cloud metadata</strong>, copy the <strong>Tableau Cloud entity ID</strong> and <strong>Tableau Cloud ACS URL</strong>.</li>
<li>Under <strong>4. Upload metadata to Tableau</strong>, select <strong>Choose a file</strong>, and upload the <code>.xml</code> file created in step <a href="#2-download-the-metadata-file">2. Download the metadata file</a></li>
<li>Under <strong>5. Map attributes</strong>, turn on <strong>Full name</strong>. For <strong>Name (full name)</strong>, enter <code>name</code>.</li>
<li>(Optional) Choose whether users who are accessing embedded views will <strong>Authenticate in a separate pop-up window</strong> or <strong>Authenticate using an inline frame</strong>.</li>
<li>Select <strong>Save Changes</strong>.</li>
</ol>
<h2 id="4-finish-adding-a-saas-application-to-cloudflare-one"><ol start="4">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Tableau Cloud entity ID from Tableau Cloud SAML SSO set-up.</li>
<li><strong>Assertion Consumer Service URL</strong>: Tableau Cloud ACS URL from Tableau Cloud SAML SSO set-up.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="5-test-the-integration-and-set-default-authentication-type"><ol start="5">
<li>Test the integration and set default authentication type</li>
</ol></h2>
<ol>
<li>In Tableau Cloud, go to <strong>Settings</strong> &gt; <strong>Authentication</strong>.</li>
<li>Under <strong>7. Test Configuration</strong>, select <strong>Test Configuration</strong>.</li>
<li>Sign in. If your sign-in is successful, <strong>You are now signed in as (username)</strong> will appear at the top of the page.</li>
<li>Close the pop-up window.</li>
<li>(Optional) Under <strong>Default Authentication Type for Embedded Views</strong>, turn on <strong>cloudflareaccess.com (SAML)</strong>. You can also configure the default authentication type for individual users under <strong>Users</strong> &gt; <strong>Actions</strong> &gt; <strong>Authentication</strong>.</li>
</ol>
