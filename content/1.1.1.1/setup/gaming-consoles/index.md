---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/
  description: Configure 1.1.1.1 on PlayStation and Xbox.
  full_title: Set up 1.1.1.1 on gaming consoles · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on gaming consoles · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on PlayStation and Xbox."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/index.md"><meta property="og:title" content="Set up 1.1.1.1 on gaming consoles · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on PlayStation and Xbox."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/#page","headline":"Set up 1.1.1.1 on gaming consoles \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on PlayStation and Xbox.","url":"https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/gaming-consoles/
  schema: 1
---
<p>The steps below configure your gaming console to use 1.1.1.1 instead of the default DNS resolver provided by your ISP.</p>
<h2 id="ps4">PS4</h2>
<ol>
<li>Go to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Set Up Internet Connection</strong>.</li>
<li>Select <strong>Wi-Fi</strong> or <strong>LAN</strong> depending on your Internet connection.</li>
<li>Select <strong>Custom</strong>.</li>
<li>Set <strong>IP Address Settings</strong> to <strong>Automatic</strong>.</li>
<li>Change <strong>DHCP Host Name</strong> to <strong>Do Not Specify</strong>.</li>
<li>Set <strong>DNS Settings</strong> to <strong>Manual</strong>.</li>
<li>Change <strong>Primary DNS</strong> and <strong>Secondary DNS</strong> to:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="8">
<li>If you are able to add more DNS servers, you can add the IPv6 addresses as well:</li>
</ol>
<pre tabindex="0"><code class="language-txt">2606:4700:4700::1111&#10;2606:4700:4700::1001&#10;</code></pre>
<ol start="9">
<li>Set <strong>MTU Settings</strong> to <strong>Automatic</strong>.</li>
<li>Set <strong>Proxy Server</strong> to <strong>Do Not Use</strong>.</li>
</ol>
<h2 id="xbox-one">Xbox One</h2>
<ol>
<li>Open the Network screen by pressing the Xbox button on your controller.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Network Settings</strong>.</li>
<li>Go to <strong>Advanced Settings</strong> &gt; <strong>DNS Settings</strong>.</li>
<li>Select <strong>Manual</strong>.</li>
<li>Set <strong>Primary DNS</strong> and <strong>Secondary DNS</strong> to:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="6">
<li>If you have the option to add more DNS servers, you can add the IPv6 addresses as well:</li>
</ol>
<pre tabindex="0"><code class="language-txt">2606:4700:4700::1111&#10;2606:4700:4700::1001&#10;</code></pre>
<ol start="7">
<li>When you are done, you will be shown a confirmation screen. Press <strong>B</strong> to save.</li>
</ol>
<h2 id="nintendo">Nintendo</h2>
<p>The following instructions work on New Nintendo 3DS, New Nintendo 3DS XL, New Nintendo 2DS XL, Nintendo 3DS, Nintendo 3DS XL, and Nintendo 2DS.</p>
<ol>
<li>Go to the home menu and choose <strong>System Settings</strong> (the wrench icon).</li>
<li>Select <strong>Internet Settings</strong> &gt; <strong>Connection Settings</strong>.</li>
<li>Select your Internet connection and then select <strong>Change Settings</strong>.</li>
<li>Select <strong>Change DNS</strong>.</li>
<li>Set <strong>Auto-Obtain DNS</strong> to <strong>No</strong>.</li>
<li>Select <strong>Detailed Setup</strong>.</li>
<li>Set <strong>Primary DNS</strong> and <strong>Secondary DNS</strong> to:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="8">
<li>If you are able to add more DNS servers, you can add the IPv6 addresses as well:</li>
</ol>
<pre tabindex="0"><code class="language-txt">2606:4700:4700::1111&#10;2606:4700:4700::1001&#10;</code></pre>
<ol start="9">
<li>Select <strong>Save</strong> &gt; <strong>OK</strong>.</li>
</ol>
<h2 id="nintendo-switch">Nintendo Switch</h2>
<ol>
<li>Press the home button and select <strong>System Settings</strong>.</li>
<li>Scroll down and select <strong>Internet</strong> &gt; <strong>Internet Settings</strong>.</li>
<li>Select your Internet connection and then select <strong>Change Settings</strong>.</li>
<li>Select <strong>DNS Settings</strong> &gt; <strong>Manual</strong>.</li>
<li>Set <strong>Primary DNS</strong> and <strong>Secondary DNS</strong> to:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="6">
<li>Select <strong>Save</strong> &gt; <strong>OK</strong>.</li>
</ol>
