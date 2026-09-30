<h2 id="type">Type</h2>
<pre><code class="language-mdx">import { Type } from &quot;~/components&quot;;&#10;&#10;&lt;Type text=&quot;Promise&lt;T | string | ArrayBuffer&gt;&quot; /&gt;&#10;</code></pre>
<h2 id="metainfo">MetaInfo</h2>
<pre><code class="language-mdx">import { MetaInfo } from &quot;~/components&quot;;&#10;&#10;&lt;MetaInfo text=&quot;(default: false) optional&quot; /&gt;&#10;</code></pre>
<h2 id="combined-example">Combined example</h2>
<pre><code class="language-mdx">import { Type, MetaInfo } from &quot;~/components&quot;;&#10;&#10;&#45; `name` &lt;Type text=&quot;string&quot; /&gt;&#10;  &#45; The name of your service.&#10;&#45; `local` &lt;Type text=&quot;boolean&quot; /&gt; &lt;MetaInfo text=&quot;(default: true) optional&quot; /&gt;&#10;  &#45; If the service should run locally or not.&#10;</code></pre>
