<p>Use the this component to add extra information to an existing glossary entry. <code>term</code> defines which glossary entry you want to prepend information to, while <code>prepend=</code> adds the extra info.</p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { GlossaryDefinition } from &quot;~/components&quot;&#10;&#10;&lt;GlossaryDefinition term=&quot;example&quot; prepend=&quot;The definition for example is: &quot; /&gt;&#10;</code></pre>
<h2 id="glossary">Glossary</h2>
<pre><code class="language-yaml">productName: Style Guide&#10;entries:&#10;  - term: example&#10;    general_definition: |-&#10;      Hello, world! You can use **Markdown** features inside of your `tooltips`.&#10;</code></pre>
