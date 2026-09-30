---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/
  description: Integrate OneLogin as a SAML identity provider for Cloudflare One.
  full_title: OneLogin (SAML) · Cloudflare One docs
  head_html: <title>OneLogin (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate OneLogin as a SAML identity provider for Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/index.md"><meta property="og:title" content="OneLogin (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate OneLogin as a SAML identity provider for Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/#page","headline":"OneLogin (SAML) \u00b7 Cloudflare One docs","description":"Integrate OneLogin as a SAML identity provider for Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/onelogin-saml/
  schema: 1
---
<p>OneLogin provides SSO identity management. Cloudflare Access supports OneLogin as an SAML identity provider.</p>
<h2 id="set-up-onelogin-as-a-saml-provider">Set up OneLogin as a SAML provider</h2>
<h2 id="1-create-an-application-in-onelogin"><ol>
<li>Create an application in OneLogin</li>
</ol></h2>
<ol>
<li>
<p>Log in to your OneLogin admin portal.</p>
</li>
<li>
<p>Select <strong>Apps</strong> &gt; <strong>Add Apps</strong>.</p>
</li>
<li>
<p>Under <strong>Find Applications</strong>, search for <strong>Cloudflare Access</strong>.</p>
</li>
<li>
<p>Select the result sponsored by <strong>Cloudflare, Inc</strong>. You can customize the name or logo.</p>
</li>
<li>
<p>Select <strong>Save</strong>. You can change this information at any time.</p>
</li>
<li>
<p>Select the <strong>Configuration</strong> tab.</p>
</li>
<li>
<p>In the <strong>Cloudflare Access Authorization Domain</strong> field, paste your team domain:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="8">
<li>
<p>Select the <strong>Parameters</strong> tab, select <strong>Add Parameter</strong> and enter your values for <strong>Cloudflare Access Field</strong>.</p>
</li>
<li>
<p>Select the <strong>Access</strong> tab</p>
</li>
<li>
<p>In Roles, use the mapping to programmatically and automatically assign users that can access the application.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/onelogin/onelogin-saml-6.png" alt="OneLogin SAML Application Access interface with available Roles listed" /></p>
<ol start="11">
<li>
<p>Select the <strong>SSO</strong> tab.</p>
</li>
<li>
<p>Copy the OneLogin <strong>SAML 2.0 Endpoint (HTTP)</strong> to the Cloudflare Single Sign On URL.</p>
</li>
<li>
<p>Copy the OneLogin <strong>Issuer URL</strong> to the Cloudflare <strong>IdP Entity ID</strong>.</p>
</li>
<li>
<p>Copy the <strong>X.509 Certificate</strong> to the Cloudflare <strong>Signing Certificate</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/onelogin/onelogin-saml-7.png" alt="OneLogin SAML Application SSO interface with SAML2.0 sign on method, Issuer URL, and X.509 Certificate" /></p>
<h3 id="2-add-onelogin-to-cloudflare-one"><ol start="2">
<li>Add OneLogin to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>SAML</strong>.</p>
</li>
<li>
<p>Input the details from your OneLogin account in the fields.</p>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, configure <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#optional-configurations">additional SAML options</a>. If you added other SAML headers and attribute names to OneLogin, be sure to add them to Cloudflare.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the login method you want to test.</p>
<h2 id="download-sp-metadata-optional">Download SP metadata (optional)</h2>
<p>OneLogin SAML allows administrators to upload metadata files from the service provider.</p>
<p>To add a metadata file to your OneLogin SAML configuration:</p>
<ol>
<li>Download your unique SAML metadata file at the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata&#10;</code></pre>
<ol start="2">
<li>
<p>Save the file as an XML document.</p>
</li>
<li>
<p>Upload the XML document to <strong>OneLogin</strong>.</p>
</li>
</ol>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://app.onelogin.com/saml/metadata/1b84ee45-d4fa-4373-8853-abz438942123&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://sandbox.onelogin.com/trust/saml2/http-post/sso/123456&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_cert&quot;: &quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;onelogin saml example&quot;&#10;}&#10;</code></pre>
