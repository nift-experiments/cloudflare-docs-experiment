---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/
  description: Signed AuthN requests (SAML) in Zero Trust integrations.
  full_title: Signed AuthN requests (SAML) · Cloudflare One docs
  head_html: <title>Signed AuthN requests (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Signed AuthN requests (SAML) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/index.md"><meta property="og:title" content="Signed AuthN requests (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Signed AuthN requests (SAML) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/#page","headline":"Signed AuthN requests (SAML) \u00b7 Cloudflare One docs","description":"Signed AuthN requests (SAML) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/signed_authn/
  schema: 1
---
<p>In a SAML request flow, Cloudflare Access functions as the service provider (SP) to the identity provider (IdP). Cloudflare Access sends a SAML request to your IdP. The signing certificate that you upload from your SAML provider verifies the response.</p>
<p>In some cases, administrators need to verify that the request from the SP is authentic. By validating both the requests from the SP and the responses from the IdP, teams can ensure that operations in the SAML relationship are signed in both directions.</p>
<p>Cloudflare Access supports this requirement in the form of Signed AuthN requests. When enabled, Access sends a signature embedded in an HTTP POST request that contains the AuthN details.</p>
<h2 id="set-up-signed-authn-requests">Set up Signed AuthN requests</h2>
<p>To set up Signed AuthN requests:</p>
<ol>
<li>
<p>In Cloudflare One, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Choose <strong>SAML</strong> on the next page.</p>
</li>
<li>
<p>Complete the fields in the dialog.</p>
</li>
<li>
<p>Go to this URL to find the certificate:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/public-cert&#10;</code></pre>
<p>Ensure that your IdP validation uses the most recent certificate. Cloudflare Access routinely rotates the public key as a security measure.</p>
<p>Cloudflare Access uses a certificate that includes the following 2 distinguished name fields:</p>
<ul>
<li><strong>Issuer Distinguished Name</strong> - <code>CN=cloudflareaccess.com, C=US, ST=Texas, L=Austin, O=Cloudflare</code></li>
<li><strong>Subject Distinguished Name</strong> - <code>CN=*.cloudflareaccess.com, C=US, ST=Texas, L=Austin, O=Cloudflare</code></li>
</ul>
<p>Most IdP configurations require 3 components to enforce AuthN signature verification:</p>
<ul>
<li><strong>Certificate issuer <a href="https://knowledge.digicert.com/generalinformation/INFO1745.html">distinguished name (DN)</a></strong></li>
<li><strong>Certificate subject distinguished name</strong></li>
<li><strong>Public certificate</strong></li>
</ul>
<ol start="6">
<li>
<p>In your IdP account, replace your authorization domain with the <span class="nb-glossary-tooltip" title="team domain">team domain</span> generated by Cloudflare Access.</p>
<p>This is an example format:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/public-cert&#10;</code></pre>
