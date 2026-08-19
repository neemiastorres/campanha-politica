from fastapi import FastAPI

app = FastAPI(
    title="LegisData API",
    description="Backend de Inteligência Eleitoral para Deputados Federais e Estaduais",
    version="1.0.0"
)

@app.get("/")
def status_sistema():
    return {
        "status": "Online",
        "sistema": "LegisData",
        "mensagem": "Servidor rodando e pronto para receber dados eleitorais."
    }

@app.get("/quociente-simulacao")
def calcular_quociente(votos_validos: int, vagas_disponiveis: int):
    """
    Simula o Quociente Eleitoral (QE) básico do estado.
    """
    if vagas_disponiveis <= 0:
        return {"erro": "Número de vagas deve ser maior que zero."}
    
    quociente = votos_validos // vagas_disponiveis
    corte_minimo_candidato = int(quociente * 0.10) # Regra dos 10% do QE
    
    return {
        "votos_validos_estado": votos_validos,
        "vagas_disponiveis": vagas_disponiveis,
        "quociente_eleitoral": quociente,
        "corte_individual_10_percent": corte_minimo_candidato
    }
