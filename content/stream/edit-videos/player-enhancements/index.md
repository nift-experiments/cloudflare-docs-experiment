---
cp9:
  canonical: https://developers.cloudflare.com/stream/edit-videos/player-enhancements/
  description: Customize the Cloudflare Stream player with branding, logos, and share links.
  full_title: Add player enhancements · Cloudflare Stream docs
  head_html: <title>Add player enhancements · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize the Cloudflare Stream player with branding, logos, and share links."><link rel="canonical" href="https://developers.cloudflare.com/stream/edit-videos/player-enhancements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/edit-videos/player-enhancements/index.md"><meta property="og:title" content="Add player enhancements · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize the Cloudflare Stream player with branding, logos, and share links."><meta property="og:url" content="https://developers.cloudflare.com/stream/edit-videos/player-enhancements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/edit-videos/player-enhancements/#page","headline":"Add player enhancements \u00b7 Cloudflare Stream docs","description":"Customize the Cloudflare Stream player with branding, logos, and share links.","url":"https://developers.cloudflare.com/stream/edit-videos/player-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/edit-videos/player-enhancements/
  schema: 1
---
<p>With player enhancements, you can modify your video player to incorporate elements of your branding such as your logo, and customize additional options to present to your viewers.</p>
<p>The player enhancements are automatically applied to videos using the Stream Player, but you will need to add the details via the <code>publicDetails</code> property when using your own player.</p>
<h2 id="properties">Properties</h2>
<ul>
<li><code>title</code>: The title that appears when viewers hover over the video. The title may differ from the file name of the video.</li>
<li><code>share_link</code>: Provides the user with a click-to-copy option to easily share the video URL. This is commonly set to the URL of the page that the video is embedded on.</li>
<li><code>channel_link</code>: The URL users will be directed to when selecting the logo from the video player.</li>
<li><code>logo</code>: A valid HTTPS URL for the image of your logo.</li>
</ul>
<h2 id="customize-your-own-player">Customize your own player</h2>
<p>The example below includes every property you can set via <code>publicDetails</code>.</p>
<pre tabindex="0"><code class="language-bash">curl --location --request POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;$ACCOUNT_ID&gt;/stream/&lt;$VIDEO_UID&gt;&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;$SECRET&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data-raw &#x27;{&#10;    &quot;publicDetails&quot;: {&#10;        &quot;title&quot;: &quot;Optional video title&quot;,&#10;        &quot;share_link&quot;: &quot;https://my-cool-share-link.cloudflare.com&quot;,&#10;        &quot;channel_link&quot;: &quot;https://www.cloudflare.com/products/cloudflare-stream/&quot;,&#10;        &quot;logo&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloudflare_Logo.png/480px-Cloudflare_Logo.png&quot;&#10;    }&#10;}&#x27; | jq &quot;.result.publicDetails&quot;&#10;</code></pre>
<p>Because the <code>publicDetails</code> properties are optional, you can choose which properties to include. In the example below, only the <code>logo</code> is added to the video.</p>
<pre tabindex="0"><code class="language-bash">curl --location --request POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;$ACCOUNT_ID&gt;/stream/&lt;$VIDEO_UID&gt;&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;$SECRET&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data-raw &#x27;{&#10;    &quot;publicDetails&quot;: {&#10;        &quot;logo&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloudflare_Logo.png/480px-Cloudflare_Logo.png&quot;&#10;    }&#10;}&#x27;&#10;</code></pre>
<p>You can also pull the JSON by using the endpoint below.</p>
<p><code>https://customer-&lt;ID&gt;.cloudflarestream.com/&lt;VIDEO_ID&gt;/metadata/playerEnhancementInfo.json</code></p>
<h2 id="update-player-properties-via-the-cloudflare-dashboard">Update player properties via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Videos</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a video from the list to edit it.</li>
<li>Select the <strong>Public Details</strong> tab.</li>
<li>From <strong>Public Details</strong>, enter information in the text fields for the properties you want to set.</li>
<li>When you are done, select <strong>Save</strong>.</li>
</ol>
