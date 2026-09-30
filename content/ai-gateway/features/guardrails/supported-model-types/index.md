<p>AI Gateway's Guardrails detects the type of AI model being used and applies safety checks accordingly:</p>
<ul>
<li><strong>Text generation models</strong>: Both prompts and responses are evaluated.</li>
<li><strong>Embedding models</strong>: Only the prompt is evaluated, as the response consists of numerical embeddings, which are not meaningful for moderation.</li>
<li><strong>Unknown models</strong>: If AI Gateway cannot determine the model type, it evaluates only the prompt and bypasses Guardrails for the response.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2892.md")
</aside>
