+++
title = "The Importance of Privacy"
date = "2021-04-06"
tags = ["Privacy"]
summary = "Why your personal information is worth protecting."
+++

I have a friend; let's call him John. 

A few years ago, John interned at a local engineering firm and was asked to apply for a Canadian security clearance to work on confidential projects.

An agent—who he describes as having an uncanny ability to 'see right through him'—questioned him for half a day. Like you might expect, the man probed him in detail about his past, his friends, and his occupation. Then, with a smirk, he pulled up a photo that John had taken on his phone years ago and accused him of trespassing.

You see, John is more adventurous than rule-abiding. In his youth, he had a habit of illegally climbing local bridges and cranes. He was never caught and didn't brag about in on social media, but he did take plenty of pictures. Yet in preparation for his interview, he had been required to submit a list of all his online accounts. Unbeknownst to him, the government had then requested his personal data from each of these companies and acquired unrestricted access to his emails, social media messages, and photo gallery. In the end, he was granted the clearance, but only after having to justify the contents of his online private life in excruciating detail.

To be fair, it's hard to feel sympathy for him. He knowingly trespassed on private property and got caught for it. Yet I am still troubled by the ease with which CSIS were able to access his private photos. You may not want to share your photos, even if they betray no criminal activity. For example, what if those with access to his data had had malicious intentions? In his autobiography *Permanent Record*, whistleblower Edward Snowden recalls how during his time at the NSA, analysts would trade the intercepted nudes of women as a kind of "informal office currency" while "reading their emails, listening in on their phone calls, and stalking them online". While this scenario is perhaps unlikely, everyone values their privacy. If you don't believe me, ask yourself this: would you be willing to share your medical records, personal photos, or credit card information online? Most likely not—it's obvious that doing so would put you at risk of abuse. Yet by making use of nearly any of the digital services we have come to rely on in today's day and age, you unknowingly consent  to the collection, distribution, and sale of an enormous quantity of personal data—information that gives corporations and governments unprecedented ability to gain power over you.


# Data Brokers

