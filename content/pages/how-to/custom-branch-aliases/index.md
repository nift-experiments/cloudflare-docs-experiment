---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/
  description: Point a custom domain to a specific branch deployment of your Cloudflare Pages project.
  full_title: Add a custom domain to a branch · Cloudflare Pages docs
  head_html: <title>Add a custom domain to a branch · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Point a custom domain to a specific branch deployment of your Cloudflare Pages project."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/index.md"><meta property="og:title" content="Add a custom domain to a branch · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Point a custom domain to a specific branch deployment of your Cloudflare Pages project."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/#page","headline":"Add a custom domain to a branch \u00b7 Cloudflare Pages docs","description":"Point a custom domain to a specific branch deployment of your Cloudflare Pages project.","url":"https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/custom-branch-aliases/
  schema: 1
---
<p>In this guide, you will learn how to add a custom domain (<code>staging.example.com</code>) that will point to a specific branch (<code>staging</code>) on your Pages project.</p>
<p>This will allow you to have a custom domain that will always show the latest build for a specific branch on your Pages project.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10896.md")
</aside>
<p>First, make sure that you have a successful deployment on the branch you would like to set up a custom domain for.</p>
<p>Next, add a custom domain under your Pages project for your desired custom domain, for example, <code>staging.example.com</code>.</p>
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-1.png" alt="Follow the instructions below to access the custom domains overview in the Pages dashboard." /></p>
<p>To do this:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Select **Custom domains** > **Setup a custom domain**.
4. Input the domain you would like to use, such as `staging.example.com`
5. Select **Continue** > **Activate domain**
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-2.png" alt="After selecting your custom domain, you will be asked to activate it." /></p>
<p>After activating your custom domain, go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns">DNS</a> for the <code>example.com</code> zone and find the <code>CNAME</code> record with the name <code>staging</code> and change the target to include your branch alias.</p>
<p>In this instance, change <code>your-project.pages.dev</code> to <code>staging.your-project.pages.dev</code>.</p>
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-3.png" alt="After activating your custom domain, change the CNAME target to include your branch name." /></p>
<p>Now the <code>staging</code> branch of your Pages project will be available on <code>staging.example.com</code>.</p>
