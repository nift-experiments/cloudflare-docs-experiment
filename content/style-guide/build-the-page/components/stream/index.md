<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { Stream } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<div class="video-frame"><img class="video-poster" src="https://pub-d9bf66e086fb4b639107aa52105b49dd.r2.dev/Connect-and-secure-from-any-network-to-anywhere.jpg" alt="Connect and secure from any network to anywhere"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/86f22d1f760b77cdc349f89b25b63c3e/iframe?preload=true&amp;letterboxColor=transparent" title="Connect and secure from any network to anywhere" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com//iframe?preload=true&amp;letterboxColor=transparent" title="Cloudflare Stream video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<pre><code class="language-mdx">&lt;Stream&#10;	id=&quot;86f22d1f760b77cdc349f89b25b63c3e&quot;&#10;	title=&quot;Connect and secure from any network to anywhere&quot;&#10;	thumbnail=&quot;https://pub-d9bf66e086fb4b639107aa52105b49dd.r2.dev/Connect-and-secure-from-any-network-to-anywhere.jpg&quot;&#10;	chapters={{&#10;		&quot;Chapter 1&quot;: &quot;30s&quot;,&#10;		&quot;Chapter 2&quot;: &quot;1m30s&quot;,&#10;		&quot;Chapter 3&quot;: &quot;3m15s&quot;,&#10;		&quot;Chapter 4&quot;: &quot;3m25s&quot;,&#10;		&quot;Chapter 5&quot;: &quot;3m35s&quot;,&#10;	}}&#10;/&gt;&#10;&#10;&lt;Stream file=&quot;warp-1-basics&quot; /&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;Stream&gt;</code> Props</h2>
<h3 id="id"><code>id</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>string</code></p>
<p>The ID of the Stream video.</p>
<h3 id="title"><code>title</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>string</code></p>
<p>The title of the Stream video.</p>
<h3 id="thumbnail"><code>thumbnail</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>Either a timestamp (i.e <code>2.5s</code> or <code>1m35s</code>) or a URL to an image.</p>
<h3 id="chapters"><code>chapters</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, string&gt;</code></p>
<p>Optional chapters displayed as cards below the video.</p>
<h3 id="expandchapters"><code>expandChapters</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p><strong>default:</strong> <code>false</code></p>
<p>If <code>chapters</code> is present, is passed through to the <code>open</code> property of the <a href="/style-guide/build-the-page/components/details/">Details component</a>.</p>
<h3 id="showmorevideos"><code>showMoreVideos</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p><strong>default:</strong> <code>true</code></p>
<p>Whether to show the &quot;Watch more videos on our Developer Channel&quot; link below the video.</p>
<h3 id="file"><code>file</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>If <code>file</code> is provided, the <code>id</code>, <code>title</code>,<code> thumbnail</code> and <code>chapters</code> properties cannot be used and are instead retrieved from the YAML file in the <a href="https://github.com/cloudflare/cloudflare-docs/tree/production/src/content/stream"><code>stream</code></a> collection.</p>
