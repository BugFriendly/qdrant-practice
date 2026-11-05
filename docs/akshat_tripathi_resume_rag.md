# Akshat Tripathi: Resume Knowledge Base

## Profile Summary

### Overview
Akshat Tripathi is a Senior Software Engineer on the AI Platform team at NextZen Minds Technology Private Limited in Kolkata, India. He has worked there since September 2024. He is a backend engineer with about three years of experience building scalable, AI-enabled backend systems in Golang and Python. His work covers microservices, retrieval-augmented generation (RAG), GraphRAG, agentic workflows, asynchronous processing, REST and gRPC APIs, Kafka, Redis, PostgreSQL, and AWS infrastructure. Before NextZen Minds, Akshat worked as a Programmer Analyst at CBNITS in Kolkata from June 2023 to August 2024.

### Contact Details
| Field | Value |
|---|---|
| Name | Akshat Tripathi |
| Current title | Senior Software Engineer - AI Platform |
| Phone | +91 8299116586 |
| Email | tripathiakshat675@gmail.com |
| LinkedIn | https://www.linkedin.com/in/akshat-tripathi-32780421b/ |
| GitHub | https://github.com/TRITON1999 |
| Location | Kolkata, India |

### Education
Akshat completed a Bachelor of Technology at the Indian Institute of Engineering Science and Technology (IIEST), Shibpur, in Howrah. He studied there from April 2019 to April 2023.

| Degree | Institution | Location | Period |
|---|---|---|---|
| Bachelor of Technology | Indian Institute of Engineering Science and Technology, Shibpur | Howrah | 04/2019 to 04/2023 |

### Project Index
This table lists every project and major work item in the knowledge base, with its employer and whether it appears on the printed resume.

| Name | Full title | Employer | Type | Period | On printed resume |
|---|---|---|---|---|---|
| eSentire | Agentic AI and MCP Integration Platform | NextZen Minds | Client project, resource augmentation | Dates to confirm | Yes |
| TravelXS | AI-Powered Travel Automation Platform | NextZen Minds | Client project | Dates to confirm | Yes |
| TotalHER | Social Platform Backend | NextZen Minds | Client project | Dates to confirm | Yes |
| Peach Health | Healthcare booking, matching, and movement monitoring platform | NextZen Minds | Client project | Dates to confirm | No |
| Order automation | Agentic AI pipeline for order processing | NextZen Minds | Internal pipeline | Dates to confirm | Yes (bullet only) |
| Zulek Pharma DCP | Digital patient care platform | CBNITS | Client project | Within 06/2023 to 08/2024 | No |
| Swift Security | Cloud security PII scanner and in-memory store | CBNITS (placement to confirm) | Product | Within 06/2023 to 08/2024 | No |
| Groie | AI No-Code Website Builder | Personal | Personal project | Dates not stated | Yes |

---

## Work Experience

### NextZen Minds Technology Private Limited

Employer: NextZen Minds Technology Private Limited (printed as "Private Lmt" on the resume)
Location: Kolkata, India

#### Senior Software Engineer, AI Platform (09/2024 to present)

Akshat works as a Senior Software Engineer on the AI Platform team at NextZen Minds. The role centers on agentic AI infrastructure. This includes a centralized MCP gateway, tool discovery and permissioning, agent evaluation, and agent workflows. He also delivered several client projects in this role. For eSentire, he was deployed as a resource and worked directly with the client's engineering team. Other client projects include TravelXS, TotalHER, and Peach Health. His other work includes an order-automation agent pipeline, a Stripe payment gateway wrapper, RAG retrieval improvements, and Kafka and RabbitMQ worker services.

#### Responsibilities and Achievements at NextZen Minds

- Migrated custom tool creation for each agentic flow to a centralized MCP gateway. Tools are now reused across services, which speeds up development. The gateway is described in the eSentire section.
- Improved agent tool-selection accuracy by refining MCP tool metadata, parameter schemas, and system-prompt routing instructions. This reduced incorrect and redundant tool calls in multi-step workflows.
- Contributed to context-window optimization. Relevant skill.md files and retrieval context are loaded selectively, based on the workflow type and the active tools.
- Built asynchronous event-processing services on Kafka and RabbitMQ, using goroutine worker pools. The services handle about 1k transactions per second (TPS).
- Designed a Stripe payment gateway wrapper and automated payment workflows that use webhooks.
- Improved document retrieval quality in RAG workflows through optimized chunking and preprocessing.
- Owned an agentic AI pipeline for order automation. The pipeline extracts order details from unstructured customer messages, maps products against catalog data, validates outputs through critic agents, and generates structured orders for downstream systems.

