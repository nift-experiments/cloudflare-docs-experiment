---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/setup/
  description: Set up Cloudflare Zero Trust for your organization. Choose a use case to get started with a guided quick-start.
  full_title: Get started · Cloudflare One docs
  head_html: <title>Get started · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare Zero Trust for your organization. Choose a use case to get started with a guided quick-start."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/setup/index.md"><meta property="og:title" content="Get started · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare Zero Trust for your organization. Choose a use case to get started with a guided quick-start."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/setup/#page","headline":"Get started \u00b7 Cloudflare One docs","description":"Set up Cloudflare Zero Trust for your organization. Choose a use case to get started with a guided quick-start.","url":"https://developers.cloudflare.com/cloudflare-one/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/setup/
  schema: 1
---
<p>Set up Cloudflare Zero Trust to protect your users, devices, and networks. Complete the prerequisites below, then choose a use case to get started.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin any use case, you need a Cloudflare account and a Zero Trust organization.</p>
<h3 id="1-create-a-cloudflare-account"><ol>
<li>Create a Cloudflare account</li>
</ol></h3>
<p>Sign up for a <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a> and enable two-factor authentication.</p>
<h3 id="2-create-a-zero-trust-organization"><ol start="2">
<li>Create a Zero Trust organization</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong>.</p>
</li>
<li>
<p>On the onboarding screen, choose a <span class="nb-glossary-tooltip" title="team name">team name</span>. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.</p>
<p>You can find your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Zero Trust</strong> &gt; <strong>Settings</strong>.</p>
</li>
<li>
<p>Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the <strong>Zero Trust Free plan</strong>, this step is still needed but you will not be charged.</p>
</li>
</ol>
<p>When you create your organization, Cloudflare automatically adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> at any time.</p>
<h2 id="what-would-you-like-to-do">What would you like to do?</h2>
<p>These use cases match the guided onboarding in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a>. To follow along in the dashboard, select <strong>Get Started</strong>.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/4432.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4426.md")
</aside>
