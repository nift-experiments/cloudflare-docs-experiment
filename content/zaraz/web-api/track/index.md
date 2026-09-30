---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/web-api/track/
  description: Send custom tracking events with the Zaraz Web API.
  full_title: zaraz.track · Cloudflare Zaraz docs
  head_html: <title>zaraz.track · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Send custom tracking events with the Zaraz Web API."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/web-api/track/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/web-api/track/index.md"><meta property="og:title" content="zaraz.track · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send custom tracking events with the Zaraz Web API."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/web-api/track/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/web-api/track/#page","headline":"zaraz.track \u00b7 Cloudflare Zaraz docs","description":"Send custom tracking events with the Zaraz Web API.","url":"https://developers.cloudflare.com/zaraz/web-api/track/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/web-api/track/
  schema: 1
---
<p>You can use <code>zaraz.track()</code> anywhere inside the <code>&lt;body&gt;</code> tag of a page.</p>
<p><code>zaraz.track()</code> allows you to track custom events on your website, that might happen in real time. It is an <code>async</code> function, so you can choose to <code>await</code> it if you would like to make sure it completed before running other code.</p>
<p>Example of user events you might be interested in tracking are successful sign-ups, calls-to-action clicks, or purchases. Common examples for other types of events are tracking the impressions of specific elements on a page, or loading a specific widget.</p>
<p>To start tracking events, use the <code>zaraz.track()</code> function like this:</p>
<pre tabindex="0"><code class="language-js">zaraz.track(eventName, [eventProperties]);&#10;</code></pre>
<p>The <code>eventName</code> parameter is a string, and the <code>eventProperties</code> parameter is an optional flat object of additional context you can attach to the event using your own keys of choice. For example, tracking a purchase with the value of 200 USD could look like this:</p>
<pre tabindex="0"><code class="language-js">zaraz.track(&quot;purchase&quot;, { value: 200, currency: &quot;USD&quot; });&#10;</code></pre>
<p>Note that the name of the event (<code>purchase</code> in the above example), the names of the keys (<code>value</code> and <code>currency</code>) and the number of keys are customizable by you. You choose what variables to track and how you want to track these variables. However, picking meaningful names will help you when you configure your triggers, because the trigger configuration has to match the events your website is sending.</p>
<p>After using <code>zaraz.track()</code> in your website, you will usually want to create a trigger based on it, and then use the trigger in an action. Start by <a href="/zaraz/custom-actions/create-trigger/">creating a new trigger</a>, with <em>Event Name</em> as your trigger's <strong>Variable name</strong>, and the <code>eventName</code> you are tracking in <strong>Match string</strong>. Following the above example, your trigger will look like this:</p>
<p><strong>Trigger example: Match <code>zaraz.track(&quot;purchase&quot;)</code></strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Event Name</em></td>
<td><em>Equals</em></td>
<td><code>purchase</code></td>
</tr>
</tbody>
</table>
<p>In every tool you want to use this trigger, add an action with this trigger <a href="/zaraz/custom-actions/">configured as a firing trigger</a>. Each action that uses this trigger can access the <code>eventProperties</code> you have sent. In the <strong>Action</strong> fields, you can use <code>{{ client.&lt;KEY_NAME&gt; }}</code> to get the value of <code>&lt;KEY_NAME&gt;</code>. In the above example, Zaraz will replace <code>{{ client.value }}</code> with <code>200</code>. If your key includes special characters or numbers, surround it with backticks like <code>{{ client.`&lt;KEY_NAME&gt;` }}</code>.</p>
<p>For more information regarding the properties you can use with <code>zaraz.track()</code>, refer to <a href="/zaraz/reference/properties-reference/">Properties reference</a>.</p>
