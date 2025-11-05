
import yaml

# === LER CONFIGURAÇÃO DO YAML ===
try:
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("⚠️ Arquivo 'config.yaml' não encontrado. Usando configurações padrão.")
    config = {
        "mensagens": {
            "matriz_simetrica": "✅ A matriz é simétrica!",
            "matriz_nao_simetrica": "❌ A matriz não é simétrica!"
        },
        "config": {
            "centralizar_saida": True,
            "mostrar_matriz": True
        }
    }

# === INFORMAÇÕES DO PROJETO ===
print("\n" + "=" * 100)
print(f"Projeto: {config.get('projeto', 'Desconhecido')}")
print(f"Autor: {config.get('autor', 'Anônimo')}")
print("=" * 100 + "\n")

# === PROGRAMA PRINCIPAL ===
nfilas = int(input("Digite o número de filas: "))
ncol = int(input("Digite o número de colunas: "))
matriz = []
v = True

for i in range(nfilas):
    fila = []
    for j in range(ncol):
        col = int(input(f"Digite o elemento [{i}][{j}]: "))
        fila.append(col)
    matriz.append(fila)

print("\n")
if config["config"]["mostrar_matriz"]:
    print("Imprimindo a matriz:".center(100))
    print("")
    for i in range(nfilas):
        if config["config"]["centralizar_saida"]:
            print(" " * ((100 - (ncol * 2 + 2)) // 2), end="")
        print("|", end=" ")
        for j in range(ncol):
            print(matriz[i][j], end=" ")
        print("|")

# === VERIFICAÇÃO DE SIMETRIA ===
if nfilas == ncol:
    for i in range(nfilas):
        for j in range(ncol):
            if matriz[i][j] != matriz[j][i]:
                v = False
                break
        if not v:
            break
else:
    v = False

print("\n")
if v:
    print(config["mensagens"]["matriz_simetrica"].center(100))
else:
    print(config["mensagens"]["matriz_nao_simetrica"].center(100))
