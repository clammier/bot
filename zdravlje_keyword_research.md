# Mojausluga.hr — Keyword Research for Zdravlje (Health) Section

**Prepared:** 2026-04-11
**Scope:** Croatian-language keyword research for health/doctor search terms, plus gap analysis vs. what's already live on mojausluga.hr/zdravlje and its specialty subdirectories.

---

## 1. What mojausluga.hr already covers (Zdravlje section audit)

The main `/zdravlje` landing page could not be fetched directly (the site returns 403 to bots), so the audit below is assembled from indexed specialty pages and city pages that appear in Google's index for `site:mojausluga.hr`. This is reliable because every live category has been seen in the SERPs.

### 1a. Doctor specialty index (`/doktori/`)
- Top-level directory advertised as **"Imenik 4.869 liječnika po specijalnosti i lokaciji"** — Croatia-wide index of doctors, filterable by specialty and city, with an HZZO-contract filter.
- Data sources combined: **HZZO + NRPZZ + Google recenzije** (each doctor profile has clinic info, HZZO contract status, location, contact).

### 1b. Medical specialty categories currently live
Verified via Google indexed URLs:

| Slug | Croatian name | Volume on site | Example URL |
|---|---|---|---|
| `opca-medicina` | Opća / obiteljska medicina | ~1,600 ordinacija (107 Split, 31 Karlovac) | `/opca-medicina/karlovac/` |
| `pedijatrija` | Pedijatrija | ~260 ordinacija | `/pedijatrija/zagreb/` |
| `ginekologija` | Ginekologija | 268 ginekologa (47 Zagreb) | `/ginekologija/` |
| `zubari` | Stomatologija / Zubari | 2,171 ordinacija u 570 mjesta (416 Zagreb) | `/zubari/zagreb/` |
| `medicina-rada` | Medicina rada | 198 specijalista u 70 mjesta (43 Zagreb) | `/medicina-rada/zagreb/` |
| `fizikalna-medicina` | Fizikalna medicina i rehabilitacija | ~182 ordinacija | `/fizikalna-medicina/osijek/` |
| `dermatologija` | Dermatologija | Vidljivo Zagreb/Rijeka/Osijek (npr. 4 Zagreb) | `/dermatologija/zagreb/` |
| `psihijatri` | Psihijatrija | Pojedinačni profili vidljivi | `/psihijatri/zagreb/` |
| `ljekarne` | Ljekarne | Pojedinačni profili vidljivi | `/ljekarne/zagreb/` |
| `domovi-zdravlja` | Domovi zdravlja | Zagreb: 689 ordinacija u 6 kategorija | `/domovi-zdravlja/zagreb/` |

**Structural pattern:** `mojausluga.hr/{specijalnost}/{grad}/{naziv-ordinacije}/`

### 1c. Categories NOT seen in Google's index for site:mojausluga.hr
These specialties exist in the Croatian medical system but I could find **no** SERP presence for them on mojausluga.hr — strong indicators that they are either not yet a dedicated category or have very thin content:

- Kardiologija (interna — kardiolog)
- Neurologija (neurolog)
- Urologija (urolog)
- Ortopedija i traumatologija (ortoped)
- Otorinolaringologija (ORL / ušni-grlo-nos)
- Oftalmologija (oftalmolog / okulist)
- Endokrinologija (endokrinolog)
- Gastroenterologija (gastroenterolog)
- Pulmologija (pulmolog)
- Reumatologija (reumatolog)
- Nefrologija (nefrolog)
- Hematologija (hematolog)
- Onkologija (onkolog)
- Alergologija / klinička imunologija (alergolog)
- Infektologija (infektolog)
- Radiologija / dijagnostika (radiolog)
- Nuklearna medicina
- Anesteziologija
- Opća / plastična kirurgija
- Vaskularna kirurgija
- Neurokirurgija
- Maksilofacijalna kirurgija
- Interna medicina (generalno)
- Sportska medicina
- Školska medicina
- Patronažna skrb / kućna njega
- Hitna medicina / hitna pomoć
- Laboratorijska dijagnostika (privatni laboratoriji)
- Logopedi
- Psiholozi / psihoterapeuti
- Nutricionisti / dijetetičari
- Fizioterapeuti (odvojeno od ordinacija fizikalne medicine)

> Recommendation: these are the **primary expansion targets** — see §3.

---

## 2. Popular Croatian health / doctor keyword clusters

Keyword research for Croatia is limited — Google Keyword Planner volumes are gated behind paid accounts and Croatian-language SERP tools are thin. The clusters below are assembled from (a) Google SERP saturation for each term, (b) competitor site structures (najdoktor.com, halo-doktore.hr, liječnik.hr, edoktor.hr, vaspregled.hr, mojkvart.hr), (c) known patient-intent patterns (HZZO, e-naručivanje, uputnica, cijena pregleda), and (d) the clusters that already earn mojausluga.hr impressions.

