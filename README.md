# Projeto de Estatística — Team 07

Análise dos registos de incêndios rurais do SGIF (ICNF) para os concelhos de
**Braga, Guimarães, Guarda e Faro**, entre 2001 e 2025, com foco na causa dos
incêndios (negligente vs. intencional) antes e depois de 2017.

## Conteúdo

| Ficheiro | Descrição |
|---|---|
| `verificar_dados.py` | Verificação rápida dos dados: ocorrências por ano, tipos de causa, valores em falta, tempos de intervenção e tabela para o teste |
| `41-Codificacao-causas.pdf` | Documento do ICNF com a codificação das causas |
| `dados/` | Registos do SGIF 2001–2025 em CSV (incluídos no repositório) |

## Dados

Os registos de incêndios do SGIF (ICNF), em CSV, estão na pasta `dados/`:

    dados/
    ├── Registos_Incendios_SGIF_2001_2010.csv
    ├── Registos_Incendios_SGIF_2011_2020.csv
    └── Registos_Incendios_SGIF_2021_2025.csv

Fonte: ICNF – Registos individuais de incêndios 2001 a 2025 (Partes 1, 2 e 3).

## Como correr

```bash
pip install pandas openpyxl
python verificar_dados.py
```


## Steps of Statistical Investigation

- [x] Research Question
- [ ] Collect Data
- [ ] Explore Data (Project, Plot)
- [ ] Draw Inferences
- [ ] Formulate Conclusions
- [ ] Look Back and Aheads


## Main Research Question

Did the distribution of human-caused fire ignitions (negligence versus intentional actions) and the annual number of fire ignitions change significantly before and after the 2017 wildfire crisis across four Portuguese municipalities with distinct demographic pressures: **Braga**, **Guimarães**, **Guarda**, and **Faro**?

---

## Specific Research Questions

### 1. Proportion Test

**Objective:** Evaluate whether the composition of human-caused fires changed over time.

**Research Question:**

> Did the proportion of intentional fires among human-caused fire ignitions change significantly between the pre-2017 and post-2017 periods in Braga, Guimarães, Guarda, and Faro?

---

### 2. Independent Samples t-Test

**Objective:** Compare fire ignition activity before and after the 2017 wildfire crisis.

**Research Question:**

> Did the mean annual number of fire ignitions differ significantly between the pre-2017 and post-2017 periods in Braga, Guimarães, Guarda, and Faro?

---

### 3. One-Way ANOVA

**Objective:** Compare average fire ignition activity across municipalities.

**Research Question:**

> Did the mean annual number of fire ignitions differ significantly among Braga, Guimarães, Guarda, and Faro over the study period?