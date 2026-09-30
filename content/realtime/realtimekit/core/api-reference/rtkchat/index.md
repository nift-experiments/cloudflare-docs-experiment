---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/
  description: ''
  full_title: RTKChat · Cloudflare Realtime docs
  head_html: <title>RTKChat · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/index.md"><meta property="og:title" content="RTKChat · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/#page","headline":"RTKChat \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkchat/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKChat"></a></p>
<p>This is the chat module, which can be used to send and receive messages from the meeting.</p>
<ul>
<li><a href="#module_RTKChat">RTKChat</a>
<ul>
<li><del><a href="#module_RTKChat+messages">.messages</a></del></li>
<li><a href="#module_RTKChat+setMaxTextLimit">.setMaxTextLimit(limit)</a></li>
<li><a href="#module_RTKChat+updateRateLimits">.updateRateLimits(num, period)</a></li>
<li><a href="#module_RTKChat+sendTextMessage">.sendTextMessage(message, [peerIds])</a></li>
<li><a href="#module_RTKChat+sendCustomMessage">.sendCustomMessage(message, [peerIds])</a></li>
<li><a href="#module_RTKChat+sendImageMessage">.sendImageMessage(image, [peerIds])</a></li>
<li><a href="#module_RTKChat+sendFileMessage">.sendFileMessage(file, [peerIds])</a></li>
<li><a href="#module_RTKChat+sendMessage">.sendMessage(message, [participantIds])</a></li>
<li><a href="#module_RTKChat+editTextMessage">.editTextMessage(messageId, message)</a></li>
<li><a href="#module_RTKChat+editImageMessage">.editImageMessage(messageId, image)</a></li>
<li><a href="#module_RTKChat+editFileMessage">.editFileMessage(messageId, file)</a></li>
<li><a href="#module_RTKChat+editMessage">.editMessage(messageId, message)</a></li>
<li><a href="#module_RTKChat+deleteMessage">.deleteMessage(messageId)</a></li>
<li><a href="#module_RTKChat+pin">.pin(id)</a></li>
<li><a href="#module_RTKChat+unpin">.unpin(id)</a></li>
<li><a href="#module_RTKChat+fetchPublicMessages">.fetchPublicMessages(options)</a></li>
<li><a href="#module_RTKChat+fetchPrivateMessages">.fetchPrivateMessages(options)</a></li>
<li><a href="#module_RTKChat+fetchPinnedMessages">.fetchPinnedMessages(options)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKChat+messages"></a></p>
<h3 id="meeting-chat-messages"><del>meeting.chat.messages</del></h3>
***Deprecated***
<p><strong>Kind</strong>: instance property of <a href="#module_RTKChat"><code>RTKChat</code></a><br />
<a name="module_RTKChat+setMaxTextLimit"></a></p>
<h3 id="meeting-chat-setmaxtextlimit-limit">meeting.chat.setMaxTextLimit(limit)</h3>
Set the max character limit of a text message
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>limit</td>
<td><code>number</code></td>
<td>Max character limit for a text message.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+updateRateLimits"></a></p>
<h3 id="meeting-chat-updateratelimits-num-period">meeting.chat.updateRateLimits(num, period)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num</td>
<td><code>number</code></td>
</tr>
<tr>
<td>period</td>
<td><code>number</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+sendTextMessage"></a></p>
<h3 id="meeting-chat-sendtextmessage-message-peerids">meeting.chat.sendTextMessage(message, [peerIds])</h3>
Sends a chat text message to the room.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>message</td>
<td><code>string</code></td>
<td>The message that must be sent to the room.</td>
</tr>
<tr>
<td>[peerIds]</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>Peer ids to send the message to.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+sendCustomMessage"></a></p>
<h3 id="meeting-chat-sendcustommessage-message-peerids">meeting.chat.sendCustomMessage(message, [peerIds])</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>message</td>
<td><code>CustomMessagePayload</code></td>
<td>Custom message payload.</td>
</tr>
<tr>
<td>[peerIds]</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>Peer ids to send the message to.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+sendImageMessage"></a></p>
<h3 id="meeting-chat-sendimagemessage-image-peerids">meeting.chat.sendImageMessage(image, [peerIds])</h3>
Sends an image message to the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>image</td>
<td><code>File</code> | <code>ReactNativeFile</code></td>
<td>The image that is to be sent.</td>
</tr>
<tr>
<td>[peerIds]</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>Peer ids to send the message to.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+sendFileMessage"></a></p>
<h3 id="meeting-chat-sendfilemessage-file-peerids">meeting.chat.sendFileMessage(file, [peerIds])</h3>
Sends a file to the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>file</td>
<td><code>File</code> | <code>ReactNativeFile</code></td>
<td>A File object.</td>
</tr>
<tr>
<td>[peerIds]</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>Peer ids to send the message to.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+sendMessage"></a></p>
<h3 id="meeting-chat-sendmessage-message-participantids">meeting.chat.sendMessage(message, [participantIds])</h3>
Sends a message to the meeting. This method can be used to send text, image,
or file messages. The message type is determined by the key 'type' in `message`
object.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>message</td>
<td><code>MessagePayload</code></td>
<td>An object including the type and content of the message.</td>
</tr>
<tr>
<td>[participantIds]</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>An array including the userIds of the participants.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+editTextMessage"></a></p>
<h3 id="meeting-chat-edittextmessage-messageid-message">meeting.chat.editTextMessage(messageId, message)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>messageId</td>
<td><code>string</code></td>
<td>Id of the message to edit.</td>
</tr>
<tr>
<td>message</td>
<td><code>string</code></td>
<td>Updated text message.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+editImageMessage"></a></p>
<h3 id="meeting-chat-editimagemessage-messageid-image">meeting.chat.editImageMessage(messageId, image)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>messageId</td>
<td><code>string</code></td>
<td>Id of the message to edit.</td>
</tr>
<tr>
<td>image</td>
<td><code>File</code> | <code>ReactNativeFile</code></td>
<td>Updated image file.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+editFileMessage"></a></p>
<h3 id="meeting-chat-editfilemessage-messageid-file">meeting.chat.editFileMessage(messageId, file)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>messageId</td>
<td><code>string</code></td>
<td>Id of the message to edit.</td>
</tr>
<tr>
<td>file</td>
<td><code>File</code> | <code>ReactNativeFile</code></td>
<td>Updated file.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+editMessage"></a></p>
<h3 id="meeting-chat-editmessage-messageid-message">meeting.chat.editMessage(messageId, message)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>messageId</td>
<td><code>string</code></td>
<td>Id of the message to edit.</td>
</tr>
<tr>
<td>message</td>
<td><code>MessagePayload</code></td>
<td>Updated message payload.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+deleteMessage"></a></p>
<h3 id="meeting-chat-deletemessage-messageid">meeting.chat.deleteMessage(messageId)</h3>
**Kind**: instance method of [<code>RTKChat</code>](#module_RTKChat)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>messageId</td>
<td><code>string</code></td>
<td>Id of the message to delete.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+pin"></a></p>
<h3 id="meeting-chat-pin-id">meeting.chat.pin(id)</h3>
Pins a chat message
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td><code>string</code></td>
<td>ID of the message to be pinned</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+unpin"></a></p>
<h3 id="meeting-chat-unpin-id">meeting.chat.unpin(id)</h3>
Unpins a chat message
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td><code>string</code></td>
<td>ID of the message to be unpinned</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+fetchPublicMessages"></a></p>
<h3 id="meeting-chat-fetchpublicmessages-options">meeting.chat.fetchPublicMessages(options)</h3>
Fetches messages from the chat with pagination.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>options</td>
<td><code>FetchMessageOptions</code></td>
<td>Configuration options for fetching messages, including timestamp, limit, and direction for pagination.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+fetchPrivateMessages"></a></p>
<h3 id="meeting-chat-fetchprivatemessages-options">meeting.chat.fetchPrivateMessages(options)</h3>
Fetches private messages between the current user and another participant with pagination.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>options</td>
<td><code>FetchPrivateMessagesOptions</code></td>
<td>Configuration options for fetching private messages, including private RTKChat ID (User ID of the participant) and pagination settings.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKChat+fetchPinnedMessages"></a></p>
<h3 id="meeting-chat-fetchpinnedmessages-options">meeting.chat.fetchPinnedMessages(options)</h3>
Fetches pinned messages with pagination.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKChat"><code>RTKChat</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>options</td>
<td><code>FetchMessageOptions</code></td>
<td>Configuration options for fetching pinned messages, including timestamp, limit, and direction.</td>
</tr>
</tbody>
</table>