#### Technology Used at NextZen Minds

| Area | Technologies |
|---|---|
| Languages | Golang, Python |
| Agent frameworks | LangGraph, LangChain, LlamaIndex, FastMCP, Go ADK, CrewAI, Openclaw |
| MCP | Gateway, client-facing MCP server, tool discovery, RequestState, elicitation, sampling |
| Messaging | Kafka, RabbitMQ |
| Data stores | PostgreSQL, Redis, Qdrant (vector database) |
| AWS | Lambda, API Gateway, S3, SQS, SNS, EC2, IAM |
| Identity | Okta (client-facing MCP authorizer and integration) |
| Payments | Stripe, webhooks |
| Evaluation | RAGAS, LangSmith |

#### Metrics at NextZen Minds

The resume records one throughput figure for this role: about 1k TPS for the Kafka and RabbitMQ worker services. No quantified results are recorded for the Stripe gateway, the RAG retrieval work, or the order automation pipeline.

---

### CBNITS

Employer: CBNITS
Location: Kolkata, India

#### Programmer Analyst (06/2023 to 08/2024)

Akshat worked as a Programmer Analyst at CBNITS. His main work was on a HIPAA-compliant backend. This covered performance optimization, role-based and attribute-based access control, and a break-the-glass access workflow for emergency situations. He also worked on two projects from the same period: Zulek Pharma DCP, a digital patient care platform, and Swift Security, a cloud security product that detects personal data in documents.

#### Responsibilities and Achievements at CBNITS

- Reduced the p95 latency of consultation and booking endpoints from 820ms to 510ms. The work added Redis caching for the top 1,000 queries and fixed an N+1 query problem in the product join.
- Designed a hybrid RBAC and ABAC authorization system for a HIPAA-compliant backend. Role-to-endpoint mappings are stored in PostgreSQL and cached in Redis when a session is created. Auth middleware enforces them. A per-handler helper evaluates resource-level conditions on access to protected health information (PHI).
- Built a break-the-glass workflow. It grants time-bound role elevation, enforces per-user invocation limits, escalates digitally approved requests beyond a threshold, and sends compliance notifications. It writes structured JSON audit logs that capture the role, action, resource, and emergency context.
- Optimized database queries and backend services, reducing CPU and memory utilization by 40%.

#### Technology Used at CBNITS

| Area | Technologies |
|---|---|
| Languages | Golang, Python |
| Data stores | PostgreSQL, Redis |
| Access control | RBAC, ABAC, auth middleware, break-the-glass workflow |
| Logging | Structured JSON audit logs |
| Messaging and storage | SNS, SQS, S3 (Zulek Pharma DCP) |
| Compliance | HIPAA, PHI handling |

#### Metrics at CBNITS

| Metric | Value | Notes |
|---|---|---|
| p95 latency, consultation and booking endpoints | 820ms to 510ms | Redis caching and an N+1 fix. Measurement period to confirm. |
| Cache scope | Top 1,000 queries | Redis |
| CPU and memory utilization | Reduced by 40% | Measurement method to confirm. |

---

## Projects at NextZen Minds

### eSentire: Agentic AI and MCP Integration Platform

Employer: NextZen Minds
Engagement: Resource augmentation. Akshat was deployed as a resource and worked directly with eSentire's team.
Purpose: The platform supports eSentire's security investigations and their engineering tools. It exposes internal APIs through MCP, connects agents to security workflows, and gives clients a self-service MCP endpoint.

Akshat worked on three workstreams for eSentire.

#### Workstream 1: Internal MCP Gateway

The internal MCP gateway connects to other MCP servers and proxies them, so that one endpoint gives access to many tools. It is for internal use. eSentire's own coding harness uses it, connected to Atlassian, GitHub, Slack for notifications, and Grafana MCP servers. Investigation agents and other agentic workflows also use it.

