---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/
  description: Learn how to integrate PingOne as a SAML identity provider with Cloudflare One.
  full_title: PingOne (SAML) · Cloudflare One docs
  head_html: <title>PingOne (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to integrate PingOne as a SAML identity provider with Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/index.md"><meta property="og:title" content="PingOne (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to integrate PingOne as a SAML identity provider with Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/#page","headline":"PingOne (SAML) \u00b7 Cloudflare One docs","description":"Learn how to integrate PingOne as a SAML identity provider with Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/pingone-saml/
  schema: 1
---
<p>The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as a SAML identity provider.</p>
<h2 id="set-up-pingone-as-a-saml-provider">Set up PingOne as a SAML provider</h2>
<h2 id="1-create-an-application-in-pingone"><ol>
<li>Create an application in PingOne</li>
</ol></h2>
<ol>
<li>
<p>In your PingIdentity environment, go to <strong>Connections</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Add Application</strong>.</p>
</li>
<li>
<p>Enter an <strong>Application Name</strong>.</p>
</li>
<li>
<p>Select <strong>SAML Application</strong>.</p>
</li>
<li>
<p>Select <strong>Configure</strong>.</p>
</li>
<li>
<p>To fill in your Cloudflare Access metadata:</p>
<ol>
<li>Select <strong>Import from URL</strong>.</li>
<li>Set the <strong>Import URL</strong> to:</li>
</ol>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata&#10;</code></pre>
<p>where <code>&lt;your-team-name&gt;</code> is your Cloudflare One <span class="nb-glossary-tooltip" title="team domain">team name</span>. 3. Select <strong>Import</strong>. 4. <strong>Save</strong> the configuration.</p>
<ol start="7">
<li>
<p>In the <strong>Configuration</strong> tab, select <strong>Download metadata</strong> and save the XML metadata file. This file will be used in a later step to add PingOne to Cloudflare One.</p>
</li>
<li>
<p>In the <strong>Attribute Mappings</strong> tab, add the following required attributes (case sensitive) and select <strong>Save</strong>.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Application attribute</th>
<th>Outgoing value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>email</code></td>
<td>Email Address</td>
</tr>
<tr>
<td><code>givenName</code></td>
<td>Given Name</td>
</tr>
<tr>
<td><code>surName</code></td>
<td>Family Name</td>
</tr>
</tbody>
</table>
<p>These <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#saml-attributes">SAML attributes</a> tell Cloudflare Access who the user is.</p>
<ol start="9">
<li>Set the application to <strong>Active</strong>.</li>
</ol>
<h3 id="2-add-pingone-to-cloudflare-one"><ol start="2">
<li>Add PingOne to Cloudflare One</li>
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
<p>Upload your PingOne XML metadata file.</p>
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
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your connection</a> and create <a href="/cloudflare-one/access-controls/policies/">Access policies</a> based on the configured login method and SAML attributes.</p>
