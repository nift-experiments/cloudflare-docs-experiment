<p>This guide will show you how to manage miscategorization of reports. To complete this guide, you will need to generate an <a href="/fundamentals/api/get-started/create-token/">API token</a>.</p>
<ol>
<li>Create an <a href="/fundamentals/api/get-started/create-token/">API token</a> if you do not have one already.</li>
<li>Choose <strong>Custom Token</strong>.</li>
<li>Name the token, and grant permissions.</li>
<li>Send a <code>POST</code> request to the miscategorization <a href="https://developers.cloudflare.com/api/resources/intel/subresources/miscategorizations/methods/create/">API endpoint</a>. You can find an example below:</li>
</ol>
<pre><code class="language-json">&#10;export URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/intel/miscategorization&quot;&#10;curl -X POST &quot;$URL&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type:application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;content_adds&quot;: [&#10;  ],&#10;  &quot;content_removes&quot;: [&#10;  ],&#10;  &quot;indicator_type&quot;: &quot;domain&quot;,&#10;  &quot;ip&quot;: null,&#10;  &quot;security_adds&quot;: [&#10;    115&#10;  ],&#10;  &quot;security_removes&quot;: [&#10;  ],&#10;  &quot;url&quot;: &quot;cloudflare.com&quot;&#10;}&#x27;&#10;</code></pre>
<p>You should receive a response with the value <code>&quot;success&quot;: true</code>:</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: &quot;&quot;,&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Once you send the request, the Cloudflare Support team will receive it and will be able to take action.</p>
