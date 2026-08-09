# Slide 1 — Title
## LLIMONIIE: Open Named Information Extraction for Italian with Instruction-Tuned LLMs

- Paper focus: low-resource Italian Information Extraction
- New task: ONIE (Open Named Information Extraction)
- New framework: LLIMONIIE
- New synthetic dataset + public release

---

# Slide 2 — Motivation
## Why this matters

- Unstructured text is growing rapidly
- Traditional IE needs fixed ontologies + high annotation effort
- Open IE is flexible but often shallow (weak typing/context)
- Most advances are English-centric; Italian is under-resourced

---

# Slide 3 — Problem Definition (ONIE)
## From OIE to ONIE

- OIE output: (subject, relation, object), often untyped entities
- ONIE adds:
  - typed entities (context-sensitive)
  - concise semantic relation labels
  - no fixed ontology requirement
- Goal: cross-domain generalization

---

# Slide 4 — LLIMONIIE Framework
## Instruction-tuned seq2seq extraction

- ONIE is modeled as autoregressive seq2seq generation
- One model family, instruction-switched across 3 tasks:
  1. Open Named NER
  2. Open Relation Extraction (RE)
  3. Joint extraction (entities + relations)

---

# Slide 5 — Task Design
## Three tasks in detail

- **Open Named NER:** extract entities + dual labels
- **Open RE:** extract triplets given text + entities
- **JOINT:** output typed triplets in one pass
- Multi-task instruction tuning enables unified behavior

---

# Slide 6 — Dataset Creation Pipeline
## LLM distillation for Italian ONIE

- 5 balanced categories:
  - Science, Politics, Technology, Literature, Music & Film
- 10,000 docs total (2,000/category)
- Two-step annotation:
  1. NER generation
  2. RE generation from extracted entities
- Post-processing:
  - format compliance checks
  - Triplet Critic semantic filtering

---

# Slide 7 — Annotation Innovation
## Dual-label entities

- Each entity gets:
  - specific context label
  - hypernym (general class)
- Example concept: [Singer, Person] instead of only Person
- Relations remain open predicates (not a closed schema)

---

# Slide 8 — Experimental Setup
## Models, tuning, benchmarks

- Backbones (<10B):
  - Llama 3 (8B)
  - Anita (8B)
  - Phi-3-mini (3.8B)
- Fine-tuning: QLoRA 4-bit, 2 epochs, RTX A6000
- Datasets:
  - SMILER
  - REDIT
  - RE-DocRED (translated to Italian)

---

# Slide 9 — Evaluation Strategy
## Why semantic matching

- Exact matching is too strict for generative IE
- Similarity model: BGE-M3 (threshold 0.8)
- Triplet Critic validates semantically correct non-gold outputs
- Metrics: Precision, Recall, F1

---

# Slide 10 — Key Results (Table 9)
## JOINT task: ICL (5-shot) vs SFT (LLIMONIIE), F1

- **Llama 3 (8B):** 44.4 → 70.6 (**+26.2**)
- **Anita (8B):** 22.75 → 72.0 (**+49.25**)
- **Phi-3-mini (3.8B):** 43.49 → 71.5 (**+28.01**)
- Strong gains across all five domains

---

# Slide 11 — Critical Analysis
## Strengths and limitations

### Strengths
- Novel ONIE formalization for low-resource language
- Unified instruction-based multitask extraction
- Valuable public dataset contribution
- Clear SFT gains over ICL

### Limitations
- Synthetic labels may carry LLM bias
- Translated benchmark may introduce artifacts
- Similarity/Critic-based scoring affects strict comparability

---

# Slide 12 — Conclusion & Future Work
## Main takeaways

- LLIMONIIE significantly advances Italian open IE
- ONIE + dual-type entities improve semantic expressiveness
- SFT is crucial for robust JOINT extraction
- Future work:
  1. n-ary triplets
  2. transfer to other low-resource languages
  3. knowledge graph population
