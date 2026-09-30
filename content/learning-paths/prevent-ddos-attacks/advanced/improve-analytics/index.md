<p>Cloudflare provides analytics for <a href="/waf/analytics/security-events/">security events</a>, <a href="/analytics/account-and-zone-analytics/zone-analytics/">traffic patterns</a>, and more according to the level of your zone's plan.</p>
<p>To augment these default analytics and gather more information about potential DDoS attacks, explore the following options.</p>
<h2 id="restore-visitor-ip-addresses">Restore visitor IP addresses</h2>
<p>When traffic <a href="/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/">proxied through Cloudflare</a> reaches your origin server, it will come from Cloudflare's IP addresses.</p>
<p>If needed, you can <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">restore the original visitor's IP address</a> so you can have that information in your server logs.</p>
<h2 id="cloudflare-logs">Cloudflare Logs</h2>
<p>Enterprise customers can set up <a href="/logs/logpush/">Logpush</a> jobs to regularly send Cloudflare logs to the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/9854.md")
</div> of their choice.
<p>This data can help when looking at long-term DDoS attack trends or when you need custom visualizations.</p>
<h2 id="bot-management">Bot Management</h2>
<p>For more detailed analytics about potential bot attacks, Enterprise customers can also purchase <a href="/bots/get-started/bot-management/">Bot Management</a>.</p>
<p>For a full tour of Bot Analytics, see <a href="https://blog.cloudflare.com/introducing-bot-analytics/">our blog post</a>. At a high level, the tool includes:</p>
<ul>
<li><strong>Requests by bot score</strong>: View your total domain traffic and segment it vertically by traffic type. Keep an eye on <em>automated</em> and <em>likely automated</em> traffic.</li>
<li><strong>Bot score distribution</strong>: View the number of requests assigned a bot score 1 through 99.</li>
<li><strong>Bot score source</strong>: Identify the most common detection engines used to score your traffic. Hover over a tooltip to learn more about each engine.</li>
<li><strong>Top requests by attribute</strong>: View more detailed information on specific IP addresses and other characteristics.</li>
</ul>
<p>Bot Analytics shows up to one week of data at a time and can display data up to 30 days old. Bot Analytics displays data in real time in most cases.</p>
