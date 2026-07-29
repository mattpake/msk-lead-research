
# lead research tool proposal


the goal is to build a real internal sales tool for finding and managing good construction and transport leads in the Moravian-Silesian Region.

For v1, the tool will focus on:

* roofers
* electricians
* general contractors
* road freight companies
* companies with around 10–50 employees
* Ostrava and nearby areas
* a first test batch of 20–30 companies

The goal is quality, not volume. The tool should help you find good companies, understand them, prepare personal outreach, and track what happens next.

## recommended stack

* Next.js, TypeScript, and Tailwind CSS for the frontend
* Python and FastAPI for the backend
* LangGraph for the research and approval workflow
* SQLite for v1
* Google Places and selected business directories for lead discovery
* Firecrawl or a similar service for website research
* AI for company analysis, scoring, and email drafts
* CSV and Google Sheets export

I recommend Next.js instead of simple HTML because this tool needs a proper dashboard, filters, logs, detail pages, approval screens, and room for future growth.

## how the tool will work

### 1. company discovery

The tool will search for companies by:

* location
* company type
* industry
* selected business categories

The existing list of 18 companies will be used as a reference for what a good lead looks like.

### 2. data collection

For each company, the tool can collect:

* company name
* website
* phone
* public email
* address
* city
* company type
* source
* rating and review count
* LinkedIn or public social links
* short company description

### 3. validation and cleaning

The tool will check:

* duplicate companies
* broken websites
* invalid email formats
* wrong region
* wrong company type
* inactive companies
* companies that are too small or too large
* missing contact details

Each rejected company should show a clear reason.

### 4. company research

The tool will read the company website and prepare a short research summary.

The summary can include:

* what the company does
* which services it offers
* whether it fits the target
* possible size
* possible business problems
* which software or automation service may help
* which case study is most relevant

The system should clearly mark unknown information instead of guessing.

### 5. lead scoring

Each company will receive a score based on simple rules such as:

* region match
* industry match
* company size match
* valid contact details
* active website
* clear business need
* fit with your services
* fit with Hebík Transport or OCTO.CAB

The score and the reason behind it should be visible and editable.

### 6. email drafts

For approved leads, AI will prepare a personal email draft using the company research.

The draft should include:

* a real reason for contacting the company
* one possible problem
* one useful service
* the most relevant case study
* a simple call to action

Nothing will be sent automatically in v1. Every email will require human review and approval.

### 7. tracking

For every lead, the tool will track:

* source
* research status
* lead score
* accepted or rejected
* email draft
* approved
* sent
* replied
* meeting booked
* follow-up date
* notes

This will help us understand which source, company type, and message works best.

## dashboard

The dashboard should include:

* lead list
* search and filters
* lead score
* company detail page
* research summary
* email draft review
* approval status
* outreach status
* reply and meeting tracking
* scraping progress
* workflow logs
* errors and retry option
* CSV and Google Sheets export

## LangGraph workflow

LangGraph is useful because the process has many connected steps:

1. discover company
2. collect data
3. validate data
4. remove duplicates
5. research website
6. score the lead
7. prepare email draft
8. pause for human review
9. save the decision
10. update outreach status

This gives us saved state, retries, logs, and human approval without building a simple AI wrapper.

## v1 scope

The first version should include:

* import the current 18-company list
* discover more companies in the selected region
* prepare a final batch of 20–30 good leads
* validation and duplicate removal
* company website research
* lead scoring
* accepted and rejected reasons
* email draft generation
* human approval
* source-to-message-to-reply-to-meeting tracking
* logs and error handling
* CSV and Google Sheets export

## future options

After the first batch is tested, we can later add:

* more regions
* more company types
* more data sources
* Gmail integration
* automatic reply detection
* calendar integration
* follow-up automation
* PostgreSQL
* team accounts
* deeper analytics
* advanced tracing

These should not make v1 too large before the process is proven.

## rough time and cost

Estimated effort:

**35–45 hours**

At 10 hours per week:

**around 4–5 weeks**

At the current rate of $20 per hour:

**$700–$900**

The final estimate depends on the selected data sources, dashboard detail, Google Sheets integration, and how much tracking and logging is included.

## questions before development

1. Can you share the current list of 18 companies?

2. Which cities around Ostrava should be included?

3. Should construction and transport use separate scoring rules?

4. What information must be available before a lead can be approved?

5. Should companies without an email still be accepted if they have a phone number or contact form?


6. Do you want both a dashboard and Google Sheets export?

7. Should the tool prepare follow-up drafts as well?

8. Will sent, replied, and meeting status be updated manually in v1?

9. Do you want Gmail and calendar integration now, or after the first batch is tested?
