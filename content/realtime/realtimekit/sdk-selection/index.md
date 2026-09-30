---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/
  description: Choose between RealtimeKit UI Kit and Core SDK for your platform and framework.
  full_title: Select SDK(s) · Cloudflare Realtime docs
  head_html: <title>Select SDK(s) · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose between RealtimeKit UI Kit and Core SDK for your platform and framework."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/index.md"><meta property="og:title" content="Select SDK(s) · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose between RealtimeKit UI Kit and Core SDK for your platform and framework."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/#page","headline":"Select SDK(s) \u00b7 Cloudflare Realtime docs","description":"Choose between RealtimeKit UI Kit and Core SDK for your platform and framework.","url":"https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/sdk-selection/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11597.md")
</aside>
<h3 id="offerings">Offerings</h3>
<p>RealtimeKit provides two ways to build real-time media applications:</p>
<p><strong>UI Kit</strong>: <div class="nb-r-t-k-pill"></p>
@markup("md", "content/.markup/bodies/11598.md")
</div> UI library of pre-built, customizable components for rapid development — sits on top of the Core SDK.
<p><strong>Core SDK</strong>: Client SDK built on top of Realtime SFU that provides a full set of APIs for managing video calls, from joining and leaving sessions to muting, unmuting, and toggling audio and video.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11596.md")
</aside>
<h3 id="select-your-framework">Select your framework</h3>
<p>RealtimeKit support all the popular frameworks for web and mobile platforms. Please select the Platform and Framework that you are building on.</p>
<table>
<thead>
<tr>
<th>Framework/Library</th>
<th>Core SDK</th>
<th>UI Kit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Web-Components (HTML, Vue, Svelte)</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit">@cloudflare/realtimekit</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-ui">@cloudflare/realtimekit-ui</a></td>
</tr>
<tr>
<td>React</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react">@cloudflare/realtimekit-react</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-ui">@cloudflare/realtimekit-react-ui</a></td>
</tr>
<tr>
<td>Angular</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit">@cloudflare/realtimekit</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-angular-ui">@cloudflare/realtimekit-angular-ui</a></td>
</tr>
<tr>
<td>Android</td>
<td><a href="https://central.sonatype.com/artifact/com.cloudflare.realtimekit/core">com.cloudflare.realtimekit:core</a></td>
<td><a href="https://central.sonatype.com/artifact/com.cloudflare.realtimekit/ui-android">com.cloudflare.realtimekit:ui-android</a></td>
</tr>
<tr>
<td>iOS</td>
<td><a href="https://github.com/dyte-in/RealtimeKitCoreiOS">RealtimeKit</a></td>
<td><a href="https://github.com/dyte-in/RealtimeKitUI">RealtimeKitUI</a></td>
</tr>
<tr>
<td>React Native</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-native">@cloudflare/realtimekit-react-native</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-native-ui">@cloudflare/realtimekit-react-native-ui</a></td>
</tr>
</tbody>
</table>
<h3 id="technical-comparison">Technical comparison</h3>
<p>Here is a comprehensive guide to help you choose the right option for your project. This comparison will help you understand the trade-offs between using the Core SDK alone versus combining it with the UI Kit.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Core SDK only</th>
<th>UI Kit</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>What you get</strong></td>
<td>Core APIs for managing media, host controls, chat, recording and more.</td>
<td>prebuilt UI components along with Core APIs.</td>
</tr>
<tr>
<td><strong>Bundle size</strong></td>
<td>Minimal (media/network only)</td>
<td>Larger (includes Core SDK + UI components)</td>
</tr>
<tr>
<td><strong>Time to ship</strong></td>
<td>Longer (build UI from scratch). Typically 5-6 days.</td>
<td>Faster (UI Kit handles Core SDK calls). Can build an ship under 2 hours.</td>
</tr>
<tr>
<td><strong>Customization</strong></td>
<td>Complete control, manual implementation. Need to build you own UI</td>
<td>High level of customization with plug and play component library.</td>
</tr>
<tr>
<td><strong>State management</strong></td>
<td>Needs to be manually handled.</td>
<td>Automatic, UI Kit takes care of state management.</td>
</tr>
<tr>
<td><strong>UI flexibility</strong></td>
<td>Unlimited (build anything)</td>
<td>High (component library + add-ons)</td>
</tr>
<tr>
<td><strong>Learning curve</strong></td>
<td>Steeper (learn Core SDK APIs directly)</td>
<td>Gentler (declarative components wrap Core SDK)</td>
</tr>
<tr>
<td><strong>Maintenance</strong></td>
<td>More code to maintain. Larger project.</td>
<td>Less code, component updates included</td>
</tr>
<tr>
<td><strong>Design system</strong></td>
<td>Headless, integrates with any design system.</td>
<td>Allows you to provide your theme.</td>
</tr>
<tr>
<td><strong>Access to Core SDK</strong></td>
<td>Direct API access</td>
<td>Direct API access + UI components</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11595.md")
</aside>
