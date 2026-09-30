<h2 id="draft-16-messages">Draft-16 messages</h2>
<h3 id="supported">Supported</h3>
<table>
<thead>
<tr>
<th>Message</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>SUBSCRIBE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>UNSUBSCRIBE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>PUBLISH</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>PUBLISH_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE_ERROR</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>UNSUBSCRIBE_NAMESPACE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_ERROR</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>TRACK_STATUS</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>TRACK_STATUS_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SETUP_MESSAGES (client and server)</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
</tbody>
</table>
<h3 id="partial">Partial</h3>
<table>
<thead>
<tr>
<th>Message</th>
<th>Support</th>
<th>Notes</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>MAX_REQUEST_ID</td>
<td>Partial</td>
<td>Initial limit negotiated in SETUP and mid-session raises are applied. REQUESTS_BLOCKED does not trigger an automatic limit increase.</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>REQUESTS_BLOCKED</td>
<td>Partial</td>
<td>Received and logged. It does not trigger an automatic MAX_REQUEST_ID response.</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
</tbody>
</table>
<h3 id="unsupported">Unsupported</h3>
<table>
<thead>
<tr>
<th>Message</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>GOAWAY</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>SUBSCRIBE_UPDATE</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>PUBLISH_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>FETCH</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>FETCH_OK</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>FETCH_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>FETCH_CANCEL</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
<tr>
<td>TRACK_STATUS_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16">draft-ietf-moq-transport-16</a></td>
</tr>
</tbody>
</table>
<h2 id="draft-14-messages">Draft-14 messages</h2>
<h3 id="supported-1">Supported</h3>
<table>
<thead>
<tr>
<th>Message</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>SUBSCRIBE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>UNSUBSCRIBE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>TRACK_STATUS</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_NAMESPACE_CANCEL</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_NAMESPACE_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_NAMESPACE_ERROR</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_NAMESPACE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_NAMESPACE_DONE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_DONE</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_ERROR</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>TRACK_STATUS_OK</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SETUP_MESSAGES (client and server)</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
</tbody>
</table>
<h3 id="unsupported-1">Unsupported</h3>
<table>
<thead>
<tr>
<th>Message</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>GOAWAY</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>MAX_REQUEST_ID</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>REQUESTS_BLOCKED</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_UPDATE</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>PUBLISH_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>FETCH</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>FETCH_OK</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>FETCH_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>FETCH_CANCEL</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>TRACK_STATUS_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE_OK</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>SUBSCRIBE_NAMESPACE_ERROR</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
<tr>
<td>UNSUBSCRIBE_NAMESPACE</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-ietf-moq-transport-14</a></td>
</tr>
</tbody>
</table>
