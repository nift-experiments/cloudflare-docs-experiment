---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/
  description: Display content in switchable tab panels.
  full_title: Tabs · Cloudflare Style Guide
  head_html: <title>Tabs · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display content in switchable tab panels."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/index.md"><meta property="og:title" content="Tabs · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display content in switchable tab panels."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/#page","headline":"Tabs \u00b7 Cloudflare Style Guide","description":"Display content in switchable tab panels.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/tabs/
  schema: 1
---
<p>This component can help you create a tabbed interface to show related information more efficiently. Use it when there are different ways of getting the same thing done:</p>
<ul>
<li>Dashboard / API / Terraform</li>
<li>Different code syntax styles</li>
<li>Account-level vs zone-level navigation</li>
<li>GRE / IPsec tunnels</li>
</ul>
<h2 id="additional-guidance">Additional guidance</h2>
<p>The primary answer or core instruction should always appear in the main content flow, not exclusively inside a tab or collapsible section.</p>
<p>Use tabs for platform-specific variations (for example, Dashboard versus API versus Terraform) only after stating the general concept. Use Details for supplementary information, not for the primary answer.</p>
<pre tabindex="0"><code class="language-mdx">import { Tabs, TabItem } from &quot;~/components&quot;;&#10;&#10;&lt;Tabs&gt;&#10;	&lt;TabItem label=&quot;Stars&quot; icon=&quot;star&quot;&gt;&#10;		Sirius, Vega, Betelgeuse&#10;	&lt;/TabItem&gt;&#10;	&lt;TabItem label=&quot;Moons&quot; icon=&quot;moon&quot;&gt;&#10;		Io, Europa, Ganymede&#10;	&lt;/TabItem&gt;&#10;&lt;/Tabs&gt;&#10;</code></pre>
<h3 id="tab-icons">Tab icons</h3>
<p>Optionally, you can choose a corresponding icon from Starlight’s <a href="https://starlight.astro.build/reference/icons/#all-icons">Icons</a> for tab labels.</p>
<h2 id="synchronize-tabs">Synchronize Tabs</h2>
<p>If you have tabs that follow a particular pattern (Dashboard / API / Terraform), add a <code>syncKey</code> parameter that includes a <code>string</code> value.</p>
<p>We use the following <code>syncKey</code> values in our docs:</p>
<ul>
<li><code>dashPlusAPI</code>: Dashboard / API / Terraform</li>
<li><code>workersExamples</code>: For different code language tabs in the Workers docs (JavaScript, TypeScript, Python, Rust)</li>
</ul>
<h3 id="example">Example</h3>
<pre tabindex="0"><code class="language-mdx">import { Tabs, TabItem } from &quot;~/components&quot;;&#10;&#10;&lt;Tabs syncKey=&quot;dashPlusAPI&quot;&gt; &lt;TabItem label=&quot;Dashboard&quot;&gt;&#10;&#10;Dash instructions&#10;&#10;&lt;/TabItem&gt; &lt;TabItem label=&quot;API&quot;&gt;&#10;&#10;API instructions&#10;&#10;&lt;/TabItem&gt; &lt;/Tabs&gt;&#10;</code></pre>
<p>Will synchronize with:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14629.md")
</div></div>
