---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/
  description: Integrate Jamf Pro with Access.
  full_title: Jamf Pro · Cloudflare One docs
  head_html: <title>Jamf Pro · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Jamf Pro with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/index.md"><meta property="og:title" content="Jamf Pro · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Jamf Pro with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/#page","headline":"Jamf Pro \u00b7 Cloudflare One docs","description":"Integrate Jamf Pro with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/jamf-pro-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Single_Sign-On.html">Jamf Pro</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Jamf Pro account</li>
</ul>
<h2 id="1-collect-jamf-pro-information"><ol>
<li>Collect Jamf Pro information</li>
</ol></h2>
<ol>
<li>In Jamf Pro, go to <strong>Settings</strong> &gt; <strong>Systems</strong> &gt; <strong>Single Sign-On</strong> &gt; <strong>Edit</strong>.</li>
<li>Copy the pre-populated URL in <strong>Entity ID</strong>.</li>
<li>Paste the URL in a web browser to download the Jamf metadata file.</li>
<li>Open the <code>metadata.xml</code> file in a text editor, and copy the values for <strong>Entity ID</strong> and <strong>Assertion Consumer Service</strong>.</li>
</ol>
<h2 id="2-add-a-saas-application-to-cloudflare-one"><ol start="2">
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Jamf</code> or <code>Jamf Pro</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Entity ID value from Jamf Pro metadata file.</li>
<li><strong>Assertion Consumer Service URL</strong>: Assertion Consumer Service value from Jamf Pro metadata file.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="3-edit-access-saml-metadata"><ol start="3">
<li>Edit Access SAML Metadata</li>
</ol></h2>
<ol>
<li>Paste the <strong>SAML Metadata endpoint</strong> from application configuration in Cloudflare One into a browser.</li>
<li>Copy the file and paste it into a text editor.</li>
<li>Change <code>WantAuthnRequestsSigned=&quot;true&quot;</code> to <code>WantAuthnRequestsSigned=&quot;false&quot;</code>.</li>
<li>Set the file extension as <code>.xml</code> and save.</li>
</ol>
<h2 id="4-add-a-saml-sso-provider-to-jamf-pro"><ol start="4">
<li>Add a SAML SSO provider to Jamf Pro</li>
</ol></h2>
<ol>
<li>In Jamf Pro, go to <strong>Settings</strong> &gt; <strong>Single Sign-On</strong> &gt; <strong>Edit</strong>.</li>
<li>In Identity Provider menu, select <strong>Other</strong>.</li>
<li>Label <strong>Other provider</strong> as <code>Cloudflare</code>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Entity ID from Jamf Pro metadata file.</li>
<li><strong>Identity Provider Metadata Source</strong>: Select <strong>Metadata File</strong> and upload the <code>.xml</code> file from step <a href="#2-add-a-saas-application-to-cloudflare-one">2. Edit Access SAML Metadata</a>.</li>
<li><strong>Identity Provider User Mapping</strong>: <em>Name ID</em></li>
<li><strong>Jamf Pro User Mapping</strong>: <em>Email</em></li>
</ul>
</li>
<li>Turn on <strong>Single Sign On</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4850.md")
</aside>
<h2 id="5-test-the-integration"><ol start="5">
<li>Test the Integration</li>
</ol></h2>
<p>Log out of Jamf Pro and open an incognito browser window. Go to your Jamf Pro URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
