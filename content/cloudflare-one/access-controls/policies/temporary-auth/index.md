---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/
  description: Temporary authentication in Access.
  full_title: Temporary authentication · Cloudflare One docs
  head_html: <title>Temporary authentication · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Temporary authentication in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/index.md"><meta property="og:title" content="Temporary authentication · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Temporary authentication in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/#page","headline":"Temporary authentication \u00b7 Cloudflare One docs","description":"Temporary authentication in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/temporary-auth/
  schema: 1
---
<p>With Cloudflare Access, you can require that users obtain approval before they can access a specific self-hosted application or SaaS application. The administrator will receive an email notification to approve or deny the request. Unlike a typical Allow policy, the user will have to request access at the end of each session. This allows you to define the users who should have persistent access and those who must request temporary access.</p>
<h2 id="set-up-temporary-authentication">Set up temporary authentication</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Choose a <strong>Self-hosted</strong> or <strong>SaaS</strong> application and select <strong>Configure</strong>.</li>
<li>Choose an <strong>Allow</strong> policy and select <strong>Configure</strong>.</li>
<li>Under <strong>Additional settings</strong>, turn on <a href="/cloudflare-one/access-controls/policies/require-purpose-justification/"><strong>Purpose justification</strong></a>.</li>
<li>Turn on <strong>Temporary authentication</strong>.</li>
<li>Enter the <strong>Email addresses of the approvers</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4575.md")
</aside>
7. Save the policy.
<p>Temporary authentication is now enabled for users who match this policy. You can optionally add a second <strong>Allow</strong> policy for users who should have persistent access. Be sure the policy order is set to allow persistent users through.</p>
<h2 id="temporary-authentication-requests">Temporary authentication requests</h2>
<p>When a user accesses the application, they will be prompted to enter a purpose justification and submit an access request. The request is automatically emailed to approvers. Alternatively, the user can manually present the approval link to approvers.
<img src="/assets/upstream/images/cloudflare-one/policies/temp-auth-request.png" alt="Temporary authentication request page shown to users" /></p>
<p>Approvers will receive a request similar to the example below. The approver can then grant access for a set amount of time, up to a maximum of 24 hours.</p>
<p><img src="/assets/upstream/images/cloudflare-one/policies/temp-auth-approval.png" alt="Temporary authentication approval page shown to administrators" /></p>
