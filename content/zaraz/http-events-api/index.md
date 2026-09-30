<p>The Zaraz HTTP Events API allows you to send information to Zaraz from places that cannot run the <a href="/zaraz/web-api/">Web API</a>, such as your server or your mobile app. It is useful for tracking events that are happening outside the browser, like successful transactions, sign-ups and more. The API also allows sending multiple events in batches.</p>
<h2 id="configure-the-api-endpoint">Configure the API endpoint</h2>
<p>The API is disabled unless you configure an endpoint for it. The endpoint determines under what URL the API will be accessible. For example, if you set the endpoint to be <code>/zaraz/api</code>, and your domain is <code>example.com</code>, requests to the API will go to <code>https://example.com/zaraz/api</code>.</p>
<p>To enable the API endpoint:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Under **Endpoints** > **HTTP Events API**, set your desired path. Remember the path is relative to your domain, and it must start with a `/`.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/9.md")
</aside>
<h2 id="send-events">Send events</h2>
<p>The endpoint you have configured for the API will receive <code>POST</code> requests with a JSON payload. Below, there is an example payload:</p>
<pre><code class="language-json">{&#10;  &quot;events&quot;: [&#10;    {&#10;      &quot;client&quot;: {&#10;        &quot;__zarazTrack&quot;: &quot;transaction successful&quot;,&#10;        &quot;value&quot;: &quot;200&quot;&#10;      }&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>The payload must contain an <code>events</code> array. Each Event Object in this array corresponds to one event you want Zaraz to process. The above example is similar to calling <code>zaraz.track('transaction successful', { value: &quot;200&quot; })</code> using the Web API.</p>
<p>The Event Object holds the <code>client</code> object, in which you can pass information about the event itself. Every key you include in the Event Object will be available as a <em>Track Property</em> in the Zaraz dashboard.</p>
<p>There are two reserved keys:</p>
<ul>
<li><code>__zarazTrack</code>: The value of this key will be available as <em>Event Name</em>. This is what you will usually build your triggers around. In the above example, setting this to <code>transaction successful</code> is the same as <a href="/zaraz/web-api/track/">using the Web API</a> and calling <code>zaraz.track(&quot;transaction successful&quot;)</code>.</li>
<li><code>__zarazEcommerce</code>: This key needs to be set to <code>true</code> if you want Zaraz to process the event as an e-commerce event.</li>
</ul>
<h3 id="the-system-key">The <code>system</code> key</h3>
<p>In addition to the <code>client</code> key, you can use the <code>system</code> key to include information about the device from which the event originated. For example, you can submit the <code>User-Agent</code> string, the cookies and the screen resolution. Zaraz will use this information when connecting to different third-party tools. Since some tools depend on certain fields, it is often useful to include all the information you can.</p>
<p>The same payload from before will resemble the following example, when we add the <code>system</code> information:</p>
<pre><code class="language-json">{&#10;  &quot;events&quot;: [&#10;    {&#10;      &quot;client&quot;: {&#10;        &quot;__zarazTrack&quot;: &quot;transaction successful&quot;,&#10;        &quot;value&quot;: &quot;200&quot;&#10;      },&#10;      &quot;system&quot;: {&#10;        &quot;page&quot;: {&#10;          &quot;url&quot;: &quot;https://example.com&quot;,&#10;          &quot;title&quot;: &quot;My website&quot;&#10;        },&#10;        &quot;device&quot;: {&#10;          &quot;language&quot;: &quot;en-US&quot;,&#10;          &quot;ip&quot;: &quot;192.168.0.1&quot;&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>For all available system keys, refer to the table below:</p>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.cookies</code></td>
<td>Object</td>
<td>A key-value object holding cookies from the device associated with the event.</td>
</tr>
<tr>
<td><code>system.device.ip</code></td>
<td>String</td>
<td>The IP address of the device associated with the event.</td>
</tr>
<tr>
<td><code>system.device.resolution</code></td>
<td>String</td>
<td>The screen resolution of the device associated with the event, in a <code>WIDTHxHEIGHT</code> format.</td>
</tr>
<tr>
<td><code>system.device.viewport</code></td>
<td>String</td>
<td>The viewport of the device associated with the event, in a <code>WIDTHxHEIGHT</code> format.</td>
</tr>
<tr>
<td><code>system.device.language</code></td>
<td>String</td>
<td>The language code used by the device associated with the event.</td>
</tr>
<tr>
<td><code>system.device.user-agent</code></td>
<td>String</td>
<td>The <code>User-Agent</code> string of the device associated with the event.</td>
</tr>
<tr>
<td><code>system.page.title</code></td>
<td>String</td>
<td>The title of the page associated with the event.</td>
</tr>
<tr>
<td><code>system.page.url</code></td>
<td>String</td>
<td>The URL of the page associated with the event.</td>
</tr>
<tr>
<td><code>system.page.referrer</code></td>
<td>String</td>
<td>The URL of the referrer page in the time the event took place.</td>
</tr>
<tr>
<td><code>system.page.encoding</code></td>
<td>String</td>
<td>The encoding of the page associated with the event.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8.md")
</aside>
<h2 id="process-api-responses">Process API responses</h2>
<p>For each Event Object in your payload, Zaraz will respond with a Result Object. The Result Objects order matches the order of your Event Objects.</p>
<p>Depending on what tools you are loading using Zaraz, the body of the response coming from the API might include information you will want to process. This is because some tools do not have a complete server-side implementation and still depend on cookies, client-side JavaScript or similar mechanisms. Each Result Object can include the following information:</p>
<table>
<thead>
<tr>
<th>Result key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>fetch</code></td>
<td>Fetch requests that tools want to send from the user browser.</td>
</tr>
<tr>
<td><code>execute</code></td>
<td>JavaScript code that tools want to execute in the user browser.</td>
</tr>
<tr>
<td><code>return</code></td>
<td>Information that tools return.</td>
</tr>
<tr>
<td><code>cookies</code></td>
<td>Cookies that tools want to set for the user.</td>
</tr>
</tbody>
</table>
<p>You do not have to process the information above, but some tools might depend on this to work properly. You can start using the HTTP Events API without processing the information in the table above, and adjust accordingly later.</p>