Consider the case of [real-time-bidding](https://web.archive.org/web/20210501021338/https://developers.google.com/authorized-buyers/rtb/start#about-protocol-buffers). Every time you visit an ad-enabled website, your information—including your location, your unique advertising ID, a list of your interests, and the site's content categories[^1]— is sent to hundreds or thousands of different advertisers.  Each advertiser analyzes this data and then bids in a virtual auction for the available ad slots. Whether or not they win, they are each free to process, store, and even sell that information to *data-brokers*, companies whose business it is to aggregate data from different sources and link it to a person's identity.

We all know that our information is being collected and sold, but few understand the consequences of doing so. To illustrate, here are a few of the content categories mentioned above—known as [publisher verticals](https://web.archive.org/web/20210531021350/https://developers.google.com/adwords/api/docs/appendix/verticals)—that advertisers may target:

{{<table>}}
| Criterion ID | Category                                                                        |
|--------------|---------------------------------------------------------------------------------|
| 113          | /People & Society/Ethnic & Identity Groups/Lesbian, Gay, Bisexual & Transgender |
| 640          | /Health/Mental Health/Depression                                                |
| 625          | /Health/Health Conditions/AIDS & HIV                                            |
| 647          | /Health/Reproductive Health/Infertility                                         |
| 677          | /People & Society/Disabled & Special Needs                                      |
{{</table>}}


[^1]: There are two different major RTB protocols in use, OpenRTB and Google Authorized Buyers, whose specifications can be found [here](https://web.archive.org/web/20210531024917/https://developers.google.com/authorized-buyers/rtb/realtime-bidding-guide) and [here](https://web.archive.org/web/20210531031340/https://www.iab.com/wp-content/uploads/2016/03/OpenRTB-API-Specification-Version-2-5-FINAL.pdf) respectively.

It is clear why those who browse such content may not want it recorded, yet it almost always is: sensitive information like the above is among the most sought after data used by these companies to build profiles of everyone with an online presence.  You do not have access these profiles, but they do exist. Acxiom and Experian, two of the largest data brokers, maintain databases of over [2.5 billion](https://marketing.acxiom.com/rs/982-LRE-196/images/Acxiom%20Global%20Data.pdf) and [918 million](https://www.experianplc.com/media/2744/discover-experian-fy17.pdf) citizens respectively. Through a legal request, a New York Times reporter was able to [access](https://www.nytimes.com/2019/11/04/business/secret-consumer-score-access.html) her profile from one such company, [Sift](https://sift.com/). It was 400 pages long, and included a list of every time she opened certain apps and the contents of the every message she sent within.

These companies collect data from a variety of sources. For example, your phone broadcasts your realtime location, even when [location services](https://web.archive.org/web/20210531144313/https://qz.com/1131515/google-collects-android-users-locations-even-when-location-services-are-disabled/) [are disabled](https://krebsonsecurity.com/2019/12/the-iphone-11-pros-location-data-puzzler/). Every purchase you make with a credit card is logged. Facebook keeps a record of everything you do, from the [time](https://web.archive.org/web/20200304031720/https://www.thesun.co.uk/tech/7508508/instagram-time-spent-photos-looking-stalking/) you spend looking at each post to your [self-censorhip](https://web.archive.org/web/20160611103102/http://www.wired.co.uk/article/facebook-is-tracking-what-you-dont-do) (the things you write out but never say). They even track your browsing on websites they don't own through an embedded [tracking pixel](https://web.archive.org/web/20210416223908/https://www.consumerreports.org/privacy/how-facebook-tracks-you-even-when-youre-not-on-facebook/). While we can't know exactly what happens to our data—it doesn't belong to us—it is almost always sold.

Ultimately, the business of these companies is to allow advertisers to target particular demographics. Individuals are assigned to "market segments" and given scores based on different metrics. For example, Experian maintains an ["audience lookbook"](https://www.experian.com/content/dam/marketing/na/assets/ems/marketing-services/documents/product-sheets/audience-lookbook.pdf) of financial market segments. These segments range from "Secure, Savvy Credit User" to "Insecure Debt Dependent"—consumers who are "concerned about the possibility of losing a home" and who "tend to live beyond their means". Another of their products, [Connect](https://web.archive.org/web/20171228185848/https://www.experian.com/connect/medical-financing-view-credit-report-and-score-of-patients.html), scores patients based on their predicted ability to repay their hospital bills. "Before you begin a medical procedure and extend them financing, be more informed about your patient's financial situation," the tagline reads.


As a credit reporting company, Experian has access to your payment history, allowing them to make these judgments with at least a plausible degree of accuracy. It becomes more dangerous, however, when relevant information is sparse and brokers must extrapolate from whatever data is available. Experian's main competitor, Equifax, recently began [purchasing](https://www.youtube.com/watch?v=3KeycN_50ac) customer data from *cell service providers* in Latin America—including "call duration, time calls are made, who initiates a call or test, numbers frequently called" to "help predict people's willingness and ability to repay a loan or propensity to respond to a marketing offer". 

This example is not isolated. Facebook has [filed](https://patents.google.com/patent/US9100400B2/en) a patent to predict a user's credit-worthiness based on their list of friends. [Cornerstone](https://www.cornerstoneondemand.com/), a company that uses analytics to score job applicants, considers a huge number a factors including [browser-choice](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/#easy-footnote-bottom-28)—those who use Chrome or Firefox are preferred to those who use Safari. 

This trend is becoming increasingly common—in a recent  [survey](https://www2.deloitte.com/us/en/insights/focus/human-capital-trends/2017/people-analytics-in-hr.html), 71% of companies reported using "people analytics" services like Cornerstone to determine who to hire and how much to pay them. Data brokers hoard information: buying and selling any and all user data they can get their hands on. They then use machine learning algorithms to find patterns and trends in that data with which they can score users. Because these trends are broadly accurate, they profit enormously. Yet the result is an asymmetry of information and ultimately of power: we as consumers do not have access to the data and the algorithms that determine the loans we are granted and the job offers we receive. When this data is false, we cannot correct it because it does not belong to us. When this data is based on biased metrics, these algorithms only serve to reinforce these biases. For example, if a population is predicted to be financially irresponsible because of those they phone or who they befriend on Facebook, they will only be driven to further desperation. As the authors of the excellent paper [The Datafication of Employment](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/) put it eloquently, "Reputational scores based on historical data reify the lopsided structure of American society, further advantaging the already advantages and marginalizing the marginalized."

# It never goes away

Perhaps you find the violation of privacy a small price to pay for the convenience of modern services. However, given that data is rarely deleted, do you trust that it will *never* be misused? In 1999, the data broker Docusearch [sold](https://epic.org/privacy/boyer/) the social security number and work address of twenty year-old Amy Boyer to a young man for $154. He later drove to work and shot her. What 's more, data breaches are common. In 2017, Equifax was hacked. The social security numbers of 143 million Americans and the credit card numbers of 200,000 Americas were [accessed](https://en.wikipedia.org/wiki/2017_Equifax_data_breach). This data was not sold—the breach was likely political in motivation—but it could have, and the consequences would have been devastating.

<!-- Numbers don’t lie. <Sift> -->

In the end, it should be the responsibility of the government to put in place regulations that limit the predatory surveillance and algorithmic scoring of its citizens, yet sadly it is they who have often proved to do so the most.

# The Government

In 2013, Edward Snowden famously revealed the extent of the US surveillance program. He showed how through ongoing programs like [PRISM](https://abcnews.go.com/blogs/politics/2013/07/glenn-greenwald-low-level-nsa-analysts-have-powerful-and-invasive-search-tool), analysts could "listen to whatever emails they want, whatever telephone calls, browsing histories [etc.]" with "no need to go to a court". That the NSA, a branch of the military, had [direct access](https://www.theguardian.com/world/2013/jun/06/us-tech-giants-nsa-data) to the servers of companies like Google, Facebook, Apple, and Microsoft.

This collection was likely [unconstitutional](https://www.washingtonpost.com/opinions/nsa-surveillance-may-be-legal--but-its-unconstitutional/2013/06/21/b9ddec20-d44d-11e2-a73e-826d299ff459_story.html), but was justified as an essential measure to protect national security. Yet it is demonstrably clear that this information is being used for more than just counter-terrorism. This year, Motherboard [reported](https://www.vice.com/en/article/y3g97x/location-data-apps-drone-strikes-iowa-national-guard) that the Iowa National Guard, a military unit that carries out international drone strikes, purchased from the data broker Babel Street the realtime location data of millions of unsuspecting smartphone users from around the world. This data is sourced from thousands of apps with built-in tracking SDKs, including the [prayer app](https://www.vice.com/en/article/jgqm5x/us-military-location-data-xmode-locate-x) Muslim Pro, which purports to have over [105 million](https://www.muslimpro.com/) downloads.

Like many others my age, my mistrust of the government is growing. I do not believe that they always have my best intentions at heart, and I certainly do not trust them to safeguard my most personal information. We are edging ever closer to authoritarian social credit systems like that of [China](https://en.wikipedia.org/wiki/Social_Credit_System#Examples_of_policies), where misdemeanours like [eating on the train](http://politics.people.com.cn/n1/2019/0515/c1001-31086953.html) or spreading ["misinformation"](https://web.archive.org/web/20191109012259/https://credit.suzhou.com.cn/news/show/22296.html) on social media might lower your credit score and blacklist you from [travelling or enrolling your children in better schools.](https://www.vox.com/the-goods/2018/11/2/18057450/china-social-credit-score-spend-frivolously-video-games) When you consent to surveillance, you consent not only to the handling of your data by those currently in power, but also all those who will gain power in the future. 

# You can't opt out

Worst of all, it is nearly impossible to participate in today's society without consenting to the sale of your personal information. The argument, "if you don't like it, don't use it" does not hold in a world where I attend classes on Zoom and depend on Microsoft for my job. And I have it good: schools and workplaces around the world are using the pandemic to justify the introduction Orwellian [surveillance](https://www.eff.org/deeplinks/2020/02/schools-are-pushing-boundaries-surveillance-technologies) [technologies](https://www.eff.org/deeplinks/2020/06/inside-invasive-secretive-bossware-tracking-workers). Simply put, to opt out of these services feels akin to opting out of electricity—possible in theory, but not without making real sacrifices.

# What we can do

It doesn't have to be this way.

Targeted advertisements are not evil. It makes sense that the contents of a search, or a user's approximate location, be used to increase the relevance of the ads they see. That's not evil. 

What is evil is for your precise location, your purchase history, and your health information be collected, shared among companies, and algorithmically scrutinized to make judgments about your character that may not be correct. For that data to be collected by the government and stored in perpetuity.

Unfortunately, for-profit companies are contractually obligated to pursue profit at any cost. As the court of Delaware (where most tech companies are incorporated) makes [clear](https://www.weil.com/-/media/files/pdfs/2018/fiduciary-duties-of-corporate-directors-in-uncertain-times.pdf):

> The board of directors of a for-profit corporation must, within the limits of its legal discretion, treat stockholder welfare as the only end, considering other interests only to the extent that doing so is rationally related to stockholder welfare.

Unfortunately, we are dependant upon the government to protect us from the abuses of these companies. We need to hold them accountable to put in place *regulations* that protect our rights.
Here's what needs to be done:

1. You should own your data and be able to choose what you share. You should be informed about the information that companies collect and have the ability to correct it when it is false. 

2. You should be informed as to how this data is used. Your profiles should be available to you

3. Governments should not be able to access your data without a warrant.

<!-- The more you realize you're being watched, the more pressure you feel to act like a model citizen at all times. This leads to a [chilling effect](https://en.wikipedia.org/wiki/Chilling_effect), where citizens are afraid to exercise their fundamental rights—like the right to protest—for fear of prosecution. -->


# In sum

Put simply, those who seek to collect your data do so to gain power over you, and to protect it is to assert your independence. Companies profit massively from the exploitation of your most sensitive information—your beliefs, secrets, and fears—and the government is complicit. These institutions build extremely detailed profiles of our lives to predict and influence our behaviour without regard for the bias and accuracy of that information. 

Privacy is healthy. Privacy blinds the system, forces these institutions to treat us fairly and impartially, and preserves our autonomy. It ensures that mistakes from the past are forgotten and that conflicting opinions are allowed to breed in spaces free from surveillance.

I want to live in a world where I can take a picture on my phone without it being brought up in an interview or share secrets with a loved one in confidence. When I know that my every move is being watched, I become tired and afraid. I no longer want to express myself in my freest capacity or share an opinion that may lose me points on an invisible scoreboard that determines my future.

> When surveillance is everywhere, it becomes safer to keep quiet, or to echo the opinions that others accept. But society progresses through listening to the arguments of those who are critical, those who rebel against the status quo.
><br> — Carissa Véliz, *Privacy is Power*

# Read some more

- [Corporate Surveillance in Everyday Life](https://crackedlabs.org/dl/CrackedLabs_Christl_CorporateSurveillance.pdf) is an excellent overview of the topic by an independent Austrian researcher.

- [Privacy is Power](https://www.goodreads.com/en/book/show/51781479) is an equally fantastic book about privacy written by Carissa Véliz, a philosophy professor at Oxford.

- [The Datafication of Employment](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/#easy-footnote-bottom-17) is an incredibly well-written paper on the use of "people analytics" algorithms in hiring and compensation decisions.


<!-- they can use it to selectively grant and deny you opportunities, without ever telling you why. Sift believes that [numbers don't lie](https://sift.com/products/payment-protection). -->

<!-- The authors of the excellent paper [The Datafication of Employment](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/) put it eloquently: "Those identified as financially desperate receive ads for predatory loan products and for-profit colleges, while those identified as affluent are targeted for high-paying jobs and low-interest banking products." -->

<!-- It means that you don't object to the police reading any of your personal messages to find evidence of crime. It means that you find it reasonable for your employer to know your financial history, political beliefs, or medical records. -->

<!-- https://www.nytimes.com/2019/07/23/us/politics/william-barr-encryption-security.html -->

<!-- to think that these companies are responsible arbiters of our most sensitive information is naive and dangerous. -->
