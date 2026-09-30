---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/consent-management/api/
  description: Control consent programmatically with the Zaraz Consent API.
  full_title: Consent API · Cloudflare Zaraz docs
  head_html: <title>Consent API · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Control consent programmatically with the Zaraz Consent API."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/consent-management/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/consent-management/api/index.md"><meta property="og:title" content="Consent API · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control consent programmatically with the Zaraz Consent API."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/consent-management/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/consent-management/api/#page","headline":"Consent API \u00b7 Cloudflare Zaraz docs","description":"Control consent programmatically with the Zaraz Consent API.","url":"https://developers.cloudflare.com/zaraz/consent-management/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/consent-management/api/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The Consent API allows you to programmatically control all aspects of the Consent Management program. This includes managing the modal, the consent status, and obtaining information about your configured purposes.</p>
<p>Using the Consent API, you can integrate Zaraz Consent preferences with an external Consent Management Platform, customize your consent modal, or restrict consent management to users in specific regions.</p>
<hr />
<h2 id="events">Events</h2>
<h3 id="consent-api-ready"><code>Consent API Ready</code></h3>
<p>It can be useful to know when the Consent API is fully loaded on the page so that code interacting with its methods and properties is not called prematurely.</p>
<pre tabindex="0"><code class="language-js">document.addEventListener(&quot;zarazConsentAPIReady&quot;, () =&gt; {&#10;  // do things with the Consent API&#10;});&#10;</code></pre>
<h3 id="consent-choices-updated"><code>Consent Choices Updated</code></h3>
<p>This event is fired every time the user makes changes to their consent preferences. It can be used to act on changes to the consent, for example when updating a tool with the new consent preferences.</p>
<pre tabindex="0"><code class="language-js">document.addEventListener(&quot;zarazConsentChoicesUpdated&quot;, () =&gt; {&#10;  // read the new consent preferences using `zaraz.consent.getAll();` and do things with it&#10;});&#10;</code></pre>
<hr />
<h2 id="properties">Properties</h2>
<p>The following are properties of the <code>zaraz.consent</code> object.</p>
<ul>
<li>
<p><code>modal</code> boolean</p>
<ul>
<li>Get or set the current visibility status of the consent modal dialog.</li>
</ul>
</li>
<li>
<p><code>purposes</code> object read-only</p>
<ul>
<li>An object containing all configured purposes, with their ID, name, description, and order.</li>
</ul>
</li>
<li>
<p><code>APIReady</code> boolean read-only</p>
<ul>
<li>Indicates whether the Consent API is currently available on the page.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="methods">Methods</h2>
<h3 id="get"><code>Get</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.get(purposeId);&#10;</code></pre>
<ul>
<li><code>get(purposeId)</code> : <code>boolean | undefined</code></li>
</ul>
<p>Get the current consent status for a purpose using the purpose ID.</p>
<ul>
<li><code>true</code>: The consent was granted.</li>
<li><code>false</code>: The consent was not granted.</li>
<li><code>undefined</code>: The purpose does not exist.</li>
</ul>
<h4 id="parameters">Parameters</h4>
<ul>
<li>
<p><code>purposeId</code> string</p>
<ul>
<li>The ID representing the Purpose.</li>
</ul>
</li>
</ul>
<h3 id="set"><code>Set</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.set(consentPreferences);&#10;</code></pre>
<ul>
<li><code>set(consentPreferences)</code> : <code>undefined</code></li>
</ul>
<p>Set the consent status for some purposes using the purpose ID.</p>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>
<p><code>consentPreferences</code> object</p>
<ul>
<li>a <code>{ purposeId: boolean }</code> object describing the purposes you want to set and their respective consent status.</li>
</ul>
</li>
</ul>
<h3 id="get-all"><code>Get All</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.getAll();&#10;</code></pre>
<ul>
<li><code>getAll()</code> : <code>{ purposeId: boolean }</code></li>
</ul>
<p>Returns an object with the consent status of all purposes.</p>
<h3 id="set-all"><code>Set All</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.setAll(consentStatus);&#10;</code></pre>
<ul>
<li><code>setAll(consentStatus)</code> : <code>undefined</code></li>
</ul>
<p>Set the consent status for all purposes at once.</p>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>
<p><code>consentStatus</code> boolean</p>
<ul>
<li>Indicates whether the consent was granted or not.</li>
</ul>
</li>
</ul>
<h3 id="get-all-checkboxes"><code>Get All Checkboxes</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.getAllCheckboxes();&#10;</code></pre>
<ul>
<li><code>getAllCheckboxes()</code> : <code>{ purposeId: boolean }</code></li>
</ul>
<p>Returns an object with the checkbox status of all purposes.</p>
<h3 id="set-checkboxes"><code>Set Checkboxes</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.setCheckboxes(checkboxesStatus);&#10;</code></pre>
<ul>
<li><code>setCheckboxes(checkboxesStatus)</code> : <code>undefined</code></li>
</ul>
<p>Set the consent status for some purposes using the purpose ID.</p>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>
<p><code>checkboxesStatus</code> object</p>
<ul>
<li>a <code>{ purposeId: boolean }</code> object describing the checkboxes you want to set and their respective checked status.</li>
</ul>
</li>
</ul>
<h3 id="set-all-checkboxes"><code>Set All Checkboxes</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.setAllCheckboxes(checkboxStatus);&#10;</code></pre>
<ul>
<li><code>setAllCheckboxes(checkboxStatus)</code> : <code>undefined</code></li>
</ul>
<p>Set the <code>checkboxStatus</code> status for all purposes in the consent modal at once.</p>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li>
<p><code>checkboxStatus</code> boolean</p>
<ul>
<li>Indicates whether the purposes should be marked as checked or not.</li>
</ul>
</li>
</ul>
<h3 id="send-queued-events"><code>Send queued events</code></h3>
<pre tabindex="0"><code class="language-js">zaraz.consent.sendQueuedEvents();&#10;</code></pre>
<ul>
<li><code>sendQueuedEvents()</code> : <code>undefined</code></li>
</ul>
<p>If some Pageview-based events were not sent due to a lack of consent, they can be sent using this method after consent was granted.</p>
<h2 id="examples">Examples</h2>
<h3 id="restricting-consent-checks-based-on-location">Restricting consent checks based on location</h3>
<p>You can combine multiple features of Zaraz to effectively disable Consent Management for some visitors. For example, if you would like to use it only for visitors from the EU, you can disable the automatic showing of the consent modal and add a Custom HTML tool with the following script:</p>
<pre tabindex="0"><code class="language-html">&lt;script&gt;&#10;function getCookie(name) {&#10;  const value = `; ${document.cookie}`&#10;  return value?.split(`; ${name}=`)[1]?.split(&quot;;&quot;)[0]&#10;}&#10;&#10;function handleZarazConsentAPIReady() {&#10;  const consent_cookie = getCookie(&quot;cf_consent&quot;)&#10;  const isEUCountry = &quot;{{system.device.location.isEUCountry}}&quot; === &quot;1&quot;&#10;  if (!consent_cookie) {&#10;    if (isEUCountry) {&#10;      zaraz.consent.modal = true&#10;    } else {&#10;      zaraz.consent.setAll(true)&#10;      zaraz.consent.sendQueuedEvents()&#10;    }&#10;  }&#10;}&#10;&#10;if (zaraz.consent?.APIReady) {&#10;  handleZarazConsentAPIReady()&#10;} else {&#10;  document.addEventListener(&quot;zarazConsentAPIReady&quot;, handleZarazConsentAPIReady)&#10;}&#10;&lt;/script&gt;&#10;</code></pre>
<p>Note: If you've customized the cookie name for the Consent Manager, use that customized name instead of &quot;cf_consent&quot;  in the snippet above.</p>
<p>By letting this Custom HTML tool to run without consent requirements, the modal will appear to all EU visitors, while for other visitors consent will be automatically granted. The <code>{{ system.device.location.isEUCountry }}</code> property will be <code>1</code> if the visitor is from an EU country and <code>0</code> otherwise. You can use any other property or variable to customize the Consent Management behavior in a similar manner, such as <code>{{ system.device.location.country }}</code> to restrict consent checks based on country code.</p>
