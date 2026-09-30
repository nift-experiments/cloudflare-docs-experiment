---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/get-started/
  description: Set up Cloudflare Zaraz to manage third-party tools from the dashboard.
  full_title: Get started · Cloudflare Zaraz docs
  head_html: <title>Get started · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare Zaraz to manage third-party tools from the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare Zaraz to manage third-party tools from the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/get-started/#page","headline":"Get started \u00b7 Cloudflare Zaraz docs","description":"Set up Cloudflare Zaraz to manage third-party tools from the dashboard.","url":"https://developers.cloudflare.com/zaraz/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/get-started/
  schema: 1
---
<p>Before being able to use Zaraz, it is recommended that you proxy your website through Cloudflare. Refer to <a href="/fundamentals/account/">Set up Cloudflare</a> for more information. If you do not want to proxy your website through Cloudflare, refer to <a href="/zaraz/advanced/domains-not-proxied/">Use Zaraz on domains not proxied by Cloudflare</a>.</p>
<h2 id="add-a-third-party-tool-to-your-website">Add a third-party tool to your website</h2>
<p>You can add new third-party tools and load them into your website through the Cloudflare dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag Setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. If you have already added a tool before, select **Third-party tools** and click on **Add new tool**.
3. Choose a tool from the tools catalog. Select **Continue** to confirm your selection.
4. In **Set up**, configure the settings for your new tool. The information you need to enter will depend on the tool you choose. If you want to use any dynamic properties or variables, select the `+` sign in the drop-down menu next to the relevant field.
5. In **Actions** setup the actions for your new tool. You should be able to select Pageviews, Events or E-Commerce <sup><a href="#footnote-1">1</a></sup>.
6. Select **Save**.
<h2 id="events-triggers-and-actions">Events, triggers and actions</h2>
<p>Zaraz relies on events, triggers and actions to determine when to load the tools you need in your website, and what action they need to perform. The way you configure Zaraz and where you start largely depend on the tool you wish to use. When using a tool that supports Automatic Actions, this process is largely done for you. If the tool you are adding doesn't support Automatic Actions, read more about configuring <a href="/zaraz/custom-actions">Custom Actions</a>.</p>
<p>When using Automatic Actions, the available actions are as follows:</p>
<ul>
<li><strong>Pageviews</strong> - for tracking every pageview on your website</li>
<li><strong>Events</strong> - For tracking calls using the <a href="/zaraz/web-api/track"><code>zaraz.track</code> Web API</a></li>
<li><strong>E-commerce</strong> - For tracking calls to <a href="/zaraz/web-api/ecommerce"><code>zaraz.ecommerce</code> Web API</a></li>
</ul>
<h2 id="web-api">Web API</h2>
<p>If you need to programmatically start actions in your tools, Cloudflare Zaraz provides a unified Web API to send events to Zaraz, and from there, to third-party tools. This Web API includes the <code>zaraz.track()</code>, <code>zaraz.set()</code> and <code>zaraz.ecommerce()</code> methods.</p>
<p><a href="/zaraz/web-api/track/">The Track method</a> allows you to track custom events and actions on your website that might happen in real time. <a href="/zaraz/web-api/set/">The Set method</a> is an easy shortcut to define a variable once and have it sent with every future Track call. <a href="/zaraz/web-api/ecommerce/">E-commerce</a> is a unified method for sending e-commerce related data to multiple tools without needing to configure triggers and events. Refer to <a href="/zaraz/web-api/">Web API</a> for more information.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you suspect that something is not working the way it should, or if you want to verify the operation of tools on your website, read more about <a href="/zaraz/web-api/debug-mode/">Debug Mode</a> and <a href="/zaraz/monitoring/">Zaraz Monitoring</a>. Also, check the <a href="/zaraz/faq/">FAQ</a> page to see if your question was already answered there.</p>
<h2 id="platform-plugins">Platform plugins</h2>
<p>Users and companies have developed plugins that make using Zaraz easier on specific platforms. We recommend checking out these plugins if you are using one of these platforms.</p>
<h3 id="woocommerce">WooCommerce</h3>
<ul>
<li><a href="https://beetle-tracking.com/">Beetle Tracking</a> - Integrate Zaraz with your WordPress WooCommerce website to track e-commerce events with zero configuration. Beetle Tracking also supports consent management and other advanced features.</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Some tools do not supported Automatic Actions, see the section about [Custom Actions](/zaraz/custom-actions) if the tool you are adding doesn't present Automatic Actions.</li></ol></section>
