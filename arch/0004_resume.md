---
title: Using my modular resume
author: Wynand Gouws
date: 2025-02-25
public: true
---

# Using my modular resume

## Per job branches

- Checkout a branch per job using `git checkout -b <JobTitle>`

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

- Save this information in `info.json`

### Use JSON to write cover letter

- Use the following in gpt

```
Please help me write a professional job application email based on the following information:

=== MY RESUME ===
As described above

=== JOB DETAILS ===
{
< PASTE info from info.json here >
}

Instructions:

1. Create an email that is ready to send without any placeholders or edits needed
2. If any critical information is missing (like company name or job title), respond with an error message instead of generating incomplete content
3. Skip any optional fields if they're empty rather than including placeholder text
4. Use natural sentence structure instead of obvious template language
5. Include specific details from both the resume and job description to show genuine interest and fit
6. Any links or contact information should be properly formatted and ready to use

Format the response as a JSON object with these keys:
{
"status": "success" or "error",
"error_message": "Only present if status is error, explaining what critical information is missing",
"email": {
"subject": "The email subject line",
"body_html": "The email body in HTML format with proper formatting",
"body_text": "The plain text version of the email",
"metadata": {
"key_points_addressed": ["list of main points addressed"],
"skills_highlighted": ["list of skills mentioned"],
"resume_matches": ["specific experiences/skills from resume that match job requirements"],
"missing_recommended_info": ["optional fields that were missing but would strengthen the application if available"],
"tone_analysis": "brief analysis of the email's tone"
}
}
}

Critical required fields (will return error if missing):

- Job title
- Company name
- Job description
- Resume content

Recommended but optional fields:

- Hiring manager name
- Department
- Location
- Application instructions
- Referral source
- Required skills list

Please ensure all HTML in body_html is properly escaped for JSON and uses only basic formatting tags (p, br, b, i, ul, li) to ensure maximum email client compatibility.
```

- Save that output as `letter_info.json` and run `python ./json_to_coverletter.py`
- Convert cover_letter.tex to pdf using `tectonic cover_letter.tex`
