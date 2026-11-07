# Projeto de Estatística — Team 07

Análise dos registos de incêndios rurais do SGIF (ICNF) para os concelhos de
**Braga, Guimarães, Guarda e Faro**, entre 2011 e 2025, com foco na causa dos
incêndios (negligente vs. intencional) antes e depois de 2017.

## Conteúdo

| Ficheiro | Descrição |
|---|---|
| `verificar_dados.py` | Verificação rápida dos dados: ocorrências por ano, tipos de causa, valores em falta, tempos de intervenção e tabela para o teste |
| `41-Codificacao-causas.pdf` | Documento do ICNF com a codificação das causas |
| `dados/` | Dados do SGIF (**não incluídos no repositório**, ver abaixo) |

## Dados

Os ficheiros de dados são grandes e por isso não estão no repositório.
Para correr o script:

1. Descarregar do site do ICNF os registos de incêndios do SGIF
   (Parte 2: 2011–2020 e Parte 3: 2021–2025).
2. Criar uma pasta `dados/` na raiz do projeto e descompactar lá os ficheiros:
   ```
   dados/
   ├── Registos_Incendios_SGIF_2011_2020.xlsx
   └── Registos_Incendios_SGIF_2021_2025.xlsx
   ```

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