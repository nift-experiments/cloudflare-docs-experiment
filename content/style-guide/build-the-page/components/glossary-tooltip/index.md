<p>Use this component to add tooltips to words in your markdown files. The info for the tooltips is pulled in from the glossary yaml file.</p>
<p><code>term</code> specifies which glossary entry you want to pull information from.
The text between the opening and closing components is the word or words that you want to define with the glossary entry.</p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { GlossaryTooltip } from &quot;~/components&quot;&#10;&#10;&lt;GlossaryTooltip term=&quot;example&quot;&gt;Hover over me!&lt;/GlossaryTooltip&gt;&#10;</code></pre>
<h2 id="glossary">Glossary</h2>
<pre><code class="language-yaml">productName: Style Guide&#10;entries:&#10;  - term: example&#10;    general_definition: |-&#10;      Hello, world! You can use **Markdown** features inside of your `tooltips`.&#10;</code></pre>
