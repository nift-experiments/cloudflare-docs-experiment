<p>Agent Memory uses a two-level isolation model: <strong>namespaces</strong> define memory domains, and <strong>profiles</strong> provide isolated memory stores for individual users, agents, teams, tenants, or application objects.</p>
<h2 id="namespaces">Namespaces</h2>
<p>A namespace is a top-level container that scopes a set of memory profiles. Use namespaces to separate applications, environments, tenants, or memory layers such as user, team, and organization memory.</p>
<h2 id="profiles">Profiles</h2>
<p>A profile is an isolated memory store for a single entity. Each profile has its own stored memories and retrieval indexes.</p>
<h2 id="sessions">Sessions</h2>
<p>A session groups memories that come from the same interaction or conversation. Sessions are optional, but they make it easier to identify, inspect, and manage memories created from a specific conversation.</p>
<p>Sessions are scoped to a profile. Two different profiles can use the same session ID without conflict.</p>
<h2 id="isolation-model">Isolation model</h2>
<p>Conceptually, memories are scoped as <code>namespace &gt; profile &gt; memory</code>. No data crosses these boundaries:</p>
<pre><code class="language-txt">Namespace: my-assistant-prod&#10;  Profile: alice&#10;    Memories&#10;    Messages&#10;  Profile: bob&#10;    Memories&#10;    Messages&#10;</code></pre>
<p>A <code>recall()</code> on Alice's profile never returns memories from Bob's profile. Each profile is a self-contained memory system.</p>
