<p>R2 is built on top of Workers and supports Unicode natively. One nuance of Unicode that is often overlooked is the issue of <a href="https://en.wikipedia.org/wiki/Filename#Encoding_indication_interoperability">filename interoperability</a> due to <a href="https://en.wikipedia.org/wiki/Unicode_equivalence">Unicode equivalence</a>.</p>
<p>Based on feedback from our users, we have chosen to NFC-normalize key names before storing by default. This means that <code>Héllo</code> and <code>Héllo</code>, for example, are the same object in R2 but different objects in other storage providers. Although <code>Héllo</code> and <code>Héllo</code> may be different character byte sequences, they are rendered the same.</p>
<p>R2 preserves the encoding for display though. When you list the objects, you will get back the last encoding you uploaded with.</p>
<p>There are still some platform-specific differences to consider:</p>
<ul>
<li>Windows and macOS filenames are case-insensitive while R2 and Linux are not.</li>
<li>Windows console support for Unicode can be error-prone. Make sure to run <code>chcp 65001</code> before using command-line tools or use Cygwin if your object names appear to be incorrect.</li>
<li>Linux allows distinct files that are unicode-equivalent because filenames are byte streams. Unicode-equivalent filenames on Linux will point to the same R2 object.</li>
</ul>
<p>If it is important for you to be able to bypass the unicode equivalence and use byte-oriented key names, contact your Cloudflare account team.</p>
