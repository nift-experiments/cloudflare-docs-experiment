---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/
  description: Learn about block pages in this guide.
  full_title: Block pages · Cloudflare Learning Paths
  head_html: <title>Block pages · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about block pages in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/index.md"><meta property="og:title" content="Block pages · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about block pages in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Email security (formerly Area 1),Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/#page","headline":"Block pages \u00b7 Cloudflare Learning Paths","description":"Learn about block pages in this guide.","url":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/
  schema: 1
---
<h2 id="enable-the-block-page-for-dns-policies">Enable the block page for DNS policies</h2>
<p>For DNS policies, you will need to enable the block page on a per-policy basis.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <p><strong>Traffic policies</strong> &amp;gt; <strong>Firewall policies</strong> &amp;gt; <strong>DNS</strong></p>
.</li>
<li>Select <strong>Add a policy</strong> to create a new policy, or choose the policy you want to customize and select <strong>Edit</strong>. You can only edit the block page for policies with a Block action.</li>
<li>Under <strong>Configure policy settings</strong>, turn on <strong>Modify Gateway block behavior</strong>.</li>
<li>Choose your block behavior:
<ul>
<li><strong>Use account-level block setting</strong>: Use the global block page setting configured in your account settings. The global setting can be the default Gateway block page, an <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">HTTP redirect</a>, or a <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#customize-the-block-page">custom Gateway block page</a>.</li>
<li><strong>Override account setting with URL redirect</strong>: Redirect users with a <code>307</code> HTTP redirect to a URL you specify on a policy level.</li>
</ul>
</li>
<li>(Optional) If your account-level block page setting uses a custom Gateway block page, you can turn on <strong>Add an additional message to your custom block page when traffic matches this policy</strong> to add a custom message to your custom block page when traffic is blocked by this policy. This option will replace the <strong>Message</strong> field.</li>
<li>Select <strong>Save policy</strong>.</li>
</ol>
<p>Depending on your settings, Gateway will display a block page in your users' browsers or redirect them to a specified URL when they are blocked by this policy.</p>
<h2 id="customize-the-block-page">Customize the block page</h2>
<p>You can customize the Cloudflare-hosted block page by making global changes that Gateway will display every time a user reaches your block page. Customizations will apply regardless of the type of policy (DNS or HTTP) that blocks the traffic.</p>
<p>To customize your block page:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9716.md")
</div></div>
<p>Gateway will now display a custom Gateway block page when your users visit a blocked website.</p>
<h3 id="add-a-logo-image">Add a logo image</h3>
<p>You can include an external logo image to display on your custom block page. The block page resizes all images to 146x146 pixels. The URL must be valid and no longer than 2048 characters. Accepted file types include SVG, PNG, JPEG, and GIF.</p>
