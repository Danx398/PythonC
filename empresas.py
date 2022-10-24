#!/usr/bin/python3

def _main() -> None:
    empresas_meses = {
        "ENERO": 0,
        "FEBRERO": 0,
        "MARZO": 0,
        "ABRIL": 0,
        "MAYO": 0,
        "JUNIO": 0,
        "JULIO": 0,
        "AGOSTO": 0,
        "SEPTIEMBRE": 0,
        "OCTUBRE": 0,
        "NOVIEMBRE": 0,
        "DICIEMBRE": 0,
    }

    for i in range(15):
        empresa = input()
        if empresa[5:7] == "01":
            empresas_meses["ENERO"] += 1
        if empresa[5:7] == "02":
            empresas_meses["FEBRERO"] += 1
        if empresa[5:7] == "03":
            empresas_meses["MARZO"] += 1
        if empresa[5:7] == "04":
            empresas_meses["ABRIL"] += 1
        if empresa[5:7] == "05":
            empresas_meses["MAYO"] += 1
        if empresa[5:7] == "06":
            empresas_meses["JUNIO"] += 1
        if empresa[5:7] == "07":
            empresas_meses["JULIO"] += 1
        if empresa[5:7] == "08":
            empresas_meses["AGOSTO"] += 1
        if empresa[5:7] == "09":
            empresas_meses["SEPTIEMBRE"] += 1
        if empresa[5:7] == "10":
            empresas_meses["OCTUBRE"] += 1
        if empresa[5:7] == "11":
            empresas_meses["NOVIEMBRE"] += 1
        if empresa[5:7] == "12":
            empresas_meses["DICIEMBRE"] += 1

    for i in range(len(empresas_meses)):
        print(list(empresas_meses.keys())[i], list(empresas_meses.values())[i])
    pass
_main()
