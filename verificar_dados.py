# Verificação rápida dos dados SGIF para a research question do Team 07
#
# Como usar:
#   1. Criar uma pasta chamada "dados" ao lado deste script
#   2. Descompactar lá dentro os zips do ICNF (Parte 2: 2011-2020 e Parte 3: 2021-2025)
#   3. Correr:  python verificar_dados.py

import glob
import os
import pandas as pd

PASTA = "dados"
CONCELHOS = ["BRAGA", "GUIMARAES", "GUARDA", "FARO"]

# ---- Ler todos os ficheiros da pasta (procura também em subpastas) ----
ficheiros = sorted(
    f for ext in ("xlsx", "xls", "csv")
    for f in glob.glob(os.path.join(PASTA, "**", f"*.{ext}"), recursive=True)
)
if not ficheiros:
    raise SystemExit(f"Nenhum ficheiro encontrado na pasta '{PASTA}'. Descompactem lá os zips do ICNF.")

partes = []
for f in ficheiros:
    print("A ler:", f)
    if f.lower().endswith(".csv"):
        t = pd.read_csv(f, sep=None, engine="python", encoding="latin-1")
    else:
        t = pd.read_excel(f)
    t.columns = t.columns.astype(str).str.upper().str.strip()
    partes.append(t)

df = pd.concat(partes, ignore_index=True)
print(f"\nTotal de registos: {len(df)}\n")
print("Colunas:", list(df.columns), "\n")

# ---- Normalizar nomes de concelho (acentos/maiúsculas variam entre anos) ----
df["CONC_N"] = (df["CONCELHO"].astype(str).str.upper().str.strip()
                .str.normalize("NFKD").str.encode("ascii", "ignore").str.decode("ascii"))
print("Grafias encontradas:",
      df.loc[df["CONC_N"].str.contains("BRAGA|GUIMAR|GUARDA|FARO"), "CONCELHO"].unique(), "\n")

d = df[df["CONC_N"].isin(CONCELHOS)].copy()

# Ano: a partir da data de alerta; se não existir, usa a coluna ANO
if "DATAALERTA" in d.columns:
    d["ANO_N"] = pd.to_datetime(d["DATAALERTA"], errors="coerce", dayfirst=True).dt.year
else:
    d["ANO_N"] = d["ANO"]

# ---- 1) Nº de ocorrências por concelho e ano ----
print("1) Ocorrências por ano e concelho")
print(pd.crosstab(d["ANO_N"], d["CONC_N"]), "\n")

# ---- 2) Tipo de causa, incluindo vazios (vazio = não investigado) ----
causa = d["TIPOCAUSA"].astype(str).str.strip().replace({"": None, "nan": None, "None": None})
d["SEM_CAUSA"] = causa.isna()
d["TIPOCAUSA_N"] = causa.fillna("SEM INFO (vazio)")
print("2) Tipo de causa por concelho")
print(pd.crosstab(d["TIPOCAUSA_N"], d["CONC_N"]), "\n")

# ---- 3) % sem causa por ano (verificar se muda antes/depois de 2017) ----
print("3) % de registos sem causa, por ano e concelho")
print((pd.crosstab(d["ANO_N"], d["CONC_N"],
                   values=d["SEM_CAUSA"], aggfunc="mean") * 100).round(1), "\n")

# ---- 4) Missing nas variáveis quantitativas ----
cols = ["AREATOTAL_HA", "DATAHORAALERTA", "DATAHORA_PRIMEIRAINTERVENCAO",
        "DATAHORA_EXTINCAO", "DURACAO_HORAS"]
cols = [c for c in cols if c in d.columns]
print("4) % missing por ano (variáveis quantitativas)")
print((d.groupby("ANO_N")[cols].apply(lambda x: x.isna().mean()) * 100).round(1), "\n")

# ---- 5) Tempo até 1.ª intervenção (minutos): valores estranhos ----
alerta = pd.to_datetime(d["DATAHORAALERTA"], errors="coerce", dayfirst=True)
interv = pd.to_datetime(d["DATAHORA_PRIMEIRAINTERVENCAO"], errors="coerce", dayfirst=True)
d["T_INTERV_MIN"] = (interv - alerta).dt.total_seconds() / 60
print("5) Tempo até 1.ª intervenção (min) por concelho")
print(d.groupby("CONC_N")["T_INTERV_MIN"].describe().round(1))
print("   Negativos:", int((d["T_INTERV_MIN"] < 0).sum()),
      "| Acima de 24h:", int((d["T_INTERV_MIN"] > 1440).sum()), "\n")

# ---- 6) Tabela para o teste: negligente vs intencional, por período ----
d["PERIODO"] = pd.cut(d["ANO_N"], bins=[2010, 2016, 2017, 2025],
                      labels=["2011-2016", "2017", "2018-2025"])
h = d[d["TIPOCAUSA_N"].str.lower().isin(["negligente", "intencional"])
      & (d["PERIODO"] != "2017")]
print("6) Negligente vs Intencional por período (2017 excluído)")
print(pd.crosstab([h["CONC_N"], h["PERIODO"]], h["TIPOCAUSA_N"]))