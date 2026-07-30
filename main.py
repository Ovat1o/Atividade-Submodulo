import sys
import time

# Aponta para a pasta do submódulo baixado
sys.path.append('./texto-magico') 

# Importando as funções da biblioteca do colega
from operacoes import inverter_texto, gritar_texto

def iniciar_sistema():
    print("==================================================")
    print("   Gerenciador de Tarefas Caóticas (GTC)          ")
    print("==================================================")
    
    tarefa = input("Digite a tarefa que você está procrastinando: ")
    
    print("\nCalculando o nível de desespero...")
    time.sleep(1)
    
    # Consumindo a função gritar_texto
    tarefa_urgente = gritar_texto(f"pare de enrolar e vá fazer agora: {tarefa}")
    print(f"[URGÊNCIA MÁXIMA] {tarefa_urgente}")
    
    # Consumindo a função inverter_texto
    # Útil para esconder a tarefa de quem estiver olhando para a sua tela
    tarefa_oculta = inverter_texto(tarefa)
    print(f"[MODO PRIVACIDADE] Tarefa criptografada com sucesso: {tarefa_oculta}")
    
    print("\nBoa sorte. Você vai precisar!")

if __name__ == "__main__":
    iniciar_sistema()