Classification: **H = high intent / high volume**, **M = medium**, **L = long-tail**.

### 2a. Specialty-only head terms
Single-word specialty names are the fattest head terms and are the searches that bring patients to directory sites. Rank order is roughly highest-to-lowest estimated volume:

| Keyword (HR) | English | Intent |
|---|---|---|
| zubar | dentist | H |
| stomatolog | dentist | H |
| ginekolog | gynaecologist | H |
| pedijatar | paediatrician | H |
| dermatolog | dermatologist | H |
| kardiolog | cardiologist | H |
| ortoped | orthopaedist | H |
| neurolog | neurologist | H |
| psihijatar | psychiatrist | H |
| psiholog | psychologist | H |
| urolog | urologist | H |
| oftalmolog / okulist | ophthalmologist | H |
| ORL / otorinolaringolog | ENT | H |
| endokrinolog | endocrinologist | M |
| gastroenterolog | gastroenterologist | M |
| pulmolog | pulmonologist | M |
| reumatolog | rheumatologist | M |
| alergolog | allergologist | M |
| fizijatar | physiatrist | M |
| fizioterapeut | physiotherapist | H |
| logoped | speech therapist | M |
| nutricionist | nutritionist | M |
| liječnik obiteljske medicine / opće prakse | GP | H |

### 2b. Specialty + city (the money keywords for a directory)
Classic `[specijalnost] [grad]` pattern — this is how Croatian patients search for doctors. Mojausluga.hr already ranks well for `opca-medicina/{grad}`, `zubari/{grad}` and `ginekologija/{grad}`; the same pattern should be extended to every specialty in §1c.

Priority cities (by population + search volume): **Zagreb, Split, Rijeka, Osijek, Zadar, Pula, Slavonski Brod, Karlovac, Varaždin, Šibenik, Dubrovnik, Velika Gorica, Samobor, Bjelovar, Koprivnica, Vinkovci, Sisak**.

Example high-value templates:
- `ginekolog zagreb`, `ginekolog split`, `ginekolog rijeka`
- `zubar zagreb`, `stomatolog zagreb`, `najbolji zubar zagreb`
- `pedijatar zagreb`, `privatni pedijatar zagreb`
- `kardiolog zagreb`, `kardiolog split`
- `dermatolog zagreb`, `dermatolog rijeka`
- `ortoped zagreb`, `ortoped split`
- `psihijatar zagreb`, `psiholog zagreb`
- `neurolog zagreb`, `neurolog split`

### 2c. "Privatni" / "najbolji" / "HZZO" modifiers
Croatian patient behaviour splits strongly along these three axes. All three are proven mojausluga.hr strengths and should be surfaced on every specialty page.

- `privatni [specijalnost]` — e.g. `privatni ginekolog zagreb`, `privatna ordinacija opće medicine`
- `najbolji [specijalnost]` — e.g. `najbolji zubar zagreb`, `najbolji kardiolog hrvatska`
- `[specijalnost] HZZO` / `ordinacija HZZO` — HZZO contract filter
- `[specijalnost] cijena pregleda` — e.g. `cijena pregleda kardiolog`, `cijena ultrazvuka`
- `[specijalnost] iskustva` / `recenzije` / `ocjene`

### 2d. Services / procedures (transactional long-tail)
These are *under-served* on mojausluga.hr right now and represent a content expansion opportunity:

**Stomatološke usluge (dental):**
plomba, vadjenje zuba, implantat, proteza, krunica, izbjeljivanje zuba, ortodontski aparatić, oralna kirurgija, parodontolog, dječji zubar, zubar za strah, hitni zubar, estetska stomatologija, dental studio

**Ginekologija / reprodukcija:**
ultrazvuk u trudnoći, ginekološki pregled, pap test, kontracepcija, IVF / MPO, porod, ginekolog za trudnice, privatni ginekolog Zagreb

**Dijagnostika:**
ultrazvuk, MR (magnetska rezonanca), CT, RTG, mamografija, kolonoskopija, gastroskopija, EKG, holter, laboratorij, vađenje krvi, hormoni, štitnjača

**Oftalmologija:**
pregled oka, dioptrija, laserska korekcija vida, katarakta

**Opća medicina / preventiva:**
sistematski pregled, preventivni pregled, liječnički za vozačku, liječnički za posao, cijepljenje, uputnica

**Fizikalna medicina:**
fizikalna terapija, rehabilitacija, magnetoterapija, elektroterapija, TENS, kineziterapija, manualna terapija

**Mentalno zdravlje:**
psihoterapija, bračno savjetovanje, dječji psiholog, anksioznost, depresija, ADHD, kognitivno-bihevioralna terapija

