---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/
  description: Update your domain nameservers to Cloudflare for APO to work.
  full_title: Change nameservers · Cloudflare Automatic Platform Optimization docs
  head_html: <title>Change nameservers · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="Update your domain nameservers to Cloudflare for APO to work."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/index.md"><meta property="og:title" content="Change nameservers · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update your domain nameservers to Cloudflare for APO to work."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/#page","headline":"Change nameservers \u00b7 Cloudflare Automatic Platform Optimization docs","description":"Update your domain nameservers to Cloudflare for APO to work.","url":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/get-started/change-nameservers/
  schema: 1
---
<p>After you <a href="/automatic-platform-optimization/get-started/confirm-dns-records/">confirm your DNS records</a>, change your nameservers.</p>
<p>Updating your domain to use Cloudflare's nameservers is a critical step to ensure Cloudflare can optimize and protect your site. Nameservers are your primary DNS controller and identify the location of your domain on the Internet.</p>
<p>Domain registrars can take up to 24 hours to process the nameserver updates. You will receive an email from Cloudflare once your site is activated.</p>
<h2 id="lookup-domain-name-registration">Lookup domain name registration</h2>
<ol>
<li>Visit <a href="https://lookup.icann.org/">WHOIS</a> to look up your domain name registration.</li>
<li>In the text field, enter your domain name without <code>https://www.</code> and select <strong>Lookup</strong>.</li>
<li>From <strong>Domain Information</strong>, make note of the nameserver information that displays. You will update those nameservers to point to Cloudflare.</li>
</ol>
<p>We recommend keeping this browser tab or window open and opening a new tab or window for the next section.</p>
<h2 id="update-your-nameserver-with-your-domain-registrar">Update your nameserver with your domain registrar</h2>
<ol>
<li>Log in to the administrator account for your domain registrar.</li>
<li>Navigate to DNS Management.</li>
<li>Locate your nameserver information. Your nameservers should match the information from Step 3 of Lookup domain name registration.</li>
<li>Replace the existing nameserver information with the Cloudflare nameservers from Step 4 of Create the custom nameserver with Cloudflare.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3344.md")
</aside>
