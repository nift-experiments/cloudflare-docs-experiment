---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/
  description: Understand 3xx redirection HTTP status codes.
  full_title: 3xx Redirection · Cloudflare Support docs
  head_html: <title>3xx Redirection · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand 3xx redirection HTTP status codes."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/index.md"><meta property="og:title" content="3xx Redirection · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand 3xx redirection HTTP status codes."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/#page","headline":"3xx Redirection \u00b7 Cloudflare Support docs","description":"Understand 3xx redirection HTTP status codes.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/3xx-redirection/
  schema: 1
---
<p>3xx codes are a class of responses which indicate that the HTTP client must take another course of action to obtain the complete requested resource.</p>
<p>The redirect location should be specified in one of the following ways:</p>
<ul>
<li>In the <code>Location</code> header field of the response, which is useful for automatic redirection.</li>
<li>In the payload of the response, optionally including a hyperlink to the correct location.</li>
</ul>
<h2 id="300-multiple-choices">300 Multiple Choices</h2>
<p>The 300 Multiple Choices status indicates that multiple options are available for the requested resource, and the client may select one.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>The status is typically used when a resource is available in multiple representations or formats. For instance:</p>
<ul>
<li>Offering multiple versions of a video in different formats (for example, MP4, AVI).</li>
<li>Providing a list of files with different <a href="https://en.wikipedia.org/wiki/File_extensions">extensions</a> or compression types.</li>
<li>Presenting <a href="https://en.wikipedia.org/wiki/Word_sense_disambiguation">word sense disambiguation</a> options for a term with multiple meanings.</li>
</ul>
<p>The response may include a <code>Location</code> header pointing to a preferred option or provide a payload with hyperlinks to the available choices, allowing the client to decide.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare generally bypasses the 300 Multiple Choices response for automated redirections to ensure optimal performance and user experience.</p>
<h2 id="301-moved-permanently">301 Moved Permanently</h2>
<p>The 301 Moved Permanently status indicates that the requested resource has been assigned a new permanent URI. All future references to this resource should use one of the enclosed URIs.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases-1">Common use cases</h3>
<p>This status is commonly used to inform clients that:</p>
<ul>
<li>A resource has been permanently relocated to a new URI.</li>
<li>Search engines should update their indexes to reflect the new URI.</li>
<li>Bookmarks or other saved references should be updated.</li>
</ul>
<p>The response typically includes a <code>Location</code> header specifying the new URI. This enables automatic redirection by most User-Agents.</p>
<h3 id="cloudflare-specific-information-1">Cloudflare-specific information</h3>
<p>Cloudflare can generate 301 Moved Permanently responses without needing to query the origin server. For more information, refer to <a href="/rules/url-forwarding/">Redirect Rules</a>.</p>
<h2 id="302-found">302 Found</h2>
<p>The 302 Found status, also referred to as a temporary redirect, indicates that the requested resource is temporarily located at a different URI. Unlike a 301 Moved Permanently status, which denotes a permanent relocation, the 302 Found status is specifically intended for temporary use.</p>
<p>While the User-Agent may follow the <code>Location</code> header to retrieve the resource, it should not replace the current URI as it would for a 301 Moved Permanently.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases-2">Common use cases</h3>
<p>This status is typically used to:</p>
<ul>
<li>Temporarily redirect traffic during maintenance or upgrades.</li>
<li>Direct users to an alternate resource without altering saved references.</li>
<li>A/B test different versions of a resource without making permanent changes.</li>
</ul>
<h3 id="cloudflare-specific-information-2">Cloudflare-specific information</h3>
<p>Cloudflare can generate these responses, eliminating the need to send a request to the origin serve. Learn more about how Cloudflare can help generate redirects with <a href="/rules/url-forwarding/">Redirect Rules</a>.</p>
<h2 id="303-see-other-since-http-1-1">303 See Other (since HTTP/1.1)</h2>
<p>The 303 See Other status indicates that the client should retrieve the resource at a different URI using a <code>GET</code> request. Unlike a 301 Moved Permanently redirect, the resource at the redirect location is not necessarily equivalent to the originally requested resource.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases-3">Common use cases</h3>
<p>The 303 status is typically used in response to a <code>POST</code> or <code>DELETE</code> request to indicate that the origin server has successfully processed the data and to support proper caching behavior.</p>
<p>Although the initial 303 response is not cacheable, the response to the subsequent <code>GET</code> request can be cached, as it is tied to a distinct URI.</p>
<h3 id="cloudflare-specific-information-3">Cloudflare-specific information</h3>
<p>Cloudflare allows for the configuration of 303 redirects through <a href="/rules/url-forwarding/">Redirect Rules</a>, enabling seamless handling of these responses directly at the edge. This approach improves performance by avoiding unnecessary requests to the origin server.</p>
<h2 id="304-not-modified">304 Not Modified</h2>
<p>The 304 Not Modified status indicates that the requested resource is available and valid in the client's cache. This means that the origin server has not modified the resource since the client's last request, allowing the client to use the cached resource without connecting to the origin server again. Requirements for caches receiving a 304 response are defined in <a href="https://tools.ietf.org/html/rfc7234#section-4.3.4">Section 4.3.4 of RFC 7234</a>.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>
<h3 id="common-use-cases-4">Common use cases</h3>
<p>A 304 Not Modified response is used when the client sends a conditional <code>GET</code> or <code>HEAD</code> request to validate a cached resource. The server confirms that the cached version is still up to date, allowing the client to use it without re-downloading the resource. This helps reduce unnecessary data transmission and improves efficiency.</p>
<p>A 304 response contains:</p>
<ul>
<li>No message body: The 304 response itself does not include the actual resource (like an image or webpage content). Instead, it just confirms that the cached version is valid.</li>
<li>Required headers: The response includes important metadata (such as <code>Cache-Control</code>, <code>Content-Location</code>, <code>Date</code>, <code>ETag</code>, <code>Expires</code>, or <code>Vary</code>) that tells the client how to manage the cached resource. These headers are the same ones that would accompany the resource if it were sent with a 200 OK response.</li>
</ul>
<h3 id="cloudflare-specific-information-4">Cloudflare-specific information</h3>
<p>When a stale request must be revalidated at the origin, Cloudflare sends a 304 response to confirm that the cached version matches the origin version. The response includes the <code>CF-Cache-Status: REVALIDATED</code> header, and Cloudflare validates the version using the <code>If-Modified-Since</code> header. For more information, refer to <a href="/cache/reference/etag-headers/">ETag Headers</a>.</p>
<h2 id="305-use-proxy-deprecated">305 Use Proxy (deprecated)</h2>
<p>This status code indicates that the request must be routed through the proxy specified in the <code>Location</code> header instead of being sent directly to the origin server. However, due to security concerns, the 305 Use Proxy status code has been deprecated.</p>
<h2 id="306-switch-proxy-deprecated">306 Switch Proxy (deprecated)</h2>
<p>This status code indicates that subsequent requests should be sent through the specified proxy. However, the 306 Switch Proxy status code is deprecated and is no longer in use.</p>
<h2 id="307-temporary-redirect">307 Temporary Redirect</h2>
<p>The 307 Temporary Redirect status indicates that a requested resource has been temporarily moved to a different URI, as specified in the <code>Location</code> header. Unlike a 302 redirect, the original request method (for example, <code>GET</code> or <code>POST</code>) must remain unchanged when the redirect is followed automatically. This ensures that temporary changes to a resource's location do not disrupt the intended behavior of the request. User agents may automatically follow the redirect using the <code>Location</code> header, but should not replace the original URI for future requests.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases-5">Common use cases</h3>
<p>The 307 status is useful for temporarily relocating resources during server maintenance or upgrades while ensuring the original request method is preserved. It is also commonly used to direct traffic to temporary URLs for promotions, campaigns, or special events without altering the original URI for future requests.</p>
<h3 id="cloudflare-specific-information-5">Cloudflare-specific information</h3>
<p>Cloudflare can handle 307 Temporary Redirect responses efficiently, enabling temporary redirects without requiring changes at the origin server. This can be configured using <a href="/rules/url-forwarding/">Redirect Rules</a>.</p>
<h2 id="308-permanent-redirect">308 Permanent Redirect</h2>
<p>The 308 Permanent Redirect status indicates that the requested resource has been permanently moved to a new URI, as specified in the <code>Location</code> header. Unlike a 301 redirect, the original request method (for example, <code>GET</code>, <code>POST</code>) must remain unchanged when automatically following the redirect. User agents should follow the redirect using the <code>Location</code> header and replace the original URI with the new one for subsequent requests.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7538#section-3">RFC 7538</a>.</p>
<h3 id="common-use-cases-6">Common use cases</h3>
<p>The 308 Permanent Redirect status is commonly used for permanent resource relocation, API version upgrades, domain or path migrations, and maintaining method integrity in redirects. Additionally, it helps with SEO by transferring link equity to the new URI.</p>
<h3 id="cloudflare-specific-information-6">Cloudflare-specific information</h3>
<p>Cloudflare can handle 308 Permanent Redirects efficiently, ensuring redirection while maintaining request integrity. These redirects can be configured using <a href="/rules/url-forwarding/">Redirect Rules</a>.</p>
