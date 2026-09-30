<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11597.md")
</aside>
<h3 id="offerings">Offerings</h3>
<p>RealtimeKit provides two ways to build real-time media applications:</p>
<p><strong>UI Kit</strong>: <div class="nb-r-t-k-pill"></p>
@markup("md", "content/.markup/bodies/11598.md")
</div> UI library of pre-built, customizable components for rapid development — sits on top of the Core SDK.
<p><strong>Core SDK</strong>: Client SDK built on top of Realtime SFU that provides a full set of APIs for managing video calls, from joining and leaving sessions to muting, unmuting, and toggling audio and video.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11596.md")
</aside>
<h3 id="select-your-framework">Select your framework</h3>
<p>RealtimeKit support all the popular frameworks for web and mobile platforms. Please select the Platform and Framework that you are building on.</p>
<table>
<thead>
<tr>
<th>Framework/Library</th>
<th>Core SDK</th>
<th>UI Kit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Web-Components (HTML, Vue, Svelte)</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit">@cloudflare/realtimekit</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-ui">@cloudflare/realtimekit-ui</a></td>
</tr>
<tr>
<td>React</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react">@cloudflare/realtimekit-react</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-ui">@cloudflare/realtimekit-react-ui</a></td>
</tr>
<tr>
<td>Angular</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit">@cloudflare/realtimekit</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-angular-ui">@cloudflare/realtimekit-angular-ui</a></td>
</tr>
<tr>
<td>Android</td>
<td><a href="https://central.sonatype.com/artifact/com.cloudflare.realtimekit/core">com.cloudflare.realtimekit:core</a></td>
<td><a href="https://central.sonatype.com/artifact/com.cloudflare.realtimekit/ui-android">com.cloudflare.realtimekit:ui-android</a></td>
</tr>
<tr>
<td>iOS</td>
<td><a href="https://github.com/dyte-in/RealtimeKitCoreiOS">RealtimeKit</a></td>
<td><a href="https://github.com/dyte-in/RealtimeKitUI">RealtimeKitUI</a></td>
</tr>
<tr>
<td>React Native</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-native">@cloudflare/realtimekit-react-native</a></td>
<td><a href="https://www.npmjs.com/package/@cloudflare/realtimekit-react-native-ui">@cloudflare/realtimekit-react-native-ui</a></td>
</tr>
</tbody>
</table>
<h3 id="technical-comparison">Technical comparison</h3>
<p>Here is a comprehensive guide to help you choose the right option for your project. This comparison will help you understand the trade-offs between using the Core SDK alone versus combining it with the UI Kit.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Core SDK only</th>
<th>UI Kit</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>What you get</strong></td>
<td>Core APIs for managing media, host controls, chat, recording and more.</td>
<td>prebuilt UI components along with Core APIs.</td>
</tr>
<tr>
<td><strong>Bundle size</strong></td>
<td>Minimal (media/network only)</td>
<td>Larger (includes Core SDK + UI components)</td>
</tr>
<tr>
<td><strong>Time to ship</strong></td>
<td>Longer (build UI from scratch). Typically 5-6 days.</td>
<td>Faster (UI Kit handles Core SDK calls). Can build an ship under 2 hours.</td>
</tr>
<tr>
<td><strong>Customization</strong></td>
<td>Complete control, manual implementation. Need to build you own UI</td>
<td>High level of customization with plug and play component library.</td>
</tr>
<tr>
<td><strong>State management</strong></td>
<td>Needs to be manually handled.</td>
<td>Automatic, UI Kit takes care of state management.</td>
</tr>
<tr>
<td><strong>UI flexibility</strong></td>
<td>Unlimited (build anything)</td>
<td>High (component library + add-ons)</td>
</tr>
<tr>
<td><strong>Learning curve</strong></td>
<td>Steeper (learn Core SDK APIs directly)</td>
<td>Gentler (declarative components wrap Core SDK)</td>
</tr>
<tr>
<td><strong>Maintenance</strong></td>
<td>More code to maintain. Larger project.</td>
<td>Less code, component updates included</td>
</tr>
<tr>
<td><strong>Design system</strong></td>
<td>Headless, integrates with any design system.</td>
<td>Allows you to provide your theme.</td>
</tr>
<tr>
<td><strong>Access to Core SDK</strong></td>
<td>Direct API access</td>
<td>Direct API access + UI components</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11595.md")
</aside>
