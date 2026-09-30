<p>Cloudflare Gateway allows you to block known and potential security risks on the public Internet, as well as specific categories of content. Domains are categorized by <a href="/security-center/cloudforce-one/">Cloudforce One</a>, Cloudflare's threat intelligence solution. To review the categories for a specific domain, use <a href="/radar/glossary/#content-categories">Cloudflare Radar</a>.</p>
<p>Cloudflare categorizes domains into content categories and security categories, which cover security risks and security threats:</p>
<ul>
<li><strong>Content categories</strong>: An upstream vendor supplies content categories for domains. These categories help us organize domains into broad topic areas. However, the specific criteria and methods used by our vendor may not be disclosed.</li>
<li><strong>Security risks</strong>: Cloudflare determines security risks for domains using internal models. These models analyze various factors, including the age of a domain and its reputation. This allows us to identify potentially risky domains.</li>
<li><strong>Security threats</strong>: To identify malicious domains that pose security threats, Cloudflare employs a mix of internal data sources, machine learning models, commercial feeds, and open-source threat intelligence.</li>
</ul>
<p>You can block security and content categories by creating DNS or HTTP policies. Once you have configured your policies, you will be able to inspect network activity and the associated categories in your Gateway logs.</p>
<p>To request changes to a domain's categorization, refer to <a href="/security-center/investigate/change-categorization/">Change categorization</a>. For more information on investigating potentially risky domains, refer to <a href="/security-center/investigate/investigate-threats/#domain">Investigate threats</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="subdomain-category">Subdomain category</h3>
@markup("md", "content/.markup/bodies/4422.md")
</aside>
<h2 id="security-categories">Security categories</h2>
<table>
<thead>
<tr>
<th>Category</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anonymizer</td>
<td>Sites that allow users to surf the Internet anonymously.</td>
</tr>
<tr>
<td>Brand Embedding</td>
<td>Sites that imitate a verified brand, for example <code>facobook.com</code>.</td>
</tr>
<tr>
<td>Command and Control &amp; Botnet</td>
<td>Sites that are queried by compromised devices to exfiltrate information or potentially infect other devices in a network.</td>
</tr>
<tr>
<td>Compromised Domain</td>
<td>Sites where a legitimate domain has been compromised or taken over and had malicious content planted or injected.</td>
</tr>
<tr>
<td>Cryptomining</td>
<td>Sites that mine cryptocurrency by taking over the user's computing resources.</td>
</tr>
<tr>
<td>DGA Domains</td>
<td>Domains generated programmatically by Domain Generation Algorithms (DGA) associated with malware. These algorithmically created domain names change frequently, making them harder to block individually.</td>
</tr>
<tr>
<td>DNS Tunneling</td>
<td>Domains with detected DNS tunneling activity, including attempts to encode or exfiltrate data in DNS queries and responses (for example, in <code>TXT</code> records) or to use DNS for command-and-control (C2) communications.</td>
</tr>
<tr>
<td>Malware</td>
<td>Sites hosting malicious content and other compromised websites.</td>
</tr>
<tr>
<td>Phishing</td>
<td>Domains that are known for stealing personal information.</td>
</tr>
<tr>
<td>Potentially Unwanted Software</td>
<td>Domains that distribute software that may come bundled with other less legitimate software or functionality, like toolbars, adware, and grayware.</td>
</tr>
<tr>
<td>Private IP Address</td>
<td>Domains that resolve to private IP Addresses.</td>
</tr>
<tr>
<td>Scam</td>
<td>Fraudulent websites and schemes designed to trick victims into giving away money or personal information.</td>
</tr>
<tr>
<td>Spam</td>
<td>Sites that are known for targeting users with unwanted sweepstakes, surveys, and advertisements.</td>
</tr>
<tr>
<td>Spyware</td>
<td>Sites that are known to distribute or contain code that displays unwanted advertisements or that gathers user information without the user's knowledge.</td>
</tr>
</tbody>
</table>
<h2 id="content-categories">Content categories</h2>
<table>
<thead>
<tr>
<th>Category</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ads</td>
<td>Sites that are hosting content related to advertising.</td>
</tr>
<tr>
<td>Adult Themes</td>
<td>Sites that are hosting content related to pornography, nudity, sexuality, and other adult themes.</td>
</tr>
<tr>
<td>Business &amp; Economy</td>
<td>Sites that are related to business, economy, finance, education, science and technology.</td>
</tr>
<tr>
<td>Child Abuse</td>
<td>Sites hosting child abuse content.</td>
</tr>
<tr>
<td>CIPA</td>
<td>Sites related to aiding schools and organizations in abiding by Children's Internet Protection Act (CIPA) requirements.</td>
</tr>
<tr>
<td>Education</td>
<td>Sites hosting educational content that are not included in other categories like Science, Technology or Educational institutions.</td>
</tr>
<tr>
<td>Entertainment</td>
<td>Sites that are hosting entertaining content that are not included in other categories like Comic books, Audio streaming, Video streaming etc.</td>
</tr>
<tr>
<td>Gambling</td>
<td>Sites that are providing online gambling or are related to gambling.</td>
</tr>
<tr>
<td>Government &amp; Politics</td>
<td>Sites related to government and politics.</td>
</tr>
<tr>
<td>Health</td>
<td>Sites containing information about health and fitness.</td>
</tr>
<tr>
<td>Information Technology</td>
<td>Sites related to information technology.</td>
</tr>
<tr>
<td>Internet Communication</td>
<td>Sites hosting applications that are used for communication like chat, mail etc.</td>
</tr>
<tr>
<td>Job Search &amp; Careers</td>
<td>Sites that facilitate searching for jobs and careers.</td>
</tr>
<tr>
<td>Miscellaneous</td>
<td>Sites that are not included in the listed security and content categories.</td>
</tr>
<tr>
<td>Questionable Content</td>
<td>Sites hosting content that are related to hacking, piracy, profanity and other questionable activities.</td>
</tr>
<tr>
<td>Real Estate</td>
<td>Sites related to real estate.</td>
</tr>
<tr>
<td>Religion</td>
<td>Sites hosting content about religion, alternative religion, religious teachings, religious groups, and spirituality.</td>
</tr>
<tr>
<td>Security Risks</td>
<td>Sites that are <a href="#security-risk-subcategories">new or misconfigured</a>. We recommend that you allow or isolate this content category to avoid accidentally blocking trusted domains.</td>
</tr>
<tr>
<td>Shopping &amp; Auctions</td>
<td>Sites that are hosting content related to ecommerce, coupons, shopping, auctions and marketplaces.</td>
</tr>
<tr>
<td>Social &amp; Family</td>
<td>Sites related to society and lifestyle.</td>
</tr>
<tr>
<td>Society &amp; Lifestyle</td>
<td>Sites hosting information about lifestyle that are not included in other categories like fashion, food &amp; drink etc.</td>
</tr>
<tr>
<td>Sports</td>
<td>Sites related to sports &amp; recreation.</td>
</tr>
<tr>
<td>Technology</td>
<td>Sites hosting information about technology that are not included in the science category.</td>
</tr>
<tr>
<td>Travel</td>
<td>Sites that contain information about listings, reservations, services for travel.</td>
</tr>
<tr>
<td>Vehicles</td>
<td>Sites related vehicles, automobiles, including news, reviews, and other hobbyist information.</td>
</tr>
<tr>
<td>Violence</td>
<td>Sites hosting and/or promoting violent content.</td>
</tr>
<tr>
<td>Weather</td>
<td>Sites related to weather.</td>
</tr>
</tbody>
</table>
<h3 id="miscellaneous-subcategories">Miscellaneous subcategories</h3>
<table>
<thead>
<tr>
<th>Category</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Login Screens</td>
<td>Sites hosting login screens that might also be included in other categories.</td>
</tr>
<tr>
<td>Miscellaneous</td>
<td>Sites that do not belong to other content categories.</td>
</tr>
<tr>
<td>No Content</td>
<td>Sites that have no content.</td>
</tr>
<tr>
<td>Redirect</td>
<td>Domains that redirect to other sites.</td>
</tr>
<tr>
<td>Unreachable</td>
<td>Domains that resolve to unreachable IP addresses.</td>
</tr>
</tbody>
</table>
<h3 id="security-risk-subcategories">Security risk subcategories</h3>
<table>
<thead>
<tr>
<th>Category</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>New Domains</td>
<td>Domains registered within the past 30 days.</td>
</tr>
<tr>
<td>Newly Seen Domains</td>
<td>Domains that were resolved for the first time within the past 30 days.</td>
</tr>
<tr>
<td>Parked &amp; For Sale Domains</td>
<td>Domains that are not connected to a hosting service.</td>
</tr>
</tbody>
</table>
<h3 id="category-and-subcategory-ids">Category and subcategory IDs</h3>
<table>
<thead>
<tr>
<th>Category ID</th>
<th>Category Name</th>
<th>Subcategory ID</th>
<th>Subcategory Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Ads</td>
<td>66</td>
<td>Advertisements</td>
</tr>
<tr>
<td>2</td>
<td>Adult Themes</td>
<td>67</td>
<td>Adult Themes</td>
</tr>
<tr>
<td>2</td>
<td>Adult Themes</td>
<td>125</td>
<td>Nudity</td>
</tr>
<tr>
<td>2</td>
<td>Adult Themes</td>
<td>133</td>
<td>Pornography</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>186</td>
<td>Brokerage &amp; Investing</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>75</td>
<td>Business</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>89</td>
<td>Economy &amp; Finance</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>183</td>
<td>Cryptocurrency</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>185</td>
<td>Personal Finance</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>90</td>
<td>Education</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>91</td>
<td>Educational Institutions</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>189</td>
<td>Reference</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>144</td>
<td>Science</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>150</td>
<td>Space &amp; Astronomy</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>70</td>
<td>Arts</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>74</td>
<td>Audio Streaming</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>76</td>
<td>Cartoons &amp; Anime</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>79</td>
<td>Comic Books</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>92</td>
<td>Entertainment</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>96</td>
<td>Fine Art</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>100</td>
<td>Gaming</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>106</td>
<td>Home Video/DVD</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>107</td>
<td>Humor</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>116</td>
<td>Magazines</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>120</td>
<td>Movies</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>121</td>
<td>Music</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>122</td>
<td>News &amp; Media</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>127</td>
<td>Paranormal</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>139</td>
<td>Radio</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>156</td>
<td>Television</td>
</tr>
<tr>
<td>7</td>
<td>Entertainment</td>
<td>164</td>
<td>Video Streaming</td>
</tr>
<tr>
<td>8</td>
<td>Gambling</td>
<td>99</td>
<td>Gambling</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>190</td>
<td>Charity and Non-profit</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>101</td>
<td>Government/Legal</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>137</td>
<td>Politics, Advocacy, and Government-Related</td>
</tr>
<tr>
<td>10</td>
<td>Health</td>
<td>103</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>10</td>
<td>Health</td>
<td>146</td>
<td>Sex Education</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>77</td>
<td>Chat</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>98</td>
<td>Forums</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>108</td>
<td>Information Security</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>110</td>
<td>Instant Messengers</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>111</td>
<td>Internet Phone &amp; VOIP</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>118</td>
<td>Messaging</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>126</td>
<td>P2P</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>129</td>
<td>Personal Blogs</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>168</td>
<td>Webmail</td>
</tr>
<tr>
<td>12</td>
<td>Internet Communication</td>
<td>172</td>
<td>Photo Sharing</td>
</tr>
<tr>
<td>13</td>
<td>Job Search &amp; Careers</td>
<td>113</td>
<td>Job Search &amp; Careers</td>
</tr>
<tr>
<td>15</td>
<td>Miscellaneous</td>
<td>115</td>
<td>Login Screens</td>
</tr>
<tr>
<td>15</td>
<td>Miscellaneous</td>
<td>119</td>
<td>Miscellaneous</td>
</tr>
<tr>
<td>15</td>
<td>Miscellaneous</td>
<td>124</td>
<td>No Content</td>
</tr>
<tr>
<td>15</td>
<td>Miscellaneous</td>
<td>141</td>
<td>URL Alias/Redirect</td>
</tr>
<tr>
<td>15</td>
<td>Miscellaneous</td>
<td>161</td>
<td>Unreachable</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>85</td>
<td>Deceptive Ads</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>87</td>
<td>Drugs</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>102</td>
<td>Hacking</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>135</td>
<td>Profanity</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>138</td>
<td>Questionable Activities</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>157</td>
<td>Militancy, Hate &amp; Extremism</td>
</tr>
<tr>
<td>17</td>
<td>Questionable Content</td>
<td>162</td>
<td>Unreliable Information</td>
</tr>
<tr>
<td>18</td>
<td>Real Estate</td>
<td>140</td>
<td>Real Estate</td>
</tr>
<tr>
<td>19</td>
<td>Religion</td>
<td>142</td>
<td>Religion &amp; Spirituality</td>
</tr>
<tr>
<td>20</td>
<td>Safe for Kids</td>
<td>143</td>
<td>Safe for Kids</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>68</td>
<td>Anonymizer</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>80</td>
<td>Command and Control &amp; Botnet</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>187</td>
<td>Compromised Domain</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>83</td>
<td>Cryptomining</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>117</td>
<td>Malware</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>131</td>
<td>Phishing</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>188</td>
<td>Potentially unwanted software</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>134</td>
<td>Private IP Address</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>151</td>
<td>Spam</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>153</td>
<td>Spyware</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>175</td>
<td>DNS Tunneling</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>176</td>
<td>Domain Generation Algorithm</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>178</td>
<td>Brand Embedding</td>
</tr>
<tr>
<td>21</td>
<td>Security threats</td>
<td>191</td>
<td>Scam</td>
</tr>
<tr>
<td>22</td>
<td>Shopping &amp; Auctions</td>
<td>73</td>
<td>Auctions &amp; Marketplaces</td>
</tr>
<tr>
<td>22</td>
<td>Shopping &amp; Auctions</td>
<td>82</td>
<td>Coupons</td>
</tr>
<tr>
<td>22</td>
<td>Shopping &amp; Auctions</td>
<td>88</td>
<td>Ecommerce</td>
</tr>
<tr>
<td>22</td>
<td>Shopping &amp; Auctions</td>
<td>148</td>
<td>Shopping</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>71</td>
<td>Arts &amp; Crafts</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>72</td>
<td>Astrology</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>78</td>
<td>Clothing</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>84</td>
<td>Dating &amp; Relationships</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>86</td>
<td>Digital Postcards</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>93</td>
<td>Parenting</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>94</td>
<td>Fashion</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>97</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>104</td>
<td>Hobbies &amp; Interests</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>105</td>
<td>Home &amp; Garden</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>114</td>
<td>Lifestyle</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>130</td>
<td>Pets</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>132</td>
<td>Photography</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>136</td>
<td>Professional Networking</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>147</td>
<td>Sexuality</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>149</td>
<td>Social Networks</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>154</td>
<td>Swimsuits</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>158</td>
<td>Tobacco</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>173</td>
<td>Body Art</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>174</td>
<td>Lingerie &amp; Bikini</td>
</tr>
<tr>
<td>24</td>
<td>Society &amp; Lifestyle</td>
<td>181</td>
<td>Alcohol</td>
</tr>
<tr>
<td>25</td>
<td>Sports</td>
<td>152</td>
<td>Sports</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>69</td>
<td>APIs</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>81</td>
<td>Content Servers</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>95</td>
<td>File Sharing</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>109</td>
<td>Information Technology</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>123</td>
<td>News, Portal &amp; Search</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>145</td>
<td>Search Engines</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>155</td>
<td>Technology</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>159</td>
<td>Translator</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>184</td>
<td>Artificial Intelligence</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>192</td>
<td>Remote Access</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>193</td>
<td>Shareware/Freeware</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>194</td>
<td>Keep Awake Software</td>
</tr>
<tr>
<td>27</td>
<td>Travel</td>
<td>160</td>
<td>Travel</td>
</tr>
<tr>
<td>28</td>
<td>Vehicles</td>
<td>163</td>
<td>Vehicles</td>
</tr>
<tr>
<td>29</td>
<td>Violence</td>
<td>165</td>
<td>Violence</td>
</tr>
<tr>
<td>29</td>
<td>Violence</td>
<td>166</td>
<td>Weapons</td>
</tr>
<tr>
<td>30</td>
<td>Weather</td>
<td>167</td>
<td>Weather</td>
</tr>
<tr>
<td>31</td>
<td>Always blocked</td>
<td>170</td>
<td>Child Abuse</td>
</tr>
<tr>
<td>32</td>
<td>Security Risks</td>
<td>128</td>
<td>Parked &amp; For Sale Domains</td>
</tr>
<tr>
<td>32</td>
<td>Security Risks</td>
<td>169</td>
<td>New Domains</td>
</tr>
<tr>
<td>32</td>
<td>Security Risks</td>
<td>177</td>
<td>Newly Seen Domains</td>
</tr>
<tr>
<td>34</td>
<td>CIPA</td>
<td>182</td>
<td>CIPA Filter</td>
</tr>
</tbody>
</table>
<h2 id="filtering-options">Filtering options</h2>
<h3 id="filter-traffic-by-resolved-ip-category">Filter traffic by resolved IP category</h3>
<p>When creating a DNS policy for security or content categories, you can optionally turn on <strong>Filter traffic by resolved IP category</strong> in the policy settings. When turned on, Gateway will block queries based on their resolved IP address in addition to the domain name. This setting may increase the number of false positives because domains in the blocked category can share IP addresses with legitimate domains.</p>
<h3 id="ignore-cname-domain-categories">Ignore <code>CNAME</code> domain categories</h3>
<p>The categories for a site's Canonical Name (<code>CNAME</code>) records may differ from its <code>A</code> record. For example, <code>blog.example.com</code> may be categorized under Personal Blogs, while <code>example.com</code> is categorized under Technology. To limit matches for a DNS policy to only the root domain's categories, turn on <strong>Ignore CNAME domain categories</strong>.</p>
<p>Regardless of this setting, <code>CNAME</code> domain categories will still appear in your Gateway <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> logs.</p>
<h2 id="categorization-process">Categorization process</h2>
<p>Cloudflare's domain categorization engine begins with multiple data sources, including:</p>
<ol>
<li>
<p>Cloudflare's proprietary data using our global network.</p>
</li>
<li>
<p>Third-party intelligence feeds. Cloudflare uses data from over 30 open-source intelligence feeds and premium commercial feeds, such as Avira and Zvelo.</p>
</li>
</ol>
<p>Then, the initial categorization is refined via:</p>
<ol start="3">
<li>
<p>Machine learning models. Our algorithms, including DGA Domains, DNS tunneling, and phishing detection models analyze patterns and behaviors to detect new and evolving threats.</p>
</li>
<li>
<p>Community feedback. Through a review process, Cloudflare assesses feedback by both our internal models and threat analysts. This ensures that our categorizations reflect the most current and accurate threat intelligence.</p>
</li>
</ol>
<h2 id="terraform">Terraform</h2>
<p>Terraform users can retrieve the category list with the <code>cloudflare_zero_trust_gateway_categories_list</code> data source. This allows you to create Gateway policies with the category's name rather than its numeric ID. For example:</p>
<pre><code class="language-tf">data &quot;cloudflare_zero_trust_gateway_categories_list&quot; &quot;categories&quot; {&#10;  account_id = var.cloudflare_account_id&#10;}&#10;&#10;locals {&#10;  main_categories_map = {&#10;    for idx, c in data.cloudflare_zero_trust_gateway_categories_list.categories.result :&#10;    c.name =&gt; c.id&#10;  }&#10;&#10;  subcategories_map = merge(flatten([&#10;    for idx, c in data.cloudflare_zero_trust_gateway_categories_list.categories.result : {&#10;      for k, v in coalesce(c.subcategories, []) :&#10;      v.name =&gt; v.id&#10;    }&#10;  ])...)&#10;}&#10;&#10;resource &quot;cloudflare_zero_trust_gateway_policy&quot; &quot;zt_block_dns_tech_categories&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;DNS Blocked&quot;&#10;  action     = &quot;block&quot;&#10;  traffic    = &quot;any(dns.content_category[*] in {${join(&quot; &quot;, [&#10;    local.main_categories_map[&quot;Technology&quot;],&#10;    local.subcategories_map[&quot;APIs&quot;],&#10;    local.subcategories_map[&quot;Artificial Intelligence&quot;],&#10;    local.subcategories_map[&quot;Content Servers&quot;],&#10;    local.subcategories_map[&quot;Translator&quot;]&#10;  ])}})&quot;&#10;}&#10;</code></pre>
