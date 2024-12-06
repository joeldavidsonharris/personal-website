Title: What language should a data team speak?
Date: 2024-11-26
Slug: data-team-language
Tags: data
Author: Joel Harris
Summary: And the need for a business glossary

[TOC]

---

## What problem are we trying to solve?

A data team gets the best results and has the happiest stakeholders when there is minimal difference between what the data team is offering and what the stakeholders are expecting.

A good way to align expectations is to have clear definitions of what data is available for analysis, and clear indications of the effort required to perform the analysis.

There are two areas where this needs to be applied:

1. How the data team markets its services to the business
2. How the data team operates internally

Both parts of the system need to adhere to the same terminology and definitions in order to increase alignment.

## A possible approach

In order to align both the data team and the business, we need a common language. This will serve as a basis for two things:

1. How the business asks its questions
2. How the data team structures its data

The language we want both the business and the data team to speak is the language of the business itself. Businesses are composed of two elementary components:

1. Entities are things are exist - customers, employees, services, products
2. Events are things that happen - work orders, subscriptions, customer movements

In general, events are what the business want to measure, and entities are how we filter or aggregate the events.

All entities and events that the business wants to ask questions about should be defined, with accompanying plain English descriptions such as: “a subscription is a period of time where a customer is receiving a service”.

This list of entities and events make up the basis of our common language, we call it the “business glossary”.

Whenever we talk about entities and events within the data team, as well as with the business, we should ensure that:

1. They are defined in the business glossary
2. Everyone understands and agrees on the definitions

If either of the two points are not true, then we need to align all parties until they are true. If we do not, we open the door to misunderstandings further down the line.

An important artefact that builds on the business glossary is the “event matrix”. This matrix tells us which entities are associated with an event. A simple event matrix might look like this (events on the left, entities on the top): 

|  | Customer | Employee | Service | Date |
| --- | --- | --- | --- | --- |
| Work order | ✓ | ✓ |  | ✓ |
| Subscription | ✓ |  | ✓ | ✓ |
| Customer movement | ✓ |  |  | ✓ |

The event matrix gives us an intuitive way of understanding which entities are attached to an event.

With the business glossary and the event matrix, we already have most of the information we need, the next part is applying this information.

## How do we structure our data?

We should align our data with the concepts outlined in the data glossary using two table types:

1. Facts represent events
2. Dimensions represent entities

The dimensions that are linked to each fact should match the relationships in the event matrix.

## How should we gather requirements?

We should gather requirements using the language of the business - the business glossary. We should frame these requirements in the form of questions that the business needs answered. Examples include:

- How many customers are subscribed?
- Which services are the most subscribed?
- Which employees complete the most work orders?

Because of the artefacts we discussed earlier we can very quickly understand two things:

1. What these questions actually mean - because we have a clean definition of each entity and event in our business glossary
2. Whether we can answer them - because we know which entities and events are associated in our event matrix

By gathering requirements in this way we are able to ensure that the business will get what they are expecting, and increase stakeholder satisfaction.

## Can we do even better?

At the beginning I mentioned that we can use these techniques to communicate the effort required to perform analysis. We can achieve this by doing three things:

1. Profiling all of our possible sources of data, even the ones we are not currently using
2. Ensuring that we have business glossary definitions for the entities and events that can be derived from the sources
3. Noting that these entities and events are not currently available for analysis

By doing this, we can prioritise ingestion of new sources as the business starts asking questions about entities and events that are contained in those sources. We can also communicate to the business that effort to answer a question may be low if the source is already ingested - or high if not.

Another improvement that can help the business ask more precise questions is including a set of available “attributes” along with each entity and event in the business glossary. Attributes for a customer could include a customers age, gender, and region. Just as before, we should make sure to clearly define these attributes to reduce any misalignment.

Making this information available to the business makes communication much more simple as they can quickly understand which questions they can ask, such as:

- How many customers do we have in each region?
- Which age group has the highest churn percentage?

These attributes should be physically represented by columns in the dimensions we mentioned earlier.

## What does this look like in action?

Let's imagine that we've:

- Created a business glossary with entities, events, attributes, and statuses
- Created an event matrix that links entities and events
- Aligned our table and column names with our business glossary
- Communicated and agreed on business glossary terms internally and with the business

We're now in a position where:

- An engineer or analyst working with the data can understand more about the meaning of tables and columns based on the wording
- A business user can easily shop for a dashboard or ad-hoc analysis by browsing the business glossary and event matrix
- Requirements can be gathered in the form of plain English questions, referencing entities, events, and attributes
- Expectations for what the business can and cannot have, as well as effort required, can be communicated clearly in business terms