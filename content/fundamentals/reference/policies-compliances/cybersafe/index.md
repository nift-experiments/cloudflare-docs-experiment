<p>Project Cybersafe Schools grants eligible schools with free access to Cloudflare's <a href="/email-security/">Email security</a> and <a href="/cloudflare-one/traffic-policies/">Gateway</a> products.</p>
<h2 id="school-eligibility">School Eligibility</h2>
<p>This program is only available to eligible school districts. To be eligible, Project Cybersafe School participants must be:</p>
<ul>
<li>K-12 public school districts located in the United States.</li>
<li>Up to 2,500 students in the district.</li>
</ul>
<h2 id="children-s-internet-protection-act-cipa">Children’s Internet Protection Act (CIPA)</h2>
<p>The <a href="https://www.fcc.gov/sites/default/files/childrens_internet_protection_act_cipa.pdf">Children's Internet Protection Act (CIPA)</a> is a federal law enacted by the United States Congress to address concerns about children's access to inappropriate or harmful content over the Internet. CIPA requires K-12 schools and libraries that receive certain federal funding to implement Internet safety measures to protect minors from harmful online content.</p>
<p>The law aims to prevent students from accessing explicit, obscene, or otherwise harmful material. It also emphasizes the use of technology protection measures, including DNS filtering, to safeguard against Internet threats such as ransomware, phishing sites, and other potentially harmful content.</p>
<h3 id="cipa-requirements">CIPA Requirements</h3>
<p>CIPA mandates that K-12 schools and libraries adopt Internet safety policies that include measures to block or filter access to specific categories of content. These categories encompass a wide range of topics that could be harmful or inappropriate for minors. Compliance with these requirements helps ensure that students' online experiences are safer and more secure.</p>
<h3 id="configuration">Configuration</h3>
<p>To facilitate compliance with CIPA requirements, administrators can <a href="/cloudflare-one/traffic-policies/dns-policies/common-policies/#turn-on-cipa-filter">enable a single filtering policy option</a>. This includes applying the required filter categories to block access to unwanted or harmful online content.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9007.md")
</aside>
<p>Cloudflare’s recommended CIPA rule blocks the following content subcategories:</p>
<ul>
<li>Adult Themes</li>
<li>Alcohol</li>
<li>Anonymizer</li>
<li>Brand Embedding</li>
<li>Child Abuse</li>
<li>Command and Control &amp; Botnet</li>
<li>Cryptomining</li>
<li>DGA Domains</li>
<li>DNS Tunneling</li>
<li>Drugs</li>
<li>Gambling</li>
<li>Hacking</li>
<li>Malware</li>
<li>Militancy, Hate &amp; Extremism</li>
<li>Nudity</li>
<li>P2P</li>
<li>Phishing</li>
<li>Pornography</li>
<li>Private IP Address</li>
<li>Profanity</li>
<li>Questionable Activities</li>
<li>School Cheating</li>
<li>Spam</li>
<li>Spyware</li>
<li>Tobacco</li>
<li>Violence</li>
<li>Weapons</li>
</ul>
<p>Review the <a href="/cloudflare-one/traffic-policies/domain-categories/">domain categories</a> for more information.</p>
<h3 id="onboarding-guide">Onboarding Guide</h3>
<p>For a comprehensive guide, refer to the <a href="/learning-paths/cybersafe/concepts/">Project Cybersafe Schools Learning Path</a>, which takes you step by step through the technical concepts, creating an account, onboarding your traffic, and enabling the CIPA filters.</p>
