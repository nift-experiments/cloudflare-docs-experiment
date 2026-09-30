---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/
  description: Integrate Digicert with Access.
  full_title: Digicert · Cloudflare One docs
  head_html: <title>Digicert · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Digicert with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/index.md"><meta property="og:title" content="Digicert · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Digicert with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/#page","headline":"Digicert \u00b7 Cloudflare One docs","description":"Integrate Digicert with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/digicert-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://docs.digicert.com/en/certcentral/manage-account/saml-admin-single-sign-on-guide/configure-saml-single-sign-on.html">Digicert</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Digicert account</li>
<li><a href="https://docs.digicert.com/en/certcentral/manage-account/saml-admin-single-sign-on-guide/saml-single-sign-on-prerequisites.html">SAML</a> enabled in your Digicert account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Digicert</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://www.digicert.com/account/sso/metadata</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.digicert.com/account/sso/</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-in-digicert"><ol start="2">
<li>Add a SAML SSO provider in Digicert</li>
</ol></h2>
<ol>
<li>In Digicert, select <strong>Settings</strong> &gt; <strong>Single Sign-On</strong> &gt; <strong>Set up SAML</strong>.</li>
<li>Under <strong>How will you send data from your IDP?</strong>, turn on <strong>Use a dynamic URL</strong>.</li>
<li>Under <strong>Use a dynamic URL</strong>, paste the SAML Metadata endpoint from application configuration in Cloudflare One.</li>
<li>Under <strong>How will you identify a user?</strong>, turn on <strong>NameID</strong>.</li>
<li>Under <strong>Federation Name</strong>, enter a name (for example, <code>Cloudflare Access</code>). Your users will select this name when signing in.</li>
<li>Select <strong>Save SAML Settings</strong>.</li>
</ol>
<h2 id="3-test-and-enable-sso-in-digicert"><ol start="3">
<li>Test and Enable SSO in Digicert</li>
</ol></h2>
<ol>
<li>In Digicert, select <strong>Settings</strong> &gt; <strong>Single Sign-On</strong>.</li>
<li>Copy the <strong>SP Initiated Custom SSO URL</strong>.</li>
<li>Paste the URL into an incognito browser window and sign in. Upon successful sign in, SAML SSO is fully enabled.</li>
<li>(Optional) By default, users can choose to sign in directly or with SSO. To require SSO sign in, go to <strong>Account</strong> &gt; <strong>Users</strong>. Turn on <strong>Only allow this user to log in through SAML/OIDC SSO</strong> in the user details of the desired user.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4867.md")
</aside>
