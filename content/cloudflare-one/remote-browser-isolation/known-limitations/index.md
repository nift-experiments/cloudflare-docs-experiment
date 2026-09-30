---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/
  description: Reference information for Known limitations in Browser Isolation.
  full_title: Known limitations - Browser Isolation · Cloudflare One docs
  head_html: <title>Known limitations - Browser Isolation · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Known limitations in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/index.md"><meta property="og:title" content="Known limitations - Browser Isolation · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Known limitations in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/#page","headline":"Known limitations - Browser Isolation \u00b7 Cloudflare One docs","description":"Reference information for Known limitations in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/known-limitations/
  schema: 1
---
<p>Below, you will find information regarding the current limitations for Browser Isolation.</p>
<h2 id="website-compatibility">Website compatibility</h2>
<p>Our Network Vector Rendering (NVR) technology sends drawing instructions to the user's browser instead of streaming video of the page. This allows us to deliver a secure remote computing experience without the bandwidth limitations of video streams. While we expect most websites to work perfectly, some browser features and web technologies are unsupported and will be implemented in the future:</p>
<ul>
<li>Webcam and microphone support is unavailable.</li>
<li>Websites that use WebGL (a browser technology for rendering 3D graphics) may not function. To turn off WebGL in the browser, refer to <a href="/cloudflare-one/remote-browser-isolation/troubleshooting/#webgl-rendering-error">WebGL Rendering Error</a>.</li>
<li>Netflix and Spotify Web Player are unavailable.</li>
<li>H.265/HEVC (a video compression format) is not a supported video format at this time.</li>
</ul>
<h2 id="single-active-window">Single active window</h2>
<p>Browser Isolation supports one active window at a time. All tabs and windows in the same local browser (for example, all Chrome tabs) share a single isolated session. Within that session, the remote browser actively renders and processes only the tab or window currently in focus. Browser Isolation deactivates background tabs and windows until you switch to them.</p>
<p>This means that workflows requiring simultaneous activity across multiple windows are unavailable.</p>
<p>For example:</p>
<ul>
<li>Audio or video playing in one isolated window will pause when you switch to a different isolated window.</li>
<li>Real-time content (such as live dashboards or streaming media) will not update in background windows.</li>
<li>Applications that rely on multi-window communication or synchronization are not supported.</li>
</ul>
<h2 id="browser-compatibility">Browser compatibility</h2>
<table>
<thead>
<tr>
<th>Browser</th>
<th>Compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Chrome</td>
<td>✅</td>
</tr>
<tr>
<td>Mozilla Firefox</td>
<td>✅</td>
</tr>
<tr>
<td>Safari</td>
<td>✅</td>
</tr>
<tr>
<td>Microsoft Edge (Chromium-based)</td>
<td>✅</td>
</tr>
<tr>
<td>Other Chromium-based browsers (Opera, Brave)</td>
<td>✅</td>
</tr>
<tr>
<td>Internet Explorer 11 and below</td>
<td>❌</td>
</tr>
</tbody>
</table>
<h3 id="ios">iOS</h3>
<p>On iOS, Apple WebKit requires direct user interaction before the local browser can pass keyboard input into the remote browser. This means users should tap twice to begin entering text in an isolated session.</p>
<p>The first tap focuses the text field. The second tap starts text entry.</p>
<p>Browser Isolation shows an inline prompt over the focused text field when this interaction is required. If the text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the field instead.</p>
<h3 id="brave">Brave</h3>
<p>Browser Isolation uses <a href="/cloudflare-one/remote-browser-isolation/network-dependencies/#webrtc-channel">WebRTC</a> for low-latency communication between the local and remote browser. Brave's WebRTC IP Handling Policy can impact how Cloudflare RBI loads and functions. If the WebRTC IP Handling Policy is configured to <strong>Disable Non-Proxied UDP</strong>, RBI may fail to load correctly because Brave blocks the UDP connections that WebRTC requires.</p>
<p>To ensure RBI loads correctly, go to <code>brave://settings/privacy</code> in your Brave browser window, find <strong>WebRTC IP Handling Policy</strong>, and change the setting from <strong>Disable Non-Proxied UDP</strong> to one of the following:</p>
<ul>
<li><strong>Default</strong></li>
<li><strong>Default Public and Private Interfaces</strong></li>
<li><strong>Default Public Interface Only</strong></li>
</ul>
<h2 id="protocol-support">Protocol support</h2>
<p>Browser Isolation requires HTTPS. Websites served over unencrypted HTTP cannot be isolated.</p>
<h2 id="virtual-machines">Virtual machines</h2>
<p>Browser Isolation is not supported in virtualized environments (VMs).</p>
<h2 id="gateway-selectors">Gateway selectors</h2>
<p>Certain selectors for Gateway HTTP policies bypass Browser Isolation, including:</p>
<ul>
<li><a href="/cloudflare-one/traffic-policies/http-policies/#destination-continent">Destination Continent IP Geolocation</a></li>
<li><a href="/cloudflare-one/traffic-policies/http-policies/#destination-country">Destination Country IP Geolocation</a></li>
<li><a href="/cloudflare-one/traffic-policies/http-policies/#destination-ip">Destination IP</a></li>
</ul>
<p>You cannot use these selectors to isolate traffic and isolation matches for these selectors will not appear in your Gateway logs. Additionally, you cannot apply other policies based on these selectors while in isolation. For example, if you have a Block policy that matches traffic based on destination IP, Gateway will not block the matching traffic if it is already isolated by an Isolate policy.</p>
<h2 id="file-download-size">File download size</h2>
<p>When a user downloads a file within the remote browser, the file is held in memory and destroyed at the end of the remote browser session. Therefore, the total size of files downloaded per session is shared with the amount of memory available to the remote browser. We recommend a maximum individual file size of 512 MB.</p>
<h2 id="multifactor-authentication">Multifactor authentication</h2>
<p><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> does not support Yubikey or WebAuthN (hardware security key authentication). These authentication technologies require the isolated website to use the same domain name as the non-isolated website. Clientless Web Isolation changes the URL by adding a prefix, which breaks this requirement. Therefore, Yubikey and WebAuthN will not work with prefixed Clientless Web Isolation URLs but will work normally for <a href="/cloudflare-one/remote-browser-isolation/setup/">in-line deployments</a> such as <a href="/cloudflare-one/access-controls/policies/isolate-application/">isolated Access applications</a>.</p>
<h2 id="saml-applications">SAML applications</h2>
<p>Cloudflare Remote Browser Isolation now <a href="/cloudflare-one/changelog/browser-isolation/#2025-05-13">supports SAML applications that use HTTP-POST bindings</a>. SAML is a protocol used for single sign-on (SSO), and some SAML implementations send login data via an HTTP POST request (HTTP-POST bindings). This resolves previous issues such as <code>405</code> errors and login loops during SSO authentication flows.</p>
<p>You no longer need to isolate both the Identity Provider (IdP) and Service Provider (SP), or switch to HTTP-Redirect bindings, to use Browser Isolation with POST-based SSO. Users can log in to internal or SaaS applications in the isolated browser securely and seamlessly.</p>
<p><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> may still be preferred in some deployment models. Clientless Web Isolation implicitly isolates all traffic (both IdP and SP) and supports HTTP-POST SAML bindings.</p>
<h2 id="browser-isolation-is-not-compatible-with-private-apps-on-non-443-ports">Browser Isolation is not compatible with private apps on non-<code>443</code> ports</h2>
<p>Browser Isolation is not compatible with <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">self-hosted private applications</a> that use private IPs or hostnames on ports other than <code>443</code>. Trying to access self-hosted applications on non-<code>443</code> ports will result in a Gateway block page.</p>
<p>To use Browser Isolation for an application on a private IP address with a non-<code>443</code> port, configure a <a href="/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/">private network application</a> instead.</p>
