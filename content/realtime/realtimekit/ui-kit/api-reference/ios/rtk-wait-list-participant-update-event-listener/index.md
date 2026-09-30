<p>A helper class for listening to waitlist participant events.
Provides callbacks for join, remove, accept, and reject events, and methods for managing waitlist requests.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rtkClient</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
</tbody>
</table>
<h2 id="callback-properties">Callback properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>participantJoinedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a participant joins the waitlist</td>
</tr>
<tr>
<td><code>participantRemovedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a participant is removed from the waitlist</td>
</tr>
<tr>
<td><code>participantRequestAcceptedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a waitlist request is accepted</td>
</tr>
<tr>
<td><code>participantRequestRejectCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a waitlist request is rejected</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>acceptWaitingRequest(participant:)</code></td>
<td><code>Void</code></td>
<td>Accepts a participant's waitlist request</td>
</tr>
<tr>
<td><code>rejectWaitingRequest(participant:)</code></td>
<td><code>Void</code></td>
<td>Rejects a participant's waitlist request</td>
</tr>
<tr>
<td><code>clean()</code></td>
<td><code>Void</code></td>
<td>Removes all registered listeners and cleans up resources</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let waitlistListener = RtkWaitListParticipantUpdateEventListener(&#10;    rtkClient: rtkClient&#10;)&#10;&#10;waitlistListener.participantJoinedCompletion = {&#10;    print(&quot;New participant in waitlist&quot;)&#10;}&#10;&#10;waitlistListener.participantRemovedCompletion = {&#10;    print(&quot;Participant removed from waitlist&quot;)&#10;}&#10;</code></pre>
<h3 id="accept-or-reject-requests">Accept or reject requests</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let waitlistListener = RtkWaitListParticipantUpdateEventListener(&#10;    rtkClient: rtkClient&#10;)&#10;&#10;// Accept a waiting participant&#10;waitlistListener.acceptWaitingRequest(participant: waitingParticipant)&#10;&#10;// Reject a waiting participant&#10;waitlistListener.rejectWaitingRequest(participant: waitingParticipant)&#10;</code></pre>
