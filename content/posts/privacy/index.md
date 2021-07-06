+++
title = "The Importance of Privacy"
date = "2021-04-06"
tags = ["Privacy"]
summary = "Why your personal information is worth protecting."
+++

I have a friend; let's call him John. 

John works at a local engineering firm. A few years ago, he was asked to apply for a security clearance to work on confidential government contracts.

As you might expect, in preparation for his interview he was required to fill out a series of forms. These included his personal information, his employer information and, importantly, a list of all the online accounts registered to his email address.

At first, his interview went smoothly. An agent—who he describes as having an uncanny ability to 'see right through him'—probed him in detail about his past, his friends, and his occupation. Then, with a smirk, the man pulled up a photo from John's phone—a photo that shows him trespassing on private property, and told him to explain.

You see, my friend is more adventurous than rule-abiding. In his youth, he had a habit of illegally climbing local bridges and cranes. He was never caught and didn't brag about in on social media, but he did take plenty of pictures, each of which was automatically backed up to his Google account. Now, in order to assess his trustworthiness, the government had simply requested the personal data of each of his accounts and, without needing his password, had acquired unrestricted access to his data—including his emails, social media messages, and photo gallery.

- - -

The value of privacy has been forgotten. The mainstream belief is that only those like John—*criminals* like John—should fear the collection, distribution, and sale of their data. In contrast, I believe that privacy is a fundamental right. In this essay, I hope to show you that privacy is important, and that by making use of nearly any of the digital services we have come to rely on, you unknowingly consent to the collection, distribution, and sale of an enormous quantity of personal data—information that gives corporations and governments unprecedented ability to gain power over you.

# Data Brokers

Nowadays, everything you do online is tracked. For example:

