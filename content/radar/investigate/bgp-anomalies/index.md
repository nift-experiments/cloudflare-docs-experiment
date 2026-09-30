<p>To access Cloudflare Radar BGP Anomaly Detection results, you will first need to create an API token that includes a <code>Account:Radar</code> permission. All the following examples should work with a free-tier Cloudflare account.</p>
<h2 id="search-bgp-hijack-events">Search BGP hijack events</h2>
<p>In the following example, we will query the <a href="/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list/">BGP hijack events API</a> for the most recent BGP origin hijacks originated by or affecting <code>AS64512</code> (example ASN).</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/bgp/hijacks/events?invlovedAsn=64512&amp;format=json&amp;per_page=10&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>The result shows the most recent 10 BGP hijack events that affects <code>AS64512</code>.</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;asn_info&quot;: [&#10;      {&#10;        &quot;asn&quot;: 64512,&#10;        &quot;org_name&quot;: &quot;XXXXX&quot;,&#10;        &quot;country_code&quot;: &quot;XX&quot;&#10;      },&#10;      ...&#10;    ],&#10;    &quot;events&quot;: [&#10;      {&#10;        &quot;duration&quot;: 0,&#10;        &quot;event_type&quot;: 0,&#10;        &quot;hijack_msgs_count&quot;: 1,&#10;        &quot;hijacker_asn&quot;: 64512,&#10;        &quot;id&quot;: 1234,&#10;        &quot;is_stale&quot;: false,&#10;        &quot;max_hijack_ts&quot;: &quot;2023-04-27T14:01:55.952&quot;,&#10;        &quot;max_msg_ts&quot;: &quot;2023-04-27T14:01:55.952&quot;,&#10;        &quot;min_hijack_ts&quot;: &quot;2023-04-27T14:01:55.952&quot;,&#10;        &quot;on_going_count&quot;: 1,&#10;        &quot;peer_asns&quot;: [&#10;          8455&#10;        ],&#10;        &quot;peer_ip_count&quot;: 1,&#10;        &quot;prefixes&quot;: [&#10;          &quot;192.0.2.0/24&quot;&#10;        ],&#10;        &quot;tags&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;irr_new_origin_invalid&quot;,&#10;            &quot;score&quot;: 4&#10;          },&#10;          {&#10;            &quot;name&quot;: &quot;irr_old_origin_valid&quot;,&#10;            &quot;score&quot;: 0&#10;          },&#10;          ...&#10;        ],&#10;        &quot;victim_asns&quot;: [&#10;          64513&#10;        ],&#10;        &quot;confidence_score&quot;: 4&#10;      },&#10;    ],&#10;    &quot;total_monitors&quot;: 163&#10;  },&#10;  ...&#10;}&#10;</code></pre>
<p>In the response we can learn about the following information about each event:</p>
<ul>
<li><code>hijack_msg_count</code>: the number of potential BGP hijack messages observed from all peers.</li>
<li><code>peer_asns</code>: the AS numbers of the route collector peers who observed the hijack messages.</li>
<li><code>prefixes</code>: the affected prefixes.</li>
<li><code>hijacker_asn</code> and <code>victim_asns</code>: the potential hijacker ASN and victim ASNs.</li>
<li><code>confidence_score</code>: a quantitative score describing how confident the system is for this event being a hijack:
<ul>
<li>1-3: low confidence.</li>
<li>4-7: medium confidence.</li>
<li>8-above: high confidence.</li>
</ul>
</li>
<li><code>tags</code>: the evidence collected for the events. Each <code>tag</code> is also associated with a score that affects the overall confidence score:
<ul>
<li>a positive score indicates that the event is <em>more likely</em> to be a hijack.</li>
<li>a negative score indicates that the event is <em>less likely</em> to be a hijack.</li>
</ul>
</li>
</ul>
<p>Users can further filter out low-confidence events by attaching a <code>minConfidence=8</code> parameter, which will return only events with a <code>confidence_score</code> of <code>8</code> or higher.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/bgp/hijacks/events?invlovedAsn=64512&amp;format=json&amp;per_page=10&amp;minConfidence=8&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="search-bgp-route-leak-events">Search BGP route leak events</h2>
<p>BGP route leak is another type of BGP anomalies that Cloudflare Radar detects. Currently, we focus on detecting specifically
the <code>provider-customer-provider</code> type of route leak. You can learn more about our design and methodology in <a href="https://blog.cloudflare.com/route-leak-detection-with-cloudflare-radar/">our blog post</a>.</p>
<p>In the following example, we will query the <a href="/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list/">BGP route leak events API</a> for the most recent BGP route leak events affecting <code>AS64512</code>.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/bgp/leaks/events?invlovedAsn=64512&amp;format=json&amp;per_page=10&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>The result shows the most recent 10 BGP route leak events that affects <code>AS64512</code>.</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;asn_info&quot;: [&#10;      {&#10;        &quot;asn&quot;: 64512,&#10;        &quot;org_name&quot;: &quot;XXXXXXX&quot;,&#10;        &quot;country_code&quot;: &quot;XX&quot;&#10;      },&#10;      ...&#10;    ],&#10;    &quot;events&quot;: [&#10;      {&#10;        &quot;detected_ts&quot;: &quot;2023-04-21T23:10:06&quot;,&#10;        &quot;finished&quot;: false,&#10;        &quot;id&quot;: 1234,&#10;        &quot;leak_asn&quot;: 64512,&#10;        &quot;leak_count&quot;: 14,&#10;        &quot;leak_seg&quot;: [&#10;          64514,&#10;          64512,&#10;          64513&#10;        ],&#10;        &quot;leak_type&quot;: 1,&#10;        &quot;max_ts&quot;: &quot;2023-04-21T23:10:56&quot;,&#10;        &quot;min_ts&quot;: &quot;2023-04-21T23:09:46&quot;,&#10;        &quot;origin_count&quot;: 1,&#10;        &quot;peer_count&quot;: 13,&#10;        &quot;prefix_count&quot;: 1&#10;      },&#10;      ...&#10;    ]&#10;  },&#10;  ...&#10;}&#10;</code></pre>
<p>In the response we can learn about the following information about each event:</p>
<ul>
<li><code>leak_asn</code>: the AS who potentially caused the leak.</li>
<li><code>leak_seg</code>: the AS path segment observed and believed to be a leak.</li>
<li><code>min_ts</code> and <code>max_ts</code>: the earliest and latest timestamps of the leak announcements.</li>
<li><code>leak_count</code>: the total number of BGP route leak announcements observed.</li>
<li><code>peer_count</code>: the number of route collector peers observed the leak.</li>
<li><code>prefix_count</code> and <code>origin_count</code>: the number of prefixes and origin ASes affected by the leak.</li>
</ul>
<h2 id="send-alerts-for-bgp-hijacks">Send alerts for BGP hijacks</h2>
<p>In this example, we will show you how you can build a Cloudflare Workers app that sends out alerts for BGP hijacks relevant to a given ASN using webhooks (works for Google Hangouts, Discord, Telegram, etc) or email.</p>
<p>We will use Cloudflare Workers as the platform and use its Cron Triggers to periodically check for new alerts.</p>
<p>For the app, we would like it to do the following things:</p>
<ul>
<li>Fetch from Cloudflare API with a given API token.</li>
<li>Check against Cloudflare KV to know what events are new.</li>
<li>Construct messages for new hijacks and send out alerts via webhook triggers.</li>
</ul>
<h3 id="worker-app-setup">Worker app setup</h3>
<p>We will start with setting up a Cloudflare Worker app.</p>
<p>First, create a new Workers app in a local directory:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- hijack-alerts</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- hijack-alerts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare hijack-alerts</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare hijack-alerts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest hijack-alerts</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest hijack-alerts" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>To start developing your Worker, <code>cd</code> into your new project directory:</p>
<pre><code class="language-sh">cd hijack-alerts&#10;</code></pre>
<p>In your Wrangler file, change the default checking frequency (once per hour) to what you like. Here is an example
of configuring the workers to run the script five minutes.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11557.md")
</div>
<p>In this example, we will also need to use Cloudflare KV to save the latest checked event IDs which allows us to know what events are new. Once you have created a KV, you can head back to the <code>wrangler.jsonc</code> file and add the following sections:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11558.md")
</div>
<h3 id="fetch-for-newly-detected-bgp-hijacks">Fetch for newly detected BGP hijacks</h3>
<p>Start with the API fetching function.</p>
<p>The following <code>apiFetch(env, paramsStr)</code> handles taking in a request parameters string, construct proper headers and
fetch from the Cloudflare API BGP hijacks endpoint.</p>
<pre><code class="language-javascript">async function apiFetch(env, paramsStr) {&#10;	const config = {&#10;		headers: {&#10;			Authorization: `Bearer ${env.CF_API_TOKEN}`,&#10;		},&#10;	};&#10;	const res = await fetch(&#10;		`https://api.cloudflare.com/client/v4/radar/bgp/hijacks/events?${paramsStr}`,&#10;		config,&#10;	);&#10;&#10;	if (!res.ok) {&#10;		console.log(JSON.stringify(res));&#10;		return null;&#10;	}&#10;	return await res.json();&#10;}&#10;</code></pre>
<p>The <code>env</code> parameter is passed in from the caller, and we do not need to worry about construct it. The <code>paramsStr</code> is a
string variable that holds the query parameters in a query URL.</p>
<p>Now in our main cron trigger function, we will need to construct the query parameters and call the API fetch function.
The default cron trigger worker script is defined as the follows:</p>
<pre><code class="language-javascript">&#10;export default {&#10;    async scheduled(controller, env, ctx) {&#10;    ...&#10;    }&#10;}&#10;</code></pre>
<p>In our example, we use the <code>env</code> variables to get the runtime variables like the TOKEN and ASN of interest, and Cloudflare
KV bindings. We do not use the <code>controller</code> and <code>ctx</code> variables in this example.</p>
<p>First, we will need to learn about what are the new events. We define new events as the events the app has not yet processed.
We use the Cloudflare KV bucket previously created and defined (<code>HIJACKS_KV</code>) to save and retrieve the most recent
processed event ID.</p>
<pre><code class="language-javascript">let kv_latest_id = parseInt(await env.HIJACKS_KV.get(&quot;latest_id&quot;));&#10;const first_batch = isNaN(kv_latest_id);&#10;</code></pre>
<p>The main loop that checks for the most recent events looks like this (some of the validation code is skipped):</p>
<pre><code class="language-javascript">let new_events = [];&#10;let page = 1;&#10;while (true) {&#10;	// query for events&#10;	const query_params = `per_page=10&amp;page=${page}&amp;involvedAsn=${env.TARGET_ASN}&amp;sortBy=ID&amp;sortOrder=DESC`;&#10;	const data = await apiFetch(env, query_params);&#10;&#10;	// first batch, save KV value only&#10;	if (first_batch) {&#10;		await env.HIJACKS_KV.put(&quot;latest_id&quot;, events[0].id.toString());&#10;		return;&#10;	}&#10;&#10;	// some validation skipped&#10;	// ...&#10;&#10;	let reached_last = false;&#10;	for (const event of data.result.events) {&#10;		if (event.id &lt;= kv_latest_id) {&#10;			// reached the latest events&#10;			reached_last = true;&#10;			break;&#10;		}&#10;		new_events.push(event);&#10;	}&#10;	if (reached_last) {&#10;		break;&#10;	}&#10;	page += 1;&#10;}&#10;</code></pre>
<p>Now that we have all the newly detected events saved in <code>new_events</code> variable, we can then send out alerts:</p>
<pre><code class="language-javascript">// sort events by increasing ID order&#10;new_events.sort((a, b) =&gt; a.id - b.id);&#10;const kv_latest_id = new_events[new_events.length - 1].id;&#10;// push new events&#10;for (const event of new_events) {&#10;	await send_alert(env, event);&#10;}&#10;// update latest_id KV value&#10;await env.HIJACKS_KV.put(&quot;latest_id&quot;, kv_latest_id.toString());&#10;</code></pre>
<h3 id="send-alerts-using-webhook">Send alerts using webhook</h3>
<p>The function <code>send_alert</code> handles constructing alert message and sending out alerts using webhook. Here we demonstrate
an example plain-text message template using Google Hangouts webhook. Users can customize the message and the use of webhook based on their
platform of choice and needs.</p>
<pre><code class="language-javascript">async function send_hangout_alert(env, event) {&#10;	const webhook_url = `${env.WEBHOOK_URL}&amp;threadKey=bgp-hijacks-event-${event.id}`;&#10;&#10;	const data = JSON.stringify({&#10;		text: `Detected BGP hijack event (${event.id}):&#10;Detected time: *${event.min_hijack_ts} UTC*&#10;Detected ASN: *${event.hijacker_asn}*&#10;Expected ASN(s): *${event.victim_asns.join(&quot; &quot;)}*&#10;Prefixes: *${event.prefixes.join(&quot; &quot;)}*&#10;Tags: *${event.tags.map((tag) =&gt; tag.name).join(&quot; &quot;)}*&#10;Peer Count: *${event.peer_ip_count}*&#10;`,&#10;	});&#10;	await fetch(webhook_url, {&#10;		method: &quot;POST&quot;,&#10;		headers: {&#10;			&quot;Content-Type&quot;: &quot;application/json; charset=UTF-8&quot;,&#10;		},&#10;		body: data,&#10;	});&#10;}&#10;</code></pre>
<p>Note that the webhook is considered secret and should be set to the environment via <code>wrangler secret put WEBHOOK_URL</code> command.</p>
<p>The last step is to deploy the application with command <code>npx wrangler deploy</code> and the app should be up and running on your Cloudflare account, and will be triggered to execute every five minutes.</p>
<h3 id="send-email-alerts-from-workers">Send email alerts from Workers</h3>
<p>If you have <a href="/email-service/">Email Routing</a> enabled for your domain, you can also send email alerts directly from Workers. Refer to <a href="/email-service/api/send-emails/workers-api/">Send emails from Workers</a> to learn more.</p>
<p>For this alert to work, you will need to configure the proper email bindings in the <a href="/workers/wrangler/configuration/#email-bindings">Wrangler configuration file</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11559.md")
</div>
<p>Then, you can create an email-sending function to send alert emails to your configured destination address:</p>
<pre><code class="language-javascript">async function send_email_alert(hijacker, prefixes, victims) {&#10;	const msg = createMimeMessage();&#10;	msg.setSender({&#10;		name: &quot;BGP Hijack Alerter&quot;,&#10;		addr: &quot;&lt;YOUR_APP&gt;@&lt;YOUR_APP_DOMAIN&gt;&quot;,&#10;	});&#10;	msg.setRecipient(&quot;&lt;YOUR_EMAIL&gt;@example.com&quot;);&#10;	msg.setSubject(&quot;BGP hijack alert&quot;);&#10;	msg.addMessage({&#10;		contentType: &quot;text/plain&quot;,&#10;		data: `BGP hijack detected:&#10;    Detected origin: ${hijacker}&#10;    Expected origins: ${victims.join(&quot; &quot;)}&#10;    Prefixes: ${prefixes.join(&quot; &quot;)}&#10;    `,&#10;	});&#10;&#10;	var message = new EmailMessage(&#10;		&quot;&lt;YOUR_APP&gt;@&lt;YOUR_APP_DOMAIN&gt;&quot;,&#10;		&quot;&lt;YOUR_EMAIL&gt;@example.com&quot;,&#10;		msg.asRaw(),&#10;	);&#10;	try {&#10;		await env.SEND_EMAIL_BINDING.send(message);&#10;	} catch (e) {&#10;		return new Response(e.message);&#10;	}&#10;}&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Refer to our API documentation for <a href="/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list/">BGP route leaks</a> and <a href="/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list/">BGP hijacks</a> for more information on these topics.</p>