The gateway includes a tool extension mechanism. Any user can add a new MCP tool by writing a YAML configuration file. The file states the wrapper type for the tool, such as an HTTP call or an SDK call. Teams can publish tools without building a new MCP server for each one.

#### Workstream 2: Self-Service MCP for Clients

The self-service MCP is client-facing. It wraps eSentire's existing APIs, which are populated with each client's data, and exposes them as MCP tools.

Akshat built the first version (v1) and then migrated the work to v2. Version 2 added server discovery and RequestState. RequestState converts MCP streaming calls into a stateless flow, and elicitation and sampling were updated to work through it. Version 2 also added dynamic tool and parameter discovery based on the user's role. A user sees only the tools and parameters their role allows.

The project includes a pseudo-Okta dynamic client discovery endpoint. It provides a client ID view without creating a new client. This reduces setup friction for clients who want to connect to the MCP.

A tool discovery engine wraps the tools/list method. It reads tool definitions from YAML files or a cache, checks each user's permissions, and edits the tools/list response for each customer.

The client-facing MCP runs on AWS Lambda. Akshat owned the Lambda cold-start handling, the validation middleware, the authorizer, and the Okta integration. The server handles about 400 tool invocations per hour.

#### Workstream 3: Agent Integration and Investigation Workflow

Akshat connected the gateway's tools to single-agent and multi-agent workflows. He added tool-call evaluation, output handling, and a tool circuit breaker.

Investigation workflows route findings to cybersecurity. For those workflows to work, the agents need full context on each finding. Akshat added specific tools for this, including get-finding-by-ID and get-assets. He then built the whole finding workflow around them.

#### Resume Bullets for eSentire (as printed)

- Built multi-step agentic workflows using LangGraph with conditional branching, retry logic, and tool-chaining. The workflows automate cross-domain tasks such as data enrichment, alert triage, and report generation, with structured state management across agent nodes.
- Developed a Model Context Protocol (MCP) server that exposes internal REST and gRPC APIs as discoverable, schema-annotated tools for Claude Code and Claude Desktop. This lets an LLM orchestrate existing backend services without rewriting integration layers.
- Architected a serverless, Lambda-based MCP implementation behind API Gateway, with connection pooling and cold-start optimization. Warm invocations take under 200ms. The implementation enforces IAM-scoped, least-privilege access per tool.
- Implemented tool-call validation middleware. It schema-checks inbound MCP requests, sanitizes parameters, and enforces rate limits per client session. This prevents runaway agent loops and unauthorized API calls.

#### Technology and Metrics for eSentire

| Area | Details |
|---|---|
| Protocols | MCP, RequestState, elicitation, sampling, tools/list |
| Gateway integrations | Atlassian, GitHub, Slack, Grafana |
| Runtime | AWS Lambda, API Gateway |
| Identity and access | Okta, pseudo-Okta dynamic client discovery, IAM, per-tool least privilege |
| Agent frameworks | LangGraph |
| Client-facing scale | About 400 tool invocations per hour (peak or average to confirm) |
| Warm invocation latency | Under 200ms (from resume) |

---

### TravelXS: AI-Powered Travel Automation Platform

Employer: NextZen Minds
Type: Multi-agent system with agentic RAG
Purpose: The system produces an end-to-end travel itinerary that a travel agent can share with a client. Agents handle the work from the first client email to the final PDF.

#### Client Intake and Requirements Gathering

Client emails arrive through SMTP servers. The servers send a webhook notification for each incoming email. The notification triggers an AI classification agent, which decides whether the email is a new request, an update to an existing request, or a follow-up on an old one.

For a new request, the requirements agent collects everything needed to plan the trip. This covers the destinations, the time period, the spending budget, any specific event the client wants to attend at a destination, and the scenarios that depend on those answers. When fields are missing, the system flags them and sends follow-up emails over SMTP. An email-parsing agent built with LangChain uses few-shot prompted LLM calls to extract the requirements, such as dates, destinations, budget, and preferences.

#### Event Research and Flight and Hotel Selection

