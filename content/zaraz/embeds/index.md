<p>Embeds are tools for incorporating external content, like social media posts, directly onto webpages, enhancing user engagement without compromising site performance and security.</p>
<p>Cloudflare Zaraz introduces server-side rendering for embeds, avoiding third-party JavaScript to improve security, privacy, and page speed. This method processes content on the server side, removing the need for direct communication between the user's browser and third-party servers.</p>
<p>To add an Embed to Your Website:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag Setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration**.
3. Click "add new tool" and activate the desired tools on your Cloudflare Zaraz dashboard.
4. Add a placeholder in your HTML, specifying the necessary attributes. For a generic embed, the snippet looks like this:
<pre><code class="language-html">&lt;componentName-embedName attribute=&quot;value&quot;&gt;&lt;/componentName-embedName&gt;&#10;</code></pre>
<p>Replace <code>componentName</code>, <code>embedName</code> and <code>attribute=&quot;value&quot;</code> with the specific Managed Component requirements. Zaraz automatically detects placeholders and replaces them with the content in a secure and efficient way.</p>
<h2 id="examples">Examples</h2>
<h3 id="x-twitter-embed">X (Twitter) embed</h3>
<pre><code class="language-html">&lt;twitter-post tweet-id=&quot;12345&quot;&gt;&lt;/twitter-post&gt;&#10;</code></pre>
<p>Replace <code>tweet-id</code> with the actual tweet ID for the content you wish to embed.</p>
<h3 id="instagram-embed">Instagram embed</h3>
<pre><code class="language-html">&lt;instagram-post post-url=&quot;https://www.instagram.com/p/ABC/&quot; captions=&quot;true&quot;&gt;&lt;/instagram-post&gt;&#10;</code></pre>
<p>Replace <code>post-url</code> with the actual URL for the content you wish to embed. To include posts captions set captions attribute to <code>true</code>.</p>
