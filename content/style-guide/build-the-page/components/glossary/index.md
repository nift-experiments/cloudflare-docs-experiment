<p>Use the glossary definition shortcode to render the defined glossary definition. Additionally, you can include a <a href="/style-guide/build-the-page/components/glossary-definition/">prepend value</a> to add words to the start of the definition.</p>
<p>Create the glossary entries in a file dedicated to your product. These YAML files live in <code>/src/content/glossary/&lt;YOUR-PRODUCT&gt;.yaml</code></p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { Glossary } from &quot;~/components&quot;&#10;&#10;&lt;Glossary /&gt;&#10;</code></pre>
<h2 id="glossary">Glossary</h2>
<pre><code class="language-yaml">productName: Style Guide&#10;entries:&#10;  - term: example&#10;    general_definition: |-&#10;      Hello, world! You can use **Markdown** features inside of your `tooltips`.&#10;</code></pre>
