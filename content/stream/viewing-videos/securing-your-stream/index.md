---
cp9:
  canonical: https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/
  description: Restrict access to Cloudflare Stream videos using signed URLs and tokens.
  full_title: Secure your Stream · Cloudflare Stream docs
  head_html: <title>Secure your Stream · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict access to Cloudflare Stream videos using signed URLs and tokens."><link rel="canonical" href="https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/index.md"><meta property="og:title" content="Secure your Stream · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict access to Cloudflare Stream videos using signed URLs and tokens."><meta property="og:url" content="https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/#page","headline":"Secure your Stream \u00b7 Cloudflare Stream docs","description":"Restrict access to Cloudflare Stream videos using signed URLs and tokens.","url":"https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/viewing-videos/securing-your-stream/
  schema: 1
---
<h2 id="signed-urls-tokens">Signed URLs / Tokens</h2>
<p>By default, videos on Stream can be viewed by anyone with just a video id. If you want to make your video private by default and only give access to certain users, you can use the signed URL feature. When you mark a video to require signed URL, it can no longer be accessed publicly with only the video id. Instead, the user will need a signed url token to watch or download the video.</p>
<p>Here are some common use cases for using signed URLs:</p>
<ul>
<li>Restricting access so only logged in members can watch a particular video</li>
<li>Let users watch your video for a limited time period (ie. 24 hours)</li>
<li>Restricting access based on geolocation</li>
</ul>
<h3 id="making-a-video-require-signed-urls">Making a video require signed URLs</h3>
<p>Turn on <code>requireSignedURLs</code> to protect a video using signed URLs. This option will prevent <em>any public links</em>, such as <code>customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_ID&gt;/watch</code> or the built-in player, from working.</p>
<p>Restricting viewing can be done by updating the video's metadata.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/{video_uid}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot;&#10;&#45;-data &quot;{\&quot;uid\&quot;: \&quot;&lt;VIDEO_UID&gt;\&quot;, \&quot;requireSignedURLs\&quot;: true }&quot;&#10;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;&lt;VIDEO_UID&gt;&quot;,&#10;    ...&#10;    &quot;requireSignedURLs&quot;: true&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="workers-binding">Workers binding</h4>
<p>You can also require signed URLs using the Stream binding in your Worker. Refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a> for setup instructions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14327.md")
</div>
<h2 id="three-ways-to-generate-signed-tokens">Three Ways to Generate Signed Tokens</h2>
<p>You can program your app to generate tokens in three ways:</p>
<ul>
<li>
<p><strong>Low-volume or testing: Use the <code>/token</code> endpoint to generate a short-lived signed token.</strong> This is recommended for testing purposes or if you are generating less than 1,000 tokens per day. It requires making an API call to Cloudflare for each token, <em>which is subject to <a href="/fundamentals/api/reference/limits/">rate limiting</a>.</em> The default result is valid for 1 hour. This method does not support <a href="/stream/webrtc-beta/">Live WebRTC</a>.</p>
</li>
<li>
<p><strong>Recommended: Use a signing key to create tokens.</strong> If you have thousands of daily users or need to generate a high volume of tokens, as with <a href="/stream/webrtc-beta/">Live WebRTC</a>, you can create tokens yourself using a signing key. This way, you do not need to call a Stream API each time you need to generate a token, and is therefore <em>not</em> a rate-limited operation.</p>
</li>
<li>
<p><strong>Workers binding: Use the Stream binding to generate tokens.</strong> If you are using Cloudflare Workers with the Stream binding, you can generate tokens directly without making a separate API call or managing signing keys. This is the simplest approach for Workers users. For advanced customization such as access rules or custom expiration, use a signing key instead.</p>
</li>
</ul>
<h2 id="option-1-using-the-token-endpoint">Option 1: Using the /token endpoint</h2>
<p>You can call the <code>/token</code> endpoint for any video that is marked private to get a signed URL token which expires in one hour. This method does not support <a href="/stream/webrtc-beta/">Live WebRTC</a>.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/{video_uid}/token \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>You will see a response similar to this if the request succeeds:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;token&quot;: &quot;eyJhbGciOiJSUzI1NiIsImtpZCI6ImNkYzkzNTk4MmY4MDc1ZjJlZjk2MTA2ZDg1ZmNkODM4In0.eyJraWQiOiJjZGM5MzU5ODJmODA3NWYyZWY5NjEwNmQ4NWZjZDgzOCIsImV4cCI6IjE2MjE4ODk2NTciLCJuYmYiOiIxNjIxODgyNDU3In0.iHGMvwOh2-SuqUG7kp2GeLXyKvMavP-I2rYCni9odNwms7imW429bM2tKs3G9INms8gSc7fzm8hNEYWOhGHWRBaaCs3U9H4DRWaFOvn0sJWLBitGuF_YaZM5O6fqJPTAwhgFKdikyk9zVzHrIJ0PfBL0NsTgwDxLkJjEAEULQJpiQU1DNm0w5ctasdbw77YtDwdZ01g924Dm6jIsWolW0Ic0AevCLyVdg501Ki9hSF7kYST0egcll47jmoMMni7ujQCJI1XEAOas32DdjnMvU8vXrYbaHk1m1oXlm319rDYghOHed9kr293KM7ivtZNlhYceSzOpyAmqNFS7mearyQ&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="workers-binding-1">Workers binding</h4>
<p>You can generate a signed token using the Stream binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14328.md")
</div>
<p>To render the video or use assets like manifests or thumbnails, use the <code>token</code> value in place of the video/input ID. For example, to use the Stream player, replace the ID between <code>cloudflarestream.com/</code> and <code>/iframe</code> with the token: <code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;TOKEN&gt;/iframe</code>.</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/eyJhbGciOiJSUzI1NiIsImtpZCI6ImNkYzkzNTk4MmY4MDc1ZjJlZjk2MTA2ZDg1ZmNkODM4In0.eyJraWQiOiJjZGM5MzU5ODJmODA3NWYyZWY5NjEwNmQ4NWZjZDgzOCIsImV4cCI6IjE2MjE4ODk2NTciLCJuYmYiOiIxNjIxODgyNDU3In0.iHGMvwOh2-SuqUG7kp2GeLXyKvMavP-I2rYCni9odNwms7imW429bM2tKs3G9INms8gSc7fzm8hNEYWOhGHWRBaaCs3U9H4DRWaFOvn0sJWLBitGuF_YaZM5O6fqJPTAwhgFKdikyk9zVzHrIJ0PfBL0NsTgwDxLkJjEAEULQJpiQU1DNm0w5ctasdbw77YtDwdZ01g924Dm6jIsWolW0Ic0AevCLyVdg501Ki9hSF7kYST0egcll47jmoMMni7ujQCJI1XEAOas32DdjnMvU8vXrYbaHk1m1oXlm319rDYghOHed9kr293KM7ivtZNlhYceSzOpyAmqNFS7mearyQ/iframe&quot;&#10;	style=&quot;border: none;&quot;&#10;	height=&quot;720&quot;&#10;	width=&quot;1280&quot;&#10;	allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;	allowfullscreen=&quot;true&quot;&#10;&gt;&lt;/iframe&gt;&#10;</code></pre>
<p>Similarly, if you are using your own player, retrieve the HLS or DASH manifest by replacing the video ID in the manifest URL with the <code>token</code> value:</p>
<ul>
<li><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;TOKEN&gt;/manifest/video.m3u8</code></li>
<li><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;TOKEN&gt;/manifest/video.mpd</code></li>
</ul>
<h3 id="customizing-default-restrictions">Customizing default restrictions</h3>
<p>If you call the <code>/token</code> endpoint without any body, it will return a token that expires in one hour without any other restrictions or access to <a href="/stream/viewing-videos/download-videos/">downloads</a>. This token can be customized by providing additional properties in the request:</p>
<pre tabindex="0"><code class="language-javascript">	const signed_url_restrictions = {&#10;		// Extend the lifetime of the token to 12 hours:&#10;		exp: Math.floor(Date.now() / 1000) + 12 * 60 * 60,&#10;		// Allow access to MP4 or Audio Download URLs:&#10;		downloadable: true,&#10;		// Geo or IP access restrictions:&#10;		accessRules: {&#10;			// ... see examples below&#10;		}&#10;	};&#10;&#10;	const init = {&#10;		method: &quot;POST&quot;,&#10;		headers: {&#10;			Authorization: &quot;Bearer &lt;API_TOKEN&gt;&quot;,&#10;			&quot;content-type&quot;: &quot;application/json;charset=UTF-8&quot;,&#10;		},&#10;		body: JSON.stringify(signed_url_restrictions),&#10;	};&#10;&#10;	const signedurl_service_response = await fetch(&#10;		&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/{video_uid}/token&quot;,&#10;		init,&#10;	);&#10;&#10;	return new Response(&#10;		JSON.stringify(await signedurl_service_response.json()),&#10;		{ status: 200 },&#10;	);&#10;</code></pre>
<p>However, if you are generating tokens programmatically or adding customizations like these, it is faster and more scalable to use a signing key and generate the token within your application entirely.</p>
<h2 id="option-2-using-the-stream-binding">Option 2: Using the Stream binding</h2>
<p>If you are using the Stream binding in your Worker, you can generate signed tokens without making a separate API call to the <code>/token</code> endpoint or managing signing keys yourself. The binding handles token generation internally.</p>
<p>Refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a> for setup instructions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14329.md")
</div>
<p>The token generated by the binding expires in one hour by default. If you need to customize restrictions such as expiration time, geolocation, or download access, use <a href="#option-3-using-a-signing-key-to-create-signed-tokens">a signing key</a> to create tokens with custom claims.</p>
<h2 id="option-3-using-a-signing-key-to-create-signed-tokens">Option 3: Using a signing key to create signed tokens</h2>
<p>If you are generating a high-volume of tokens, using <a href="/stream/webrtc-beta/">Live WebRTC</a>, or need to customize the access rules, generate new tokens using a signing key so you do not need to call the Stream API each time.</p>
<h3 id="step-1-call-the-stream-key-endpoint-once-to-obtain-a-key">Step 1: Call the <code>/stream/key</code> endpoint <em>once</em> to obtain a key</h3>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/keys&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>The response will return <code>pem</code> and <code>jwk</code> values.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;8f926b2b01f383510025a78a4dcbf6a&quot;,&#10;		&quot;pem&quot;: &quot;LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBemtHbXhCekFGMnBIMURiWmgyVGoyS3ZudlBVTkZmUWtNeXNCbzJlZzVqemRKTmRhCmtwMEphUHhoNkZxOTYveTBVd0lBNjdYeFdHb3kxcW1CRGhpdTVqekdtYW13NVgrYkR3TEdTVldGMEx3QnloMDYKN01Rb0xySHA3MDEycXBVNCtLODUyT1hMRVVlWVBrOHYzRlpTQ2VnMVdLRW5URC9oSmhVUTFsTmNKTWN3MXZUbQpHa2o0empBUTRBSFAvdHFERHFaZ3lMc1Vma2NsRDY3SVRkZktVZGtFU3lvVDVTcnFibHNFelBYcm9qaFlLWGk3CjFjak1yVDlFS0JCenhZSVEyOVRaZitnZU5ya0t4a2xMZTJzTUFML0VWZkFjdGkrc2ZqMkkyeEZKZmQ4aklmL2UKdHBCSVJZVDEza2FLdHUyYmk0R2IrV1BLK0toQjdTNnFGODlmTHdJREFRQUJBb0lCQUYzeXFuNytwNEtpM3ZmcgpTZmN4ZmRVV0xGYTEraEZyWk1mSHlaWEFJSnB1MDc0eHQ2ZzdqbXM3Tm0rTFVhSDV0N3R0bUxURTZacy91RXR0CjV3SmdQTjVUaFpTOXBmMUxPL3BBNWNmR2hFN1pMQ2wvV2ZVNXZpSFMyVDh1dGlRcUYwcXpLZkxCYk5kQW1MaWQKQWl4blJ6UUxDSzJIcmlvOW1KVHJtSUUvZENPdG80RUhYdHpZWjByOVordHRxMkZrd3pzZUdaK0tvd09JaWtvTgp2NWFOMVpmRGhEVG0wdG1Vd0tLbjBWcmZqalhRdFdjbFYxTWdRejhwM2xScWhISmJSK29PL1NMSXZqUE16dGxOCm5GV1ZEdTRmRHZsSjMyazJzSllNL2tRVUltT3V5alY3RTBBcm5vR2lBREdGZXFxK1UwajluNUFpNTJ6aTBmNloKdFdvwdju39xOFJWQkwxL2tvWFVmYk00S04ydVFadUdjaUdGNjlCRDJ1S3o1eGdvTwowVTBZNmlFNG9Cek5GUW5hWS9kayt5U1dsQWp2MkgraFBrTGpvZlRGSGlNTmUycUVNaUFaeTZ5cmRkSDY4VjdIClRNRllUQlZQaHIxT0dxZlRmc00vRktmZVhWY1FvMTI1RjBJQm5iWjNSYzRua1pNS0hzczUyWE1DZ1lFQTFQRVkKbGIybDU4blVianRZOFl6Uk1vQVo5aHJXMlhwM3JaZjE0Q0VUQ1dsVXFZdCtRN0NyN3dMQUVjbjdrbFk1RGF3QgpuTXJsZXl3S0crTUEvU0hlN3dQQkpNeDlVUGV4Q3YyRW8xT1loMTk3SGQzSk9zUythWWljemJsYmJqU0RqWXVjCkdSNzIrb1FlMzJjTXhjczJNRlBWcHVibjhjalBQbnZKd0k5aUpGVUNnWUVBMjM3UmNKSEdCTjVFM2FXLzd3ekcKbVBuUm1JSUczeW9UU0U3OFBtbHo2bXE5eTVvcSs5aFpaNE1Fdy9RbWFPMDF5U0xRdEY4QmY2TFN2RFh4QWtkdwpWMm5ra0svWWNhWDd3RHo0eWxwS0cxWTg3TzIwWWtkUXlxdjMybG1lN1JuVDhwcVBDQTRUWDloOWFVaXh6THNoCkplcGkvZFhRWFBWeFoxYXV4YldGL3VzQ2dZRUFxWnhVVWNsYVlYS2dzeUN3YXM0WVAxcEwwM3h6VDR5OTBOYXUKY05USFhnSzQvY2J2VHFsbGVaNCtNSzBxcGRmcDM5cjIrZFdlemVvNUx4YzBUV3Z5TDMxVkZhT1AyYk5CSUpqbwpVbE9ldFkwMitvWVM1NjJZWVdVQVNOandXNnFXY21NV2RlZjFIM3VuUDVqTVVxdlhRTTAxNjVnV2ZiN09YRjJyClNLYXNySFVDZ1lCYmRvL1orN1M3dEZSaDZlamJib2h3WGNDRVd4eXhXT2ZMcHdXNXdXT3dlWWZwWTh4cm5pNzQKdGRObHRoRXM4SHhTaTJudEh3TklLSEVlYmJ4eUh1UG5pQjhaWHBwNEJRNTYxczhjR1Z1ZSszbmVFUzBOTDcxZApQL1ZxUWpySFJrd3V5ckRFV2VCeEhUL0FvVEtEeSt3OTQ2SFM5V1dPTGJvbXQrd3g0NytNdWc9PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo=&quot;,&#10;		&quot;jwk&quot;: &quot;eyJ1c2UiOiJzaWciLCJrdHkiOiJSU0EiLCJraWQiOiI4ZjkyNmIyYjAxZjM4MzUxNzAwMjVhNzhhNGRjYmY2YSIsImFsZyI6IlJTMjU2IiwibiI6InprR214QnpBRjJwSDFEYlpoMlRqMkt2bnZQVU5GZlFrTXlzQm8yZWc1anpkSk5kYWtwMEphUHhoNkZxOTZfeTBVd0lBNjdYeFdHb3kxcW1CRGhpdTVqekdtYW13NVgtYkR3TEdTVldGMEx3QnloMDY3TVFvTHJIcDcwMTJxcFU0LUs4NTJPWExFVWVZUGs4djNGWlNDZWcxV0tFblREX2hKaFVRMWxOY0pNY3cxdlRtR2tqNHpqQVE0QUhQX3RxRERxWmd5THNVZmtjbEQ2N0lUZGZLVWRrRVN5b1Q1U3JxYmxzRXpQWHJvamhZS1hpNzFjak1yVDlFS0JCenhZSVEyOVRaZi1nZU5ya0t4a2xMZTJzTUFMX0VWZkFjdGktc2ZqMkkyeEZKZmQ4aklmX2V0cEJJUllUMTNrYUt0dTJiaTRHYi1XUEstS2hCN1M2cUY4OWZMdyIsImUiOiJBUUFCIiwiZCI6IlhmS3FmdjZuZ3FMZTktdEo5ekY5MVJZc1ZyWDZFV3RreDhmSmxjQWdtbTdUdmpHM3FEdU9henMyYjR0Um9mbTN1MjJZdE1UcG16LTRTMjNuQW1BODNsT0ZsTDJsX1VzNy1rRGx4OGFFVHRrc0tYOVo5VG0tSWRMWlB5NjJKQ29YU3JNcDhzRnMxMENZdUowQ0xHZEhOQXNJcllldUtqMllsT3VZZ1Q5MEk2MmpnUWRlM05oblN2MW42MjJyWVdURE94NFpuNHFqQTRpS1NnMl9sbzNWbDhPRU5PYlMyWlRBb3FmUld0LU9OZEMxWnlWWFV5QkRQeW5lVkdxRWNsdEg2Zzc5SXNpLU04ek8yVTJjVlpVTzdoOE8tVW5mYVRhd2xnei1SQlFpWTY3S05Yc1RRQ3VlZ2FJQU1ZVjZxcjVUU1Ai2odx5iT0xSX3BtMWFpdktyUSIsInAiOiI5X1o5ZUpGTWI5X3E4UlZCTDFfa29YVWZiTTRLTjJ1UVp1R2NpR0Y2OUJEMnVLejV4Z29PMFUwWTZpRTRvQnpORlFuYVlfZGsteVNXbEFqdjJILWhQa0xqb2ZURkhpTU5lMnFFTWlBWnk2eXJkZEg2OFY3SFRNRllUQlZQaHIxT0dxZlRmc01fRktmZVhWY1FvMTI1RjBJQm5iWjNSYzRua1pNS0hzczUyWE0iLCJxIjoiMVBFWWxiMmw1OG5VYmp0WThZelJNb0FaOWhyVzJYcDNyWmYxNENFVENXbFVxWXQtUTdDcjd3TEFFY243a2xZNURhd0JuTXJsZXl3S0ctTUFfU0hlN3dQQkpNeDlVUGV4Q3YyRW8xT1loMTk3SGQzSk9zUy1hWWljemJsYmJqU0RqWXVjR1I3Mi1vUWUzMmNNeGNzMk1GUFZwdWJuOGNqUFBudkp3STlpSkZVIiwiZHAiOiIyMzdSY0pIR0JONUUzYVdfN3d6R21QblJtSUlHM3lvVFNFNzhQbWx6Nm1xOXk1b3EtOWhaWjRNRXdfUW1hTzAxeVNMUXRGOEJmNkxTdkRYeEFrZHdWMm5ra0tfWWNhWDd3RHo0eWxwS0cxWTg3TzIwWWtkUXlxdjMybG1lN1JuVDhwcVBDQTRUWDloOWFVaXh6THNoSmVwaV9kWFFYUFZ4WjFhdXhiV0ZfdXMiLCJkcSI6InFaeFVVY2xhWVhLZ3N5Q3dhczRZUDFwTDAzeHpUNHk5ME5hdWNOVEhYZ0s0X2NidlRxbGxlWjQtTUswcXBkZnAzOXIyLWRXZXplbzVMeGMwVFd2eUwzMVZGYU9QMmJOQklKam9VbE9ldFkwMi1vWVM1NjJZWVdVQVNOandXNnFXY21NV2RlZjFIM3VuUDVqTVVxdlhRTTAxNjVnV2ZiN09YRjJyU0thc3JIVSIsInFpIjoiVzNhUDJmdTB1N1JVWWVubzIyNkljRjNBaEZzY3NWam55NmNGdWNGanNIbUg2V1BNYTU0dS1MWFRaYllSTFBCOFVvdHA3UjhEU0NoeEhtMjhjaDdqNTRnZkdWNmFlQVVPZXRiUEhCbGJudnQ1M2hFdERTLTlYVF8xYWtJNngwWk1Mc3F3eEZuZ2NSMF93S0V5Zzh2c1BlT2gwdlZsamkyNkpyZnNNZU9fakxvIn0=&quot;,&#10;		&quot;created&quot;: &quot;2021-06-15T21:06:54.763937286Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>These values will not be shown again so we recommend saving them securely right away. If you are using Cloudflare Workers, you can store them using <a href="/workers/configuration/secrets/">Secrets</a>. If you are using another platform, store them in secure environment variables.</p>
<p>You will use these values later to generate the tokens. The pem and jwk fields are base64-encoded, you must decode them before using them (an example of this is shown in step 2).</p>
<h3 id="step-2-generate-tokens-using-the-key">Step 2: Generate tokens using the key</h3>
<p>Once you generate the key in step 1, you can use the <code>pem</code> or <code>jwk</code> values to generate self-signing URLs on your own. Using this method, you do not need to call the Stream API each time you are creating a new token.</p>
<p>Here's an example Cloudflare Worker script which generates tokens that expire in 60 minutes and only work for users accessing the video from UK. In lines 2 and 3, you will configure the <code>id</code> and <code>jwk</code> values from step 1:</p>
<pre tabindex="0"><code class="language-javascript">// Global variables&#10;const jwkKey = &quot;{PRIVATE-KEY-IN-JWK-FORMAT}&quot;;&#10;const keyID = &quot;&lt;KEY_ID&gt;&quot;;&#10;const videoUID = &quot;&lt;VIDEO_UID&gt;&quot;;&#10;// expiresTimeInS is the expired time in second of the video&#10;const expiresTimeInS = 3600;&#10;&#10;// Main function&#10;async function streamSignedUrl() {&#10;	const encoder = new TextEncoder();&#10;	const expiresIn = Math.floor(Date.now() / 1000) + expiresTimeInS;&#10;	const headers = {&#10;		alg: &quot;RS256&quot;,&#10;		kid: keyID,&#10;	};&#10;	const data = {&#10;		sub: videoUID,&#10;		kid: keyID,&#10;		exp: expiresIn,&#10;		// Add `downloadable` boolean for access to MP4 or Audio Downloads:&#10;		// downloadable: true,&#10;		accessRules: [&#10;			{&#10;				type: &quot;ip.geoip.country&quot;,&#10;				action: &quot;allow&quot;,&#10;				country: [&quot;GB&quot;],&#10;			},&#10;			{&#10;				type: &quot;any&quot;,&#10;				action: &quot;block&quot;,&#10;			},&#10;		],&#10;	};&#10;&#10;	const token = `${objectToBase64url(headers)}.${objectToBase64url(data)}`;&#10;&#10;	const jwk = JSON.parse(atob(jwkKey));&#10;&#10;	const key = await crypto.subtle.importKey(&#10;		&quot;jwk&quot;,&#10;		jwk,&#10;		{&#10;			name: &quot;RSASSA-PKCS1-v1_5&quot;,&#10;			hash: &quot;SHA-256&quot;,&#10;		},&#10;		false,&#10;		[&quot;sign&quot;],&#10;	);&#10;&#10;	const signature = await crypto.subtle.sign(&#10;		{ name: &quot;RSASSA-PKCS1-v1_5&quot; },&#10;		key,&#10;		encoder.encode(token),&#10;	);&#10;&#10;	const signedToken = `${token}.${arrayBufferToBase64Url(signature)}`;&#10;&#10;	return signedToken;&#10;}&#10;&#10;// Utilities functions&#10;function arrayBufferToBase64Url(buffer) {&#10;	return btoa(String.fromCharCode(...new Uint8Array(buffer)))&#10;		.replace(/=/g, &quot;&quot;)&#10;		.replace(/\+/g, &quot;-&quot;)&#10;		.replace(/\//g, &quot;_&quot;);&#10;}&#10;&#10;function objectToBase64url(payload) {&#10;	return arrayBufferToBase64Url(&#10;		new TextEncoder().encode(JSON.stringify(payload)),&#10;	);&#10;}&#10;</code></pre>
<h3 id="step-3-rendering-the-video">Step 3: Rendering the video</h3>
<p>If you are using the Stream Player, insert the <code>token</code> value returned by the Worker in Step 2 in place of the <code>video id</code>, replacing the entire string located between <code>cloudflarestream.com/</code> and <code>/iframe</code>:</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/eyJhbGciOiJSUzI1NiIsImtpZCI6ImNkYzkzNTk4MmY4MDc1ZjJlZjk2MTA2ZDg1ZmNkODM4In0.eyJraWQiOiJjZGM5MzU5ODJmODA3NWYyZWY5NjEwNmQ4NWZjZDgzOCIsImV4cCI6IjE2MjE4ODk2NTciLCJuYmYiOiIxNjIxODgyNDU3In0.iHGMvwOh2-SuqUG7kp2GeLXyKvMavP-I2rYCni9odNwms7imW429bM2tKs3G9INms8gSc7fzm8hNEYWOhGHWRBaaCs3U9H4DRWaFOvn0sJWLBitGuF_YaZM5O6fqJPTAwhgFKdikyk9zVzHrIJ0PfBL0NsTgwDxLkJjEAEULQJpiQU1DNm0w5ctasdbw77YtDwdZ01g924Dm6jIsWolW0Ic0AevCLyVdg501Ki9hSF7kYST0egcll47jmoMMni7ujQCJI1XEAOas32DdjnMvU8vXrYbaHk1m1oXlm319rDYghOHed9kr293KM7ivtZNlhYceSzOpyAmqNFS7mearyQ/iframe&quot;&#10;	style=&quot;border: none;&quot;&#10;	height=&quot;720&quot;&#10;	width=&quot;1280&quot;&#10;	allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;	allowfullscreen=&quot;true&quot;&#10;&gt;&lt;/iframe&gt;&#10;</code></pre>
<p>If you are using your own player, replace the video id in the manifest url with the <code>token</code> value:</p>
<p><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/eyJhbGciOiJSUzI1NiIsImtpZCI6ImNkYzkzNTk4MmY4MDc1ZjJlZjk2MTA2ZDg1ZmNkODM4In0.eyJraWQiOiJjZGM5MzU5ODJmODA3NWYyZWY5NjEwNmQ4NWZjZDgzOCIsImV4cCI6IjE2MjE4ODk2NTciLCJuYmYiOiIxNjIxODgyNDU3In0.iHGMvwOh2-SuqUG7kp2GeLXyKvMavP-I2rYCni9odNwms7imW429bM2tKs3G9INms8gSc7fzm8hNEYWOhGHWRBaaCs3U9H4DRWaFOvn0sJWLBitGuF_YaZM5O6fqJPTAwhgFKdikyk9zVzHrIJ0PfBL0NsTgwDxLkJjEAEULQJpiQU1DNm0w5ctasdbw77YtDwdZ01g924Dm6jIsWolW0Ic0AevCLyVdg501Ki9hSF7kYST0egcll47jmoMMni7ujQCJI1XEAOas32DdjnMvU8vXrYbaHk1m1oXlm319rDYghOHed9kr293KM7ivtZNlhYceSzOpyAmqNFS7mearyQ/manifest/video.m3u8</code></p>
<p>To allow access to <a href="/stream/viewing-videos/download-videos/">MP4 or audio downloads</a>, make sure the video has the download type already enabled. Then add <code>downloadable: true</code> to the payload as shown in the comment above when generating the signed URL. Replace the video id in the download URL with the <code>token</code> value:</p>
<ul>
<li><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/eyJhbGciOiJ.../downloads/default.mp4</code></li>
</ul>
<h3 id="revoking-keys">Revoking keys</h3>
<p>You can create up to 1,000 keys and rotate them at your convenience.
Once revoked all tokens created with that key will be invalidated.</p>
<pre tabindex="0"><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/keys/{key_id}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;&#10;&#35; Response:&#10;{&#10;  &quot;result&quot;: &quot;Revoked&quot;,&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="supported-restrictions">Supported Restrictions</h2>
<table>
<thead>
<tr>
<th>Property Name</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>exp</td>
<td>Expiration. A unix epoch timestamp after which the token will stop working. Cannot be greater than 24 hours in the future from when the token is signed</td>
<td></td>
</tr>
<tr>
<td>nbf</td>
<td><em>Not Before</em> value. A unix epoch timestamp before which the token will not work</td>
<td></td>
</tr>
<tr>
<td>downloadable</td>
<td>if true, the token can be used to download the mp4 (assuming the video has downloads enabled)</td>
<td></td>
</tr>
<tr>
<td>accessRules</td>
<td>An array that specifies one or more ip and geo restrictions. accessRules are evaluated first-to-last. If a Rule matches, the associated action is applied and no further rules are evaluated. A token may have at most 5 members in the accessRules array.</td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="accessrules-schema">accessRules Schema</h3>
<p>Each accessRule must include 2 required properties:</p>
<ul>
<li><code>type</code>: supported values are <code>any</code>, <code>ip.src</code> and <code>ip.geoip.country</code></li>
<li><code>action</code>: support values are <code>allow</code> and <code>block</code></li>
</ul>
<p>Depending on the rule type, accessRules support 2 additional properties:</p>
<ul>
<li><code>country</code>: an array of 2-letter country codes in <a href="https://www.iso.org/obp/ui/#search">ISO 3166-1 Alpha 2</a> format.</li>
<li><code>ip</code>: an array of ip ranges. It is recommended to include both IPv4 and IPv6 variants in a rule if possible. Having only a single variant in a rule means that rule will ignore the other variant. For example, an IPv4-based rule will never be applicable to a viewer connecting from an IPv6 address. CIDRs should be preferred over specific IP addresses. Some devices, such as mobile, may change their IP over the course of a view. Video Access Control are evaluated continuously while a video is being viewed. As a result, overly strict IP rules may disrupt playback.</li>
</ul>
<p><strong><em>Example 1: Block views from a specific country</em></strong></p>
<pre tabindex="0"><code class="language-txt">...&#10;&quot;accessRules&quot;: [&#10;	{&#10;		&quot;type&quot;: &quot;ip.geoip.country&quot;,&#10;		&quot;action&quot;: &quot;block&quot;,&#10;		&quot;country&quot;: [&quot;US&quot;, &quot;DE&quot;, &quot;MX&quot;],&#10;	},&#10;]&#10;</code></pre>
<p>The first rule matches on country, US, DE, and MX here. When that rule matches, the block action will have the token considered invalid. If the first rule doesn't match, there are no further rules to evaluate. The behavior in this situation is to consider the token valid.</p>
<p><strong><em>Example 2: Allow only views from specific country or IPs</em></strong></p>
<pre tabindex="0"><code class="language-txt">...&#10;&quot;accessRules&quot;: [&#10;	{&#10;		&quot;type&quot;: &quot;ip.geoip.country&quot;,&#10;		&quot;country&quot;: [&quot;US&quot;, &quot;MX&quot;],&#10;		&quot;action&quot;: &quot;allow&quot;,&#10;	},&#10;	{&#10;		&quot;type&quot;: &quot;ip.src&quot;,&#10;		&quot;ip&quot;: [&quot;93.184.216.0/24&quot;, &quot;2400:cb00::/32&quot;],&#10;		&quot;action&quot;: &quot;allow&quot;,&#10;	},&#10;	{&#10;		&quot;type&quot;: &quot;any&quot;,&#10;		&quot;action&quot;: &quot;block&quot;,&#10;	},&#10;]&#10;</code></pre>
<p>The first rule matches on country, US and MX here. When that rule matches, the allow action will have the token considered valid. If it doesn't match we continue evaluating rules</p>
<p>The second rule is an IP rule matching on CIDRs, 93.184.216.0/24 and 2400:cb00::/32. When that rule matches, the allow action will consider the rule valid.</p>
<p>If the first two rules don't match, the final rule of any will match all remaining requests and block those views.</p>
<h2 id="security-considerations">Security considerations</h2>
<h3 id="hotlinking-protection">Hotlinking Protection</h3>
<p>By default, Stream embed codes can be used on any domain. If needed, you can limit the domains a video can be embedded on from the Stream dashboard.</p>
<p>In the dashboard, you will see a text box by each video labeled <code>Enter allowed origin domains separated by commas</code>. If you click on it, you can list the domains that the Stream embed code should be able to be used on.
`</p>
<ul>
<li><code>*.badtortilla.com</code> covers <code>a.badtortilla.com</code>, <code>a.b.badtortilla.com</code> and does not cover <code>badtortilla.com</code></li>
<li><code>example.com</code> does not cover <a href="http://www.example.com">www.example.com</a> or any subdomain of example.com</li>
<li><code>localhost</code> requires a port if it is not being served over HTTP on port 80 or over HTTPS on port 443</li>
<li>There is no path support - <code>example.com</code> covers <code>example.com/\*</code></li>
</ul>
<p>You can also control embed limitation programmatically using the Stream API. <code>uid</code> in the example below refers to the video id.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/{video_uid} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &quot;{\&quot;uid\&quot;: \&quot;&lt;VIDEO_UID&gt;\&quot;, \&quot;allowedOrigins\&quot;: [\&quot;example.com\&quot;]}&quot;&#10;</code></pre>
<p>You can also set allowed origins using the Stream binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/14330.md")
</div>
<h3 id="allowed-origins">Allowed Origins</h3>
<p>The Allowed Origins feature lets you specify which origins are allowed for playback. This feature works even if you are using your own video player. When using your own video player, Allowed Origins restricts which domain the HLS/DASH manifests and the video segments can be requested from.</p>
<h3 id="signed-urls">Signed URLs</h3>
<p>Combining signed URLs with embedding restrictions allows you to strongly control how your videos are viewed. This lets you serve only trusted users while preventing the signed URL from being hosted on an unknown site.</p>
