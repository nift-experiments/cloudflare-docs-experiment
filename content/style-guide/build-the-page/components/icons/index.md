<p>There are two icon components which pull from two different icon sets.</p>
<h2 id="icon">Icon</h2>
<p>The <code>Icon</code> component from Nimbus is available as a standalone component.</p>
<p>Primarily, this is used for Cloudflare product icons which are stored in <code>/src/icons/*.svg</code>.</p>
<pre><code class="language-mdx">import { Icon } from &quot;~/components&quot;;&#10;&#10;&lt;Icon name=&quot;workers&quot; class=&quot;text-5xl text-orange-400&quot; /&gt;&#10;</code></pre>
<h2 id="card-and-linkcard">Card and LinkCard</h2>
<p>Components like <code>Card</code> and <code>LinkCard</code> accept a plain <code>icon</code> string prop — any <a href="https://icon-sets.iconify.design/">iconify</a> icon name.</p>
<pre><code class="language-mdx">import { Card, LinkCard } from &quot;~/components&quot;;&#10;&#10;&lt;Card title=&quot;Example&quot; icon=&quot;ph:rocket-launch&quot; /&gt;&#10;&lt;LinkCard title=&quot;Example&quot; href=&quot;/workers/&quot; icon=&quot;ph:rocket-launch&quot; /&gt;&#10;</code></pre>
<p>Content authored before the Nimbus migration may still use Starlight-style icon names (for example <code>icon=&quot;seti:shell&quot;</code>). These are automatically mapped to an equivalent iconify icon at build time. New content should use iconify names directly.</p>
<h2 id="icon-library">Icon library</h2>
<p>Optionally, you can choose a corresponding icon from Starlight’s <a href="https://starlight.astro.build/reference/icons/#all-icons">Icons</a> for cards or tabs.</p>
