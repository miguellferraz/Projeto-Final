import math

class Calculadora:
    def __init__(self):
        self.historico = []
    
    def adicionar_historico(self, operacao, resultado):
        self.historico.append(f"{operacao} = {resultado}")
    
    def calcular(self, operacao):
        try:
            contexto = {func: getattr(math, func) for func in dir(math) if not func.startswith("__")}
            resultado = eval(operacao, {"__builtins__": None}, contexto)
            self.adicionar_historico(operacao, resultado)
            return resultado
        except Exception as e:
            return f"Erro: {e}"
    
    def mostrar_historico(self):
        return "\n".join(self.historico) if self.historico else "Sem histórico ainda."
    
    def salvar_historico(self, arquivo="historico_calculos.txt"):
        with open(arquivo, "w") as file:
            file.write(self.mostrar_historico())

def main():
    print("Bem-vindo à Calculadora Avançada!")
    print("Suporta operações básicas (+, -, *, /) e funções matemáticas como:")
    print("math.sqrt(x), math.sin(x), math.cos(x), math.log(x), etc.")
    
    calculadora = Calculadora()
    
    while True:
        print("\nOpções:")
        print("1. Fazer um cálculo")
        print("2. Mostrar histórico")
        print("3. Salvar histórico em arquivo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            operacao = input("Digite a operação (ex: 2 ** 3 ou math.sqrt(16)): ")
            resultado = calculadora.calcular(operacao)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            print("\nHistórico de cálculos:")
            print(calculadora.mostrar_historico())
        elif opcao == "3":
            calculadora.salvar_historico()
            print("Histórico salvo em 'historico_calculos.txt'.")
        elif opcao == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
