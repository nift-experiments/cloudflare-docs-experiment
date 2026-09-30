<!-- Auto Generated Below -->
<p><a name="module_RTKPolls"></a></p>
<p>The RTKPolls module consists of the polls that have been created in the meeting.</p>
<ul>
<li><a href="#module_RTKPolls">RTKPolls</a>
<ul>
<li><a href="#module_RTKPolls+items">.items</a></li>
<li><a href="#module_RTKPolls+create">.create(question, options, anonymous, hideVotes)</a></li>
<li><a href="#module_RTKPolls+vote">.vote(pollId, index)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPolls+items"></a></p>
<h3 id="meeting-polls-items">meeting.polls.items</h3>
An array of poll items.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPolls"><code>RTKPolls</code></a><br />
<a name="module_RTKPolls+create"></a></p>
<h3 id="meeting-polls-create-question-options-anonymous-hidevotes">meeting.polls.create(question, options, anonymous, hideVotes)</h3>
Creates a poll in the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPolls"><code>RTKPolls</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>question</td>
<td></td>
<td>The question that is to be voted for.</td>
</tr>
<tr>
<td>options</td>
<td></td>
<td>The options of the poll.</td>
</tr>
<tr>
<td>anonymous</td>
<td><code>false</code></td>
<td>If true, the poll votes are anonymous.</td>
</tr>
<tr>
<td>hideVotes</td>
<td><code>false</code></td>
<td>If true, the votes on the poll are hidden.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPolls+vote"></a></p>
<h3 id="meeting-polls-vote-pollid-index">meeting.polls.vote(pollId, index)</h3>
Casts a vote on an existing poll.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPolls"><code>RTKPolls</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>pollId</td>
<td>The ID of the poll that is to be voted on.</td>
</tr>
<tr>
<td>index</td>
<td>The index of the option.</td>
</tr>
</tbody>
</table>
