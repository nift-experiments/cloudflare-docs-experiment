---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/
  description: Integrate Google Cloud with Access.
  full_title: Google Cloud · Cloudflare One docs
  head_html: <title>Google Cloud · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Google Cloud with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/index.md"><meta property="og:title" content="Google Cloud · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Google Cloud with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/#page","headline":"Google Cloud \u00b7 Cloudflare One docs","description":"Integrate Google Cloud with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/google-cloud-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://support.google.com/cloudidentity/topic/7558767">Google Cloud</a> as a SAML application in Cloudflare One.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4855.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Google Workspace account</li>
<li><a href="https://support.google.com/cloudidentity/answer/7389973">Cloud Identity Free or Premium</a> set up in your organization's Google Cloud account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Google Cloud</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>google.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.google.com/a/&lt;your_domain.com&gt;/acs</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-a-x-509-certificate"><ol start="2">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the Public key from application configuration in Cloudflare One into a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
<li>Set the file extension as <code>.crt</code> and save.</li>
</ol>
<h2 id="3-create-an-sso-provider-in-google-cloud"><ol start="3">
<li>Create an SSO provider in Google Cloud</li>
</ol></h2>
<ol>
<li>In your <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Security</strong> &gt; <strong>Authentication</strong> &gt; <strong>SSO with third party IdP</strong>.</li>
<li>Select <strong>Third-party SSO profile for your organization</strong> &gt; <strong>Add SSO Profile</strong>.</li>
<li>Turn on <strong>Set up SSO with third-party identity provider</strong>.</li>
<li>Fill in the following information:
<ul>
<li><strong>Sign-in page URL</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Sign-out page URL</strong>: <code>https://&lt;team-name&gt;.cloudflareaccess.com/cdn-cgi/access/logout</code>, where <code>&lt;team-name&gt;</code> is your Cloudflare One <span class="nb-glossary-tooltip" title="team name">team name</span>.</li>
<li><strong>Verification certificate</strong>: Upload the <code>.crt</code> certificate file from step <a href="#2-create-a-x509-certificate">2. Create a x.509 certificate</a>.</li>
</ul>
</li>
<li>(Optional) Turn on <strong>Use a domain specific issuer</strong>. If you select this option, Google will send an issuer specific to your Google Cloud domain (<code>google.com/a/&lt;your_domain.com&gt;</code> instead of the standard <code>google.com</code>).</li>
</ol>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and go to your Google Cloud URL (<code>https://console.cloud.google.com/a/&lt;your_domain.com&gt;</code>). Sign in using credentials that do not belong to a super admin account.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p><code>Error: &quot;G Suite - This account cannot be accessed because the login credentials could not be verified.&quot;</code></p>
<p>If you see this error, it is likely that the public key and private key do not match. Confirm that your certificate file includes the correct public key.</p>