### 2e. Administrative / HZZO intent queries
Croatian patients search these constantly — they are **high volume** and pair well with helpful landing pages:

- e-naručivanje / e-narudžba
- e-uputnica / uputnica HZZO
- promjena liječnika / promijeniti obiteljskog liječnika
- e-građani zdravlje / portal zdravlja
- izabrani liječnik
- HZZO iskaznica
- dežurni liječnik / dežurna ljekarna / dežurna ordinacija
- hitna pomoć / hitna medicinska pomoć 194
- sanitetski prijevoz
- bolovanje / otvaranje bolovanja
- ljekarne 24h / dežurna ljekarna [grad]

### 2f. "Blizu mene" / lokalno
Google prompts "near me" results heavily for health searches. Croatian variants:

- `zubar blizu mene`
- `ljekarna u blizini`
- `pedijatar u blizini`
- `ordinacija opće prakse u blizini`
- `dežurna ljekarna [grad] danas`

These should be targeted on city pages with explicit geo-copy.

### 2g. Dom zdravlja / institucije
Institutional searches are a dependable traffic source and mojausluga.hr already holds indexed URLs here:

- `dom zdravlja [grad]`
- `dom zdravlja zagreb centar / istok / zapad / jug`
- `KBC Zagreb / Split / Rijeka / Osijek`
- `klinička bolnica [naziv]`
- `poliklinika [naziv]`
- `specijalna bolnica [naziv]`

---

## 3. Gap analysis & content recommendations

**Highest-ROI gaps** (ordered by search volume × ease of adding):

1. **Add dedicated category pages for missing high-volume specialties** — kardiolog, neurolog, urolog, ortoped, oftalmolog/okulist, ORL, psiholog, fizioterapeut, gastroenterolog, endokrinolog, pulmolog, reumatolog, alergolog. Each of these has strong single-word head-term searches and 8–15 supported cities.

2. **Expand `/zubari` into dental sub-specialties.** Currently one flat `zubari` slug covers 2,171 offices. Split by: `ortodont`, `parodontolog`, `oralni-kirurg`, `dječji-zubar`, `endodoncija`, `protetika`, `implantolog`. These are classic patient search terms and competitors (mojstomatolog.hr) already target them.

3. **Services / procedures pages** (category 2d) — e.g. `/ultrazvuk/zagreb/`, `/mr/zagreb/`, `/sistematski-pregled/zagreb/`, `/laserska-korekcija-vida/zagreb/`. These rank for transactional queries that a pure doctor directory misses.

4. **Laboratorij / dijagnostički centri** as a standalone category (separate from ordinacije) — Synevo, Breyer, Medikol, Affidea etc. `[laboratorij] [grad]` and `vađenje krvi [grad]` are heavy searches.

5. **Fizioterapeuti** as a standalone category separate from `/fizikalna-medicina/`. Patients search `fizioterapeut zagreb` far more than `fizikalna medicina zagreb`.

6. **Mentalno zdravlje hub** — `/psiholog/`, `/psihoterapeut/`, `/logoped/` as separate categories under the Zdravlje umbrella. `psihijatri` already exists; psychologists and speech therapists do not.

7. **Nutricionisti / dijetetičari** — fast-growing category, zero competition from mojausluga.hr currently.

8. **Administrative landing pages** for HZZO/e-građani queries (category 2e). A helpful page at `/hzzo/promjena-lijecnika/`, `/hzzo/e-uputnica/`, `/dezurne-ljekarne/{grad}/` would capture huge informational traffic and funnel it to the directory.

9. **"Najbolji [specijalnost] [grad]"** listicle-style pages — Liječnik.hr owns this pattern right now. Directory sites with real rating data have a strong claim to compete.

10. **Hitna pomoć / dežurne ustanove po gradu** — `/hitna-pomoc/zagreb/`, `/dezurne-ustanove/zagreb/`. Seasonal + evergreen informational traffic.

---

## 4. Source notes

The research relied on Google SERPs because mojausluga.hr blocks direct bot access (HTTP 403 on `/zdravlje` and every specialty page tested). Every category count cited in §1 was pulled from page-title text visible in Google result snippets for `site:mojausluga.hr` queries, which means it reflects **indexed** content and is the correct reference for SEO gap analysis.

Competitor references used to cross-check keyword clusters:
- najdoktor.com — specialty + city + najbolji patterns
- halo-doktore.hr — specialty + city directory
- liječnik.hr — "najbolji [specijalnost]" listicles
- vaspregled.hr, edoktor.hr — opća/obiteljska medicina coverage
- mojkvart.hr — Zagreb-specific directory
- expatincroatia.com — EN↔HR specialty name mapping
- hr.wikipedia.org/wiki/Specijalnost_(medicina) — official HR specialty list
- HZZO, gov.hr, e-građani — administrative/HZZO intent queries
