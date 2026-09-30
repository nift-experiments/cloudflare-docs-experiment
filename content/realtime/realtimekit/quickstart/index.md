---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/quickstart/
  description: Set up RealtimeKit in your application with API tokens, SDK installation, and your first meeting.
  full_title: Quickstart · Cloudflare Realtime docs
  head_html: <title>Quickstart · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up RealtimeKit in your application with API tokens, SDK installation, and your first meeting."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/quickstart/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/quickstart/index.md"><meta property="og:title" content="Quickstart · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up RealtimeKit in your application with API tokens, SDK installation, and your first meeting."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/quickstart/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/quickstart/#page","headline":"Quickstart \u00b7 Cloudflare Realtime docs","description":"Set up RealtimeKit in your application with API tokens, SDK installation, and your first meeting.","url":"https://developers.cloudflare.com/realtime/realtimekit/quickstart/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/quickstart/
  schema: 1
---
<h3 id="prerequisites">Prerequisites</h3>
<p>To integrate RealtimeKit in your application, you must have a <a href="https://dash.cloudflare.com">Cloudflare account</a>.</p>
<ol>
<li>Follow the <a href="/fundamentals/api/get-started/create-token/">Create API token guide</a> to create a new token via the <a href="https://dash.cloudflare.com/profile/api-tokens">Cloudflare dashboard</a>.</li>
<li>When configuring permissions, ensure that <strong>Realtime</strong> / <strong>Realtime Admin</strong> permissions are selected.</li>
<li>Configure any additional <a href="/fundamentals/api/reference/permissions/">access policies and restrictions</a> as needed for your use case.</li>
</ol>
<p><em>Optional:</em> Alternatively, <a href="/fundamentals/api/how-to/create-via-api/">create tokens programmatically via the API</a>. Please ensure your access policy includes the <strong>Realtime</strong> permission.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/z4ZQIjN3I7k" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h3 id="installation">Installation</h3>
<p>Select a framework based on the platform you are building for.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11600.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11601.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11602.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11603.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11604.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11611.md")
</div>
<h3 id="create-a-realtimekit-app">Create a RealtimeKit App</h3>
<p>You can create an application from the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare Dashboard</a>, by clicking on Create App.</p>
<p><em>Optional:</em> You can also use our <a href="/api/resources/realtime_kit/">API reference</a> for creating an application:</p>
<pre tabindex="0"><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/apps&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&quot;name&quot;: &quot;My First Cloudflare RealtimeKit app&quot;}&#x27;&#10;</code></pre>
<blockquote>
<p><strong>Note:</strong> We recommend creating different apps for staging and production environments.</p>
</blockquote>
<h3 id="create-a-meeting">Create a Meeting</h3>
<p>Use our <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Meetings API</a> to create a meeting. We will use the <strong>ID from the response</strong> in subsequent steps.</p>
<pre tabindex="0"><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&quot;title&quot;: &quot;My First Cloudflare RealtimeKit meeting&quot;}&#x27;&#10;</code></pre>
<h3 id="add-participants">Add Participants</h3>
<h4 id="create-a-preset">Create a Preset</h4>
<p>Presets define what permissions a user should have. Learn more in the Concepts guide.
You can create new presets using the <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">Presets API</a> or via the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit dashboard</a>.</p>
<blockquote>
<p><strong>Note:</strong> Skip this step if you created the app in the dashboard—default presets are already set up for you.</p>
</blockquote>
<blockquote>
<p><strong>Note:</strong> Presets can be reused across multiple meetings. Define a role (for example, admin or viewer) once and apply it to participants in any number of meetings.</p>
</blockquote>
<h4 id="add-a-participant">Add a Participant</h4>
<p>A participant is added to a meeting using the <code>Meeting ID</code> created above and selecting a <code>Preset Name</code> from the available options.</p>
<p>The response includes an <code>authToken</code> which the <strong>Client SDK uses to add this participant to the meeting</strong> room.</p>
<pre tabindex="0"><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings/&lt;meeting_id&gt;/participants&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Mary Sue&quot;,&#10;  &quot;preset_name&quot;: &quot;&lt;preset_name&gt;&quot;,&#10;  &quot;custom_participant_id&quot;: &quot;&lt;uuid_of_the_user_in_your_system&gt;&quot;&#10;}&#x27;&#10;</code></pre>
<p>Learn more about adding participants in the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">API reference</a>.</p>
<h3 id="frontend-integration">Frontend Integration</h3>
<p>You can now add the RealtimeKit Client SDK to your application.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11612.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11613.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11614.md")
</div>
