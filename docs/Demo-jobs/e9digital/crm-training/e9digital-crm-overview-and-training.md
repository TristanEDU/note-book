# e9digital CRM Overview & Training

This note summarizes the CRM implementation process, internal testing, and client training planning.

---
## From `crm-implementation-notes.md`

# CRM Implementation - Technical Objectives

## High-Level Goals
- Deploy and configure GoHighLevel (GHL)
- Integrate GHL with WordPress
- Build attribution and tracking systems for marketing campaigns

## Functional Requirements
- Contact forms with spam filtering (non-sales leads)
- CRM setup with stages and pipeline
- Drip email campaigns for sales follow-up
- Prospect activity tracking (email opens, link clicks, site visits)

## Data & Metrics
- Import marketing and sales cost data
- Track:
  - Cost per Lead (CPL)
  - Cost per Sale (CPS)
  - Lead-to-Sale %, Proposal-to-Sale %
  - Revenue and ROI per campaign

## Reporting
- Dashboard views for all key campaign and prospect activities
- Affiliate tracking and commission calculations (research GHL’s affiliate features)

## Potential Expansion
- If successful, project may be **white-labeled** and offered to e9digital clients

## Additional Considerations
- No existing systems to migrate
- Marketing ops built from the ground up

---

## From `Day-one-test.md`

# GoHighLevel Day 1 Knowledge Test & Review

## 🧪 Knowledge Test Walkthrough

Each question was answered in real time. Your response is followed by a corrected/enhanced version to solidify understanding.

---

### **Question 1**

**Prompt:** What are the core components of the GoHighLevel platform, and how would you explain its value proposition to a non-technical client like e9digital?

**Your Answer:**\
GoHighLevel is a CRM platform. Its core components are marketing management, sales management, conversion tracking, automation, integrated customer communication, brand reputation management.

**Correct Answer:**\
GoHighLevel is an all-in-one sales and marketing platform. Its core components include:

- CRM & Pipeline Management
- Marketing Automation (email/SMS/workflows)
- Funnel & Website Builder
- Reputation Management
- Two-Way Communication
- Appointment Scheduling
- Attribution & Campaign Tracking
- White-labeling for agencies

**Client-Facing Summary:**\
"It simplifies and unifies all your sales and marketing operations in one place, saving you time, improving client communication, and increasing lead conversion."

---

### **Question 2**

**Prompt:** Walk me through how you would set up a lead capture form that tracks the marketing source and automatically adds the lead to a pipeline.

**Your Answer:**\
I would use the integrated form builder inside of GHL to build the form and I would have a question asking where the lead learned about the company.

**Correct Answer:**

- Use the form builder with hidden UTM fields (source, medium, campaign)
- Embed on funnel or WP site
- Trigger a workflow on submission
  - Add to pipeline
  - Tag lead
  - Set custom fields

---

### **Question 3**

**Prompt:** How does GoHighLevel handle marketing attribution, and how would you set it up to track whether a lead came from Google Ads, Facebook, or organic search?

**Your Answer:**\
It can integrate Google Analytics as well as other attribution tools and present them to you cleanly.

**Correct Answer:**

- Use UTM links in ad traffic
- Capture via hidden form fields
- Store data in custom fields
- Tag contacts or update workflows accordingly
- Use reporting tab for attribution overview

---

### **Question 4**

**Prompt:** Explain how GHL's pipeline and opportunity stages work. How would you use them to track and manage a lead's journey from first contact to closed sale?

**Your Answer:**\
When a client is put into the pipeline either manually or as a result of an automation, they are moved along based on further interactions and actions.

**Correct Answer:**

- Create custom stages (e.g., New → Contacted → Proposal Sent → Closed)
- Automate pipeline entry via workflows
- Manually or automatically move based on lead actions
- Use filters and reporting for deal forecasting

---

### **Question 5**

