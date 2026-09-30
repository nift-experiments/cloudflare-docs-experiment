<p class="article-summary">Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.</p>
<h2 id="snippet-code">Snippet code</h2>
<pre><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Define delay&#10;		const delay_in_seconds = 5;&#10;		// Introduce a delay&#10;		await new Promise((resolve) =&gt;&#10;			setTimeout(resolve, delay_in_seconds * 1000),&#10;		); // Set delay in milliseconds&#10;&#10;		// Pass the request to the origin&#10;		const response = await fetch(request);&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
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
<td>Bot Score</td>
<td>less than</td>
<td><code>10</code></td>
</tr>
</tbody>
</table>
<p>If you are using the Expression Editor, enter the following expression:</p>
<pre><code class="language-txt">(cf.bot_management.score lt 10)&#10;</code></pre>
