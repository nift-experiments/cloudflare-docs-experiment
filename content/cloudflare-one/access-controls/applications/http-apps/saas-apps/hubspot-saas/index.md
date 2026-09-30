---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/
  description: Integrate Hubspot with Access.
  full_title: Hubspot · Cloudflare One docs
  head_html: <title>Hubspot · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Hubspot with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/index.md"><meta property="og:title" content="Hubspot · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Hubspot with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/#page","headline":"Hubspot \u00b7 Cloudflare One docs","description":"Integrate Hubspot with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/hubspot-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://knowledge.hubspot.com/account-security/set-up-single-sign-on-sso">Hubspot</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Hubspot Enterprise plan account</li>
</ul>
<h2 id="1-configure-hubspot"><ol>
<li>Configure Hubspot</li>
</ol></h2>
<ol>
<li>Go to <strong>Settings</strong> &gt; <strong>Account</strong>, then go to <strong>Defaults</strong> &gt; <strong>Security</strong>.</li>
<li>Select <em>Single Sign-on</em>.</li>
<li>Copy the values for <em>Audience URI</em> and <em>Sign on URL</em>.</li>
</ol>
<h2 id="2-configure-cloudflare-access"><ol start="2">
<li>Configure Cloudflare Access</li>
</ol></h2>
<ol>
<li>
<p>In Cloudflare One, go to <strong>Access controls</strong> &gt; <strong>Applications</strong>, select <strong>Create new application</strong>, and select <strong>SaaS application</strong>.</p>
</li>
<li>
<p>Set the <strong>Application type</strong> to <em>Hubspot</em>.</p>
</li>
<li>
<p>Use the following Hubspot field mappings:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Hubspot values</th>
<th>Cloudflare values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Audience URI</td>
<td>Entity ID</td>
</tr>
<tr>
<td>Sign On URL</td>
<td>Assertion Consumer Service URL</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>
<p>Set <strong>NameID</strong> to <em>Email</em>.</p>
</li>
<li>
<p>Add any desired <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to your application.</p>
</li>
<li>
<p>Copy the <strong>SSO endpoint</strong> and <strong>Access Entity ID</strong>.</p>
</li>
<li>
<p>Save the application.</p>
</li>
</ol>
<h2 id="3-create-a-x-509-certificate"><ol start="3">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ol>
<h2 id="4-finalize-hubspot-configuration"><ol start="4">
<li>Finalize Hubspot configuration</li>
</ol></h2>
<ol>
<li>Use the following field mappings:</li>
</ol>
<table>
<thead>
<tr>
<th>Cloudflare value</th>
<th>Hubspot value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SSO endpoint</td>
<td>Identity Provider Single Sign-on URL</td>
</tr>
<tr>
<td>Entity ID</td>
<td>Identity Provider Identifier</td>
</tr>
<tr>
<td>Public key</td>
<td>Certificate</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Select <strong>Verify</strong> to validate the integration.</li>
</ol>
<p>Your configuration is now complete. Hubspot SSO can be switched on for specific users or the entire account.</p>
