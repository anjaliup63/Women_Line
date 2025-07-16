# Women_Line_Team|| NLP Annotation and Schema Design 

This repository contains the annotated dataset and schema design work completed for the NLP module as part of the project assignment scheduled for **16th–17th July**.
##  Task Overview

responsibility was to:
- Define the **NLP schema** for classification.
- Annotate the dataset using the defined schema.
- Create clear and consistent labels for future model training.

---

##  NLP Schema Defined

The annotation was done across the following four fields:

| Field       | Description                                                     | Example Values                          |
|-------------|------------------------------------------------------------------|------------------------------------------|
| `Intent`    | The user’s goal or purpose behind the message                   | `mental_wellness`, `diet_advice`         |
| `Symptom`   | Issues or problems mentioned in the prompt                      | `stress`, `headache`, `anxiety`          |
| `Sentiment` | Emotional tone of the prompt                                    | `positive`, `neutral`, `negative`        |
| `Language`  | Language used in the prompt (multilingual support included)     | `Hindi`, `English`, `Bengali`, `Telugu`  |

---

##  Files Included

| File Name                          | Description                                   |
|-----------------------------------|-----------------------------------------------|
| `annotated_prompts_with_intent.csv` | Annotated dataset with all four schema fields |              

---

## Status

-  Schema defined
-  Data annotated
-  Labels created and cleaned
- Ready for model training or further NLP processing

---
