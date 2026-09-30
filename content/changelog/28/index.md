---
cp9:
  canonical: https://developers.cloudflare.com/changelog/28/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 28 | Cloudflare Docs
  head_html: <title>Changelog - page 28 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/28/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 28"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/28/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/28/#page","headline":"Changelog - page 28 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/28/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/28/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-01-15">Jan 15, 2026</time><div>
<h2 id="post-2026-01-15-flux-2-klein-4b-workers-ai"><a href="/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/">Launching FLUX.2 [klein] 4B on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-4b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-15-flux-2-klein-4b-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<pre tabindex="0"><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-klein-4b">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form width=1024 <br />
--form height=1024</p>
<pre tabindex="0"><code>&#10;Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')</p>
<p>// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {
multipart: {
body: formStream,
contentType: formContentType
}
})</p>
<pre tabindex="0"><code></code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-14">Jan 14, 2026</time><div>
<h2 id="post-2026-01-14-Download-URL-Scanner-Report-PDF"><a href="/changelog/post/2026-01-14-Download-URL-Scanner-Report-PDF/">URL Scanner now supports PDF report downloads</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We have expanded the reporting capabilities of the Cloudflare URL Scanner. In addition to existing JSON and HAR exports, users can now generate and download a <strong>PDF report</strong> directly from the Cloudflare dashboard.
This update streamlines how security analysts can share findings with stakeholders who may not have access to the Cloudflare dashboard or specialized tools to parse JSON and HAR files.</p>
<p><strong>Key Benefits:</strong></p>
<ul>
<li>Consolidate scan results, including screenshots, security signatures, and metadata, into a single, portable document</li>
<li>Easily share professional-grade summaries with non-technical stakeholders or legal teams for faster incident response</li>
</ul>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>PDF Export Button:</strong> A new download option is available in the URL Scanner results page within the Cloudflare dashboard</li>
<li><strong>Unified Documentation:</strong> Access all scan details—from high-level summaries to specific security flags—in one offline-friendly file</li>
</ul>
<p>To get started with the URL Scanner and explore our reporting capabilities, visit the <a href="https://developers.cloudflare.com/api/resources/url_scanner/">URL Scanner API documentation</a>.</p>
<hr />
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-14">Jan 14, 2026</time><div>
<h2 id="post-2026-01-13-warp-macos-ga"><a href="/changelog/post/2026-01-13-warp-macos-ga/">WARP client for macOS (version 2025.10.186.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-14">Jan 14, 2026</time><div>
<h2 id="post-2026-01-13-warp-windows-ga"><a href="/changelog/post/2026-01-13-warp-windows-ga/">WARP client for Windows (version 2025.10.186.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features. New features include the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>, and a new WARP client device posture check for <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/">Antivirus</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
<li>Fixed an issue that caused occasional audio degradation and increased CPU usage on Windows by optimizing route configurations for large <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#domain-based-split-tunnels">domain-based split tunnel rules</a>.</li>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where sending large messages to the daemon by Inter-Process Communication (IPC) could cause the daemon to fail and result in service interruptions.</li>
<li>Added support for a new WARP client device posture check for <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/">Antivirus</a>. The check confirms the presence of an antivirus program on a Windows device with the option to check if the antivirus is up to date.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-13">Jan 13, 2026</time><div>
<h2 id="post-2026-01-13-ai-crawl-control-read-only-role"><a href="/changelog/post/2026-01-13-ai-crawl-control-read-only-role/">AI Crawl Control Read Only role now available</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>Account administrators can now assign the <strong>AI Crawl Control Read Only</strong> role to provide read-only access to AI Crawl Control at the domain level.</p>
<p>Users with this role can view the <strong>Overview</strong>, <strong>Crawlers</strong>, <strong>Metrics</strong>, <strong>Robots.txt</strong>, and <strong>Settings</strong> tabs but cannot modify crawler actions or settings.</p>
<p>This role is specific for AI Crawl Control. You still require correct permissions to access other areas / features of the dashboard.</p>
<p>To assign, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and add a policy with the <strong>AI Crawl Control Read Only</strong> role scoped to the desired domain.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-13">Jan 13, 2026</time><div>
<h2 id="post-2026-01-13-wrangler-types-multi-environment"><a href="/changelog/post/2026-01-13-wrangler-types-multi-environment/">`wrangler types` now generates types for all environments</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <code>wrangler types</code> command now generates TypeScript types for bindings from <strong>all environments</strong> defined in your Wrangler configuration file by default.</p>
<p>Previously, <code>wrangler types</code> only generated types for bindings in the top-level configuration (or a single environment when using the <code>--env</code> flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.</p>
<p>Now, running <code>wrangler types</code> collects bindings from all environments and includes them in the generated <code>Env</code> type. This ensures your types are complete regardless of which environment you deploy to.</p>
<h4 id="2026-01-13-wrangler-types-multi-environment-generating-types-for-a-specific-environment">Generating types for a specific environment</h4>
<p>If you want the previous behavior of generating types for only a specific environment, you can use the <code>--env</code> flag:</p>
<pre tabindex="0"><code class="language-sh">wrangler types --env production&#10;</code></pre>
<p>Learn more about <a href="/workers/wrangler/commands/general/#types">generating types for your Worker</a> in the Wrangler documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-13">Jan 13, 2026</time><div>
<h2 id="post-2026-01-13-warp-linux-ga"><a href="/changelog/post/2026-01-13-warp-linux-ga/">WARP client for Linux (version 2025.10.186.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li>Linux <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/disk-encryption/">disk encryption posture check</a> now supports non-filesystem encryption types like <code>dm-crypt</code>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where the GUI becomes unresponsive when the <strong>Re-Authenticate in browser</strong> button is clicked.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-12">Jan 12, 2026</time><div>
<h2 id="post-2026-01-12-enhanced-visibility-post-delivery-actions"><a href="/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/">Enhanced visibility for post-delivery actions</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17721.md")</aside>
<p><img src="/assets/upstream/images/changelog/email-security/enhanced-visibility-post-delivery-actions.png" alt="failure-log-example" /></p>
<p>This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-12">Jan 12, 2026</time><div>
<h2 id="post-2026-01-12-dma-metro-code-field"><a href="/changelog/post/2026-01-12-dma-metro-code-field/">Metro code field now available in Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>The <code>ip.src.metro_code</code> field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.</p>
<p>You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.</p>
<h4 id="2026-01-12-dma-metro-code-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ip.src.metro_code</code></td>
<td>String | null</td>
<td>The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>ip.src.metro_code eq &quot;501&quot;&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/">Fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-12">Jan 12, 2026</time><div>
<h2 id="post-2026-01-12-STIX2-available-for-threat-events-api"><a href="/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/">Cloudflare Threat Events now support STIX2 format</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We are excited to announce that <strong>Cloudflare Threat Events</strong> now supports the <strong>STIX2 (Structured Threat Information Expression)</strong> format. This was a highly requested feature designed to streamline how security teams consume and act upon our threat intelligence.</p>
<p>By adopting this industry-standard format, you can now integrate Cloudflare's threat events data more effectively into your existing security ecosystem.</p>
<h4 id="2026-01-12-STIX2-available-for-threat-events-api-key-benefits">Key benefits</h4>
<ul>
<li>
<p>Eliminate the need for custom parsers, as STIX2 allows for &quot;out of the box&quot; ingestion into major <strong>Threat Intel Platforms (TIPs)</strong>, <strong>SIEMs</strong>, and <strong>SOAR</strong> tools.</p>
</li>
<li>
<p>STIX2 provides a standardized way to represent relationships between indicators, sightings, and threat actors, giving your analysts a clearer picture of the threat landscape.</p>
</li>
</ul>
<p>For technical details on how to query events using this format, please refer to our <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/">Threat Events API Documentation</a>.</p>
<hr />
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-12">Jan 12, 2026</time><div>
<h2 id="post-2026-01-12-waf-release"><a href="/changelog/post/2026-01-12-waf-release/">WAF Release - 2026-01-12</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="72963b917ef74697b5bde02f48a1841a">48a1841a</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR MAKE_SET/ELT" (ID: <code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Benchmark Function" (ID: <code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>)</td>
</tr>
</tbody>    
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-12">Jan 12, 2026</time><div>
<h2 id="post-2026-01-11-wrangler-types-check"><a href="/changelog/post/2026-01-11-wrangler-types-check/">Validate your generated types with `wrangler types --check`</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports a <code>--check</code> flag for the <code>wrangler types</code> command. This flag validates that your generated types are up to date without writing any changes to disk.</p>
<p>This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types --check&#10;</code></pre>
<p>If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.</p>
<p>For more information, see the <a href="/workers/wrangler/commands/general/#types">Wrangler types documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-09">Jan 9, 2026</time><div>
<h2 id="post-2025-12-11-builds-event-subscriptions"><a href="/changelog/post/2025-12-11-builds-event-subscriptions/">Get notified when your Workers builds succeed or fail</a></h2>
<div class="changelog-badges"><span>workers</span><span>queues</span></div><div class="changelog-body"><p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-09">Jan 9, 2026</time><div>
<h2 id="post-2026-01-09-wrangler-tab-completion"><a href="/changelog/post/2026-01-09-wrangler-tab-completion/">Shell tab completions for Wrangler CLI</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.</p>
<p>Tab completions are supported for Bash, Zsh, Fish, and PowerShell.</p>
<h4 id="2026-01-09-wrangler-tab-completion-setup">Setup</h4>
<p>Generate the completion script for your shell and add it to your configuration file:</p>
<pre tabindex="0"><code class="language-sh">&#35; Bash&#10;wrangler complete bash &gt;&gt; ~/.bashrc&#10;&#10;&#35; Zsh&#10;wrangler complete zsh &gt;&gt; ~/.zshrc&#10;&#10;&#35; Fish&#10;wrangler complete fish &gt;&gt; ~/.config/fish/config.fish&#10;&#10;&#35; PowerShell&#10;wrangler complete powershell &gt;&gt; $PROFILE&#10;</code></pre>
<p>After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:</p>
<pre tabindex="0"><code class="language-sh">wrangler d&lt;TAB&gt;          # completes to &#x27;deploy&#x27;, &#x27;dev&#x27;, &#x27;d1&#x27;, etc.&#10;wrangler kv &lt;TAB&gt;        # shows subcommands: namespace, key, bulk&#10;</code></pre>
<p>Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by <a href="https://github.com/bombshell-dev/tab/"><code>@bomb.sh/tab</code></a>.</p>
<p>See the <a href="/workers/wrangler/commands/general/#complete"><code>wrangler complete</code> documentation</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-08">Jan 8, 2026</time><div>
<h2 id="post-2026-01-08-Access-audit-log-for-DoH-users"><a href="/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/">Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare <a href="/cloudflare-one/insights/logs/">admin activity logs</a> now capture each time a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTP (DoH) user</a> is created.</p>
<p>These logs can be viewed from the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, pulled via the <a href="/api/">Cloudflare API</a>, and exported through <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-07">Jan 7, 2026</time><div>
<h2 id="post-2026-01-07-analytics-engine-support-for-like-and-having"><a href="/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/">Workers Analytics Engine SQL now supports filtering using HAVING and LIKE</a></h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now use the <code>HAVING</code> clause and <code>LIKE</code> pattern matching operators in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a>.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.</p>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-filtering-using-having">Filtering using <code>HAVING</code></h4>
<p>The <code>HAVING</code> clause complements the <code>WHERE</code> clause by enabling you to filter groups based on aggregate values. While <code>WHERE</code> filters rows before aggregation, <code>HAVING</code> filters groups after aggregation is complete.</p>
<p>You can use <code>HAVING</code> to filter groups where the average exceeds a threshold:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING average_temp &gt; 10&#10;</code></pre>
<p>You can also filter groups based on aggregates such as the number of items in the group:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    count() AS num_readings&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING num_readings &gt; 100&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-pattern-matching-using-like">Pattern matching using <code>LIKE</code></h4>
<p>The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:</p>
<ul>
<li><code>LIKE</code> - case-sensitive pattern matching</li>
<li><code>NOT LIKE</code> - case-sensitive pattern exclusion</li>
<li><code>ILIKE</code> - case-insensitive pattern matching</li>
<li><code>NOT ILIKE</code> - case-insensitive pattern exclusion</li>
</ul>
<p>Pattern matching supports two wildcard characters: <code>%</code> (matches zero or more characters) and <code>_</code> (matches exactly one character).</p>
<p>You can match strings starting with a prefix:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM logs&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;</code></pre>
<p>You can also match file extensions (case-insensitive):</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM requests&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;</code></pre>
<p>Another example is excluding strings containing specific text:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM events&#10;WHERE blob3 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-ready-to-get-started">Ready to get started?</h4>
<p>Learn more about the <a href="/analytics/analytics-engine/sql-reference/statements/#having-clause"><code>HAVING</code> clause</a> or <a href="/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators">pattern matching operators</a> in the Workers Analytics Engine SQL reference documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-05">Jan 5, 2026</time><div>
<h2 id="post-2026-01-05-custom-instance-types"><a href="/changelog/post/2026-01-05-custom-instance-types/">Custom container instance types now available for all users</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Custom instance types are now enabled for all <a href="/containers">Cloudflare Containers</a> users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined <a href="/containers/platform/limits/#instance-types">instance types</a>. Previously, only select Enterprise customers were able to customize their instance type.</p>
<p>To use a custom instance type, specify the <code>instance_type</code> property as an object with <code>vcpu</code>, <code>memory_mib</code>, and <code>disk_mb</code> fields in your Wrangler configuration:</p>
<pre tabindex="0"><code class="language-toml">[[containers]]&#10;image = &quot;./Dockerfile&quot;&#10;instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }&#10;</code></pre>
<p>Individual limits for custom instance types are based on the <code>standard-4</code> instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like <code>lite</code> or <code>basic</code>.</p>
<p>See the <a href="/containers/platform/limits/#custom-instance-types">limits documentation</a> for the full list of constraints on custom instance types.
See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-01">Jan 1, 2026</time><div>
<h2 id="post-2026-01-01-microfrontends"><a href="/changelog/post/2026-01-01-microfrontends/">Build microfrontend applications on Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy microfrontends to Cloudflare, splitting a single application into smaller, independently deployable units that render as one cohesive application. This lets different teams using different frameworks develop, test, and deploy each microfrontend without coordinating releases.</p>
<p>Microfrontends solve several challenges for large-scale applications:</p>
<ul>
<li><strong>Independent deployments</strong>: Teams deploy updates on their own schedule without redeploying the entire application</li>
<li><strong>Framework flexibility</strong>: Build multi-framework applications (for example, Astro, Remix, and Next.js in one app)</li>
<li><strong>Gradual migration</strong>: Migrate from a monolith to a distributed architecture incrementally</li>
</ul>
<p>Create a microfrontend project:</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This template automatically creates a router worker with pre-configured routing logic, and lets you configure <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> to Workers you have already deployed to your Cloudflare account. The router Worker analyzes incoming requests, matches them against configured routes, and forwards requests to the appropriate microfrontend via service bindings. The router automatically rewrites HTML, CSS, and headers to ensure assets load correctly from each microfrontend's mount path. The router includes advanced features like preloading for faster navigation between microfrontends, smooth page transitions using the View Transitions API, and automatic path rewriting for assets, redirects, and cookies.</p>
<p>Each microfrontend can be a full-framework application, a static site with Workers Static Assets, or any other Worker-based application.</p>
<p>Get started with the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe">microfrontends template</a>, or read the <a href="/workers/framework-guides/web-apps/microfrontends/">microfrontends documentation</a> for implementation details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-31">Dec 31, 2025</time><div>
<h2 id="post-2025-12-31-connector-breakout-traffic-netflow"><a href="/changelog/post/2025-12-31-connector-breakout-traffic-netflow/">Breakout traffic visibility via NetFlow</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-22">Dec 22, 2025</time><div>
<h2 id="post-2025-12-22-agents-sdk-ai-sdk-v6"><a href="/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/">Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> v0.3.0 bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v6</a> and introducing the unified tool pattern, dynamic tool approval, and enhanced React hooks with improved tool handling.</p>
<p>This release includes improved streaming and tool support, dynamic tool approval (for &quot;human in the loop&quot; systems), enhanced React hooks with <code>onToolCall</code> callback, improved error handling for streaming responses, and seamless migration from v5 patterns.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable tool execution and approval workflows.</p>
<p>Additionally, we've updated <strong>workers-ai-provider v3.0.0</strong>, the official provider for Cloudflare Workers AI models, and <strong>ai-gateway-provider v3.0.0</strong>, the provider for Cloudflare AI Gateway, to be compatible with AI SDK v6.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-agents-sdk-v0-3-0">Agents SDK v0.3.0</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-unified-tool-pattern">Unified Tool Pattern</h4>
<p>AI SDK v6 introduces a unified tool pattern where all tools are defined on the server using the <code>tool()</code> function. This replaces the previous client-side <code>AITool</code> pattern.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-server-side-tool-definition">Server-Side Tool Definition</h4>
<pre tabindex="0"><code class="language-ts">import { tool } from &quot;ai&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;// Server: Define ALL tools on the server&#10;const tools = {&#10;	// Server-executed tool&#10;	getWeather: tool({&#10;		description: &quot;Get weather for a city&quot;,&#10;		inputSchema: z.object({ city: z.string() }),&#10;		execute: async ({ city }) =&gt; fetchWeather(city)&#10;	}),&#10;&#10;	// Client-executed tool (no execute = client handles via onToolCall)&#10;	getLocation: tool({&#10;		description: &quot;Get user location from browser&quot;,&#10;		inputSchema: z.object({})&#10;		// No execute function&#10;	}),&#10;&#10;	// Tool requiring approval (dynamic based on input)&#10;	processPayment: tool({&#10;		description: &quot;Process a payment&quot;,&#10;		inputSchema: z.object({ amount: z.number() }),&#10;		needsApproval: async ({ amount }) =&gt; amount &gt; 100,&#10;		execute: async ({ amount }) =&gt; charge(amount)&#10;	})&#10;};&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-client-side-tool-handling">Client-Side Tool Handling</h4>
<pre tabindex="0"><code class="language-ts">// Client: Handle client-side tools via onToolCall callback&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		if (toolCall.toolName === &quot;getLocation&quot;) {&#10;			const position = await new Promise((resolve, reject) =&gt; {&#10;				navigator.geolocation.getCurrentPosition(resolve, reject);&#10;			});&#10;			addToolOutput({&#10;				toolCallId: toolCall.toolCallId,&#10;				output: {&#10;					lat: position.coords.latitude,&#10;					lng: position.coords.longitude&#10;				}&#10;			});&#10;		}&#10;	}&#10;});&#10;</code></pre>
<p><strong>Key benefits of the unified tool pattern:</strong></p>
<ul>
<li><strong>Server-defined tools</strong>: All tools are defined in one place on the server</li>
<li><strong>Dynamic approval</strong>: Use <code>needsApproval</code> to conditionally require user confirmation</li>
<li><strong>Cleaner client code</strong>: Use <code>onToolCall</code> callback instead of managing tool configs</li>
<li><strong>Type safety</strong>: Full TypeScript support with proper tool typing</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v6 capabilities.</p>
<pre tabindex="0"><code class="language-ts">// Basic chat setup with onToolCall&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		// Handle client-side tool execution&#10;		await addToolOutput({&#10;			toolCallId: toolCall.toolCallId,&#10;			output: { result: &quot;success&quot; }&#10;		});&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-dynamic-tool-approval">Dynamic Tool Approval</h4>
<p>Use <code>needsApproval</code> on server tools to conditionally require user confirmation:</p>
<pre tabindex="0"><code class="language-ts">const paymentTool = tool({&#10;	description: &quot;Process a payment&quot;,&#10;	inputSchema: z.object({&#10;		amount: z.number(),&#10;		recipient: z.string()&#10;	}),&#10;	needsApproval: async ({ amount }) =&gt; amount &gt; 1000,&#10;	execute: async ({ amount, recipient }) =&gt; {&#10;		return await processPayment(amount, recipient);&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>The <code>isToolUIPart</code> and <code>getToolName</code> functions now check both static and dynamic tool parts:</p>
<pre tabindex="0"><code class="language-ts">import { isToolUIPart, getToolName } from &quot;ai&quot;;&#10;&#10;const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolOutput({&#10;		toolCallId: part.toolCallId,&#10;		output: &quot;User approved the action&quot;&#10;	});&#10;}&#10;</code></pre>
<p>If you need the v5 behavior (static-only checks), use the new functions:</p>
<pre tabindex="0"><code class="language-ts">import { isStaticToolUIPart, getStaticToolName } from &quot;ai&quot;;&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-converttomodelmessages-is-now-async">convertToModelMessages() is now async</h4>
<p>The <code>convertToModelMessages()</code> function is now asynchronous. Update all calls to await the result:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages } from &quot;ai&quot;;&#10;&#10;const result = streamText({&#10;	messages: await convertToModelMessages(this.messages),&#10;	model: openai(&quot;gpt-4o&quot;)&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-modelmessage-type">ModelMessage type</h4>
<p>The <code>CoreMessage</code> type has been removed. Use <code>ModelMessage</code> instead:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages, type ModelMessage } from &quot;ai&quot;;&#10;&#10;const modelMessages: ModelMessage[] = await convertToModelMessages(messages);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-generateobject-mode-option-removed">generateObject mode option removed</h4>
<p>The <code>mode</code> option for <code>generateObject</code> has been removed:</p>
<pre tabindex="0"><code class="language-ts">// Before (v5)&#10;const result = await generateObject({&#10;	mode: &quot;json&quot;,&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;&#10;// After (v6)&#10;const result = await generateObject({&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-structured-output-with-generatetext">Structured Output with generateText</h4>
<p>While <code>generateObject</code> and <code>streamObject</code> are still functional, the recommended approach is to use <code>generateText</code>/<code>streamText</code> with the <code>Output.object()</code> helper:</p>
<pre tabindex="0"><code class="language-ts">import { generateText, Output, stepCountIs } from &quot;ai&quot;;&#10;&#10;const { output } = await generateText({&#10;	model: openai(&quot;gpt-4&quot;),&#10;	output: Output.object({&#10;		schema: z.object({ name: z.string() })&#10;	}),&#10;	stopWhen: stepCountIs(2),&#10;	prompt: &quot;Generate a name&quot;&#10;});&#10;</code></pre>
<blockquote>
<p><strong>Note</strong>: When using structured output with <code>generateText</code>, you must configure multiple steps with <code>stopWhen</code> because generating the structured output is itself a step.</p>
</blockquote>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-workers-ai-provider-v3-0-0">workers-ai-provider v3.0.0</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v3.0.0 with AI SDK v6 support.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre tabindex="0"><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v3.0.0 - enhanced v6 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v6 file handling with automatic conversion:</p>
<pre tabindex="0"><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre tabindex="0"><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages: await convertToModelMessages(messages),&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-provider-v3-0-0">ai-gateway-provider v3.0.0</h4>
<p>The ai-gateway-provider v3.0.0 now supports AI SDK v6, enabling you to use Cloudflare AI Gateway with multiple AI providers including Anthropic, Azure, AWS Bedrock, Google Vertex, and Perplexity.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-setup">AI Gateway Setup</h4>
<p>Use Cloudflare AI Gateway to add analytics, caching, and rate limiting to your AI applications:</p>
<pre tabindex="0"><code class="language-ts">import { createAIGateway } from &quot;ai-gateway-provider&quot;;&#10;&#10;// Create AI Gateway provider (v3.0.0 - enhanced v6 internals)&#10;const model = createAIGateway({&#10;	gatewayUrl: &quot;https://gateway.ai.cloudflare.com/v1/your-account-id/gateway&quot;,&#10;	headers: {&#10;		&quot;Authorization&quot;: `Bearer ${env.AI_GATEWAY_TOKEN}`&#10;	}&#10;})({&#10;	provider: &quot;openai&quot;,&#10;	model: &quot;gpt-4o&quot;&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-migration-from-v5">Migration from v5</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-deprecated-apis">Deprecated APIs</h4>
<p>The following APIs are deprecated in favor of the unified tool pattern:</p>
<table>
<thead>
<tr>
<th>Deprecated</th>
<th>Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AITool</code> type</td>
<td>Use AI SDK's <code>tool()</code> function on server</td>
</tr>
<tr>
<td><code>extractClientToolSchemas()</code></td>
<td>Define tools on server, no client schemas needed</td>
</tr>
<tr>
<td><code>createToolsFromClientSchemas()</code></td>
<td>Define tools on server with <code>tool()</code></td>
</tr>
<tr>
<td><code>toolsRequiringConfirmation</code> option</td>
<td>Use <code>needsApproval</code> on server tools</td>
</tr>
<tr>
<td><code>experimental_automaticToolResolution</code></td>
<td>Use <code>onToolCall</code> callback</td>
</tr>
<tr>
<td><code>tools</code> option in <code>useAgentChat</code></td>
<td>Use <code>onToolCall</code> for client-side execution</td>
</tr>
<tr>
<td><code>addToolResult()</code></td>
<td>Use <code>addToolOutput()</code></td>
</tr>
</tbody>
</table>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-breaking-changes-summary">Breaking Changes Summary</h4>
<ol>
<li><strong>Unified Tool Pattern</strong>: All tools must be defined on the server using <code>tool()</code></li>
<li><strong><code>convertToModelMessages()</code> is async</strong>: Add <code>await</code> to all calls</li>
<li><strong><code>CoreMessage</code> removed</strong>: Use <code>ModelMessage</code> instead</li>
<li><strong><code>generateObject</code> mode removed</strong>: Remove <code>mode</code> option</li>
<li><strong><code>isToolUIPart</code> behavior changed</strong>: Now checks both static and dynamic tool parts</li>
</ol>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-installation">Installation</h4>
<p>Update your dependencies to use the latest versions:</p>
<pre tabindex="0"><code class="language-bash">npm install agents@^0.3.0 workers-ai-provider@^3.0.0 ai-gateway-provider@^3.0.0 ai@^6.0.0 @ai-sdk/react@^3.0.0 @ai-sdk/openai@^3.0.0&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v6.md">Migration Guide</a> - Comprehensive migration documentation from v5 to v6</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0">AI SDK v6 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://vercel.com/blog/ai-sdk-6">AI SDK v6 Announcement</a> - Learn about new features in v6</li>
<li><a href="https://sdk.vercel.ai/docs">AI SDK Documentation</a> - Complete AI SDK reference</li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade from v5 to v6?</li>
<li><strong>Unified tool pattern</strong> - How does the new server-defined tool pattern work for you?</li>
<li><strong>Dynamic tool approval</strong> - Does the <code>needsApproval</code> feature meet your needs?</li>
<li><strong>AI Gateway integration</strong> - How well does the new provider work with your setup?</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-19">Dec 19, 2025</time><div>
<h2 id="post-2025-12-19-terraform-v5.15.0-provider"><a href="/changelog/post/2025-12-19-terraform-v5.15.0-provider/">Terraform v5.15.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-19-terraform-v5.15.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search:</strong> Add AI Search endpoints (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915">6f02adb</a>)</li>
<li><strong>certificate_pack:</strong> Ensure proper Terraform resource ID handling for path parameters in API calls (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a">081f32a</a>)</li>
<li><strong>worker_version:</strong> Support <code>startup_time_ms</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba">286ab55</a>)</li>
<li><strong>zero_trust_dlp_custom_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_gateway_policy:</strong> Support <code>forensic_copy</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
<li><strong>zero_trust_list:</strong> Support additional types (category, location, device) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>access_rules:</strong> Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d">4457791</a>)</li>
<li><strong>cloudflare_pages_project:</strong> Addressing drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e">6edffcf</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0">3db318e</a>)</li>
<li><strong>cloudflare_worker:</strong> Can be cleanly imported (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f">4859b52</a>)</li>
<li><strong>cloudflare_worker:</strong> Ensure clean imports (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a">5b525bc</a>)</li>
<li><strong>list_items:</strong> Add validation for IP List items to avoid inconsistent state (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada">b6733dc</a>)</li>
<li><strong>zero_trust_access_application:</strong> Remove all conditions from sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7">3197f1a</a>)</li>
<li><strong>spectrum_application:</strong> Map missing fields during spectrum resource import (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495">#6495</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa">ddb4e72</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-19-terraform-v5.15.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-19">Dec 19, 2025</time><div>
<h2 id="post-2025-12-19-tanstack-start-prerendering"><a href="/changelog/post/2025-12-19-tanstack-start-prerendering/">Static prerendering support for TanStack Start</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://tanstack.com/start/">TanStack Start</a> apps can now prerender routes to static HTML at build time with access to build time environment variables
and bindings,  and serve them as <a href="/workers/static-assets/">static assets</a>. To enable prerendering, configure the <code>prerender</code> option of the TanStack Start plugin in your Vite config:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;&#10;export default defineConfig({&#10;  plugins: [&#10;    cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;    tanstackStart({&#10;      prerender: {&#10;        enabled: true,&#10;      },&#10;    }),&#10;  ],&#10;});&#10;</code></pre>
<p>This feature requires <code>@tanstack/react-start</code> v1.138.0 or later. See the <a href="/workers/framework-guides/web-apps/tanstack-start/#static-prerendering">TanStack Start framework guide</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-overview-tab"><a href="/changelog/post/2025-12-18-overview-tab/">New AI Crawl Control Overview tab</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>The <strong>Overview</strong> tab is now the default view in AI Crawl Control. The previous default view with controls for individual AI crawlers is available in the <strong>Crawlers</strong> tab.</p>
<h4 id="2025-12-18-overview-tab-what-s-new">What's new</h4>
<ul>
<li><strong>Executive summary</strong> — Monitor total requests, volume change, most common status code, most popular path, and high-volume activity</li>
<li><strong>Operator grouping</strong> — Track crawlers by their operating companies (OpenAI, Microsoft, Google, ByteDance, Anthropic, Meta)</li>
<li><strong>Customizable filters</strong> — Filter your snapshot by date range, crawler, operator, hostname, or path</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview-tab.png" alt="AI Crawl Control Overview tab showing executive summary, metrics, and crawler groups" /></p>
<h4 id="2025-12-18-overview-tab-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>, where the <strong>Overview</strong> tab opens by default with your activity snapshot.</li>
<li>Use filters to customize your view by date range, crawler, operator, hostname, or path.</li>
<li>Navigate to the <strong>Crawlers</strong> tab to manage controls for individual crawlers.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a> and <a href="/ai-crawl-control/features/manage-ai-crawlers/">managing AI crawlers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-cached-request-classification"><a href="/changelog/post/2025-12-18-cached-request-classification/">Improved accuracy of cached request classification in analytics</a></h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.</p>
<p>Previously, requests were classified as &quot;cached&quot; based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.</p>
<p>The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in <a href="/analytics/account-and-zone-analytics/zone-analytics/">HTTP Analytics</a>, so only requests genuinely served from cache are counted as cached.</p>
<p><strong>What changed:</strong></p>
<ul>
<li><strong>Zone Overview</strong> — Cache ratios now reflect actual cache performance.</li>
<li><strong>HTTP Analytics</strong> — No change. HTTP Analytics already used the correct classification logic.</li>
<li><strong>Historical data</strong> — This fix applies to new requests only. Previously logged data is not retroactively updated.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-r2-data-catalog-snapshot-expiration"><a href="/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/">R2 Data Catalog now supports automatic snapshot expiration</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> now supports automatic snapshot expiration for Apache Iceberg tables.</p>
<p>In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.</p>
<p>Without regular cleanup, these accumulated snapshots can lead to:</p>
<ul>
<li>Metadata overhead</li>
<li>Slower table operations</li>
<li>Increased storage costs.</li>
</ul>
<p>Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;&#35; Expire snapshots older than 7 days, always retain at least 10 recent snapshots&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: age threshold in days</li>
<li><code>--retain-last</code>: minimum snapshot count to retain</li>
</ul>
<p>Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.</p>
<p>This feature complements <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> or <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/27/">Previous</a><span>Page 28 of 50</span><a class="pagination-next" rel="next" href="/changelog/29/">Next</a></nav>
</div>
