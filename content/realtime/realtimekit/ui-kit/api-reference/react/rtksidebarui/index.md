<h2 id="properties">Properties</h2>
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
<td><code>currentTab</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Default tab to open</td>
</tr>
<tr>
<td><code>focusCloseButton</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Option to focus close button when opened</td>
</tr>
<tr>
<td><code>hideCloseAction</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide Close Action</td>
</tr>
<tr>
<td><code>hideHeader</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide Main Header</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>{ people: string; people_checked: string; chat: string; poll: string; participants: string; rocket: string; call_end: string; share: string; mic_on: string; mic_off: string; video_on: string; video_off: string; share_screen_start: string; share_screen_stop: string; share_screen_person: string; clock: string; dismiss: string; send: string; search: string; more_vertical: string; chevron_down: string; chevron_up: string; chevron_left: string; chevron_right: string; settings: string; wifi: string; speaker: string; speaker_off: string; download: string; full_screen_maximize: string; full_screen_minimize: string; copy: string; attach: string; image: string; emoji_multiple: string; image_off: string; disconnected: string; wand: string; recording: string; subtract: string; stop_recording: string; warning: string; pin: string; pin_off: string; spinner: string; breakout_rooms: string; add: string; shuffle: string; edit: string; delete: string; back: string; save: string; web: string; checkmark: string; spotlight: string; join_stage: string; leave_stage: string; pip_off: string; pip_on: string; signal_1: string; signal_2: string; signal_3: string; signal_4: string; signal_5: string; start_livestream: string; stop_livestream: string; viewers: string; debug: string; info: string; devices: string; horizontal_dots: string; ai_sparkle: string; meeting_ai: string; captionsOn: string; captionsOff: string; play: string; pause: string; fastForward: string; minimize: string; maximize: string; }</code></td>
<td>✅</td>
<td>-</td>
<td>Icon Pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>tabs</code></td>
<td><code>RtkSidebarTab1[]</code></td>
<td>✅</td>
<td>-</td>
<td>Tabs</td>
</tr>
<tr>
<td><code>view</code></td>
<td><code>RtkSidebarView1</code></td>
<td>✅</td>
<td>-</td>
<td>View</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkSidebarUi } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkSidebarUi /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkSidebarUi } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkSidebarUi&#10;      currentTab=&quot;example&quot;&#10;      focusCloseButton={true}&#10;      hideCloseAction={true}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
