<p>One of the fields you can add to the <a href="/style-guide/build-the-page/frontmatter/">Frontmatter</a> is <code>banner</code>. It displays a prominent section at the top of the page and supports the use of HTML for links and formatting.</p>
<p>Only use it to alert about disruptive situations and take note to remove it when applicable.</p>
<h2 id="example">Example</h2>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Do &lt;strong&gt;not&lt;/strong&gt; use banners in the &lt;a href=&quot;/style-guide/build-the-page/frontmatter/&quot;&gt;Frontmatter&lt;/a&gt; unless a change will cause customer application to break.&#10;&#45;--&#10;</code></pre>
<h2 id="styles-types">Styles / Types</h2>
<h3 id="note">Note</h3>
<p>The note banner is used to alert about important information.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Ensure you read this!&#10;  type: note&#10;&#45;--&#10;</code></pre>
<h3 id="tip">Tip</h3>
<p>The tip banner is used to alert about important suggestions.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Consider this alternative!&#10;  type: tip&#10;&#45;--&#10;</code></pre>
<h3 id="caution">Caution</h3>
<p>The caution banner is used to warn readers of upcoming disruptive changes.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: This is deprecated and will break on &lt;strong&gt;1970-01-01&lt;/strong&gt;!&#10;  type: caution&#10;&#45;--&#10;</code></pre>
<h3 id="danger">Danger</h3>
<p>The danger banner is used to alert about errors.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: This has been removed!&#10;  type: danger&#10;&#45;--&#10;</code></pre>
<h3 id="default">Default</h3>
<p>The default banner is used in all other circumstances.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Do &lt;strong&gt;not&lt;/strong&gt; use banners in the &lt;a href=&quot;/style-guide/build-the-page/frontmatter/&quot;&gt;Frontmatter&lt;/a&gt; unless a change will cause customer application to break.&#10;&#45;--&#10;</code></pre>
