---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/
  description: Reference information for Extensions in Browser Isolation.
  full_title: Extensions · Cloudflare One docs
  head_html: <title>Extensions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Extensions in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/index.md"><meta property="og:title" content="Extensions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Extensions in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/#page","headline":"Extensions \u00b7 Cloudflare One docs","description":"Reference information for Extensions in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/extensions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/extensions/
  schema: 1
---
<p>Browser Isolation supports running native Chromium Web Extensions in the remote browser.</p>
<p>When a page is isolated, it runs in a remote browser — not in the user's local browser. Extensions installed locally cannot interact with isolated pages because the page content exists only on the remote side. This capability allows extending tools that require DOM access (the ability to read and modify page content and structure), such as password managers and ad blockers, to isolated pages.</p>
<h2 id="install-an-extension-inside-the-remote-browser">Install an extension inside the remote browser</h2>
<h3 id="prerequisite-isolate-chrome-web-store">Prerequisite: Isolate Chrome Web Store</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4468.md")
</aside>
<p>Installing extensions requires Chrome Web Store isolation. Create an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> to isolate the Chrome Web Store (chromewebstore.google.com).</p>
<h3 id="install-an-extension">Install an extension</h3>
<ol>
<li>Go to <code>https://chromewebstore.google.com/</code> while isolated.</li>
<li>Choose your desired extension.</li>
<li>Select <strong>Add to Chrome</strong>. To confirm extension installation, select <strong>Add extension</strong>.</li>
</ol>
<p>Remote browser extensions are automatically reinstalled across isolated sessions.</p>
<h2 id="remove-an-extension-from-the-remote-browser">Remove an extension from the remote browser</h2>
<ol>
<li>Go to any isolated webpage.</li>
<li>Right-click anywhere to open the context menu and select <strong>Show isolation toolbar</strong>.</li>
<li>Select the jigsaw icon in the isolation toolbar to open the extension manager.</li>
<li>Select the hamburger icon for the desired extension to open the extension controls.</li>
<li>Select <strong>Remove from Chromium</strong>. To confirm removal, select <strong>Remove</strong>.</li>
</ol>
<h2 id="useful-extensions">Useful extensions</h2>
<h3 id="modify-remote-browser-user-agent">Modify remote browser user agent</h3>
<p><a href="https://chromewebstore.google.com/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg">User-Agent Switcher for Chrome</a> enables controlling the User Agent sent from the remote browser to an isolated website.</p>
<h3 id="control-remote-browser-request-headers">Control remote browser request headers</h3>
<p><a href="https://chromewebstore.google.com/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj">ModHeader</a> enables controlling arbitrary request headers sent from the remote browser to an isolated website.</p>