An event research agent looks up the events that happen at each destination during the client's time period. For each event, it checks feasibility, the start time, when the event usually takes place, and reviews. It writes an event journal. The journal shows the areas and events where the client needs to be present at each destination.

The travel agency already had a catalog of hotels and travel partners. A traverser searches that catalog for the best flights and budget-friendly hotels near the event venues. It covers the options that fit the client's time period and budget.

#### Feasibility Check

The feasibility check has two steps.

The first step is deterministic. Plain code, not an LLM, detects overlaps between flight times and booking or arrival times. It measures how long each overlap lasts and marks each timeline as feasible or not feasible. The flagged overlaps are handed to the critic agent through a JSON schema.

The second step is the critic agent. It reviews the flagged overlaps and looks for problems other agents may have missed. It cross-checks the timelines in other ways and reviews them step by step. It evaluates error margins, delay scenarios, and alternatives. Its output is passed to the next stage through a JSON schema.

The resume describes the critic differently. It says the critic validates tour-location geo-feasibility and cross-checks coordinates against mapping APIs. Both descriptions may apply. This is noted for confirmation in the verification list.

#### Itinerary Assembly and PDF Report

A main itinerary engine assembles the traverser output and the client's requests into one JSON itinerary. The itinerary covers the whole trip, from start to end. It includes the start date, arrival time, end time, travel legs, and tour guide details.

A report-generation agent takes the JSON itinerary schema and converts it into a shareable PDF report for the client.

Every handoff between agents uses a JSON schema.

#### Evaluation

The team built an evaluation pipeline with RAGAS and reported its results. LangSmith was added for tracing and evaluation. The resume also lists a handoff bullet: the system generates structured handoff payloads for the operations team, which removed manual intake work.

#### Technology and Metrics for TravelXS

| Area | Details |
|---|---|
| Agent frameworks | LangChain (email parsing), LangGraph (multi-agent pipeline with supervisor pattern) |
| Patterns | Few-shot prompting, critic agents, supervisor agent, agentic RAG, JSON schema handoffs |
| Integrations | SMTP with webhooks, mapping APIs (to confirm), travel catalog |
| Evaluation | RAGAS, LangSmith |
| Output | JSON itinerary schema, PDF report |
| Metrics | No volume or accuracy figures recorded |

---

### TotalHER: Social Platform Backend

Employer: NextZen Minds
Purpose: TotalHER is a social media platform for female active influencers and female users who face harassment on general platforms. The platform gives them a safer space.

#### Platform Architecture

The backend is built as microservices. The User, Content, Stories, and Privacy services each scale horizontally on their own. PostgreSQL stores transactional data. Redis handles session caching and rate limiting. The services run on AWS EC2, with S3 for media storage. Compute-heavy event-driven work for the Post, Story, and Conference services is offloaded to AWS Lambda for asynchronous fan-out processing.

The Stories service is ephemeral. Content expires automatically through a TTL, and an event-driven cleanup runs on Lambda. Viewer analytics track unique views and completion rates.

A configurable ABAC-style privacy module enforces visibility at the resource level. It supports rules for each post and for each user.

#### Recommendations with Collaborative Filtering

Akshat built the recommendation system. Each user is represented as a node in a graph. The system uses that graph to recommend friends, posts, and connections, and to handle friend requests.

It clusters users by their interests and aligns similar interests. Collaborative filtering estimates how likely a user is to like a given item, and it uses that estimate to recommend posts.

#### Fan-out Posting and Feed Generation

Each user has their own feed queue. When a user posts, the post is pushed into each user's feed queue. Queues for inactive users are not pushed to. They stack up without being filled, so the database does not fill with feed data for users who are not active. Whether the push goes to all users or only to followers is to be confirmed.

Feeds are generated from user activity. Active users get their personal feed regenerated more often. Less active users have their feed stalled.

When a user returns after a long absence, they first see trending feeds. Their personal feed is regenerated in the background, based on their current interests and their past likes. Once it is ready, the personalized feed replaces the trending view.

#### Chat System

The chat system uses webhook workers connected through Kafka. The workers pass messages across the system. Multiple clusters of webhook workers run in parallel.

Each user connects to at least two workers. The first is the primary worker, and the second is a backup. If one worker goes down, the user keeps their session through the backup, so there is no single point of failure.

