<p>2xx status codes indicate success, meaning that the client's request was received, understood, and accepted by the server.</p>
<h2 id="200-ok">200 OK</h2>
<p>A 200 response indicates that the request has succeeded.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>A 200 response is commonly used in the following scenarios:</p>
<ul>
<li>GET requests: Returns requested resources such as webpages, images, or API data, along with relevant headers.</li>
<li>HEAD requests: Retrieves only headers corresponding to the requested resource, such as metadata. For example, file size or last modified date.</li>
<li>POST requests: Confirms successful processing of submitted data, such as form submissions, often with details about the result in the response body.</li>
</ul>
<p>A 200 response should ideally include a payload but is not required. Occasionally, an origin server may return a 200 response with zero content length. However, following RFC standards, a 204 response is recommended in such cases (except for the CONNECT method).</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>By default, 200 responses are cacheable by proxy servers and browsers. If specific <a href="/cache/concepts/customize-cache/">cache controls</a> are not defined, <a href="/cache/concepts/default-cache-behavior/">static resources</a> with a 200 response are cached for two hours at Cloudflare's edge.</p>
<h2 id="201-created">201 Created</h2>
<p>A 201 response indicates the successful creation of one or more new resources. The server typically includes the location of the newly created resource in either the <code>Location</code> header or the request URI.</p>
<h3 id="common-use-cases-1">Common use cases</h3>
<p>Creating a new resource in response to a POST request. For example, creating a new user, article, or record.</p>
<h3 id="cloudflare-specific-information-1">Cloudflare-specific information</h3>
<p>Cloudflare forwards 201 responses without modification.</p>
<p>For further information, refer to <a href="https://tools.ietf.org/html/rfc7231#section-7.2">RFC 7231</a> for more details about validator headers, like <strong>ETag</strong> and <strong>Last-Modified</strong> in a 201 response.</p>
<h2 id="203-non-authoritative-information">203 Non-authoritative information</h2>
<p>A 203 response indicates that the request was successful, but the response did not come directly from the origin server. The response was instead delivered by a proxy or intermediate server.</p>
<h3 id="common-use-cases-2">Common use cases</h3>
<p>Servers use this response to tell a client that the resource was cached by a proxy server.</p>
<h3 id="cloudflare-specific-information-2">Cloudflare-specific information</h3>
<p>Cloudflare does not cache 203 responses. For details about how Cloudflare handles 203 responses, refer to <a href="/fundamentals/reference/http-headers/">Cloudflare HTTP headers</a>.</p>
<h2 id="204-no-content">204 No content</h2>
<p>A 204 response indicates that the request was successfully processed, but there is no content to return in the response.</p>
<h3 id="common-use-cases-3">Common use cases</h3>
<p>This response is often used by servers to indicate that a document editor's save action to the origin server was completed successfully.</p>
<h3 id="cloudflare-specific-information-3">Cloudflare-specific information</h3>
<p>204 responses never contain payloads, as specified by the HTTP standard, and Cloudflare does not cache these responses.</p>
<h2 id="205-reset-content">205 Reset content</h2>
<p>A 205 response tells the client to return to its previous state after a request.</p>
<h3 id="common-use-cases-4">Common use cases</h3>
<p>This response occurs after a user submits a form or other data and they want to tell the client to refresh the page or allow a new submission.</p>
<h3 id="cloudflare-specific-information-4">Cloudflare-specific information</h3>
<p>205 responses must not contain any payloads and Cloudflare does not cache these responses.</p>
<h2 id="206-partial-content">206 Partial content</h2>
<p>A 206 response means that the request was partially successful, often used for serving large files in smaller chunks.</p>
<h3 id="common-use-cases-5">Common use cases</h3>
<p>This response is often used to decrease latency when clients are processing larger files that might require split or interrupted downloads. For instance, for streaming video or serving file ranges for progressive loading.</p>
<p>A 206 response includes either:</p>
<ul>
<li>Partial payload that contains a <code>Content-Range</code> header specifying the requested range and the data provided in the response.</li>
<li>Multipart payload that omits the <code>Content-Range</code> header at the top level but includes <code>Content-Type</code> and <code>Content-Range</code> headers for each part of the multipart response body.</li>
</ul>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7233#page-10">Section 4.1 of RFC 7233</a>.</p>
<h3 id="cloudflare-specific-information-5">Cloudflare-specific information</h3>
<p>Cloudflare handles 206 responses for range requests, but <a href="/cache/concepts/default-cache-behavior/">caching behavior</a> may vary depending on the file type and origin settings.</p>
