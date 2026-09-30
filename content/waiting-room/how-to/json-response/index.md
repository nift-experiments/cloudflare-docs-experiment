<p>If you need to manage traffic in a non-browser environment such as a mobile app or web app, Cloudflare provides a JSON-friendly waiting room that can be consumed via your API endpoints:</p>
<ol>
<li>When a user is queued, we return our own JSON response.</li>
<li>When a user leaves the waiting room, we forward the request to your origin server and return the response from your origin server (be it JSON, XML, an HTML page, etc.).</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15745.md")
</aside>
<p>In order to consume the waiting room response in the JSON format, take the following steps:</p>
<h2 id="step-1-enable-json-response">Step 1 – Enable JSON response</h2>
<p>To receive a JSON response, you first need to enable that option in your waiting room.</p>
<ul>
<li><strong>Via the dashboard</strong>: When <a href="/waiting-room/how-to/customize-waiting-room/">customizing a waiting room</a>, enable <strong>JSON Response</strong>.</li>
<li><strong>Via the API</strong>: When <a href="/api/resources/waiting_rooms/methods/create/">creating a waiting room</a>, set <code>json_response_enabled</code> to true.</li>
</ul>
<h2 id="step-2-get-json-data">Step 2 – Get JSON data</h2>
<p>Make a request to your waiting room endpoint with the header <code>Accept: application/json</code>. Note that the header has to match exactly <code>Accept: application/json</code>. If it is anything else or has any additional content such as <code>Accept: application/json, text/html</code> the response will not return in the JSON format. You must retry the request every <code>refreshIntervalSeconds</code> in order for users to advance in the queue.</p>
<pre><code class="language-bash">curl &quot;https://example.com/waitingroom&quot; \&#10;&#45;-header &quot;Accept: application/json&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;cfWaitingRoom&quot;: {&#10;		&quot;inWaitingRoom&quot;: true,&#10;		&quot;waitTime&quot;: 5,&#10;		&quot;waitTimeKnown&quot;: true,&#10;		&quot;waitTimeFormatted&quot;: &quot;5 minutes&quot;,&#10;		&quot;queueIsFull&quot;: false,&#10;		&quot;queueAll&quot;: false,&#10;		&quot;lastUpdated&quot;: &quot;2021-08-03T23:46:00.000Z&quot;,&#10;		&quot;refreshIntervalSeconds&quot;: 20&#10;	}&#10;}&#10;</code></pre>
<h2 id="cookies-in-the-request-header">Cookies in the request header</h2>
<p>Waiting Room is driven by a waiting room cookie that determines the position of the user in the queue. Because of this, the cookie is updated in the response headers for each request. For each request to an endpoint protected by Waiting Room, the application must include the up-to-date cookie retrieved during the previous request. This is mandatory regardless of a user having been queued or not. If a request does not include a cookie, the waiting room will assume this is a new user and will return a new cookie in the response header. Consequently, this will place the user at the end of the queue. Thus, when consuming the waiting room in a non-browser environment it is important to include the waiting room cookie in the request header and keep it updated after each request.</p>
<p>Refer to the <a href="/waiting-room/reference/waiting-room-cookie/">Waiting Room cookies</a>, for more information.</p>
<h2 id="advancing-in-the-queue">Advancing in the queue</h2>
<p>In a browser environment, the page automatically refreshes every <code>refreshIntervalSeconds</code> to ensure that the user advances in the queue. In a non-browser environment, where the Waiting Room JSON-friendly API is being consumed, it is expected that your backend service (or API) also refreshes/makes a request to the Waiting Room configured endpoint every <code>refreshIntervalSeconds</code> to ensure the advancing of the user in the queue.</p>
<p>These are some of the places where the JSON-friendly response can be consumed (this list is not exhaustive):</p>
<ol>
<li>
<p>In a mobile app traffic</p>
<ul>
<li><strong>Integrate Waiting Room variables</strong> – Create a new template in your mobile app to receive the JSON response. For a full list of these variables, refer to the <code>json_response_enabled</code> parameter in the <a href="/api/resources/waiting_rooms/methods/create/">Cloudflare API docs</a>.</li>
<li><strong>Allow cookies</strong> – As mentioned above, a waiting room <a href="/waiting-room/reference/waiting-room-cookie/">requires cookies</a>, and your mobile app will need to support cookies. For ease of use, consider using a cookie manager like <a href="https://pkg.go.dev/net/http#CookieJar">CookieJar</a>.</li>
<li><strong>Consume JSON data</strong> - Make a request to the Waiting Room endpoint with the <code>Accept: application/json</code> header.</li>
</ul>
</li>
<li>
<p>Inside Cloudflare Workers (or in your own backend service)</p>
<ul>
<li>
<p><strong>Integrate Waiting Room variables</strong> – Expect a JSON response in your backend API. For a full list of these variables, refer to the <code>json_response_enabled</code> parameter in the <a href="/api/resources/waiting_rooms/methods/create/">Cloudflare API docs</a>.</p>
</li>
<li>
<p><strong>Include cookies in the request header</strong> – As mentioned above, a waiting room <a href="/waiting-room/reference/waiting-room-cookie/">requires cookies</a>, and your backend API will need to support cookies. For ease of use, consider using a cookie manager like <a href="https://pkg.go.dev/net/http#CookieJar">CookieJar</a>.</p>
</li>
<li>
<p><strong>Enable JSON response</strong> - Via the dashboard or via the API.</p>
</li>
<li>
<p><strong>Consume JSON data</strong> - Make a request to the Waiting Room endpoint with the <code>Accept: application/json</code> header.</p>
<p>Here is an example, demonstrating the usage of the waiting room endpoint inside a Worker. The request headers include the necessary <code>accept</code> and <code>cookie</code> header values that are required by the Waiting Room API. The accept header ensures that a JSON-friendly response is returned, if a user is queued. Otherwise, if the request is sent to the origin, then whatever the response origin returns gets returned back. In this example, a hardcoded <code>__cfwaitingroom</code> value is embedded in the cookie field. In a real-life application, however, we expect that a cookie returned by the Waiting Room API is used in each of the subsequent requests to ensure that the user is placed accordingly in the queue and let through to the origin when it is the users turn.</p>
</li>
</ul>
</li>
</ol>
<pre><code class="language-javascript">const waitingroomSite = &quot;https://examples.cloudflareworkers.com/waiting-room&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		const init = {&#10;			headers: {&#10;				accept: &quot;application/json&quot;,&#10;				cookie: &quot;__cfwaitingroom=F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgV&quot;,&#10;			},&#10;		};&#10;&#10;		return fetch(waitingroomSite, init)&#10;			.then((response) =&gt; response.json())&#10;			.then((response) =&gt; {&#10;				if (response.cfWaitingRoom.inWaitingRoom) {&#10;					return Response(&quot;in waiting room&quot;, { &quot;content-type&quot;: &quot;text/html&quot; });&#10;				}&#10;				return new Response(response);&#10;			});&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15744.md")
</aside>