**Prompt:** What’s the difference between a campaign and a workflow in GoHighLevel, and which should you use for building a drip email sequence?

**Your Answer:**\
A campaign is a targeted sequence of ads. A workflow is a reactive series of steps.

**Correct Answer:**

- Campaign = legacy tool for linear drip (email/SMS)
- Workflow = visual logic builder (preferred)
- Use workflows for modern sequences with triggers, delays, and branching logic

---

### **Question 6**

**Prompt:** How would you integrate GoHighLevel with WordPress so that form submissions and calendar bookings push into GHL?

**Your Answer:**\
I would embed forms created in the GHL form builder directly into the WP site whenever possible, and when not I would use webhooks and Zapier.

**Correct Answer:**

- Preferred: GHL embed codes for forms/calendars
- Alternative: Zapier or webhooks with WP plugins
- Optionally use GHL WordPress plugin for easier embed management

---

### **Question 7**

**Prompt:** A lead books a call through the embedded calendar. What should happen automatically afterward?

**Your Answer:**\
I would automate a confirmation/welcome email and potentially an SMS. Then I would move them into the booked call stage of the pipeline.

**Correct Answer:**

- Confirmation email & SMS
- Move to pipeline stage: Booked
- Tag contact
- Notify internal team
- Set reminders before the call

---

### **Question 8**

**Prompt:** What are the minimum custom fields you would create to support attribution and automation inside a new GHL setup?

**Your Answer:**\
I am not sure.

**Correct Answer:**

- utm_source, utm_medium, utm_campaign
- Lead Source
- Referring URL
- GCLID
- Booked Call Date
- Owner or Assigned Rep

---

### **Question 9**

**Prompt:** What’s the purpose of tags in GHL, and how would you use them differently from custom fields or contact statuses?

**Your Answer:**\
Tags can indicate the purpose or status of a contact. Example: cold leads, or high-priority leads.

**Correct Answer:**

- Tags = temporary, stackable labels for segmentation or automation
- Custom fields = structured data (email, lead source)
- Contact status = global status (e.g., customer, prospect)

---

### **Question 10**

**Prompt:** What metrics would you monitor weekly to evaluate whether GHL is driving ROI for a company like e9digital?

**Your Answer:**\
I would monitor things like GHL funnels and landing pages, tracking things like conversions and new leads.

**Correct Answer:**

- New leads and source
- Funnel conversion rate
- Booked calls
- Pipeline movement
- Closed deals
- No-show rate
- Email/SMS performance

---

## 📊 Insights & Areas for Improvement

### ✅ Strengths:

- Strong working understanding of the platform and core terminology
- Solid mental model of how leads move through funnels and automations
- Accurate intuition on form building and integration techniques

### ⚠️ Suggested Improvements:

#### 1. Custom Fields & Attribution Tracking

