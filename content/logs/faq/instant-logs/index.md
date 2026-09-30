<p><a href="/logs/faq/">❮ Back to FAQ</a></p>
<h3 id="i-am-getting-an-http-301-when-attempting-to-connect-to-my-websocket-what-can-i-do">I am getting an HTTP 301 when attempting to connect to my WebSocket. What can I do?</h3>
<p>Make sure you are using the <code>wss://</code> protocol when connecting to your WebSocket.</p>
<h3 id="i-am-getting-an-http-429-what-can-i-do">I am getting an HTTP 429. What can I do?</h3>
<p>Connection requests are rate limited. Try your request again after waiting a few minutes.</p>
<h3 id="why-am-i-not-receiving-data">Why am I not receiving data?</h3>
<p>First, double-check if you have a filter defined. If you do, it may be too strict (or incorrect) which ends up dropping all your data.</p>
<p>If you are confident in your filter, check the sample rate you used when creating the session. For example, a sample of 100 means you will receive one log for every 100 requests to your zone.</p>
<p>Finally, make sure the destination is proxied through Cloudflare (also known as orange clouded). We cannot log your request if it does not go through Cloudflare's global network.</p>
<h3 id="i-am-getting-an-error-fetching-my-data-how-can-i-solve-this">I am getting an error fetching my data. How can I solve this?</h3>
<p>Make sure you have the correct permissions. To use Instant Logs you need Super Administrator, Administrator, Log Share, or Log Share Reader permissions.</p>
