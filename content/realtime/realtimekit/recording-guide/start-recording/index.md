---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/
  description: Start composite recording of a RealtimeKit meeting using the API, SDK, or auto-record flag.
  full_title: Start Recording · Cloudflare Realtime docs
  head_html: <title>Start Recording · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Start composite recording of a RealtimeKit meeting using the API, SDK, or auto-record flag."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/index.md"><meta property="og:title" content="Start Recording · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Start composite recording of a RealtimeKit meeting using the API, SDK, or auto-record flag."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/#page","headline":"Start Recording \u00b7 Cloudflare Realtime docs","description":"Start composite recording of a RealtimeKit meeting using the API, SDK, or auto-record flag.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/start-recording/
  schema: 1
---
<p>This topic explains how to use RealtimeKit to implement composite recording.</p>
<p>Before getting started with this guide, we recommend that you read
<a href="/realtime/realtimekit/quickstart/">Get Started with RealtimeKit</a> to familiarize yourself with RealtimeKit.</p>
<p>To familiarize yourself with the RealtimeKit REST APIs, we recommend exploring the <a href="/api/resources/realtime_kit/">RealtimeKit REST API</a>.</p>
<p>There are three ways to start recording a RealtimeKit meeting:</p>
<ul>
<li>Using the <code>record_on_start</code> flag when
<a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a></li>
<li>Using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a></li>
<li>Client side start recording methods on the SDK</li>
</ul>
<p>RealtimeKit stores recordings for a period of 7 days, after which they will expire and no longer be accessible. It is important to either download a copy of your recording or <a href="/realtime/realtimekit/recording-guide/custom-cloud-storage/">set up storage</a> before the link expires.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11810.md")
</aside>
<h2 id="using-the-record-on-start-parameter">Using the <code>record_on_start</code> parameter</h2>
<p>When <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>, you can
specify the <code>record_on_start</code> parameter to start the recording as soon as someone joins the
meeting.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="specify-storage-config">Specify storage config</h3>
@markup("md", "content/.markup/bodies/11809.md")
</aside>
<h3 id="request">Request</h3>
<p>Specify the <code>record_on_start</code> parameter. If this flag is true, then a recording
will be started as soon as a meeting starts on RealtimeKit, i.e, when the first
participant joins the meeting.</p>
<pre tabindex="0"><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;title&quot;: &quot;Lorem Ipsum&quot;,&#10;  &quot;record_on_start&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="response">Response</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;id&quot;: &quot;497f6eca-6276-4993-bfeb-53cbbbba6f08&quot;,&#10;		&quot;record_on_start&quot;: true,&#10;		&quot;created_at&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;updated_at&quot;: &quot;2025-08-24T14:15:22Z&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="using-the-start-recording-api">Using the Start Recording API</h2>
<p>You can also start a recording using the
<a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>Specify the <code>meeting ID</code> of the meeting that you want to record.</p>
<p>Use the <a href="/api/resources/realtime_kit/subresources/meetings/methods/get/">List meetings API</a> for an
app or <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a> to
get the meeting ID. The API returns a parameter called <code>id</code>, which is your
meeting ID.</p>
<h3 id="request-1">Request</h3>
<pre tabindex="0"><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;&#10;}&#x27;&#10;</code></pre>
<h3 id="response-1">Response</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;		&quot;download_url&quot;: &quot;http://example.com&quot;,&#10;		&quot;download_url_expiry&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;download_audio_url&quot;: &quot;http://example1.com&quot;,&#10;		&quot;file_size&quot;: 0,&#10;		&quot;session_id&quot;: &quot;1ffd059c-17ea-40a8-8aef-70fd0307db82&quot;,&#10;		&quot;output_file_name&quot;: &quot;string&quot;,&#10;		&quot;status&quot;: &quot;INVOKED&quot;,&#10;		&quot;invoked_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;started_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;stopped_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;storage_config&quot;: {&#10;			&quot;type&quot;: &quot;cloudflare&quot;,&#10;			&quot;secret_key&quot;: &quot;string&quot;,&#10;			&quot;bucket&quot;: &quot;string&quot;,&#10;			&quot;path&quot;: &quot;string&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