#### Technology for TotalHER

| Area | Details |
|---|---|
| Services | User, Content, Stories, Privacy |
| Data stores | PostgreSQL, Redis |
| Messaging | Kafka, webhook workers, AWS Lambda fan-out |
| AWS | EC2, S3, Lambda |
| Access control | ABAC-style privacy module |
| Techniques | Collaborative filtering, graph-based recommendations, fan-out on write, TTL expiry |

---

### Peach Health: Healthcare Platform

Employer: NextZen Minds
Status: Not on the printed resume. It is a candidate for addition.
Compliance: The whole application is HIPAA compliant.
Akshat's role: He owned the whole booking system end to end.

Peach Health connects patients with healthcare providers (HCPs). It handles booking, video sessions, care plans, and movement-based exercise tracking.

#### Patient Admission and HCP Matching

Patients are admitted to the platform and then matched with an HCP. Akshat designed the matching algorithm. It routes each patient to the most available and highest-rated HCP. Patients can see each HCP's availability before they book.

#### HCP Calendar and Video Sessions

The platform shows each HCP's calendar to patients. When a patient needs a video session, they can book a slot on the HCP's calendar. The booking syncs with the HCP.

#### Resource Library and Curriculum

The platform has a library of resources that patients can read. Each patient's plan is set by their diagnosis. The plan contains reading material and recommended exercises. The HCP's recommendations are added to the patient's curriculum.

#### Patient, Case, and HCP Notes

The platform has three note types: the patient note, the case note, and the HCP note. Akshat built all three. Movement readings from the monitoring engine are attached to the relevant notes.

#### Movement Detection and Monitoring

Patients can turn on their camera and do their prescribed exercises in the browser. A monitoring engine tracks their joint points and builds a stick-skeleton model of their body. It records joint movement readings, such as hip movement, any restriction in movement, and signs of pain. It also records whether the patient performed each exercise correctly. The readings are attached to the patient's notes.

Akshat worked on the front-end ML model for this feature. The specific pose-tracking model and where inference runs are to be confirmed.

#### Technology for Peach Health

| Area | Details |
|---|---|
| Domain | Healthcare booking, provider matching, care plans, video sessions |
| Compliance | HIPAA |
| Matching | Custom availability and rating-based algorithm |
| Calendar | HCP calendar integration, video session sync |
| Movement tracking | Browser camera, joint-point tracking, stick-skeleton model (to confirm) |
| Notes | Patient note, case note, HCP note |

---

## Projects at CBNITS

### Zulek Pharma DCP: Digital Patient Care Platform

Employer: CBNITS
Status: Not on the printed resume.
Purpose: Zulek Pharma's dynamic platform of care for patients. Akshat's work covered the worker pools, the backend, database queries, and hybrid caching.

#### Worker Pools and Report Generation

The platform generates many reports for patients. Each patient's receipts are converted into reports, and patients can export those reports at any time.

Akshat built worker pools for asynchronous work. Each pool has its own SQS and SNS connections. Requests are streamed to one of the pools, and the first available worker picks each one up. The worker generates the report and stores it in S3. The user receives a URL and downloads the report from there.

#### Hybrid Caching

Some API responses are cached by session ID. When the same request arrives again with the same session ID, the cached response is returned. When a write changes the result of a cached API, the cache is invalidated. Depending on the case, either the entries for the affected users are removed, or those entries are updated.

The platform was hitting very large write blocks, and the caching helped reduce the load on the database.

#### Technology for Zulek Pharma DCP

| Area | Details |
|---|---|
| Messaging | SNS, SQS |
| Storage | S3 (report storage) |
| Caching | Session-keyed API cache with write-based invalidation |
| Work | Worker pools, asynchronous report generation, database query work |

---

### Cloud Security: Swift Security

Employer: CBNITS (placement to be confirmed)
Status: Not on the printed resume.
Purpose: A cloud security product that finds personal data in documents before they are sent to other parties.

#### PII Capture and Sessions

When a user sends a document to another party, Swift Security scans the document. It captures any personally identifiable information (PII) in the document and stores the findings in a lightweight, in-memory database.

A scan starts a session, and the session gets a session ID. APIs are mapped to that session ID, so each request can be linked to the sentences or documents it refers to.

