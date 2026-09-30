<p>The 1xx Informational status codes serve as interim responses that provide connection status updates without completing the request-response cycle. These codes are not intended for final actions but rather to indicate that the request is being processed or additional steps are required.</p>
<p>The requirements the server must follow when sending 1xx Informational status codes in response to a client's request include:</p>
<ul>
<li>Responses must be terminated by the first empty line following the status line.</li>
<li>1xx responses are not supported by HTTP/1.0; the origin server should never send a 1xx response to an HTTP/1.0 client.</li>
</ul>
<p>Cloudflare forwards all 1xx responses from origin servers but does not generate them directly.</p>
<h2 id="100-continue">100 Continue</h2>
<p>The 100 Continue status indicates that the server has received the request headers and is ready for the client to send the request body. For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>Allows clients to verify if the server will accept their request headers before sending a potentially large or unusable request body, optimizing data flow.</p>
<p>When a client includes the <code>Expect: 100-continue</code> header, it is requesting a confirmation before sending the request body, prompting the server to respond immediately with either <code>100 Continue</code> to proceed or an appropriate status code (for example, <code>401 Unauthorized</code> or <code>413 Payload Too Large</code>) if the request is unacceptable.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare uses Keep-Alive connections to maintain persistent communication between clients and servers, making the <code>100 Continue</code> response typically unnecessary, as Keep-Alive reduces overhead and eliminates the need for intermediate confirmations.</p>
<h2 id="101-switching-protocols">101 Switching Protocols</h2>
<p>The 101 Switching Protocols status code indicates that the origin server accepts the client's request to switch protocols. For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases-1">Common use cases</h3>
<p>The 101 Switching Protocols status code indicates that the server has accepted the client's request to change protocols, either by including an <code>Upgrade</code> header or through a change in the application protocol on the connection. When the <code>Upgrade</code> header is used, the server agrees to switch to a protocol higher on the client's priority list and responds with an <code>Upgrade</code> header to specify the new protocol(s). This change is assumed to benefit both the client and the server, with WebSockets being the most common use case.</p>
<h3 id="cloudflare-specific-information-1">Cloudflare-specific information</h3>
<p>Cloudflare supports WebSocket connections, which often involve the 101 Switching Protocols status code. The protocol switch allows clients to establish a WebSocket connection for real-time, bidirectional communication. For information about Cloudflare's Websockets, refer to <a href="https://blog.cloudflare.com/cloudflare-now-supports-websockets/">Cloudflare Now Supports Websockets</a>.</p>
<h2 id="102-processing">102 Processing</h2>
<p>102 Processing status code indicates that the server has received the request and is currently processing it, but the final response is not yet ready. This status code is only applicable to HTTP/1.1 and higher. For more information, refer to <a href="https://tools.ietf.org/html/rfc2518">RFC 2518</a>.</p>
<h3 id="common-use-cases-2">Common use cases</h3>
<p>The 102 Processing status code is commonly used in scenarios requiring long-running operations, such as complex database transactions or large file processing. It helps maintain the connection during extended processing times, typically exceeding 20 seconds, ensuring efficient communication between the client and server throughout the operation.</p>
<h3 id="cloudflare-specific-information-2">Cloudflare-specific information</h3>
<p>If Cloudflare receives a 102 Processing response, it expects a final response within 125 seconds. Failure to receive this response results in an <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">Error 522: Connection Timed Out</a>. However, sending interim 102 Processing responses can help prevent <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">Error 524: A timeout occurred</a>, ensuring that the connection remains active while the server processes the request.</p>