**Resource:** [Using Custom Fields](https://help.gohighlevel.com/support/solutions/articles/48001161579-how-to-use-custom-fields)\
**Fix:** Practice creating custom fields and mapping UTM parameters into workflows.

#### 2. Workflow Logic Mastery

**Resource:** [How to Use Workflows](https://help.gohighlevel.com/support/solutions/articles/155000001701-how-to-use-workflows-in-gohighlevel)\
**Fix:** Set up test workflows with branching logic and internal notifications.

#### 3. Pipeline & Sales Stage Reporting

**Resource:** [Step-by-Step Guide to Pipelines](https://help.gohighlevel.com/support/solutions/articles/155000001985-step-by-step-guide-creating-pipelines)\
**Fix:** Build a mock pipeline with real-world stages and test filtering by value and source.

#### 4. ROI Tracking

**Resource:** [Understanding Attribution Source](https://help.gohighlevel.com/support/solutions/articles/48001219997-understanding-attribution-source-ad-reporting-)\
**Fix:** Practice using the attribution report tab and building UTM-tagged funnels.

---

## From `e9digital-overview.md`

# e9digital - Project Overview

## Client
- **Name:** Conrad Strabone
- **Company:** e9digital
- **Website:** [https://e9digital.com](https://e9digital.com)

## Context
- Scheduled Meeting: **Tuesday, May 13 at 8:30 AM EST**
- Initial contact via Upwork.
- Likely seeking a **contract-based** implementer (not enterprise scale).
- May pursue **white-label CRM** solution if the implementation is successful.

## Current Tools in Use
- **Google Analytics**
- **Google Search Console**
- **CallRail**

## Intentions
- New implementation, **no legacy systems** in place.
- Seeking to **build marketing infrastructure** and sales pipeline from scratch.

---

## From `gohighlevel-client-training-plan.md`

# 🧠 In-Depth Training Plan for Client Call (GoHighLevel + Marketing Systems)

## 📅 3-Day Intensive Schedule

---

## 📆 Day 1: GoHighLevel CRM & Marketing Attribution

### 🎯 Objective:
Understand GoHighLevel's CRM functionalities and grasp marketing attribution models.

### 📚 Modules

#### GoHighLevel CRM Overview
- 🎥 [GoHighLevel Tutorial For Beginners 2024 (Software Overview)](https://www.youtube.com/watch?v=ujvIXXH8Utc)
	- General intro to Highlevel and explination of it's capabilities
- 🎥 [How To Use GoHighLevel as a CRM (HighLevel CRM Tutorial 2024)](https://www.youtube.com/watch?v=hdUnbmynQN0)
	- Just a Overview
- 📖 [2024 Go High Level Tutorial For Beginners – Streamline Results](https://streamlineresults.com/go-high-level-tutorial-for-beginners/)
	- Basic tutorial on setup and basic functions

#### Marketing Attribution Models
- 📖 [Marketing Attribution Guide – NoGood](https://nogood.io/2024/08/07/marketing-attribution/)
	- Marketing attribution is what helps marketers and bussiness understand how and what contributed to a given sale and their sales in general. This allows them to fine tune their marketing stratigies
	- It also helps them see how their marketing efforts contribute to the main goals of the company
	- some of the key roles are:
		- Aligning sales and marketing: 59% of businesses believe that aligning sales and marketing is the primary goal of marketing attribution. This is because attribution helps determine the influence of multiple marketing and sales activities across the customer journey and defines credit at each touchpoint.
		- Optimizing marketing spend: This helps the company understand where they should point their marketing buget.
		- Enhancing Customer Experience: this helps them understand the marketing journey and when and where to place key touch points
		- Mearuring ROI
	- Types of Attribution Data:
		- Software based data relies on digital metrics and touch points to monitor user interaction this can be really granular and detailed but will also miss a lot of non digital indicators
		- Self Reported Data is the data that the consumer reports generaly in the form of surveys or questionairs. This data is very usfull as it can provide insitght into what the customer thinks effected him or her and also non digital indicators such as word-of-mouth and phisical advertisment. It is howver in general very inaccurate due to bias's and other factors.
		- Hybrid Data is a mix of the two previous catagories. leading to grater acuracy and scope however it can be very diffacult to implement this well.
	- Single Touch atribution models:
		- First Touch: is where the first interaction a customer has with your marketing (*such as visiting your website or clicking on a facebook post*) is given 100% of the credit for the conversion. This is great for identifying which channesl lead to the most brand awarness however they to not take any of the middle or final steps into acount which can be detrimental if the first step is not the crucial one in the customer journey
		- Last Touch: Considers only the last interaction of the user befor the conversion which is good for understanding how to push users over the edge on converting however if it is soley used it can lead to short sighted ness and missing brandawarness opportunities as it does not account for any of the leadup steps...
	- Multi Touch attribution models:
		- Linear Touch: Gives equal credit to all the steps in a customer journey for the conversion. This is good for getting a clear view of how the costomer interacted but can be faulty if it has incomplete information suchas the use of multiple devices and it does not take into account how things like seasonal channeles affect things.
		- Time Decay: This gives more weight to a touch point the closer it is in the journey to the conversion. It is prone to issues due to the fact that it does not consider the affect of the initial efforts and is generaly only good for B2B marketing.
		- U Shaped model: This gives 40% to the first and last touch point and then spreads the other 20% between the middle points. It is usfule if you want to see specific touchpoints while still haveing a overveiw of the situation. Most commonly it is used for e-commerce metrics such as ROAS and CLV...
		- W shaped model: is simaler to U shaped but it also focus on a middle point as well. It is generaly most usful in a B2B setting with well defined funnels that are easy to calculate. In most cases it is just to cumbersome and diffacult to set up as well as being to complicated to operate.
	- Data Driven Attribution:
		- Data driven models use machien learning and predictive analytics to decide which are the most valuble touchpoints, the algorithim determins which framework is best. This is very valuble for complex customer journeys witha a lot of touch points however due to the complexity and cost to opperate they are genealy only practical for companies with large bugets.
	- **Custom Attribution:**
		- Custom attribution allos a company to make up it's own rules about which touch points get credit. This is good for complex or abnormal marketing stratigies that other models have a hard time capturing but due the the complexity and cost of setting up and maintianing such a system it is only generaly practical companys with the budget and direct need for such a system.

[Marketing attribution image](../../assets/Marketing_Attribution_Image.webp)

| Attribution Model | Use Case | Pros | Cons |
|-------------------|----------|------|------|
| First-Touch | - Brand awareness<br>- Customer acquisition | - Simple to implement<br>- Highlights initial touchpoints | - Ignores the middle and end of the journey<br>- Overemphasizes first interaction |
| Last-Touch | - Conversion Rate Optimization<br>- Customer acquisition | - Highlights final touchpoints leading to conversion | - Ignores earlier interactions<br>- Overemphasizes last interaction |
| Linear | - Customer retention<br>- Customer engagement | - Distributes credit evenly<br>- Reflects all touchpoints | - Can dilute the impact of key interactions<br>- Doesn’t differentiate touchpoint importance |
| Time-decay | - Channel optimization<br>- Customer retention | - Gives more credit to recent touchpoints<br>- Reflects journey progression | - Can undervalue initial interactions<br>- Doesn’t differentiate touchpoint importance |
| U-shaped | - Customer acquisition<br>- Brand awareness | - Emphasizes first and last touchpoints<br>- Highlights key stages | - Ignores middle touchpoints<br>- Can be complex to set up |
| W-shaped | - Customer acquisition<br>- Conversion Rate Optimization | - Emphasizes first, middle, and last touchpoints<br>- Reflects multiple stages | - Can overemphasize certain interactions<br>- More complex to implement |
| Data-driven | - ROAS<br>- Channel Optimization | - Uses actual data for accuracy<br>- Reflects true impact | - Requires significant data<br>- Can be complex to implement |
| Custom | - Specific business goal<br>- Complex journeys | - Tailored to business needs<br>- Flexible | - Requires significant data<br>- Requires significant data and expertise<br>- Complex to set up |

- Wrapping up
	- **What to avoid in attribution modeling**
		- Last click is not always *"good enough'* in general try to use multi touch instead.
		- Attribution models are **NOT** *"one size fits all"* you will use a different model for say a brand awarness campaingn then you would for a campaign that focus's on conversions
		- Models are not nessarily 100% acurate. It is important to constantly check them and make sure that the data is up to date and acurate.
		- Attribution models **NEED** regular reveiws and updates
		- Attribution modeling is not just for digital Channels. It is nessesary to intagrate offline data as well.
	- **How to build Custom Data Attribution models:**
		1. Decide and define clea, Detailed objectives
		2. Decide what constitutes as a conversion event
		3. Set a Lookback window. This means deciding how long between interactons the user goes before the last interaction no longer counts towards the conversion
		4. Give each touch point proper weight and prpare to review them on a regular bases
		5. It is nessasary to regulary test and evaluate your model including A/B Testing
		6. Utilize proper vendors and tools to implement properly. Google analitcs may be biased toward google channels undervaluing non google channels
		7. contenued testing and refinement

>>>*If you want to improve your marketing attribution, it is important that you first agree with everyone involved about the goals that you want to achieve in your organization. Understanding the questions that need to be answered will help you define the attribution models and methods you can choose from. Before you commit to a particular approach, evaluate your team’s capabilities. Although custom attribution gives you the best picture of your customers, it can be a complex process. Either opt for an out-of-the-box solution or choose to create your customized attribution model.*

>>>*Attribution is not just about deriving data, but rather using scientifically validated approaches to understand the impact of different attribution models on business goals and KPIs. By selecting the right data and methods and maintaining a flexible, adaptable approach, you can gain a more accurate and actionable view of your marketing effectiveness, ultimately leading to better decision-making and higher ROI.*

- 📖 [Attribution Models & Conversion Tracking – Two Trees PPC](https://twotreesppc.com/resources/2024-guide-to-attribution-models-and-conversion-tracking)
	- A conversion does not nessesaraly have to be a sale it can be any goal that we are trying to drive the user towards such as a contact form submission or a newsletter sighnup...
	- Without attribution modeling it is almost imposible to utilize conversion based insights such as lead costs and per conversion cost
	- Essentialy you are comparing the paths of customers who did convert to the paths of those whoe didnt to understand the keypoints that are succeful and those that fail.
	- Thank you pages are the most common method of tracking conversions
	- Enhanced conversion can help track a multiple conversion prosses to the final sale *"For example, enhanced conversions allow you to attribute multiple conversions and events to a final sale: perhaps the user signed up for your newsletter, added 3 items to their cart, and then visited the website from a remarketing ad to complete the final conversion (sale)."*
	- Enhanced conversion analytic gives a better veiw of both online and offline data.
>>>While attribution modeling can sound like a minefield, it’s often something that goes unnoticed day-to-day. But, it’s a crucial factor to understand when optimizing campaigns and during data-driven decisionmaking. Without getting it right, you may end up making disastrous decisions for your brand.

- 📖 [Marketing Attribution: Everything You Need To Know – POWR Blog](https://blog.powr.io/marketing-attribution-everything-you-need-to-know-2024)
	- This is the best one for scenario based examples, it pretty much covers the same topics that the other two do but it gives better exampels and explinations however it is less technical.

🕒 Estimated Time: 3 hours

#### I had ChatGPT test me exstinsivly in the subjects Disscused in day one
- I need to study the procces for building a lead capture form
- What is UTM data?
- How do you use tracking links?
- What is a drip email sequence and how do you build it?
[Day one test Note](./Day-one-test.md)

---

## 📆 Day 2: Drip Campaigns & Affiliate Tracking

### 🎯 Objective:
Learn to set up effective drip campaigns and understand affiliate tracking mechanisms.

### 📚 Modules

#### Drip Email Campaigns
- 📖 [How To Create Automated and Effective Drip Campaigns – Shopify](https://www.shopify.com/blog/drip-campaign)
- 📖 [9 Email Drip Campaign Best Practices – Seino.ai](https://www.seino.ai/blog/email-drip-campaign-best-practices)
- 📖 [Drip Marketing: Ultimate Guide – Moosend](https://moosend.com/blog/drip-marketing-guide/)

#### Affiliate Tracking
- 📖 [Affiliate Tracking Beginner's Guide – Partnero](https://www.partnero.com/articles/what-is-affiliate-tracking-a-beginners-guide-to-getting-started-2024)
- 📖 [Affiliate Marketing Tracking Methods – Tapfiliate](https://tapfiliate.com/blog/affiliate-marketing-tracking-methods/)
- 📖 [All Types Of Affiliate Tracking Methods – Scaleo](https://www.scaleo.io/blog/affiliate-network-affiliate-tracking-method-types/)

🕒 Estimated Time: 3 hours

---

## 📆 Day 3: Analytics Systems & Practical Application

### 🎯 Objective:
Master analytics tools and apply knowledge to practical campaign scenarios.

### 📚 Modules

#### Google Analytics 4 (GA4)
- 🎥 [Google Analytics 4 Tutorial 2024 – pRKpaZJJRxk](https://www.youtube.com/watch?v=pRKpaZJJRxk)
- 🎥 [Google Analytics 4 Full Course – m.youtube](https://m.youtube.com/watch?v=u_ECkoHVlZ8)

#### Data Analysis Fundamentals
- 📖 [Data Analysis Tutorial – GeeksforGeeks](https://www.geeksforgeeks.org/data-analysis-tutorial/)
- 🎥 [Data Analytics Full Course 2024 – Simplilearn](https://www.youtube.com/watch?v=ZUdlc5LsmHA)

#### Practical Tasks
- ✅ Set up a mock campaign in GoHighLevel
- ✅ Implement a basic drip campaign
- ✅ Track affiliate links and analyze them in GA4

🕒 Estimated Time: 4 hours

---

## 🔧 Additional Resources

- 🌐 [GoHighLevel Official Website](https://www.gohighlevel.com/)
- 🌐 [How to Setup GoHighLevel in 2024 – Feedbackwrench](https://www.feedbackwrench.com/post/how-to-setup-gohighlevel)
- 🌐 [Affiliate Management Guide for 2024 – Respona](https://respona.com/blog/affiliate-management/)

---

With this training, you'll be fully equipped to speak confidently and strategically about campaign setup, automation, attribution, CRM, and affiliate systems during your client call.

---

## From `gohighlevel-training-checklist.md`

# 📋 GoHighLevel & CRM Implementation Training Checklist

## ✅ Friday: Attribution, Forms, CRM Basics

- [ ] [Marketing Attribution 101 – How to Track ROI](https://www.youtube.com/watch?v=Q1eIPKdzP0Y)
- [ ] [Google Analytics 4 Full Setup Tutorial](https://www.youtube.com/watch?v=Ytuxoyxk90g)
- [ ] [How to Build Lead Forms That Connect to a CRM](https://www.youtube.com/watch?v=qqmpFv68YrA)
- [ ] [GoHighLevel CRM Tutorial for Beginners (2024)](https://www.youtube.com/watch?v=FtW1XcYf7oM)

## ✅ Saturday: Drip Campaigns, Metrics, Email Analytics

- [ ] [GoHighLevel Workflows Tutorial - Automate Everything](https://www.youtube.com/watch?v=8_Epk8rC5_U)
- [ ] [Marketing KPI Dashboard in Google Sheets / Looker Studio](https://www.youtube.com/watch?v=Gxy3cfObuHU)
- [ ] [Understanding CPL, CPS, ROAS, and ROI in Marketing](https://www.youtube.com/watch?v=5yYxqWr3lIg)
- [ ] [Email Campaign Analytics Explained (Opens, Clicks, ROI)](https://www.youtube.com/watch?v=DRjL7eI3keM)
- [ ] [Track Email Opens and Clicks in GoHighLevel](https://www.youtube.com/watch?v=d6H-0S8L0hw)

## ✅ Sunday: Prospect Behavior, Affiliate Tracking, White-Label Setup

- [ ] [Track User Activity on Your Website in HighLevel](https://www.youtube.com/watch?v=kdOwvWmUzCc)
- [ ] [GoHighLevel Affiliate Manager – Full Setup & Tracking](https://www.youtube.com/watch?v=JQtwLjlFvUs)
- [ ] [GoHighLevel White Label Setup (Full Guide)](https://www.youtube.com/watch?v=Kh6u6nRoRkE)

---

