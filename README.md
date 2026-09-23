# LLIMONIIE Paper Presentation

This repository contains presentation materials for understanding and presenting the paper:

**LLIMONIIE: Large Language Instructed Model for Open Named Italian Information Extraction**

## Project Description

The project focuses on explaining and presenting a research paper that introduces:

- **ONIE (Open Named Information Extraction):** a new task formulation for extracting typed entities and open relations without predefined ontologies.
- **LLIMONIIE:** an instruction-tuned, end-to-end generative framework for Italian Information Extraction.
- **A synthetic Italian ONIE dataset:** built through an LLM-based distillation pipeline and released for the research community.

## Repository Contents

- `slides.md` — a 12-slide presentation deck in Markdown format.
- `LLIMONIIE_step_by_step_test.ipynb` — a notebook that aligns this repo with the reference LLIMONIIE workflow for step-by-step tests on your dataset.
- `scripts/01_parse_and_clean.py` — a configurable cleaner that converts raw article exports into JSONL for notebook tests.
- `PromptTemplates/` — local prompt assets for NER, RE, and JOINT extraction stages.

## Step-by-step notebook workflow

The notebook `/home/runner/work/Facts_extraction/Facts_extraction/LLIMONIIE_step_by_step_test.ipynb` mirrors the reference implementation stages with the assets in this repository:

1. **Dataset cleaning** → `/home/runner/work/Facts_extraction/Facts_extraction/scripts/01_parse_and_clean.py`
2. **NER prompt stage** → `/home/runner/work/Facts_extraction/Facts_extraction/PromptTemplates/prompt_ner.txt`
3. **RE prompt stage** → `/home/runner/work/Facts_extraction/Facts_extraction/PromptTemplates/prompt_re_fr.txt`
4. **JOINT prompt stage** → `/home/runner/work/Facts_extraction/Facts_extraction/PromptTemplates/prompt_joint_fr.txt`

The cleaner now accepts a user-supplied input file or directory, output file, and minimum content length so the notebook can be pointed at a custom dataset export folder.

## Presentation Highlights

The slides cover:

1. Motivation and problem context
2. ONIE task definition
3. LLIMONIIE methodology
4. Dataset creation pipeline
5. Experimental setup and evaluation strategy
6. Key results (including ICL vs SFT comparison)
7. Strengths, limitations, and future work

## Based on

Springer paper (Machine Learning journal):
https://link.springer.com/article/10.1007/s10844-025-00978-w

## Notes

- The deck is designed for quick adaptation to PowerPoint or Google Slides.
- Speaker-facing structure is included in concise bullet form for each slide.
