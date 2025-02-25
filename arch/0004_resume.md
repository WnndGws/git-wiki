---
title: Using my modular resume
author: Wynand Gouws
date: 2025-02-25
public: true
---

# Using my modular resume

## Cheating by using LLM

### JSON-ify the job page

- Turn the job description into parsable json using the following command:

```
Please analyze these HTML contents from a job posting and extract information into a structured JSON format.

< Paste the page html here >

Format the response as valid JSON object with these exact keys:
- contact_email
- application_instructions
- job_posting_text (in markdown)
- job_posting_link
- additional_info (salary, location, etc.)
- job_title
- job_company
- job_department
- job_location
- job_skills
- job_instructions (how to apply)

optional keys

- hiring_manager_name
- job_portal
```
