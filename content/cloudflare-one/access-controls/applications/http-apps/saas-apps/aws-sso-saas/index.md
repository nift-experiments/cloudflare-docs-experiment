---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/
  description: Integrate AWS with Access.
  full_title: AWS · Cloudflare One docs
  head_html: <title>AWS · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate AWS with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/index.md"><meta property="og:title" content="AWS · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate AWS with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/#page","headline":"AWS \u00b7 Cloudflare One docs","description":"Integrate AWS with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/aws-sso-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html">AWS</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to an AWS account</li>
</ul>
<h2 id="1-get-aws-urls"><ol>
<li>Get AWS URLs</li>
</ol></h2>
<ol>
<li>In the AWS admin panel, search for <code>IAM Identity Center</code>.</li>
<li>Go to <strong>IAM Identity Center</strong> &gt; <strong>Settings</strong>.</li>
<li>In the <strong>Identity source</strong> tab, select the <strong>Actions</strong> dropdown and select <em>Change identity source</em>.</li>
<li>Change the identity source to <strong>External identity provider</strong>.</li>
<li>Copy the values shown in <strong>Service provider metadata</strong>. You will need these values when configuring the SaaS application in Cloudflare One.</li>
</ol>
<p>Next, we will obtain <strong>Identity provider metadata</strong> from Cloudflare One.</p>
<h2 id="2-add-a-saas-application-to-cloudflare-one"><ol start="2">
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In a separate tab or window, open the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Amazon AWS</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: IAM Identity Center issuer URL</li>
<li><strong>Assertion Consumer Service URL</strong>: IAM Identity Center Assertion Consumer Service (ACS) URL</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>(Optional) Additional SAML attribute statements can be passed from your IdP to AWS SSO. To learn more about AWS Attribute mapping, refer to <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html#supportedidpattributes">Attribute mappings - AWS Single Sign-On</a>.</li>
<li>AWS supports uploading a metadata XML file. To download your SAML metadata from Access:
<ol>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>In a separate browser window, go to the SAML Metadata endpoint (<code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/saml/xxx/saml-metadata</code>).</li>
<li>Save the page as <code>access_saml_metadata.xml</code>.</li>
</ol>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="3-complete-aws-configuration"><ol start="3">
<li>Complete AWS configuration</li>
</ol></h2>
<ol>
<li>
<p>Return to the <strong>IAM Identity Center</strong> &gt; <strong>Settings</strong> &gt; <strong>Change identity source</strong> tab.</p>
</li>
<li>
<p>Under <strong>IdP SAML metadata</strong>, upload your <code>access_saml_metadata.xml</code> file.</p>
</li>
<li>
<p>Select <strong>Next</strong> to review settings, type <strong>ACCEPT</strong> and select <strong>Change identity source</strong> to confirm changes.</p>
</li>
<li>
<p>Confirm that <strong>Provisioning</strong> is set to <em>Manual</em>.</p>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4869.md")
</aside>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>To test the connection, go to your <strong>AWS access portal URL</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
