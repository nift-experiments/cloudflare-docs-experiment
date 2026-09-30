<p>Learn how Cloudflare analytics tracks requests made by <a href="/workers/">Cloudflare Workers</a>.</p>
<h2 id="what-is-a-subrequest">What is a subrequest</h2>
<p>With a no-op Worker (a Worker that simply proxies traffic by passing on the original client request to the origin and proxying the response) running on a particular route, the request to the origin is counted as a 'subrequest', separate from initial client to edge request. Thus, unless the Worker responds with a static response and never hits an origin, the eyeball → edge request, and edge → origin request will each be counted separately towards the request or bandwidth count in Analytics. Subrequests are not included in the <strong>Requests</strong> or <strong>Bandwidth</strong> graphs of the Cloudflare <strong>Analytics</strong> app.</p>
<hr />
<h2 id="zone-analytics">Zone analytics</h2>
<p>In the dashboard, the numbers in zone analytics reflect visitor traffic. That is, the number of requests shown in zone analytics (under the Analytics tabs in the dashboard) is the number of requests that were served to the client.</p>
<p>Similarly, the bandwidth is counted based on the bandwidth that is sent to the client, and status codes reflect the status codes that were served back to the client (so if a subrequest received a 500, but you respond with a 200, a 200 will be shown in the status codes breakdown).</p>
<hr />
<h2 id="worker-analytics">Worker analytics</h2>
<p>For a breakdown of subrequest traffic (origin facing traffic), you may go to the Cloudflare <strong>Analytics</strong> app and select the <strong>Workers</strong> tab. Under the <strong>Workers</strong> tab, below the Service Workers panel, are a <strong>Subrequests</strong> breakdown by count, <strong>Bandwidth</strong> and <strong>Status Codes</strong>. This will help you spot and debug errors at your origin (such as spikes in 500s), and identify your cache-hit ratio to help you understand traffic going to your origin.</p>
<hr />
<h2 id="faq">FAQ</h2>
<p><strong>Why do I not have any analytics for Workers?</strong></p>
<ul>
<li>If you are not currently using Workers (do not have Workers deployed on any routes or filters), we will not have any information to show you.</li>
<li>If your Worker sends a static response back to the client without ever calling fetch() to an origin, you are not making any subrequests, thus, all traffic will be shown in zone Analytics</li>
</ul>
<p><strong>Will this impact billing?</strong> </p>
<p>No, <a href="/workers/platform/pricing/">billing for Workers</a> is based on requests that go through a Worker. </p>
<p><strong>Why am I seeing such a high cache hit ratio?</strong></p>
<p>Requests served by a Worker always show as cached. For an accurate cache hit ratio on subrequests, refer to the <strong>Subrequests</strong> graph in the <strong>Analytics</strong> app under the <strong>Workers</strong> analytics tab.</p>
