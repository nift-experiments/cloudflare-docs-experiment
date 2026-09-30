---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/
  description: Learn how to integrate Centrify as a SAML identity provider with Cloudflare One.
  full_title: Centrify (SAML) · Cloudflare One docs
  head_html: <title>Centrify (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to integrate Centrify as a SAML identity provider with Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/index.md"><meta property="og:title" content="Centrify (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to integrate Centrify as a SAML identity provider with Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/#page","headline":"Centrify (SAML) \u00b7 Cloudflare One docs","description":"Learn how to integrate Centrify as a SAML identity provider with Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/centrify-saml/
  schema: 1
---
<p>Centrify secures access to infrastructure, DevOps, cloud, and other modern enterprise so you can prevent the number one cause of breaches: privileged access abuse.</p>
<h2 id="set-up-centrify-as-a-saml-provider">Set up Centrify as a SAML provider</h2>
<h2 id="1-create-an-application-in-centrify"><ol>
<li>Create an application in Centrify</li>
</ol></h2>
<ol>
<li>
<p>Log in to your <strong>Centrify</strong> admin portal and select <strong>Apps</strong>.</p>
</li>
<li>
<p>Select <strong>Add Web Apps</strong>.</p>
</li>
<li>
<p>Select the <strong>Custom</strong> tab.</p>
</li>
<li>
<p>Next to the <strong>SAML</strong> icon, select <strong>Add</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/saml-centrify/saml-centrify-3.png" alt="Centrify Settings Add Application details page with template text" /></p>
<ol start="5">
<li>
<p>Enter the required information for your application.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Settings</strong> in the left pane.</p>
</li>
<li>
<p>In the middle menu pane, select <strong>Trust</strong>.</p>
</li>
<li>
<p>Choose the <strong>Manual Configuration</strong> option.</p>
</li>
<li>
<p>In the <strong>SP Entity ID</strong> and <strong>Assertion Consumer Service (ACS) URL fields</strong>, enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre tabindex="0"><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<ol start="11">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>In the middle menu pane, select <strong>User Access</strong>.</p>
</li>
<li>
<p>Select <strong>Add</strong>. The <strong>Select Role</strong> dialog displays.</p>
</li>
<li>
<p>Complete your roles access assignments. The Role rules display on the <strong>User Access</strong> card.</p>
</li>
<li>
<p>In the <strong>User Access</strong> card's middle menu pane, select <strong>SAML Response</strong>.</p>
</li>
<li>
<p>Select <strong>Active</strong> &gt; <strong>Add</strong> to create a new <strong>Attribute Name</strong>, <strong>Email</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/saml-centrify/saml-centrify-9.png" alt="Centrify SAML Response card with Settings Email Attribute selected" /></p>
<ol start="17">
<li>
<p>Enter the user email addresses in the <strong>Attribute Value</strong> field.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Settings</strong> again from the left menu pane, and <strong>Trust</strong>.</p>
</li>
<li>
<p>Select the <strong>Manual Configuration</strong> option.</p>
</li>
</ol>
<h3 id="2-add-centrify-to-cloudflare-one"><ol start="2">
<li>Add Centrify to Cloudflare One</li>
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
<p>Copy and paste the corresponding information from Centrify into the fields.</p>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, configure <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#optional-configurations">additional SAML options</a>.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the identity provider you want to test.</p>
<h2 id="download-sp-metadata-optional">Download SP metadata (optional)</h2>
<p>Some IdPs allow administrators to upload metadata files from their SP (service provider).</p>
<p>To get your Cloudflare metadata file:</p>
<ol>
<li>Download your unique SAML metadata file at the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata&#10;</code></pre>
<ol start="2">
<li>
<p>Save the file in XML format.</p>
</li>
<li>
<p>Upload the XML document to your <strong>Centrify</strong> account.</p>
</li>
</ol>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://abc123.my.centrify.com/baaa2117-0ec0-4d76-84cc-abccb551a123&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://abc123.my.centrify.com/applogin/appKey/baaa2117-0ec0-4d76-84cc-abccb551a123/customerId/abc123&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_cert&quot;: &quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;centrify saml example&quot;&#10;}&#10;</code></pre>
