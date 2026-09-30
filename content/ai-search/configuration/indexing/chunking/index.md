<p>Chunking is the process of splitting large data into smaller segments before embedding them for search. AI Search uses <strong>recursive chunking</strong>, which breaks your content at natural boundaries (like paragraphs or sentences), and then further splits it if the chunks are too large.</p>
<h2 id="what-is-recursive-chunking">What is recursive chunking</h2>
<p>Recursive chunking tries to keep chunks meaningful by:</p>
<ul>
<li><strong>Splitting at natural boundaries:</strong> like paragraphs, then sentences.</li>
<li><strong>Checking the size:</strong> if a chunk is too long (based on token count), it’s split again into smaller parts.</li>
</ul>
<p>This way, chunks are easy to embed and retrieve, without cutting off thoughts mid-sentence.</p>
<h2 id="chunking-controls">Chunking controls</h2>
<p>AI Search exposes two parameters to help you control chunking behavior:</p>
<ul>
<li><strong>Chunk size</strong>: The number of tokens per chunk. The option range may vary depending on the model.</li>
<li><strong>Chunk overlap</strong>: The percentage of overlapping tokens between adjacent chunks.
<ul>
<li>Minimum: <code>0%</code></li>
<li>Maximum: <code>30%</code></li>
</ul>
</li>
</ul>
<p>These settings apply during the indexing step, before your data is embedded and stored in your search index.</p>
<h2 id="choosing-chunk-size-and-overlap">Choosing chunk size and overlap</h2>
<p>Chunking affects both how your content is retrieved and how much context is passed into the generation model. Try out this external <a href="https://huggingface.co/spaces/m-ric/chunk_visualizer">chunk visualizer tool</a> to help understand how different chunk settings could look.</p>
<h3 id="additional-considerations">Additional considerations:</h3>
<ul>
<li><strong>Index size:</strong> Smaller chunk sizes produce more chunks and more total vectors. Refer to the <a href="/ai-search/platform/limits-pricing/">AI Search limits</a> to ensure your configuration stays within instance limits.</li>
<li><strong>Generation model context window:</strong> Generation models have a limited context window that must fit all retrieved chunks (<code>max_num_results</code> × <code>chunk size</code>), the user query, and the model's output. Be careful with large chunks or high <code>max_num_results</code> values to avoid context overflows.</li>
<li><strong>Cost and performance:</strong> Larger chunks and higher <code>max_num_results</code> settings result in more tokens passed to the model, which can increase latency and cost. You can monitor this usage in <a href="/ai-gateway/">AI Gateway</a>.</li>
</ul>