- Your phone broadcasts your realtime location, even when [GPS](https://web.archive.org/web/20210531144313/https://qz.com/1131515/google-collects-android-users-locations-even-when-location-services-are-disabled/) [is disabled](https://krebsonsecurity.com/2019/12/the-iphone-11-pros-location-data-puzzler/). 
- Every purchase you make with a credit card is logged and [sold](https://www.forbes.com/sites/petercohan/2018/07/22/mastercard-amex-and-envestnet-profit-from-400m-business-of-selling-transaction-data/?sh=76e8ef467722) to advertisers. 
- Facebook keeps a record of everything you do, from the [time](https://web.archive.org/web/20200304031720/https://www.thesun.co.uk/tech/7508508/instagram-time-spent-photos-looking-stalking/) you spend looking at each post, to the [things you type out but never post](https://web.archive.org/web/20160611103102/http://www.wired.co.uk/article/facebook-is-tracking-what-you-dont-do), to your browsing history on websites they [don't own](https://web.archive.org/web/20210416223908/https://www.consumerreports.org/privacy/how-facebook-tracks-you-even-when-youre-not-on-facebook/) through an embedded tracking pixel. 
- Startups like [NumberEight](https://www.wired.com/story/companies-track-phones-movements-target-ads/) use the sensor data on your smartphone to infer your behaviour—like when you wake up and how you get to work—while [TVision](https://www.tvisioninsights.com/resources/mit-profile) uses your camera to "track how many people are watching, their attention level, even their emotions, all in real time."

What's more, this data is not siloed; it is distributed widely. For example, every time you visit an ad-enabled website, your information—including your location, a list of your interests, and the site's content categories[^1]— is sent to hundreds or thousands of different advertisers in a process known as [real-time-bidding](https://web.archive.org/web/20210501021338/https://developers.google.com/authorized-buyers/rtb/start#about-protocol-buffers). Each advertiser analyzes this data and then bids in a virtual auction for the available ad slots. Whether or not they win, they are each free to process, store, and even sell that information. 

This is perhaps not surprising. Nowadays, it is common knowledge that such information is collected, but most consider it to be a minor inconvenience. Yet what if this data is sensitive? Consider a few of the content categories—so-called [publisher verticals](https://web.archive.org/web/20210531021350/https://developers.google.com/adwords/api/docs/appendix/verticals)—that advertisers may target:

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


It is clear why those who browse such content may not want it recorded, yet it commonly is: sensitive information like the above is among the most sought after by *data-brokers*—companies whose business it is to aggregate data from different sources and link it to a person's identity. Experian and Acxiom, two of the largest such companies, maintain profiles of over [918 million](https://www.experianplc.com/media/2744/discover-experian-fy17.pdf) and [2.5 billion](https://marketing.acxiom.com/rs/982-LRE-196/images/Acxiom%20Global%20Data.pdf) citizens respectively. You do not have access to these profiles, but they do exist. Through a legal request, a New York Times reporter was able to access [hers](https://www.nytimes.com/2019/11/04/business/secret-consumer-score-access.html) from the data broker Sift. It was 400 pages long, and included a list of every time she opened certain apps and the contents of the every message she sent within.


Ultimately, the business of these companies is to allow advertisers to target particular demographics. Individuals are assigned to "market segments" and given scores based on different metrics. For example, Experian maintains an ["audience lookbook"](https://www.experian.com/content/dam/marketing/na/assets/ems/marketing-services/documents/product-sheets/audience-lookbook.pdf) of financial market segments. These segments range from "Secure, Savvy Credit User" to "Insecure Debt Dependent"—consumers who are "concerned about the possibility of losing a home" and who "tend to live beyond their means". Another of their products, [Connect](https://web.archive.org/web/20171228185848/https://www.experian.com/connect/medical-financing-view-credit-report-and-score-of-patients.html), scores patients based on their predicted ability to repay their hospital bills. "Before you begin a medical procedure and extend them financing, be more informed about your patient's financial situation," the tagline reads.


As a credit reporting company, Experian has access to your payment history, allowing them to make these judgments with at least a plausible degree of accuracy. It becomes more dangerous, however, when relevant information is sparse and brokers must extrapolate from whatever data is available. Experian's main competitor, Equifax, recently began [purchasing](https://www.youtube.com/watch?v=3KeycN_50ac) customer data from *cell service providers* in Latin America—including "call duration, time calls are made, who initiates a call or test, numbers frequently called" to "help predict people's willingness and ability to repay a loan or propensity to respond to a marketing offer". 

This example is not isolated. Facebook has [filed](https://patents.google.com/patent/US9100400B2/en) a patent to predict a user's credit-worthiness based on their list of friends. [Cornerstone](https://www.cornerstoneondemand.com/), a company that uses analytics to score job applicants, considers a huge number of factors including [browser-choice](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/#easy-footnote-bottom-28) (those who use Chrome or Firefox score higher those who use Safari).


Data brokers hoard information: buying and selling any and all user data they can get their hands on. They then use machine learning algorithms to find patterns and trends in that data with which they can score users. Because these trends are broadly accurate, they profit enormously. In a recent [survey](https://www2.deloitte.com/us/en/insights/focus/human-capital-trends/2017/people-analytics-in-hr.html), 71% of companies reported using "people analytics" services like Cornerstone to determine who to hire and how much to pay them. Yet the result is an asymmetry of information and ultimately of power: we as consumers do not have access to the data and the algorithms that determine the loans we are granted and the job offers we receive. When this data is false, we cannot correct it because it does not belong to us. When this data is based on biased metrics, these algorithms only serve to reinforce these biases. For example, if a population is predicted to be financially irresponsible because of those they phone or who they befriend on Facebook, they will only be driven to further desperation. As the authors of the excellent paper [The Datafication of Employment](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/) put it eloquently, "Reputational scores based on historical data reify the lopsided structure of American society, further advantaging the already advantages and marginalizing the marginalized." In the end, it is the responsibility of the government to put in place regulations that limit the predatory surveillance of its citizens. Unfortunately, however, it is they who surveil us the most.
<!-- # It never goes away -->

<!-- Perhaps you find the violation of privacy a small price to pay for the convenience of modern services. However, given that data is rarely deleted, do you trust that it will *never* be misused? In 1999, the data broker Docusearch [sold](https://epic.org/privacy/boyer/) the social security number and work address of twenty year-old Amy Boyer to a young man for $154. He later drove to her work and shot her.  -->

<!-- What's more, data breaches are common. In 2017, Equifax was hacked: the social security numbers of 143 million Americans and the credit card numbers of 200,000 Americas were [accessed](https://en.wikipedia.org/wiki/2017_Equifax_data_breach). If you use Facebook, your phone number is likely publicly available because of [poor security](https://www.businessinsider.com/stolen-data-of-533-million-facebook-users-leaked-online-2021-4). -->


# The Government

In 2013, Edward Snowden famously revealed the extent of the US surveillance program. He showed how through ongoing programs like [PRISM](https://abcnews.go.com/blogs/politics/2013/07/glenn-greenwald-low-level-nsa-analysts-have-powerful-and-invasive-search-tool), analysts could "listen to whatever emails they want, whatever telephone calls, browsing histories [etc.]" with "no need to go to a court". That the NSA, a branch of the military, had [direct access](https://www.theguardian.com/world/2013/jun/06/us-tech-giants-nsa-data) to the servers of companies like Google, Facebook, Apple, and Microsoft.

This collection was likely [unconstitutional](https://www.washingtonpost.com/opinions/nsa-surveillance-may-be-legal--but-its-unconstitutional/2013/06/21/b9ddec20-d44d-11e2-a73e-826d299ff459_story.html), but was justified as an essential measure to protect national security. Yet it is demonstrably clear that this information is being used for more than just counter-terrorism. This year, Motherboard [reported](https://www.vice.com/en/article/y3g97x/location-data-apps-drone-strikes-iowa-national-guard) that the Iowa National Guard, a military unit that carries out international drone strikes, purchased the realtime location data of millions of unsuspecting smartphone users from the data broker Babel Street. This data is sourced from thousands of apps with built-in tracking SDKs, including the popular [prayer app](https://www.vice.com/en/article/jgqm5x/us-military-location-data-xmode-locate-x) Muslim Pro, which purports to have over [105 million](https://www.muslimpro.com/) downloads.

Like many others my age, my mistrust of the government is growing. I do not believe that they always have my best intentions at heart, and I certainly do not trust them to safeguard my most personal information. For example, what if those with access to my friends personal photos had malicious intentions? In his biography *Permanent Record*, Snowden recalls how during his time at the NSA, analysts would trade the intercepted nudes of women as a kind of "informal office currency" while "reading their emails, listening in on their phone calls, and stalking them online". 

Such abuses of power are not the exception. History shows that those with authority naturally seek further control. With every secret surveillance program we inch closer to authoritarian systems like that of [China](https://en.wikipedia.org/wiki/Social_Credit_System#Examples_of_policies), where misdemeanours like [eating on the train](http://politics.people.com.cn/n1/2019/0515/c1001-31086953.html) or spreading ["misinformation"](https://web.archive.org/web/20191109012259/https://credit.suzhou.com.cn/news/show/22296.html) on social media might lower your credit score and blacklist you from [travelling or enrolling your children in better schools.](https://www.vox.com/the-goods/2018/11/2/18057450/china-social-credit-score-spend-frivolously-video-games) While a similar government-sponsored social credit score may not be implemented in North America for years, we should be careful: data is never deleted. When you consent to surveillance, you consent not only to the handling of your data by those currently in power, but also all those who will gain power in the future. 

Worst of all, it is nearly impossible to participate in today's society without consenting to the sale of your personal information. Every bank, social media service, and cell phone carrier requires you to accept cryptic privacy policies. Even if you don't accept, governments have given themselves the power to collect your data in secret. Simply, to opt out of surveillance is akin to opting out of electricity—possible only in theory.

# What we can do

It doesn't have to be this way.

Targeted advertisements are not evil. It makes sense that the contents of a search, or a user's approximate location, be used to increase the relevance of the ads they see.

What is evil is for your precise location, your purchase history, and your health information be collected, shared among companies, and algorithmically scrutinized to make judgments about your character that may not be correct. For that data to be collected by the government and stored in their servers indefinitely.

Unfortunately, for-profit companies are contractually obligated to pursue profit at any cost. As the court of Delaware (where most tech companies are incorporated) makes [clear](https://www.weil.com/-/media/files/pdfs/2018/fiduciary-duties-of-corporate-directors-in-uncertain-times.pdf):

> The board of directors of a for-profit corporation must, within the limits of its legal discretion, treat stockholder welfare as the only end, considering other interests only to the extent that doing so is rationally related to stockholder welfare.

Consequently, we are dependant upon the government to regulate the data companies collect and how they use it. However, because the government has a vested interest in maintaining the status quo, it is our responsibility to apply political pressure and demand the following regulations:

1. All data collection should be *opt-in*. Users should be able to choose exactly what they share and be told exactly how that data will be used.

2. Companies should not be able to punish users who do not opt-in, for example by charging extra for privacy.

3. Users should have the right to view any data that a service stores about them, be able to download a machine-parsable copy of that data, and request for it to be deleted at any time.

4. Like lawyers and doctors, companies should be bound to fiduciary rules that outline the care they must take in storing user data.

5. When all else fails, users should have the right to pursue legal action against companies who violate the above laws if the government does not have the means to do so. This is called "private right of action".

These are only a few of what I consider to be the most important privacy regulations. For a more complete list, visit the [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2019/06/effs-recommendations-consumer-data-privacy-laws), the most influential organization in the fight against mass surveillance.

# In sum

In the end, John was granted the clearance. The agent was sympathetic: John explained that he was smarter now, that his actions were a product of an irresponsible youth and that he had long since stopped trespassing. Yet the incident was still troubling. It is obvious that inconsequential mistakes of the past have the right to be forgotten and that such surveillance amplifies imbalances of power.

Even so, privacy is not simply about hiding data that betrays wrongdoing, but about protecting it from the wrongdoing of others.  Those who seek to collect your data do so to gain power over you, and to protect it is to assert your independence. Companies profit massively from the exploitation of your most sensitive information—your beliefs, secrets, and fears—and the government is complicit. To think that these companies are responsible arbiters of our most sensitive information is naive and dangerous.

Privacy is healthy. Privacy blinds the system, forces these institutions to treat us fairly and impartially, and preserves our autonomy. It ensures that mistakes from the past are forgotten and that conflicting opinions are allowed to breed in spaces free from surveillance.

I want to live in a world where I can take a picture on my phone without it being brought up in an interview or share secrets with a loved one in confidence. When I know that my every move is being watched, I become tired and afraid. I no longer want to express myself in my freest capacity or share an opinion that may lose me points on an invisible scoreboard that determines my future.

I want the right to be forgotten.

# Read some more

- [Corporate Surveillance in Everyday Life](https://crackedlabs.org/dl/CrackedLabs_Christl_CorporateSurveillance.pdf) is an excellent overview of the topic by an independent Austrian researcher.

- [Privacy is Power](https://www.goodreads.com/en/book/show/51781479) is an equally fantastic book about privacy written by Carissa Véliz, a philosophy professor at Oxford.

- [The Datafication of Employment](https://tcf.org/content/report/datafication-employment-surveillance-capitalism-shaping-workers-futures-without-knowledge/#easy-footnote-bottom-17) is an incredibly well-written paper on the use of "people analytics" algorithms in hiring and compensation decisions.

- Anything written by the [Electronic Frontier Foundation](https://www.eff.org/), a bastion of light in a backward world.
