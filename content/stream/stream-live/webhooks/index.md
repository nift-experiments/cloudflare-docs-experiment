---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/webhooks/
  description: Configure webhook notifications for Cloudflare Stream Live connect, disconnect, and error events.
  full_title: Receive Live Webhooks · Cloudflare Stream docs
  head_html: <title>Receive Live Webhooks · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure webhook notifications for Cloudflare Stream Live connect, disconnect, and error events."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/webhooks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/webhooks/index.md"><meta property="og:title" content="Receive Live Webhooks · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure webhook notifications for Cloudflare Stream Live connect, disconnect, and error events."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/webhooks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/webhooks/#page","headline":"Receive Live Webhooks \u00b7 Cloudflare Stream docs","description":"Configure webhook notifications for Cloudflare Stream Live connect, disconnect, and error events.","url":"https://developers.cloudflare.com/stream/stream-live/webhooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/webhooks/
  schema: 1
---
<p>Stream Live offers webhooks to notify your service when an Input connects, disconnects, or encounters an error with Stream Live.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14397.md")
</aside>
<details><summary>Stream Live Notifications</summary><strong>Who is it for?</strong><p>Customers who are using <a href="/stream/">Stream</a> and want to receive webhooks with the status of their videos.</p>
<strong>Other options / filters</strong><p>You can input Stream Live IDs to receive notifications only about those inputs. If left blank, you will receive a list for all inputs.</p>
<p>The following input states will fire notifications. You can toggle them on or off:</p>
<ul>
<li><code>live_input.connected</code></li>
<li><code>live_input.disconnected</code></li>
</ul>
<strong>Included with</strong><p>Stream subscription.</p>
<strong>What should you do if you receive one?</strong><p>Stream notifications are entirely customizable by the customer. Action will depend on the customizations enabled.</p>
</details>
<h2 id="subscribe-to-stream-live-webhooks">Subscribe to Stream Live Webhooks</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Destinations</strong> tab.</li>
<li>On the <strong>Destinations</strong> page under <strong>Webhooks</strong>, select <strong>Create</strong>.</li>
<li>Enter the information for your webhook and select <strong>Save and Test</strong>.</li>
<li>To create the notification, from the <strong>Notifications</strong> page, select the <strong>All Notifications</strong> tab.</li>
<li>Next to <strong>Notifications</strong>, select <strong>Add</strong>.</li>
<li>Under the list of products, locate <strong>Stream</strong> and select <strong>Select</strong>.</li>
<li>Enter a name and optional description.</li>
<li>Under <strong>Webhooks</strong>, select <strong>Add webhook</strong> and select your newly created webhook.</li>
<li>Select <strong>Next</strong>.</li>
<li>By default, you will receive webhook notifications for all Live Inputs. If you only wish to receive webhooks for certain inputs, enter a comma-delimited list of Input IDs in the text field.</li>
<li>When you are done, select <strong>Create</strong>.<br/><br/></li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;name&quot;: &quot;Live Webhook Test&quot;,&#10;  &quot;text&quot;: &quot;Notification type: Stream Live Input\nInput ID: eb222fcca08eeb1ae84c981ebe8aeeb6\nEvent type: live_input.disconnected\nUpdated at: 2022-01-13T11:43:41.855717910Z&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;notification_name&quot;: &quot;Stream Live Input&quot;,&#10;    &quot;input_id&quot;: &quot;eb222fcca08eeb1ae84c981ebe8aeeb6&quot;,&#10;    &quot;event_type&quot;: &quot;live_input.disconnected&quot;,&#10;    &quot;updated_at&quot;: &quot;2022-01-13T11:43:41.855717910Z&quot;&#10;  },&#10;  &quot;ts&quot;: 1642074233&#10;}&#10;</code></pre>
<p>The <code>event_type</code> property of the data object will either be <code>live_input.connected</code>, <code>live_input.disconnected</code>, or <code>live_input.errored</code>.</p>
<p>If there are issues detected with the input, the <code>event_type</code> will be <code>live_input.errored</code>. Additional data will be under the <code>live_input_errored</code> json key and will include a <code>code</code> with one of the values listed below.</p>
<h2 id="error-codes">Error codes</h2>
<ul>
<li><code>ERR_GOP_OUT_OF_RANGE</code> – The input GOP size or keyframe interval is out of range.</li>
<li><code>ERR_UNSUPPORTED_VIDEO_CODEC</code> – The input video codec is unsupported for the protocol used.</li>
<li><code>ERR_UNSUPPORTED_AUDIO_CODEC</code> – The input audio codec is unsupported for the protocol used.</li>
<li><code>ERR_STORAGE_QUOTA_EXHAUSTED</code> – The account storage quota has been exceeded. Delete older content or purchase additional storage.</li>
<li><code>ERR_MISSING_SUBSCRIPTION</code> – Unauthorized to start a live stream. Check subscription or log into Dash for details.</li>
<li><code>ERR_UNHEALTHY</code> – The active broadcast cannot be processed for an unknown reason that is most often due to encoder misconfiguration. Confirm the broadcast follows <a href="/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations">required and recommended settings</a>, then disconnect and reconnect to try again.</li>
</ul>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;name&quot;: &quot;Live Webhook Test&quot;,&#10;  &quot;text&quot;: &quot;Notification type: Stream Live Input\nInput ID: 2c28dd2cc444cb77578c4840b51e43a8\nEvent type: live_input.errored\nUpdated at: 2024-07-09T18:07:51.077371662Z\nError Code: ERR_GOP_OUT_OF_RANGE\nError Message: Input GOP size or keyframe interval is out of range.\nVideo Codec: \nAudio Codec: &quot;,&#10;  &quot;data&quot;: {&#10;    &quot;notification_name&quot;: &quot;Stream Live Input&quot;,&#10;    &quot;input_id&quot;: &quot;eb222fcca08eeb1ae84c981ebe8aeeb6&quot;,&#10;    &quot;event_type&quot;: &quot;live_input.errored&quot;,&#10;    &quot;updated_at&quot;: &quot;2024-07-09T18:07:51.077371662Z&quot;,&#10;    &quot;live_input_errored&quot;: {&#10;      &quot;error&quot;: {&#10;        &quot;code&quot;: &quot;ERR_GOP_OUT_OF_RANGE&quot;,&#10;        &quot;message&quot;: &quot;Input GOP size or keyframe interval is out of range.&quot;&#10;      },&#10;      &quot;video_codec&quot;: &quot;&quot;,&#10;      &quot;audio_codec&quot;: &quot;&quot;&#10;    }&#10;  },&#10;  &quot;ts&quot;: 1720548474,&#10;}&#10;</code></pre>
