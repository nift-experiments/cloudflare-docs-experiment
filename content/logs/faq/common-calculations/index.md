<p><a href="/logs/faq/">❮ Back to FAQ</a></p>
<h3 id="how-can-i-calculate-bytes-served-by-the-origin-from-cloudflare-logs">How can I calculate bytes served by the origin from Cloudflare Logs?</h3>
<p>The best way to calculate bytes served by the origin is to use the <code>CacheResponseBytes</code> field in Cloudflare Logs, and to filter only requests that come from the origin. Make sure to filter out <code>OriginResponseStatus</code> values <code>0</code> and <code>304</code>, which indicate a revalidated response.</p>
<h3 id="how-do-i-calculate-bandwidth-usage-for-my-zone">How do I calculate bandwidth usage for my zone?</h3>
<p>Bandwidth (or data transfer) can be calculated by adding the <code>EdgeResponseBytes</code> field in HTTP request logs. There are some types of requests that are not factored into bandwidth calculations. In order to only include relevant requests in calculations, add the filter <code>ClientRequestSource = 'eyeball'</code>.</p>
