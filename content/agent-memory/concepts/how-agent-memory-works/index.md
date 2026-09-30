<p>Agent Memory is a managed service that gives your applications persistent, AI-powered memory. It automatically turns raw conversations into structured knowledge and retrieves the right context when you need it.</p>
<h2 id="memory-types">Memory types</h2>
<p>Agent Memory classifies every extracted memory into one of four types:</p>
<ul>
<li><strong>Facts</strong> — Stable knowledge about a person, project, or tool. Preferences, identities, relationships, and goals. Facts evolve over time through supersession: when a newer fact replaces an older one on the same topic, the old version is preserved but the latest surfaces in recall results.</li>
<li><strong>Events</strong> — Completed actions anchored to a point in time. Deployments, decisions, milestones, and observations. Events accumulate and do not conflict with each other.</li>
<li><strong>Instructions</strong> — Reusable procedures, workflows, and conventions. Like facts, instructions support supersession when updated.</li>
<li><strong>Tasks</strong> — Short-lived, session-scoped items such as active investigations and follow-ups. Tasks are deprioritized after the session ends.</li>
</ul>
<h2 id="how-ingestion-works">How ingestion works</h2>
<p>When you call <code>ingest()</code>, Agent Memory processes the conversation through several stages:</p>
<ol>
<li>
<p><strong>Extraction</strong> — AI reads the conversation and identifies discrete, memorable items. Each item is a standalone piece of knowledge with a clear summary and supporting content.</p>
</li>
<li>
<p><strong>Classification</strong> — Each extracted item is classified into a memory type (fact, event, instruction, or task) and assigned a topic key, keywords, and search queries for later retrieval.</p>
</li>
<li>
<p><strong>Deduplication</strong> — The system checks for duplicates against both the current batch and existing stored memories. Facts and instructions with the same topic key supersede older versions rather than creating duplicates.</p>
</li>
<li>
<p><strong>Storage</strong> — Memories are written to durable storage with full-text search indexes. Non-task memories are also embedded as vectors for semantic search.</p>
</li>
</ol>
<p>Raw conversation messages are always stored verbatim alongside extracted memories, preserving the original transcript for full-text search.</p>
<h2 id="how-recall-works">How recall works</h2>
<p>When you call <code>recall()</code>, Agent Memory runs multiple retrieval strategies in parallel:</p>
<ol>
<li>
<p><strong>Query analysis</strong> — AI analyzes your query to determine the best retrieval approach, generating keyword terms, topic keys, and semantic search vectors.</p>
</li>
<li>
<p><strong>Parallel retrieval</strong> — The system simultaneously searches across keyword indexes, topic key lookups, semantic vector indexes, and raw conversation messages.</p>
</li>
<li>
<p><strong>Scoring and ranking</strong> — Results from all sources are combined and ranked to surface the most relevant memories while maintaining diversity across retrieval methods.</p>
</li>
<li>
<p><strong>Synthesis</strong> — AI generates a natural language answer from the top-ranked memories, grounded in the actual stored content.</p>
</li>
</ol>
<p>If no memories match the query, <code>recall()</code> returns an empty answer rather than hallucinating a response.</p>
<h2 id="idempotency-and-deduplication">Idempotency and deduplication</h2>
<p>Agent Memory is designed for safe re-ingestion:</p>
<ul>
<li>
<p><strong>Messages are content-addressed.</strong> Each message gets a deterministic ID derived from its content and session. Sending the same message twice does not create a duplicate.</p>
</li>
<li>
<p><strong>Sessions are deterministic.</strong> If you do not provide a <code>sessionId</code>, one is derived from the message content. The same conversation always maps to the same session.</p>
</li>
<li>
<p><strong>Facts and instructions evolve.</strong> When a new memory shares a topic key with an existing one (for example, &quot;editor preference&quot;), the old memory is marked as superseded. The latest version surfaces in recall results, but the full history is preserved.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agent-memory/concepts/namespaces-profiles/"><h3 id="card-profiles-and-namespaces-agent-memory-concepts-namespaces-profiles">Profiles and namespaces</h3><p>Understand the isolation model for memory storage.</p></a>
<a class="nb-card nb-link-card" href="/agent-memory/api/workers-api/"><h3 id="card-workers-api-agent-memory-api-workers-api">Workers API</h3><p>Configure bindings and use profiles from Worker code.</p></a></p>