#### In-Memory Eventually Consistent Store

Akshat designed the in-memory database. It is eventually consistent and supports transactions. Each stored item has asset properties.

The store reaches consistency when the PII discovered in a document matches the PII already stored for it. Once that happens, the cached results are ready to be packaged.

#### Packaging, S3 Storage, and Retrieval

When the results are consistent, they are packaged and sent to S3. They are not read back unless the system or a user requests them. The stored objects are indexed, so the system can identify which parts of an S3 object it needs and load only those parts when a request comes in.

#### Technology for Swift Security

| Area | Details |
|---|---|
| Data detection | PII capture from documents |
| Storage | Custom in-memory, eventually consistent database with transactions |
| Archive | S3, with indexed partial retrieval |
| Sessions | Session ID per scan, API mapping by sentence or document |

---

## Personal Projects

### Groie: AI No-Code Website Builder

Type: Personal project
Link: https://app.groie.io/login

Groie is an AI no-code website builder. Its backend uses gRPC microservices with PostgreSQL and Redis. The platform includes RAG-based content workflows that help users produce content more efficiently.

#### Achievements (as printed)

- Built gRPC microservices with PostgreSQL and Redis. The services handle 700 requests per second with a p95 latency of 150ms.
- Reduced publish-to-live time by 40% through caching and query optimization.
- Integrated RAG-based content workflows to improve user productivity and content generation efficiency.

#### Metrics for Groie

| Metric | Value | Notes |
|---|---|---|
| Throughput | 700 requests per second | Production or load test to confirm |
| p95 latency | 150ms | |
| Publish-to-live time | Reduced by 40% | Caching and query optimization |

---

## Skills Reference

### Skills by Category

| Category | Skills |
|---|---|
| Programming languages | Golang, Python |
| Backend development | REST APIs, gRPC, microservices, event-driven systems, WebSockets, goroutine worker pools, FastAPI, Gin, Mux |
| Data stores | PostgreSQL, Redis, MongoDB, MySQL, Qdrant (vector database) |
| Messaging and queues | Kafka, RabbitMQ, AWS SNS, AWS SQS |
| AWS | S3, SNS, SQS, EC2, ALB, API Gateway, Lambda, IAM |
| DevOps | Docker, CI/CD pipelines |
| AI and agents | LangChain, LangGraph, LlamaIndex, FastMCP, Go ADK, CrewAI, Openclaw, MCP (gateway, servers, tool discovery) |
| Retrieval | RAG, GraphRAG, agentic RAG, chunking and preprocessing |
| Evaluation | RAGAS, LangSmith |
| Security and access control | RBAC, ABAC, OAuth-style client discovery, Okta, API security, IAM least privilege |
| Compliance | HIPAA, PHI handling, PII detection |
| Frontend | React.js |
| Concepts | Caching, distributed systems, async processing, RAG workflows |

---

## Verification Notes

These items are not confirmed and should be checked before the knowledge base is used to answer questions about specific claims:

- Employer name: the resume prints "Private Lmt". This is probably "Ltd".
- Project dates: the resume does not give dates for eSentire, TravelXS, TotalHER, or Peach Health.
- eSentire: which workstream the LangGraph, Lambda, and validation bullets belong to.
- eSentire: whether the Claude Code and Claude Desktop references describe the gateway or the client-facing server.
- eSentire: whether about 400 tool invocations per hour is a peak or an average.
- TravelXS: whether the critic is a timeline checker, a geo-feasibility checker, or both.
- TravelXS: which LLMs and mapping or booking APIs were used, and whether the system reached real clients.
- TotalHER: whether feed fan-out goes to all users or only followers, and what counts as an active user.
- Peach Health: the pose-tracking model, where inference runs, and whether it reached production.
- Zulek Pharma DCP: the expiry period of the report URL, and the exact cache technology.
- Swift Security: whether it belongs to CBNITS or to Peach Health.
- Groie: whether it is live with real users, and whether the 700 requests per second figure is from production traffic or a load test.
- Missing metrics: Stripe gateway, RAG retrieval improvement, order automation accuracy and volume, TravelXS volume, TotalHER users, and Peach Health patients.
