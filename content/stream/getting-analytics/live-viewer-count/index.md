<p>The Stream player has full support for live viewer counts by default. To get the viewer count for live videos for use with third party players, make a <code>GET</code> request to the <code>/views</code> endpoint.</p>
<pre><code class="language-bash">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID&gt;/views&#10;</code></pre>
<p>Below is a response for a live video with several active viewers:</p>
<pre><code class="language-json">{ &quot;liveViewers&quot;: 113 }&#10;</code></pre>
