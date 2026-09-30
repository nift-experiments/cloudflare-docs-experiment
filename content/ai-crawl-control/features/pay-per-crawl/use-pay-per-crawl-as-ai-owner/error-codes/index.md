<p>Pay per crawl error responses include a <code>crawler-error</code> header with a specific error code. The following table provides a complete reference of all possible error codes:</p>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>HTTP Status</th>
<th>What to do</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CrawlerForbidden</code></td>
<td>403</td>
<td>The site owner has blocked your crawler. You cannot access this content.</td>
</tr>
<tr>
<td><code>StrongAuthRequired</code></td>
<td>400</td>
<td>Include valid Web Bot Auth headers with strong authentication in your request.</td>
</tr>
<tr>
<td><code>InvalidSignature</code></td>
<td>400</td>
<td>Include both <code>signature-input</code> and <code>signature</code> headers in your request. Refer to <a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth documentation</a>.</td>
</tr>
<tr>
<td><code>InvalidCrawlerPriceValue</code></td>
<td>400</td>
<td>Check that your <code>crawler-exact-price</code> or <code>crawler-max-price</code> header value is properly formatted (for example, <code>USD 0.01</code>).</td>
</tr>
<tr>
<td><code>MissingCrawlerPrice</code></td>
<td>402</td>
<td>Include either <code>crawler-exact-price</code> or <code>crawler-max-price</code> header in your request.</td>
</tr>
<tr>
<td><code>PaymentFailed</code></td>
<td>403</td>
<td>Verify your payment processing is configured correctly in Pay Per Crawl settings. Contact Cloudflare support if the issue persists.</td>
</tr>
<tr>
<td><code>InvalidCrawlerExactPrice</code></td>
<td>402</td>
<td>Update your <code>crawler-exact-price</code> to match the <code>crawler-price</code> value from the response header.</td>
</tr>
<tr>
<td><code>InvalidCrawlerMaxPrice</code></td>
<td>402</td>
<td>Increase your <code>crawler-max-price</code> to meet or exceed the <code>crawler-price</code> value from the response header.</td>
</tr>
<tr>
<td><code>ConflictingPriceHeaders</code></td>
<td>400</td>
<td>Use only one price header per request. Remove either <code>crawler-max-price</code> or <code>crawler-exact-price</code>.</td>
</tr>
<tr>
<td><code>InvalidContentPrice</code></td>
<td>502</td>
<td>The origin returned an invalid price. This is a site owner configuration issue. Try again later or contact the site owner.</td>
</tr>
<tr>
<td><code>InternalError</code></td>
<td>500</td>
<td>A server error occurred. Retry your request with exponential backoff.</td>
</tr>
</tbody>
</table>
