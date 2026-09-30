<p>Our docs have a few conventions around files.</p>
<h2 id="naming">Naming</h2>
<p>When creating new files, follow specific conventions for your naming.</p>
<p>Filenames should:</p>
<ul>
<li>Semantically communicate the purpose of the file</li>
<li>Be lowercased</li>
<li>Use dashes between words</li>
</ul>
<pre><code class="language-txt">/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx&#10;//assets/upstream/images/api-shield/api-shield-call-sequence.png&#10;</code></pre>
<pre><code class="language-txt">/src/content/docs/fundamentals/concepts/What is Cloudflare.mdx&#10;/src/content/docs/fundamentals/concepts/What-is-Cloudflare.mdx&#10;//assets/upstream/images/api-shield/API_Image_1.png&#10;</code></pre>
<p>These conventions are important for user readability, SEO conventions, and making sure our GitHub actions do not break.</p>
<h2 id="folders">Folders</h2>
<p>Each folder should have a file named <code>index.mdx</code>.</p>
<pre><code class="language-txt">/src/content/docs/fundamentals/concepts/index.mdx&#10;</code></pre>
<p>The content at <code>/src/content/docs/fundamentals/concepts/index.mdx</code> will be rendered at <code>https://developers.cloudflare.com/fundamentals/concepts/</code>.</p>
<h2 id="content-files">Content files</h2>
<p>Add regular content files to the <code>/src/content/docs/{product_folder}/</code> directory.</p>
<pre><code class="language-txt">/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx&#10;</code></pre>
<h2 id="image-files">Image files</h2>
<p>Add image files to the <code>//assets/upstream/images/{product_folder}/</code> directory.</p>
<pre><code class="language-txt">//assets/upstream/images/api-shield/api-shield-call-sequence.png&#10;</code></pre>
