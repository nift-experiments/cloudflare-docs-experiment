<p>A component which lists all participants, with the ability to run privileged actions on each participant according to your permissions.</p>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>show</code></td>
<td><code>fragmentManager: FragmentManager, tag: String?</code></td>
<td>Display the participant list bottom sheet</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val rtkParticipantsFragment = RtkParticipantsFragment()&#10;rtkParticipantsFragment.show(fragmentManager, &quot;PARTICIPANTS_TAG&quot;)&#10;</code></pre>
