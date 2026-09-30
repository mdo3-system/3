# Project Specification: Eiken Graded Reader Series with Aesop's Fables for 電子書籍

## 1. Project Overview
- **Title Concept**: Dual-Level Eiken Fables: Aesop's Fables for Step-Up Learning (英検ステップアップ多読：イソップ寓話編)
- **Target Platform**: 電子書籍 Store (KDP) Reflowable eBook / Text-to-Speech (TTS) supported.
- **Core Concept**:
  - Compare two adjacent Eiken levels within the same story (Vol 1: Grade 4 vs Grade 3; Vol 2: Grade 3 vs Pre-2; Vol 3: Pre-2 vs Grade 2; Vol 4: Grade 2 vs Pre-1).
  - Enable readers to perceive the contrast between "known baseline patterns" and "polished target expressions".
  - Encourage memorization/recitation of high-impact collocations, idioms, and morals for Eiken Writing & Speaking exams.
  - Accompanied by mature, aesthetic illustrations (generated via NanaBanana2 / AI image generation).

---

## 2. Technical & KDP Publishing Guidelines (Error-Free Requirements)

To ensure zero conversion errors on Amazon KDP and 100% support for **Enhanced Typesetting (KFX)** and **音声読み上げ機能 (TTS)**:

1. **No Prompt Specification in Manuscript**:
   - Do NOT include technical prompt text (`Visual Illustration Spec & Prompt`) inside the reader manuscript files.
   - Each chapter starts directly with the Chapter Title and Illustration Image.

2. **No Manual Page Breaks**:
   - Do NOT insert explicit HTML page break tags (`<div style="page-break-before: always;"></div>`) inside markdown content. Allow 電子書籍 reflowable rendering engine to layout pages naturally.

3. **Responsive Comparison Cards (No Wide Tables)**:
   - Wide 4-column `<table>` elements trigger Enhanced Typesetting validation errors on Amazon KDP.
   - All phrase comparison sections MUST be formatted as **Responsive Comparison Cards** (`<div class="comparison-card">`) to guarantee 100% compliance across smartphones and 電子書籍 devices.

4. **Cover Image Specification**:
   - Format: JPEG (`.jpg` extension only, 24-bit sRGB).
   - Dimensions: **1,600 x 2,560 pixels** (Aspect Ratio 1 : 1.6).
   - Layout: **Aspect Fit (0% cropped)** on deep dark navy background (`#0D1B2A`).

5. **Accessibility & Alt Text**:
   - All `<img>` elements MUST contain descriptive `alt="..."` attributes (e.g. `alt="The Tortoise and the Hare Illustration"`).

6. **TTS (Text-to-Speech) Compliance**:
   - Keep English story sections purely in English without interleaved Japanese phrases to prevent TTS pronunciation garbling.
   - Place Japanese translations and explanations in the second half of the chapter.

---

## 3. Standard Chapter Manuscript Template

Every chapter follows this clean 6-stage structure:

```markdown
# Chapter [N]: [Story Title in English] ([Japanese Title])

<div style="text-align: center; margin-bottom: 20px;">
  <img src="images/[story_image].png" alt="[Story Title] Illustration" style="max-width: 100%; height: auto;" />
</div>

## 1. Benchmark Level: Eiken Grade [Lower Level]
*Read in ~1 to 1.5 minutes. Baseline vocabulary and syntax.*

[Pure English story adhering strictly to Grade [Lower] limits]

## 2. Target Level: Eiken Grade [Higher Level]
*Read in ~2 to 3 minutes. Upgraded vocabulary, sophisticated sentence structures, and idioms.*

[Pure English story rewriting the narrative with Grade [Higher] syntax, relative clauses, participles, and thematic vocabulary]

## 3. Classic Original English Text (イソップ寓話 クラシック原文)
*Townsend / Jacobs Edition (Public Domain)*

[Historical public domain English text]

## 4. Japanese Translation (日本語訳)

[Japanese translation of the fable and moral]

## 5. Recite & Compare (そらんじたいキーフレーズ対比)
*Memorize these contrastive expressions to elevate speaking, writing, and reading fluency.*

<div class="comparison-card">
  <div class="card-header">■ 場面：[Scene Title]</div>
  <div class="card-row-g4">【Grade [Lower] 基礎】 <em>[Baseline Phrase]</em></div>
  <div class="card-row-g3">【Grade [Higher] 暗唱】 <strong><em>[Target Phrase]</em></strong></div>
  <div class="card-note">【ポイント】 <strong>解説・試験活用</strong>：[Explanation of nuance and Eiken writing/speaking utility]</div>
</div>

## 6. Key Vocabulary & Exam Notes (語彙・文法・試験対策解説)
- **[Word/Idiom 1]**: [Part of speech] [Meaning] (Exam relevance / collocation)
- **[Word/Idiom 2]**: [Part of speech] [Meaning] (Exam relevance / collocation)
```

---

## 4. Linguistic Specifications per Eiken Grade

| Eiken Level | Word Count Target | Key Grammar Constraints | Key Lexical & Exam Focus |
|---|---|---|---|
| **Grade 4 (4級)** | 120–180 words | Past tense, progressive, can/must/may, comparative/superlative, simple gerunds/infinitives. | Daily conversational collocations, basic time/reason conjunctions (*when*, *because*). |
| **Grade 3 (3級)** | 180–240 words | Present perfect, relative pronouns (who/which/that), basic passive voice, subordinate clauses (*as soon as*, *so that*). | Informative email structures, transitions (*however*, *finally*, *in the end*). |
| **Pre-2 (準2級)** | 260–340 words | Subjunctive past, participial constructions, relative adverbs (*where*, *why*), modal + have + p.p., cause-and-effect transitions (*therefore*, *in order to*, *as a result*). | Societal, environmental, and behavioral discourse vocabulary; structured argumentative phrasing for essay writing. |
| **Grade 2 (2級)** | 350–430 words | Complex inversions, inanimate subjects, cleft sentences, nominalization. | Formal essay structures, academic collocations, sophisticated discourse markers. |
| **Pre-1 (準1級)** | 450–550 words | High nominal density, advanced adverbial modifiers, elevated idiomatic nuance. | Philosophical interpretation of human nature, cognitive bias, ethical reasoning. |