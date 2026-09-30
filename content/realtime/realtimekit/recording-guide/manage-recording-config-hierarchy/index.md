<p>This document provides an overview of the precedence structure for managing recording configurations within our system. It explains how various configuration levels interact and prioritize settings. The recording configuration can be defined at three different levels:</p>
<ul>
<li><a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording a meeting API</a></li>
<li><a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a></li>
<li>Specified via <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare RealtimeKit Dashboard</a></li>
</ul>
<h2 id="understand-recording-configuration-precedence">Understand Recording Configuration Precedence</h2>
<p>To comprehend the precedence of recording configurations, it is important to delve into the following details. This understanding becomes crucial when dealing with multiple configurations set through APIs and the developer portal.</p>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Config</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording API</a> configs</td>
<td>Highest priority in the system. Any settings defined here will take precedence over other configurations.</td>
</tr>
<tr>
<td>2</td>
<td><a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a> configs</td>
<td>Second level of priority in the system. Settings here will supersede Org level config but not Start recording a meeting API configs.</td>
</tr>
<tr>
<td>3</td>
<td>Specified via Dashboard</td>
<td>Lowest priority in the system. Settings defined here will be overridden by both Start recording a meeting API config and Create a meeting API config.</td>
</tr>
</tbody>
</table>
<h2 id="example-scenario">Example Scenario</h2>
<p>To illustrate the precedence order in action, consider the following scenario for the same meeting:</p>
<ol>
<li>
<p>Org Level Config specifies that recordings to be stored in the Cloudflare R2 bucket.</p>
</li>
<li>
<p>Create a Meeting API sets recordings to be stored in the AWS S3 storage bucket using the H264 codec.</p>
</li>
<li>
<p>Start recording a meeting API is configured to store recordings in the GCS bucket using the VP8 codec.</p>
</li>
</ol>
<p>In this scenario, the Start recording a meeting API takes precedence over the Create a Meeting API Config and Org Level Config.
As a result, the meeting's recording will be stored in the GCS bucket using VP8 codec, regardless of the defaults set at other levels.</p>
<head>
	<title>Manage Recording Config Precedence Order Guide</title>
	<meta name="description" content="Learn how to manage recording configuration hierarchy with RealtimeKit's capabilities. Follow our guide for effective hierarchy management." />
</head>
