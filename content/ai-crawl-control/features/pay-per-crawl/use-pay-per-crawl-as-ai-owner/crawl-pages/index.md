<pre><code class="language-mermaid">graph LR&#10;A[Set up your&lt;br&gt;Cloudflare Account] --&gt; B[Verify your&lt;br&gt;AI crawler]&#10;B --&gt; C[Discover&lt;br&gt;payable content]&#10;C --&gt; D[Connect to&lt;br&gt;Stripe]&#10;D --&gt; E[Crawl pages]:::highlight&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>Once your AI crawler complies with Web Bot Auth, you can begin to crawl webpages. For more information on how pay per crawl works, refer to <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">What is Pay Per Crawl?</a></p>
<h2 id="1-identify-payment-requirements"><ol>
<li>Identify payment requirements</li>
</ol></h2>
<p>When an AI crawler makes a request to a page protected by pay per crawl, the server will respond with <code>HTTP/2 402 Payment Required</code>. This response will also include the <code>crawler-price</code> header which specifies the cost to access the content. For example, a response may look like the following:</p>
<pre><code class="language-txt">HTTP/2 402&#10;date: Fri, 06 Jun 2025 08:42:38 GMT&#10;crawler-price: USD 0.01&#10;</code></pre>
<p>To access this content, the AI crawler must provide headers for paid access.</p>
<h2 id="2-access-paid-content"><ol start="2">
<li>Access paid content</li>
</ol></h2>
<h3 id="2-1-include-payment-headers">2.1. Include payment headers</h3>
<p>Your AI crawler can specify the price it is willing to pay by providing one of two headers:</p>
<ul>
<li><code>crawler-exact-price</code>: This is the exact price the AI crawler is configured to pay for access. This value should exactly match the price set in the response header <code>crawler-price</code>. Include this header in your second request if your AI crawler first received a HTTP status code 402, and you wish to access the content by paying the <code>crawler-price</code>.</li>
<li><code>crawler-max-price</code>: This is the maximum price the AI crawler is configured to pay for access on any content. Use this option if you wish to access any pay per crawl content with a crawl price equal or lower than the maximum price. If a page's <code>crawler-price</code> is higher than your <code>crawler-max-price</code>, your AI crawler will receive a HTTP 402 response.</li>
</ul>
<h3 id="2-2-sign-your-request-with-web-bot-auth">2.2. Sign your request with Web Bot Auth</h3>
<p>Include Web Bot Auth headers by following the steps in <a href="/bots/reference/bot-verification/web-bot-auth/#4-after-verification-sign-your-requests">Sign your requests</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/2772.md")
</aside>
<h3 id="2-3-review-response-headers">2.3. Review response headers</h3>
<p>When you specify a header to indicate payment, you may receive one of two responses:</p>
<h4 id="successful-http-200-response">Successful HTTP 200 response</h4>
<p>The value of the <code>crawler-charged</code> header indicates the exact amount that will be billed to your Cloudflare account for the request.</p>
<pre><code class="language-txt">HTTP 200&#10;date: Fri, 06 Jun 2025 08:42:38 GMT&#10;crawler-charged: USD 0.01&#10;</code></pre>
<h4 id="unsuccessful-response">Unsuccessful response</h4>
<p>If the request is unsuccessful, you will receive an error response with a <code>crawler-error</code> header indicating the specific issue.</p>
<pre><code class="language-txt">HTTP/2 402&#10;date: Fri, 06 Jun 2025 08:42:38 GMT&#10;content-type: text/plain; charset=utf-8&#10;crawler-price: USD 0.01&#10;crawler-error: InvalidCrawlerExactPrice&#10;</code></pre>
<p>Refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">Pay Per Crawl error codes</a> for a complete list of error codes and troubleshooting guidance.</p>
<h2 id="3-track-your-spending"><ol start="3">
<li>Track your spending</li>
</ol></h2>
<p>When you successfully access pay per crawl content (response with HTTP status code 200), the response will include <code>crawler-charged</code>. For example:</p>
<pre><code>crawler-charged: USD 0.01&#10;</code></pre>
<p>Cloudflare strongly recommends tracking and saving these values to keep an accurate record of the bill your AI crawler has accrued.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>You may wish to refer to the following resources.</p>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a></li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">Pay Per Crawl error codes</a></li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/faq/">Pay Per Crawl FAQs</a></li>
</ul>
