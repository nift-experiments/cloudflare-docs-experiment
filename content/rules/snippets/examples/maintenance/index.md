<p class="article-summary">Serve a custom maintenance page. Ideal for downtime notifications, planned maintenance, or emergency messages.</p>
<h2 id="snippet-code">Snippet code</h2>
<pre><code class="language-js">// Define your customizable inputs&#10;const statusCode = 503;&#10;const title = &quot;We&#x27;ll Be Right Back!&quot;;&#10;const message =&#10;	&quot;Our site is currently undergoing scheduled maintenance. We’re working hard to bring you a better experience. Thank you for your patience and understanding.&quot;;&#10;const estimatedTime = &quot;1 hour&quot;;&#10;const contactEmail = &quot;support@example.com&quot;;&#10;const contactPhone = &quot;+1 234 567 89&quot;;&#10;&#10;export default {&#10;	async fetch(request) {&#10;		// Serve the maintenance page as a response&#10;		return new Response(generateMaintenancePage(), {&#10;			status: statusCode,&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;text/html&quot;,&#10;				&quot;Retry-After&quot;: &quot;3600&quot;, // Suggest retry after 1 hour&#10;			},&#10;		});&#10;	},&#10;};&#10;&#10;function generateMaintenancePage() {&#10;	return `&#10;    &lt;!DOCTYPE html&gt;&#10;    &lt;html lang=&quot;en&quot;&gt;&#10;    &lt;head&gt;&#10;        &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;        &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;        &lt;title&gt;${title}&lt;/title&gt;&#10;        &lt;style&gt;&#10;            body {&#10;                margin: 0;&#10;                font-family: Arial, sans-serif;&#10;                display: flex;&#10;                align-items: center;&#10;                justify-content: center;&#10;                height: 100vh;&#10;                background-color: #f4f4f4;&#10;                color: #333;&#10;                text-align: center;&#10;            }&#10;            .container {&#10;                max-width: 600px;&#10;                padding: 20px;&#10;            }&#10;            h1 {&#10;                font-size: 2rem;&#10;                color: #0056b3;&#10;                margin-bottom: 10px;&#10;            }&#10;            p {&#10;                font-size: 1rem;&#10;                margin-bottom: 20px;&#10;                line-height: 1.5;&#10;            }&#10;            .contact {&#10;                margin-top: 20px;&#10;                font-size: 0.9rem;&#10;                color: #666;&#10;            }&#10;            .contact a {&#10;                color: #0056b3;&#10;                text-decoration: none;&#10;            }&#10;            .contact a:hover {&#10;                text-decoration: underline;&#10;            }&#10;            .logo {&#10;                margin: 20px 0;&#10;                max-width: 150px;&#10;            }&#10;            .timer {&#10;                font-weight: bold;&#10;                color: #e63946;&#10;            }&#10;        &lt;/style&gt;&#10;    &lt;/head&gt;&#10;    &lt;body&gt;&#10;        &lt;div class=&quot;container&quot;&gt;&#10;            &lt;h1&gt;${title}&lt;/h1&gt;&#10;            &lt;p&gt;${message}&lt;/p&gt;&#10;            &lt;p&gt;If all goes to plan, we&#x27;ll be back online in &lt;span class=&quot;timer&quot;&gt;${estimatedTime}&lt;/span&gt;. 🚀&lt;/p&gt;&#10;            &lt;p class=&quot;contact&quot;&gt;&#10;                Need help? Reach out to us at &lt;a href=&quot;mailto:${contactEmail}&quot;&gt;${contactEmail}&lt;/a&gt;&#10;                or call us at &lt;a href=&quot;tel:${contactPhone}&quot;&gt;${contactPhone}&lt;/a&gt;.&#10;            &lt;/p&gt;&#10;        &lt;/div&gt;&#10;    &lt;/body&gt;&#10;    &lt;/html&gt;&#10;    `;&#10;}&#10;</code></pre>
<h2 id="snippet-rule">Snippet rule</h2>
<p>Configure a custom filter expression:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Source Address</td>
<td>is not in list</td>
<td><code>admin_ips</code></td>
</tr>
</tbody>
</table>
<p>If you are using the Expression Editor, enter the following expression:</p>
<pre><code class="language-txt">(not ip.src in $admin_ips)&#10;</code></pre>
<p>The <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a> <code>admin_ips</code> was previously created and contains the list of IP addresses of the site administrators, which will be able to access the site during the maintenance period.</p>
